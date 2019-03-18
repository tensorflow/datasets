<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.TFRecordExampleAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="write_from_generator"/>
</div>

# tfds.file_adapter.TFRecordExampleAdapter

## Class `TFRecordExampleAdapter`

Inherits From: [`FileFormatAdapter`](../../tfds/file_adapter/FileFormatAdapter.md)



Defined in [`core/file_format_adapter.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py).

Writes/Reads serialized Examples protos to/from TFRecord files.

Constraints on generators:

* The generator must yield feature dictionaries (`dict<str feature_name,
  feature_value>`).
* The allowed feature types are `int`, `float`, and `str` (or `bytes` in
  Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(example_reading_spec)
```

Construct a TFRecordExampleAdapter.

#### Args:

example_reading_spec (dict): feature name to tf.FixedLenFeature or
  tf.VarLenFeature. Passed to tf.parse_single_example.



## Properties

<h3 id="filetype_suffix"><code>filetype_suffix</code></h3>





## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

``` python
dataset_from_filename(filename)
```



<h3 id="write_from_generator"><code>write_from_generator</code></h3>

``` python
write_from_generator(
    generator_fn,
    output_files
)
```





