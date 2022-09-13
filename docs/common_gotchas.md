# Common implementation gotchas

This page describe the common implementation gotcha when implementing a new
dataset.

## Legacy `SplitGenerator` should be avoided

The old `tfds.core.SplitGenerator` API is deprecated.

```python
def _split_generator(...):
  return [
      tfds.core.SplitGenerator(name='train', gen_kwargs={'path': train_path}),
      tfds.core.SplitGenerator(name='test', gen_kwargs={'path': test_path}),
  ]
```

Should be replaced by:

```python
def _split_generator(...):
  return {
      'train': self._generate_examples(path=train_path),
      'test': self._generate_examples(path=test_path),
  }
```

**Rationale**: The new API is less verbose and more explicit. The old API will
be removed in future version.

## New datasets should be self-contained in a folder

When adding a dataset inside the `tensorflow_datasets/` repository, please make
sure to follow the dataset-as-folder structure (all checksums, dummy data,
implementation code self-contained in a folder).

*   Old datasets (bad): `<category>/<ds_name>.py`
*   New datasets (good): `<category>/<ds_name>/<ds_name>.py`

Use the
[TFDS CLI](https://www.tensorflow.org/datasets/cli#tfds_new_implementing_a_new_dataset)
(`tfds new`, or `gtfds new` for googlers) to generate the template.

**Rationale**: Old structure required absolute paths for checksums, fake data
and was distributing the dataset files in many places. It was making it harder
to implement datasets outside the TFDS repository. For consistency, the new
structure should be used everywhere now.

## Description lists should be formatted as markdown

The `DatasetInfo.description` `str` is formatted as markdown. Markdown lists
require an empty line before the first item:

```python
_DESCRIPTION = """
Some text.
                      # << Empty line here !!!
1. Item 1
2. Item 1
3. Item 1
                      # << Empty line here !!!
Some other text.
"""
```

**Rationale**: Badly formatted description create visual artifacts in our
catalog documentation. Without the empty lines, the above text would be rendered
as:

Some text. 1. Item 1 2. Item 1 3. Item 1 Some other text

## Forgot ClassLabel names

When using `tfds.features.ClassLabel`, try to provide the human-readable labels
`str` with `names=` or `names_file=` (instead of `num_classes=10`).

```python
features = {
    'label': tfds.features.ClassLabel(names=['dog', 'cat', ...]),
}
```

**Rationale**: Human readable labels are used in many places:

*   Allow to yield `str` directly in `_generate_examples`: `yield {'label':
    'dog'}`
*   Exposed in the users like `info.features['label'].names` (conversion method
    `.str2int('dog')`,... also available)
*   Used in the
    [visualization utils](https://www.tensorflow.org/datasets/overview#tfdsas_dataframe)
    `tfds.show_examples`, `tfds.as_dataframe`

## Forgot image shape

When using `tfds.features.Image`, `tfds.features.Video`, if the images have
static shape, they should be explicitly specified:

```python
features = {
    'image': tfds.features.Image(shape=(256, 256, 3)),
}
```

**Rationale**: It allow static shape inference (e.g.
`ds.element_spec['image'].shape`), which is required for batching (batching
images of unknown shape would require resizing them first).

## Prefer more specific type instead of `tfds.features.Tensor`

When possible, prefer the more specific types `tfds.features.ClassLabel`,
`tfds.features.BBoxFeatures`,... instead of the generic `tfds.features.Tensor`.

**Rationale**: In addition of being more semantically correct, specific features
provides additional metadata to users and are detected by tools.

## Lazy imports in global space

Lazy imports should not be called from the global space. For example the
following is wrong:

```python
tfds.lazy_imports.apache_beam # << Error: Import beam in the global scope

def f() -> beam.Map:
  ...
```

**Rationale**: Using lazy imports in the global scope would import the module
for all tfds users, defeating the purpose of lazy imports.

## Dynamically computing train/test splits

If the dataset does not provide official splits, neither should TFDS. The
following should be avoided:

```python
_TRAIN_TEST_RATIO = 0.7

def _split_generator():
  ids = list(range(num_examples))
  np.random.RandomState(seed).shuffle(ids)

  # Split train/test
  train_ids = ids[_TRAIN_TEST_RATIO * num_examples:]
  test_ids = ids[:_TRAIN_TEST_RATIO * num_examples]
  return {
      'train': self._generate_examples(train_ids),
      'test': self._generate_examples(test_ids),
  }
```

**Rationale**: TFDS try to provide datasets as close as the original data. The
[sub-split API](https://www.tensorflow.org/datasets/splits) should be used
instead to let users dynamically create the subsplits they want:

```python
ds_train, ds_test = tfds.load(..., split=['train[:80%]', 'train[80%:]'])
```

## Python style guide

### Prefer to use pathlib API

Instead of the `tf.io.gfile` API, it is preferable to use the
[pathlib API](https://docs.python.org/3/library/pathlib.html). All `dl_manager`
methods returns pathlib-like objects compatible with GCS, S3,...

```python
path = dl_manager.download_and_extract('http://some-website/my_data.zip')

json_path = path / 'data/file.json'

json.loads(json_path.read_text())
```

**Rationale**: pathlib API is a modern object oriented file API which remove
boilerplate. Using `.read_text()` / `.read_bytes()` also guarantee the files are
correctly closed.

### If the method is not using `self`, it should be a function

If a class method is not using `self`, it should be a simple function (defined
outside the class).

**Rationale**: It makes it explicit to the reader that the function do not have
side effects, nor hidden input/output:

```python
x = f(y)  # Clear inputs/outputs

x = self.f(y)  # Does f depend on additional hidden variables ? Is it stateful ?
```
