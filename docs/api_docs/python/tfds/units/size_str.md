<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.units.size_str" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.units.size_str

``` python
tfds.units.size_str(size_in_bytes)
```



Defined in [`core/units.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/units.py).

<!-- Placeholder for "Used in" -->

Returns a human readable size string.

If size_in_bytes is None, then returns "?? GiB".

For example `size_str(1.5 * tfds.units.GiB) == "1.50 GiB"`.

#### Args:

* <b>`size_in_bytes`</b>: `int` or `None`, the size, in bytes, that we want to
    format as a human-readable size string.