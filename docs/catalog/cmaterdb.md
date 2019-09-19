<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cmaterdb" />
  <meta itemprop="description" content="This dataset contains images of -&#10;  Handwritten Bangla numerals - balanced dataset of total 6000 Bangla numerals (32x32 RGB coloured, 6000 images), each having 600 images per class(per digit). &#10;  Handwritten Devanagari numerals - balanced dataset of total 3000 Devanagari numerals (32x32 RGB coloured, 3000 images), each having 300 images per class(per digit). &#10;  Handwritten Telugu numerals - balanced dataset of total 3000 Telugu numerals (32x32 RGB coloured, 3000 images), each having 300 images per class(per digit). &#10;&#10;CMATERdb is the pattern recognition database repository created at the 'Center for Microprocessor Applications for Training Education and Research' (CMATER) research lab, Jadavpur University, India.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cmaterdb" />
  <meta itemprop="sameAs" content="https://code.google.com/archive/p/cmaterdb/" />
</div>

# `cmaterdb`

This dataset contains images of - Handwritten Bangla numerals - balanced dataset
of total 6000 Bangla numerals (32x32 RGB coloured, 6000 images), each having 600
images per class(per digit). Handwritten Devanagari numerals - balanced dataset
of total 3000 Devanagari numerals (32x32 RGB coloured, 3000 images), each having
300 images per class(per digit). Handwritten Telugu numerals - balanced dataset
of total 3000 Telugu numerals (32x32 RGB coloured, 3000 images), each having 300
images per class(per digit).

CMATERdb is the pattern recognition database repository created at the 'Center
for Microprocessor Applications for Training Education and Research' (CMATER)
research lab, Jadavpur University, India.

*   URL:
    [https://code.google.com/archive/p/cmaterdb/](https://code.google.com/archive/p/cmaterdb/)
*   `DatasetBuilder`:
    [`tfds.image.cmaterdb.Cmaterdb`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cmaterdb.py)

`cmaterdb` is configured with `tfds.image.cmaterdb.CmaterdbConfig` and has the
following configurations predefined (defaults to the first one):

*   `bangla` (`v1.0.0`) (`Size: 573.81 KiB`): CMATERdb Bangla Numerals

*   `devanagari` (`v1.0.0`) (`Size: 275.29 KiB`): CMATERdb Devangari Numerals

*   `telugu` (`v1.0.0`) (`Size: 283.90 KiB`): CMATERdb Telugu Numerals

## `cmaterdb/bangla`

CMATERdb Bangla Numerals

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,000
TRAIN | 5,000
TEST  | 1,000

### Features

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://code.google.com/archive/p/cmaterdb/](https://code.google.com/archive/p/cmaterdb/)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `cmaterdb/devanagari`

CMATERdb Devangari Numerals

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,000
TRAIN | 2,500
TEST  | 500

### Features

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://code.google.com/archive/p/cmaterdb/](https://code.google.com/archive/p/cmaterdb/)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## `cmaterdb/telugu`

CMATERdb Telugu Numerals

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,000
TRAIN | 2,500
TEST  | 500

### Features

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

### Urls

*   [https://code.google.com/archive/p/cmaterdb/](https://code.google.com/archive/p/cmaterdb/)

### Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## Citation

```
@article{Das:2012:GAB:2161007.2161320,
  author = {Das, Nibaran and Sarkar, Ram and Basu, Subhadip and Kundu, Mahantapas
            and Nasipuri, Mita and Basu, Dipak Kumar},
  title = {A Genetic Algorithm Based Region Sampling for Selection of Local Features
          in Handwritten Digit Recognition Application},
  journal = {Appl. Soft Comput.},
  issue_date = {May, 2012},
  volume = {12},
  number = {5},
  month = may,
  year = {2012},
  issn = {1568-4946},
  pages = {1592--1606},
  numpages = {15},
  url = {http://dx.doi.org/10.1016/j.asoc.2011.11.030},
  doi = {10.1016/j.asoc.2011.11.030},
  acmid = {2161320},
  publisher = {Elsevier Science Publishers B. V.},
  address = {Amsterdam, The Netherlands, The Netherlands},
  keywords = {Feature selection, Genetic algorithm, N-Quality consensus,
  Optimal local regions, Region sampling, Variable sized local regions},
}
@article{Das:2012:SFC:2240301.2240421,
  author = {Das, Nibaran and Reddy, Jagan Mohan and Sarkar, Ram and Basu, Subhadip and Kundu,
            Mahantapas and Nasipuri, Mita and Basu, Dipak Kumar},
  title = {A Statistical-topological Feature Combination for Recognition of Handwritten Numerals},
  journal = {Appl. Soft Comput.},
  issue_date = {August, 2012},
  volume = {12},
  number = {8},
  month = aug,
  year = {2012},
  issn = {1568-4946},
  pages = {2486--2495},
  numpages = {10},
  url = {http://dx.doi.org/10.1016/j.asoc.2012.03.039},
  doi = {10.1016/j.asoc.2012.03.039},
  acmid = {2240421},
  publisher = {Elsevier Science Publishers B. V.},
  address = {Amsterdam, The Netherlands, The Netherlands},
  keywords = {Character recognition, Feature combination, MPCA, PCA, SVM, Statistical, Topological},
}
```

--------------------------------------------------------------------------------
