<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.Sequence" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="dtype"/>
<meta itemprop="property" content="serialized_keys"/>
<meta itemprop="property" content="shape"/>
<meta itemprop="property" content="__getattr__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode_example"/>
<meta itemprop="property" content="encode_example"/>
<meta itemprop="property" content="get_serialized_info"/>
<meta itemprop="property" content="get_tensor_info"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.features.Sequence

## Class `Sequence`

Inherits From: [`FeatureConnector`](../../tfds/features/FeatureConnector.md)



Defined in [`core/features/sequence_feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/sequence_feature.py).

Similar to `tfds.featuresSequenceDict`, but only contains a single feature.

Ex:
In `DatasetInfo`:

```
features=tfds.features.FeatureDict({
    'image': tfds.features.Image(),
    'labels': tfds.features.Sequence(tfds.features.ClassLabel(num_classes=5)),
})
```

At generation time:

```
yield {
    'image': 'path/to/img.png',
    'labels': [0, 3, 3, 2, 4],
}
```

Note that the underlying feature attributes can be accessed directly through
the sequence.

```
builder.info.features['labels'].names
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    feature,
    **kwargs
)
```

Construct a sequence from a specific feature.

#### Args:

* <b>`feature`</b>: <a href="../../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a>, The feature to wrap as sequence
* <b>`**kwargs`</b>: Same additional arguments as for <a href="../../tfds/features/SequenceDict.md"><code>tfds.features.SequenceDict</code></a>,
    like `length`.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Return the dtype (or dict of dtype) of this FeatureConnector.

<h3 id="serialized_keys"><code>serialized_keys</code></h3>

List of the flattened feature keys after serialization.

<h3 id="shape"><code>shape</code></h3>

Return the shape (or dict of shape) of this FeatureConnector.



## Methods

<h3 id="__getattr__"><code>__getattr__</code></h3>

``` python
__getattr__(key)
```

Allow to access the underlying attributes directly.

<h3 id="decode_example"><code>decode_example</code></h3>

``` python
decode_example(tfexample_data)
```

Wrapper around SequenceDict.

<h3 id="encode_example"><code>encode_example</code></h3>

``` python
encode_example(example_data)
```

Wrapper around SequenceDict.

<h3 id="get_serialized_info"><code>get_serialized_info</code></h3>

``` python
get_serialized_info()
```



<h3 id="get_tensor_info"><code>get_tensor_info</code></h3>

``` python
get_tensor_info()
```



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



