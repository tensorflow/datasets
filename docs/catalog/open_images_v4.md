<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="open_images_v4" />
  <meta itemprop="description" content="Open Images is a dataset of ~9M images that have been annotated with image-level&#10; labels and object bounding boxes.&#10;&#10;The training set of V4 contains 14.6M bounding boxes for 600 object classes on&#10;1.74M images, making it the largest existing dataset with object location&#10;annotations. The boxes have been largely manually drawn by professional&#10;annotators to ensure accuracy and consistency. The images are very diverse and&#10;often contain complex scenes with several objects (8.4 per image on average).&#10;Moreover, the dataset is annotated with image-level labels spanning thousands of&#10;classes.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/open_images_v4" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/openimages/web/index.html" />
</div>

# `open_images_v4`

Open Images is a dataset of ~9M images that have been annotated with image-level
labels and object bounding boxes.

The training set of V4 contains 14.6M bounding boxes for 600 object classes on
1.74M images, making it the largest existing dataset with object location
annotations. The boxes have been largely manually drawn by professional
annotators to ensure accuracy and consistency. The images are very diverse and
often contain complex scenes with several objects (8.4 per image on average).
Moreover, the dataset is annotated with image-level labels spanning thousands of
classes.

*   URL:
    [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html)
*   `DatasetBuilder`:
    [`tfds.image.open_images.OpenImagesV4`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/open_images.py)

`open_images_v4` is configured with `tfds.image.open_images.OpenImagesV4Config`
and has the following configurations predefined (defaults to the first one):

*   `original` (`v0.2.0`) (`Size: 565.11 GiB`): Images at their original
    resolution and quality.

*   `300k` (`v0.2.1`) (`Size: 565.11 GiB`): Images have roughly 300,000 pixels,
    at 72 JPEG quality.

*   `200k` (`v0.2.1`) (`Size: 565.11 GiB`): Images have roughly 200,000 pixels,
    at 72 JPEG quality.

## `open_images_v4/original`

Images at their original resolution and quality.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,910,098
TRAIN      | 1,743,042
TEST       | 125,436
VALIDATION | 41,620

### Features

```python
FeaturesDict({
    'bobjects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'is_depiction': Tensor(shape=(), dtype=tf.int8),
        'is_group_of': Tensor(shape=(), dtype=tf.int8),
        'is_inside': Tensor(shape=(), dtype=tf.int8),
        'is_occluded': Tensor(shape=(), dtype=tf.int8),
        'is_truncated': Tensor(shape=(), dtype=tf.int8),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=601),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'objects': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=19995),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'objects_trainable': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=7186),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
})
```

### Urls

*   [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html)

## `open_images_v4/300k`

Images have roughly 300,000 pixels, at 72 JPEG quality.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,910,098
TRAIN      | 1,743,042
TEST       | 125,436
VALIDATION | 41,620

### Features

```python
FeaturesDict({
    'bobjects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'is_depiction': Tensor(shape=(), dtype=tf.int8),
        'is_group_of': Tensor(shape=(), dtype=tf.int8),
        'is_inside': Tensor(shape=(), dtype=tf.int8),
        'is_occluded': Tensor(shape=(), dtype=tf.int8),
        'is_truncated': Tensor(shape=(), dtype=tf.int8),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=601),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'objects': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=19995),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'objects_trainable': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=7186),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
})
```

### Urls

*   [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html)

## `open_images_v4/200k`

Images have roughly 200,000 pixels, at 72 JPEG quality.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,910,098
TRAIN      | 1,743,042
TEST       | 125,436
VALIDATION | 41,620

### Features

```python
FeaturesDict({
    'bobjects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'is_depiction': Tensor(shape=(), dtype=tf.int8),
        'is_group_of': Tensor(shape=(), dtype=tf.int8),
        'is_inside': Tensor(shape=(), dtype=tf.int8),
        'is_occluded': Tensor(shape=(), dtype=tf.int8),
        'is_truncated': Tensor(shape=(), dtype=tf.int8),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=601),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'objects': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=19995),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'objects_trainable': Sequence({
        'confidence': Tensor(shape=(), dtype=tf.int32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=7186),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
})
```

### Urls

*   [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html)

## Citation
```
@article{OpenImages,
  author = {Alina Kuznetsova and
            Hassan Rom and
            Neil Alldrin and
            Jasper Uijlings and
            Ivan Krasin and
            Jordi Pont-Tuset and
            Shahab Kamali and
            Stefan Popov and
            Matteo Malloci and
            Tom Duerig and
            Vittorio Ferrari},
  title = {The Open Images Dataset V4: Unified image classification,
           object detection, and visual relationship detection at scale},
  year = {2018},
  journal = {arXiv:1811.00982}
}
@article{OpenImages2,
  author = {Krasin, Ivan and
            Duerig, Tom and
            Alldrin, Neil and
            Ferrari, Vittorio
            and Abu-El-Haija, Sami and
            Kuznetsova, Alina and
            Rom, Hassan and
            Uijlings, Jasper and
            Popov, Stefan and
            Kamali, Shahab and
            Malloci, Matteo and
            Pont-Tuset, Jordi and
            Veit, Andreas and
            Belongie, Serge and
            Gomes, Victor and
            Gupta, Abhinav and
            Sun, Chen and
            Chechik, Gal and
            Cai, David and
            Feng, Zheyun and
            Narayanan, Dhyanesh and
            Murphy, Kevin},
  title = {OpenImages: A public dataset for large-scale multi-label and
           multi-class image classification.},
  journal = {Dataset available from
             https://storage.googleapis.com/openimages/web/index.html},
  year={2017}
}
```

--------------------------------------------------------------------------------
