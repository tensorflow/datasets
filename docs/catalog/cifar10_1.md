<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cifar10_1" />
  <meta itemprop="description" content="The CIFAR-10.1 dataset is a new test set for CIFAR-10. CIFAR-10.1 contains roughly 2,000 new test images &#10;that were sampled after multiple years of research on the original CIFAR-10 dataset. The data collection &#10;for CIFAR-10.1 was designed to minimize distribution shift relative to the original dataset. We describe &#10;the creation of CIFAR-10.1 in the paper &quot;Do CIFAR-10 Classifiers Generalize to CIFAR-10?&quot;. &#10;The images in CIFAR-10.1 are a subset of the TinyImages dataset. &#10;There are currently two versions of the CIFAR-10.1 dataset: v4 and v6.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cifar10_1" />
  <meta itemprop="sameAs" content="https://github.com/modestyachts/CIFAR-10.1" />
</div>

# `cifar10_1`

The CIFAR-10.1 dataset is a new test set for CIFAR-10. CIFAR-10.1 contains
roughly 2,000 new test images that were sampled after multiple years of research
on the original CIFAR-10 dataset. The data collection for CIFAR-10.1 was
designed to minimize distribution shift relative to the original dataset. We
describe the creation of CIFAR-10.1 in the paper "Do CIFAR-10 Classifiers
Generalize to CIFAR-10?". The images in CIFAR-10.1 are a subset of the
TinyImages dataset. There are currently two versions of the CIFAR-10.1 dataset:
v4 and v6.

*   URL:
    [https://github.com/modestyachts/CIFAR-10.1](https://github.com/modestyachts/CIFAR-10.1)
*   `DatasetBuilder`:
    [`tfds.image.cifar10_1.Cifar10_1`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cifar10_1.py)

`cifar10_1` is configured with `tfds.image.cifar10_1.Cifar10_1Config` and has
the following configurations predefined (defaults to the first one):

*   `v4` (`v1.0.0`) (`Size: 5.93 MiB`): It is the first version of our dataset
    on which we tested any classifier. As mentioned above, this makes the v4
    dataset independent of the classifiers we evaluate. The numbers reported in
    the main sections of our paper use this version of the dataset. It was built
    from the top 25 TinyImages keywords for each class, which led to a slight
    class imbalance. The largest difference is that ships make up only 8% of the
    test set instead of 10%. v4 contains 2,021 images.

*   `v6` (`v1.0.0`) (`Size: 5.87 MiB`): It is derived from a slightly improved
    keyword allocation that is exactly class balanced. This version of the
    dataset corresponds to the results in Appendix D of our paper. v6 contains
    2,000 images.

## `cifar10_1/v4`

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

## `cifar10_1/v6`

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

## Statistics

Split | Examples
:---- | -------:
TEST  | 2,000
ALL   | 2,000

## Urls

*   [https://github.com/modestyachts/CIFAR-10.1](https://github.com/modestyachts/CIFAR-10.1)

## Supervised keys (for `as_supervised=True`)

`(u'image', u'label')`

## Citation

```
@article{recht2018cifar10.1,
  author = {Benjamin Recht and Rebecca Roelofs and Ludwig Schmidt and Vaishaal Shankar},
  title = {Do CIFAR-10 Classifiers Generalize to CIFAR-10?},
  year = {2018},
  note = {\url{https://arxiv.org/abs/1806.00451}},
}

@article{torralba2008tinyimages,
  author = {Antonio Torralba and Rob Fergus and William T. Freeman},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title = {80 Million Tiny Images: A Large Data Set for Nonparametric Object and Scene Recognition},
  year = {2008},
  volume = {30},
  number = {11},
  pages = {1958-1970}
}
```

--------------------------------------------------------------------------------
