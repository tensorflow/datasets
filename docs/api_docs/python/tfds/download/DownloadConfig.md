<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.DownloadConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tfds.download.DownloadConfig

## Class `DownloadConfig`





Defined in [`core/download/download_manager.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/download_manager.py).

Configuration for <a href="../../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    extract_dir=None,
    manual_dir=None,
    download_mode=None,
    compute_stats=None,
    max_examples_per_split=None,
    register_checksums=False
)
```

Constructs a `DownloadConfig`.

#### Args:

* <b>`extract_dir`</b>: `str`, directory where extracted files are stored.
    Defaults to "<download_dir>/extracted".
* <b>`manual_dir`</b>: `str`, read-only directory where manually downloaded/extracted
    data is stored. Defaults to
    "<download_dir>/manual".
* <b>`download_mode`</b>: <a href="../../tfds/download/GenerateMode.md"><code>tfds.GenerateMode</code></a>, how to deal with downloads or data
    that already exists. Defaults to `REUSE_DATASET_IF_EXISTS`, which will
    reuse both downloads and data if it already exists.
* <b>`compute_stats`</b>: `tfds.download.ComputeStats`, whether to compute
    statistics over the generated data. Defaults to `AUTO`.
* <b>`max_examples_per_split`</b>: `int`, optional max number of examples to write
    into each split.
* <b>`register_checksums`</b>: `bool`, defaults to False. If True, checksum of
    downloaded files are recorded.



