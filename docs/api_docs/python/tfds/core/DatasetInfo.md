<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.DatasetInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="as_proto"/>
<meta itemprop="property" content="features"/>
<meta itemprop="property" content="initialized"/>
<meta itemprop="property" content="num_examples"/>
<meta itemprop="property" content="splits"/>
<meta itemprop="property" content="supervised_keys"/>
<meta itemprop="property" content="urls"/>
<meta itemprop="property" content="__getattr__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="compute_dynamic_properties"/>
<meta itemprop="property" content="read_from_directory"/>
<meta itemprop="property" content="write_to_directory"/>
</div>

# tfds.core.DatasetInfo

## Class `DatasetInfo`





Defined in [`core/dataset_info.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py).

Structure defining the info of the dataset.

Information on the datasets are available through the builder.info property.
Properties: name: `str`, name of this dataset. description: `str`, description
of this dataset. version: `str`, semantic version of the dataset (ex: '1.2.0')
features:
<a href="../../tfds/features/FeaturesDict.md"><code>tfds.features.FeaturesDict</code></a>:
Information on the feature dict of the `tf.data.Dataset` object from the
`builder.as_dataset()` method. splits: `SplitDict`, the available Splits for
this dataset. urls: `list(str)`, the homepage(s) for this dataset.
size_in_bytes: `integer`, approximate size in bytes of the raw size of the
dataset that we will be downloading from the internet. num_examples: `integer`,
number of examples across all splits. examples_per_split: `dict(string,
integer)`, number of examples per split.

Note that some of those fields are dynamically computed at data generation
time, and updated by `compute_dynamic_properties`.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    name=None,
    description=None,
    version=None,
    features=None,
    supervised_keys=None,
    splits=None,
    urls=None,
    size_in_bytes=0,
    citation=None
)
```

Constructor of the DatasetInfo.

#### Args:

*   <b>`name`</b>: (`str`) Name of the dataset, usually set to builder.name.
*   <b>`description`</b>: `str`, description of this dataset.
*   <b>`version`</b>: `str`, semantic version of the dataset (ex: '1.2.0')
*   <b>`features`</b>:
    (<a href="../../tfds/features/FeaturesDict.md"><code>tfds.features.FeaturesDict</code></a>)
    Information on the feature dict of the `tf.data.Dataset()` object from the
    `builder.as_dataset()` method.
*   <b>`supervised_keys`</b>: (`tuple`) Specifies the input feature and the
    label for supervised learning, if applicable for the dataset.
*   <b>`splits`</b>: `SplitDict`, the available Splits for this dataset.
*   <b>`urls`</b>: `list(str)`, optional, the homepage(s) for this dataset.
*   <b>`size_in_bytes`</b>: `integer`, optional, approximate size in bytes of
    the raw size of the dataset that we will be downloading from the internet.
*   <b>`citation`</b>: `str`, optional, the citation to use for this dataset.

## Properties

<h3 id="as_proto"><code>as_proto</code></h3>



<h3 id="features"><code>features</code></h3>



<h3 id="initialized"><code>initialized</code></h3>



<h3 id="num_examples"><code>num_examples</code></h3>



<h3 id="splits"><code>splits</code></h3>



<h3 id="supervised_keys"><code>supervised_keys</code></h3>



<h3 id="urls"><code>urls</code></h3>





## Methods

<h3 id="__getattr__"><code>__getattr__</code></h3>

```python
__getattr__(key)
```

<h3 id="compute_dynamic_properties"><code>compute_dynamic_properties</code></h3>

``` python
compute_dynamic_properties(builder)
```



<h3 id="read_from_directory"><code>read_from_directory</code></h3>

``` python
read_from_directory(dataset_info_dir)
```

Update the DatasetInfo properties from the metadata file.

This function updates all the dynamically generated fields (num_samples,
hash, time of creation,...) of the DatasetInfo. This reads the metadata
file on the dataset directory to extract the info and expose them.
This function is called after the data has been generated in
.download_and_prepare() and when the data is loaded and already exists.

This will overwrite all previous metadata.

#### Args:

* <b>`dataset_info_dir`</b>: `str` The directory containing the metadata file. This
    should be the root directory of a specific dataset version.

<h3 id="write_to_directory"><code>write_to_directory</code></h3>

``` python
write_to_directory(dataset_info_dir)
```





