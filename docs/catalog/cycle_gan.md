<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cycle_gan" />
  <meta itemprop="description" content="Dataset with images from 2 classes (see config name for information on the specific class)" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cycle_gan" />
  <meta itemprop="sameAs" content="https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/" />
</div>

# `cycle_gan`

Dataset with images from 2 classes (see config name for information on the
specific class)

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

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/summer2winter_yosemite`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/horse2zebra`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/monet2photo`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/cezanne2photo`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/ukiyoe2photo`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/vangogh2photo`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/maps`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/cityscapes`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/facades`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `cycle_gan/iphone2dslr_flower`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split  | Examples
:----- | -------:
ALL    | 6,186
TRAINB | 3,325
TRAINA | 1,812
TESTA  | 569
TESTB  | 480

## Urls

*   [https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/)

## Supervised keys (for `as_supervised=True`)
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
