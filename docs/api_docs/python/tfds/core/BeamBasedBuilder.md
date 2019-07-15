<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.BeamBasedBuilder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="builder_config"/>
<meta itemprop="property" content="data_dir"/>
<meta itemprop="property" content="info"/>
<meta itemprop="property" content="version"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_dataset"/>
<meta itemprop="property" content="download_and_prepare"/>
<meta itemprop="property" content="BUILDER_CONFIGS"/>
<meta itemprop="property" content="SUPPORTED_VERSIONS"/>
<meta itemprop="property" content="VERSION"/>
<meta itemprop="property" content="builder_configs"/>
<meta itemprop="property" content="name"/>
</div>

# tfds.core.BeamBasedBuilder

## Class `BeamBasedBuilder`

Beam based Builder.

<a target="_blank" href=https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py>View
source</a>

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href=https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py>View
source</a>

```python
__init__(
    data_dir=None,
    config=None,
    version=None
)
```

Constructs a DatasetBuilder.

Callers must pass arguments as keyword arguments.

#### Args:

*   <b>`data_dir`</b>: `str`, directory to read/write data. Defaults to
    datasets are stored.
*   <b>`config`</b>:
    <a href="../../tfds/core/BuilderConfig.md"><code>tfds.core.BuilderConfig</code></a>
    or `str` name, optional configuration for the dataset that affects the data
    generated on disk. Different `builder_config`s will have their own
    subdirectories and versions.
*   <b>`version`</b>: `str`. Optional version at which to load the dataset. An
    error is raised if specified version cannot be satisfied. Eg: '1.2.3',
    '1.2.*'. The special value "experimental_latest" will use the highest
    version, even if not default. This is not recommended unless you know what
    you are doing, as the version could be broken.

## Properties

<h3 id="builder_config"><code>builder_config</code></h3>

<a href="../../tfds/core/BuilderConfig.md"><code>tfds.core.BuilderConfig</code></a> for this builder.

<h3 id="data_dir"><code>data_dir</code></h3>

<h3 id="info"><code>info</code></h3>

<a href="../../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a> for this builder.

<h3 id="version"><code>version</code></h3>

## Methods

<h3 id="as_dataset"><code>as_dataset</code></h3>

<a target="_blank" href=https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py>View
source</a>

```python
as_dataset(
    split=None,
    batch_size=None,
    shuffle_files=None,
    as_supervised=False,
    in_memory=None
)
```

Constructs a `tf.data.Dataset`.

Callers must pass arguments as keyword arguments.

#### Args:

*   <b>`split`</b>:
    <a href="../../tfds/core/SplitBase.md"><code>tfds.core.SplitBase</code></a>,
    which subset(s) of the data to read. If None (default), returns all splits
    in a dict `<key: tfds.Split, value: tf.data.Dataset>`.
*   <b>`batch_size`</b>: `int`, batch size. Note that variable-length features
    will be 0-padded if `batch_size` is set. Users that want more custom
    behavior should use `batch_size=None` and use the `tf.data` API to construct
    a custom pipeline. If `batch_size == -1`, will return feature dictionaries
    of the whole dataset with `tf.Tensor`s instead of a `tf.data.Dataset`.
*   <b>`shuffle_files`</b>: `bool`, whether to shuffle the input files. Defaults
    to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.
*   <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default, the returned
    `tf.data.Dataset` will have a dictionary with all the features.
*   <b>`in_memory`</b>: `bool`, if `True`, loads the dataset in memory which
    increases iteration speeds. Note that if `True` and the dataset has unknown
    dimensions, the features will be padded to the maximum size across the
    dataset.

#### Returns:

`tf.data.Dataset`, or if `split=None`, `dict<key: tfds.Split, value:
tfds.data.Dataset>`.

If `batch_size` is -1, will return feature dictionaries containing
the entire dataset in `tf.Tensor`s instead of a `tf.data.Dataset`.

<h3 id="download_and_prepare"><code>download_and_prepare</code></h3>

<a target="_blank" href=https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py>View
source</a>

``` python
download_and_prepare(
    download_dir=None,
    download_config=None
)
```

Downloads and prepares dataset for reading.

#### Args:

*   <b>`download_dir`</b>: `str`, directory where downloaded files are stored.
    Defaults to "~/tensorflow-datasets/downloads".
*   <b>`download_config`</b>:
    <a href="../../tfds/download/DownloadConfig.md"><code>tfds.download.DownloadConfig</code></a>,
    further configuration for downloading and preparing dataset.

#### Raises:

* <b>`IOError`</b>: if there is not enough disk space available.



## Class Members

*   `BUILDER_CONFIGS` <a id="BUILDER_CONFIGS"></a>
*   `SUPPORTED_VERSIONS` <a id="SUPPORTED_VERSIONS"></a>
*   `VERSION = None` <a id="VERSION"></a>
*   `builder_configs` <a id="builder_configs"></a>
*   `name = 'beam_based_builder'` <a id="name"></a>
