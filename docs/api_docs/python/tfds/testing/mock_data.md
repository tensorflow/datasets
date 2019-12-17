<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing.mock_data" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.testing.mock_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Mock tfds to generate random data.

```python
tfds.testing.mock_data(
    *args,
    **kwds
)
```

<!-- Placeholder for "Used in" -->

This function requires the true metadata files (dataset_info.json, label.txt,
vocabulary files) to be stored in `data_dir/dataset_name/version`, as they would
be for the true dataset. The actual examples will be randomly generated using
`builder.info.features.get_tensor_info()`. Download and prepare step will be
skipped.

Warning: As the mocked builder will use the true metadata (label names,...), the
`info.split['train'].num_examples` won't match `len(list(ds_train))`.

Usage (automated):

```
with mock_data(num_examples=5):
  ds = tfds.load('some_dataset', split='train')

  for ex in ds:  # ds will yield randomly generated examples.
    ex
```

The examples will be deterministically generated. Train and test split will
yield the same examples.

If you want more fine grain control over the generated examples, you can
manually overwrite the `DatasetBuilder._as_dataset` method. Usage (manual):

```
def as_dataset(self, *args, **kwargs):
  return tf.data.Dataset.from_generator(
      lambda: ({
          'image': np.ones(shape=(28, 28, 1), dtype=np.uint8),
          'label': i % 10,
      } for i in range(num_examples)),
      output_types=self.info.features.dtype,
      output_shapes=self.info.features.shape,
  )

with mock_data(as_dataset_fn=as_dataset):
  ds = tfds.load('some_dataset', split='train')

  for ex in ds:  # ds will yield the fake data example of 'as_dataset'.
    ex
```

#### Args:

*   <b>`num_examples`</b>: `int`, the number of fake example to generate.
*   <b>`as_dataset_fn`</b>: if provided, will replace the default random example
    generator. This function mock the `FileAdapterBuilder._as_dataset`
*   <b>`data_dir`</b>: `str`, `data_dir` folder from where to load the metadata.
    Will overwrite `data_dir` kwargs from
    <a href="../../tfds/load.md"><code>tfds.load</code></a>.

#### Yields:

None
