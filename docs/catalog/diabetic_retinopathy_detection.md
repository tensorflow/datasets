<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="diabetic_retinopathy_detection" />
  <meta itemprop="description" content="A large set of high-resolution retina images taken under a variety of imaging conditions.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;diabetic_retinopathy_detection&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/diabetic_retinopathy_detection-original-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/diabetic_retinopathy_detection" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/diabetic-retinopathy-detection/data" />
  <meta itemprop="citation" content="@ONLINE {kaggle-diabetic-retinopathy,&#10;    author = &quot;Kaggle and EyePacs&quot;,&#10;    title  = &quot;Kaggle Diabetic Retinopathy Detection&quot;,&#10;    month  = &quot;jul&quot;,&#10;    year   = &quot;2015&quot;,&#10;    url    = &quot;https://www.kaggle.com/c/diabetic-retinopathy-detection/data&quot;&#10;}" />
</div>

# `diabetic_retinopathy_detection`


Warning: Manual download required. See instructions below.

*   **Description**:

A large set of high-resolution retina images taken under a variety of imaging
conditions.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/diabetic-retinopathy-detection-dataset">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.kaggle.com/c/diabetic-retinopathy-detection/data](https://www.kaggle.com/c/diabetic-retinopathy-detection/data)

*   **Source code**:
    [`tfds.image_classification.DiabeticRetinopathyDetection`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/diabetic_retinopathy_detection.py)

*   **Versions**:

    *   **`3.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `1.13 MiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    You have to download this dataset from Kaggle.
    https://www.kaggle.com/c/diabetic-retinopathy-detection/data
    After downloading, unpack the test.zip file into test/ directory in manual_dir
    and sample.zip to sample/. Also unpack the sampleSubmissions.csv and
    trainLabels.csv.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'sample'`     | 10
`'test'`       | 42,670
`'train'`      | 35,126
`'validation'` | 10,906

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=5),
    'name': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape           | Dtype  | Description
:------ | :----------- | :-------------- | :----- | :----------
        | FeaturesDict |                 |        |
image   | Image        | (None, None, 3) | uint8  |
label   | ClassLabel   |                 | int64  |
name    | Text         |                 | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@ONLINE {kaggle-diabetic-retinopathy,
    author = "Kaggle and EyePacs",
    title  = "Kaggle Diabetic Retinopathy Detection",
    month  = "jul",
    year   = "2015",
    url    = "https://www.kaggle.com/c/diabetic-retinopathy-detection/data"
}
```


## diabetic_retinopathy_detection/original (default config)

*   **Config description**: Images at their original resolution and quality.

*   **Dataset size**: `89.15 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/diabetic_retinopathy_detection-original-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/diabetic_retinopathy_detection-original-3.0.0.html";
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

## diabetic_retinopathy_detection/1M

*   **Config description**: Images have roughly 1,000,000 pixels, at 72 quality.

*   **Dataset size**: `3.96 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/diabetic_retinopathy_detection-1M-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/diabetic_retinopathy_detection-1M-3.0.0.html";
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

## diabetic_retinopathy_detection/250K

*   **Config description**: Images have roughly 250,000 pixels, at 72 quality.

*   **Dataset size**: `1.30 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/diabetic_retinopathy_detection-250K-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/diabetic_retinopathy_detection-250K-3.0.0.html";
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

## diabetic_retinopathy_detection/btgraham-300

*   **Config description**: Images have been preprocessed as the winner of the
    Kaggle competition did in 2015: first they are resized so that the radius of
    an eyeball is 300 pixels, then they are cropped to 90% of the radius, and
    finally they are encoded with 72 JPEG quality.

*   **Dataset size**: `3.65 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/diabetic_retinopathy_detection-btgraham-300-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/diabetic_retinopathy_detection-btgraham-300-3.0.0.html";
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