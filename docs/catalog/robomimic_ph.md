<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robomimic_ph" />
  <meta itemprop="description" content="The Robomimic proficient human datasets were collected by 1 proficient operator&#10;using the [RoboTurk](https://roboturk.stanford.edu/) platform (with the&#10;exception of Transport, which had 2 proficient operators working together).&#10;Each dataset consists of 200 successful trajectories.&#10;&#10;Each task has two versions: one with low dimensional observations (`low_dim`),&#10;and one with images (`image`).&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robomimic_ph&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robomimic_ph" />
  <meta itemprop="sameAs" content="https://arise-initiative.github.io/robomimic-web/" />
  <meta itemprop="citation" content="@inproceedings{robomimic2021,&#10;  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},&#10;  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany&#10;          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese&#10;          and Yuke Zhu and Roberto Mart\&#x27;{i}n-Mart\&#x27;{i}n},&#10;  booktitle={Conference on Robot Learning},&#10;  year={2021}&#10;}" />
</div>

# `robomimic_ph`


*   **Description**:

The Robomimic proficient human datasets were collected by 1 proficient operator
using the [RoboTurk](https://roboturk.stanford.edu/) platform (with the
exception of Transport, which had 2 proficient operators working together). Each
dataset consists of 200 successful trajectories.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Homepage**:
    [https://arise-initiative.github.io/robomimic-web/](https://arise-initiative.github.io/robomimic-web/)

*   **Source code**:
    [`tfds.datasets.robomimic_ph.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/robomimic_ph/robomimic_ph_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Citation updated.

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

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


## robomimic_ph/lift_ph_image (default config)

*   **Download size**: `798.43 MiB`

*   **Dataset size**: `114.47 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(32,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |

## robomimic_ph/lift_ph_low_dim

*   **Download size**: `17.69 MiB`

*   **Dataset size**: `8.50 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(32,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |

## robomimic_ph/can_ph_image

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `474.55 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(71,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |

## robomimic_ph/can_ph_low_dim

*   **Download size**: `43.38 MiB`

*   **Dataset size**: `27.73 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(71,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |

## robomimic_ph/square_ph_image

*   **Download size**: `2.42 GiB`

*   **Dataset size**: `401.28 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(45,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
steps/states                               | Tensor       | (45,)       | float64 |
train                                      | Tensor       |             | bool    |
valid                                      | Tensor       |             | bool    |

## robomimic_ph/square_ph_low_dim

*   **Download size**: `47.69 MiB`

*   **Dataset size**: `29.91 MiB`

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
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(45,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
steps/states                           | Tensor       | (45,) | float64 |
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |

## robomimic_ph/transport_ph_image

*   **Download size**: `15.07 GiB`

*   **Dataset size**: `3.64 GiB`

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
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
            'robot1_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot1_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=uint8),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=float64),
            'shouldercamera0_image': Image(shape=(84, 84, 3), dtype=uint8),
            'shouldercamera1_image': Image(shape=(84, 84, 3), dtype=uint8),
        }),
        'reward': float64,
        'states': Tensor(shape=(115,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
episode_id                                 | Tensor       |             | string  |
horizon                                    | Tensor       |             | int32   |
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

## robomimic_ph/transport_ph_low_dim

*   **Download size**: `294.70 MiB`

*   **Dataset size**: `208.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': bool,
    '20_percent_train': bool,
    '20_percent_valid': bool,
    '50_percent': bool,
    '50_percent_train': bool,
    '50_percent_valid': bool,
    'episode_id': string,
    'horizon': int32,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=float64),
        'discount': int32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
            'robot1_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(115,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
episode_id                             | Tensor       |        | string  |
horizon                                | Tensor       |        | int32   |
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

## robomimic_ph/tool_hang_ph_image

*   **Download size**: `61.96 GiB`

*   **Dataset size**: `9.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

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
            'object': Tensor(shape=(44,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_eye_in_hand_image': Image(shape=(240, 240, 3), dtype=uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
            'sideview_image': Image(shape=(240, 240, 3), dtype=uint8),
        }),
        'reward': float64,
        'states': Tensor(shape=(58,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape         | Dtype   | Description
:----------------------------------------- | :----------- | :------------ | :------ | :----------
                                           | FeaturesDict |               |         |
episode_id                                 | Tensor       |               | string  |
horizon                                    | Tensor       |               | int32   |
steps                                      | Dataset      |               |         |
steps/action                               | Tensor       | (7,)          | float64 |
steps/discount                             | Tensor       |               | int32   |
steps/is_first                             | Tensor       |               | bool    |
steps/is_last                              | Tensor       |               | bool    |
steps/is_terminal                          | Tensor       |               | bool    |
steps/observation                          | FeaturesDict |               |         |
steps/observation/object                   | Tensor       | (44,)         | float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)          | float64 | End-effector position
steps/observation/robot0_eef_quat          | Tensor       | (4,)          | float64 | End-effector orientation
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)          | float64 | End-effector angular velocity
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)          | float64 | End-effector cartesian velocity
steps/observation/robot0_eye_in_hand_image | Image        | (240, 240, 3) | uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)          | float64 | Gripper position
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)          | float64 | Gripper velocity
steps/observation/robot0_joint_pos         | Tensor       | (7,)          | float64 | 7DOF joint positions
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)          | float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)          | float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)          | float64 | 7DOF joint velocities
steps/observation/sideview_image           | Image        | (240, 240, 3) | uint8   |
steps/reward                               | Tensor       |               | float64 |
steps/states                               | Tensor       | (58,)         | float64 |
train                                      | Tensor       |               | bool    |
valid                                      | Tensor       |               | bool    |

## robomimic_ph/tool_hang_ph_low_dim

*   **Download size**: `192.29 MiB`

*   **Dataset size**: `121.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

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
            'object': Tensor(shape=(44,), dtype=float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=float64),
        }),
        'reward': float64,
        'states': Tensor(shape=(58,), dtype=float64),
    }),
    'train': bool,
    'valid': bool,
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
steps/observation/object               | Tensor       | (44,) | float64 |
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
steps/states                           | Tensor       | (58,) | float64 |
train                                  | Tensor       |       | bool    |
valid                                  | Tensor       |       | bool    |
