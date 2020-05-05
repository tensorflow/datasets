<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="visual_domain_decathlon" />
  <meta itemprop="description" content="This contains the 10 datasets used in the Visual Domain Decathlon, part of&#10;the PASCAL in Detail Workshop Challenge (CVPR 2017).&#10;The goal of this challenge is to solve simultaneously ten image classification&#10;problems representative of very different visual domains.&#10;&#10;Some of the datasets included here are also available as separate datasets in&#10;TFDS. However, notice that images were preprocessed for the Visual Domain&#10;Decathlon (resized isotropically to have a shorter size of 72 pixels) and&#10;might have different train/validation/test splits. Here we use the official&#10;splits for the competition.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;visual_domain_decathlon&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/visual_domain_decathlon" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/decathlon/" />
  <meta itemprop="citation" content="@ONLINE{hakanbilensylvestrerebuffitomasjakab2017,&#10;    author = &quot;Hakan Bilen, Sylvestre Rebuffi, Tomas Jakab&quot;,&#10;    title  = &quot;Visual Domain Decathlon&quot;,&#10;    year   = &quot;2017&quot;,&#10;    url    = &quot;https://www.robots.ox.ac.uk/~vgg/decathlon/&quot;&#10;}" />
</div>

# `visual_domain_decathlon`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

This contains the 10 datasets used in the Visual Domain Decathlon, part of the
PASCAL in Detail Workshop Challenge (CVPR 2017). The goal of this challenge is
to solve simultaneously ten image classification problems representative of very
different visual domains.

Some of the datasets included here are also available as separate datasets in
TFDS. However, notice that images were preprocessed for the Visual Domain
Decathlon (resized isotropically to have a shorter size of 72 pixels) and might
have different train/validation/test splits. Here we use the official splits for
the competition.

*   **Homepage**:
    [https://www.robots.ox.ac.uk/~vgg/decathlon/](https://www.robots.ox.ac.uk/~vgg/decathlon/)
*   **Source code**:
    [`tfds.image_classification.visual_domain_decathlon.VisualDomainDecathlon`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/visual_domain_decathlon.py)
*   **Versions**:
    *   **`1.2.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        No release notes.
*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`
*   **Citation**:

```
@ONLINE{hakanbilensylvestrerebuffitomasjakab2017,
    author = "Hakan Bilen, Sylvestre Rebuffi, Tomas Jakab",
    title  = "Visual Domain Decathlon",
    year   = "2017",
    url    = "https://www.robots.ox.ac.uk/~vgg/decathlon/"
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## visual_domain_decathlon/aircraft (default config)

*   **Config description**: Data based on "Aircraft", with images resized
    isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/cifar100

*   **Config description**: Data based on "CIFAR-100", with images resized
    isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/daimlerpedcls

*   **Config description**: Data based on "Daimler Pedestrian Classification",
    with images resized isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/dtd

*   **Config description**: Data based on "Describable Textures", with images
    resized isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/gtsrb

*   **Config description**: Data based on "German Traffic Signs", with images
    resized isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=43),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/imagenet12

*   **Config description**: Data based on "Imagenet", with images resized
    isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/omniglot

*   **Config description**: Data based on "Omniglot", with images resized
    isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1623),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/svhn

*   **Config description**: Data based on "Street View House Numbers", with
    images resized isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/ucf101

*   **Config description**: Data based on "UCF101 Dynamic Images", with images
    resized isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=101),
    'name': Text(shape=(), dtype=tf.string),
})
```

## visual_domain_decathlon/vgg-flowers

*   **Config description**: Data based on "VGG-Flowers", with images resized
    isotropically to have a shorter size of 72 pixels.

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
    'name': Text(shape=(), dtype=tf.string),
})
```
