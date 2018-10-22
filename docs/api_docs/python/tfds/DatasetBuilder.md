<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.DatasetBuilder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_dataset"/>
<meta itemprop="property" content="download_and_prepare"/>
<meta itemprop="property" content="numpy_iterator"/>
<meta itemprop="property" content="name"/>
</div>

# tfds.DatasetBuilder

## Class `DatasetBuilder`



Abstract base class for datasets.

Typical usage:

```python
mnist_builder = tfds.MNIST(data_dir="~/tfds_data")
mnist_builder.download_and_prepare()
train_dataset = mnist_builder.as_dataset(tfds.Split.TRAIN)
assert isinstance(train_dataset, tf.data.Dataset)

# And then the rest of your input pipeline
train_dataset = train_dataset.repeat().shuffle(1024).batch(128).prefetch(4)
features = train_dataset.make_one_shot_iterator().get_next()
image, label = features['input'], features['target']
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Construct a DatasetBuilder.

Callers must pass arguments as keyword arguments.

#### Args:

data_dir (str): directory to read/write data.
  Optional, useful for testing.



## Methods

<h3 id="as_dataset"><code>as_dataset</code></h3>

``` python
as_dataset(
    *args,
    **kwargs
)
```

Constructs a `tf.data.Dataset`.

Callers must pass arguments as keyword arguments.

Subclasses must override _as_dataset.

#### Args:

* <b>`split`</b>: <a href="../tfds/Split.md"><code>tfds.Split</code></a>, which subset of the data to read.
* <b>`shuffle_files`</b>: `bool` (optional), whether to shuffle the input files.
    Defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.


#### Returns:

`tf.data.Dataset`

<h3 id="download_and_prepare"><code>download_and_prepare</code></h3>

``` python
download_and_prepare(
    *args,
    **kwargs
)
```

Downloads and prepares dataset for reading.

Subclasses must override _download_and_prepare.

#### Args:

cache_dir (str): Cached directory where to extract the data. If None,
  a default tmp directory will be used.
dl_manager (DownloadManager): DownloadManager to use. Only one of
  dl_manager and cache_dir can be set


#### Raises:

* <b>`ValueError`</b>: If the user defines both cache_dir and dl_manager

<h3 id="numpy_iterator"><code>numpy_iterator</code></h3>

``` python
numpy_iterator(**as_dataset_kwargs)
```

Generates numpy elements from the given <a href="../tfds/Split.md"><code>tfds.Split</code></a>.

This generator can be useful for non-TensorFlow programs.

#### Args:

* <b>`**as_dataset_kwargs`</b>: Keyword arguments passed on to
    <a href="../tfds/DatasetBuilder.md#as_dataset"><code>tfds.DatasetBuilder.as_dataset</code></a>.


#### Returns:

Generator yielding feature dictionaries
`dict<str feature_name, numpy.array feature_val>`.



## Class Members

<h3 id="name"><code>name</code></h3>

