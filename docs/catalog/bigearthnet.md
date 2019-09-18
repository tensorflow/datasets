<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bigearthnet" />
  <meta itemprop="description" content="The BigEarthNet is a new large-scale Sentinel-2 benchmark archive, consisting of&#10;590,326 Sentinel-2 image patches. The image patch size on the ground is&#10;1.2 x 1.2 km with variable image size depending on the channel resolution.&#10;This is a multi-label dataset with 43 imbalanced labels.&#10;&#10;To construct the BigEarthNet, 125 Sentinel-2&#10;tiles acquired between June 2017 and May 2018 over the 10 countries (Austria,&#10;Belgium, Finland, Ireland, Kosovo, Lithuania, Luxembourg, Portugal, Serbia,&#10;Switzerland) of Europe were initially selected. All the tiles were&#10;atmospherically corrected by the Sentinel-2 Level 2A product generation and&#10;formatting tool (sen2cor). Then, they were divided into 590,326 non-overlapping&#10;image patches. Each image patch was annotated by the multiple land-cover classes&#10;(i.e., multi-labels) that were provided from the CORINE Land Cover database of&#10;the year 2018 (CLC 2018).&#10;&#10;Bands and pixel resolution in meters:&#10;B01: Coastal aerosol; 60m&#10;B02: Blue; 10m&#10;B03: Green; 10m&#10;B04: Red; 10m&#10;B05: Vegetation red edge; 20m&#10;B06: Vegetation red edge; 20m&#10;B07: Vegetation red edge; 20m&#10;B08: NIR; 10m&#10;B09: Water vapor; 60m&#10;B11: SWIR; 20m&#10;B12: SWIR; 20m&#10;B8A: Narrow NIR; 20m&#10;&#10;License: Community Data License Agreement - Permissive, Version 1.0.&#10;&#10;URL: http://bigearth.net/&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bigearthnet" />
  <meta itemprop="sameAs" content="http://bigearth.net" />
</div>

# `bigearthnet`

The BigEarthNet is a new large-scale Sentinel-2 benchmark archive, consisting of
590,326 Sentinel-2 image patches. The image patch size on the ground is 1.2 x
1.2 km with variable image size depending on the channel resolution. This is a
multi-label dataset with 43 imbalanced labels.

To construct the BigEarthNet, 125 Sentinel-2
tiles acquired between June 2017 and May 2018 over the 10 countries (Austria,
Belgium, Finland, Ireland, Kosovo, Lithuania, Luxembourg, Portugal, Serbia,
Switzerland) of Europe were initially selected. All the tiles were
atmospherically corrected by the Sentinel-2 Level 2A product generation and
formatting tool (sen2cor). Then, they were divided into 590,326 non-overlapping
image patches. Each image patch was annotated by the multiple land-cover classes
(i.e., multi-labels) that were provided from the CORINE Land Cover database of
the year 2018 (CLC 2018).

Bands and pixel resolution in meters:
B01: Coastal aerosol; 60m
B02: Blue; 10m
B03: Green; 10m
B04: Red; 10m
B05: Vegetation red edge; 20m
B06: Vegetation red edge; 20m
B07: Vegetation red edge; 20m
B08: NIR; 10m
B09: Water vapor; 60m
B11: SWIR; 20m
B12: SWIR; 20m
B8A: Narrow NIR; 20m

License: Community Data License Agreement - Permissive, Version 1.0.

URL: http://bigearth.net/

*   URL: [http://bigearth.net](http://bigearth.net)
*   `DatasetBuilder`:
    [`tfds.image.bigearthnet.Bigearthnet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/bigearthnet.py)

`bigearthnet` is configured with `tfds.image.bigearthnet.BigearthnetConfig` and
has the following configurations predefined (defaults to the first one):

*   `rgb` (`v0.0.2`) (`Size: ?? GiB`): Sentinel-2 RGB channels

*   `all` (`v0.0.2`) (`Size: ?? GiB`): 13 Sentinel-2 channels

## `bigearthnet/rgb`

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(120, 120, 3), dtype=tf.uint8),
    'labels': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=43)),
    'metadata': FeaturesDict({
        'acquisition_date': Text(shape=(), dtype=tf.string),
        'coordinates': FeaturesDict({
            'lrx': Tensor(shape=(), dtype=tf.int64),
            'lry': Tensor(shape=(), dtype=tf.int64),
            'ulx': Tensor(shape=(), dtype=tf.int64),
            'uly': Tensor(shape=(), dtype=tf.int64),
        }),
        'projection': Text(shape=(), dtype=tf.string),
        'tile_source': Text(shape=(), dtype=tf.string),
    }),
})
```

## `bigearthnet/all`

```python
FeaturesDict({
    'B01': Tensor(shape=[20, 20], dtype=tf.float32),
    'B02': Tensor(shape=[120, 120], dtype=tf.float32),
    'B03': Tensor(shape=[120, 120], dtype=tf.float32),
    'B04': Tensor(shape=[120, 120], dtype=tf.float32),
    'B05': Tensor(shape=[60, 60], dtype=tf.float32),
    'B06': Tensor(shape=[60, 60], dtype=tf.float32),
    'B07': Tensor(shape=[60, 60], dtype=tf.float32),
    'B08': Tensor(shape=[120, 120], dtype=tf.float32),
    'B09': Tensor(shape=[20, 20], dtype=tf.float32),
    'B11': Tensor(shape=[60, 60], dtype=tf.float32),
    'B12': Tensor(shape=[60, 60], dtype=tf.float32),
    'B8A': Tensor(shape=[60, 60], dtype=tf.float32),
    'filename': Text(shape=(), dtype=tf.string),
    'labels': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=43)),
    'metadata': FeaturesDict({
        'acquisition_date': Text(shape=(), dtype=tf.string),
        'coordinates': FeaturesDict({
            'lrx': Tensor(shape=(), dtype=tf.int64),
            'lry': Tensor(shape=(), dtype=tf.int64),
            'ulx': Tensor(shape=(), dtype=tf.int64),
            'uly': Tensor(shape=(), dtype=tf.int64),
        }),
        'projection': Text(shape=(), dtype=tf.string),
        'tile_source': Text(shape=(), dtype=tf.string),
    }),
})
```

## Statistics
None computed

## Urls

*   [http://bigearth.net](http://bigearth.net)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
```
@article{Sumbul2019BigEarthNetAL,
  title={BigEarthNet: A Large-Scale Benchmark Archive For Remote Sensing Image Understanding},
  author={Gencer Sumbul and Marcela Charfuelan and Beg{"u}m Demir and Volker Markl},
  journal={CoRR},
  year={2019},
  volume={abs/1902.06148}
}
```

--------------------------------------------------------------------------------
