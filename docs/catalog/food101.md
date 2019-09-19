<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="food101" />
  <meta itemprop="description" content="This dataset consists of 101 food categories, with 101'000 images. For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/food101" />
  <meta itemprop="sameAs" content="http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz" />
</div>

# `food101`

This dataset consists of 101 food categories, with 101'000 images. For each
class, 250 manually reviewed test images are provided as well as 750 training
images. On purpose, the training images were not cleaned, and thus still contain
some amount of noise. This comes mostly in the form of intense colors and
sometimes wrong labels. All images were rescaled to have a maximum side length
of 512 pixels.

*   URL:
    [http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz](http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz)
*   `DatasetBuilder`:
    [`tfds.image.food101.Food101`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/food101.py)
*   Version: `v1.0.0`
*   Size: `4.65 GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=101),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 101,000
TRAIN | 101,000

## Urls

*   [http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz](http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@inproceedings{bossard14,
  title = {Food-101 -- Mining Discriminative Components with Random Forests},
  author = {Bossard, Lukas and Guillaumin, Matthieu and Van Gool, Luc},
  booktitle = {European Conference on Computer Vision},
  year = {2014}
}
```

--------------------------------------------------------------------------------
