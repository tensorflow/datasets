<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robosuite_panda_pick_place_can" />
  <meta itemprop="description" content="These datasets have been created with the PickPlaceCan environment of the&#10;[robosuite robotic arm simulator](https://robosuite.ai/). The human datasets&#10;were recorded by a single operator using&#10;the [RLDS Creator](https://github.com/google-research/rlds-creator) and a&#10;gamepad controller.&#10;&#10;The synthetic datasets have been recorded using the&#10;[EnvLogger library](https://github.com/deepmind/envlogger).&#10;&#10;Episodes consist of 400 steps. In each episode, a tag is&#10;added when the task is completed, this tag is stored as part of the custom step&#10;metadata.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robosuite_panda_pick_place_can&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can" />
  <meta itemprop="sameAs" content="https://github.com/google-research/rlds" />
  <meta itemprop="citation" content="@misc{google-research, title={RLDS},&#10;url={https://github.com/google-research/rlds}, journal={GitHub},&#10;author={S. Ramos, S. Girgin et al.}}" />
</div>

# `robosuite_panda_pick_place_can`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

These datasets have been created with the PickPlaceCan environment of the
[robosuite robotic arm simulator](https://robosuite.ai/). The human datasets
were recorded by a single operator using the
[RLDS Creator](https://github.com/google-research/rlds-creator) and a gamepad
controller.

The synthetic datasets have been recorded using the
[EnvLogger library](https://github.com/deepmind/envlogger).

Episodes consist of 400 steps. In each episode, a tag is added when the task is
completed, this tag is stored as part of the custom step metadata.

*   **Homepage**:
    [https://github.com/google-research/rlds](https://github.com/google-research/rlds)

*   **Source code**:
    [`tfds.rlds.robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rlds/robosuite_panda_pick_place_can/robosuite_panda_pick_place_can.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

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
@misc{google-research, title={RLDS},
url={https://github.com/google-research/rlds}, journal={GitHub},
author={S. Ramos, S. Girgin et al.}}
```

## robosuite_panda_pick_place_can/human_dc29b40a (default config)

*   **Config description**: Human generated dataset (50 episodes).

*   **Download size**: `96.67 MiB`

*   **Dataset size**: `407.24 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50

*   **Features**:

```python
FeaturesDict({
    'agent_id': tf.string,
    'episode_id': tf.string,
    'episode_index': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.float64,
        'image': Image(shape=(None, None, 3), dtype=tf.uint8),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=tf.float64),
            'Can_quat': Tensor(shape=(4,), dtype=tf.float64),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'object-state': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'tag:placed': tf.bool,
    }),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robosuite_panda_pick_place_can-human_dc29b40a-1.0.0.html";
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

## robosuite_panda_pick_place_can/synthetic_stochastic_sac_afe13968

*   **Config description**: Synthetic dataset generated by a stochastic agent
    trained with SAC (200 episodes).

*   **Download size**: `144.44 MiB`

*   **Dataset size**: `622.86 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Features**:

```python
FeaturesDict({
    'agent_id': tf.string,
    'episode_id': tf.string,
    'episode_index': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float32),
        'discount': tf.float64,
        'image': Image(shape=(None, None, 3), dtype=tf.uint8),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=tf.float32),
            'Can_quat': Tensor(shape=(4,), dtype=tf.float32),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float32),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'object-state': Tensor(shape=(14,), dtype=tf.float32),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float32),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float32),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float32),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=tf.float32),
        }),
        'reward': tf.float64,
        'tag:placed': tf.bool,
    }),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robosuite_panda_pick_place_can-synthetic_stochastic_sac_afe13968-1.0.0.html";
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