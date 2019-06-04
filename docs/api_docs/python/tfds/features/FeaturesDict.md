<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.FeaturesDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="items"/>
<meta itemprop="property" content="keys"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
<meta itemprop="property" content="values"/>
</div>

# tfds.features.FeaturesDict

## Class `FeaturesDict`

Composite `FeatureConnector`; each feature in `dict` has its own connector.

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

<!-- Placeholder for "Used in" -->

The encode/decode method of the spec feature will recursively encode/decode
every sub-connector given on the constructor.
Other features can inherit from this class and call super() in order to get
nested container.

#### Example:

#### For DatasetInfo:

```
features = tfds.features.FeaturesDict({
    'input': tfds.features.Image(),
    'output': tf.int32,
})
```

#### At generation time:

```
for image, label in generate_examples:
  yield {
      'input': image,
      'output': label
  }
```

At tf.data.Dataset() time:

```
for example in tfds.load(...):
  tf_input = example['input']
  tf_output = example['output']
```

For nested features, the FeaturesDict will internally flatten the keys for the
features and the conversion to tf.train.Example. Indeed, the tf.train.Example
proto do not support nested feature, while tf.data.Dataset does.
But internal transformation should be invisible to the user.

#### Example:

```
tfds.features.FeaturesDict({
    'input': tf.int32,
    'target': {
        'height': tf.int32,
        'width': tf.int32,
    },
})
```

Will internally store the data as:

```
{
    'input': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
    'target/height': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
    'target/width': tf.io.FixedLenFeature(shape=(), dtype=tf.int32),
}
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(feature_dict)
```

Initialize the features.

#### Args:

feature_dict (dict): Dictionary containing the feature connectors of a
  example. The keys should correspond to the data dict as returned by
  tf.data.Dataset(). Types (tf.int32,...) and dicts will automatically
  be converted into FeatureConnector.

#### Raises:

* <b>`ValueError`</b>: If one of the given features is not recognized



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(key)
```

Return the feature associated with the key.

<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```

<h3 id="decode_example"><code>decode_example</code></h3>

```python
decode_example(example_dict)
```

See base class for details.

<h3 id="encode_example"><code>encode_example</code></h3>

``` python
encode_example(example_dict)
```

See base class for details.

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

``` python
get_serialized_info()
```

See base class for details.

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="items"><code>items</code></h3>

``` python
items()
```

<h3 id="keys"><code>keys</code></h3>

``` python
keys()
```

<h3 id="load_metadata"><code>load_metadata</code></h3>

``` python
load_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

``` python
save_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="values"><code>values</code></h3>

``` python
values()
```
