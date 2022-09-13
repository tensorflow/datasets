<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="groove" />
  <meta itemprop="description" content="The Groove MIDI Dataset (GMD) is composed of 13.6 hours of aligned MIDI and&#10;(synthesized) audio of human-performed, tempo-aligned expressive drumming&#10;captured on a Roland TD-11 V-Drum electronic drum kit.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;groove&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/groove" />
  <meta itemprop="sameAs" content="https://g.co/magenta/groove-dataset" />
  <meta itemprop="citation" content="@inproceedings{groove2019,&#10;    Author = {Jon Gillick and Adam Roberts and Jesse Engel and Douglas Eck and David Bamman},&#10;    Title = {Learning to Groove with Inverse Sequence Transformations},&#10;    Booktitle = {International Conference on Machine Learning (ICML)}&#10;    Year = {2019},&#10;}" />
</div>

# `groove`


*   **Description**:

The Groove MIDI Dataset (GMD) is composed of 13.6 hours of aligned MIDI and
(synthesized) audio of human-performed, tempo-aligned expressive drumming
captured on a Roland TD-11 V-Drum electronic drum kit.

*   **Homepage**:
    [https://g.co/magenta/groove-dataset](https://g.co/magenta/groove-dataset)

*   **Source code**:
    [`tfds.audio.Groove`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/groove.py)

*   **Versions**:

    *   **`2.0.1`** (default): No release notes.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@inproceedings{groove2019,
    Author = {Jon Gillick and Adam Roberts and Jesse Engel and Douglas Eck and David Bamman},
    Title = {Learning to Groove with Inverse Sequence Transformations},
    Booktitle   = {International Conference on Machine Learning (ICML)}
    Year = {2019},
}
```


## groove/full-midionly (default config)

*   **Config description**: Groove dataset without audio, unsplit.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `5.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 129
`'train'`      | 897
`'validation'` | 124

*   **Feature structure**:

```python
FeaturesDict({
    'bpm': tf.int32,
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': tf.string,
    'midi': tf.string,
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': tf.string,
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype     | Description
:-------------- | :----------- | :---- | :-------- | :----------
                | FeaturesDict |       |           |
bpm             | Tensor       |       | tf.int32  |
drummer         | ClassLabel   |       | tf.int64  |
id              | Tensor       |       | tf.string |
midi            | Tensor       |       | tf.string |
style           | FeaturesDict |       |           |
style/primary   | ClassLabel   |       | tf.int64  |
style/secondary | Tensor       |       | tf.string |
time_signature  | ClassLabel   |       | tf.int64  |
type            | ClassLabel   |       | tf.int64  |

## groove/full-16000hz

*   **Config description**: Groove dataset with audio, unsplit.

*   **Download size**: `4.76 GiB`

*   **Dataset size**: `2.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 124
`'train'`      | 846
`'validation'` | 120

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.float32),
    'bpm': tf.int32,
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': tf.string,
    'midi': tf.string,
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': tf.string,
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape   | Dtype      | Description
:-------------- | :----------- | :------ | :--------- | :----------
                | FeaturesDict |         |            |
audio           | Audio        | (None,) | tf.float32 |
bpm             | Tensor       |         | tf.int32   |
drummer         | ClassLabel   |         | tf.int64   |
id              | Tensor       |         | tf.string  |
midi            | Tensor       |         | tf.string  |
style           | FeaturesDict |         |            |
style/primary   | ClassLabel   |         | tf.int64   |
style/secondary | Tensor       |         | tf.string  |
time_signature  | ClassLabel   |         | tf.int64   |
type            | ClassLabel   |         | tf.int64   |

## groove/2bar-midionly

*   **Config description**: Groove dataset without audio, split into 2-bar
    chunks.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `19.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,204
`'train'`      | 18,163
`'validation'` | 2,252

*   **Feature structure**:

```python
FeaturesDict({
    'bpm': tf.int32,
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': tf.string,
    'midi': tf.string,
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': tf.string,
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype     | Description
:-------------- | :----------- | :---- | :-------- | :----------
                | FeaturesDict |       |           |
bpm             | Tensor       |       | tf.int32  |
drummer         | ClassLabel   |       | tf.int64  |
id              | Tensor       |       | tf.string |
midi            | Tensor       |       | tf.string |
style           | FeaturesDict |       |           |
style/primary   | ClassLabel   |       | tf.int64  |
style/secondary | Tensor       |       | tf.string |
time_signature  | ClassLabel   |       | tf.int64  |
type            | ClassLabel   |       | tf.int64  |

## groove/2bar-16000hz

*   **Config description**: Groove dataset with audio, split into 2-bar chunks.

*   **Download size**: `4.76 GiB`

*   **Dataset size**: `4.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,873
`'train'`      | 14,390
`'validation'` | 2,034

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.float32),
    'bpm': tf.int32,
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': tf.string,
    'midi': tf.string,
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': tf.string,
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape   | Dtype      | Description
:-------------- | :----------- | :------ | :--------- | :----------
                | FeaturesDict |         |            |
audio           | Audio        | (None,) | tf.float32 |
bpm             | Tensor       |         | tf.int32   |
drummer         | ClassLabel   |         | tf.int64   |
id              | Tensor       |         | tf.string  |
midi            | Tensor       |         | tf.string  |
style           | FeaturesDict |         |            |
style/primary   | ClassLabel   |         | tf.int64   |
style/secondary | Tensor       |         | tf.string  |
time_signature  | ClassLabel   |         | tf.int64   |
type            | ClassLabel   |         | tf.int64   |

## groove/4bar-midionly

*   **Config description**: Groove dataset without audio, split into 4-bar
    chunks.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `27.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,033
`'train'`      | 17,261
`'validation'` | 2,121

*   **Feature structure**:

```python
FeaturesDict({
    'bpm': tf.int32,
    'drummer': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': tf.string,
    'midi': tf.string,
    'style': FeaturesDict({
        'primary': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'secondary': tf.string,
    }),
    'time_signature': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype     | Description
:-------------- | :----------- | :---- | :-------- | :----------
                | FeaturesDict |       |           |
bpm             | Tensor       |       | tf.int32  |
drummer         | ClassLabel   |       | tf.int64  |
id              | Tensor       |       | tf.string |
midi            | Tensor       |       | tf.string |
style           | FeaturesDict |       |           |
style/primary   | ClassLabel   |       | tf.int64  |
style/secondary | Tensor       |       | tf.string |
time_signature  | ClassLabel   |       | tf.int64  |
type            | ClassLabel   |       | tf.int64  |
