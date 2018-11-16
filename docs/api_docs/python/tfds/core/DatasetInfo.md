<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.DatasetInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="features"/>
<meta itemprop="property" content="splits"/>
<meta itemprop="property" content="supervised_keys"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="update_from_metadata_dir"/>
</div>

# tfds.core.DatasetInfo

## Class `DatasetInfo`





Defined in [`core/dataset_info.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py).

Structure defining the info of the dataset.

Information on the datasets are available through the builder.info property.
Properties:
  features (FeaturesDict): Information on the feature dict of the
    `tf.data.Dataset()` object from the `builder.as_dataset()` method.
  splits (SplitDict): Available Splits for this dataset

Note that some of those fields are dynamically computed at data generation
time (ex: num_samples) and will be updated by update_from_metadata_dir().

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    features,
    supervised_keys=None
)
```

Constructor of the DatasetInfo.

#### Args:

* <b>`features`</b>: (<a href="../../tfds/features/FeaturesDict.md"><code>tfds.features.FeaturesDict</code></a>) Information on the feature dict
    of the `tf.data.Dataset()` object from the `builder.as_dataset()`
    method.
* <b>`supervised_keys`</b>: (`tuple`) Specifies the input feature and the
    label for supervised learning, if applicable for the dataset.



## Properties

<h3 id="features"><code>features</code></h3>



<h3 id="splits"><code>splits</code></h3>



<h3 id="supervised_keys"><code>supervised_keys</code></h3>





## Methods

<h3 id="update_from_metadata_dir"><code>update_from_metadata_dir</code></h3>

``` python
update_from_metadata_dir(metadata_dir)
```

Update the DatasetInfo properties from the metadata file.

This function update all the dynamically generated fields (num_samples,
hash, time of creation,...) of the DatasetInfo. This reads the metadata
file on the dataset directory to extract the info and expose them.
This function is called after the data has been generated in
.download_and_prepare() and when the data is loaded and already exists.

This will overwrite all previous metadata.

#### Args:

* <b>`metadata_dir`</b>: (str) The directory containing the metadata file. This
    should be the root directory of a specific dataset version.



