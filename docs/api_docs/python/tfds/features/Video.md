<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Video" />
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

# tfds.features.Video

## Class `Video`

`FeatureConnector` for videos, encoding frames individually on disk.

Inherits From: [`Sequence`](../../tfds/features/Sequence.md)



Defined in [`core/features/video_feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/video_feature.py).

<!-- Placeholder for "Used in" -->

Video: The image connector accepts as input a 4 dimensional uint8 array
representing a video, a sequence of paths to encoded frames, or a path or a
file object that can be decoded with ffmpeg. Note that not all formats in
ffmpeg support reading from pipes, so providing a file object might fail.
Furthermore, if a path is given that is not on the local file system, we first
copy it to a temporary local file before passing it to ffmpeg.

#### Output:

*   <b>`video`</b>: tf.Tensor of type tf.uint8 and shape [num_frames, height,
    width, channels], where channels must be 1 or 3

#### Example:

*   In the DatasetInfo object: features=features.FeatureDict({ 'video':
    features.Video(shape=(None, 64, 64, 3)), })

*   During generation: `yield { 'input': np.ones(shape=(128, 64, 64, 3),
    dtype=np.uint8), }` or `yield { ' video': ['path/to/frame001.png',
    'path/to/frame002.png'], }` or `yield { 'input': '/path/to/video.avi', }` or
    `yield { 'input': gfile.GFile('/complex/path/video.avi'), }`

<h2 id="__init__"><code>__init__</code></h2>

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

``` python
encode_example(video_or_path_or_fobj)
```

Converts the given image into a dict convertible to tf example.

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
