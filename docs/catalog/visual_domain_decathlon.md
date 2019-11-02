<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="visual_domain_decathlon" />
  <meta itemprop="description" content="This contains the 10 datasets used in the Visual Domain Decathlon, part of&#10;the PASCAL in Detail Workshop Challenge (CVPR 2017).&#10;The goal of this challenge is to solve simultaneously ten image classification&#10;problems representative of very different visual domains.&#10;&#10;Some of the datasets included here are also available as separate datasets in&#10;TFDS. However, notice that images were preprocessed for the Visual Domain&#10;Decathlon (resized isotropically to have a shorter size of 72 pixels) and&#10;might have different train/validation/test splits. Here we use the official&#10;splits for the competition.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('visual_domain_decathlon', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/visual_domain_decathlon" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/decathlon/" />
  <meta itemprop="citation" content="@ONLINE{hakanbilensylvestrerebuffitomasjakab2017,&#10;    author = &quot;Hakan Bilen, Sylvestre Rebuffi, Tomas Jakab&quot;,&#10;    title  = &quot;Visual Domain Decathlon&quot;,&#10;    year   = &quot;2017&quot;,&#10;    url    = &quot;https://www.robots.ox.ac.uk/~vgg/decathlon/&quot;&#10;}&#10;" />
</div>
# `visual_domain_decathlon`

This contains the 10 datasets used in the Visual Domain Decathlon, part of the
PASCAL in Detail Workshop Challenge (CVPR 2017). The goal of this challenge is
to solve simultaneously ten image classification problems representative of very
different visual domains.

Some of the datasets included here are also available as separate datasets in
TFDS. However, notice that images were preprocessed for the Visual Domain
Decathlon (resized isotropically to have a shorter size of 72 pixels) and might
have different train/validation/test splits. Here we use the official splits for
the competition.

*   URL:
    [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)
*   `DatasetBuilder`:
    [`tfds.image.visual_domain_decathlon.VisualDomainDecathlon`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/visual_domain_decathlon.py)

`visual_domain_decathlon` is configured with
`tfds.image.visual_domain_decathlon.VisualDomainDecathlonConfig` and has the
following configurations predefined (defaults to the first one):

*   `aircraft` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "Aircraft", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `cifar100` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "CIFAR-100", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `daimlerpedcls` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "Daimler
    Pedestrian Classification", with images resized isotropically to have a
    shorter size of 72 pixels.

*   `dtd` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "Describable Textures",
    with images resized isotropically to have a shorter size of 72 pixels.

*   `gtsrb` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "German Traffic Signs",
    with images resized isotropically to have a shorter size of 72 pixels.

*   `imagenet12` (`v1.1.0`) (`Size: 6.40 GiB`): Data based on "Imagenet", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `omniglot` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "Omniglot", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `svhn` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "Street View House
    Numbers", with images resized isotropically to have a shorter size of 72
    pixels.

*   `ucf101` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "UCF101 Dynamic
    Images", with images resized isotropically to have a shorter size of 72
    pixels.

*   `vgg-flowers` (`v1.1.0`) (`Size: 1.04 GiB`): Data based on "VGG-Flowers",
    with images resized isotropically to have a shorter size of 72 pixels.

## `visual_domain_decathlon/aircraft`

Data based on "Aircraft", with images resized isotropically to have a shorter
size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 10,000
TRAIN      | 3,334
TEST       | 3,333
VALIDATION | 3,333

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/cifar100`

Data based on "CIFAR-100", with images resized isotropically to have a shorter
size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 60,000
TRAIN      | 40,000
TEST       | 10,000
VALIDATION | 10,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/daimlerpedcls`

Data based on "Daimler Pedestrian Classification", with images resized
isotropically to have a shorter size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 49,000
TRAIN      | 23,520
TEST       | 19,600
VALIDATION | 5,880

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/dtd`

Data based on "Describable Textures", with images resized isotropically to have
a shorter size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,640
TEST       | 1,880
TRAIN      | 1,880
VALIDATION | 1,880

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/gtsrb`

Data based on "German Traffic Signs", with images resized isotropically to have
a shorter size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 51,839
TRAIN      | 31,367
TEST       | 12,630
VALIDATION | 7,842

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=43),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/imagenet12`

Data based on "Imagenet", with images resized isotropically to have a shorter
size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,329,405
TRAIN      | 1,232,167
VALIDATION | 49,000
TEST       | 48,238

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/omniglot`

Data based on "Omniglot", with images resized isotropically to have a shorter
size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 32,460
TRAIN      | 17,853
TEST       | 8,115
VALIDATION | 6,492

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1623),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/svhn`

Data based on "Street View House Numbers", with images resized isotropically to
have a shorter size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 99,289
TRAIN      | 47,217
VALIDATION | 26,040
TEST       | 26,032

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/ucf101`

Data based on "UCF101 Dynamic Images", with images resized isotropically to have
a shorter size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 13,320
TRAIN      | 7,585
TEST       | 3,783
VALIDATION | 1,952

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=101),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `visual_domain_decathlon/vgg-flowers`

Data based on "VGG-Flowers", with images resized isotropically to have a shorter
size of 72 pixels.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 8,189
TEST       | 6,149
TRAIN      | 1,020
VALIDATION | 1,020

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
    'name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@ONLINE{hakanbilensylvestrerebuffitomasjakab2017,
    author = "Hakan Bilen, Sylvestre Rebuffi, Tomas Jakab",
    title  = "Visual Domain Decathlon",
    year   = "2017",
    url    = "https://www.robots.ox.ac.uk/~vgg/decathlon/"
}
```

--------------------------------------------------------------------------------
