<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="coco" />
  <meta itemprop="description" content="COCO is a large-scale object detection, segmentation, and&#10;captioning dataset. This version contains images, bounding boxes &quot;&#10;and labels for the 2017 version.&#10;Note:&#10; * Some images from the train and validation sets don't have annotations.&#10; * Coco 2014 and 2017 uses the same images, but different train/val/test splits&#10; * The test split don't have any annotations (only images).&#10; * Coco defines 91 classes but the data only uses 80 classes.&#10; * Panotptic annotations defines defines 200 classes but only uses 133.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/coco" />
  <meta itemprop="sameAs" content="http://cocodataset.org/#home" />
</div>

# `coco`

COCO is a large-scale object detection, segmentation, and captioning dataset.
This version contains images, bounding boxes " and labels for the 2017 version.
Note: * Some images from the train and validation sets don't have annotations. *
Coco 2014 and 2017 uses the same images, but different train/val/test splits *
The test split don't have any annotations (only images). * Coco defines 91
classes but the data only uses 80 classes. * Panotptic annotations defines
defines 200 classes but only uses 133.

*   URL: [http://cocodataset.org/#home](http://cocodataset.org/#home)
*   `DatasetBuilder`:
    [`tfds.image.coco.Coco`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/coco.py)

`coco` is configured with `tfds.image.coco.CocoConfig` and has the following
configurations predefined (defaults to the first one):

*   `2014` (`v1.1.0`) (`Size: 37.57 GiB`): COCO is a large-scale object
    detection, segmentation, and captioning dataset. This version contains
    images, bounding boxes " and labels for the 2014 version. Note:

    *   Some images from the train and validation sets don't have annotations.
    *   Coco 2014 and 2017 uses the same images, but different train/val/test
        splits
    *   The test split don't have any annotations (only images).
    *   Coco defines 91 classes but the data only uses 80 classes.
    *   Panotptic annotations defines defines 200 classes but only uses 133.

*   `2017` (`v1.1.0`) (`Size: 25.20 GiB`): COCO is a large-scale object
    detection, segmentation, and captioning dataset. This version contains
    images, bounding boxes " and labels for the 2017 version. Note:

    *   Some images from the train and validation sets don't have annotations.
    *   Coco 2014 and 2017 uses the same images, but different train/val/test
        splits
    *   The test split don't have any annotations (only images).
    *   Coco defines 91 classes but the data only uses 80 classes.
    *   Panotptic annotations defines defines 200 classes but only uses 133.

*   `2017_panoptic` (`v1.1.0`) (`Size: 19.57 GiB`): COCO is a large-scale object
    detection, segmentation, and captioning dataset. This version contains
    images, bounding boxes " and labels for the 2017 version. Note:

    *   Some images from the train and validation sets don't have annotations.
    *   Coco 2014 and 2017 uses the same images, but different train/val/test
        splits
    *   The test split don't have any annotations (only images).
    *   Coco defines 91 classes but the data only uses 80 classes.
    *   Panotptic annotations defines defines 200 classes but only uses 133.

## `coco/2014`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'image/id': Tensor(shape=(), dtype=tf.int64),
    'objects': Sequence({
        'area': Tensor(shape=(), dtype=tf.int64),
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': Tensor(shape=(), dtype=tf.int64),
        'is_crowd': Tensor(shape=(), dtype=tf.bool),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=80),
    }),
})
```

## `coco/2017`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'image/id': Tensor(shape=(), dtype=tf.int64),
    'objects': Sequence({
        'area': Tensor(shape=(), dtype=tf.int64),
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': Tensor(shape=(), dtype=tf.int64),
        'is_crowd': Tensor(shape=(), dtype=tf.bool),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=80),
    }),
})
```

## `coco/2017_panoptic`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'image/id': Tensor(shape=(), dtype=tf.int64),
    'panoptic_image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'panoptic_image/filename': Text(shape=(), dtype=tf.string),
    'panoptic_objects': Sequence({
        'area': Tensor(shape=(), dtype=tf.int64),
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': Tensor(shape=(), dtype=tf.int64),
        'is_crowd': Tensor(shape=(), dtype=tf.bool),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=133),
    }),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 123,287
TRAIN      | 118,287
VALIDATION | 5,000

## Urls

*   [http://cocodataset.org/#home](http://cocodataset.org/#home)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
```
@article{DBLP:journals/corr/LinMBHPRDZ14,
  author    = {Tsung{-}Yi Lin and
               Michael Maire and
               Serge J. Belongie and
               Lubomir D. Bourdev and
               Ross B. Girshick and
               James Hays and
               Pietro Perona and
               Deva Ramanan and
               Piotr Doll{'{a}}r and
               C. Lawrence Zitnick},
  title     = {Microsoft {COCO:} Common Objects in Context},
  journal   = {CoRR},
  volume    = {abs/1405.0312},
  year      = {2014},
  url       = {http://arxiv.org/abs/1405.0312},
  archivePrefix = {arXiv},
  eprint    = {1405.0312},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/LinMBHPRDZ14},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
