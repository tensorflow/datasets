<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.decode.SkipDecoding" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="setup"/>
</div>

# tfds.decode.SkipDecoding

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

## Class `SkipDecoding`

Transformation which skip the decoding entirelly.

Inherits From: [`Decoder`](../../tfds/decode/Decoder.md)

<!-- Placeholder for "Used in" -->

#### Example of usage:

```python
ds = ds.load(
    'imagenet2012',
    split='train',
    decoders={
        'image': tfds.decode.SkipDecoding(),
    }
)

for ex in ds.take(1):
  assert ex['image'].dtype == tf.string
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py">View
source</a>

```python
__init__()
```

## Properties

<h3 id="dtype"><code>dtype</code></h3>

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

Forward the serialized feature field.

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
