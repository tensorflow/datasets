<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quickdraw_bitmap" />
  <meta itemprop="description" content="The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The bitmap dataset contains these drawings converted from vector format into 28x28 grayscale images" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quickdraw_bitmap" />
  <meta itemprop="sameAs" content="https://github.com/googlecreativelab/quickdraw-dataset" />
</div>

# `quickdraw_bitmap`

The Quick Draw Dataset is a collection of 50 million drawings across 345
categories, contributed by players of the game Quick, Draw!. The bitmap dataset
contains these drawings converted from vector format into 28x28 grayscale images

*   URL:
    [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)
*   `DatasetBuilder`:
    [`tfds.image.quickdraw.QuickdrawBitmap`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/quickdraw.py)
*   Version: `v1.0.0`
*   Size: `36.82 GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=345),
})
```

## Statistics

Split | Examples
:---- | ---------:
ALL   | 50,426,266
TRAIN | 50,426,266

## Urls

*   [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{DBLP:journals/corr/HaE17,
  author    = {David Ha and
               Douglas Eck},
  title     = {A Neural Representation of Sketch Drawings},
  journal   = {CoRR},
  volume    = {abs/1704.03477},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.03477},
  archivePrefix = {arXiv},
  eprint    = {1704.03477},
  timestamp = {Mon, 13 Aug 2018 16:48:30 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/HaE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
