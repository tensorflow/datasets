<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_dogs" />
  <meta itemprop="description" content="The Stanford Dogs dataset contains images of 120 breeds of dogs from around&#10;the world. This dataset has been built using images and annotation from&#10;ImageNet for the task of fine-grained image categorization. There are&#10;20,580 images, out of which 12,000 are used for training and 8580 for&#10;testing. Class labels and bounding box annotations are provided&#10;for all the 12,000 images.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_dogs" />
  <meta itemprop="sameAs" content="http://vision.stanford.edu/aditya86/ImageNetDogs/main.html" />
</div>

# `stanford_dogs`

The Stanford Dogs dataset contains images of 120 breeds of dogs from around the
world. This dataset has been built using images and annotation from ImageNet for
the task of fine-grained image categorization. There are 20,580 images, out of
which 12,000 are used for training and 8580 for testing. Class labels and
bounding box annotations are provided for all the 12,000 images.

*   URL:
    [http://vision.stanford.edu/aditya86/ImageNetDogs/main.html](http://vision.stanford.edu/aditya86/ImageNetDogs/main.html)
*   `DatasetBuilder`:
    [`tfds.image.stanford_dogs.StanfordDogs`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/stanford_dogs.py)
*   Version: `v0.1.0`
*   Size: `778.12 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=120),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
    }),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 20,580
TRAIN | 12,000
TEST  | 8,580

## Urls

*   [http://vision.stanford.edu/aditya86/ImageNetDogs/main.html](http://vision.stanford.edu/aditya86/ImageNetDogs/main.html)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,
author = "Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and
          Li Fei-Fei",
title = "Novel Dataset for Fine-Grained Image Categorization",
booktitle = "First Workshop on Fine-Grained Visual Categorization,
             IEEE Conference on Computer Vision and Pattern Recognition",
year = "2011",
month = "June",
address = "Colorado Springs, CO",
}
@inproceedings{imagenet_cvpr09,
        AUTHOR = {Deng, J. and Dong, W. and Socher, R. and Li, L.-J. and
                  Li, K. and Fei-Fei, L.},
        TITLE = {{ImageNet: A Large-Scale Hierarchical Image Database}},
        BOOKTITLE = {CVPR09},
        YEAR = {2009},
        BIBSOURCE = "http://www.image-net.org/papers/imagenet_cvpr09.bib"}
```

--------------------------------------------------------------------------------
