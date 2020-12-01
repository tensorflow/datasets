<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="curated_breast_imaging_ddsm" />
  <meta itemprop="description" content="The CBIS-DDSM (Curated Breast Imaging Subset of DDSM) is an updated and&#10;standardized version of the Digital Database for Screening Mammography (DDSM).&#10;The DDSM is a database of 2,620 scanned film mammography studies.&#10;It contains normal, benign, and malignant cases with verified pathology&#10;information.&#10;&#10;The default config is made of patches extracted from the original mammograms,&#10;following the description from http://arxiv.org/abs/1708.09427, in order to&#10;frame the task to solve in a traditional image classification setting.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;curated_breast_imaging_ddsm&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/curated_breast_imaging_ddsm-patches-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/curated_breast_imaging_ddsm" />
  <meta itemprop="sameAs" content="https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM" />
  <meta itemprop="citation" content="@misc{CBIS_DDSM_Citation,&#10;  doi = {10.7937/k9/tcia.2016.7o02s9cy},&#10;  url = {https://wiki.cancerimagingarchive.net/x/lZNXAQ},&#10;  author = {Sawyer-Lee,  Rebecca and Gimenez,  Francisco and Hoogi,  Assaf and Rubin,  Daniel},&#10;  title = {Curated Breast Imaging Subset of DDSM},&#10;  publisher = {The Cancer Imaging Archive},&#10;  year = {2016},&#10;}&#10;@article{TCIA_Citation,&#10;  author = {&#10;    K. Clark and B. Vendt and K. Smith and J. Freymann and J. Kirby and&#10;    P. Koppel and S. Moore and S. Phillips and D. Maffitt and M. Pringle and&#10;    L. Tarbox and F. Prior&#10;  },&#10;  title = {{The Cancer Imaging Archive (TCIA): Maintaining and Operating a&#10;  Public Information Repository}},&#10;  journal = {Journal of Digital Imaging},&#10;  volume = {26},&#10;  month = {December},&#10;  year = {2013},&#10;  pages = {1045-1057},&#10;}&#10;@article{DBLP:journals/corr/abs-1708-09427,&#10;  author    = {Li Shen},&#10;  title     = {End-to-end Training for Whole Image Breast Cancer Diagnosis using&#10;               An All Convolutional Design},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1708.09427},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1708.09427},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1708.09427},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:35 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-09427},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `curated_breast_imaging_ddsm`

Warning: Manual download required. See instructions below.

*   **Description**:

The CBIS-DDSM (Curated Breast Imaging Subset of DDSM) is an updated and
standardized version of the Digital Database for Screening Mammography (DDSM).
The DDSM is a database of 2,620 scanned film mammography studies. It contains
normal, benign, and malignant cases with verified pathology information.

The default config is made of patches extracted from the original mammograms,
following the description from http://arxiv.org/abs/1708.09427, in order to
frame the task to solve in a traditional image classification setting.

*   **Homepage**:
    [https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM](https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM)

*   **Source code**:
    [`tfds.image_classification.CuratedBreastImagingDDSM`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cbis_ddsm.py)

*   **Versions**:

    *   `2.0.1`: New split API (https://tensorflow.org/datasets/splits)
    *   **`3.0.0`** (default): Better cropping sampling
        (https://github.com/tensorflow/datasets/pull/2502)

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    You can download the images from
    https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM

Because special software and libraries are needed to download and read the
images contained in the dataset, TFDS assumes that the user has downloaded the
original DCIM files and converted them to PNG.

The following commands (or equivalent) should be used to generate the PNG files,
in order to guarantee reproducible results:

```sh
find $DATASET_DCIM_DIR -name '*.dcm' | \
xargs -n1 -P8 -I{} bash -c 'f={}; dcmj2pnm $f | convert - ${f/.dcm/.png}'
```

Resulting images should be put in `manual_dir`, like:
`<manual_dir>/Mass-Training_P_01981_RIGHT_MLO_1/1.3.6.../000000.png`.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

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

## curated_breast_imaging_ddsm/patches (default config)

*   **Config description**: Patches containing both calsification and mass
    cases, plus pathces with no abnormalities. Designed as a traditional 5-class
    classification task.

*   **Download size**: `2.01 MiB`

*   **Dataset size**: `801.46 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,770
`'train'`      | 49,780
`'validation'` | 5,580

*   **Features**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/curated_breast_imaging_ddsm-patches-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/curated_breast_imaging_ddsm-patches-3.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## curated_breast_imaging_ddsm/original-calc

*   **Config description**: Original images of the calcification cases
    compressed in lossless PNG.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `4.42 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 284
`'train'` | 1,227

*   **Features**:

```python
FeaturesDict({
    'abnormalities': Sequence({
        'assessment': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
        'calc_distribution': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
        'calc_type': ClassLabel(shape=(), dtype=tf.int64, num_classes=48),
        'id': tf.int32,
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

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/curated_breast_imaging_ddsm-original-calc-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/curated_breast_imaging_ddsm-original-calc-3.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## curated_breast_imaging_ddsm/original-mass

*   **Config description**: Original images of the mass cases compressed in
    lossless PNG.

*   **Download size**: `966.57 KiB`

*   **Dataset size**: `4.80 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 348
`'train'` | 1,166

*   **Features**:

```python
FeaturesDict({
    'abnormalities': Sequence({
        'assessment': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
        'id': tf.int32,
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

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/curated_breast_imaging_ddsm-original-mass-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/curated_breast_imaging_ddsm-original-mass-3.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->