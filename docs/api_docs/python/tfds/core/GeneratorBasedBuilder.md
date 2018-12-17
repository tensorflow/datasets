<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.GeneratorBasedBuilder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="builder_config"/>
<meta itemprop="property" content="info"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_dataset"/>
<meta itemprop="property" content="as_numpy"/>
<meta itemprop="property" content="download_and_prepare"/>
<meta itemprop="property" content="BUILDER_CONFIGS"/>
<meta itemprop="property" content="VERSION"/>
<meta itemprop="property" content="builder_configs"/>
<meta itemprop="property" content="name"/>
</div>

# tfds.core.GeneratorBasedBuilder

## Class `GeneratorBasedBuilder`

Inherits From: [`DatasetBuilder`](../../tfds/core/DatasetBuilder.md)



Defined in [`core/dataset_builder.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py).

Base class for datasets with data generation based on dict generators.

`GeneratorBasedBuilder` is a convenience class that abstracts away much
of the data writing and reading of `DatasetBuilder`. It expects subclasses to
implement generators of feature dictionaries across the dataset splits
(`_split_generators`) and to specify a file type
(`_file_format_adapter`). See the method docstrings for details.

Minimally, subclasses must override `_split_generators` and
`_file_format_adapter`.

`FileFormatAdapter`s are defined in
`tensorflow_datasets.core.file_format_adapter` and specify constraints on the
feature dictionaries yielded by example generators. See the class docstrings.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(**kwargs)
```

Builder constructor.

#### Args:

* <b>`**kwargs`</b>: Constructor kwargs forwarded to DatasetBuilder



## Properties

<h3 id="builder_config"><code>builder_config</code></h3>



<h3 id="info"><code>info</code></h3>

Return the dataset info object. See `DatasetInfo` for details.



## Methods

<h3 id="as_dataset"><code>as_dataset</code></h3>

``` python
as_dataset(
    split,
    batch_size=1,
    shuffle_files=None,
    as_supervised=False
)
```

Constructs a `tf.data.Dataset`.

Callers must pass arguments as keyword arguments.

Subclasses must override _as_dataset.

#### Args:

* <b>`split`</b>: <a href="../../tfds/Split.md"><code>tfds.Split</code></a>, which subset of the data to read.
* <b>`batch_size`</b>: `int`, batch size. Note that variable-length features will
    be 0-padded if `batch_size > 1`. Users that want more custom behavior
    should use `batch_size=1` and use the `tf.data` API to construct a
    custom pipeline.
* <b>`shuffle_files`</b>: `bool` (optional), whether to shuffle the input files.
    Defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.
* <b>`as_supervised`</b>: `bool`, if `True`, the returned `tf.data.Dataset`
    will have a 2-tuple structure `(input, label)` according to
    `builder.info.supervised_keys`. If `False`, the default,
    the returned `tf.data.Dataset` will have a dictionary with all the
    features.


#### Returns:

`tf.data.Dataset`

<h3 id="as_numpy"><code>as_numpy</code></h3>

``` python
as_numpy(
    batch_size=1,
    **as_dataset_kwargs
)
```

Generates batches of NumPy arrays from the given <a href="../../tfds/Split.md"><code>tfds.Split</code></a>.

#### Args:

* <b>`batch_size`</b>: `int`, batch size for the NumPy arrays. If -1 or None,
    `as_numpy` will return the full dataset at once, each feature having its
    own array.
* <b>`**as_dataset_kwargs`</b>: Keyword arguments passed on to
    <a href="../../tfds/core/DatasetBuilder.md#as_dataset"><code>tfds.core.DatasetBuilder.as_dataset</code></a>.


#### Yields:

Feature dictionaries
`dict<str feature_name, numpy.array feature_val>`.

If `batch_size` is -1 or None, will return a single dictionary containing
the entire dataset instead of yielding batches.

<h3 id="download_and_prepare"><code>download_and_prepare</code></h3>

``` python
download_and_prepare(
    download_dir=None,
    extract_dir=None,
    manual_dir=None,
    mode=None,
    compute_stats=True
)
```

Downloads and prepares dataset for reading.

Subclasses must override _download_and_prepare.

#### Args:

* <b>`download_dir`</b>: `str`, directory where downloaded files are stored.
    Defaults to "~/tensorflow-datasets/downloads".
* <b>`extract_dir`</b>: `str`, directory where extracted files are stored.
    Defaults to "~/tensorflow-datasets/extracted".
* <b>`manual_dir`</b>: `str`, read-only directory where manually downloaded/extracted
    data is stored. Defaults to
    "~/tensorflow-datasets/manual/{dataset_name}".
* <b>`mode`</b>: <a href="../../tfds/download/GenerateMode.md"><code>tfds.GenerateMode</code></a>: Mode to FORCE_REDOWNLOAD,
    or REUSE_DATASET_IF_EXISTS. Defaults to REUSE_DATASET_IF_EXISTS.
* <b>`compute_stats`</b>: `boolean` If True, compute statistics over the generated
    data and write the <a href="../../tfds/core/DatasetInfo.md"><code>tfds.core.DatasetInfo</code></a> protobuf to disk.


#### Raises:

* <b>`ValueError`</b>: If the user defines both cache_dir and dl_manager



## Class Members

<h3 id="BUILDER_CONFIGS"><code>BUILDER_CONFIGS</code></h3>

<h3 id="VERSION"><code>VERSION</code></h3>

<h3 id="builder_configs"><code>builder_configs</code></h3>

<h3 id="name"><code>name</code></h3>

