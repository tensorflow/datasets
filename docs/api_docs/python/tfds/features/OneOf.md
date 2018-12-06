<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.OneOf" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="serialized_keys"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__getattr__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.OneOf

## Class `OneOf`

Inherits From: [`FeaturesDict`](../../tfds/features/FeaturesDict.md)



Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

Feature which encodes multiple features, but decodes only one at runtime.

This avoids having duplicate files for every version of your dataset. You
can just encode everything on disk in a single dataset, and choose which
output you want for the tf.data.Dataset at decode time.

Example:

```
features = tfds.features.FeaturesDict({
    'labels': features.OneOf('coco', {
        'coco': tf.string,
        'cifar10': tf.string,
    }),
})
```

At generation time, encode both coco and cifar labels:

```
for example in generate_examples:
  yield self.info.features.encode_example({
      'labels': {
          'coco': 'person',
          'cifar10': 'airplane',
      },
  })
```

At tf.data.Dataset() time, only the label from coco is decoded:

```
for example in tfds.load(...):
  tf_label = example['labels']  # == 'person'
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    choice,
    feature_dict
)
```

Create the features for the container.

#### Args:

choice (str): The key of the spec to decode.
feature_dict (dict): Dictionary containing the sub fields. The choice
  should match one of the key.


#### Raises:

* <b>`ValueError`</b>: If the choice is invalid.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

List of the flattened feature keys after serialization.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.



## Methods

<h3 id="__getattr__"><code>__getattr__</code></h3>

``` python
__getattr__(key)
```

Access choice attribute.

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(key)
```

Return the feature associated with the key.

<h3 id="decode_example"><code>decode_example</code></h3>

``` python
decode_example(tfexample_dict)
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



