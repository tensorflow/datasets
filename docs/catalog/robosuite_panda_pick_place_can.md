<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robosuite_panda_pick_place_can" />
  <meta itemprop="description" content="These datasets have been created with the PickPlaceCan environment of the&#10;[robosuite robotic arm simulator](https://robosuite.ai/). The human datasets&#10;were recorded by a single operator using&#10;the [RLDS Creator](https://github.com/google-research/rlds-creator) and a&#10;gamepad controller.&#10;&#10;The synthetic datasets have been recorded using the&#10;[EnvLogger library](https://github.com/deepmind/envlogger).&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;Episodes consist of 400 steps. In each episode, a tag is&#10;added when the task is completed, this tag is stored as part of the custom step&#10;metadata.&#10;&#10;Note that, due to the EnvLogger dependency, generation of this dataset is&#10;currently supported on Linux environments only.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robosuite_panda_pick_place_can&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can" />
  <meta itemprop="sameAs" content="https://github.com/google-research/rlds" />
  <meta itemprop="citation" content="@misc{ramos2021rlds,&#10;      title={RLDS: an Ecosystem to Generate, Share and Use Datasets in Reinforcement Learning},&#10;      author={Sabela Ramos and Sertan Girgin and Léonard Hussenot and Damien Vincent and Hanna Yakubovich and Daniel Toyama and Anita Gergely and Piotr Stanczyk and Raphael Marinier and Jeremiah Harmsen and Olivier Pietquin and Nikola Momchev},&#10;      year={2021},&#10;      eprint={2111.02767},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.LG}&#10;}" />
</div>

# `robosuite_panda_pick_place_can`


*   **Description**:

These datasets have been created with the PickPlaceCan environment of the
[robosuite robotic arm simulator](https://robosuite.ai/). The human datasets
were recorded by a single operator using the
[RLDS Creator](https://github.com/google-research/rlds-creator) and a gamepad
controller.

The synthetic datasets have been recorded using the
[EnvLogger library](https://github.com/deepmind/envlogger).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

Episodes consist of 400 steps. In each episode, a tag is added when the task is
completed, this tag is stored as part of the custom step metadata.

Note that, due to the EnvLogger dependency, generation of this dataset is
currently supported on Linux environments only.

*   **Source code**:
    [`tfds.rlds.datasets.robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rlds/datasets/robosuite_panda_pick_place_can/robosuite_panda_pick_place_can.py)

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
@misc{ramos2021rlds,
      title={RLDS: an Ecosystem to Generate, Share and Use Datasets in Reinforcement Learning},
      author={Sabela Ramos and Sertan Girgin and Léonard Hussenot and Damien Vincent and Hanna Yakubovich and Daniel Toyama and Anita Gergely and Piotr Stanczyk and Raphael Marinier and Jeremiah Harmsen and Olivier Pietquin and Nikola Momchev},
      year={2021},
      eprint={2111.02767},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```


## robosuite_panda_pick_place_can/human_dc29b40a (default config)

*   **Config description**: Human generated dataset (50 episodes).

*   **Homepage**:
    [https://github.com/google-research/rlds](https://github.com/google-research/rlds)

*   **Download size**: `96.67 MiB`

*   **Dataset size**: `407.24 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50

*   **Feature structure**:

```python
FeaturesDict({
    'agent_id': string,
    'episode_id': string,
    'episode_index': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': float64,
        'image': Image(shape=(None, None, 3), dtype=uint8),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=float64),
            'Can_quat': Tensor(shape=(4,), dtype=float64),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=float32),
            'object-state': Tensor(shape=(14,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=float64),
        }),
        'reward': float64,
        'tag:placed': bool,
    }),
})
```

*   **Feature documentation**:

Feature                                  | Class        | Shape           | Dtype   | Description
:--------------------------------------- | :----------- | :-------------- | :------ | :----------
                                         | FeaturesDict |                 |         |
agent_id                                 | Tensor       |                 | string  |
episode_id                               | Tensor       |                 | string  |
episode_index                            | Tensor       |                 | int32   |
steps                                    | Dataset      |                 |         |
steps/action                             | Tensor       | (7,)            | float64 |
steps/discount                           | Tensor       |                 | float64 |
steps/image                              | Image        | (None, None, 3) | uint8   |
steps/is_first                           | Tensor       |                 | bool    |
steps/is_last                            | Tensor       |                 | bool    |
steps/is_terminal                        | Tensor       |                 | bool    |
steps/observation                        | FeaturesDict |                 |         |
steps/observation/Can_pos                | Tensor       | (3,)            | float64 |
steps/observation/Can_quat               | Tensor       | (4,)            | float64 |
steps/observation/Can_to_robot0_eef_pos  | Tensor       | (3,)            | float64 |
steps/observation/Can_to_robot0_eef_quat | Tensor       | (4,)            | float32 |
steps/observation/object-state           | Tensor       | (14,)           | float64 |
steps/observation/robot0_eef_pos         | Tensor       | (3,)            | float64 |
steps/observation/robot0_eef_quat        | Tensor       | (4,)            | float64 |
steps/observation/robot0_gripper_qpos    | Tensor       | (2,)            | float64 |
steps/observation/robot0_gripper_qvel    | Tensor       | (2,)            | float64 |
steps/observation/robot0_joint_pos_cos   | Tensor       | (7,)            | float64 |
steps/observation/robot0_joint_pos_sin   | Tensor       | (7,)            | float64 |
steps/observation/robot0_joint_vel       | Tensor       | (7,)            | float64 |
steps/observation/robot0_proprio-state   | Tensor       | (32,)           | float64 |
steps/reward                             | Tensor       |                 | float64 |
steps/tag:placed                         | Tensor       |                 | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robosuite_panda_pick_place_can-human_dc29b40a-1.0.0.html";
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

## robosuite_panda_pick_place_can/human_images_dc29b40a

*   **Config description**: Human generated dataset, including images with
    different camera angles in the observation. Note that it may take some time
    to generate.

*   **Homepage**:
    [https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can](https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can)

*   **Download size**: `10.95 GiB`

*   **Dataset size**: `7.53 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50

*   **Feature structure**:

```python
FeaturesDict({
    'agent_id': string,
    'episode_id': string,
    'episode_index': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': float64,
        'image': Image(shape=(None, None, 3), dtype=uint8),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=float64),
            'Can_quat': Tensor(shape=(4,), dtype=float64),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=float32),
            'agentview_image': Image(shape=(256, 256, 3), dtype=uint8),
            'birdview_image': Image(shape=(256, 256, 3), dtype=uint8),
            'object-state': Tensor(shape=(14,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(256, 256, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=float64),
            'robot0_robotview_image': Image(shape=(256, 256, 3), dtype=uint8),
        }),
        'reward': float64,
        'tag:placed': bool,
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape           | Dtype   | Description
:----------------------------------------- | :----------- | :-------------- | :------ | :----------
                                           | FeaturesDict |                 |         |
agent_id                                   | Tensor       |                 | string  |
episode_id                                 | Tensor       |                 | string  |
episode_index                              | Tensor       |                 | int32   |
steps                                      | Dataset      |                 |         |
steps/action                               | Tensor       | (7,)            | float64 |
steps/discount                             | Tensor       |                 | float64 |
steps/image                                | Image        | (None, None, 3) | uint8   |
steps/is_first                             | Tensor       |                 | bool    |
steps/is_last                              | Tensor       |                 | bool    |
steps/is_terminal                          | Tensor       |                 | bool    |
steps/observation                          | FeaturesDict |                 |         |
steps/observation/Can_pos                  | Tensor       | (3,)            | float64 |
steps/observation/Can_quat                 | Tensor       | (4,)            | float64 |
steps/observation/Can_to_robot0_eef_pos    | Tensor       | (3,)            | float64 |
steps/observation/Can_to_robot0_eef_quat   | Tensor       | (4,)            | float32 |
steps/observation/agentview_image          | Image        | (256, 256, 3)   | uint8   |
steps/observation/birdview_image           | Image        | (256, 256, 3)   | uint8   |
steps/observation/object-state             | Tensor       | (14,)           | float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)            | float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)            | float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (256, 256, 3)   | uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)            | float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)            | float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)            | float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)            | float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)            | float64 |
steps/observation/robot0_proprio-state     | Tensor       | (32,)           | float64 |
steps/observation/robot0_robotview_image   | Image        | (256, 256, 3)   | uint8   |
steps/reward                               | Tensor       |                 | float64 |
steps/tag:placed                           | Tensor       |                 | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robosuite_panda_pick_place_can-human_images_dc29b40a-1.0.0.html";
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

## robosuite_panda_pick_place_can/synthetic_stochastic_sac_afe13968

*   **Config description**: Synthetic dataset generated by a stochastic agent
    trained with SAC (200 episodes).

*   **Homepage**:
    [https://github.com/google-research/rlds](https://github.com/google-research/rlds)

*   **Download size**: `144.44 MiB`

*   **Dataset size**: `622.86 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'agent_id': string,
    'episode_id': string,
    'episode_index': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32),
        'discount': float64,
        'image': Image(shape=(None, None, 3), dtype=uint8),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=float32),
            'Can_quat': Tensor(shape=(4,), dtype=float32),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=float32),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=float32),
            'object-state': Tensor(shape=(14,), dtype=float32),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float32),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float32),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float32),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float32),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float32),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float32),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float32),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=float32),
        }),
        'reward': float64,
        'tag:placed': bool,
    }),
})
```

*   **Feature documentation**:

Feature                                  | Class        | Shape           | Dtype   | Description
:--------------------------------------- | :----------- | :-------------- | :------ | :----------
                                         | FeaturesDict |                 |         |
agent_id                                 | Tensor       |                 | string  |
episode_id                               | Tensor       |                 | string  |
episode_index                            | Tensor       |                 | int32   |
steps                                    | Dataset      |                 |         |
steps/action                             | Tensor       | (7,)            | float32 |
steps/discount                           | Tensor       |                 | float64 |
steps/image                              | Image        | (None, None, 3) | uint8   |
steps/is_first                           | Tensor       |                 | bool    |
steps/is_last                            | Tensor       |                 | bool    |
steps/is_terminal                        | Tensor       |                 | bool    |
steps/observation                        | FeaturesDict |                 |         |
steps/observation/Can_pos                | Tensor       | (3,)            | float32 |
steps/observation/Can_quat               | Tensor       | (4,)            | float32 |
steps/observation/Can_to_robot0_eef_pos  | Tensor       | (3,)            | float32 |
steps/observation/Can_to_robot0_eef_quat | Tensor       | (4,)            | float32 |
steps/observation/object-state           | Tensor       | (14,)           | float32 |
steps/observation/robot0_eef_pos         | Tensor       | (3,)            | float32 |
steps/observation/robot0_eef_quat        | Tensor       | (4,)            | float32 |
steps/observation/robot0_gripper_qpos    | Tensor       | (2,)            | float32 |
steps/observation/robot0_gripper_qvel    | Tensor       | (2,)            | float32 |
steps/observation/robot0_joint_pos_cos   | Tensor       | (7,)            | float32 |
steps/observation/robot0_joint_pos_sin   | Tensor       | (7,)            | float32 |
steps/observation/robot0_joint_vel       | Tensor       | (7,)            | float32 |
steps/observation/robot0_proprio-state   | Tensor       | (32,)           | float32 |
steps/reward                             | Tensor       |                 | float64 |
steps/tag:placed                         | Tensor       |                 | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robosuite_panda_pick_place_can-synthetic_stochastic_sac_afe13968-1.0.0.html";
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