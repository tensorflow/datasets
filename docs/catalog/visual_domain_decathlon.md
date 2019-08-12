<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="visual_domain_decathlon" />
  <meta itemprop="description" content="This contains the 10 datasets used in the Visual Domain Decathlon, part of
the PASCAL in Detail Workshop Challenge (CVPR 2017).
The goal of this challenge is to solve simultaneously ten image classification
problems representative of very different visual domains.

Some of the datasets included here are also available as separate datasets in
TFDS. However, notice that images were preprocessed for the Visual Domain
Decathlon (resized isotropically to have a shorter size of 72 pixels) and
might have different train/validation/test splits. Here we use the official
splits for the competition." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/visual_domain_decathlon" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/decathlon/" />
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

*   `aircraft` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Aircraft", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `cifar100` (`v1.0.0`) (`Size: ?? GiB`): Data based on "CIFAR-100", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `daimlerpedcls` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Daimler
    Pedestrian Classification", with images resized isotropically to have a
    shorter size of 72 pixels.

*   `dtd` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Describable Textures",
    with images resized isotropically to have a shorter size of 72 pixels.

*   `gtsrb` (`v1.0.0`) (`Size: ?? GiB`): Data based on "German Traffic Signs",
    with images resized isotropically to have a shorter size of 72 pixels.

*   `imagenet12` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Imagenet", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `omniglot` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Omniglot", with
    images resized isotropically to have a shorter size of 72 pixels.

*   `svhn` (`v1.0.0`) (`Size: ?? GiB`): Data based on "Street View House
    Numbers", with images resized isotropically to have a shorter size of 72
    pixels.

*   `ucf101` (`v1.0.0`) (`Size: ?? GiB`): Data based on "UCF101 Dynamic Images",
    with images resized isotropically to have a shorter size of 72 pixels.

*   `vgg-flowers` (`v1.0.0`) (`Size: ?? GiB`): Data based on "VGG-Flowers", with
    images resized isotropically to have a shorter size of 72 pixels.

## `visual_domain_decathlon/aircraft`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/cifar100`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/daimlerpedcls`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/dtd`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/gtsrb`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=43),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/imagenet12`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/omniglot`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1623),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/svhn`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/ucf101`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=101),
    'name': Text(shape=(), dtype=tf.string),
})
```

## `visual_domain_decathlon/vgg-flowers`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
    'name': Text(shape=(), dtype=tf.string),
})
```

## Statistics
None computed

## Urls

*   [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)

## Supervised keys (for `as_supervised=True`)
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
