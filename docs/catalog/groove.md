<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="groove" />
  <meta itemprop="description" content="The Groove MIDI Dataset (GMD) is composed of 13.6 hours of aligned MIDI and&#10;(synthesized) audio of human-performed, tempo-aligned expressive drumming&#10;captured on a Roland TD-11 V-Drum electronic drum kit.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('groove', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/groove" />
  <meta itemprop="sameAs" content="https://g.co/magenta/groove-dataset" />
  <meta itemprop="citation" content="&#10;@inproceedings{groove2019,&#10;    Author = {Jon Gillick and Adam Roberts and Jesse Engel and Douglas Eck and David Bamman},&#10;    Title = {Learning to Groove with Inverse Sequence Transformations},&#10;    Booktitle    = {International Conference on Machine Learning (ICML)}&#10;    Year = {2019},&#10;}&#10;" />
</div>

# `groove`

The Groove MIDI Dataset (GMD) is composed of 13.6 hours of aligned MIDI and
(synthesized) audio of human-performed, tempo-aligned expressive drumming
captured on a Roland TD-11 V-Drum electronic drum kit.

*   URL:
    [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)
*   `DatasetBuilder`:
    [`tfds.audio.groove.Groove`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/groove.py)

`groove` is configured with `tfds.audio.groove.GrooveConfig` and has the
following configurations predefined (defaults to the first one):

*   `full-midionly` (`v1.0.0`) (`Size: 3.11 MiB`): Groove dataset without audio,
    unsplit.

*   `full-16000hz` (`v1.0.0`) (`Size: 4.76 GiB`): Groove dataset with audio,
    unsplit.

*   `2bar-midionly` (`v1.0.0`) (`Size: 3.11 MiB`): Groove dataset without audio,
    split into 2-bar chunks.

*   `2bar-16000hz` (`v1.0.0`) (`Size: 4.76 GiB`): Groove dataset with audio,
    split into 2-bar chunks.

*   `4bar-midionly` (`v1.0.0`) (`Size: 3.11 MiB`): Groove dataset without audio,
    split into 4-bar chunks.

## `groove/full-midionly`
Groove dataset without audio, unsplit.

Versions:

*   **`1.0.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 1,150
TRAIN      | 897
TEST       | 129
VALIDATION | 124

### Features
```python
FeaturesDict({
    'bpm': Tensor(shape=(), dtype=tf.int32),
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Tensor(shape=(), dtype=tf.string),
    'midi': Tensor(shape=(), dtype=tf.string),
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': Tensor(shape=(), dtype=tf.string),
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

## `groove/full-16000hz`
Groove dataset with audio, unsplit.

Versions:

*   **`1.0.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 1,090
TRAIN      | 846
TEST       | 124
VALIDATION | 120

### Features
```python
FeaturesDict({
    'audio': Tensor(shape=[None], dtype=tf.float32),
    'bpm': Tensor(shape=(), dtype=tf.int32),
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Tensor(shape=(), dtype=tf.string),
    'midi': Tensor(shape=(), dtype=tf.string),
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': Tensor(shape=(), dtype=tf.string),
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

## `groove/2bar-midionly`
Groove dataset without audio, split into 2-bar chunks.

Versions:

*   **`1.0.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 22,619
TRAIN      | 18,163
VALIDATION | 2,252
TEST       | 2,204

### Features
```python
FeaturesDict({
    'bpm': Tensor(shape=(), dtype=tf.int32),
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Tensor(shape=(), dtype=tf.string),
    'midi': Tensor(shape=(), dtype=tf.string),
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': Tensor(shape=(), dtype=tf.string),
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

## `groove/2bar-16000hz`
Groove dataset with audio, split into 2-bar chunks.

Versions:

*   **`1.0.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 18,297
TRAIN      | 14,390
VALIDATION | 2,034
TEST       | 1,873

### Features
```python
FeaturesDict({
    'audio': Tensor(shape=[None], dtype=tf.float32),
    'bpm': Tensor(shape=(), dtype=tf.int32),
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Tensor(shape=(), dtype=tf.string),
    'midi': Tensor(shape=(), dtype=tf.string),
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': Tensor(shape=(), dtype=tf.string),
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

## `groove/4bar-midionly`
Groove dataset without audio, split into 4-bar chunks.

Versions:

*   **`1.0.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 21,415
TRAIN      | 17,261
VALIDATION | 2,121
TEST       | 2,033

### Features
```python
FeaturesDict({
    'bpm': Tensor(shape=(), dtype=tf.int32),
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Tensor(shape=(), dtype=tf.string),
    'midi': Tensor(shape=(), dtype=tf.string),
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': Tensor(shape=(), dtype=tf.string),
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

## Citation

```
@inproceedings{groove2019,
    Author = {Jon Gillick and Adam Roberts and Jesse Engel and Douglas Eck and David Bamman},
    Title = {Learning to Groove with Inverse Sequence Transformations},
    Booktitle   = {International Conference on Machine Learning (ICML)}
    Year = {2019},
}
```

--------------------------------------------------------------------------------
