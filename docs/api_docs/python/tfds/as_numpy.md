<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.as_numpy" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.as_numpy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_utils.py">View
source</a>

Converts a `tf.data.Dataset` to an iterable of NumPy arrays.

``` python
tfds.as_numpy(
    dataset,
    graph=None
)
```

<!-- Placeholder for "Used in" -->

`as_numpy` converts a possibly nested structure of `tf.data.Dataset`s
and `tf.Tensor`s to iterables of NumPy arrays and NumPy arrays, respectively.

Note that because TensorFlow has support for ragged tensors and NumPy has no
equivalent representation,
[`tf.RaggedTensor`s](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
are left as-is for the user to deal with them (e.g. using `to_list()`). In TF 1
(i.e. graph mode), `tf.RaggedTensor`s are returned as
`tf.ragged.RaggedTensorValue`s.

#### Example:

```
ds = tfds.load(name="mnist", split="train")
ds_numpy = tfds.as_numpy(ds)  # Convert `tf.data.Dataset` to Python generator
for ex in ds_numpy:
  # `{'image': np.array(shape=(28, 28, 1)), 'labels': np.array(shape=())}`
  print(ex)
```

#### Args:

*   <b>`dataset`</b>: a possibly nested structure of `tf.data.Dataset`s and/or
    `tf.Tensor`s.
*   <b>`graph`</b>: `tf.Graph`, optional, explicitly set the graph to use.

#### Returns:

A structure matching `dataset` where `tf.data.Dataset`s are converted to
generators of NumPy arrays and `tf.Tensor`s are converted to NumPy arrays.
