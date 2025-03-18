<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lost_and_found" />
  <meta itemprop="description" content="The LostAndFound Dataset addresses the problem of detecting unexpected small&#10;obstacles on the road often caused by lost cargo. The dataset comprises 112&#10;stereo video sequences with 2104 annotated frames (picking roughly every tenth&#10;frame from the recorded data).&#10;&#10;The dataset is designed analogous to the &#x27;Cityscapes&#x27; dataset. The datset&#10;provides: - stereo image pairs in either 8 or 16 bit color resolution -&#10;precomputed disparity maps - coarse semantic labels for objects and street&#10;&#10;Descriptions of the labels are given here:&#10;http://www.6d-vision.com/laf_table.pdf&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lost_and_found&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lost_and_found" />
  <meta itemprop="sameAs" content="http://www.6d-vision.com/lostandfounddataset" />
  <meta itemprop="citation" content="@inproceedings{pinggera2016lost,&#10;  title={Lost and found: detecting small road hazards for self-driving vehicles},&#10;  author={Pinggera, Peter and Ramos, Sebastian and Gehrig, Stefan and Franke, Uwe and Rother, Carsten and Mester, Rudolf},&#10;  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},&#10;  year={2016}&#10;}" />
</div>

# `lost_and_found`


*   **Description**:

The LostAndFound Dataset addresses the problem of detecting unexpected small
obstacles on the road often caused by lost cargo. The dataset comprises 112
stereo video sequences with 2104 annotated frames (picking roughly every tenth
frame from the recorded data).

The dataset is designed analogous to the 'Cityscapes' dataset. The datset
provides: - stereo image pairs in either 8 or 16 bit color resolution -
precomputed disparity maps - coarse semantic labels for objects and street

Descriptions of the labels are given here:
http://www.6d-vision.com/laf_table.pdf

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/lost-and-found">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.6d-vision.com/lostandfounddataset](http://www.6d-vision.com/lostandfounddataset)

*   **Source code**:
    [`tfds.datasets.lost_and_found.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/lost_and_found/lost_and_found_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,203
`'train'` | 1,036

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{pinggera2016lost,
  title={Lost and found: detecting small road hazards for self-driving vehicles},
  author={Pinggera, Peter and Ramos, Sebastian and Gehrig, Stefan and Franke, Uwe and Rother, Carsten and Mester, Rudolf},
  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2016}
}
```


## lost_and_found/semantic_segmentation (default config)

*   **Config description**: Lost and Found semantic segmentation dataset.

*   **Download size**: `5.44 GiB`

*   **Dataset size**: `5.42 GiB`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lost_and_found-semantic_segmentation-1.0.0.html";
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

## lost_and_found/stereo_disparity

*   **Config description**: Lost and Found stereo images and disparity maps.

*   **Download size**: `12.16 GiB`

*   **Dataset size**: `12.22 GiB`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lost_and_found-stereo_disparity-1.0.0.html";
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

## lost_and_found/full

*   **Config description**: Full Lost and Found dataset.

*   **Download size**: `12.19 GiB`

*   **Dataset size**: `12.25 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=uint8),
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=uint8),
    'instance_id': Image(shape=(1024, 2048, 1), dtype=uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape           | Dtype  | Description
:----------------- | :----------- | :-------------- | :----- | :----------
                   | FeaturesDict |                 |        |
disparity_map      | Image        | (1024, 2048, 1) | uint8  |
image_id           | Text         |                 | string |
image_left         | Image        | (1024, 2048, 3) | uint8  |
image_right        | Image        | (1024, 2048, 3) | uint8  |
instance_id        | Image        | (1024, 2048, 1) | uint8  |
segmentation_label | Image        | (1024, 2048, 1) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lost_and_found-full-1.0.0.html";
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

## lost_and_found/full_16bit

*   **Config description**: Full Lost and Found dataset.

*   **Download size**: `34.90 GiB`

*   **Dataset size**: `35.05 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'disparity_map': Image(shape=(1024, 2048, 1), dtype=uint8),
    'image_id': Text(shape=(), dtype=string),
    'image_left': Image(shape=(1024, 2048, 3), dtype=uint8),
    'image_right': Image(shape=(1024, 2048, 3), dtype=uint8),
    'instance_id': Image(shape=(1024, 2048, 1), dtype=uint8),
    'segmentation_label': Image(shape=(1024, 2048, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape           | Dtype  | Description
:----------------- | :----------- | :-------------- | :----- | :----------
                   | FeaturesDict |                 |        |
disparity_map      | Image        | (1024, 2048, 1) | uint8  |
image_id           | Text         |                 | string |
image_left         | Image        | (1024, 2048, 3) | uint8  |
image_right        | Image        | (1024, 2048, 3) | uint8  |
instance_id        | Image        | (1024, 2048, 1) | uint8  |
segmentation_label | Image        | (1024, 2048, 1) | uint8  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lost_and_found-full_16bit-1.0.0.html";
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