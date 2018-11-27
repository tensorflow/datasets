<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.units.size_str" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.units.size_str

``` python
tfds.units.size_str(size_in_bytes)
```



Defined in [`core/units.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/units.py).

Returns a human readable size string.

If size_in_bytes is None, then returns "?? GiB".

#### Args:

* <b>`size_in_bytes`</b>: `integer` or `None`, the size, in bytes, that we want to
    format as a human understandable size string.