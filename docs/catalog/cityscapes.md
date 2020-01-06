<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="cityscapes" />
  <meta itemprop="description" content="Cityscapes is a dataset consisting of diverse urban street scenes across 50 different cities&#10;  at varying times of the year as well as ground truths for several vision tasks including&#10;  semantic segmentation, instance level segmentation (TODO), and stereo pair disparity inference.&#10;&#10;&#10;  For segmentation tasks (default split, accessible via 'cityscapes/semantic_segmentation'), Cityscapes provides&#10;  dense pixel level annotations for 5000 images at 1024 * 2048 resolution pre-split into training (2975),&#10;  validation (500) and test (1525) sets. Label annotations for segmentation tasks span across 30+ classes&#10;  commonly encountered during driving scene perception. Detailed label information may be found here:&#10;  https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99&#10;&#10;  Cityscapes also provides coarse grain segmentation annotations (accessible via 'cityscapes/semantic_segmentation_extra')&#10;  for 19998 images in a 'train_extra' split which may prove useful for pretraining / data-heavy models.&#10;&#10;&#10;  Besides segmentation, cityscapes also provides stereo image pairs and ground truths for disparity inference&#10;  tasks on both the normal and extra splits (accessible via 'cityscapes/stereo_disparity' and&#10;  'cityscapes/stereo_disparity_extra' respectively).&#10;&#10;  Ingored examples:&#10;  - For 'cityscapes/stereo_disparity_extra':&#10;    - troisdorf_000000_000073_{*} images (no disparity map present)&#10;&#10;  WARNING: this dataset requires users to setup a login and password in order to get the files.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('cityscapes', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cityscapes" />
  <meta itemprop="sameAs" content="https://www.cityscapes-dataset.com" />
  <meta itemprop="citation" content="@inproceedings{Cordts2016Cityscapes,&#10;  title={The Cityscapes Dataset for Semantic Urban Scene Understanding},&#10;  author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},&#10;  booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;  year={2016}&#10;}&#10;" />
</div>

# `cityscapes` (Manual download)

Cityscapes is a dataset consisting of diverse urban street scenes across 50
different cities at varying times of the year as well as ground truths for
several vision tasks including semantic segmentation, instance level
segmentation (TODO), and stereo pair disparity inference.

For segmentation tasks (default split, accessible via
'cityscapes/semantic_segmentation'), Cityscapes provides dense pixel level
annotations for 5000 images at 1024 * 2048 resolution pre-split into training
(2975), validation (500) and test (1525) sets. Label annotations for
segmentation tasks span across 30+ classes commonly encountered during driving
scene perception. Detailed label information may be found here:
https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99

Cityscapes also provides coarse grain segmentation annotations (accessible via
'cityscapes/semantic_segmentation_extra') for 19998 images in a 'train_extra'
split which may prove useful for pretraining / data-heavy models.

Besides segmentation, cityscapes also provides stereo image pairs and ground
truths for disparity inference tasks on both the normal and extra splits
(accessible via 'cityscapes/stereo_disparity' and
'cityscapes/stereo_disparity_extra' respectively).

Ingored examples: - For 'cityscapes/stereo_disparity_extra': -
troisdorf_000000_000073_{*} images (no disparity map present)

WARNING: this dataset requires users to setup a login and password in order to
get the files.

*   URL:
    [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)
*   `DatasetBuilder`:
    [`tfds.image.cityscapes.Cityscapes`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cityscapes.py)

`cityscapes` is configured with `tfds.image.cityscapes.CityscapesConfig` and has
the following configurations predefined (defaults to the first one):

*   `semantic_segmentation` (`v1.0.0`) (`Size: ?? GiB`): Cityscapes semantic
    segmentation dataset.

*   `semantic_segmentation_extra` (`v1.0.0`) (`Size: ?? GiB`): Cityscapes
    semantic segmentation dataset with train_extra split and coarse labels.

*   `stereo_disparity` (`v1.0.0`) (`Size: ?? GiB`): Cityscapes stereo image and
    disparity maps dataset.

*   `stereo_disparity_extra` (`v1.0.0`) (`Size: ?? GiB`): Cityscapes stereo
    image and disparity maps dataset with train_extra split.

## `cityscapes/semantic_segmentation`

Cityscapes semantic segmentation dataset.

Versions:

*   **`1.0.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/cityscapes/`): You have to
download files from https://www.cityscapes-dataset.com/login/ (This dataset
requires registration). For basic config (semantic_segmentation) you must
download 'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'. Other
configs do require additional files - please see code for more details.

### Statistics

None computed

### Features

```python
FeaturesDict({
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
})
```

### Homepage

*   [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)

## `cityscapes/semantic_segmentation_extra`

Cityscapes semantic segmentation dataset with train_extra split and coarse
labels.

Versions:

*   **`1.0.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/cityscapes/`): You have to
download files from https://www.cityscapes-dataset.com/login/ (This dataset
requires registration). For basic config (semantic_segmentation) you must
download 'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'. Other
configs do require additional files - please see code for more details.

### Statistics

None computed

### Features

```python
FeaturesDict({
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
})
```

### Homepage

*   [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)

## `cityscapes/stereo_disparity`

Cityscapes stereo image and disparity maps dataset.

Versions:

*   **`1.0.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/cityscapes/`): You have to
download files from https://www.cityscapes-dataset.com/login/ (This dataset
requires registration). For basic config (semantic_segmentation) you must
download 'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'. Other
configs do require additional files - please see code for more details.

### Statistics

None computed

### Features

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)

## `cityscapes/stereo_disparity_extra`

Cityscapes stereo image and disparity maps dataset with train_extra split.

Versions:

*   **`1.0.0`** (default):

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/cityscapes/`): You have to
download files from https://www.cityscapes-dataset.com/login/ (This dataset
requires registration). For basic config (semantic_segmentation) you must
download 'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'. Other
configs do require additional files - please see code for more details.

### Statistics

None computed

### Features

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
})
```

### Homepage

*   [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)

## Citation

```
@inproceedings{Cordts2016Cityscapes,
  title={The Cityscapes Dataset for Semantic Urban Scene Understanding},
  author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},
  booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2016}
}
```

--------------------------------------------------------------------------------
