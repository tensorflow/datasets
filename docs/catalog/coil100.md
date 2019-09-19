<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="coil100" />
  <meta itemprop="description" content="The dataset contains 7200 color images of 100 objects&#10;(72 images per object). The objects have a wide variety of complex geometric and reflectance characteristics.&#10;The objects were placed on a motorized turntable against a black background.&#10;The turntable was rotated through 360 degrees to vary object pose with respect to a fxed color camera.&#10;Images of the objects were taken at pose intervals of   5 degrees.This corresponds to&#10;72 poses per object" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/coil100" />
  <meta itemprop="sameAs" content="http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php" />
</div>

# `coil100`

The dataset contains 7200 color images of 100 objects (72 images per object).
The objects have a wide variety of complex geometric and reflectance
characteristics. The objects were placed on a motorized turntable against a
black background. The turntable was rotated through 360 degrees to vary object
pose with respect to a fxed color camera. Images of the objects were taken at
pose intervals of 5 degrees.This corresponds to 72 poses per object

*   URL:
    [http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php](http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php)
*   `DatasetBuilder`:
    [`tfds.image.coil100.Coil100`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/coil100.py)
*   Version: `v1.0.0`
*   Size: `124.63 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(128, 128, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=72),
    'object_id': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 7,200
TRAIN | 7,200

## Urls

*   [http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php](http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{nene1996columbia,
  title={Columbia object image library (coil-20)},
  author={Nene, Sameer A and Nayar, Shree K and Murase, Hiroshi and others},
  year={1996},
  publisher={Technical report CUCS-005-96}
}
```

--------------------------------------------------------------------------------
