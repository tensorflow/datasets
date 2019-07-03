<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.download

<a href="../tfds/download/DownloadManager.md"><code>tfds.download.DownloadManager</code></a>
API.

Defined in [`core/download/__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/__init__.py).

<!-- Placeholder for "Used in" -->


## Classes

[`class ComputeStatsMode`](../tfds/download/ComputeStatsMode.md): Mode to decide
if dynamic dataset info fields should be computed or not.

[`class DownloadConfig`](../tfds/download/DownloadConfig.md): Configuration for <a href="../tfds/core/DatasetBuilder.md#download_and_prepare"><code>tfds.core.DatasetBuilder.download_and_prepare</code></a>.

[`class DownloadManager`](../tfds/download/DownloadManager.md): Manages the download and extraction of files, as well as caching.

[`class ExtractMethod`](../tfds/download/ExtractMethod.md): The extraction
method to use to pre-process a downloaded file.

[`class GenerateMode`](../tfds/download/GenerateMode.md): `Enum` for how to treat pre-existing downloads and data.

[`class Resource`](../tfds/download/Resource.md): Represents a resource to download, extract, or both.

## Functions

[`iter_archive(...)`](../tfds/download/iter_archive.md): Yields (path_in_archive, f_obj) for archive at path using <a href="../tfds/download/ExtractMethod.md"><code>tfds.download.ExtractMethod</code></a>.

