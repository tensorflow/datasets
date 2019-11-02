<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quickdraw_bitmap" />
  <meta itemprop="description" content="The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The bitmap dataset contains these drawings converted from vector format into 28x28 grayscale images&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('quickdraw_bitmap', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quickdraw_bitmap" />
  <meta itemprop="sameAs" content="https://github.com/googlecreativelab/quickdraw-dataset" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/HaE17,&#10;  author    = {David Ha and&#10;               Douglas Eck},&#10;  title     = {A Neural Representation of Sketch Drawings},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1704.03477},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1704.03477},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1704.03477},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:30 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/HaE17},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
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
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

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

## Homepage

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
