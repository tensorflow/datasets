<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="scan" />
  <meta itemprop="description" content="SCAN tasks with various splits.&#10;&#10;SCAN is a set of simple language-driven navigation tasks for studying&#10;compositional learning and zero-shot generalization.&#10;&#10;See https://github.com/brendenlake/SCAN for a description of the splits.&#10;&#10;Example usage:&#10;data = tfds.load('scan/length')&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('scan', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scan" />
  <meta itemprop="sameAs" content="https://github.com/brendenlake/SCAN" />
  <meta itemprop="citation" content="&#10;@inproceedings{Lake2018GeneralizationWS,&#10;  title={Generalization without Systematicity: On the Compositional Skills of&#10;         Sequence-to-Sequence Recurrent Networks},&#10;  author={Brenden M. Lake and Marco Baroni},&#10;  booktitle={ICML},&#10;  year={2018},&#10;  url={https://arxiv.org/pdf/1711.00350.pdf},&#10;}&#10;" />
</div>

# `scan`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   URL:
    [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)
*   `DatasetBuilder`:
    [`tfds.text.scan.Scan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/scan.py)

`scan` is configured with `tfds.text.scan.ScanConfig` and has the following
configurations predefined (defaults to the first one):

*   `simple` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `addprim_jump` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `addprim_turn_left` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `filler_num0` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `filler_num1` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `filler_num2` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `filler_num3` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `length` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `template_around_right` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with
    various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `template_jump_around_right` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with
    various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `template_opposite_right` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with
    various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

*   `template_right` (`v1.0.0`) (`Size: 17.82 MiB`): SCAN tasks with various
    splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

## `scan/simple`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 20,910
TRAIN | 16,728
TEST  | 4,182

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/addprim_jump`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 22,376
TRAIN | 14,670
TEST  | 7,706

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/addprim_turn_left`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 23,098
TRAIN | 21,890
TEST  | 1,208

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/filler_num0`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 16,398
TRAIN | 15,225
TEST  | 1,173

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/filler_num1`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 17,463
TRAIN | 16,290
TEST  | 1,173

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/filler_num2`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 18,564
TRAIN | 17,391
TEST  | 1,173

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/filler_num3`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,701
TRAIN | 18,528
TEST  | 1,173

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/length`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 20,910
TRAIN | 16,990
TEST  | 3,920

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/template_around_right`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,701
TRAIN | 15,225
TEST  | 4,476

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/template_jump_around_right`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,701
TRAIN | 18,528
TEST  | 1,173

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/template_opposite_right`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,701
TRAIN | 15,225
TEST  | 4,476

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## `scan/template_right`

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

See https://github.com/brendenlake/SCAN for a description of the splits.

Example usage: data = tfds.load('scan/length')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,701
TRAIN | 15,225
TEST  | 4,476

### Features

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)

### Supervised keys (for `as_supervised=True`)

`('commands', 'actions')`

## Citation

```
@inproceedings{Lake2018GeneralizationWS,
  title={Generalization without Systematicity: On the Compositional Skills of
         Sequence-to-Sequence Recurrent Networks},
  author={Brenden M. Lake and Marco Baroni},
  booktitle={ICML},
  year={2018},
  url={https://arxiv.org/pdf/1711.00350.pdf},
}
```

--------------------------------------------------------------------------------
