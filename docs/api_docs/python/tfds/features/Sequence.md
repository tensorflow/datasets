<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Sequence" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="feature"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__getattr__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__getstate__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__setstate__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.Sequence

## Class `Sequence`

Composite `FeatureConnector` for a `dict` where each value is a list.

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/sequence_feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py).

<!-- Placeholder for "Used in" -->

`Sequence` correspond to sequence of
<a href="../../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a>.
At generation time, a list for each of the sequence element is given. The output
of `tf.data.Dataset` will batch all the elements of the sequence together.

If the length of the sequence is static and known in advance, it should be
specified in the constructor using the `length` param.

Note that `SequenceDict` do not support features which are of type
`tf.io.FixedLenSequenceFeature`.

#### Example:

#### At construction time:

```
tfds.features.Sequence(tfds.features.Image(), length=NB_FRAME)
```

or: `tfds.features.Sequence({ 'frame': tfds.features.Image(shape=(64, 64, 3))
'action': tfds.features.ClassLabel(['up', 'down', 'left', 'right']) },
length=NB_FRAME)`

During data generation: `yield { 'frame': np.ones(shape=(NB_FRAME, 64, 64, 3)),
'action': ['left', 'left', 'up', ...], }`

Tensor returned by `.as_dataset()`: `{ 'frame': tf.Tensor(shape=(NB_FRAME, 64,
64, 3), dtype=tf.uint8), 'action': tf.Tensor(shape=(NB_FRAME,), dtype=tf.int64),
}`

At generation time, you can specify a list of features dict, a dict of list
values or a stacked numpy array. The lists will automatically be distributed
into their corresponding `FeatureConnector`.

<h2 id="__init__"><code>__init__</code></h2>

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

<h3 id="__getattr__"><code>__getattr__</code></h3>

``` python
__getattr__(key)
```

Allow to access the underlying attributes directly.

<h3 id="__getitem__"><code>__getitem__</code></h3>

```python
__getitem__(key)
```

Convenience method to access the underlying features.

<h3 id="__getstate__"><code>__getstate__</code></h3>

```python
__getstate__()
```

<h3 id="__setstate__"><code>__setstate__</code></h3>

```python
__setstate__(state)
```

<h3 id="decode_example"><code>decode_example</code></h3>

```python
decode_example(tfexample_dict)
```

<h3 id="encode_example"><code>encode_example</code></h3>

```python
encode_example(example_dict)
```

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

```python
load_metadata(
    *args,
    **kwargs
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

```python
save_metadata(
    *args,
    **kwargs
)
```

See base class for details.
