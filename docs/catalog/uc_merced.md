<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="uc_merced" />
  <meta itemprop="description" content="UC Merced is a 21 class land use remote sensing image dataset, with 100 images&#10;per class. The images were manually extracted from large images from the USGS&#10;National Map Urban Area Imagery collection for various urban areas around the&#10;country. The pixel resolution of this public domain imagery is 0.3 m.&#10;Each image measures 256x256 pixels.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('uc_merced', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/uc_merced" />
  <meta itemprop="sameAs" content="http://weegee.vision.ucmerced.edu/datasets/landuse.html" />
  <meta itemprop="citation" content="@InProceedings{Nilsback08,&#10;   author = &quot;Yang, Yi and Newsam, Shawn&quot;,&#10;   title = &quot;Bag-Of-Visual-Words and Spatial Extensions for Land-Use Classification&quot;,&#10;   booktitle = &quot;ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM GIS)&quot;,&#10;   year = &quot;2010&quot;,&#10;}" />
</div>
# `uc_merced`

UC Merced is a 21 class land use remote sensing image dataset, with 100 images
per class. The images were manually extracted from large images from the USGS
National Map Urban Area Imagery collection for various urban areas around the
country. The pixel resolution of this public domain imagery is 0.3 m. Each image
measures 256x256 pixels.

*   URL:
    [http://weegee.vision.ucmerced.edu/datasets/landuse.html](http://weegee.vision.ucmerced.edu/datasets/landuse.html)
*   `DatasetBuilder`:
    [`tfds.image.uc_merced.UcMerced`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/uc_merced.py)
*   Version: `v0.0.1`
*   Versions:

    *   **`0.0.1`** (default):
    *   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `317.07 MiB`

## Features
```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=21),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 2,100
TRAIN | 2,100

## Homepage

*   [http://weegee.vision.ucmerced.edu/datasets/landuse.html](http://weegee.vision.ucmerced.edu/datasets/landuse.html)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@InProceedings{Nilsback08,
   author = "Yang, Yi and Newsam, Shawn",
   title = "Bag-Of-Visual-Words and Spatial Extensions for Land-Use Classification",
   booktitle = "ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM GIS)",
   year = "2010",
}
```

--------------------------------------------------------------------------------
