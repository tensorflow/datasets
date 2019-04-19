<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.file_adapter



Defined in [`core/file_format_adapter.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py).

<!-- Placeholder for "Used in" -->

<a href="../tfds/file_adapter/FileFormatAdapter.md"><code>tfds.file_adapter.FileFormatAdapter</code></a>s for GeneratorBasedBuilder.

FileFormatAdapters implement methods to write and read data from a
particular file format.

Currently, two FileAdapter are available:
 * TFRecordExampleAdapter: To store the pre-processed dataset as .tfrecord file
 * CSVAdapter: To store the dataset as CSV file

```python
return TFRecordExampleAdapter({
    "x": tf.FixedLenFeature(tuple(), tf.int64)
})
```

## Classes

[`class FileFormatAdapter`](../tfds/file_adapter/FileFormatAdapter.md): Provides writing and reading methods for a file format.

[`class TFRecordExampleAdapter`](../tfds/file_adapter/TFRecordExampleAdapter.md): Writes/Reads serialized Examples protos to/from TFRecord files.

[`class CSVAdapter`](../tfds/file_adapter/CSVAdapter.md): Writes/reads features to/from CSV files.

