<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="binarized_mnist" />
  <meta itemprop="description" content="A specific binarization of the MNIST images originally used in&#10;(Salakhutdinov &amp; Murray, 2008). This dataset is frequently used to evaluate&#10;generative models of images, so labels are not provided.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/binarized_mnist" />
  <meta itemprop="sameAs" content="http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/" />
</div>

# `binarized_mnist`

A specific binarization of the MNIST images originally used in (Salakhutdinov &
Murray, 2008). This dataset is frequently used to evaluate generative models of
images, so labels are not provided.

*   URL:
    [http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/](http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/)
*   `DatasetBuilder`:
    [`tfds.image.binarized_mnist.BinarizedMNIST`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/binarized_mnist.py)
*   Version: `v1.0.0`
*   Size: `104.68 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 70,000
TRAIN      | 50,000
TEST       | 10,000
VALIDATION | 10,000

## Urls

*   [http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/](http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/)

## Citation
```
@inproceedings{salakhutdinov2008quantitative,
title={On the quantitative analysis of deep belief networks},
author={Salakhutdinov, Ruslan and Murray, Iain},
booktitle={Proceedings of the 25th international conference on Machine learning},
pages={872--879},
year={2008},
organization={ACM}
}
```

--------------------------------------------------------------------------------
