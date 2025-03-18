<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robomimic_mg" />
  <meta itemprop="description" content="The Robomimic machine generated datasets were collected using a Soft Actor&#10;Critic agent trained with a dense reward.&#10;Each dataset consists of the agent&#x27;s replay buffer.&#10;&#10;Each task has two versions: one with low dimensional observations (`low_dim`),&#10;and one with images (`image`).&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robomimic_mg&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robomimic_mg" />
  <meta itemprop="sameAs" content="https://arise-initiative.github.io/robomimic-web/" />
  <meta itemprop="citation" content="@inproceedings{robomimic2021,&#10;  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},&#10;  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany&#10;          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese&#10;          and Yuke Zhu and Roberto Mart\&#x27;{i}n-Mart\&#x27;{i}n},&#10;  booktitle={Conference on Robot Learning},&#10;  year={2021}&#10;}" />
</div>

# `robomimic_mg`


*   **Description**:

The Robomimic machine generated datasets were collected using a Soft Actor
Critic agent trained with a dense reward. Each dataset consists of the agent's
replay buffer.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Homepage**:
    [https://arise-initiative.github.io/robomimic-web/](https://arise-initiative.github.io/robomimic-web/)

*   **Source code**:
    [`tfds.datasets.robomimic_mg.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/robomimic_mg/robomimic_mg_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{robomimic2021,
  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},
  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany
          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese
          and Yuke Zhu and Roberto Mart\'{i}n-Mart\'{i}n},
  booktitle={Conference on Robot Learning},
  year={2021}
}
```


## robomimic_mg/lift_mg_image (default config)

*   **Download size**: `18.04 GiB`

*   **Dataset size**: `2.73 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'agentview_image': Image(shape=(84, 84, 3), dtype=uint8),
            'object': Tensor(shape=(10,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
        }),
        'reward': float64,
        'states': Tensor(shape=(32,), dtype=float64),
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
steps                                      | Dataset      |             |         |
steps/action                               | Tensor       | (7,)        | float64 |
steps/discount                             | Tensor       |             | int32   |
steps/is_first                             | Tensor       |             | bool    |
steps/is_last                              | Tensor       |             | bool    |
steps/is_terminal                          | Tensor       |             | bool    |
steps/observation                          | FeaturesDict |             |         |
steps/observation/agentview_image          | Image        | (84, 84, 3) | uint8   |
steps/observation/object                   | Tensor       | (10,)       | float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | float64 | End-effector position
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | float64 | End-effector cartesian velocity
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | float64 | Gripper position
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | float64 | Gripper velocity
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | float64 | 7DOF joint velocities
steps/reward                               | Tensor       |             | float64 |
steps/states                               | Tensor       | (32,)       | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mg-lift_mg_image-1.0.0.html";
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

## robomimic_mg/lift_mg_low_dim

*   **Download size**: `302.25 MiB`

*   **Dataset size**: `195.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(10,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
        }),
        'reward': float64,
        'states': Tensor(shape=(32,), dtype=float64),
    }),
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype   | Description
:------------------------------------- | :----------- | :---- | :------ | :----------
                                       | FeaturesDict |       |         |
episode_id                             | Tensor       |       | string  |
horizon                                | Tensor       |       | int32   |
steps                                  | Dataset      |       |         |
steps/action                           | Tensor       | (7,)  | float64 |
steps/discount                         | Tensor       |       | int32   |
steps/is_first                         | Tensor       |       | bool    |
steps/is_last                          | Tensor       |       | bool    |
steps/is_terminal                      | Tensor       |       | bool    |
steps/observation                      | FeaturesDict |       |         |
steps/observation/object               | Tensor       | (10,) | float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | float64 | End-effector position
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | float64 | End-effector cartesian velocity
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | float64 | Gripper position
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | float64 | Gripper velocity
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | float64 | 7DOF joint velocities
steps/reward                           | Tensor       |       | float64 |
steps/states                           | Tensor       | (32,) | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mg-lift_mg_low_dim-1.0.0.html";
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

## robomimic_mg/can_mg_image

*   **Download size**: `47.14 GiB`

*   **Dataset size**: `11.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,900

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'agentview_image': Image(shape=(84, 84, 3), dtype=uint8),
            'object': Tensor(shape=(14,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
        }),
        'reward': float64,
        'states': Tensor(shape=(71,), dtype=float64),
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
steps                                      | Dataset      |             |         |
steps/action                               | Tensor       | (7,)        | float64 |
steps/discount                             | Tensor       |             | int32   |
steps/is_first                             | Tensor       |             | bool    |
steps/is_last                              | Tensor       |             | bool    |
steps/is_terminal                          | Tensor       |             | bool    |
steps/observation                          | FeaturesDict |             |         |
steps/observation/agentview_image          | Image        | (84, 84, 3) | uint8   |
steps/observation/object                   | Tensor       | (14,)       | float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | float64 | End-effector position
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | float64 | End-effector cartesian velocity
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | float64 | Gripper position
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | float64 | Gripper velocity
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | float64 | 7DOF joint velocities
steps/reward                               | Tensor       |             | float64 |
steps/states                               | Tensor       | (71,)       | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mg-can_mg_image-1.0.0.html";
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

## robomimic_mg/can_mg_low_dim

*   **Download size**: `1.01 GiB`

*   **Dataset size**: `697.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,900

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(14,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
        }),
        'reward': float64,
        'states': Tensor(shape=(71,), dtype=float64),
    }),
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype   | Description
:------------------------------------- | :----------- | :---- | :------ | :----------
                                       | FeaturesDict |       |         |
episode_id                             | Tensor       |       | string  |
horizon                                | Tensor       |       | int32   |
steps                                  | Dataset      |       |         |
steps/action                           | Tensor       | (7,)  | float64 |
steps/discount                         | Tensor       |       | int32   |
steps/is_first                         | Tensor       |       | bool    |
steps/is_last                          | Tensor       |       | bool    |
steps/is_terminal                      | Tensor       |       | bool    |
steps/observation                      | FeaturesDict |       |         |
steps/observation/object               | Tensor       | (14,) | float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | float64 | End-effector position
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | float64 | End-effector cartesian velocity
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | float64 | Gripper position
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | float64 | Gripper velocity
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | float64 | 7DOF joint velocities
steps/reward                           | Tensor       |       | float64 |
steps/states                           | Tensor       | (71,) | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mg-can_mg_low_dim-1.0.0.html";
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