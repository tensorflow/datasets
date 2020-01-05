<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.builder" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.builder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/registered.py">View
source</a>

Fetches a
<a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>
by string name.

``` python
tfds.builder(
    name,
    **builder_init_kwargs
)
```

<!-- Placeholder for "Used in" -->

#### Args:

*   <b>`name`</b>: `str`, the registered name of the `DatasetBuilder` (the snake
    case version of the class name). This can be either `"dataset_name"` or
    `"dataset_name/config_name"` for datasets with `BuilderConfig`s. As a
    convenience, this string may contain comma-separated keyword arguments for
    the builder. For example `"foo_bar/a=True,b=3"` would use the `FooBar`
    dataset passing the keyword arguments `a=True` and `b=3` (for builders with
    configs, it would be `"foo_bar/zoo/a=True,b=3"` to use the `"zoo"` config
    and pass to the builder keyword arguments `a=True` and `b=3`).
*   <b>`**builder_init_kwargs`</b>: `dict` of keyword arguments passed to the
    `DatasetBuilder`. These will override keyword arguments passed in `name`, if
    any.

#### Returns:

A
<a href="../tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>.

#### Raises:

*   <b>`DatasetNotFoundError`</b>: if `name` is unrecognized.
