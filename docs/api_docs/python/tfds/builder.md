<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.builder" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.builder

``` python
tfds.builder(
    name,
    **ctor_kwargs
)
```

Fetches a <a href="../tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a> by string name.

#### Args:

* <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake case
    version of the class name). As a convenience, this string may contain
    comma-separated keyword arguments for the builder separated from the name
    by a "/". For example `"foo_bar/a=True,b=3"` would use the `FooBar`
    dataset with keyword arguments `a=True` and `b=3`.
* <b>`**ctor_kwargs`</b>: `dict` of keyword arguments passed to the `DatasetBuilder`.
    These will override keyword arguments passed in `name`, if any.


#### Returns:

A <a href="../tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a>.


#### Raises:

* <b>`ValueError`</b>: if `name` is unrecognized.