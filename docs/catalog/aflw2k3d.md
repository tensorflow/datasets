<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="aflw2k3d" />
  <meta itemprop="description" content="AFLW2000-3D is a dataset of 2000 images that have been annotated with image-level&#10;68-point 3D facial landmarks.&#10;This dataset is typically used for evaluation of 3D facial landmark detection&#10;models. The head poses are very diverse and often hard to be detected by a &#10;cnn-based face detector.&#10;The 2D landmarks are skipped in this dataset, since some of the data are not&#10;consistent to 21 points, as the original paper mentioned.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/aflw2k3d" />
  <meta itemprop="sameAs" content="http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm" />
</div>

# `aflw2k3d`

AFLW2000-3D is a dataset of 2000 images that have been annotated with
image-level 68-point 3D facial landmarks. This dataset is typically used for
evaluation of 3D facial landmark detection models. The head poses are very
diverse and often hard to be detected by a cnn-based face detector. The 2D
landmarks are skipped in this dataset, since some of the data are not consistent
to 21 points, as the original paper mentioned.

*   URL:
    [http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm)
*   `DatasetBuilder`:
    [`tfds.image.aflw2k3d.Aflw2k3d`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/aflw2k3d.py)
*   Version: `v1.0.0`
*   Size: `83.36 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(450, 450, 3), dtype=tf.uint8),
    'landmarks_68_3d_xy_normalized': Tensor(shape=(68, 2), dtype=tf.float32),
    'landmarks_68_3d_z': Tensor(shape=(68, 1), dtype=tf.float32),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 2,000
TRAIN | 2,000

## Urls

*   [http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm)

## Citation
```
@article{DBLP:journals/corr/ZhuLLSL15,
  author    = {Xiangyu Zhu and
               Zhen Lei and
               Xiaoming Liu and
               Hailin Shi and
               Stan Z. Li},
  title     = {Face Alignment Across Large Poses: {A} 3D Solution},
  journal   = {CoRR},
  volume    = {abs/1511.07212},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.07212},
  archivePrefix = {arXiv},
  eprint    = {1511.07212},
  timestamp = {Mon, 13 Aug 2018 16:48:23 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuLLSL15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
