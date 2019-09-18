<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="curated_breast_imaging_ddsm" />
  <meta itemprop="description" content="The CBIS-DDSM (Curated Breast Imaging Subset of DDSM) is an updated and&#10;standardized version of the Digital Database for Screening Mammography (DDSM).&#10;The DDSM is a database of 2,620 scanned film mammography studies.&#10;It contains normal, benign, and malignant cases with verified pathology&#10;information.&#10;&#10;The default config is made of patches extracted from the original mammograms,&#10;following the description from http://arxiv.org/abs/1708.09427, in order to&#10;frame the task to solve in a traditional image classification setting.&#10;&#10;Because special software and libraries are needed to download and read the&#10;images contained in the dataset, TFDS assumes that the user has downloaded the&#10;original DCIM files and converted them to PNG.&#10;&#10;The following commands (or equivalent) should be used to generate the PNG files,&#10;in order to guarantee reproducible results:&#10;&#10;  find $DATASET_DCIM_DIR -name '*.dcm' | \&#10;  xargs -n1 -P8 -I{} bash -c 'f={}; dcmj2pnm $f | convert - ${f/.dcm/.png}'&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/curated_breast_imaging_ddsm" />
  <meta itemprop="sameAs" content="https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM" />
</div>

# `curated_breast_imaging_ddsm`

The CBIS-DDSM (Curated Breast Imaging Subset of DDSM) is an updated and
standardized version of the Digital Database for Screening Mammography (DDSM).
The DDSM is a database of 2,620 scanned film mammography studies. It contains
normal, benign, and malignant cases with verified pathology information.

The default config is made of patches extracted from the original mammograms,
following the description from http://arxiv.org/abs/1708.09427, in order to
frame the task to solve in a traditional image classification setting.

Because special software and libraries are needed to download and read the
images contained in the dataset, TFDS assumes that the user has downloaded the
original DCIM files and converted them to PNG.

The following commands (or equivalent) should be used to generate the PNG files,
in order to guarantee reproducible results:

find $DATASET_DCIM_DIR -name '*.dcm' | \
xargs -n1 -P8 -I{} bash -c 'f={}; dcmj2pnm $f | convert - ${f/.dcm/.png}'

*   URL:
    [https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM](https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM)
*   `DatasetBuilder`:
    [`tfds.image.cbis_ddsm.CuratedBreastImagingDDSM`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/cbis_ddsm.py)

`curated_breast_imaging_ddsm` is configured with
`tfds.image.cbis_ddsm.CuratedBreastImagingDDSMConfig` and has the following
configurations predefined (defaults to the first one):

*   `patches` (`v0.2.0`) (`Size: 2.01 MiB`): Patches containing both
    calsification and mass cases, plus pathces with no abnormalities. Designed
    as a traditional 5-class classification task.

*   `original-calc` (`v0.1.0`) (`Size: 1.06 MiB`): Original images of the
    calcification cases compressed in lossless PNG.

*   `original-mass` (`v0.1.0`) (`Size: 966.57 KiB`): Original images of the mass
    cases compressed in lossless PNG.

## `curated_breast_imaging_ddsm/patches`

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
})
```

## `curated_breast_imaging_ddsm/original-calc`

```python
FeaturesDict({
    'abnormalities': Sequence({
        'assessment': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
        'calc_distribution': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
        'calc_type': ClassLabel(shape=(), dtype=tf.int64, num_classes=48),
        'id': Tensor(shape=(), dtype=tf.int32),
        'mask': Image(shape=(None, None, 1), dtype=tf.uint8),
        'pathology': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
        'subtlety': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'breast': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 1), dtype=tf.uint8),
    'patient': Text(shape=(), dtype=tf.string),
    'view': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## `curated_breast_imaging_ddsm/original-mass`

```python
FeaturesDict({
    'abnormalities': Sequence({
        'assessment': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
        'id': Tensor(shape=(), dtype=tf.int32),
        'mask': Image(shape=(None, None, 1), dtype=tf.uint8),
        'mass_margins': ClassLabel(shape=(), dtype=tf.int64, num_classes=20),
        'mass_shape': ClassLabel(shape=(), dtype=tf.int64, num_classes=21),
        'pathology': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
        'subtlety': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    }),
    'breast': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 1), dtype=tf.uint8),
    'patient': Text(shape=(), dtype=tf.string),
    'view': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 1,514
TRAIN | 1,166
TEST  | 348

## Urls

*   [https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM](https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
```
@misc{CBIS_DDSM_Citation,
  doi = {10.7937/k9/tcia.2016.7o02s9cy},
  url = {https://wiki.cancerimagingarchive.net/x/lZNXAQ},
  author = {Sawyer-Lee,  Rebecca and Gimenez,  Francisco and Hoogi,  Assaf and Rubin,  Daniel},
  title = {Curated Breast Imaging Subset of DDSM},
  publisher = {The Cancer Imaging Archive},
  year = {2016},
}
@article{TCIA_Citation,
  author = {
    K. Clark and B. Vendt and K. Smith and J. Freymann and J. Kirby and
    P. Koppel and S. Moore and S. Phillips and D. Maffitt and M. Pringle and
    L. Tarbox and F. Prior
  },
  title = {{The Cancer Imaging Archive (TCIA): Maintaining and Operating a
  Public Information Repository}},
  journal = {Journal of Digital Imaging},
  volume = {26},
  month = {December},
  year = {2013},
  pages = {1045-1057},
}
@article{DBLP:journals/corr/abs-1708-09427,
  author    = {Li Shen},
  title     = {End-to-end Training for Whole Image Breast Cancer Diagnosis using
               An All Convolutional Design},
  journal   = {CoRR},
  volume    = {abs/1708.09427},
  year      = {2017},
  url       = {http://arxiv.org/abs/1708.09427},
  archivePrefix = {arXiv},
  eprint    = {1708.09427},
  timestamp = {Mon, 13 Aug 2018 16:48:35 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-09427},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
