<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bc_z" />
  <meta itemprop="description" content="Teleoped Google robot doing mostly pick-place from a table&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bc_z&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bc_z" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/datasets/google/bc-z-robot/discussion/309201" />
  <meta itemprop="citation" content="@inproceedings{jang2021bc,&#10;title={{BC}-Z: Zero-Shot Task Generalization with Robotic Imitation Learning},&#10;author={Eric Jang and Alex Irpan and Mohi Khansari and Daniel Kappler and Frederik Ebert and Corey Lynch and Sergey Levine and Chelsea Finn},&#10;booktitle={5th Annual Conference on Robot Learning},&#10;year={2021},&#10;url={https://openreview.net/forum?id=8kbp23tSGYv}}" />
</div>

# `bc_z`


*   **Description**:

Teleoped Google robot doing mostly pick-place from a table

*   **Homepage**:
    [https://www.kaggle.com/datasets/google/bc-z-robot/discussion/309201](https://www.kaggle.com/datasets/google/bc-z-robot/discussion/309201)

*   **Source code**:
    [`tfds.robotics.rtx.BcZ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `81.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 39,350
`'val'`   | 3,914

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'future/axis_angle_residual': Tensor(shape=(30,), dtype=float32, description=The next 10 actions for the rotation. Each action is a 3D delta to add to the current axis angle.),
            'future/target_close': Tensor(shape=(10,), dtype=int64, description=The next 10 actions for the gripper. Each action is the value the gripper closure should be changed to (notably it is *not* a delta.)),
            'future/xyz_residual': Tensor(shape=(30,), dtype=float32, description=The next 10 actions for the positions. Each action is a 3D delta to add to current position.),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'episode_success': float32,
            'image': Image(shape=(171, 213, 3), dtype=uint8, description=Camera image of the robot, downsampled 3x),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32, description=An embedding of the task via Universal Sentence Encoder (https://tfhub.dev/google/universal-sentence-encoder/4)),
            'natural_language_instruction': string,
            'present/autonomous': int64,
            'present/axis_angle': Tensor(shape=(3,), dtype=float32, description=The current rotation of the end effector in axis-angle representation.),
            'present/intervention': int64,
            'present/sensed_close': Tensor(shape=(1,), dtype=float32, description=How much the gripper is currently closed. Scaled from 0 to 1, but not all values from 0 to 1 are reachable. The range in the data is about 0.2 to 1),
            'present/xyz': Tensor(shape=(3,), dtype=float32, description=The current position of the end effector in axis-angle representation, in robot frame),
            'sequence_length': int64,
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                        | Class        | Shape         | Dtype   | Description
:--------------------------------------------- | :----------- | :------------ | :------ | :----------
                                               | FeaturesDict |               |         |
steps                                          | Dataset      |               |         |
steps/action                                   | FeaturesDict |               |         |
steps/action/future/axis_angle_residual        | Tensor       | (30,)         | float32 | The next 10 actions for the rotation. Each action is a 3D delta to add to the current axis angle.
steps/action/future/target_close               | Tensor       | (10,)         | int64   | The next 10 actions for the gripper. Each action is the value the gripper closure should be changed to (notably it is *not* a delta.)
steps/action/future/xyz_residual               | Tensor       | (30,)         | float32 | The next 10 actions for the positions. Each action is a 3D delta to add to current position.
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/episode_success              | Tensor       |               | float32 | A 0-1 success label
steps/observation/image                        | Image        | (171, 213, 3) | uint8   | Camera image of the robot, downsampled 3x
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 | An embedding of the task via Universal Sentence Encoder (https://tfhub.dev/google/universal-sentence-encoder/4)
steps/observation/natural_language_instruction | Tensor       |               | string  | The task the robot was asked to do.
steps/observation/present/autonomous           | Tensor       |               | int64   | Episodes are collected via DAgger. This is a 0/1 label for whether the action is from the policy or the teleoperator. 1 = from policy.
steps/observation/present/axis_angle           | Tensor       | (3,)          | float32 | The current rotation of the end effector in axis-angle representation.
steps/observation/present/intervention         | Tensor       |               | int64   | Episodes are collected via DAgger. This is a 0/1 label for whether the action is from the policy or the teleoperator. 1 = from teleoperator. This is exactly the opposite of present/autonomous
steps/observation/present/sensed_close         | Tensor       | (1,)          | float32 | How much the gripper is currently closed. Scaled from 0 to 1, but not all values from 0 to 1 are reachable. The range in the data is about 0.2 to 1
steps/observation/present/xyz                  | Tensor       | (3,)          | float32 | The current position of the end effector in axis-angle representation, in robot frame
steps/observation/sequence_length              | Tensor       |               | int64   | Length of the episode
steps/reward                                   | Scalar       |               | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bc_z-0.1.0.html";
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

*   **Citation**:

```
@inproceedings{jang2021bc,
title={{BC}-Z: Zero-Shot Task Generalization with Robotic Imitation Learning},
author={Eric Jang and Alex Irpan and Mohi Khansari and Daniel Kappler and Frederik Ebert and Corey Lynch and Sergey Levine and Chelsea Finn},
booktitle={5th Annual Conference on Robot Learning},
year={2021},
url={https://openreview.net/forum?id=8kbp23tSGYv}}
```

