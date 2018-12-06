<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Text" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="encoder"/>
<meta itemprop="property" content="serialized_keys"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="ints2str"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
<meta itemprop="property" content="str2ints"/>
</div>

# tfds.features.Text

## Class `Text`

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/text_feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text_feature.py).

Feature which encodes/decodes text, possibly to integers.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(encoder=None)
```

Constructs a Text FeatureConnector.

#### Args:

* <b>`encoder`</b>: `TextEncoder`, an encoder that can convert text to integers.
    If None, the text will be utf-8 byte-encoded.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="encoder"><code>encoder</code></h3>



<h3 id="serialized_keys"><code>serialized_keys</code></h3>

List of the flattened feature keys after serialization.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.

<h3 id="vocab_size"><code>vocab_size</code></h3>





## Methods

<h3 id="decode_example"><code>decode_example</code></h3>

``` python
decode_example(tfexample_data)
```



<h3 id="encode_example"><code>encode_example</code></h3>

``` python
encode_example(example_data)
```



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



<h3 id="ints2str"><code>ints2str</code></h3>

``` python
ints2str(int_values)
```

Conversion string => encoded list[int].

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
* <b>`feature_name`</b>: `str`, the name of the feature (from the FeatureDict key)

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
* <b>`feature_name`</b>: `str`, the name of the feature (from the FeatureDict key)

<h3 id="str2ints"><code>str2ints</code></h3>

``` python
str2ints(str_value)
```

Conversion list[int] => decoded string.



