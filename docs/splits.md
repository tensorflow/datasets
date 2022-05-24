# Splits and slicing

All TFDS datasets expose various data splits (e.g. `'train'`, `'test'`) which
can be explored in the
[catalog](https://www.tensorflow.org/datasets/catalog/overview).

In addition of the "official" dataset splits, TFDS allow to select slice(s) of
split(s) and various combinations.

## Slicing API

Slicing instructions are specified in `tfds.load` or
`tfds.DatasetBuilder.as_dataset` through the `split=` kwarg.

```python
ds = tfds.load('my_dataset', split='train[:75%]')
```

```python
builder = tfds.builder('my_dataset')
ds = builder.as_dataset(split='test+train[:75%]')
```

Split can be:

*   **Plain split** (`'train'`, `'test'`): All examples within the split
    selected.
*   **Slices**: Slices have the same semantic as
    [python slice notation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).
    Slices can be:
    *   **Absolute** (`'train[123:450]'`, `train[:4000]`): (see note below for
        caveat about read order)
    *   **Percent** (`'train[:75%]'`, `'train[25%:75%]'`): Divide the full data
        into 100 even slices. If the data is not divisible by 100, some percent
        might contain additional examples.
    *   **Shard** (`train[:4shard]`, `train[4shard]`): Select all examples in
        the requested shard. (see `info.splits['train'].num_shards` to get the
        number of shards of the split)
*   **Union of splits** (`'train+test'`, `'train[:25%]+test'`): Splits will be
    interleaved together.
*   **Full dataset** (`'all'`): `'all'` is a special split name corresponding to
    the union of all splits (equivalent to `'train+test+...'`).
*   **List of splits** (`['train', 'test']`): Multiple `tf.data.Dataset` are
    returned separately:

```python
# Returns both train and test split separately
train_ds, test_ds = tfds.load('mnist', split=['train', 'test[:50%]'])
```

Note: Due to the shards being
[interleaved](https://www.tensorflow.org/api_docs/python/tf/data/Dataset?version=nightly#interleave),
order isn't guaranteed to be consistent between sub-splits. In other words
reading `test[0:100]` followed by `test[100:200]` may yield examples in a
different order than reading `test[:200]`. See
[determinism guide](https://www.tensorflow.org/datasets/determinism#determinism_when_reading)
to understand the order in which TFDS read examples.

## `tfds.even_splits` & multi-host training

`tfds.even_splits` generates a list of non-overlapping sub-splits of the same
size.

```python
# Divide the dataset into 3 even parts, each containing 1/3 of the data
split0, split1, split2 = tfds.even_splits('train', n=3)

ds = tfds.load('my_dataset', split=split2)
```

This can be particularly useful when training in a distributed setting, where
each host should receive a slice of the original data.

With `Jax`, this can be simplified even further using
`tfds.split_for_jax_process`:

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

`tfds.even_splits`, `tfds.split_for_jax_process` accepts on any split value as
input (e.g. `'train[75%:]+test'`)

## Slicing and metadata

It is possible to get additional info on the splits/subsplits (`num_examples`,
`file_instructions`,...) using the
[dataset info](https://www.tensorflow.org/datasets/overview#access_the_dataset_metadata):

```python
builder = tfds.builder('my_dataset')
builder.info.splits['train'].num_examples  # 10_000
builder.info.splits['train[:75%]'].num_examples  # 7_500 (also works with slices)
builder.info.splits.keys()  # ['train', 'test']
```

## Cross validation

Examples of 10-fold cross-validation using the string API:

```python
vals_ds = tfds.load('mnist', split=[
    f'train[{k}%:{k+10}%]' for k in range(0, 100, 10)
])
trains_ds = tfds.load('mnist', split=[
    f'train[:{k}%]+train[{k+10}%:]' for k in range(0, 100, 10)
])
```

The validation datasets are each going to be 10%: `[0%:10%]`, `[10%:20%]`, ...,
`[90%:100%]`. And the training datasets are each going to be the complementary
90%: `[10%:100%]` (for a corresponding validation set of `[0%:10%]`), `[0%:10%]
+ [20%:100%]`(for a validation set of `[10%:20%]`),...

## `tfds.core.ReadInstruction` and rounding

Rather than `str`, it is possible to pass splits as `tfds.core.ReadInstruction`:

For example, `split = 'train[50%:75%] + test'` is equivalent to:

```python
split = (
    tfds.core.ReadInstruction(
        'train',
        from_=50,
        to=75,
        unit='%',
    )
    + tfds.core.ReadInstruction('test')
)
ds = tfds.load('my_dataset', split=split)
```

`unit` can be:

*   `abs`: Absolute slicing
*   `%`: Percent slicing
*   `shard`: Shard slicing

`tfds.ReadInstruction` also has a rounding argument. If the number of example in
the dataset is not divide evenly by `100`:

*   `rounding='closest'` (default): The remaining examples are distributed among
    the percent, so some percent might contain additional examples.
*   `rounding='pct1_dropremainder'`: The remaining examples are dropped, but
    this guarantee all percent contain the exact same number of example (eg:
    `len(5%) == 5 * len(1%)`).

### Reproducibility & determinism

During generation, for a given dataset version, TFDS guarantee that examples are
deterministically shuffled on disk. So generating the dataset twice (in 2
different computers) won't change the example order.

Similarly, the subsplit API will always select the same `set` of examples,
regardless of platform, architecture, etc. This mean `set('train[:20%]') ==
set('train[:10%]') + set('train[10%:20%]')`.

However, the order in which examples are read might **not** be deterministic.
This depends on other parameters (e.g. whether `shuffle_files=True`).
