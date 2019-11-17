<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cycle_gan" />
  <meta itemprop="description" content="A dataset consisting of images from two classes A and B (For example: horses/zebras, apple/orange,...)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('cycle_gan', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cycle_gan" />
  <meta itemprop="sameAs" content="https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/ZhuPIE17,&#10;  author    = {Jun{-}Yan Zhu and&#10;               Taesung Park and&#10;               Phillip Isola and&#10;               Alexei A. Efros},&#10;  title     = {Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial&#10;               Networks},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1703.10593},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1703.10593},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1703.10593},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:06 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuPIE17},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
</div>
# `cycle_gan`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

*   URL:
    [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)
*   `DatasetBuilder`:
    [`tfds.image.cycle_gan.CycleGAN`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cycle_gan.py)

`cycle_gan` is configured with `tfds.image.cycle_gan.CycleGANConfig` and has the
following configurations predefined (defaults to the first one):

*   `apple2orange` (`v0.1.0`) (`Size: 74.82 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `summer2winter_yosemite` (`v0.1.0`) (`Size: 126.50 MiB`): A dataset
    consisting of images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `horse2zebra` (`v0.1.0`) (`Size: 111.45 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `monet2photo` (`v0.1.0`) (`Size: 291.09 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `cezanne2photo` (`v0.1.0`) (`Size: 266.92 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `ukiyoe2photo` (`v0.1.0`) (`Size: 279.38 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `vangogh2photo` (`v0.1.0`) (`Size: 292.39 MiB`): A dataset consisting of
    images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

*   `maps` (`v0.1.0`) (`Size: 1.38 GiB`): A dataset consisting of images from
    two classes A and B (For example: horses/zebras, apple/orange,...)

*   `cityscapes` (`v0.1.0`) (`Size: 266.65 MiB`): A dataset consisting of images
    from two classes A and B (For example: horses/zebras, apple/orange,...)

*   `facades` (`v0.1.0`) (`Size: 33.51 MiB`): A dataset consisting of images
    from two classes A and B (For example: horses/zebras, apple/orange,...)

*   `iphone2dslr_flower` (`v0.1.0`) (`Size: 324.22 MiB`): A dataset consisting
    of images from two classes A and B (For example: horses/zebras,
    apple/orange,...)

## `cycle_gan/apple2orange`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 2,528
TRAINB | 1,019
TRAINA | 995
TESTA  | 266
TESTB  | 248

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/summer2winter_yosemite`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 2,740
TRAINA | 1,231
TRAINB | 962
TESTA  | 309
TESTB  | 238

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/horse2zebra`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 2,661
TRAINB | 1,334
TRAINA | 1,067
TESTB  | 140
TESTA  | 120

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/monet2photo`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 8,231
TRAINB | 6,287
TRAINA | 1,072
TESTB  | 751
TESTA  | 121

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/cezanne2photo`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 7,621
TRAINB | 6,287
TESTB  | 751
TRAINA | 525
TESTA  | 58

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/ukiyoe2photo`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 7,863
TRAINB | 6,287
TESTB  | 751
TRAINA | 562
TESTA  | 263

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/vangogh2photo`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 7,838
TRAINB | 6,287
TESTB  | 751
TESTA  | 400
TRAINA | 400

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/maps`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 4,388
TESTA  | 1,098
TESTB  | 1,098
TRAINA | 1,096
TRAINB | 1,096

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/cityscapes`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 6,950
TRAINA | 2,975
TRAINB | 2,975
TESTA  | 500
TESTB  | 500

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/facades`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 1,012
TRAINA | 400
TRAINB | 400
TESTA  | 106
TESTB  | 106

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `cycle_gan/iphone2dslr_flower`

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

Versions:

*   **`0.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split  | Examples
:----- | -------:
ALL    | 6,186
TRAINB | 3,325
TRAINA | 1,812
TESTA  | 569
TESTB  | 480

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

### Homepage

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{DBLP:journals/corr/ZhuPIE17,
  author    = {Jun{-}Yan Zhu and
               Taesung Park and
               Phillip Isola and
               Alexei A. Efros},
  title     = {Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial
               Networks},
  journal   = {CoRR},
  volume    = {abs/1703.10593},
  year      = {2017},
  url       = {http://arxiv.org/abs/1703.10593},
  archivePrefix = {arXiv},
  eprint    = {1703.10593},
  timestamp = {Mon, 13 Aug 2018 16:48:06 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuPIE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
