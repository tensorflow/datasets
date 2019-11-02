<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_resized" />
  <meta itemprop="description" content="This dataset consists of the ImageNet dataset resized to 8x8.&#10;The images here are the ones provided by Chrabaszcz et. al. using the box resize method.&#10;&#10;For [downsampled ImageNet](http://image-net.org/small/download.php) for unsupervised learning see `downsampled_imagenet`.&#10;&#10;WARNING: The integer labels used are defined by the authors and do not match&#10;those from the other ImageNet datasets provided by Tensorflow datasets.&#10;See the original [label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),&#10;and the [labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).&#10;Additionally, the original authors 1 index there labels which we convert to&#10;0 indexed by subtracting one.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('imagenet_resized', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_resized" />
  <meta itemprop="sameAs" content="https://patrykchrabaszcz.github.io/Imagenet32/" />
  <meta itemprop="citation" content="@article{chrabaszcz2017downsampled,&#10;  title={A downsampled variant of imagenet as an alternative to the cifar datasets},&#10;  author={Chrabaszcz, Patryk and Loshchilov, Ilya and Hutter, Frank},&#10;  journal={arXiv preprint arXiv:1707.08819},&#10;  year={2017}&#10;}&#10;" />
</div>
# `imagenet_resized`

*   URL:
    [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)
*   `DatasetBuilder`:
    [`tfds.image.imagenet_resized.ImagenetResized`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/imagenet_resized.py)

`imagenet_resized` is configured with
`tfds.image.imagenet_resized.ImagenetResizedConfig` and has the following
configurations predefined (defaults to the first one):

*   `8x8` (`v0.1.0`) (`Size: 237.11 MiB`): This dataset consists of the ImageNet
    dataset resized to 8x8. The images here are the ones provided by Chrabaszcz
    et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

*   `16x16` (`v0.1.0`) (`Size: 923.34 MiB`): This dataset consists of the
    ImageNet dataset resized to 16x16. The images here are the ones provided by
    Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

*   `32x32` (`v0.1.0`) (`Size: 3.46 GiB`): This dataset consists of the ImageNet
    dataset resized to 32x32. The images here are the ones provided by
    Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

*   `64x64` (`v0.1.0`) (`Size: 13.13 GiB`): This dataset consists of the
    ImageNet dataset resized to 64x64. The images here are the ones provided by
    Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

## `imagenet_resized/8x8`

This dataset consists of the ImageNet dataset resized to 8x8. The images here
are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,167
TRAIN      | 1,281,167
VALIDATION | 50,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(8, 8, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

### Homepage

*   [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `imagenet_resized/16x16`

This dataset consists of the ImageNet dataset resized to 16x16. The images here
are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,167
TRAIN      | 1,281,167
VALIDATION | 50,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(16, 16, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

### Homepage

*   [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `imagenet_resized/32x32`

This dataset consists of the ImageNet dataset resized to 32x32. The images here
are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,167
TRAIN      | 1,281,167
VALIDATION | 50,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

### Homepage

*   [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## `imagenet_resized/64x64`

This dataset consists of the ImageNet dataset resized to 64x64. The images here
are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,167
TRAIN      | 1,281,167
VALIDATION | 50,000

### Features
```python
FeaturesDict({
    'image': Image(shape=(64, 64, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

### Homepage

*   [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)

### Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{chrabaszcz2017downsampled,
  title={A downsampled variant of imagenet as an alternative to the cifar datasets},
  author={Chrabaszcz, Patryk and Loshchilov, Ilya and Hutter, Frank},
  journal={arXiv preprint arXiv:1707.08819},
  year={2017}
}
```

--------------------------------------------------------------------------------
