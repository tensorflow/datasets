<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="places365_small" />
  <meta itemprop="description" content="The Places365-Standard dataset contains 1.8 million train images from 365 scene categories,which are used to train the Places365 CNNs.There are 50 images per category in the validation set and 900 images per category in the testing set." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/places365_small" />
  <meta itemprop="sameAs" content="http://data.csail.mit.edu/places/places365/" />
</div>

# `places365_small`

The Places365-Standard dataset contains 1.8 million train images from 365 scene
categories,which are used to train the Places365 CNNs.There are 50 images per
category in the validation set and 900 images per category in the testing set.

*   URL:
    [http://data.csail.mit.edu/places/places365/](http://data.csail.mit.edu/places/places365/)
*   `DatasetBuilder`:
    [`tfds.image.places365_small.Places365Small`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/places365_small.py)
*   Version: `v1.0.0`
*   Size: `?? GiB`

## Features

```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=366),
})
```

## Statistics

None computed

## Urls

*   [http://data.csail.mit.edu/places/places365/](http://data.csail.mit.edu/places/places365/)

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
