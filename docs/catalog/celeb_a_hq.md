<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="celeb_a_hq" />
  <meta itemprop="description" content="High-quality version of the CELEBA&#10;dataset, consisting of 30000 images in 1024 x 1024 resolution.&#10;&#10;WARNING: This dataset currently requires you to prepare images on your own.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('celeb_a_hq', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/celeb_a_hq" />
  <meta itemprop="sameAs" content="https://github.com/tkarras/progressive_growing_of_gans" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1710-10196,&#10;  author    = {Tero Karras and&#10;               Timo Aila and&#10;               Samuli Laine and&#10;               Jaakko Lehtinen},&#10;  title     = {Progressive Growing of GANs for Improved Quality, Stability, and Variation},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1710.10196},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1710.10196},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1710.10196},&#10;  timestamp = {Mon, 13 Aug 2018 16:46:42 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10196},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
</div>
# `celeb_a_hq` (Manual download)

High-quality version of the CELEBA dataset, consisting of 30000 images in 1024 x
1024 resolution.

WARNING: This dataset currently requires you to prepare images on your own.

*   URL:
    [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)
*   `DatasetBuilder`:
    [`tfds.image.celebahq.CelebAHq`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/celebahq.py)

`celeb_a_hq` is configured with `tfds.image.celebahq.CelebaHQConfig` and has the
following configurations predefined (defaults to the first one):

*   `1024` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 1024 x 1024
    resolution

*   `512` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 512 x 512 resolution

*   `256` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 256 x 256 resolution

*   `128` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 128 x 128 resolution

*   `64` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 64 x 64 resolution

*   `32` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 32 x 32 resolution

*   `16` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 16 x 16 resolution

*   `8` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 8 x 8 resolution

*   `4` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 4 x 4 resolution

*   `2` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 2 x 2 resolution

*   `1` (`v0.1.0`) (`Size: ?? GiB`): CelebaHQ images in 1 x 1 resolution

## `celeb_a_hq/1024`
CelebaHQ images in 1024 x 1024 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(1024, 1024, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/512`
CelebaHQ images in 512 x 512 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(512, 512, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/256`
CelebaHQ images in 256 x 256 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/128`
CelebaHQ images in 128 x 128 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(128, 128, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/64`
CelebaHQ images in 64 x 64 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(64, 64, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/32`
CelebaHQ images in 32 x 32 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/16`
CelebaHQ images in 16 x 16 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(16, 16, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/8`
CelebaHQ images in 8 x 8 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(8, 8, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/4`
CelebaHQ images in 4 x 4 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(4, 4, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/2`
CelebaHQ images in 2 x 2 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(2, 2, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## `celeb_a_hq/1`
CelebaHQ images in 1 x 1 resolution

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/celeb_a_hq/`): manual_dir
should contain multiple tar files with images (data2x2.tar, data4x4.tar ..
data1024x1024.tar). Detailed instructions are here:
https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,000
TRAIN | 30,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(1, 1, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

## Citation
```
@article{DBLP:journals/corr/abs-1710-10196,
  author    = {Tero Karras and
               Timo Aila and
               Samuli Laine and
               Jaakko Lehtinen},
  title     = {Progressive Growing of GANs for Improved Quality, Stability, and Variation},
  journal   = {CoRR},
  volume    = {abs/1710.10196},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.10196},
  archivePrefix = {arXiv},
  eprint    = {1710.10196},
  timestamp = {Mon, 13 Aug 2018 16:46:42 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10196},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
