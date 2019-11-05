<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="places365_small" />
  <meta itemprop="description" content="The Places365-Standard dataset contains 1.8 million train images from 365 scene categories,which are used to train the Places365 CNNs.There are 50 images per category in the validation set and 900 images per category in the testing set.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('places365_small', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/places365_small" />
  <meta itemprop="sameAs" content="http://places2.csail.mit.edu/" />
  <meta itemprop="citation" content="&#10; @article{zhou2017places,&#10;  title={Places: A 10 million Image Database for Scene Recognition},&#10;  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},&#10;  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},&#10;  year={2017},&#10;  publisher={IEEE}&#10;}&#10;&#10;" />
</div>
# `places365_small`

The Places365-Standard dataset contains 1.8 million train images from 365 scene
categories,which are used to train the Places365 CNNs.There are 50 images per
category in the validation set and 900 images per category in the testing set.

*   URL: [http://places2.csail.mit.edu/](http://places2.csail.mit.edu/)
*   `DatasetBuilder`:
    [`tfds.image.places365_small.Places365Small`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/places365_small.py)
*   Version: `v2.0.0`
*   Versions:

    *   **`2.0.0`** (default):

*   Size: `?? GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=365),
})
```

## Statistics
None computed

## Homepage

*   [http://places2.csail.mit.edu/](http://places2.csail.mit.edu/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{zhou2017places,
  title={Places: A 10 million Image Database for Scene Recognition},
  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2017},
  publisher={IEEE}
}
```

--------------------------------------------------------------------------------
