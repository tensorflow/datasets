<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.file_adapter

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py">View
source</a>

<a href="../tfds/file_adapter/FileFormatAdapter.md"><code>tfds.file_adapter.FileFormatAdapter</code></a>s
for GeneratorBasedBuilder.

FileFormatAdapters implement methods to write and read data from a
particular file format.

Currently, a single FileAdapter is available: * TFRecordExampleAdapter: To store
the pre-processed dataset as .tfrecord file

```python
return TFRecordExampleAdapter({
    "x": tf.FixedLenFeature(tuple(), tf.int64)
})
```

## Classes

[`class FileFormatAdapter`](../tfds/file_adapter/FileFormatAdapter.md): Provides writing and reading methods for a file format.

[`class TFRecordExampleAdapter`](../tfds/file_adapter/TFRecordExampleAdapter.md): Writes/Reads serialized Examples protos to/from TFRecord files.
