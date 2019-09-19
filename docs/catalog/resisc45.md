<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="resisc45" />
  <meta itemprop="description" content="RESISC45 dataset is a publicly available benchmark for Remote Sensing Image&#10;Scene Classification (RESISC), created by Northwestern Polytechnical University&#10;(NWPU). This dataset contains 31,500 images, covering 45 scene classes with 700&#10;images in each class." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/resisc45" />
  <meta itemprop="sameAs" content="http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html" />
</div>

# `resisc45`

RESISC45 dataset is a publicly available benchmark for Remote Sensing Image
Scene Classification (RESISC), created by Northwestern Polytechnical University
(NWPU). This dataset contains 31,500 images, covering 45 scene classes with 700
images in each class.

*   URL:
    [http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html](http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html)
*   `DatasetBuilder`:
    [`tfds.image.resisc45.Resisc45`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/resisc45.py)
*   Version: `v3.0.0`
*   Size: `?? GiB`

## Features
```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=45),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 31,500
TRAIN | 31,500

## Urls

*   [http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html](http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{Cheng_2017,
   title={Remote Sensing Image Scene Classification: Benchmark and State of the Art},
   volume={105},
   ISSN={1558-2256},
   url={http://dx.doi.org/10.1109/JPROC.2017.2675998},
   DOI={10.1109/jproc.2017.2675998},
   number={10},
   journal={Proceedings of the IEEE},
   publisher={Institute of Electrical and Electronics Engineers (IEEE)},
   author={Cheng, Gong and Han, Junwei and Lu, Xiaoqiang},
   year={2017},
   month={Oct},
   pages={1865-1883}
}
```

--------------------------------------------------------------------------------
