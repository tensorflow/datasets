<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="voc" />
  <meta itemprop="description" content="This dataset contains the data from the PASCAL Visual Object Classes Challenge&#10;2007, a.k.a. VOC2007, corresponding to the Classification and Detection&#10;competitions.&#10;A total of 9963 images are included in this dataset, where each image&#10;contains a set of objects, out of 20 different classes, making a total of&#10;24640 annotated objects.&#10;In the Classification competition, the goal is to predict the set of labels&#10;contained in the image, while in the Detection competition the goal is to&#10;predict the bounding box and label of each individual object.&#10;WARNING: As per the official dataset, the test set of VOC2012 does not contains&#10;annotations.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/voc" />
  <meta itemprop="sameAs" content="http://host.robots.ox.ac.uk/pascal/VOC/voc2007/" />
</div>

# `voc`

*   URL:
    [http://host.robots.ox.ac.uk/pascal/VOC/voc2007/](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/)
*   `DatasetBuilder`:
    [`tfds.image.voc.Voc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/voc.py)

`voc` is configured with `tfds.image.voc.VocConfig` and has the following
configurations predefined (defaults to the first one):

*   `2007` (`v4.0.0`) (`Size: 868.85 MiB`): This dataset contains the data from
    the PASCAL Visual Object Classes Challenge 2007, a.k.a. VOC2007,
    corresponding to the Classification and Detection competitions. A total of
    9963 images are included in this dataset, where each image contains a set of
    objects, out of 20 different classes, making a total of 24640 annotated
    objects. In the Classification competition, the goal is to predict the set
    of labels contained in the image, while in the Detection competition the
    goal is to predict the bounding box and label of each individual object.
    WARNING: As per the official dataset, the test set of VOC2012 does not
    contains annotations.

*   `2012` (`v4.0.0`) (`Size: 3.59 GiB`): This dataset contains the data from
    the PASCAL Visual Object Classes Challenge 2007, a.k.a. VOC2007,
    corresponding to the Classification and Detection competitions. A total of
    11540 images are included in this dataset, where each image contains a set
    of objects, out of 20 different classes, making a total of 27450 annotated
    objects. In the Classification competition, the goal is to predict the set
    of labels contained in the image, while in the Detection competition the
    goal is to predict the bounding box and label of each individual object.
    WARNING: As per the official dataset, the test set of VOC2012 does not
    contains annotations.

## `voc/2007`

This dataset contains the data from the PASCAL Visual Object Classes Challenge
2007, a.k.a. VOC2007, corresponding to the Classification and Detection
competitions. A total of 9963 images are included in this dataset, where each
image contains a set of objects, out of 20 different classes, making a total of
24640 annotated objects. In the Classification competition, the goal is to
predict the set of labels contained in the image, while in the Detection
competition the goal is to predict the bounding box and label of each individual
object. WARNING: As per the official dataset, the test set of VOC2012 does not
contains annotations.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 9,963
TEST       | 4,952
VALIDATION | 2,510
TRAIN      | 2,501

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'labels': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=20)),
    'labels_no_difficult': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=20)),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'is_difficult': Tensor(shape=(), dtype=tf.bool),
        'is_truncated': Tensor(shape=(), dtype=tf.bool),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
        'pose': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    }),
})
```

### Urls

*   [http://host.robots.ox.ac.uk/pascal/VOC/voc2007/](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/)

## `voc/2012`

This dataset contains the data from the PASCAL Visual Object Classes Challenge
2007, a.k.a. VOC2007, corresponding to the Classification and Detection
competitions. A total of 11540 images are included in this dataset, where each
image contains a set of objects, out of 20 different classes, making a total of
27450 annotated objects. In the Classification competition, the goal is to
predict the set of labels contained in the image, while in the Detection
competition the goal is to predict the bounding box and label of each individual
object. WARNING: As per the official dataset, the test set of VOC2012 does not
contains annotations.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 22,531
TEST       | 10,991
VALIDATION | 5,823
TRAIN      | 5,717

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'labels': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=20)),
    'labels_no_difficult': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=20)),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'is_difficult': Tensor(shape=(), dtype=tf.bool),
        'is_truncated': Tensor(shape=(), dtype=tf.bool),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
        'pose': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    }),
})
```

### Urls

*   [http://host.robots.ox.ac.uk/pascal/VOC/voc2012/](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/)

## Citation

```
@misc{pascal-voc-2012,
    author = "Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.",
    title = "The {PASCAL} {V}isual {O}bject {C}lasses {C}hallenge 2012 {(VOC2012)} {R}esults",
    howpublished = "http://www.pascal-network.org/challenges/VOC/voc2012/workshop/index.html"}
```

--------------------------------------------------------------------------------
