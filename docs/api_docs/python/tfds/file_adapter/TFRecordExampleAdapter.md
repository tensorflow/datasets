<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.TFRecordExampleAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="parse_example"/>
<meta itemprop="property" content="serialize_example"/>
<meta itemprop="property" content="write_from_generator"/>
<meta itemprop="property" content="write_from_pcollection"/>
</div>

# tfds.file_adapter.TFRecordExampleAdapter

## Class `TFRecordExampleAdapter`

Writes/Reads serialized Examples protos to/from TFRecord files.

Inherits From: [`FileFormatAdapter`](../../tfds/file_adapter/FileFormatAdapter.md)



Defined in [`core/file_format_adapter.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py).

<!-- Placeholder for "Used in" -->

Constraints on generators:

* The generator must yield feature dictionaries (`dict<str feature_name,
  feature_value>`).
* The allowed feature types are `int`, `float`, and `str` (or `bytes` in
  Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.

<h2 id="__init__"><code>__init__</code></h2>

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

## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

``` python
dataset_from_filename(filename)
```

<h3 id="parse_example"><code>parse_example</code></h3>

```python
parse_example(serialized_example)
```

Deserialize a single `tf.train.Example` proto.

#### Usage:

```
ds = tf.data.TFRecordDataset(filepath)
ds = ds.map(file_adapter.parse_example)
```

#### Args:

*   <b>`serialized_example`</b>: `tf.Tensor`, the `tf.string` tensor containing
    the serialized proto to decode.

#### Returns:

*   <b>`example`</b>: A nested `dict` of `tf.Tensor` values. The structure and
    tensors shape/dtype match the `example_specs` provided at construction.

<h3 id="serialize_example"><code>serialize_example</code></h3>

```python
serialize_example(example)
```

Serialize the given example.

#### Args:

*   <b>`example`</b>: Nested `dict` containing the input to serialize. The input
    structure and values dtype/shape must match the `example_specs` provided at
    construction.

#### Returns:

*   <b>`serialize_proto`</b>: `str`, the serialized `tf.train.Example` proto

<h3 id="write_from_generator"><code>write_from_generator</code></h3>

``` python
write_from_generator(
    generator_fn,
    output_files
)
```

<h3 id="write_from_pcollection"><code>write_from_pcollection</code></h3>

``` python
write_from_pcollection(
    pcollection,
    file_path_prefix,
    num_shards
)
```
