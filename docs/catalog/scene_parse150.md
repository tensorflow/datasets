<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scene_parse150" />
  <meta itemprop="description" content="&#10;Scene parsing is to segment and parse an image into different image regions&#10;associated with semantic categories, such as sky, road, person, and bed.&#10;MIT Scene Parsing Benchmark (SceneParse150) provides a standard training and&#10;evaluation platform for the algorithms of scene parsing.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scene_parse150" />
  <meta itemprop="sameAs" content="http://sceneparsing.csail.mit.edu/" />
</div>

# `scene_parse150`

Scene parsing is to segment and parse an image into different image regions
associated with semantic categories, such as sky, road, person, and bed. MIT
Scene Parsing Benchmark (SceneParse150) provides a standard training and
evaluation platform for the algorithms of scene parsing.

*   URL:
    [http://sceneparsing.csail.mit.edu/](http://sceneparsing.csail.mit.edu/)
*   `DatasetBuilder`:
    [`tfds.image.scene_parse_150.SceneParse150`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/scene_parse_150.py)
*   Version: `v1.0.0`
*   Size: `936.97 MiB`

## Features
```python
FeaturesDict({
    'annotation': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 22,210
TRAIN | 20,210
TEST  | 2,000

## Urls

*   [http://sceneparsing.csail.mit.edu/](http://sceneparsing.csail.mit.edu/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'annotation')`

## Citation
```
@inproceedings{zhou2017scene,
title={Scene Parsing through ADE20K Dataset},
author={Zhou, Bolei and Zhao, Hang and Puig, Xavier and Fidler, Sanja and Barriuso, Adela and Torralba, Antonio},
booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
year={2017}
}
```

--------------------------------------------------------------------------------
