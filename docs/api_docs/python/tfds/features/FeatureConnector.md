<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.FeatureConnector" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="decode_sample"/>
<meta itemprop="property" content="encode_sample"/>
<meta itemprop="property" content="get_serialized_features"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="serialized_keys"/>
</div>

# tfds.features.FeatureConnector

## Class `FeatureConnector`





Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

Feature connector class.

This class provides an interface between the way the information is stored
on disk, and the way it is presented to the user.

Here is a diagram on how FeatureConnector methods fit into the data
generation/reading:

  generator => encode_sample() => tf_example => decode_sample() => data dict

The connector can either get raw or dictionary values as input, depending on
the connector type.

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.



## Methods

<h3 id="decode_sample"><code>decode_sample</code></h3>

``` python
decode_sample(tfexample_data)
```

Decode the feature dict to TF compatible input.

#### Args:

* <b>`tfexample_data`</b>: Data or dictionary of data, as read by the tf-example
    reader.


#### Returns:

* <b>`tensor_data`</b>: Tensor or dictionary of tensor, output of the tf.data.Dataset
    object

<h3 id="encode_sample"><code>encode_sample</code></h3>

``` python
encode_sample(sample_data)
```

Encode the feature dict into tf-example compatible input.

#### Args:

* <b>`sample_data`</b>: Value or dictionary of values to convert into tf-example
    compatible data.


#### Returns:

* <b>`tfexample_data`</b>: Data or dictionary of data to write as tf-example

<h3 id="get_serialized_features"><code>get_serialized_features</code></h3>

``` python
get_serialized_features()
```

Return the tf-example features for the adapter, as stored on disk.

This function indicates how this feature is encoded on file internally.
The DatasetBuilder are written on disk as tf.train.Example proto.

Ex:

  return {
      'image': tf.VarLenFeature(tf.uint8):
      'height': tf.FixedLenFeature((), tf.int32),
      'width': tf.FixedLenFeature((), tf.int32),
  }

FeatureConnector which are not containers should return the feature proto
directly:

  return tf.FixedLenFeature((64, 64), tf.uint8)

If not defined, the retuned values are automatically deduced from the
`get_tensor_info` function.

#### Returns:

* <b>`features`</b>: Either a dict of feature proto object, or a feature proto object

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

``` python
get_tensor_info()
```

Return the tf.Tensor dtype/shape of the feature.

This returns the tensor dtype/shape, as returned by .as_dataset by the
`tf.data.Dataset` object.

Ex:

  return {
      'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8):
      'height': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
      'width': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
  }

FeatureConnector which are not containers should return the feature proto
directly:

  return tfds.features.TensorInfo(shape=(256, 256), dtype=tf.uint8)

#### Returns:

* <b>`tensor_info`</b>: Either a dict of <a href="../../tfds/features/TensorInfo.md"><code>tfds.features.TensorInfo</code></a> object, or a
    <a href="../../tfds/features/TensorInfo.md"><code>tfds.features.TensorInfo</code></a>



## Class Members

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

