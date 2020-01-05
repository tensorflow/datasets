<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.ClassLabel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="names"/>
<meta itemprop="property" content="num_classes"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="int2str"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
<meta itemprop="property" content="str2int"/>
</div>

# tfds.features.ClassLabel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

## Class `ClassLabel`

`FeatureConnector` for integer class labels.

Inherits From: [`Tensor`](../../tfds/features/Tensor.md)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
__init__(
    num_classes=None,
    names=None,
    names_file=None
)
```

Constructs a ClassLabel FeatureConnector.

There are 3 ways to define a ClassLabel, which correspond to the 3
arguments:

 * `num_classes`: create 0 to (num_classes-1) labels
 * `names`: a list of label strings
 * `names_file`: a file containing the list of labels.

Note: On python2, the strings are encoded as utf-8.

#### Args:

*   <b>`num_classes`</b>: `int`, number of classes. All labels must be <
    num_classes.
*   <b>`names`</b>: `list<str>`, string names for the integer classes. The order
    in which the names are provided is kept.
*   <b>`names_file`</b>: `str`, path to a file with names for the integer
    classes, one per line.

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="names"><code>names</code></h3>

<h3 id="num_classes"><code>num_classes</code></h3>

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

## Methods

<h3 id="decode_batch_example"><code>decode_batch_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_batch_example(example_data)
```

See base class for details.

<h3 id="decode_example"><code>decode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
decode_example(tfexample_data)
```

Decode the feature dict to TF compatible input.

Note: If eager is not enabled, this function will be executed as a tensorflow
graph (in `tf.data.Dataset.map(features.decode_example)`).

#### Args:

*   <b>`tfexample_data`</b>: Data or dictionary of data, as read by the
    tf-example reader. It correspond to the `tf.Tensor()` (or dict of
    `tf.Tensor()`) extracted from the `tf.train.Example`, matching the info
    defined in `get_serialized_info()`.

#### Returns:

*   <b>`tensor_data`</b>: Tensor or dictionary of tensor, output of the
    tf.data.Dataset object

<h3 id="decode_ragged_example"><code>decode_ragged_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_ragged_example(example_data)
```

See base class for details.

<h3 id="encode_example"><code>encode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
encode_example(example_data)
```

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
get_serialized_info()
```

Return the shape/dtype of features after encoding (for the adapter).

The `FileAdapter` then use those information to write data on disk.

This function indicates how this feature is encoded on file internally.
The DatasetBuilder are written on disk as tf.train.Example proto.

#### Ex:

```
return {
    'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8),
    'height': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
    'width': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
}
```

FeatureConnector which are not containers should return the feature proto
directly:

```
return tfds.features.TensorInfo(shape=(64, 64), tf.uint8)
```

If not defined, the retuned values are automatically deduced from the
`get_tensor_info` function.

#### Returns:

* <b>`features`</b>: Either a dict of feature proto object, or a feature proto object

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="int2str"><code>int2str</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
int2str(int_value)
```

Conversion integer => class name string.

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
load_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
save_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="str2int"><code>str2int</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/class_label_feature.py">View
source</a>

``` python
str2int(str_value)
```

Conversion class name string => integer.
