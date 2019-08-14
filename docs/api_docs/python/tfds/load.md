<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.load" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.load

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/registered.py">View
source</a>

Loads the named dataset into a `tf.data.Dataset`.

```python
tfds.load(
    name,
    split=None,
    data_dir=None,
    batch_size=None,
    in_memory=None,
    download=True,
    as_supervised=False,
    decoders=None,
    with_info=False,
    builder_kwargs=None,
    download_and_prepare_kwargs=None,
    as_dataset_kwargs=None,
    try_gcs=False
)
```

### Used in the guide:

*   [Convert Your Existing Code to TensorFlow 2.0](https://www.tensorflow.org/beta/guide/migration_guide)

### Used in the tutorials:

*   [CycleGAN](https://www.tensorflow.org/beta/tutorials/generative/cyclegan)
*   [Distributed training with Keras](https://www.tensorflow.org/beta/tutorials/distribute/keras)
*   [How-to create an Estimator from a Keras model](https://www.tensorflow.org/beta/tutorials/estimators/keras_model_to_estimator)
*   [Image segmentation](https://www.tensorflow.org/beta/tutorials/images/segmentation)
*   [Multi-worker Training with Estimator](https://www.tensorflow.org/beta/tutorials/distribute/multi_worker_with_estimator)
*   [Multi-worker Training with Keras](https://www.tensorflow.org/beta/tutorials/distribute/multi_worker_with_keras)
*   [Save and load a model using `tf.distribute.Strategy`](https://www.tensorflow.org/beta/tutorials/distribute/save_and_load)
*   [Text classification of movie reviews with Keras and TensorFlow Hub](https://www.tensorflow.org/beta/tutorials/keras/basic_text_classification_with_tfhub)
*   [Text classification with an RNN](https://www.tensorflow.org/beta/tutorials/text/text_classification_rnn)
*   [Transfer Learning Using Pretrained ConvNets](https://www.tensorflow.org/beta/tutorials/images/transfer_learning)
*   [Transformer model for language understanding](https://www.tensorflow.org/beta/tutorials/text/transformer)

If `split=None` (the default), returns all splits for the dataset. Otherwise,
returns the specified split.

`load` is a convenience method that fetches the
<a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>
by string name, optionally calls
<a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>DatasetBuilder.download_and_prepare</code></a>
(if `download=True`), and then calls
<a href="../tfds/core/DatasetBuilder.md#as_dataset"><code>DatasetBuilder.as_dataset</code></a>.
This is roughly equivalent to:

```
builder = tfds.builder(name, data_dir=data_dir, **builder_kwargs)
if download:
  builder.download_and_prepare(**download_and_prepare_kwargs)
ds = builder.as_dataset(
    split=split, as_supervised=as_supervised, **as_dataset_kwargs)
if with_info:
  return ds, builder.info
return ds
```

If you'd like NumPy arrays instead of `tf.data.Dataset`s or `tf.Tensor`s,
you can pass the return value to <a href="../tfds/as_numpy.md"><code>tfds.as_numpy</code></a>.

Callers must pass arguments as keyword arguments.

**Warning**: calling this function might potentially trigger the download
of hundreds of GiB to disk. Refer to the `download` argument.

#### Args:

*   <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake
    case version of the class name). This can be either `"dataset_name"` or
    `"dataset_name/config_name"` for datasets with `BuilderConfig`s. As a
    convenience, this string may contain comma-separated keyword arguments for
    the builder. For example `"foo_bar/a=True,b=3"` would use the `FooBar`
    dataset passing the keyword arguments `a=True` and `b=3` (for builders with
    configs, it would be `"foo_bar/zoo/a=True,b=3"` to use the `"zoo"` config
    and pass to the builder keyword arguments `a=True` and `b=3`).
*   <b>`split`</b>: <a href="../tfds/Split.md"><code>tfds.Split</code></a> or
    `str`, which split of the data to load. If None, will return a `dict` with
    all splits (typically
    <a href="../tfds/Split.md#TRAIN"><code>tfds.Split.TRAIN</code></a> and
    <a href="../tfds/Split.md#TEST"><code>tfds.Split.TEST</code></a>).
*   <b>`data_dir`</b>: `str` (optional), directory to read/write data. Defaults
    datasets are stored.
*   <b>`batch_size`</b>: `int`, if set, add a batch dimension to examples. Note
    that variable length features will be 0-padded. If `batch_size=-1`, will
    return the full dataset as `tf.Tensor`s.
*   <b>`in_memory`</b>: `bool`, if `True`, loads the dataset in memory which
    increases iteration speeds. Note that if `True` and the dataset has unknown
    dimensions, the features will be padded to the maximum size across the
    dataset.
*   <b>`download`</b>: `bool` (optional), whether to call
    <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>
    before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is expected
    to be in `data_dir`. If `True` and the data is already in `data_dir`,
    when data_dir is a Placer path.
*   <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default, the returned
    `tf.data.Dataset` will have a dictionary with all the features.
*   <b>`decoders`</b>: Nested dict of `Decoder` objects which allow to customize
    the decoding. The structure should match the feature structure, but only
    customized feature keys need to be present. See
    [the guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)
    for more info.
*   <b>`with_info`</b>: `bool`, if True, tfds.load will return the tuple
    (tf.data.Dataset, tfds.core.DatasetInfo) containing the info associated with
    the builder.
*   <b>`builder_kwargs`</b>: `dict` (optional), keyword arguments to be passed
    to the
    <a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>
    constructor. `data_dir` will be passed through by default.
*   <b>`download_and_prepare_kwargs`</b>: `dict` (optional) keyword arguments
    passed to
    <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>
    if `download=True`. Allow to control where to download and extract the
    cached data. If not set, cache_dir and manual_dir will automatically be
    deduced from data_dir.
*   <b>`as_dataset_kwargs`</b>: `dict` (optional), keyword arguments passed to
    <a href="../tfds/core/DatasetBuilder.md#as_dataset"><code>tfds.core.DatasetBuilder.as_dataset</code></a>.
    `split` will be passed through by default. Example: `{'shuffle_files':
    True}`. Note that shuffle_files is False by default unless `split ==
    tfds.Split.TRAIN`.
*   <b>`try_gcs`</b>: `bool`, if True, tfds.load will see if the dataset exists
    on the public GCS bucket before building it locally.

#### Returns:

*   <b>`ds`</b>: `tf.data.Dataset`, the dataset requested, or if `split` is
    None, a `dict<key: tfds.Split, value: tfds.data.Dataset>`. If
    `batch_size=-1`, these will be full datasets as `tf.Tensor`s.
*   <b>`ds_info`</b>:
    <a href="../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a>,
    if `with_info` is True, then
    <a href="../tfds/load.md"><code>tfds.load</code></a> will return a tuple
    `(ds, ds_info)` containing dataset information (version, features, splits,
    num_examples,...). Note that the `ds_info` object documents the entire
    dataset, regardless of the `split` requested. Split-specific information is
    available in `ds_info.splits`.
