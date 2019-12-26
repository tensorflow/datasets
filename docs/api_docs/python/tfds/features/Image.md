<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Image" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
<meta itemprop="property" content="set_dtype"/>
<meta itemprop="property" content="set_encoding_format"/>
<meta itemprop="property" content="set_shape"/>
</div>

# tfds.features.Image

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

## Class `Image`

`FeatureConnector` for images.

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)

<!-- Placeholder for "Used in" -->

During `_generate_examples`, the feature connector accept as input any of:

*   `str`: path to a {bmp,gif,jpeg,png} image (ex: `/path/to/img.png`).
*   `np.array`: 3d `np.uint8` array representing an image.
*   A file object containing the png or jpeg encoded image string (ex:
    `io.BytesIO(encoded_img_bytes)`)

#### Output:

`tf.Tensor` of type `tf.uint8` and shape `[height, width, num_channels]` for
BMP, JPEG, and PNG images and shape `[num_frames, height, width, 3]` for GIF
images.

#### Example:

*   In the
    <a href="../../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a>
    object:

```python
features=features.FeaturesDict({
    'input': features.Image(),
    'target': features.Image(shape=(None, None, 1),
                               encoding_format='png'),
})
```

*   During generation:

```python
yield {
    'input': 'path/to/img.jpg',
    'target': np.ones(shape=(64, 64, 1), dtype=np.uint8),
}
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

```python
__init__(
    shape=None,
    dtype=None,
    encoding_format=None
)
```

Construct the connector.

#### Args:

*   <b>`shape`</b>: tuple of ints or None, the shape of decoded image. For GIF
    images: (num_frames, height, width, channels=3). num_frames, height and
    width can be None. For other images: (height, width, channels). height and
    width can be None. See `tf.image.encode_*` for doc on channels parameter.
    Defaults to (None, None, 3).
*   <b>`dtype`</b>: tf.uint16 or tf.uint8 (default). tf.uint16 can be used only
    with png encoding_format
*   <b>`encoding_format`</b>: 'jpeg' or 'png' (default). Format to serialize
    np.ndarray images on disk. If image is loaded from {bmg,gif,jpeg,png} file,
    this parameter is ignored, and file original encoding is used.

#### Raises:

* <b>`ValueError`</b>: If the shape is invalid



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

## Methods

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
decode_example(example)
```

Reconstruct the image from the tf example.

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
encode_example(image_or_path_or_fobj)
```

Convert the given image into a dict convertible to tf example.

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
get_serialized_info()
```

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
get_tensor_info()
```

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
load_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
save_metadata(
    data_dir,
    feature_name=None
)
```

See base class for details.

<h3 id="set_dtype"><code>set_dtype</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

```python
set_dtype(dtype)
```

Update the dtype.

<h3 id="set_encoding_format"><code>set_encoding_format</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
set_encoding_format(encoding_format)
```

Update the encoding format.

<h3 id="set_shape"><code>set_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/image_feature.py">View
source</a>

``` python
set_shape(shape)
```

Update the shape.
