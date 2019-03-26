<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.BBoxFeature" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="serialized_keys"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.BBoxFeature

## Class `BBoxFeature`

Inherits From: [`Tensor`](../../tfds/features/Tensor.md)



Defined in [`core/features/bounding_boxes.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/bounding_boxes.py).

`FeatureConnector` for a normalized bounding box.

Note: If you have multiple bounding boxes, you may want to wrap the feature
inside a `tfds.feature.SequenceDict`.

Input:
  * <a href="../../tfds/features/BBox.md"><code>tfds.features.BBox</code></a> tuple.

Output:
  bbox: tf.Tensor of type tf.float32 and shape [4,] which contains the
    normalized coordinates of the bounding box [ymin, xmin, ymax, xmax]

Example:
  * In the DatasetInfo object:
    features=features.FeatureDict({
        'bbox': features.BBox(shape=(None, 64, 64, 3)),
    })

  * During generation:
    yield {
        'input': tfds.feature.BBox(ymin=0.3, xmin=0.8, ymax=0.5, xmax=1.0),
    }

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```





## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

List of the flattened feature keys after serialization.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.



## Methods

<h3 id="decode_example"><code>decode_example</code></h3>

``` python
decode_example(tfexample_data)
```

See base class for details.

<h3 id="encode_example"><code>encode_example</code></h3>

``` python
encode_example(bbox)
```

See base class for details.

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

``` python
get_serialized_info()
```

Return the tf-example features for the adapter, as stored on disk.

This function indicates how this feature is encoded on file internally.
The DatasetBuilder are written on disk as tf.train.Example proto.

Ex:

```
return {
    'image': tf.VarLenFeature(tf.uint8):
    'height': tf.FixedLenFeature((), tf.int32),
    'width': tf.FixedLenFeature((), tf.int32),
}
```

FeatureConnector which are not containers should return the feature proto
directly:

```
return tf.FixedLenFeature((64, 64), tf.uint8)
```

If not defined, the retuned values are automatically deduced from the
`get_tensor_info` function.

#### Returns:

* <b>`features`</b>: Either a dict of feature proto object, or a feature proto object

<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

``` python
get_tensor_info()
```

See base class for details.

<h3 id="load_metadata"><code>load_metadata</code></h3>

``` python
load_metadata(
    data_dir,
    feature_name
)
```

Restore the feature metadata from disk.

If a dataset is re-loaded and generated files exists on disk, this function
will restore the feature metadata from the saved file.

#### Args:

* <b>`data_dir`</b>: `str`, path to the dataset folder to which save the info (ex:
    `~/datasets/cifar10/1.2.0/`)
* <b>`feature_name`</b>: `str`, the name of the feature (from the FeaturesDict key)

<h3 id="save_metadata"><code>save_metadata</code></h3>

``` python
save_metadata(
    data_dir,
    feature_name
)
```

Save the feature metadata on disk.

This function is called after the data has been generated (by
`_download_and_prepare`) to save the feature connector info with the
generated dataset.

Some dataset/features dynamically compute info during
`_download_and_prepare`. For instance:

 * Labels are loaded from the downloaded data
 * Vocabulary is created from the downloaded data
 * ImageLabelFolder compute the image dtypes/shape from the manual_dir

After the info have been added to the feature, this function allow to
save those additional info to be restored the next time the data is loaded.

By default, this function do not save anything, but sub-classes can
overwrite the function.

#### Args:

* <b>`data_dir`</b>: `str`, path to the dataset folder to which save the info (ex:
    `~/datasets/cifar10/1.2.0/`)
* <b>`feature_name`</b>: `str`, the name of the feature (from the FeaturesDict key)



