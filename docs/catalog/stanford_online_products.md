<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_online_products" />
  <meta itemprop="description" content="Stanford Online Products Dataset" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_online_products" />
  <meta itemprop="sameAs" content="http://cvgl.stanford.edu/projects/lifted_struct/" />
</div>

# `stanford_online_products`

Stanford Online Products Dataset

*   URL:
    [http://cvgl.stanford.edu/projects/lifted_struct/](http://cvgl.stanford.edu/projects/lifted_struct/)
*   `DatasetBuilder`:
    [`tfds.image.stanford_online_products.StanfordOnlineProducts`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/stanford_online_products.py)
*   Version: `v1.0.0`
*   Size: `2.87 GiB`

## Features
```python
FeaturesDict({
    'class_id': ClassLabel(shape=(), dtype=tf.int64, num_classes=22634),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'super_class_id': ClassLabel(shape=(), dtype=tf.int64, num_classes=12),
    'super_class_id/num': ClassLabel(shape=(), dtype=tf.int64, num_classes=12),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 120,053
TEST  | 60,502
TRAIN | 59,551

## Urls

*   [http://cvgl.stanford.edu/projects/lifted_struct/](http://cvgl.stanford.edu/projects/lifted_struct/)

## Citation
```
@inproceedings{song2016deep,
 author    = {Song, Hyun Oh and Xiang, Yu and Jegelka, Stefanie and Savarese, Silvio},
 title     = {Deep Metric Learning via Lifted Structured Feature Embedding},
 booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 year      = {2016}
}
```

--------------------------------------------------------------------------------
