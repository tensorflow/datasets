<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kitti" />
  <meta itemprop="description" content="Kitti contains a suite of vision tasks built using an autonomous driving&#10;platform. The full benchmark contains many tasks such as stereo, optical flow,&#10;visual odometry, etc. This dataset contains the object detection dataset,&#10;including the monocular images and bounding boxes. The dataset contains 7481&#10;training images annotated with 3D bounding boxes. A full description of the&#10;annotations can be found in the readme of the object development kit readme on&#10;the Kitti homepage.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kitti" />
  <meta itemprop="sameAs" content="http://www.cvlibs.net/datasets/kitti/" />
</div>

# `kitti`

Kitti contains a suite of vision tasks built using an autonomous driving
platform. The full benchmark contains many tasks such as stereo, optical flow,
visual odometry, etc. This dataset contains the object detection dataset,
including the monocular images and bounding boxes. The dataset contains 7481
training images annotated with 3D bounding boxes. A full description of the
annotations can be found in the readme of the object development kit readme on
the Kitti homepage.

*   URL:
    [http://www.cvlibs.net/datasets/kitti/](http://www.cvlibs.net/datasets/kitti/)
*   `DatasetBuilder`:
    [`tfds.image.kitti.Kitti`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/kitti.py)
*   Version: `v3.1.0`
*   Size: `11.71 GiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/file_name': Text(shape=(), dtype=tf.string),
    'objects': Sequence({
        'alpha': Tensor(shape=(), dtype=tf.float32),
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'dimensions': Tensor(shape=(3,), dtype=tf.float32),
        'location': Tensor(shape=(3,), dtype=tf.float32),
        'occluded': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
        'rotation_y': Tensor(shape=(), dtype=tf.float32),
        'truncated': Tensor(shape=(), dtype=tf.float32),
        'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=8),
    }),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 7,481
TRAIN      | 6,347
TEST       | 711
VALIDATION | 423

## Urls

*   [http://www.cvlibs.net/datasets/kitti/](http://www.cvlibs.net/datasets/kitti/)

## Citation
```
@inproceedings{Geiger2012CVPR,
  author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},
  title = {Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2012}
}
```

--------------------------------------------------------------------------------
