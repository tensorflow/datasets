<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lost_and_found" />
  <meta itemprop="description" content="&#10;The LostAndFound Dataset addresses the problem of detecting unexpected small obstacles on&#10;the road often caused by lost cargo. The dataset comprises 112 stereo video sequences&#10;with 2104 annotated frames (picking roughly every tenth frame from the recorded data).&#10;&#10;The dataset is designed analogous to the 'Cityscapes' dataset. The datset provides:&#10;- stereo image pairs in either 8 or 16 bit color resolution&#10;- precomputed disparity maps&#10;- coarse semantic labels for objects and street&#10;&#10;Descriptions of the labels are given here: http://www.6d-vision.com/laf_table.pdf&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('lost_and_found', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lost_and_found" />
  <meta itemprop="sameAs" content="http://www.6d-vision.com/lostandfounddataset" />
  <meta itemprop="citation" content="&#10;@inproceedings{pinggera2016lost,&#10;  title={Lost and found: detecting small road hazards for self-driving vehicles},&#10;  author={Pinggera, Peter and Ramos, Sebastian and Gehrig, Stefan and Franke, Uwe and Rother, Carsten and Mester, Rudolf},&#10;  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},&#10;  year={2016}&#10;}&#10;" />
</div>
# `lost_and_found`

*   URL:
    [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)
*   `DatasetBuilder`:
    [`tfds.image.lost_and_found.LostAndFound`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/lost_and_found.py)

`lost_and_found` is configured with
`tfds.image.lost_and_found.LostAndFoundConfig` and has the following
configurations predefined (defaults to the first one):

*   `semantic_segmentation` (`v1.0.0`) (`Size: 5.44 GiB`): Lost and Found
    semantic segmentation dataset.

*   `stereo_disparity` (`v1.0.0`) (`Size: 12.16 GiB`): Lost and Found stereo
    images and disparity maps.

*   `full` (`v1.0.0`) (`Size: 12.19 GiB`): Full Lost and Found dataset.

*   `full_16bit` (`v1.0.0`) (`Size: 34.90 GiB`): Full Lost and Found dataset.

## `lost_and_found/semantic_segmentation`
Lost and Found semantic segmentation dataset.

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,239
TEST  | 1,203
TRAIN | 1,036

### Features
```python
FeaturesDict({
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
})
```

### Homepage

*   [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)

## `lost_and_found/stereo_disparity`
Lost and Found stereo images and disparity maps.

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,239
TEST  | 1,203
TRAIN | 1,036

### Features
```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
})
```

### Homepage

*   [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)

## `lost_and_found/full`
Full Lost and Found dataset.

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,239
TEST  | 1,203
TRAIN | 1,036

### Features
```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'instance_id': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
})
```

### Homepage

*   [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)

## `lost_and_found/full_16bit`
Full Lost and Found dataset.

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,239
TEST  | 1,203
TRAIN | 1,036

### Features
```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'image_id': Text(shape=(), dtype=tf.string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=tf.uint8),
    'instance_id': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=tf.uint8),
})
```

### Homepage

*   [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)

## Citation
```
@inproceedings{pinggera2016lost,
  title={Lost and found: detecting small road hazards for self-driving vehicles},
  author={Pinggera, Peter and Ramos, Sebastian and Gehrig, Stefan and Franke, Uwe and Rother, Carsten and Mester, Rudolf},
  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2016}
}
```

--------------------------------------------------------------------------------
