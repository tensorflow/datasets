<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="viola" />
  <meta itemprop="description" content="Franka robot interacting with stylized kitchen tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;viola&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/viola" />
  <meta itemprop="sameAs" content="https://ut-austin-rpl.github.io/VIOLA/" />
  <meta itemprop="citation" content="@article{zhu2022viola,&#10;  title={VIOLA: Imitation Learning for Vision-Based Manipulation with Object Proposal Priors},&#10;  author={Zhu, Yifeng and Joshi, Abhishek and Stone, Peter and Zhu, Yuke},&#10;  journal={6th Annual Conference on Robot Learning (CoRL)},&#10;  year={2022}&#10;}" />
</div>

# `viola`


*   **Description**:

Franka robot interacting with stylized kitchen tasks

*   **Homepage**:
    [https://ut-austin-rpl.github.io/VIOLA/](https://ut-austin-rpl.github.io/VIOLA/)

*   **Source code**:
    [`tfds.robotics.rtx.Viola`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `10.40 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 15
`'train'` | 135

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'gripper_closedness_action': float32,
            'rotation_delta': Tensor(shape=(3,), dtype=float32),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'agentview_rgb': Image(shape=(224, 224, 3), dtype=uint8, description=RGB captured by workspace camera),
            'ee_states': Tensor(shape=(16,), dtype=float32, description=Pose of the end effector specified as a homogenous matrix.),
            'eye_in_hand_rgb': Image(shape=(224, 224, 3), dtype=uint8, description=RGB captured by in hand camera),
            'gripper_states': Tensor(shape=(1,), dtype=float32, description=gripper_states = 0 means the gripper is fully closed. The value represents the gripper width of Franka Panda Gripper.),
            'joint_states': Tensor(shape=(7,), dtype=float32, description=joint values),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
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
steps/action/gripper_closedness_action         | Tensor       |               | float32 |
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 |
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 |
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/agentview_rgb                | Image        | (224, 224, 3) | uint8   | RGB captured by workspace camera
steps/observation/ee_states                    | Tensor       | (16,)         | float32 | Pose of the end effector specified as a homogenous matrix.
steps/observation/eye_in_hand_rgb              | Image        | (224, 224, 3) | uint8   | RGB captured by in hand camera
steps/observation/gripper_states               | Tensor       | (1,)          | float32 | gripper_states = 0 means the gripper is fully closed. The value represents the gripper width of Franka Panda Gripper.
steps/observation/joint_states                 | Tensor       | (7,)          | float32 | joint values
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/viola-0.1.0.html";
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
@article{zhu2022viola,
  title={VIOLA: Imitation Learning for Vision-Based Manipulation with Object Proposal Priors},
  author={Zhu, Yifeng and Joshi, Abhishek and Stone, Peter and Zhu, Yuke},
  journal={6th Annual Conference on Robot Learning (CoRL)},
  year={2022}
}
```

