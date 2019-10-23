<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech_birds2011" />
  <meta itemprop="description" content="Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos &#10;of 200 bird species (mostly North American). The total number of &#10;categories of birds is 200 and there are 6033 images in the 2010 &#10;dataset and 11,788 images in the 2011 dataset.&#10;Annotations include bounding boxes, segmentation labels.&#10;&#10;&#10;To use this dataset:&#10;&#10;```&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('caltech_birds2011')&#10;```&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech_birds2011" />
  <meta itemprop="sameAs" content="http://www.vision.caltech.edu/visipedia/CUB-200.html" />
  <meta itemprop="citation" content="@techreport{WelinderEtal2010,&#10;Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},&#10;Institution = {California Institute of Technology},&#10;Number = {CNS-TR-2010-001},&#10;Title = {{Caltech-UCSD Birds 200}},&#10;Year = {2010}&#10;}&#10;" />
</div>
# `caltech_birds2011`

Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos of 200 bird
species (mostly North American). The total number of categories of birds is 200
and there are 6033 images in the 2010 dataset and 11,788 images in the 2011
dataset. Annotations include bounding boxes, segmentation labels.

*   URL:
    [http://www.vision.caltech.edu/visipedia/CUB-200.html](http://www.vision.caltech.edu/visipedia/CUB-200.html)
*   `DatasetBuilder`:
    [`tfds.image.caltech_birds.CaltechBirds2011`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/caltech_birds.py)
*   Version: `v0.1.0`
*   Versions:

    *   **`0.1.0`** (default):

*   Size: `1.11 GiB`

## Features
```python
FeaturesDict({
    'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=200),
    'label_name': Text(shape=(), dtype=tf.string),
    'segmentation_mask': Image(shape=(None, None, 1), dtype=tf.uint8),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 11,788
TRAIN | 5,994
TEST  | 5,794

## Urls

*   [http://www.vision.caltech.edu/visipedia/CUB-200.html](http://www.vision.caltech.edu/visipedia/CUB-200.html)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@techreport{WelinderEtal2010,
Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},
Institution = {California Institute of Technology},
Number = {CNS-TR-2010-001},
Title = {{Caltech-UCSD Birds 200}},
Year = {2010}
}
```

--------------------------------------------------------------------------------
