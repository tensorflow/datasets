<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="downsampled_imagenet" />
  <meta itemprop="description" content="Dataset with images of 2 resolutions (see config name for information on the resolution).&#10;It is used for density estimation and generative modeling experiments.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/downsampled_imagenet" />
  <meta itemprop="sameAs" content="http://image-net.org/small/download.php" />
</div>

# `downsampled_imagenet`

Dataset with images of 2 resolutions (see config name for information on the
resolution). It is used for density estimation and generative modeling
experiments.

*   URL:
    [http://image-net.org/small/download.php](http://image-net.org/small/download.php)
*   `DatasetBuilder`:
    [`tfds.image.downsampled_imagenet.DownsampledImagenet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/downsampled_imagenet.py)

`downsampled_imagenet` is configured with
`tfds.image.downsampled_imagenet.DownsampledImagenetConfig` and has the
following configurations predefined (defaults to the first one):

*   `32x32` (`v1.0.0`) (`Size: 3.98 GiB`): A dataset consisting of Train and
    Validation images of 32x32 resolution.

*   `64x64` (`v1.0.0`) (`Size: 11.73 GiB`): A dataset consisting of Train and
    Validation images of 64x64 resolution.

## `downsampled_imagenet/32x32`

A dataset consisting of Train and Validation images of 32x32 resolution.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,148
TRAIN      | 1,281,149
VALIDATION | 49,999

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Urls

*   [http://image-net.org/small/download.php](http://image-net.org/small/download.php)

## `downsampled_imagenet/64x64`

A dataset consisting of Train and Validation images of 64x64 resolution.

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,148
TRAIN      | 1,281,149
VALIDATION | 49,999

### Features

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

### Urls

*   [http://image-net.org/small/download.php](http://image-net.org/small/download.php)

## Citation
```
@article{DBLP:journals/corr/OordKK16,
  author    = {A{"{a}}ron van den Oord and
               Nal Kalchbrenner and
               Koray Kavukcuoglu},
  title     = {Pixel Recurrent Neural Networks},
  journal   = {CoRR},
  volume    = {abs/1601.06759},
  year      = {2016},
  url       = {http://arxiv.org/abs/1601.06759},
  archivePrefix = {arXiv},
  eprint    = {1601.06759},
  timestamp = {Mon, 13 Aug 2018 16:46:29 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/OordKK16},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
