<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Sequence" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="feature"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.Sequence

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

## Class `Sequence`

Composite `FeatureConnector` for a `dict` where each value is a list.

<!-- Placeholder for "Used in" -->

`Sequence` correspond to sequence of
<a href="../../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a>.
At generation time, a list for each of the sequence element is given. The output
of `tf.data.Dataset` will batch all the elements of the sequence together.

If the length of the sequence is static and known in advance, it should be
specified in the constructor using the `length` param.

Note that `Sequence` does not support features which are of type
`tf.io.FixedLenSequenceFeature`.

#### Example:

#### At construction time:

```
tfds.features.Sequence(tfds.features.Image(), length=NB_FRAME)
```

or:

```
tfds.features.Sequence({
    'frame': tfds.features.Image(shape=(64, 64, 3))
    'action': tfds.features.ClassLabel(['up', 'down', 'left', 'right'])
}, length=NB_FRAME)
```

During data generation:

```
yield {
    'frame': np.ones(shape=(NB_FRAME, 64, 64, 3)),
    'action': ['left', 'left', 'up', ...],
}
```

Tensor returned by `.as_dataset()`:

```
{
    'frame': tf.Tensor(shape=(NB_FRAME, 64, 64, 3), dtype=tf.uint8),
    'action': tf.Tensor(shape=(NB_FRAME,), dtype=tf.int64),
}
```

At generation time, you can specify a list of features dict, a dict of list
values or a stacked numpy array. The lists will automatically be distributed
into their corresponding `FeatureConnector`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

```python
__init__(
    feature,
    length=None,
    **kwargs
)
```

Construct a sequence dict.

#### Args:

*   <b>`feature`</b>: `dict`, the features to wrap
*   <b>`length`</b>: `int`, length of the sequence if static and known in
    advance
*   <b>`**kwargs`</b>: `dict`, constructor kwargs of
    <a href="../../tfds/features/FeaturesDict.md"><code>tfds.features.FeaturesDict</code></a>

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="feature"><code>feature</code></h3>

The inner feature.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

```python
__getitem__(key)
```

Convenience method to access the underlying features.

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

```python
encode_example(example_dict)
```

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

``` python
get_serialized_info()
```

See base class for details.

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

```python
load_metadata(
    *args,
    **kwargs
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py">View
source</a>

```python
save_metadata(
    *args,
    **kwargs
)
```

See base class for details.
