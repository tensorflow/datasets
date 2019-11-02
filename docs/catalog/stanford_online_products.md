<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_online_products" />
  <meta itemprop="description" content="Stanford Online Products Dataset&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('stanford_online_products', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_online_products" />
  <meta itemprop="sameAs" content="http://cvgl.stanford.edu/projects/lifted_struct/" />
  <meta itemprop="citation" content="@inproceedings{song2016deep,&#10; author    = {Song, Hyun Oh and Xiang, Yu and Jegelka, Stefanie and Savarese, Silvio},&#10; title     = {Deep Metric Learning via Lifted Structured Feature Embedding},&#10; booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10; year      = {2016}&#10;}&#10;" />
</div>
# `stanford_online_products`

Stanford Online Products Dataset

*   URL:
    [http://cvgl.stanford.edu/projects/lifted_struct/](http://cvgl.stanford.edu/projects/lifted_struct/)
*   `DatasetBuilder`:
    [`tfds.image.stanford_online_products.StanfordOnlineProducts`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/stanford_online_products.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

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

## Homepage

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
