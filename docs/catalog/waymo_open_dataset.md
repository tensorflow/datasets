<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="waymo_open_dataset" />
  <meta itemprop="description" content="The Waymo Open Dataset is comprised of high resolution sensor data&#10;collected by Waymo self-driving cars in a wide variety of conditions.&#10;This data is licensed for non-commercial use.&#10;&#10;WARNING: this dataset requires additional authorization and registration.&#10;Please look at tfds documentation for accessing GCS, and&#10;afterwards, please register via https://waymo.com/open/licensing/&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;waymo_open_dataset&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/waymo_open_dataset" />
  <meta itemprop="sameAs" content="http://www.waymo.com/open/" />
  <meta itemprop="citation" content="@InProceedings{Sun_2020_CVPR,&#10;author = {Sun, Pei and Kretzschmar, Henrik and Dotiwalla, Xerxes and Chouard, Aurelien and Patnaik, Vijaysai and Tsui, Paul and Guo, James and Zhou, Yin and Chai, Yuning and Caine, Benjamin and Vasudevan, Vijay and Han, Wei and Ngiam, Jiquan and Zhao, Hang and Timofeev, Aleksei and Ettinger, Scott and Krivokon, Maxim and Gao, Amy and Joshi, Aditya and Zhang, Yu and Shlens, Jonathon and Chen, Zhifeng and Anguelov, Dragomir},&#10;title = {Scalability in Perception for Autonomous Driving: Waymo Open Dataset},&#10;booktitle = {The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;month = {June},&#10;year = {2020}&#10;}" />
</div>

# `waymo_open_dataset`

*   **Description**:

The Waymo Open Dataset is comprised of high resolution sensor data collected by
Waymo self-driving cars in a wide variety of conditions. This data is licensed
for non-commercial use.

WARNING: this dataset requires additional authorization and registration. Please
look at tfds documentation for accessing GCS, and afterwards, please register
via https://waymo.com/open/licensing/

*   **Homepage**: [http://www.waymo.com/open/](http://www.waymo.com/open/)

*   **Source code**:
    [`tfds.object_detection.WaymoOpenDataset`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/object_detection/waymo_open_dataset.py)

*   **Versions**:

    *   **`0.2.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'camera_FRONT': FeaturesDict({
        'image': Image(shape=(1280, 1920, 3), dtype=tf.uint8),
        'labels': Sequence({
            'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
            'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        }),
    }),
    'camera_FRONT_LEFT': FeaturesDict({
        'image': Image(shape=(1280, 1920, 3), dtype=tf.uint8),
        'labels': Sequence({
            'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
            'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        }),
    }),
    'camera_FRONT_RIGHT': FeaturesDict({
        'image': Image(shape=(1280, 1920, 3), dtype=tf.uint8),
        'labels': Sequence({
            'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
            'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        }),
    }),
    'camera_SIDE_LEFT': FeaturesDict({
        'image': Image(shape=(886, 1920, 3), dtype=tf.uint8),
        'labels': Sequence({
            'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
            'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        }),
    }),
    'camera_SIDE_RIGHT': FeaturesDict({
        'image': Image(shape=(886, 1920, 3), dtype=tf.uint8),
        'labels': Sequence({
            'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
            'type': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        }),
    }),
    'context': FeaturesDict({
        'name': Text(shape=(), dtype=tf.string),
    }),
    'timestamp_micros': tf.int64,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@InProceedings{Sun_2020_CVPR,
author = {Sun, Pei and Kretzschmar, Henrik and Dotiwalla, Xerxes and Chouard, Aurelien and Patnaik, Vijaysai and Tsui, Paul and Guo, James and Zhou, Yin and Chai, Yuning and Caine, Benjamin and Vasudevan, Vijay and Han, Wei and Ngiam, Jiquan and Zhao, Hang and Timofeev, Aleksei and Ettinger, Scott and Krivokon, Maxim and Gao, Amy and Joshi, Aditya and Zhang, Yu and Shlens, Jonathon and Chen, Zhifeng and Anguelov, Dragomir},
title = {Scalability in Perception for Autonomous Driving: Waymo Open Dataset},
booktitle = {The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {June},
year = {2020}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## waymo_open_dataset/v1.2 (default config)

*   **Config description**: Waymo Open Dataset v1.2

*   **Dataset size**: `336.62 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 158,081
`'validation'` | 39,987

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/waymo_open_dataset-v1.2-0.2.0.html";
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

## waymo_open_dataset/v1.1

*   **Config description**: Waymo Open Dataset v1.1

*   **Dataset size**: `336.62 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 158,081
`'validation'` | 39,987

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/waymo_open_dataset-v1.1-0.2.0.html";
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

## waymo_open_dataset/v1.0

*   **Config description**: Waymo Open Dataset v1.0 This dataset is also
    available in pre-processed format, making it faster to load, if you select
    the correct data_dir:

```
tfds.load('waymo_open_dataset/v1.0', data_dir='gs://waymo_open_dataset_v_1_0_0_individual_files/tensorflow_datasets')
```

*   **Dataset size**: `34.73 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 14,884
`'validation'` | 4,954

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/waymo_open_dataset-v1.0-0.2.0.html";
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