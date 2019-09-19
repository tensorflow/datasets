<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="diabetic_retinopathy_detection" />
  <meta itemprop="description" content="A large set of high-resolution retina images taken under a variety of imaging conditions." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/diabetic_retinopathy_detection" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/diabetic-retinopathy-detection/data" />
</div>

# `diabetic_retinopathy_detection`

A large set of high-resolution retina images taken under a variety of imaging
conditions.

*   URL:
    [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)
*   `DatasetBuilder`:
    [`tfds.image.diabetic_retinopathy_detection.DiabeticRetinopathyDetection`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/diabetic_retinopathy_detection.py)

`diabetic_retinopathy_detection` is configured with
`tfds.image.diabetic_retinopathy_detection.DiabeticRetinopathyDetectionConfig`
and has the following configurations predefined (defaults to the first one):

*   `original` (`v2.0.0`) (`Size: 1.13 MiB`): Images at their original
    resolution and quality.

*   `1M` (`v2.1.0`) (`Size: 1.13 MiB`): Images have roughly 1,000,000 pixels, at
    72 quality.

*   `250K` (`v2.1.0`) (`Size: 1.13 MiB`): Images have roughly 250,000 pixels, at
    72 quality.

*   `btgraham-300` (`v1.0.0`) (`Size: ?? GiB`): Images have been preprocessed as
    the winner of the Kaggle competition did in 2015: first they are resized so
    that the radius of an eyeball is 300 pixels, then they are cropped to 90% of
    the radius, and finally they are encoded with 72 JPEG quality.

## `diabetic_retinopathy_detection/original`

Images at their original resolution and quality.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 88,712
TEST       | 42,670
TRAIN      | 35,126
VALIDATION | 10,906
SAMPLE     | 10

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)

## `diabetic_retinopathy_detection/1M`

Images have roughly 1,000,000 pixels, at 72 quality.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 88,712
TEST       | 42,670
TRAIN      | 35,126
VALIDATION | 10,906
SAMPLE     | 10

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)

## `diabetic_retinopathy_detection/250K`

Images have roughly 250,000 pixels, at 72 quality.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 88,712
TEST       | 42,670
TRAIN      | 35,126
VALIDATION | 10,906
SAMPLE     | 10

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)

## `diabetic_retinopathy_detection/btgraham-300`

Images have been preprocessed as the winner of the Kaggle competition did in
2015: first they are resized so that the radius of an eyeball is 300 pixels,
then they are cropped to 90% of the radius, and finally they are encoded with 72
JPEG quality.

### Statistics

None computed

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)

## Citation
```
@ONLINE {kaggle-diabetic-retinopathy,
    author = "Kaggle and EyePacs",
    title  = "Kaggle Diabetic Retinopathy Detection",
    month  = "jul",
    year   = "2015",
    url    = "https://www.kaggle.com/c/diabetic-retinopathy-detection/data"
}
```

--------------------------------------------------------------------------------
