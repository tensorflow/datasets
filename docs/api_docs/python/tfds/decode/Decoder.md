<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.decode.Decoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="setup"/>
</div>

# tfds.decode.Decoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

## Class `Decoder`

Base decoder object.

<!-- Placeholder for "Used in" -->

<a href="../../tfds/decode/Decoder.md"><code>tfds.decode.Decoder</code></a>
allows for overriding the default decoding by implementing a subclass, or
skipping it entirely with
<a href="../../tfds/decode/SkipDecoding.md"><code>tfds.decode.SkipDecoding</code></a>.

Instead of subclassing, you can also create a `Decoder` from a function with the
<a href="../../tfds/decode/make_decoder.md"><code>tfds.decode.make_decoder</code></a>
decorator.

All decoders must derive from this base class. The implementation can access the
`self.feature` property which will correspond to the `FeatureConnector` to which
this decoder is applied.

To implement a decoder, the main method to override is `decode_example`, which
takes the serialized feature as input and returns the decoded feature.

If `decode_example` changes the output dtype, you must also override the `dtype`
property. This enables compatibility with
<a href="../../tfds/features/Sequence.md"><code>tfds.features.Sequence</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

```python
__init__()
```

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Returns the `dtype` after decoding.

## Methods

<h3 id="decode_batch_example"><code>decode_batch_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

```python
decode_batch_example(serialized_example)
```

See
<a href="../../tfds/features/FeatureConnector.md#decode_batch_example"><code>FeatureConnector.decode_batch_example</code></a>
for details.

<h3 id="decode_example"><code>decode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

```python
decode_example(serialized_example)
```

Decode the example feature field (eg: image).

#### Args:

*   <b>`serialized_example`</b>: `tf.Tensor` as decoded, the dtype/shape should
    be identical to `feature.get_serialized_info()`

#### Returns:

*   <b>`example`</b>: Decoded example.

<h3 id="setup"><code>setup</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

```python
setup(feature)
```

Transformation contructor.

The initialization of decode object is deferred because the objects only know
the builder/features on which it is used after it has been constructed, the
initialization is done in this function.

#### Args:

*   <b>`feature`</b>:
    <a href="../../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a>,
    the feature to which is applied this transformation.
