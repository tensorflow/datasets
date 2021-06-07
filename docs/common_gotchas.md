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

**Rational**: The new API is less verbose and more explicit. The old API will be
removed in future version.

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

**Rational**: Badly formatted description create visual artifacts in our catalog
documentation. Without the empty lines, the above text would be rendered as:

Some text. 1. Item 1 2. Item 1 3. Item 1 Some other text

## Forgot ClassLabel names

When using `tfds.features.ClassLabel`, try to provide the human-readable labels
`str` with `names=` or `names_file=` (instead of `num_classes=10`).

```python
features = {
    'label': tfds.features.ClassLabel(names=['dog', 'cat', ...]),
}
```

**Rational**: Human readable labels are used in many places:

*   Allow to yield `str` directly in `_generate_examples`: `yield {'label':
    'dog'}`
*   Exposed in the users like `info.features['label'].names` (conversion method
    `.str2int('dog')`,... also available)
*   Used in the
    [visualization utils](https://www.tensorflow.org/datasets/overview#tfdsas_dataframe)
    `tfds.show_examples`, `tfds.as_dataframe`

## Forgot image shape

When using `tfds.features.Image`, `tfds.features.Video`, if the images have
static shape, they should be expliclty specified:

```python
features = {
    'image': tfds.features.Image(shape=(256, 256, 3)),
}
```

**Rational**: It allow static shape inference (e.g.
`ds.element_spec['image'].shape`), which is required for batching (batching
images of unknown shape would require resizing them first).

## Prefer more specific type instead of `tfds.features.Tensor`

When possible, prefer the more specific types `tfds.features.ClassLabel`,
`tfds.features.BBoxFeatures`,... instead of the generic `tfds.features.Tensor`.

**Rational**: In addition of being more semantically correct, specific features
provides additional metadata to users and are detected by tools.

## Lazy imports in global space

Lazy imports should not be called from the global space. For example the
following is wrong:

```python
tfds.lazy_imports.apache_beam # << Error: Import beam in the global scope

def f() -> beam.Map:
  ...
```

**Rational**: Using lazy imports in the global scope would import the module for
all tfds users, defeating the purpose of lazy imports.

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

**Rational**: TFDS try to provide datasets as close as the original data. The
[sub-split API](https://www.tensorflow.org/datasets/splits ``) should be used
instead to let users dynamically create the subsplits they want:

```python
ds_train, ds_test = tfds.load(..., split=['train[:80%]', 'train[80%:]'])
```
