<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="colorectal_histology_large" />
  <meta itemprop="description" content="10 large 5000 x 5000 textured colorectal cancer histology images" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/colorectal_histology_large" />
  <meta itemprop="sameAs" content="https://zenodo.org/record/53169#.XGZemKwzbmG" />
</div>

# `colorectal_histology_large`

10 large 5000 x 5000 textured colorectal cancer histology images

*   URL:
    [https://zenodo.org/record/53169#.XGZemKwzbmG](https://zenodo.org/record/53169#.XGZemKwzbmG)
*   `DatasetBuilder`:
    [`tfds.image.colorectal_histology.ColorectalHistologyLarge`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/colorectal_histology.py)
*   Version: `v0.0.1`
*   Size: `707.65 MiB`

## Features
```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(5000, 5000, 3), dtype=tf.uint8),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 10
TEST  | 10

## Urls

*   [https://zenodo.org/record/53169#.XGZemKwzbmG](https://zenodo.org/record/53169#.XGZemKwzbmG)

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
