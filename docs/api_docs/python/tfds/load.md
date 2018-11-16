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
    download=True,
    as_supervised=False,
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

Callers must pass arguments as keyword arguments.

**Warning**: calling this function might potentially trigger the download
of hundreds of GiB to disk. Refer to download argument.

#### Args:

* <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake case
    version of the class name). As a convenience, this string may contain
    comma-separated keyword arguments for the builder. For example
    `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
    arguments `a=True` and `b=3`.
* <b>`split`</b>: <a href="../tfds/Split.md"><code>tfds.Split</code></a>, which split of the data to load.
* <b>`data_dir`</b>: `str` (optional), directory to read/write data.
    Defaults to "~/tensorflow_datasets".
* <b>`download`</b>: `bool` (optional), whether to call
    <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>
    before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
    expected to be in `data_dir`. If `True` and the data is already in
    `data_dir`, `download_and_prepare` is a no-op.
    Defaults to `True`.
* <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default,
    the returned `tf.data.Dataset` will have a dictionary with all the
    features.
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

`tf.data.Dataset`