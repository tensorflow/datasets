<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech101" />
  <meta itemprop="description" content="Caltech-101 consists of pictures of objects belonging to 101 classes, plus&#10;one `background clutter` class. Each image is labelled with a single object.&#10;Each class contains roughly 40 to 800 images, totalling around 9k images.&#10;Images are of variable sizes, with typical edge lengths of 200-300 pixels.&#10;This version contains image-level labels only. The original dataset also&#10;contains bounding boxes.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech101" />
  <meta itemprop="sameAs" content="http://www.vision.caltech.edu/Image_Datasets/Caltech101/" />
</div>

# `caltech101`

Caltech-101 consists of pictures of objects belonging to 101 classes, plus one
`background clutter` class. Each image is labelled with a single object. Each
class contains roughly 40 to 800 images, totalling around 9k images. Images are
of variable sizes, with typical edge lengths of 200-300 pixels. This version
contains image-level labels only. The original dataset also contains bounding
boxes.

*   URL:
    [http://www.vision.caltech.edu/Image_Datasets/Caltech101/](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)
*   `DatasetBuilder`:
    [`tfds.image.caltech.Caltech101`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/caltech.py)
*   Version: `v1.1.0`
*   Size: `125.64 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/file_name': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 9,801
TEST  | 6,741
TRAIN | 3,060

## Urls

*   [http://www.vision.caltech.edu/Image_Datasets/Caltech101/](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{FeiFei2004LearningGV,
  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},
  author={Li Fei-Fei and Rob Fergus and Pietro Perona},
  journal={Computer Vision and Pattern Recognition Workshop},
  year={2004},
}
```

--------------------------------------------------------------------------------
