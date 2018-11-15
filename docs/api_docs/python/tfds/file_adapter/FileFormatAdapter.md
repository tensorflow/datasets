<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.FileFormatAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="write_from_generator"/>
</div>

# tfds.file_adapter.FileFormatAdapter

## Class `FileFormatAdapter`





Defined in [`core/file_format_adapter.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py).

Provides writing and reading methods for a file format.

## Properties

<h3 id="filetype_suffix"><code>filetype_suffix</code></h3>

Returns a str file type suffix (e.g. "csv").



## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

``` python
dataset_from_filename(filename)
```

Returns a `tf.data.Dataset` whose elements are dicts given a filename.

<h3 id="write_from_generator"><code>write_from_generator</code></h3>

``` python
write_from_generator(
    generator_fn,
    output_files
)
```

Write to files from generators_and_filenames.

#### Args:

* <b>`generator_fn`</b>: returns generator yielding dictionaries of feature name to
    value.
  output_files (list<str>): output files to write records to.



