<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robonet" />
  <meta itemprop="description" content="RoboNet contains over 15 million video frames of robot-object&#10;interaction, taken from 113 unique camera viewpoints.&#10;&#10;* The actions are deltas in position and rotation to the robot&#10;end-effector with one additional dimension of the action vector&#10;reserved for the gripper joint.&#10;&#10;* The states are cartesian end-effector control action space&#10;with restricted rotation, and a gripper joint&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robonet&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robonet" />
  <meta itemprop="sameAs" content="https://www.robonet.wiki/" />
  <meta itemprop="citation" content="@article{dasari2019robonet,&#10;  title={RoboNet: Large-Scale Multi-Robot Learning},&#10;  author={Dasari, Sudeep and Ebert, Frederik and Tian, Stephen and&#10;  Nair, Suraj and Bucher, Bernadette and Schmeckpeper, Karl&#10;  and Singh, Siddharth and Levine, Sergey and Finn, Chelsea},&#10;  journal={arXiv preprint arXiv:1910.11215},&#10;  year={2019}&#10;}" />
</div>

# `robonet`


*   **Description**:

RoboNet contains over 15 million video frames of robot-object interaction, taken
from 113 unique camera viewpoints.

*   The actions are deltas in position and rotation to the robot end-effector
    with one additional dimension of the action vector reserved for the gripper
    joint.

*   The states are cartesian end-effector control action space with restricted
    rotation, and a gripper joint

*   **Homepage**: [https://www.robonet.wiki/](https://www.robonet.wiki/)

*   **Source code**:
    [`tfds.video.Robonet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/robonet.py)

*   **Versions**:

    *   **`4.0.1`** (default): No release notes.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{dasari2019robonet,
  title={RoboNet: Large-Scale Multi-Robot Learning},
  author={Dasari, Sudeep and Ebert, Frederik and Tian, Stephen and
  Nair, Suraj and Bucher, Bernadette and Schmeckpeper, Karl
  and Singh, Siddharth and Levine, Sergey and Finn, Chelsea},
  journal={arXiv preprint arXiv:1910.11215},
  year={2019}
}
```

## robonet/robonet_sample_64 (default config)

*   **Config description**: 64x64 RoboNet Sample.

*   **Download size**: `119.80 MiB`

*   **Dataset size**: `183.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 700

*   **Features**:

```python
FeaturesDict({
    'actions': Tensor(shape=(None, 5), dtype=tf.float32),
    'filename': Text(shape=(), dtype=tf.string),
    'states': Tensor(shape=(None, 5), dtype=tf.float32),
    'video': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robonet-robonet_sample_64-4.0.1.html";
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

## robonet/robonet_sample_128

*   **Config description**: 128x128 RoboNet Sample.

*   **Download size**: `119.80 MiB`

*   **Dataset size**: `638.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 700

*   **Features**:

```python
FeaturesDict({
    'actions': Tensor(shape=(None, 5), dtype=tf.float32),
    'filename': Text(shape=(), dtype=tf.string),
    'states': Tensor(shape=(None, 5), dtype=tf.float32),
    'video': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robonet-robonet_sample_128-4.0.1.html";
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

## robonet/robonet_64

*   **Config description**: 64x64 RoboNet.

*   **Download size**: `36.20 GiB`

*   **Dataset size**: `41.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 162,417

*   **Features**:

```python
FeaturesDict({
    'actions': Tensor(shape=(None, 5), dtype=tf.float32),
    'filename': Text(shape=(), dtype=tf.string),
    'states': Tensor(shape=(None, 5), dtype=tf.float32),
    'video': Video(Image(shape=(64, 64, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robonet-robonet_64-4.0.1.html";
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

## robonet/robonet_128

*   **Config description**: 128x128 RoboNet.

*   **Download size**: `36.20 GiB`

*   **Dataset size**: `144.90 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 162,417

*   **Features**:

```python
FeaturesDict({
    'actions': Tensor(shape=(None, 5), dtype=tf.float32),
    'filename': Text(shape=(), dtype=tf.string),
    'states': Tensor(shape=(None, 5), dtype=tf.float32),
    'video': Video(Image(shape=(128, 128, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robonet-robonet_128-4.0.1.html";
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