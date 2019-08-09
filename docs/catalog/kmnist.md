<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kmnist" />
  <meta itemprop="description" content="Kuzushiji-MNIST is a drop-in replacement for the MNIST dataset (28x28 grayscale, 70,000 images), provided in the original MNIST format as well as a NumPy format. Since MNIST restricts us to 10 classes, we chose one character to represent each of the 10 rows of Hiragana when creating Kuzushiji-MNIST." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kmnist" />
  <meta itemprop="sameAs" content="http://codh.rois.ac.jp/kmnist/index.html.en" />
</div>

# `kmnist`

Kuzushiji-MNIST is a drop-in replacement for the MNIST dataset (28x28 grayscale,
70,000 images), provided in the original MNIST format as well as a NumPy format.
Since MNIST restricts us to 10 classes, we chose one character to represent each
of the 10 rows of Hiragana when creating Kuzushiji-MNIST.

*   URL:
    [http://codh.rois.ac.jp/kmnist/index.html.en](http://codh.rois.ac.jp/kmnist/index.html.en)
*   `DatasetBuilder`:
    [`tfds.image.mnist.KMNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/mnist.py)
*   Version: `v1.0.0`
*   Size: `20.26 MiB`

## Features

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 70,000
TRAIN | 60,000
TEST  | 10,000

## Urls

*   [http://codh.rois.ac.jp/kmnist/index.html.en](http://codh.rois.ac.jp/kmnist/index.html.en)

## Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## Citation

```
@online{clanuwat2018deep,
  author       = {Tarin Clanuwat and Mikel Bober-Irizar and Asanobu Kitamoto and Alex Lamb and Kazuaki Yamamoto and David Ha},
  title        = {Deep Learning for Classical Japanese Literature},
  date         = {2018-12-03},
  year         = {2018},
  eprintclass  = {cs.CV},
  eprinttype   = {arXiv},
  eprint       = {cs.CV/1812.01718},
}
```

--------------------------------------------------------------------------------
