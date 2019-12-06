<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="starcraft_video" />
  <meta itemprop="description" content="This data set contains videos generated from Starcraft.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('starcraft_video', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/starcraft_video" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/scv_dataset/README.html" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1812-01717,&#10;  author    = {Thomas Unterthiner and&#10;               Sjoerd van Steenkiste and&#10;               Karol Kurach and&#10;               Rapha{&quot;{e}}l Marinier and&#10;               Marcin Michalski and&#10;               Sylvain Gelly},&#10;  title     = {Towards Accurate Generative Models of Video: {A} New Metric and&#10;               Challenges},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1812.01717},&#10;  year      = {2018},&#10;  url       = {http://arxiv.org/abs/1812.01717},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1812.01717},&#10;  timestamp = {Tue, 01 Jan 2019 15:01:25 +0100},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1812-01717},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
</div>
# `starcraft_video`

This data set contains videos generated from Starcraft.

*   URL:
    [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)
*   `DatasetBuilder`:
    [`tfds.video.starcraft.StarcraftVideo`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/starcraft.py)

`starcraft_video` is configured with `tfds.video.starcraft.StarcraftVideoConfig`
and has the following configurations predefined (defaults to the first one):

*   `brawl_64` (`v0.1.2`) (`Size: 6.40 GiB`): Brawl map with 64x64 resolution.

*   `brawl_128` (`v0.1.2`) (`Size: 20.76 GiB`): Brawl map with 128x128
    resolution.

*   `collect_mineral_shards_64` (`v0.1.2`) (`Size: 7.83 GiB`):
    CollectMineralShards map with 64x64 resolution.

*   `collect_mineral_shards_128` (`v0.1.2`) (`Size: 24.83 GiB`):
    CollectMineralShards map with 128x128 resolution.

*   `move_unit_to_border_64` (`v0.1.2`) (`Size: 1.77 GiB`): MoveUnitToBorder map
    with 64x64 resolution.

*   `move_unit_to_border_128` (`v0.1.2`) (`Size: 5.75 GiB`): MoveUnitToBorder
    map with 128x128 resolution.

*   `road_trip_with_medivac_64` (`v0.1.2`) (`Size: 2.48 GiB`):
    RoadTripWithMedivac map with 64x64 resolution.

*   `road_trip_with_medivac_128` (`v0.1.2`) (`Size: 7.80 GiB`):
    RoadTripWithMedivac map with 128x128 resolution.

## `starcraft_video/brawl_64`
Brawl map with 64x64 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/brawl_128`
Brawl map with 128x128 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/collect_mineral_shards_64`
CollectMineralShards map with 64x64 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/collect_mineral_shards_128`
CollectMineralShards map with 128x128 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/move_unit_to_border_64`
MoveUnitToBorder map with 64x64 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/move_unit_to_border_128`
MoveUnitToBorder map with 128x128 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/road_trip_with_medivac_64`
RoadTripWithMedivac map with 64x64 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/road_trip_with_medivac_128`
RoadTripWithMedivac map with 128x128 resolution.

Versions:

*   **`0.1.2`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 14,000
TRAIN      | 10,000
TEST       | 2,000
VALIDATION | 2,000

### Features
```python
FeaturesDict({
    'rgb_screen': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

### Homepage

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## Citation
```
@article{DBLP:journals/corr/abs-1812-01717,
  author    = {Thomas Unterthiner and
               Sjoerd van Steenkiste and
               Karol Kurach and
               Rapha{"{e}}l Marinier and
               Marcin Michalski and
               Sylvain Gelly},
  title     = {Towards Accurate Generative Models of Video: {A} New Metric and
               Challenges},
  journal   = {CoRR},
  volume    = {abs/1812.01717},
  year      = {2018},
  url       = {http://arxiv.org/abs/1812.01717},
  archivePrefix = {arXiv},
  eprint    = {1812.01717},
  timestamp = {Tue, 01 Jan 2019 15:01:25 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1812-01717},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
