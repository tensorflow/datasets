<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagewang" />
  <meta itemprop="description" content="Imagewang contains Imagenette and Imagewoof combined&#10;Image网 (pronounced &quot;Imagewang&quot;; 网 means &quot;net&quot; in Chinese) contains Imagenette&#10;and Imagewoof combined, but with some twists that make it into a tricky&#10;semi-supervised unbalanced classification problem:&#10;&#10;* The validation set is the same as Imagewoof (i.e. 30% of Imagewoof images);&#10;  there are no Imagenette images in the validation set (they&#x27;re all in the&#10;  training set)&#10;* Only 10% of Imagewoof images are in the training set!&#10;* The remaining are in the unsup (&quot;unsupervised&quot;) directory, and you can not&#10;  use their labels in training!&#10;* It&#x27;s even hard to type and hard to say!&#10;&#10;The dataset comes in three variants:&#10;  * Full size&#10;  * 320 px&#10;  * 160 px&#10;This dataset consists of the Imagenette dataset {size} variant.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagewang&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagewang" />
  <meta itemprop="sameAs" content="https://github.com/fastai/imagenette" />
  <meta itemprop="citation" content="&#10;@misc{imagewang,&#10;  author    = &quot;Jeremy Howard&quot;,&#10;  title     = &quot;Imagewang&quot;,&#10;  url       = &quot;https://github.com/fastai/imagenette/&quot;&#10;}&#10;" />
</div>
# `imagewang`

*   URL:
    [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)
*   `DatasetBuilder`:
    [`tfds.image.imagewang.Imagewang`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/imagewang.py)

`imagewang` is configured with `tfds.image.imagewang.ImagewangConfig` and has
the following configurations predefined (defaults to the first one):

*   `full-size` (`v2.0.0`) (`Size: 1.97 GiB`): Imagewang contains Imagenette and
    Imagewoof combined.

*   `320px` (`v2.0.0`) (`Size: 460.81 MiB`): Imagewang contains Imagenette and
    Imagewoof combined.

*   `160px` (`v2.0.0`) (`Size: 140.40 MiB`): Imagewang contains Imagenette and
    Imagewoof combined.

## `imagewang/full-size`
Imagewang contains Imagenette and Imagewoof combined.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 18,598
TRAIN      | 14,669
VALIDATION | 3,929

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`('image', 'label')`

## `imagewang/320px`
Imagewang contains Imagenette and Imagewoof combined.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 18,598
TRAIN      | 14,669
VALIDATION | 3,929

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`('image', 'label')`

## `imagewang/160px`
Imagewang contains Imagenette and Imagewoof combined.

Versions:

*   **`2.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 18,598
TRAIN      | 14,669
VALIDATION | 3,929

### Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
})
```

### Homepage

*   [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

### Supervised keys (for `as_supervised=True`)
`('image', 'label')`

## Citation
```
@misc{imagewang,
  author    = "Jeremy Howard",
  title     = "Imagewang",
  url       = "https://github.com/fastai/imagenette/"
}
```

--------------------------------------------------------------------------------
