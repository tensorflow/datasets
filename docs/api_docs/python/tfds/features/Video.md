<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Video" />
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

# tfds.features.Video

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/video_feature.py">View
source</a>

## Class `Video`

`FeatureConnector` for videos, encoding frames individually on disk.

Inherits From: [`Sequence`](../../tfds/features/Sequence.md)

<!-- Placeholder for "Used in" -->

Video: The image connector accepts as input a 4 dimensional `tf.uint8` array
representing a video, a sequence of paths to encoded frames, or a path or a file
object that can be decoded with ffmpeg. Note that not all formats in ffmpeg
support reading from pipes, so providing a file object might fail. Furthermore,
if a path is given that is not on the local file system, we first copy it to a
temporary local file before passing it to ffmpeg.

#### Output:

*   <b>`video`</b>: tf.Tensor of type `tf.uint8` and shape [num_frames, height,
    width, channels], where channels must be 1 or 3

#### Example:

*   In the DatasetInfo object:

```
features=features.FeatureDict({
    'video': features.Video(shape=(None, 64, 64, 3)),
})
```

*   During generation, you can use any of:

```
yield {
    'video': np.ones(shape=(128, 64, 64, 3), dtype=np.uint8),
}
```

or list of frames:

```
yield {
    'video': ['path/to/frame001.png', 'path/to/frame002.png'],
}
```

or path to video:

```
yield {
    'video': '/path/to/video.avi',
}
```

or file object:

```
yield {
    'video': tf.io.gfile.GFile('/complex/path/video.avi'),
}
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/video_feature.py">View
source</a>

``` python
__init__(
    shape,
    encoding_format='png',
    ffmpeg_extra_args=()
)
```

Initializes the connector.

#### Args:

*   <b>`shape`</b>: tuple of ints, the shape of the video (num_frames, height,
    width, channels), where channels is 1 or 3.
*   <b>`encoding_format`</b>: The video is stored as a sequence of encoded
    images. You can use any encoding format supported by image_feature.Feature.
*   <b>`ffmpeg_extra_args`</b>: A sequence of additional args to be passed to
    the ffmpeg binary. Specifically, ffmpeg will be called as: `ffmpeg -i
    <input_file> <ffmpeg_extra_args> %010d.<encoding_format>`

#### Raises:

* <b>`ValueError`</b>: If the shape is invalid



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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/video_feature.py">View
source</a>

``` python
encode_example(video_or_path_or_fobj)
```

Converts the given image into a dict convertible to tf example.

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
