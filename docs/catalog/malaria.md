<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="malaria" />
  <meta itemprop="description" content="The Malaria dataset contains a total of 27,558 cell images&#10;with equal instances of parasitized and uninfected cells from the thin blood &#10;smear slide images of segmented cells.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('malaria', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/malaria" />
  <meta itemprop="sameAs" content="https://lhncbc.nlm.nih.gov/publication/pub9932" />
  <meta itemprop="citation" content="@article{rajaraman2018pre,&#10;  title={Pre-trained convolutional neural networks as feature extractors toward &#10;  improved malaria parasite detection in thin blood smear images},&#10;  author={Rajaraman, Sivaramakrishnan and Antani, Sameer K and Poostchi, Mahdieh&#10;  and Silamut, Kamolrat and Hossain, Md A and Maude, Richard J and Jaeger, &#10;  Stefan and Thoma, George R},&#10;  journal={PeerJ},&#10;  volume={6},&#10;  pages={e4568},&#10;  year={2018},&#10;  publisher={PeerJ Inc.}&#10;}&#10;" />
</div>
# `malaria`

The Malaria dataset contains a total of 27,558 cell images with equal instances
of parasitized and uninfected cells from the thin blood smear slide images of
segmented cells.

*   URL:
    [https://lhncbc.nlm.nih.gov/publication/pub9932](https://lhncbc.nlm.nih.gov/publication/pub9932)
*   `DatasetBuilder`:
    [`tfds.image.malaria.Malaria`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/malaria.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

*   Size: `337.08 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 27,558
TRAIN | 27,558

## Homepage

*   [https://lhncbc.nlm.nih.gov/publication/pub9932](https://lhncbc.nlm.nih.gov/publication/pub9932)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation

```
@article{rajaraman2018pre,
  title={Pre-trained convolutional neural networks as feature extractors toward
  improved malaria parasite detection in thin blood smear images},
  author={Rajaraman, Sivaramakrishnan and Antani, Sameer K and Poostchi, Mahdieh
  and Silamut, Kamolrat and Hossain, Md A and Maude, Richard J and Jaeger,
  Stefan and Thoma, George R},
  journal={PeerJ},
  volume={6},
  pages={e4568},
  year={2018},
  publisher={PeerJ Inc.}
}
```

--------------------------------------------------------------------------------
