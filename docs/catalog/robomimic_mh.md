<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robomimic_mh" />
  <meta itemprop="description" content="The Robomimic mixed human datasets were collected by several mixed-ability&#10;operators using the [RoboTurk](https://roboturk.stanford.edu/) platform.&#10;Each dataset consists of 200 demonstrations.&#10;&#10;Each task has two versions: one with low dimensional observations (`low_dim`),&#10;and one with images (`image`).&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robomimic_mh&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robomimic_mh" />
  <meta itemprop="sameAs" content="https://arise-initiative.github.io/robomimic-web/" />
  <meta itemprop="citation" content="@inproceedings{robomimic2021,&#10;  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},&#10;  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany&#10;          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese&#10;          and Yuke Zhu and Roberto Mart\&#x27;{i}n-Mart\&#x27;{i}n},&#10;  booktitle={Conference on Robot Learning},&#10;  year={2021}&#10;}" />
</div>

# `robomimic_mh`


*   **Description**:

The Robomimic mixed human datasets were collected by several mixed-ability
operators using the [RoboTurk](https://roboturk.stanford.edu/) platform. Each
dataset consists of 200 demonstrations.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Homepage**:
    [https://arise-initiative.github.io/robomimic-web/](https://arise-initiative.github.io/robomimic-web/)

*   **Source code**:
    [`tfds.datasets.robomimic_mh.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/robomimic_mh/robomimic_mh_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 300

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


## robomimic_mh/lift_mh_image (default config)

*   **Download size**: `2.50 GiB`

*   **Dataset size**: `363.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
20_percent                                 | Tensor       |             | bool    |
20_percent_train                           | Tensor       |             | bool    |
20_percent_valid                           | Tensor       |             | bool    |
50_percent                                 | Tensor       |             | bool    |
50_percent_train                           | Tensor       |             | bool    |
50_percent_valid                           | Tensor       |             | bool    |
better                                     | Tensor       |             | bool    |
better_operator_1                          | Tensor       |             | bool    |
better_operator_1_train                    | Tensor       |             | bool    |
better_operator_1_valid                    | Tensor       |             | bool    |
better_operator_2                          | Tensor       |             | bool    |
better_operator_2_train                    | Tensor       |             | bool    |
better_operator_2_valid                    | Tensor       |             | bool    |
better_train                               | Tensor       |             | bool    |
better_valid                               | Tensor       |             | bool    |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
okay                                       | Tensor       |             | bool    |
okay_better                                | Tensor       |             | bool    |
okay_better_train                          | Tensor       |             | bool    |
okay_better_valid                          | Tensor       |             | bool    |
okay_operator_1                            | Tensor       |             | bool    |
okay_operator_1_train                      | Tensor       |             | bool    |
okay_operator_1_valid                      | Tensor       |             | bool    |
okay_operator_2                            | Tensor       |             | bool    |
okay_operator_2_train                      | Tensor       |             | bool    |
okay_operator_2_valid                      | Tensor       |             | bool    |
okay_train                                 | Tensor       |             | bool    |
okay_valid                                 | Tensor       |             | bool    |
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
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |
worse                                      | Tensor       |             | bool    |
worse_better                               | Tensor       |             | bool    |
worse_better_train                         | Tensor       |             | bool    |
worse_better_valid                         | Tensor       |             | bool    |
worse_okay                                 | Tensor       |             | bool    |
worse_okay_train                           | Tensor       |             | bool    |
worse_okay_valid                           | Tensor       |             | bool    |
worse_operator_1                           | Tensor       |             | bool    |
worse_operator_1_train                     | Tensor       |             | bool    |
worse_operator_1_valid                     | Tensor       |             | bool    |
worse_operator_2                           | Tensor       |             | bool    |
worse_operator_2_train                     | Tensor       |             | bool    |
worse_operator_2_valid                     | Tensor       |             | bool    |
worse_train                                | Tensor       |             | bool    |
worse_valid                                | Tensor       |             | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-lift_mh_image-1.0.0.html";
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

## robomimic_mh/lift_mh_low_dim

*   **Download size**: `45.73 MiB`

*   **Dataset size**: `27.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype   | Description
:------------------------------------- | :----------- | :---- | :------ | :----------
                                       | FeaturesDict |       |         |
20_percent                             | Tensor       |       | bool    |
20_percent_train                       | Tensor       |       | bool    |
20_percent_valid                       | Tensor       |       | bool    |
50_percent                             | Tensor       |       | bool    |
50_percent_train                       | Tensor       |       | bool    |
50_percent_valid                       | Tensor       |       | bool    |
better                                 | Tensor       |       | bool    |
better_operator_1                      | Tensor       |       | bool    |
better_operator_1_train                | Tensor       |       | bool    |
better_operator_1_valid                | Tensor       |       | bool    |
better_operator_2                      | Tensor       |       | bool    |
better_operator_2_train                | Tensor       |       | bool    |
better_operator_2_valid                | Tensor       |       | bool    |
better_train                           | Tensor       |       | bool    |
better_valid                           | Tensor       |       | bool    |
episode_id                             | Tensor       |       | string  |
horizon                                | Tensor       |       | int32   |
okay                                   | Tensor       |       | bool    |
okay_better                            | Tensor       |       | bool    |
okay_better_train                      | Tensor       |       | bool    |
okay_better_valid                      | Tensor       |       | bool    |
okay_operator_1                        | Tensor       |       | bool    |
okay_operator_1_train                  | Tensor       |       | bool    |
okay_operator_1_valid                  | Tensor       |       | bool    |
okay_operator_2                        | Tensor       |       | bool    |
okay_operator_2_train                  | Tensor       |       | bool    |
okay_operator_2_valid                  | Tensor       |       | bool    |
okay_train                             | Tensor       |       | bool    |
okay_valid                             | Tensor       |       | bool    |
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
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |
worse                                  | Tensor       |       | bool    |
worse_better                           | Tensor       |       | bool    |
worse_better_train                     | Tensor       |       | bool    |
worse_better_valid                     | Tensor       |       | bool    |
worse_okay                             | Tensor       |       | bool    |
worse_okay_train                       | Tensor       |       | bool    |
worse_okay_valid                       | Tensor       |       | bool    |
worse_operator_1                       | Tensor       |       | bool    |
worse_operator_1_train                 | Tensor       |       | bool    |
worse_operator_1_valid                 | Tensor       |       | bool    |
worse_operator_2                       | Tensor       |       | bool    |
worse_operator_2_train                 | Tensor       |       | bool    |
worse_operator_2_valid                 | Tensor       |       | bool    |
worse_train                            | Tensor       |       | bool    |
worse_valid                            | Tensor       |       | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-lift_mh_low_dim-1.0.0.html";
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

## robomimic_mh/can_mh_image

*   **Download size**: `5.05 GiB`

*   **Dataset size**: `1.23 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
20_percent                                 | Tensor       |             | bool    |
20_percent_train                           | Tensor       |             | bool    |
20_percent_valid                           | Tensor       |             | bool    |
50_percent                                 | Tensor       |             | bool    |
50_percent_train                           | Tensor       |             | bool    |
50_percent_valid                           | Tensor       |             | bool    |
better                                     | Tensor       |             | bool    |
better_operator_1                          | Tensor       |             | bool    |
better_operator_1_train                    | Tensor       |             | bool    |
better_operator_1_valid                    | Tensor       |             | bool    |
better_operator_2                          | Tensor       |             | bool    |
better_operator_2_train                    | Tensor       |             | bool    |
better_operator_2_valid                    | Tensor       |             | bool    |
better_train                               | Tensor       |             | bool    |
better_valid                               | Tensor       |             | bool    |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
okay                                       | Tensor       |             | bool    |
okay_better                                | Tensor       |             | bool    |
okay_better_train                          | Tensor       |             | bool    |
okay_better_valid                          | Tensor       |             | bool    |
okay_operator_1                            | Tensor       |             | bool    |
okay_operator_1_train                      | Tensor       |             | bool    |
okay_operator_1_valid                      | Tensor       |             | bool    |
okay_operator_2                            | Tensor       |             | bool    |
okay_operator_2_train                      | Tensor       |             | bool    |
okay_operator_2_valid                      | Tensor       |             | bool    |
okay_train                                 | Tensor       |             | bool    |
okay_valid                                 | Tensor       |             | bool    |
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
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |
worse                                      | Tensor       |             | bool    |
worse_better                               | Tensor       |             | bool    |
worse_better_train                         | Tensor       |             | bool    |
worse_better_valid                         | Tensor       |             | bool    |
worse_okay                                 | Tensor       |             | bool    |
worse_okay_train                           | Tensor       |             | bool    |
worse_okay_valid                           | Tensor       |             | bool    |
worse_operator_1                           | Tensor       |             | bool    |
worse_operator_1_train                     | Tensor       |             | bool    |
worse_operator_1_valid                     | Tensor       |             | bool    |
worse_operator_2                           | Tensor       |             | bool    |
worse_operator_2_train                     | Tensor       |             | bool    |
worse_operator_2_valid                     | Tensor       |             | bool    |
worse_train                                | Tensor       |             | bool    |
worse_valid                                | Tensor       |             | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-can_mh_image-1.0.0.html";
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

## robomimic_mh/can_mh_low_dim

*   **Download size**: `107.28 MiB`

*   **Dataset size**: `75.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype   | Description
:------------------------------------- | :----------- | :---- | :------ | :----------
                                       | FeaturesDict |       |         |
20_percent                             | Tensor       |       | bool    |
20_percent_train                       | Tensor       |       | bool    |
20_percent_valid                       | Tensor       |       | bool    |
50_percent                             | Tensor       |       | bool    |
50_percent_train                       | Tensor       |       | bool    |
50_percent_valid                       | Tensor       |       | bool    |
better                                 | Tensor       |       | bool    |
better_operator_1                      | Tensor       |       | bool    |
better_operator_1_train                | Tensor       |       | bool    |
better_operator_1_valid                | Tensor       |       | bool    |
better_operator_2                      | Tensor       |       | bool    |
better_operator_2_train                | Tensor       |       | bool    |
better_operator_2_valid                | Tensor       |       | bool    |
better_train                           | Tensor       |       | bool    |
better_valid                           | Tensor       |       | bool    |
episode_id                             | Tensor       |       | string  |
horizon                                | Tensor       |       | int32   |
okay                                   | Tensor       |       | bool    |
okay_better                            | Tensor       |       | bool    |
okay_better_train                      | Tensor       |       | bool    |
okay_better_valid                      | Tensor       |       | bool    |
okay_operator_1                        | Tensor       |       | bool    |
okay_operator_1_train                  | Tensor       |       | bool    |
okay_operator_1_valid                  | Tensor       |       | bool    |
okay_operator_2                        | Tensor       |       | bool    |
okay_operator_2_train                  | Tensor       |       | bool    |
okay_operator_2_valid                  | Tensor       |       | bool    |
okay_train                             | Tensor       |       | bool    |
okay_valid                             | Tensor       |       | bool    |
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
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |
worse                                  | Tensor       |       | bool    |
worse_better                           | Tensor       |       | bool    |
worse_better_train                     | Tensor       |       | bool    |
worse_better_valid                     | Tensor       |       | bool    |
worse_okay                             | Tensor       |       | bool    |
worse_okay_train                       | Tensor       |       | bool    |
worse_okay_valid                       | Tensor       |       | bool    |
worse_operator_1                       | Tensor       |       | bool    |
worse_operator_1_train                 | Tensor       |       | bool    |
worse_operator_1_valid                 | Tensor       |       | bool    |
worse_operator_2                       | Tensor       |       | bool    |
worse_operator_2_train                 | Tensor       |       | bool    |
worse_operator_2_valid                 | Tensor       |       | bool    |
worse_train                            | Tensor       |       | bool    |
worse_valid                            | Tensor       |       | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-can_mh_low_dim-1.0.0.html";
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

## robomimic_mh/square_mh_image

*   **Download size**: `6.48 GiB`

*   **Dataset size**: `1.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
        'states': Tensor(shape=(45,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
20_percent                                 | Tensor       |             | bool    |
20_percent_train                           | Tensor       |             | bool    |
20_percent_valid                           | Tensor       |             | bool    |
50_percent                                 | Tensor       |             | bool    |
50_percent_train                           | Tensor       |             | bool    |
50_percent_valid                           | Tensor       |             | bool    |
better                                     | Tensor       |             | bool    |
better_operator_1                          | Tensor       |             | bool    |
better_operator_1_train                    | Tensor       |             | bool    |
better_operator_1_valid                    | Tensor       |             | bool    |
better_operator_2                          | Tensor       |             | bool    |
better_operator_2_train                    | Tensor       |             | bool    |
better_operator_2_valid                    | Tensor       |             | bool    |
better_train                               | Tensor       |             | bool    |
better_valid                               | Tensor       |             | bool    |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
okay                                       | Tensor       |             | bool    |
okay_better                                | Tensor       |             | bool    |
okay_better_train                          | Tensor       |             | bool    |
okay_better_valid                          | Tensor       |             | bool    |
okay_operator_1                            | Tensor       |             | bool    |
okay_operator_1_train                      | Tensor       |             | bool    |
okay_operator_1_valid                      | Tensor       |             | bool    |
okay_operator_2                            | Tensor       |             | bool    |
okay_operator_2_train                      | Tensor       |             | bool    |
okay_operator_2_valid                      | Tensor       |             | bool    |
okay_train                                 | Tensor       |             | bool    |
okay_valid                                 | Tensor       |             | bool    |
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
steps/states                               | Tensor       | (45,)       | float64 |
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |
worse                                      | Tensor       |             | bool    |
worse_better                               | Tensor       |             | bool    |
worse_better_train                         | Tensor       |             | bool    |
worse_better_valid                         | Tensor       |             | bool    |
worse_okay                                 | Tensor       |             | bool    |
worse_okay_train                           | Tensor       |             | bool    |
worse_okay_valid                           | Tensor       |             | bool    |
worse_operator_1                           | Tensor       |             | bool    |
worse_operator_1_train                     | Tensor       |             | bool    |
worse_operator_1_valid                     | Tensor       |             | bool    |
worse_operator_2                           | Tensor       |             | bool    |
worse_operator_2_train                     | Tensor       |             | bool    |
worse_operator_2_valid                     | Tensor       |             | bool    |
worse_train                                | Tensor       |             | bool    |
worse_valid                                | Tensor       |             | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-square_mh_image-1.0.0.html";
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

## robomimic_mh/square_mh_low_dim

*   **Download size**: `118.13 MiB`

*   **Dataset size**: `80.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_operator_1': bool,
    'better_operator_1_train': bool,
    'better_operator_1_valid': bool,
    'better_operator_2': bool,
    'better_operator_2_train': bool,
    'better_operator_2_valid': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_operator_1': bool,
    'okay_operator_1_train': bool,
    'okay_operator_1_valid': bool,
    'okay_operator_2': bool,
    'okay_operator_2_train': bool,
    'okay_operator_2_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
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
        'states': Tensor(shape=(45,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_operator_1': bool,
    'worse_operator_1_train': bool,
    'worse_operator_1_valid': bool,
    'worse_operator_2': bool,
    'worse_operator_2_train': bool,
    'worse_operator_2_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype   | Description
:------------------------------------- | :----------- | :---- | :------ | :----------
                                       | FeaturesDict |       |         |
20_percent                             | Tensor       |       | bool    |
20_percent_train                       | Tensor       |       | bool    |
20_percent_valid                       | Tensor       |       | bool    |
50_percent                             | Tensor       |       | bool    |
50_percent_train                       | Tensor       |       | bool    |
50_percent_valid                       | Tensor       |       | bool    |
better                                 | Tensor       |       | bool    |
better_operator_1                      | Tensor       |       | bool    |
better_operator_1_train                | Tensor       |       | bool    |
better_operator_1_valid                | Tensor       |       | bool    |
better_operator_2                      | Tensor       |       | bool    |
better_operator_2_train                | Tensor       |       | bool    |
better_operator_2_valid                | Tensor       |       | bool    |
better_train                           | Tensor       |       | bool    |
better_valid                           | Tensor       |       | bool    |
episode_id                             | Tensor       |       | string  |
horizon                                | Tensor       |       | int32   |
okay                                   | Tensor       |       | bool    |
okay_better                            | Tensor       |       | bool    |
okay_better_train                      | Tensor       |       | bool    |
okay_better_valid                      | Tensor       |       | bool    |
okay_operator_1                        | Tensor       |       | bool    |
okay_operator_1_train                  | Tensor       |       | bool    |
okay_operator_1_valid                  | Tensor       |       | bool    |
okay_operator_2                        | Tensor       |       | bool    |
okay_operator_2_train                  | Tensor       |       | bool    |
okay_operator_2_valid                  | Tensor       |       | bool    |
okay_train                             | Tensor       |       | bool    |
okay_valid                             | Tensor       |       | bool    |
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
steps/states                           | Tensor       | (45,) | float64 |
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |
worse                                  | Tensor       |       | bool    |
worse_better                           | Tensor       |       | bool    |
worse_better_train                     | Tensor       |       | bool    |
worse_better_valid                     | Tensor       |       | bool    |
worse_okay                             | Tensor       |       | bool    |
worse_okay_train                       | Tensor       |       | bool    |
worse_okay_valid                       | Tensor       |       | bool    |
worse_operator_1                       | Tensor       |       | bool    |
worse_operator_1_train                 | Tensor       |       | bool    |
worse_operator_1_valid                 | Tensor       |       | bool    |
worse_operator_2                       | Tensor       |       | bool    |
worse_operator_2_train                 | Tensor       |       | bool    |
worse_operator_2_valid                 | Tensor       |       | bool    |
worse_train                            | Tensor       |       | bool    |
worse_valid                            | Tensor       |       | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-square_mh_low_dim-1.0.0.html";
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

## robomimic_mh/transport_mh_image

*   **Download size**: `31.47 GiB`

*   **Dataset size**: `7.69 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=float64),
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
            'robot1_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot1_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
            'shouldercamera0_image': Image(shape=(84, 84, 3), dtype=uint8),
            'shouldercamera1_image': Image(shape=(84, 84, 3), dtype=uint8),
        }),
        'reward': float64,
        'states': Tensor(shape=(115,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype   | Description
:----------------------------------------- | :----------- | :---------- | :------ | :----------
                                           | FeaturesDict |             |         |
20_percent                                 | Tensor       |             | bool    |
20_percent_train                           | Tensor       |             | bool    |
20_percent_valid                           | Tensor       |             | bool    |
50_percent                                 | Tensor       |             | bool    |
50_percent_train                           | Tensor       |             | bool    |
50_percent_valid                           | Tensor       |             | bool    |
better                                     | Tensor       |             | bool    |
better_train                               | Tensor       |             | bool    |
better_valid                               | Tensor       |             | bool    |
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
okay                                       | Tensor       |             | bool    |
okay_better                                | Tensor       |             | bool    |
okay_better_train                          | Tensor       |             | bool    |
okay_better_valid                          | Tensor       |             | bool    |
okay_train                                 | Tensor       |             | bool    |
okay_valid                                 | Tensor       |             | bool    |
steps                                      | Dataset      |             |         |
steps/action                               | Tensor       | (14,)       | float64 |
steps/discount                             | Tensor       |             | int32   |
steps/is_first                             | Tensor       |             | bool    |
steps/is_last                              | Tensor       |             | bool    |
steps/is_terminal                          | Tensor       |             | bool    |
steps/observation                          | FeaturesDict |             |         |
steps/observation/object                   | Tensor       | (41,)       | float64 |
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
steps/observation/robot1_eef_pos           | Tensor       | (3,)        | float64 | End-effector position
steps/observation/robot1_eef_quat          | Tensor       | (4,)        | float64 | End-effector orientation
steps/observation/robot1_eef_vel_ang       | Tensor       | (3,)        | float64 | End-effector angular velocity
steps/observation/robot1_eef_vel_lin       | Tensor       | (3,)        | float64 | End-effector cartesian velocity
steps/observation/robot1_eye_in_hand_image | Image        | (84, 84, 3) | uint8   |
steps/observation/robot1_gripper_qpos      | Tensor       | (2,)        | float64 | Gripper position
steps/observation/robot1_gripper_qvel      | Tensor       | (2,)        | float64 | Gripper velocity
steps/observation/robot1_joint_pos         | Tensor       | (7,)        | float64 | 7DOF joint positions
steps/observation/robot1_joint_pos_cos     | Tensor       | (7,)        | float64 |
steps/observation/robot1_joint_pos_sin     | Tensor       | (7,)        | float64 |
steps/observation/robot1_joint_vel         | Tensor       | (7,)        | float64 | 7DOF joint velocities
steps/observation/shouldercamera0_image    | Image        | (84, 84, 3) | uint8   |
steps/observation/shouldercamera1_image    | Image        | (84, 84, 3) | uint8   |
steps/reward                               | Tensor       |             | float64 |
steps/states                               | Tensor       | (115,)      | float64 |
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |
worse                                      | Tensor       |             | bool    |
worse_better                               | Tensor       |             | bool    |
worse_better_train                         | Tensor       |             | bool    |
worse_better_valid                         | Tensor       |             | bool    |
worse_okay                                 | Tensor       |             | bool    |
worse_okay_train                           | Tensor       |             | bool    |
worse_okay_valid                           | Tensor       |             | bool    |
worse_train                                | Tensor       |             | bool    |
worse_valid                                | Tensor       |             | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-transport_mh_image-1.0.0.html";
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

## robomimic_mh/transport_mh_low_dim

*   **Download size**: `607.47 MiB`

*   **Dataset size**: `434.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'better': bool,
    'better_train': bool,
    'better_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'okay': bool,
    'okay_better': bool,
    'okay_better_train': bool,
    'okay_better_valid': bool,
    'okay_train': bool,
    'okay_valid': bool,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=float64),
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
            'robot1_eef_pos': Tensor(shape=(3,), dtype=float64, description=End-effector position),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=float64, description=End-effector orientation),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=float64, description=End-effector angular velocity),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=float64, description=End-effector cartesian velocity),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=float64, description=Gripper position),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=float64, description=Gripper velocity),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=float64, description=7DOF joint positions),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=float64, description=7DOF joint velocities),
        }),
        'reward': float64,
        'states': Tensor(shape=(115,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
    'worse': bool,
    'worse_better': bool,
    'worse_better_train': bool,
    'worse_better_valid': bool,
    'worse_okay': bool,
    'worse_okay_train': bool,
    'worse_okay_valid': bool,
    'worse_train': bool,
    'worse_valid': bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape  | Dtype   | Description
:------------------------------------- | :----------- | :----- | :------ | :----------
                                       | FeaturesDict |        |         |
20_percent                             | Tensor       |        | bool    |
20_percent_train                       | Tensor       |        | bool    |
20_percent_valid                       | Tensor       |        | bool    |
50_percent                             | Tensor       |        | bool    |
50_percent_train                       | Tensor       |        | bool    |
50_percent_valid                       | Tensor       |        | bool    |
better                                 | Tensor       |        | bool    |
better_train                           | Tensor       |        | bool    |
better_valid                           | Tensor       |        | bool    |
episode_id                             | Tensor       |        | string  |
horizon                                | Tensor       |        | int32   |
okay                                   | Tensor       |        | bool    |
okay_better                            | Tensor       |        | bool    |
okay_better_train                      | Tensor       |        | bool    |
okay_better_valid                      | Tensor       |        | bool    |
okay_train                             | Tensor       |        | bool    |
okay_valid                             | Tensor       |        | bool    |
steps                                  | Dataset      |        |         |
steps/action                           | Tensor       | (14,)  | float64 |
steps/discount                         | Tensor       |        | int32   |
steps/is_first                         | Tensor       |        | bool    |
steps/is_last                          | Tensor       |        | bool    |
steps/is_terminal                      | Tensor       |        | bool    |
steps/observation                      | FeaturesDict |        |         |
steps/observation/object               | Tensor       | (41,)  | float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)   | float64 | End-effector position
steps/observation/robot0_eef_quat      | Tensor       | (4,)   | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)   | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)   | float64 | End-effector cartesian velocity
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)   | float64 | Gripper position
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)   | float64 | Gripper velocity
steps/observation/robot0_joint_pos     | Tensor       | (7,)   | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)   | float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)   | float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)   | float64 | 7DOF joint velocities
steps/observation/robot1_eef_pos       | Tensor       | (3,)   | float64 | End-effector position
steps/observation/robot1_eef_quat      | Tensor       | (4,)   | float64 | End-effector orientation
steps/observation/robot1_eef_vel_ang   | Tensor       | (3,)   | float64 | End-effector angular velocity
steps/observation/robot1_eef_vel_lin   | Tensor       | (3,)   | float64 | End-effector cartesian velocity
steps/observation/robot1_gripper_qpos  | Tensor       | (2,)   | float64 | Gripper position
steps/observation/robot1_gripper_qvel  | Tensor       | (2,)   | float64 | Gripper velocity
steps/observation/robot1_joint_pos     | Tensor       | (7,)   | float64 | 7DOF joint positions
steps/observation/robot1_joint_pos_cos | Tensor       | (7,)   | float64 |
steps/observation/robot1_joint_pos_sin | Tensor       | (7,)   | float64 |
steps/observation/robot1_joint_vel     | Tensor       | (7,)   | float64 | 7DOF joint velocities
steps/reward                           | Tensor       |        | float64 |
steps/states                           | Tensor       | (115,) | float64 |
train                                  | Tensor       |        | bool    |
valid                                  | Tensor       |        | bool    |
worse                                  | Tensor       |        | bool    |
worse_better                           | Tensor       |        | bool    |
worse_better_train                     | Tensor       |        | bool    |
worse_better_valid                     | Tensor       |        | bool    |
worse_okay                             | Tensor       |        | bool    |
worse_okay_train                       | Tensor       |        | bool    |
worse_okay_valid                       | Tensor       |        | bool    |
worse_train                            | Tensor       |        | bool    |
worse_valid                            | Tensor       |        | bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_mh-transport_mh_low_dim-1.0.0.html";
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