<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.as_numpy" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.as_numpy

Converts a `tf.data.Dataset` to an iterable of NumPy arrays.

``` python
tfds.as_numpy(
    dataset,
    graph=None
)
```



Defined in [`core/dataset_utils.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_utils.py).

<!-- Placeholder for "Used in" -->

`as_numpy` converts a possibly nested structure of `tf.data.Dataset`s
and `tf.Tensor`s to iterables of NumPy arrays and NumPy arrays, respectively.

#### Args:

*   <b>`dataset`</b>: a possibly nested structure of `tf.data.Dataset`s and/or
    `tf.Tensor`s.
*   <b>`graph`</b>: `tf.Graph`, optional, explicitly set the graph to use.

#### Returns:

A structure matching `dataset` where `tf.data.Dataset`s are converted to
generators of NumPy arrays and `tf.Tensor`s are converted to NumPy arrays.
