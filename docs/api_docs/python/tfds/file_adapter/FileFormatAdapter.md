<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.FileFormatAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="write_from_generator"/>
<meta itemprop="property" content="write_from_pcollection"/>
</div>

# tfds.file_adapter.FileFormatAdapter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

## Class `FileFormatAdapter`

Provides writing and reading methods for a file format.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

```python
__init__(example_specs)
```

Constructor.

#### Args:

*   <b>`example_specs`</b>: Nested `dict` of
    <a href="../../tfds/features/TensorInfo.md"><code>tfds.features.TensorInfo</code></a>,
    corresponding to the structure of data to write/read.

## Properties

<h3 id="filetype_suffix"><code>filetype_suffix</code></h3>

Returns a str file type suffix (e.g. "tfrecord").

## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

``` python
dataset_from_filename(filename)
```

Returns a `tf.data.Dataset` whose elements are dicts given a filename.

<h3 id="write_from_generator"><code>write_from_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

```python
write_from_generator(
    generator,
    output_files
)
```

Write to files from generators_and_filenames.

#### Args:

*   <b>`generator`</b>: generator yielding dictionaries of feature name to
    value.
*   <b>`output_files`</b>: `list<str>`, output files to write files to.

<h3 id="write_from_pcollection"><code>write_from_pcollection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

``` python
write_from_pcollection(
    pcollection,
    file_path_prefix=None,
    num_shards=None
)
```

Write the PCollection to file.

#### Args:

*   <b>`pcollection`</b>: `beam.PCollection`, the PCollection containing the
    examples to write.
*   <b>`file_path_prefix`</b>: `str`, output files to write files to.
*   <b>`num_shards`</b>: `int`,
