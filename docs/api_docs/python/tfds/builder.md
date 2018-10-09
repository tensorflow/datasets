<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.builder" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.builder

``` python
tfds.builder(name)
```

Fetches a <a href="../tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a> by string name.

#### Args:

name (str): the registered name of the `DatasetBuilder` (the snake case
  version of the class name). As a convenience, this string may contain
  comma-separated keyword arguments for the builder. For example
  `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
  arguments `a=True` and `b=3`.


#### Returns:

Constructor for the named `DatasetBuilder`.

If `name` does not contain keyword arguments, this will be the named
`DatasetBuilder` class itself. If `name` does contain kwargs, this will be a
wrapper function with the keyword arguments partially applied.


#### Raises:

* <b>`ValueError`</b>: if `name` is unrecognized.