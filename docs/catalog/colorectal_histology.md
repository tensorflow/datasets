<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="colorectal_histology" />
  <meta itemprop="description" content="Classification of textures in colorectal cancer histology. Each example is a 150 x 150 x 3 RGB image of one of 8 classes." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/colorectal_histology" />
  <meta itemprop="sameAs" content="https://zenodo.org/record/53169#.XGZemKwzbmG" />
</div>

# `colorectal_histology`

Classification of textures in colorectal cancer histology. Each example is a 150
x 150 x 3 RGB image of one of 8 classes.

*   URL:
    [https://zenodo.org/record/53169#.XGZemKwzbmG](https://zenodo.org/record/53169#.XGZemKwzbmG)
*   `DatasetBuilder`:
    [`tfds.image.colorectal_histology.ColorectalHistology`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/colorectal_histology.py)
*   Version: `v0.0.1`
*   Size: `246.14 MiB`

## Features
```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(150, 150, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=8),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 5,000
TRAIN | 5,000

## Urls

*   [https://zenodo.org/record/53169#.XGZemKwzbmG](https://zenodo.org/record/53169#.XGZemKwzbmG)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{kather2016multi,
  title={Multi-class texture analysis in colorectal cancer histology},
  author={Kather, Jakob Nikolas and Weis, Cleo-Aron and Bianconi, Francesco and Melchers, Susanne M and Schad, Lothar R and Gaiser, Timo and Marx, Alexander and Z{"o}llner, Frank Gerrit},
  journal={Scientific reports},
  volume={6},
  pages={27988},
  year={2016},
  publisher={Nature Publishing Group}
}
```

--------------------------------------------------------------------------------
