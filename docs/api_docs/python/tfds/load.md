<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.load" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.load

``` python
tfds.load(
    name,
    split,
    data_dir=None,
    batch_size=1,
    download=True,
    as_numpy=False,
    as_supervised=False,
    with_info=False,
    builder_kwargs=None,
    download_and_prepare_kwargs=None,
    as_dataset_kwargs=None
)
```



Defined in [`core/registered.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/registered.py).

Loads the given <a href="../tfds/Split.md"><code>tfds.Split</code></a> as a `tf.data.Dataset`.

`load` is a convenience method that fetches the <a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a> by
string name, optionally calls `DatasetBuilder.download_and_prepare`
(if `download=True`), and then calls `DatasetBuilder.as_dataset`.
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

Callers must pass arguments as keyword arguments.

**Warning**: calling this function might potentially trigger the download
of hundreds of GiB to disk. Refer to download argument.

#### Args:

* <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake case
    version of the class name). This can be either `"dataset_name"` or
    `"dataset_name/config_name"` for datasets with `BuilderConfig`s.
    As a convenience, this string may contain comma-separated keyword
    arguments for the builder. For example `"foo_bar/a=True,b=3"` would use
    the `FooBar` dataset passing the keyword arguments `a=True` and `b=3`
    (for builders with configs, it would be `"foo_bar/zoo/a=True,b=3"` to
    use the `"zoo"` config and pass to the builder keyword arguments `a=True`
    and `b=3`).
* <b>`split`</b>: <a href="../tfds/Split.md"><code>tfds.Split</code></a>, which split of the data to load.
* <b>`data_dir`</b>: `str` (optional), directory to read/write data.
    Defaults to "~/tensorflow_datasets".
* <b>`batch_size`</b>: `int`, set to > 1 to get batches of examples. Note that
    variable length features will be 0-padded. If `as_numpy=True` and
    `batch_size=-1`, will return the full dataset in NumPy arrays.
* <b>`download`</b>: `bool` (optional), whether to call
    <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>
    before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
    expected to be in `data_dir`. If `True` and the data is already in
    `data_dir`, `download_and_prepare` is a no-op.
    Defaults to `True`.
* <b>`as_numpy`</b>: `bool`, whether to return a generator of NumPy array batches
    using <a href="../tfds/core/DatasetBuilder.md#as_numpy"><code>tfds.core.DatasetBuilder.as_numpy</code></a>.
* <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default,
    the returned `tf.data.Dataset` will have a dictionary with all the
    features.
* <b>`with_info`</b>: `bool`, if True, tfds.load will return the tuple
    (tf.data.Dataset, tfds.core.DatasetInfo) containing the info associated
    with the builder.
* <b>`builder_kwargs`</b>: `dict` (optional), keyword arguments to be passed to the
    <a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a> constructor. `data_dir` will be passed
    through by default.
* <b>`download_and_prepare_kwargs`</b>: `dict` (optional) keyword arguments passed to
    <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a> if `download=True`. Allow
    to control where to download and extract the cached data. If not set,
    cache_dir and manual_dir will automatically be deduced from data_dir.
* <b>`as_dataset_kwargs`</b>: `dict` (optional), keyword arguments passed to
    <a href="../tfds/core/DatasetBuilder.md#as_dataset"><code>tfds.core.DatasetBuilder.as_dataset</code></a>. `split` will be passed through by
    default.


#### Returns:

* <b>`ds`</b>: `tf.data.Dataset`, the dataset requested.
* <b>`ds_info`</b>: <a href="../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a>, if `with_info` is True, then tfds.load
    will return a tuple (ds, ds_info) containing the dataset info (version,
    features, splits, num_examples,...).