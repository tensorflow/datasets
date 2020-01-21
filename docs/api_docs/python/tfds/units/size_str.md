<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.units.size_str" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.units.size_str

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/units.py">View
source</a>

Returns a human readable size string.

``` python
tfds.units.size_str(size_in_bytes)
```

<!-- Placeholder for "Used in" -->

If size_in_bytes is None, then returns "?? GiB".

For example `size_str(1.5 * tfds.units.GiB) == "1.50 GiB"`.

#### Args:

*   <b>`size_in_bytes`</b>: `int` or `None`, the size, in bytes, that we want to
    format as a human-readable size string.
