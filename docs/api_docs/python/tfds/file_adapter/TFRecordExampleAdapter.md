<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.TFRecordExampleAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="write_from_generator"/>
<meta itemprop="property" content="write_from_pcollection"/>
</div>

# tfds.file_adapter.TFRecordExampleAdapter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

## Class `TFRecordExampleAdapter`

Writes/Reads serialized Examples protos to/from TFRecord files.

Inherits From: [`FileFormatAdapter`](../../tfds/file_adapter/FileFormatAdapter.md)

<!-- Placeholder for "Used in" -->

Constraints on generators:

* The generator must yield feature dictionaries (`dict<str feature_name,
  feature_value>`).
* The allowed feature types are `int`, `float`, and `str` (or `bytes` in
  Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

```python
__init__(example_specs)
```

## Properties

<h3 id="filetype_suffix"><code>filetype_suffix</code></h3>

## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

```python
dataset_from_filename(filename)
```

<h3 id="write_from_generator"><code>write_from_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

```python
write_from_generator(
    generator,
    output_files
)
```

<h3 id="write_from_pcollection"><code>write_from_pcollection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

``` python
write_from_pcollection(
    pcollection,
    file_path_prefix,
    num_shards
)
```
