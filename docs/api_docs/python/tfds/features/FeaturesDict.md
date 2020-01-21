<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.FeaturesDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
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

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

## Class `FeaturesDict`

Composite `FeatureConnector`; each feature in `dict` has its own connector.

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

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

<h3 id="__contains__"><code>__contains__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

```python
__contains__(k)
```

<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
__getitem__(key)
```

Return the feature associated with the key.

<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
__iter__()
```

<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
__len__()
```

<h3 id="decode_batch_example"><code>decode_batch_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_batch_example(tfexample_data)
```

Decode multiple features batched in a single tf.Tensor.

This function is used to decode features wrapped in
<a href="../../tfds/features/Sequence.md"><code>tfds.features.Sequence()</code></a>.
By default, this function apply `decode_example` on each individual elements
using `tf.map_fn`. However, for optimization, features can overwrite this method
to apply a custom batch decoding.

#### Args:

*   <b>`tfexample_data`</b>: Same `tf.Tensor` inputs as `decode_example`, but
    with and additional first dimension for the sequence length.

#### Returns:

*   <b>`tensor_data`</b>: Tensor or dictionary of tensor, output of the
    tf.data.Dataset object

<h3 id="decode_example"><code>decode_example</code></h3>

```python
decode_example(
    *args,
    **kwargs
)
```

Decode the serialize examples.

#### Args:

*   <b>`serialized_example`</b>: Nested `dict` of `tf.Tensor`
*   <b>`decoders`</b>: Nested dict of `Decoder` objects which allow to customize
    the decoding. The structure should match the feature structure, but only
    customized feature keys need to be present. See
    [the guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)
    for more info.

#### Returns:

*   <b>`example`</b>: Nested `dict` containing the decoded nested examples.

<h3 id="decode_ragged_example"><code>decode_ragged_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_ragged_example(tfexample_data)
```

Decode nested features from a tf.RaggedTensor.

This function is used to decode features wrapped in nested
<a href="../../tfds/features/Sequence.md"><code>tfds.features.Sequence()</code></a>.
By default, this function apply `decode_batch_example` on the flat values of the
ragged tensor. For optimization, features can overwrite this method to apply a
custom batch decoding.

#### Args:

*   <b>`tfexample_data`</b>: `tf.RaggedTensor` inputs containing the nested
    encoded examples.

#### Returns:

*   <b>`tensor_data`</b>: The decoded `tf.RaggedTensor` or dictionary of tensor,
    output of the tf.data.Dataset object

<h3 id="encode_example"><code>encode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
encode_example(example_dict)
```

See base class for details.

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
get_serialized_info()
```

See base class for details.

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="items"><code>items</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
items()
```

<h3 id="keys"><code>keys</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
keys()
```

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
load_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
save_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="values"><code>values</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/features_dict.py">View
source</a>

``` python
values()
```
