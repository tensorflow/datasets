<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing.DummyDatasetSharedGenerator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="builder_config"/>
<meta itemprop="property" content="data_dir"/>
<meta itemprop="property" content="info"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_dataset"/>
<meta itemprop="property" content="download_and_prepare"/>
<meta itemprop="property" content="BUILDER_CONFIGS"/>
<meta itemprop="property" content="GOOGLE_DISABLED"/>
<meta itemprop="property" content="IN_DEVELOPMENT"/>
<meta itemprop="property" content="VERSION"/>
<meta itemprop="property" content="builder_configs"/>
<meta itemprop="property" content="name"/>
</div>

# tfds.testing.DummyDatasetSharedGenerator

## Class `DummyDatasetSharedGenerator`

Inherits From: [`GeneratorBasedBuilder`](../../tfds/core/GeneratorBasedBuilder.md)



Defined in [`testing/test_utils.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_utils.py).

Test DatasetBuilder.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(**kwargs)
```

Builder constructor.

#### Args:

* <b>`**kwargs`</b>: Constructor kwargs forwarded to DatasetBuilder



## Properties

<h3 id="builder_config"><code>builder_config</code></h3>

<a href="../../tfds/core/BuilderConfig.md"><code>tfds.core.BuilderConfig</code></a> for this builder.

<h3 id="data_dir"><code>data_dir</code></h3>



<h3 id="info"><code>info</code></h3>

<a href="../../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a> for this builder.



## Methods

<h3 id="as_dataset"><code>as_dataset</code></h3>

``` python
as_dataset(
    split=None,
    batch_size=1,
    shuffle_files=None,
    as_supervised=False
)
```

Constructs a `tf.data.Dataset`.

Callers must pass arguments as keyword arguments.

#### Args:

* <b>`split`</b>: <a href="../../tfds/core/SplitBase.md"><code>tfds.core.SplitBase</code></a>, which subset(s) of the data to read. If None
    (default), returns all splits in a dict
    `<key: tfds.Split, value: tf.data.Dataset>`.
* <b>`batch_size`</b>: `int`, batch size. Note that variable-length features will
    be 0-padded if `batch_size > 1`. Users that want more custom behavior
    should use `batch_size=1` and use the `tf.data` API to construct a
    custom pipeline. If `batch_size == -1`, will return feature
    dictionaries of the whole dataset with `tf.Tensor`s instead of a
    `tf.data.Dataset`.
* <b>`shuffle_files`</b>: `bool`, whether to shuffle the input files.
    Defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.
* <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default,
    the returned `tf.data.Dataset` will have a dictionary with all the
    features.


#### Returns:

`tf.data.Dataset`, or if `split=None`, `dict<key: tfds.Split, value:
tfds.data.Dataset>`.

If `batch_size` is -1, will return feature dictionaries containing
the entire dataset in `tf.Tensor`s instead of a `tf.data.Dataset`.

<h3 id="download_and_prepare"><code>download_and_prepare</code></h3>

``` python
download_and_prepare(
    download_dir=None,
    download_config=None
)
```

Downloads and prepares dataset for reading.

#### Args:

* <b>`download_dir`</b>: `str`, directory where downloaded files are stored.
    Defaults to "~/tensorflow-datasets/downloads".
* <b>`download_config`</b>: <a href="../../tfds/download/DownloadConfig.md"><code>tfds.download.DownloadConfig</code></a>, further configuration for
    downloading and preparing dataset.



## Class Members

<h3 id="BUILDER_CONFIGS"><code>BUILDER_CONFIGS</code></h3>

<h3 id="GOOGLE_DISABLED"><code>GOOGLE_DISABLED</code></h3>

<h3 id="IN_DEVELOPMENT"><code>IN_DEVELOPMENT</code></h3>

<h3 id="VERSION"><code>VERSION</code></h3>

<h3 id="builder_configs"><code>builder_configs</code></h3>

<h3 id="name"><code>name</code></h3>

