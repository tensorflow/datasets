<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lsun" />
  <meta itemprop="description" content="Large scale images showing different objects from given categories like bedroom, tower etc." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lsun" />
  <meta itemprop="sameAs" content="https://www.yf.io/p/lsun" />
</div>

# `lsun`

Large scale images showing different objects from given categories like bedroom,
tower etc.

*   URL: [https://www.yf.io/p/lsun](https://www.yf.io/p/lsun)
*   `DatasetBuilder`:
    [`tfds.image.lsun.Lsun`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/lsun.py)

`lsun` is configured with `tfds.image.lsun.BuilderConfig` and has the following
configurations predefined (defaults to the first one):

*   `classroom` (`v0.1.1`) (`Size: 3.06 GiB`): Images of category classroom

*   `bedroom` (`v0.1.1`) (`Size: 42.77 GiB`): Images of category bedroom

*   `bridge` (`v0.1.1`) (`Size: 15.35 GiB`): Images of category bridge

*   `church_outdoor` (`v0.1.1`) (`Size: 2.29 GiB`): Images of category
    church_outdoor

*   `conference_room` (`v0.1.1`) (`Size: 3.78 GiB`): Images of category
    conference_room

*   `dining_room` (`v0.1.1`) (`Size: 10.80 GiB`): Images of category dining_room

*   `kitchen` (`v0.1.1`) (`Size: 33.34 GiB`): Images of category kitchen

*   `living_room` (`v0.1.1`) (`Size: 21.23 GiB`): Images of category living_room

*   `restaurant` (`v0.1.1`) (`Size: 12.57 GiB`): Images of category restaurant

*   `tower` (`v0.1.1`) (`Size: 11.19 GiB`): Images of category tower

## `lsun/classroom`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/bedroom`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/bridge`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/church_outdoor`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/conference_room`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/dining_room`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/kitchen`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/living_room`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/restaurant`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## `lsun/tower`

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 708,564
TRAIN      | 708,264
VALIDATION | 300

## Urls

*   [https://www.yf.io/p/lsun](https://www.yf.io/p/lsun)

## Supervised keys (for `as_supervised=True`)

`None`

## Citation

```
@article{journals/corr/YuZSSX15,
  added-at = {2018-08-13T00:00:00.000+0200},
  author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
  biburl = {https://www.bibsonomy.org/bibtex/2446d4ffb99a5d7d2ab6e5417a12e195f/dblp},
  ee = {http://arxiv.org/abs/1506.03365},
  interhash = {3e9306c4ce2ead125f3b2ab0e25adc85},
  intrahash = {446d4ffb99a5d7d2ab6e5417a12e195f},
  journal = {CoRR},
  keywords = {dblp},
  timestamp = {2018-08-14T15:08:59.000+0200},
  title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop.},
  url = {http://dblp.uni-trier.de/db/journals/corr/corr1506.html#YuZSSX15},
  volume = {abs/1506.03365},
  year = 2015
}
```

--------------------------------------------------------------------------------
