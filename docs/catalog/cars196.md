<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cars196" />
  <meta itemprop="description" content="The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cars196" />
  <meta itemprop="sameAs" content="http://imagenet.stanford.edu/internal/car196/" />
</div>

# `cars196`

The Cars dataset contains 16,185 images of 196 classes of cars. The data is
split into 8,144 training images and 8,041 testing images, where each class has
been split roughly in a 50-50 split. Classes are typically at the level of Make,
Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

*   URL:
    [http://imagenet.stanford.edu/internal/car196/](http://imagenet.stanford.edu/internal/car196/)
*   `DatasetBuilder`:
    [`tfds.image.cars196.Cars196`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cars196.py)
*   Version: `v1.0.0`
*   Size: `1.82 GiB`

## Features
```python
FeaturesDict({
    'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=197),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 16,185
TRAIN | 8,144
TEST  | 8,041

## Urls

*   [http://imagenet.stanford.edu/internal/car196/](http://imagenet.stanford.edu/internal/car196/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@inproceedings{KrauseStarkDengFei-Fei_3DRR2013,
  title = {3D Object Representations for Fine-Grained Categorization},
  booktitle = {4th International IEEE Workshop on  3D Representation and Recognition (3dRR-13)},
  year = {2013},
  address = {Sydney, Australia},
  author = {Jonathan Krause and Michael Stark and Jia Deng and Li Fei-Fei}
  }
```

--------------------------------------------------------------------------------
