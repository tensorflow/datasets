<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Tensor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_sample"/>
<meta itemprop="property" content="encode_sample"/>
<meta itemprop="property" content="get_serialized_features"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="serialized_keys"/>
</div>

# tfds.features.Tensor

## Class `Tensor`

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

Feature encoding a tf.Tensor value (both fixed and variable).

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Construct a Tensor feature.



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

See base class for details.

<h3 id="encode_sample"><code>encode_sample</code></h3>

``` python
encode_sample(sample_data)
```

See base class for details.

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

See base class for details.



## Class Members

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

