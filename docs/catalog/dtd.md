<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dtd" />
  <meta itemprop="description" content="The Describable Textures Dataset (DTD) is an evolving collection of textural&#10;images in the wild, annotated with a series of human-centric attributes,&#10;inspired by the perceptual properties of textures. This data is made available&#10;to the computer vision community for research purposes.&#10;&#10;The &quot;label&quot; of each example is its &quot;key attribute&quot; (see the official website).&#10;The official release of the dataset defines a 10-fold cross-validation&#10;partition. Our TRAIN/TEST/VALIDATION splits are those of the first fold.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dtd" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html" />
</div>

# `dtd`

The Describable Textures Dataset (DTD) is an evolving collection of textural
images in the wild, annotated with a series of human-centric attributes,
inspired by the perceptual properties of textures. This data is made available
to the computer vision community for research purposes.

The "label" of each example is its "key attribute" (see the official website).
The official release of the dataset defines a 10-fold cross-validation
partition. Our TRAIN/TEST/VALIDATION splits are those of the first fold.

*   URL:
    [https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html](https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html)
*   `DatasetBuilder`:
    [`tfds.image.dtd.Dtd`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/dtd.py)
*   Version: `v1.0.0`
*   Size: `608.33 MiB`

## Features
```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,640
TEST       | 1,880
TRAIN      | 1,880
VALIDATION | 1,880

## Urls

*   [https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html](https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html)

## Citation
```
@InProceedings{cimpoi14describing,
Author    = {M. Cimpoi and S. Maji and I. Kokkinos and S. Mohamed and A. Vedaldi},
Title     = {Describing Textures in the Wild},
Booktitle = {Proceedings of the {IEEE} Conf. on Computer Vision and Pattern Recognition ({CVPR})},
Year      = {2014}}
```

--------------------------------------------------------------------------------
