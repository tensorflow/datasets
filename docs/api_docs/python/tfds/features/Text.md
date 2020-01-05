<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Text" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="encoder"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="ints2str"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="maybe_build_from_corpus"/>
<meta itemprop="property" content="maybe_set_encoder"/>
<meta itemprop="property" content="save_metadata"/>
<meta itemprop="property" content="str2ints"/>
</div>

# tfds.features.Text

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

## Class `Text`

`FeatureConnector` for text, encoding to integers with a `TextEncoder`.

Inherits From: [`Tensor`](../../tfds/features/Tensor.md)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
__init__(
    encoder=None,
    encoder_config=None
)
```

Constructs a Text FeatureConnector.

#### Args:

*   <b>`encoder`</b>:
    <a href="../../tfds/features/text/TextEncoder.md"><code>tfds.features.text.TextEncoder</code></a>,
    an encoder that can convert text to integers. If None, the text will be
    utf-8 byte-encoded.
*   <b>`encoder_config`</b>:
    <a href="../../tfds/features/text/TextEncoderConfig.md"><code>tfds.features.text.TextEncoderConfig</code></a>,
    needed if restoring from a file with `load_metadata`.

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="encoder"><code>encoder</code></h3>

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

<h3 id="vocab_size"><code>vocab_size</code></h3>

## Methods

<h3 id="decode_batch_example"><code>decode_batch_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_batch_example(example_data)
```

See base class for details.

<h3 id="decode_example"><code>decode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
decode_example(tfexample_data)
```

Decode the feature dict to TF compatible input.

Note: If eager is not enabled, this function will be executed as a tensorflow
graph (in `tf.data.Dataset.map(features.decode_example)`).

#### Args:

*   <b>`tfexample_data`</b>: Data or dictionary of data, as read by the
    tf-example reader. It correspond to the `tf.Tensor()` (or dict of
    `tf.Tensor()`) extracted from the `tf.train.Example`, matching the info
    defined in `get_serialized_info()`.

#### Returns:

*   <b>`tensor_data`</b>: Tensor or dictionary of tensor, output of the
    tf.data.Dataset object

<h3 id="decode_ragged_example"><code>decode_ragged_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

```python
decode_ragged_example(example_data)
```

See base class for details.

<h3 id="encode_example"><code>encode_example</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
encode_example(example_data)
```

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
get_serialized_info()
```

Return the shape/dtype of features after encoding (for the adapter).

The `FileAdapter` then use those information to write data on disk.

This function indicates how this feature is encoded on file internally.
The DatasetBuilder are written on disk as tf.train.Example proto.

#### Ex:

```
return {
    'image': tfds.features.TensorInfo(shape=(None,), dtype=tf.uint8),
    'height': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
    'width': tfds.features.TensorInfo(shape=(), dtype=tf.int32),
}
```

FeatureConnector which are not containers should return the feature proto
directly:

```
return tfds.features.TensorInfo(shape=(64, 64), tf.uint8)
```

If not defined, the retuned values are automatically deduced from the
`get_tensor_info` function.

#### Returns:

* <b>`features`</b>: Either a dict of feature proto object, or a feature proto object

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="ints2str"><code>ints2str</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
ints2str(int_values)
```

Conversion list[int] => decoded string.

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
load_metadata(
    data_dir,
    feature_name
)
```

<h3 id="maybe_build_from_corpus"><code>maybe_build_from_corpus</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
maybe_build_from_corpus(
    corpus_generator,
    **kwargs
)
```

Call SubwordTextEncoder.build_from_corpus is encoder_cls is such.

If `self.encoder` is `None` and `self._encoder_cls` is of type
`SubwordTextEncoder`, the method instantiates `self.encoder` as returned by
<a href="../../tfds/features/text/SubwordTextEncoder.md#build_from_corpus"><code>SubwordTextEncoder.build_from_corpus()</code></a>.

#### Args:

*   <b>`corpus_generator`</b>: generator yielding `str`, from which subwords
    will be constructed.
*   <b>`**kwargs`</b>: kwargs forwarded to
    <a href="../../tfds/features/text/SubwordTextEncoder.md#build_from_corpus"><code>SubwordTextEncoder.build_from_corpus()</code></a>

<h3 id="maybe_set_encoder"><code>maybe_set_encoder</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
maybe_set_encoder(new_encoder)
```

Set encoder, but no-op if encoder is already set.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
save_metadata(
    data_dir,
    feature_name
)
```

<h3 id="str2ints"><code>str2ints</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py">View
source</a>

``` python
str2ints(str_value)
```

Conversion string => encoded list[int].
