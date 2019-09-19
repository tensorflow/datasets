<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="eurosat" />
  <meta itemprop="description" content="EuroSAT dataset is based on Sentinel-2 satellite images covering 13 spectral&#10;bands and consisting of 10 classes with 27000 labeled and&#10;geo-referenced samples.&#10;&#10;Two datasets are offered:&#10;- rgb: Contains only the optical R, G, B frequency bands encoded as JPEG image.&#10;- all: Contains all 13 bands in the original value range (float32).&#10;&#10;URL: https://github.com/phelber/eurosat&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/eurosat" />
  <meta itemprop="sameAs" content="https://github.com/phelber/eurosat" />
</div>

# `eurosat`

EuroSAT dataset is based on Sentinel-2 satellite images covering 13 spectral
bands and consisting of 10 classes with 27000 labeled and geo-referenced
samples.

Two datasets are offered: - rgb: Contains only the optical R, G, B frequency
bands encoded as JPEG image. - all: Contains all 13 bands in the original value
range (float32).

URL: https://github.com/phelber/eurosat

*   URL:
    [https://github.com/phelber/eurosat](https://github.com/phelber/eurosat)
*   `DatasetBuilder`:
    [`tfds.image.eurosat.Eurosat`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/eurosat.py)

`eurosat` is configured with `tfds.image.eurosat.EurosatConfig` and has the
following configurations predefined (defaults to the first one):

*   `rgb` (`v2.0.0`) (`Size: 89.91 MiB`): Sentinel-2 RGB channels

*   `all` (`v2.0.0`) (`Size: 1.93 GiB`): 13 Sentinel-2 channels

## `eurosat/rgb`

Sentinel-2 RGB channels

### Statistics

Split | Examples
:---- | -------:
ALL   | 27,000
TRAIN | 27,000

### Features

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(64, 64, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://github.com/phelber/eurosat](https://github.com/phelber/eurosat)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `eurosat/all`

13 Sentinel-2 channels

### Statistics

Split | Examples
:---- | -------:
ALL   | 27,000
TRAIN | 27,000

### Features

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'sentinel2': Tensor(shape=[64, 64, 13], dtype=tf.float32),
})
```

### Urls

*   [https://github.com/phelber/eurosat](https://github.com/phelber/eurosat)

### Supervised keys (for `as_supervised=True`)

`(u'sentinel2', u'label')`

## Citation
```
@misc{helber2017eurosat,
    title={EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification},
    author={Patrick Helber and Benjamin Bischke and Andreas Dengel and Damian Borth},
    year={2017},
    eprint={1709.00029},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

--------------------------------------------------------------------------------
