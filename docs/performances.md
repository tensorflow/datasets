# Performance tips

This document provides TensorFlow Datasets (TFDS)-specific performance tips.
Note that TFDS provides datasets as `tf.data.Dataset` objects, so the advice
from the
[`tf.data` guide](https://www.tensorflow.org/guide/data_performance#optimize_performance)
still applies.

## Benchmark datasets

Use `tfds.benchmark(ds)` to benchmark any `tf.data.Dataset` object.

Make sure to indicate the `batch_size=` to normalize the results (e.g. 100
iter/sec -> 3200 ex/sec). This works with any iterable (e.g.
`tfds.benchmark(tfds.as_numpy(ds))`).

```python
ds = tfds.load('mnist', split='train').batch(32).prefetch()
# Display some benchmark statistics
tfds.benchmark(ds, batch_size=32)
# Second iteration is much faster, due to auto-caching
tfds.benchmark(ds, batch_size=32)
```

## Small datasets (less than 1 GB)

All TFDS datasets store the data on disk in the
[`TFRecord`](https://www.tensorflow.org/tutorials/load_data/tfrecord) format.
For small datasets (e.g. MNIST, CIFAR-10/-100), reading from `.tfrecord` can add
significant overhead.

As those datasets fit in memory, it is possible to significantly improve the
performance by caching or pre-loading the dataset. Note that TFDS automatically
caches small datasets (the following section has the details).

### Caching the dataset

Here is an example of a data pipeline which explicitly caches the dataset after
normalizing the images.

```python
def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label


ds, ds_info = tfds.load(
    'mnist',
    split='train',
    as_supervised=True,  # returns `(img, label)` instead of dict(image=, ...)
    with_info=True,
)
# Applying normalization before `ds.cache()` to re-use it.
# Note: Random transformations (e.g. images augmentations) should be applied
# after both `ds.cache()` (to avoid caching randomness) and `ds.batch()` (for
# vectorization [1]).
ds = ds.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds = ds.cache()
# For true randomness, we set the shuffle buffer to the full dataset size.
ds = ds.shuffle(ds_info.splits['train'].num_examples)
# Batch after shuffling to get unique batches at each epoch.
ds = ds.batch(128)
ds = ds.prefetch(tf.data.experimental.AUTOTUNE)
```

*   [[1] Vectorizing mapping](https://www.tensorflow.org/guide/data_performance#vectorizing_mapping)

When iterating over this dataset, the second iteration will be much faster than
the first one thanks to the caching.

### Auto-caching

By default, TFDS auto-caches (with `ds.cache()`) datasets which satisfy the
following constraints:

*   Total dataset size (all splits) is defined and < 250 MiB
*   `shuffle_files` is disabled, or only a single shard is read

It is possible to opt out of auto-caching by passing `try_autocaching=False` to
`tfds.ReadConfig` in `tfds.load`. Have a look at the dataset catalog
documentation to see if a specific dataset will use auto-cache.

### Loading the full data as a single Tensor

If your dataset fits into memory, you can also load the full dataset as a single
Tensor or NumPy array. It is possible to do so by setting `batch_size=-1` to
batch all examples in a single `tf.Tensor`. Then use `tfds.as_numpy` for the
conversion from `tf.Tensor` to `np.array`.

```python
(img_train, label_train), (img_test, label_test) = tfds.as_numpy(tfds.load(
    'mnist',
    split=['train', 'test'],
    batch_size=-1,
    as_supervised=True,
))
```

## Large datasets

Large datasets are sharded (split in multiple files) and typically do not fit
in memory, so they should not be cached.

### Shuffle and training

During training, it's important to shuffle the data well - poorly shuffled data
can result in lower training accuracy.

In addition to using `ds.shuffle` to shuffle records, you should also set
`shuffle_files=True` to get good shuffling behavior for larger datasets that are
sharded into multiple files. Otherwise, epochs will read the shards in the same
order, and so data won't be truly randomized.

```python
ds = tfds.load('imagenet2012', split='train', shuffle_files=True)
```

Additionally, when `shuffle_files=True`, TFDS disables
[`options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic),
which may give a slight performance boost. To get deterministic shuffling, it is
possible to opt-out of this feature with `tfds.ReadConfig`: either by setting
`read_config.shuffle_seed` or overwriting `read_config.options.deterministic`.

### Auto-shard your data across workers (TF)

When training on multiple workers, you can use the `input_context` argument of
`tfds.ReadConfig`, so each worker will read a subset of the data.

```python
input_context = tf.distribute.InputContext(
    input_pipeline_id=1,  # Worker id
    num_input_pipelines=4,  # Total number of workers
)
read_config = tfds.ReadConfig(
    input_context=input_context,
)
ds = tfds.load('dataset', split='train', read_config=read_config)
```

This is complementary to the subsplit API. First, the subplit API is applied:
`train[:50%]` is converted into a list of files to read. Then, a `ds.shard()` op
is applied on those files. For example, when using `train[:50%]` with
`num_input_pipelines=2`, each of the 2 workers will read 1/4 of the data.

When `shuffle_files=True`, files are shuffled within one worker, but not across
workers. Each worker will read the same subset of files between epochs.

Note: When using `tf.distribute.Strategy`, the `input_context` can be
automatically created with
[distribute_datasets_from_function](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#distribute_datasets_from_function)

### Auto-shard your data across workers (Jax)

With Jax, you can use the `tfds.split_for_jax_process` or `tfds.even_splits` API
to distribute your data across workers. See the
[split API guide](https://www.tensorflow.org/datasets/splits).

```python
split = tfds.split_for_jax_process('train', drop_remainder=True)
ds = tfds.load('my_dataset', split=split)
```

`tfds.split_for_jax_process` is a simple alias for:

```python
# The current `process_index` loads only `1 / process_count` of the data.
splits = tfds.even_splits('train', n=jax.process_count(), drop_remainder=True)
split = splits[jax.process_index()]
```

### Faster image decoding

By default, TFDS automatically decodes images. However, there are cases where it
can be more performant to skip the image decoding with
`tfds.decode.SkipDecoding` and manually apply the `tf.io.decode_image` op:

*   When filtering examples (with `tf.data.Dataset.filter`), to decode images
    after examples have been filtered.
*   When cropping images, to use the fused `tf.image.decode_and_crop_jpeg` op.

The code for both examples is available in the
[decode guide](https://www.tensorflow.org/datasets/decode#usage_examples).

### Skip unused features

If you're only using a subset of the features, it is possible to entirely skip
some features. If your dataset has many unused features, not decoding them can
significantly improve performances. See
https://www.tensorflow.org/datasets/decode#only_decode_a_sub-set_of_the_features.
