<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="starcraft_video" />
  <meta itemprop="description" content="This data set contains videos generated from Starcraft." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/starcraft_video" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/scv_dataset/README.html" />
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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/brawl_128`

Brawl map with 128x128 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/collect_mineral_shards_64`

CollectMineralShards map with 64x64 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/collect_mineral_shards_128`

CollectMineralShards map with 128x128 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/move_unit_to_border_64`

MoveUnitToBorder map with 64x64 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/move_unit_to_border_128`

MoveUnitToBorder map with 128x128 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/road_trip_with_medivac_64`

RoadTripWithMedivac map with 64x64 resolution.

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

### Urls

*   [https://storage.googleapis.com/scv_dataset/README.html](https://storage.googleapis.com/scv_dataset/README.html)

## `starcraft_video/road_trip_with_medivac_128`

RoadTripWithMedivac map with 128x128 resolution.

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

### Urls

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
