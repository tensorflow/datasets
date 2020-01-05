<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.FeatureConnector" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="decode_batch_example"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="decode_ragged_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.FeatureConnector

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

## Class `FeatureConnector`

Abstract base class for feature types.

<!-- Placeholder for "Used in" -->

This class provides an interface between the way the information is stored
on disk, and the way it is presented to the user.

Here is a diagram on how FeatureConnector methods fit into the data
generation/reading:

```
generator => encode_example() => tf_example => decode_example() => data dict
```

The connector can either get raw or dictionary values as input, depending on
the connector type.

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

``` python
encode_example(example_data)
```

Encode the feature dict into tf-example compatible input.

The input example_data can be anything that the user passed at data
generation. For example:

#### For features:

```
features={
    'image': tfds.features.Image(),
    'custom_feature': tfds.features.CustomFeature(),
}
```

At data generation (in `_generate_examples`), if the user yields:

```
yield {
    'image': 'path/to/img.png',
    'custom_feature': [123, 'str', lambda x: x+1]
}
```

#### Then:

*   <a href="../../tfds/features/Image.md#encode_example"><code>tfds.features.Image.encode_example</code></a>
    will get `'path/to/img.png'` as input
*   `tfds.features.CustomFeature.encode_example` will get `[123, 'str', lambda
    x: x+1] as input

#### Args:

*   <b>`example_data`</b>: Value or dictionary of values to convert into
    tf-example compatible data.

#### Returns:

*   <b>`tfexample_data`</b>: Data or dictionary of data to write as tf-example.
    Data can be a list or numpy array. Note that numpy arrays are flattened so
    it's the feature connector responsibility to reshape them in
    `decode_example()`. Note that tf.train.Example only supports int64, float32
    and string so the data returned here should be integer, float or string.
    User type can be restored in `decode_example()`.

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

Return the tf.Tensor dtype/shape of the feature.

This returns the tensor dtype/shape, as returned by .as_dataset by the
`tf.data.Dataset` object.

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
return tfds.features.TensorInfo(shape=(256, 256), dtype=tf.uint8)
```

#### Returns:

*   <b>`tensor_info`</b>: Either a dict of
    <a href="../../tfds/features/TensorInfo.md"><code>tfds.features.TensorInfo</code></a>
    object, or a
    <a href="../../tfds/features/TensorInfo.md"><code>tfds.features.TensorInfo</code></a>

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

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

*   <b>`data_dir`</b>: `str`, path to the dataset folder to which save the info
    (ex: `~/datasets/cifar10/1.2.0/`)
*   <b>`feature_name`</b>: `str`, the name of the feature (from the FeaturesDict
    key)

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py">View
source</a>

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

*   <b>`data_dir`</b>: `str`, path to the dataset folder to which save the info
    (ex: `~/datasets/cifar10/1.2.0/`)
*   <b>`feature_name`</b>: `str`, the name of the feature (from the FeaturesDict
    key)
