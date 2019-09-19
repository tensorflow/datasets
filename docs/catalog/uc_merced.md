<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="uc_merced" />
  <meta itemprop="description" content="UC Merced is a 21 class land use remote sensing image dataset, with 100 images&#10;per class. The images were manually extracted from large images from the USGS&#10;National Map Urban Area Imagery collection for various urban areas around the&#10;country. The pixel resolution of this public domain imagery is 0.3 m.&#10;Each image measures 256x256 pixels." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/uc_merced" />
  <meta itemprop="sameAs" content="http://weegee.vision.ucmerced.edu/datasets/landuse.html" />
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

## Urls

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
