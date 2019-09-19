<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lfw" />
  <meta itemprop="description" content="Labeled Faces in the Wild:&#10;        A Database for Studying Face Recognition in&#10;        Unconstrained Environments" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lfw" />
  <meta itemprop="sameAs" content="http://vis-www.cs.umass.edu/lfw" />
</div>

# `lfw`

Labeled Faces in the Wild: A Database for Studying Face Recognition in
Unconstrained Environments

*   URL: [http://vis-www.cs.umass.edu/lfw](http://vis-www.cs.umass.edu/lfw)
*   `DatasetBuilder`:
    [`tfds.image.lfw.LFW`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/lfw.py)
*   Version: `v0.1.0`
*   Size: `172.20 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(250, 250, 3), dtype=tf.uint8),
    'label': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 13,233
TRAIN | 13,233

## Urls

*   [http://vis-www.cs.umass.edu/lfw](http://vis-www.cs.umass.edu/lfw)

## Supervised keys (for `as_supervised=True`)
`(u'label', u'image')`

## Citation
```
@TechReport{LFWTech,
    author = {Gary B. Huang and Manu Ramesh and Tamara Berg and Erik Learned-Miller},
    title = {Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments},
    institution = {University of Massachusetts, Amherst},
    year = 2007,
    number = {07-49},
    month = {October}
}
```

--------------------------------------------------------------------------------
