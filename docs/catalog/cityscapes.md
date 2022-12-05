<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cityscapes" />
  <meta itemprop="description" content="Cityscapes is a dataset consisting of diverse urban street scenes across 50&#10;different cities at varying times of the year as well as ground truths for&#10;several vision tasks including semantic segmentation, instance level&#10;segmentation (TODO), and stereo pair disparity inference.&#10;&#10;For segmentation tasks (default split, accessible via&#10;&#x27;cityscapes/semantic_segmentation&#x27;), Cityscapes provides dense pixel level&#10;annotations for 5000 images at 1024 * 2048 resolution pre-split into training&#10;(2975), validation (500) and test (1525) sets. Label annotations for&#10;segmentation tasks span across 30+ classes commonly encountered during driving&#10;scene perception. Detailed label information may be found here:&#10;https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99&#10;&#10;Cityscapes also provides coarse grain segmentation annotations (accessible via&#10;&#x27;cityscapes/semantic_segmentation_extra&#x27;) for 19998 images in a &#x27;train_extra&#x27;&#10;split which may prove useful for pretraining / data-heavy models.&#10;&#10;Besides segmentation, cityscapes also provides stereo image pairs and ground&#10;truths for disparity inference tasks on both the normal and extra splits&#10;(accessible via &#x27;cityscapes/stereo_disparity&#x27; and&#10;&#x27;cityscapes/stereo_disparity_extra&#x27; respectively).&#10;&#10;Ingored examples:&#10;&#10;-   For &#x27;cityscapes/stereo_disparity_extra&#x27;:&#10;    -   troisdorf_000000_000073_{*} images (no disparity map present)&#10;&#10;WARNING: this dataset requires users to setup a login and password in order to&#10;get the files.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cityscapes&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cityscapes" />
  <meta itemprop="sameAs" content="https://www.cityscapes-dataset.com" />
  <meta itemprop="citation" content="@inproceedings{Cordts2016Cityscapes,&#10;  title={The Cityscapes Dataset for Semantic Urban Scene Understanding},&#10;  author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},&#10;  booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;  year={2016}&#10;}" />
</div>

# `cityscapes`


Warning: Manual download required. See instructions below.

*   **Description**:

Cityscapes is a dataset consisting of diverse urban street scenes across 50
different cities at varying times of the year as well as ground truths for
several vision tasks including semantic segmentation, instance level
segmentation (TODO), and stereo pair disparity inference.

For segmentation tasks (default split, accessible via
'cityscapes/semantic_segmentation'), Cityscapes provides dense pixel level
annotations for 5000 images at 1024 * 2048 resolution pre-split into training
(2975), validation (500) and test (1525) sets. Label annotations for
segmentation tasks span across 30+ classes commonly encountered during driving
scene perception. Detailed label information may be found here:
https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99

Cityscapes also provides coarse grain segmentation annotations (accessible via
'cityscapes/semantic_segmentation_extra') for 19998 images in a 'train_extra'
split which may prove useful for pretraining / data-heavy models.

Besides segmentation, cityscapes also provides stereo image pairs and ground
truths for disparity inference tasks on both the normal and extra splits
(accessible via 'cityscapes/stereo_disparity' and
'cityscapes/stereo_disparity_extra' respectively).

Ingored examples:

-   For 'cityscapes/stereo_disparity_extra':
    -   troisdorf_000000_000073_{*} images (no disparity map present)

WARNING: this dataset requires users to setup a login and password in order to
get the files.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/cityscapes">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.cityscapes-dataset.com](https://www.cityscapes-dataset.com)

*   **Source code**:
    [`tfds.datasets.cityscapes.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/cityscapes/cityscapes_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    You have to download files from https://www.cityscapes-dataset.com/login/
    (This dataset requires registration).
    For basic config (semantic_segmentation) you must download
    'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'.
    Other configs do require additional files - please see code for more details.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{Cordts2016Cityscapes,
  title={The Cityscapes Dataset for Semantic Urban Scene Understanding},
  author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},
  booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2016}
}
```


## cityscapes/semantic_segmentation (default config)

*   **Config description**: Cityscapes semantic segmentation dataset.

*   **Dataset size**: `10.86 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,525
`'train'`      | 2,975
`'validation'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape           | Dtype  | Description
:----------------- | :----------- | :-------------- | :----- | :----------
                   | FeaturesDict |                 |        |
image_id           | Text         |                 | string |
image_left         | Image        | (1024, 2048, 3) | uint8  |
segmentation_label | Image        | (1024, 2048, 1) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cityscapes-semantic_segmentation-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## cityscapes/semantic_segmentation_extra

*   **Config description**: Cityscapes semantic segmentation dataset with
    train_extra split and coarse labels.

*   **Dataset size**: `51.92 GiB`

*   **Splits**:

Split           | Examples
:-------------- | -------:
`'train'`       | 2,975
`'train_extra'` | 19,998
`'validation'`  | 500

*   **Feature structure**:

```python
FeaturesDict({
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape           | Dtype  | Description
:----------------- | :----------- | :-------------- | :----- | :----------
                   | FeaturesDict |                 |        |
image_id           | Text         |                 | string |
image_left         | Image        | (1024, 2048, 3) | uint8  |
segmentation_label | Image        | (1024, 2048, 1) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cityscapes-semantic_segmentation_extra-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## cityscapes/stereo_disparity

*   **Config description**: Cityscapes stereo image and disparity maps dataset.

*   **Dataset size**: `25.03 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,525
`'train'`      | 2,975
`'validation'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=uint8),
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=uint8),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape           | Dtype  | Description
:------------ | :----------- | :-------------- | :----- | :----------
              | FeaturesDict |                 |        |
disparity_map | Image        | (1024, 2048, 1) | uint8  |
image_id      | Text         |                 | string |
image_left    | Image        | (1024, 2048, 3) | uint8  |
image_right   | Image        | (1024, 2048, 3) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cityscapes-stereo_disparity-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## cityscapes/stereo_disparity_extra

*   **Config description**: Cityscapes stereo image and disparity maps dataset
    with train_extra split.

*   **Dataset size**: `119.18 GiB`

*   **Splits**:

Split           | Examples
:-------------- | -------:
`'train'`       | 2,975
`'train_extra'` | 19,997
`'validation'`  | 500

*   **Feature structure**:

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=uint8),
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=uint8),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape           | Dtype  | Description
:------------ | :----------- | :-------------- | :----- | :----------
              | FeaturesDict |                 |        |
disparity_map | Image        | (1024, 2048, 1) | uint8  |
image_id      | Text         |                 | string |
image_left    | Image        | (1024, 2048, 3) | uint8  |
image_right   | Image        | (1024, 2048, 3) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cityscapes-stereo_disparity_extra-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->