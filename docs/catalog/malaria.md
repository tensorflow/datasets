<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="malaria" />
  <meta itemprop="description" content="The Malaria dataset contains a total of 27,558 cell images&#10;with equal instances of parasitized and uninfected cells from the thin blood &#10;smear slide images of segmented cells." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/malaria" />
  <meta itemprop="sameAs" content="https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip" />
</div>

# `malaria`

The Malaria dataset contains a total of 27,558 cell images with equal instances
of parasitized and uninfected cells from the thin blood smear slide images of
segmented cells.

*   URL:
    [https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip](https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip)
*   `DatasetBuilder`:
    [`tfds.image.malaria.Malaria`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/malaria.py)
*   Version: `v1.0.0`
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

## Urls

*   [https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip](https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip)

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
