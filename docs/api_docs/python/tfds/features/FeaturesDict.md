<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.FeaturesDict" />
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

# tfds.features.FeaturesDict

## Class `FeaturesDict`

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

Main feature connector orchestrator.

The encode/decode method of the spec feature will recursivelly encode/decode
every sub-connector given on the constructor.
Other features can inherit from this class and call super() in order to get
nested container.

Example:

For DatasetInfo:

  features = tfds.features.FeaturesDict({
      'input': tfds.features.Image(),
      'target': tf.int32,
  })

At generation time:

  for image, label in generate_samples:
    yield self.info.features.encode_sample({
        'input': image,
        'output': label
    })

At tf.data.Dataset() time:

  for sample in tfds.load(...):
    tf_input = sample['input']
    tf_output = sample['output']

For nested features, the FeaturesDict will internally flatten the keys for the
features and the conversion to tf.train.Example. Indeed, the tf.train.Example
proto do not support nested feature, while tf.data.Dataset does.
But internal transformation should be invisible to the user.

Example:

  tfds.features.FeaturesDict({
      'input': tf.int32,
      'target': {
          'height': tf.int32,
          'width': tf.int32,
      },
  })

Will internally store the data as:

{
    'input': ...,
    'target/height': ...,
    'target/width': ...,
}

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(feature_dict)
```

Initialize the features.

#### Args:

feature_dict (dict): Dictionary containing the feature connectors of a
  sample. The keys should correspond to the data dict as returned by
  tf.data.Dataset(). Types (tf.int32,...) and dicts will automatically
  be converted into FeatureConnector.


#### Raises:

* <b>`ValueError`</b>: If one of the given features is not recognised



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.



## Methods

<h3 id="decode_sample"><code>decode_sample</code></h3>

``` python
decode_sample(tfexample_dict)
```

See base class for details.

<h3 id="encode_sample"><code>encode_sample</code></h3>

``` python
encode_sample(sample_dict)
```

See base class for details.

<h3 id="get_serialized_features"><code>get_serialized_features</code></h3>

``` python
get_serialized_features()
```

See base class for details.

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

``` python
get_tensor_info()
```

See base class for details.



## Class Members

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

