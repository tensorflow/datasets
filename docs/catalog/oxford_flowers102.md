<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="oxford_flowers102" />
  <meta itemprop="description" content="&#10;The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly occurring&#10;in the United Kingdom. Each class consists of between 40 and 258 images. The images have&#10;large scale, pose and light variations. In addition, there are categories that have large&#10;variations within the category and several very similar categories.&#10;&#10;The dataset is divided into a training set, a validation set and a test set.&#10;The training set and validation set each consist of 10 images per class (totalling 1030 images each).&#10;The test set consist of the remaining 6129 images (minimum 20 per class).&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/oxford_flowers102" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/flowers/102/" />
</div>

# `oxford_flowers102`

The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly
occurring in the United Kingdom. Each class consists of between 40 and 258
images. The images have large scale, pose and light variations. In addition,
there are categories that have large variations within the category and several
very similar categories.

The dataset is divided into a training set, a validation set and a test set. The
training set and validation set each consist of 10 images per class (totalling
1030 images each). The test set consist of the remaining 6129 images (minimum 20
per class).

*   URL:
    [https://www.robots.ox.ac.uk/~vgg/data/flowers/102/](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)
*   `DatasetBuilder`:
    [`tfds.image.oxford_flowers102.OxfordFlowers102`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/oxford_flowers102.py)
*   Version: `v0.0.1`
*   Size: `336.76 MiB`

## Features
```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 8,189
TEST       | 6,149
VALIDATION | 1,020
TRAIN      | 1,020

## Urls

*   [https://www.robots.ox.ac.uk/~vgg/data/flowers/102/](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@InProceedings{Nilsback08,
   author = "Nilsback, M-E. and Zisserman, A.",
   title = "Automated Flower Classification over a Large Number of Classes",
   booktitle = "Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing",
   year = "2008",
   month = "Dec"
}
```

--------------------------------------------------------------------------------
