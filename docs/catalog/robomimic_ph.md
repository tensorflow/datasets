<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robomimic_ph" />
  <meta itemprop="description" content="The Proficient Human datasets were collected by 1 proficient operator using the&#10;[RoboTurk](https://roboturk.stanford.edu/) platform (with the exception of&#10;Transport, which had 2 proficient operators working together). Each dataset&#10;consists of 200 successful trajectories.&#10;&#10;Each task has two versions: one with low dimensional observations (`low_dim`),&#10;and one with images (`image`).&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robomimic_ph&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robomimic_ph" />
  <meta itemprop="sameAs" content="https://arise-initiative.github.io/robomimic-web/" />
  <meta itemprop="citation" content="@inproceedings{robomimic2021,&#10;  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},&#10;  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany&#10;          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese&#10;          and Yuke Zhu and Roberto Mart&#x27;{i}n-Mart&#x27;{i}n},&#10;  booktitle={Conference on Robot Learning},&#10;  year={2021}&#10;}" />
</div>

# `robomimic_ph`


*   **Description**:

The Proficient Human datasets were collected by 1 proficient operator using the
[RoboTurk](https://roboturk.stanford.edu/) platform (with the exception of
Transport, which had 2 proficient operators working together). Each dataset
consists of 200 successful trajectories.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Homepage**:
    [https://arise-initiative.github.io/robomimic-web/](https://arise-initiative.github.io/robomimic-web/)

*   **Source code**:
    [`tfds.robomimic.robomimic_ph.RobomimicPh`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robomimic/robomimic_ph/robomimic_ph.py)

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

*   **Citation**:

```
@inproceedings{robomimic2021,
  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},
  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany
          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese
          and Yuke Zhu and Roberto Mart'{i}n-Mart'{i}n},
  booktitle={Conference on Robot Learning},
  year={2021}
}
```


## robomimic_ph/lift_low_dim (default config)

*   **Download size**: `17.69 MiB`

*   **Dataset size**: `8.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(10,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(32,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype      | Description
:------------------------------------- | :----------- | :---- | :--------- | :----------
                                       | FeaturesDict |       |            |
20_percent                             | Tensor       |       | tf.bool    |
20_percent_train                       | Tensor       |       | tf.bool    |
20_percent_valid                       | Tensor       |       | tf.bool    |
50_percent                             | Tensor       |       | tf.bool    |
50_percent_train                       | Tensor       |       | tf.bool    |
50_percent_valid                       | Tensor       |       | tf.bool    |
episode_id                             | Tensor       |       | tf.string  |
horizon                                | Tensor       |       | tf.int32   |
steps                                  | Dataset      |       |            |
steps/action                           | Tensor       | (7,)  | tf.float64 |
steps/discount                         | Tensor       |       | tf.int32   |
steps/is_first                         | Tensor       |       | tf.bool    |
steps/is_last                          | Tensor       |       | tf.bool    |
steps/is_terminal                      | Tensor       |       | tf.bool    |
steps/observation                      | FeaturesDict |       |            |
steps/observation/object               | Tensor       | (10,) | tf.float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | tf.float64 |
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | tf.float64 |
steps/reward                           | Tensor       |       | tf.float64 |
steps/states                           | Tensor       | (32,) | tf.float64 |
train                                  | Tensor       |       | tf.bool    |
valid                                  | Tensor       |       | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-lift_low_dim-1.0.1.html";
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

## robomimic_ph/lift_image

*   **Download size**: `798.43 MiB`

*   **Dataset size**: `114.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'agentview_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'object': Tensor(shape=(10,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(32,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype      | Description
:----------------------------------------- | :----------- | :---------- | :--------- | :----------
                                           | FeaturesDict |             |            |
20_percent                                 | Tensor       |             | tf.bool    |
20_percent_train                           | Tensor       |             | tf.bool    |
20_percent_valid                           | Tensor       |             | tf.bool    |
50_percent                                 | Tensor       |             | tf.bool    |
50_percent_train                           | Tensor       |             | tf.bool    |
50_percent_valid                           | Tensor       |             | tf.bool    |
episode_id                                 | Tensor       |             | tf.string  |
horizon                                    | Tensor       |             | tf.int32   |
steps                                      | Dataset      |             |            |
steps/action                               | Tensor       | (7,)        | tf.float64 |
steps/discount                             | Tensor       |             | tf.int32   |
steps/is_first                             | Tensor       |             | tf.bool    |
steps/is_last                              | Tensor       |             | tf.bool    |
steps/is_terminal                          | Tensor       |             | tf.bool    |
steps/observation                          | FeaturesDict |             |            |
steps/observation/agentview_image          | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/object                   | Tensor       | (10,)       | tf.float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | tf.float64 |
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | tf.float64 |
steps/reward                               | Tensor       |             | tf.float64 |
steps/states                               | Tensor       | (32,)       | tf.float64 |
train                                      | Tensor       |             | tf.bool    |
valid                                      | Tensor       |             | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-lift_image-1.0.1.html";
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

## robomimic_ph/can_low_dim

*   **Download size**: `43.38 MiB`

*   **Dataset size**: `27.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(71,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype      | Description
:------------------------------------- | :----------- | :---- | :--------- | :----------
                                       | FeaturesDict |       |            |
20_percent                             | Tensor       |       | tf.bool    |
20_percent_train                       | Tensor       |       | tf.bool    |
20_percent_valid                       | Tensor       |       | tf.bool    |
50_percent                             | Tensor       |       | tf.bool    |
50_percent_train                       | Tensor       |       | tf.bool    |
50_percent_valid                       | Tensor       |       | tf.bool    |
episode_id                             | Tensor       |       | tf.string  |
horizon                                | Tensor       |       | tf.int32   |
steps                                  | Dataset      |       |            |
steps/action                           | Tensor       | (7,)  | tf.float64 |
steps/discount                         | Tensor       |       | tf.int32   |
steps/is_first                         | Tensor       |       | tf.bool    |
steps/is_last                          | Tensor       |       | tf.bool    |
steps/is_terminal                      | Tensor       |       | tf.bool    |
steps/observation                      | FeaturesDict |       |            |
steps/observation/object               | Tensor       | (14,) | tf.float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | tf.float64 |
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | tf.float64 |
steps/reward                           | Tensor       |       | tf.float64 |
steps/states                           | Tensor       | (71,) | tf.float64 |
train                                  | Tensor       |       | tf.bool    |
valid                                  | Tensor       |       | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-can_low_dim-1.0.1.html";
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

## robomimic_ph/can_image

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `474.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'agentview_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'object': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(71,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype      | Description
:----------------------------------------- | :----------- | :---------- | :--------- | :----------
                                           | FeaturesDict |             |            |
20_percent                                 | Tensor       |             | tf.bool    |
20_percent_train                           | Tensor       |             | tf.bool    |
20_percent_valid                           | Tensor       |             | tf.bool    |
50_percent                                 | Tensor       |             | tf.bool    |
50_percent_train                           | Tensor       |             | tf.bool    |
50_percent_valid                           | Tensor       |             | tf.bool    |
episode_id                                 | Tensor       |             | tf.string  |
horizon                                    | Tensor       |             | tf.int32   |
steps                                      | Dataset      |             |            |
steps/action                               | Tensor       | (7,)        | tf.float64 |
steps/discount                             | Tensor       |             | tf.int32   |
steps/is_first                             | Tensor       |             | tf.bool    |
steps/is_last                              | Tensor       |             | tf.bool    |
steps/is_terminal                          | Tensor       |             | tf.bool    |
steps/observation                          | FeaturesDict |             |            |
steps/observation/agentview_image          | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/object                   | Tensor       | (14,)       | tf.float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | tf.float64 |
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | tf.float64 |
steps/reward                               | Tensor       |             | tf.float64 |
steps/states                               | Tensor       | (71,)       | tf.float64 |
train                                      | Tensor       |             | tf.bool    |
valid                                      | Tensor       |             | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-can_image-1.0.1.html";
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

## robomimic_ph/square_low_dim

*   **Download size**: `47.69 MiB`

*   **Dataset size**: `29.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(45,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype      | Description
:------------------------------------- | :----------- | :---- | :--------- | :----------
                                       | FeaturesDict |       |            |
20_percent                             | Tensor       |       | tf.bool    |
20_percent_train                       | Tensor       |       | tf.bool    |
20_percent_valid                       | Tensor       |       | tf.bool    |
50_percent                             | Tensor       |       | tf.bool    |
50_percent_train                       | Tensor       |       | tf.bool    |
50_percent_valid                       | Tensor       |       | tf.bool    |
episode_id                             | Tensor       |       | tf.string  |
horizon                                | Tensor       |       | tf.int32   |
steps                                  | Dataset      |       |            |
steps/action                           | Tensor       | (7,)  | tf.float64 |
steps/discount                         | Tensor       |       | tf.int32   |
steps/is_first                         | Tensor       |       | tf.bool    |
steps/is_last                          | Tensor       |       | tf.bool    |
steps/is_terminal                      | Tensor       |       | tf.bool    |
steps/observation                      | FeaturesDict |       |            |
steps/observation/object               | Tensor       | (14,) | tf.float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | tf.float64 |
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | tf.float64 |
steps/reward                           | Tensor       |       | tf.float64 |
steps/states                           | Tensor       | (45,) | tf.float64 |
train                                  | Tensor       |       | tf.bool    |
valid                                  | Tensor       |       | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-square_low_dim-1.0.1.html";
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

## robomimic_ph/square_image

*   **Download size**: `2.42 GiB`

*   **Dataset size**: `401.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'agentview_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'object': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(45,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype      | Description
:----------------------------------------- | :----------- | :---------- | :--------- | :----------
                                           | FeaturesDict |             |            |
20_percent                                 | Tensor       |             | tf.bool    |
20_percent_train                           | Tensor       |             | tf.bool    |
20_percent_valid                           | Tensor       |             | tf.bool    |
50_percent                                 | Tensor       |             | tf.bool    |
50_percent_train                           | Tensor       |             | tf.bool    |
50_percent_valid                           | Tensor       |             | tf.bool    |
episode_id                                 | Tensor       |             | tf.string  |
horizon                                    | Tensor       |             | tf.int32   |
steps                                      | Dataset      |             |            |
steps/action                               | Tensor       | (7,)        | tf.float64 |
steps/discount                             | Tensor       |             | tf.int32   |
steps/is_first                             | Tensor       |             | tf.bool    |
steps/is_last                              | Tensor       |             | tf.bool    |
steps/is_terminal                          | Tensor       |             | tf.bool    |
steps/observation                          | FeaturesDict |             |            |
steps/observation/agentview_image          | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/object                   | Tensor       | (14,)       | tf.float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | tf.float64 |
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | tf.float64 |
steps/reward                               | Tensor       |             | tf.float64 |
steps/states                               | Tensor       | (45,)       | tf.float64 |
train                                      | Tensor       |             | tf.bool    |
valid                                      | Tensor       |             | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-square_image-1.0.1.html";
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

## robomimic_ph/transport_low_dim

*   **Download size**: `294.70 MiB`

*   **Dataset size**: `208.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(115,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape  | Dtype      | Description
:------------------------------------- | :----------- | :----- | :--------- | :----------
                                       | FeaturesDict |        |            |
20_percent                             | Tensor       |        | tf.bool    |
20_percent_train                       | Tensor       |        | tf.bool    |
20_percent_valid                       | Tensor       |        | tf.bool    |
50_percent                             | Tensor       |        | tf.bool    |
50_percent_train                       | Tensor       |        | tf.bool    |
50_percent_valid                       | Tensor       |        | tf.bool    |
episode_id                             | Tensor       |        | tf.string  |
horizon                                | Tensor       |        | tf.int32   |
steps                                  | Dataset      |        |            |
steps/action                           | Tensor       | (14,)  | tf.float64 |
steps/discount                         | Tensor       |        | tf.int32   |
steps/is_first                         | Tensor       |        | tf.bool    |
steps/is_last                          | Tensor       |        | tf.bool    |
steps/is_terminal                      | Tensor       |        | tf.bool    |
steps/observation                      | FeaturesDict |        |            |
steps/observation/object               | Tensor       | (41,)  | tf.float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)   | tf.float64 |
steps/observation/robot0_eef_quat      | Tensor       | (4,)   | tf.float64 |
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)   | tf.float64 |
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)   | tf.float64 |
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)   | tf.float64 |
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)   | tf.float64 |
steps/observation/robot0_joint_pos     | Tensor       | (7,)   | tf.float64 |
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)   | tf.float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)   | tf.float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)   | tf.float64 |
steps/observation/robot1_eef_pos       | Tensor       | (3,)   | tf.float64 |
steps/observation/robot1_eef_quat      | Tensor       | (4,)   | tf.float64 |
steps/observation/robot1_eef_vel_ang   | Tensor       | (3,)   | tf.float64 |
steps/observation/robot1_eef_vel_lin   | Tensor       | (3,)   | tf.float64 |
steps/observation/robot1_gripper_qpos  | Tensor       | (2,)   | tf.float64 |
steps/observation/robot1_gripper_qvel  | Tensor       | (2,)   | tf.float64 |
steps/observation/robot1_joint_pos     | Tensor       | (7,)   | tf.float64 |
steps/observation/robot1_joint_pos_cos | Tensor       | (7,)   | tf.float64 |
steps/observation/robot1_joint_pos_sin | Tensor       | (7,)   | tf.float64 |
steps/observation/robot1_joint_vel     | Tensor       | (7,)   | tf.float64 |
steps/reward                           | Tensor       |        | tf.float64 |
steps/states                           | Tensor       | (115,) | tf.float64 |
train                                  | Tensor       |        | tf.bool    |
valid                                  | Tensor       |        | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-transport_low_dim-1.0.1.html";
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

## robomimic_ph/transport_image

*   **Download size**: `15.07 GiB`

*   **Dataset size**: `3.64 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    '20_percent': tf.bool,
    '20_percent_train': tf.bool,
    '20_percent_valid': tf.bool,
    '50_percent': tf.bool,
    '50_percent_train': tf.bool,
    '50_percent_valid': tf.bool,
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(14,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(41,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot1_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot1_eye_in_hand_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'robot1_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot1_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot1_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot1_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'shouldercamera0_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
            'shouldercamera1_image': Image(shape=(84, 84, 3), dtype=tf.uint8),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(115,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape       | Dtype      | Description
:----------------------------------------- | :----------- | :---------- | :--------- | :----------
                                           | FeaturesDict |             |            |
20_percent                                 | Tensor       |             | tf.bool    |
20_percent_train                           | Tensor       |             | tf.bool    |
20_percent_valid                           | Tensor       |             | tf.bool    |
50_percent                                 | Tensor       |             | tf.bool    |
50_percent_train                           | Tensor       |             | tf.bool    |
50_percent_valid                           | Tensor       |             | tf.bool    |
episode_id                                 | Tensor       |             | tf.string  |
horizon                                    | Tensor       |             | tf.int32   |
steps                                      | Dataset      |             |            |
steps/action                               | Tensor       | (14,)       | tf.float64 |
steps/discount                             | Tensor       |             | tf.int32   |
steps/is_first                             | Tensor       |             | tf.bool    |
steps/is_last                              | Tensor       |             | tf.bool    |
steps/is_terminal                          | Tensor       |             | tf.bool    |
steps/observation                          | FeaturesDict |             |            |
steps/observation/object                   | Tensor       | (41,)       | tf.float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)        | tf.float64 |
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot0_joint_pos         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot1_eef_pos           | Tensor       | (3,)        | tf.float64 |
steps/observation/robot1_eef_quat          | Tensor       | (4,)        | tf.float64 |
steps/observation/robot1_eef_vel_ang       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot1_eef_vel_lin       | Tensor       | (3,)        | tf.float64 |
steps/observation/robot1_eye_in_hand_image | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/robot1_gripper_qpos      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot1_gripper_qvel      | Tensor       | (2,)        | tf.float64 |
steps/observation/robot1_joint_pos         | Tensor       | (7,)        | tf.float64 |
steps/observation/robot1_joint_pos_cos     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot1_joint_pos_sin     | Tensor       | (7,)        | tf.float64 |
steps/observation/robot1_joint_vel         | Tensor       | (7,)        | tf.float64 |
steps/observation/shouldercamera0_image    | Image        | (84, 84, 3) | tf.uint8   |
steps/observation/shouldercamera1_image    | Image        | (84, 84, 3) | tf.uint8   |
steps/reward                               | Tensor       |             | tf.float64 |
steps/states                               | Tensor       | (115,)      | tf.float64 |
train                                      | Tensor       |             | tf.bool    |
valid                                      | Tensor       |             | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-transport_image-1.0.1.html";
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

## robomimic_ph/tool_hang_low_dim

*   **Download size**: `192.29 MiB`

*   **Dataset size**: `121.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(44,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(58,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape | Dtype      | Description
:------------------------------------- | :----------- | :---- | :--------- | :----------
                                       | FeaturesDict |       |            |
episode_id                             | Tensor       |       | tf.string  |
horizon                                | Tensor       |       | tf.int32   |
steps                                  | Dataset      |       |            |
steps/action                           | Tensor       | (7,)  | tf.float64 |
steps/discount                         | Tensor       |       | tf.int32   |
steps/is_first                         | Tensor       |       | tf.bool    |
steps/is_last                          | Tensor       |       | tf.bool    |
steps/is_terminal                      | Tensor       |       | tf.bool    |
steps/observation                      | FeaturesDict |       |            |
steps/observation/object               | Tensor       | (44,) | tf.float64 |
steps/observation/robot0_eef_pos       | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_quat      | Tensor       | (4,)  | tf.float64 |
steps/observation/robot0_eef_vel_ang   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_eef_vel_lin   | Tensor       | (3,)  | tf.float64 |
steps/observation/robot0_gripper_qpos  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_gripper_qvel  | Tensor       | (2,)  | tf.float64 |
steps/observation/robot0_joint_pos     | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_cos | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_pos_sin | Tensor       | (7,)  | tf.float64 |
steps/observation/robot0_joint_vel     | Tensor       | (7,)  | tf.float64 |
steps/reward                           | Tensor       |       | tf.float64 |
steps/states                           | Tensor       | (58,) | tf.float64 |
train                                  | Tensor       |       | tf.bool    |
valid                                  | Tensor       |       | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-tool_hang_low_dim-1.0.1.html";
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

## robomimic_ph/tool_hang_image

*   **Download size**: `61.96 GiB`

*   **Dataset size**: `9.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': tf.string,
    'horizon': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.int32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'object': Tensor(shape=(44,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_eef_vel_ang': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_vel_lin': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eye_in_hand_image': Image(shape=(240, 240, 3), dtype=tf.uint8),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'sideview_image': Image(shape=(240, 240, 3), dtype=tf.uint8),
        }),
        'reward': tf.float64,
        'states': Tensor(shape=(58,), dtype=tf.float64),
    }),
    'train': tf.bool,
    'valid': tf.bool,
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape         | Dtype      | Description
:----------------------------------------- | :----------- | :------------ | :--------- | :----------
                                           | FeaturesDict |               |            |
episode_id                                 | Tensor       |               | tf.string  |
horizon                                    | Tensor       |               | tf.int32   |
steps                                      | Dataset      |               |            |
steps/action                               | Tensor       | (7,)          | tf.float64 |
steps/discount                             | Tensor       |               | tf.int32   |
steps/is_first                             | Tensor       |               | tf.bool    |
steps/is_last                              | Tensor       |               | tf.bool    |
steps/is_terminal                          | Tensor       |               | tf.bool    |
steps/observation                          | FeaturesDict |               |            |
steps/observation/object                   | Tensor       | (44,)         | tf.float64 |
steps/observation/robot0_eef_pos           | Tensor       | (3,)          | tf.float64 |
steps/observation/robot0_eef_quat          | Tensor       | (4,)          | tf.float64 |
steps/observation/robot0_eef_vel_ang       | Tensor       | (3,)          | tf.float64 |
steps/observation/robot0_eef_vel_lin       | Tensor       | (3,)          | tf.float64 |
steps/observation/robot0_eye_in_hand_image | Image        | (240, 240, 3) | tf.uint8   |
steps/observation/robot0_gripper_qpos      | Tensor       | (2,)          | tf.float64 |
steps/observation/robot0_gripper_qvel      | Tensor       | (2,)          | tf.float64 |
steps/observation/robot0_joint_pos         | Tensor       | (7,)          | tf.float64 |
steps/observation/robot0_joint_pos_cos     | Tensor       | (7,)          | tf.float64 |
steps/observation/robot0_joint_pos_sin     | Tensor       | (7,)          | tf.float64 |
steps/observation/robot0_joint_vel         | Tensor       | (7,)          | tf.float64 |
steps/observation/sideview_image           | Image        | (240, 240, 3) | tf.uint8   |
steps/reward                               | Tensor       |               | tf.float64 |
steps/states                               | Tensor       | (58,)         | tf.float64 |
train                                      | Tensor       |               | tf.bool    |
valid                                      | Tensor       |               | tf.bool    |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robomimic_ph-tool_hang_image-1.0.1.html";
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