<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.load" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.load

``` python
tfds.load(
    *args,
    **kwargs
)
```

Loads the given <a href="../tfds/Split.md"><code>tfds.Split</code></a> as a `tf.data.Dataset`.

`load` is a convenience method that fetches the <a href="../tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a> by
string name, optionally calls `DatasetBuilder.download_and_prepare`
(if `download=True`), and then calls `DatasetBuilder.as_dataset`.

Callers must pass arguments as keyword arguments.

#### Args:

* <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake case
    version of the class name). As a convenience, this string may contain
    comma-separated keyword arguments for the builder. For example
    `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
    arguments `a=True` and `b=3`.
* <b>`split`</b>: <a href="../tfds/Split.md"><code>tfds.Split</code></a>, which split of the data to load.
* <b>`data_dir`</b>: `str`, directory to read/write data.
* <b>`download`</b>: `bool` (optional), whether to call
    <a href="../tfds/DatasetBuilder.md#download_and_prepare"><code>tfds.DatasetBuilder.download_and_prepare</code></a>
    before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
    expected to be in `data_dir`. If `True` and the data is already in
    `data_dir`, `download_and_prepare` is a no-op.
    Defaults to `False`.
* <b>`as_dataset_kwargs`</b>: `dict` (optional), keyword arguments passed to
    <a href="../tfds/DatasetBuilder.md#as_dataset"><code>tfds.DatasetBuilder.as_dataset</code></a>. `split` will be passed through by
    default.


#### Returns:

`tf.data.Dataset`