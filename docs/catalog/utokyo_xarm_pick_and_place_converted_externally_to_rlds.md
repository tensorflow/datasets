<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="utokyo_xarm_pick_and_place_converted_externally_to_rlds" />
  <meta itemprop="description" content="xArm picking and placing objects&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;utokyo_xarm_pick_and_place_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/utokyo_xarm_pick_and_place_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="--" />
  <meta itemprop="citation" content="@misc{matsushima2023weblab,&#10;  title={Weblab xArm Dataset},&#10;  author={Tatsuya Matsushima and Hiroki Furuta and Yusuke Iwasawa and Yutaka Matsuo},&#10;  year={2023},&#10;}" />
</div>

# `utokyo_xarm_pick_and_place_converted_externally_to_rlds`


*   **Description**:

xArm picking and placing objects

*   **Homepage**: [--](--)

*   **Source code**:
    [`tfds.robotics.rtx.UtokyoXarmPickAndPlaceConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `1.29 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 92
`'val'`   | 10

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x EEF position, 3x EEF orientation yaw/pitch/roll, 1x gripper open/close position].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'end_effector_pose': Tensor(shape=(6,), dtype=float32, description=Robot end effector pose, consists of [3x EEF position, 3x EEF orientation yaw/pitch/roll].),
            'hand_image': Image(shape=(224, 224, 3), dtype=uint8, description=Hand camera RGB observation.),
            'image': Image(shape=(224, 224, 3), dtype=uint8, description=Main camera RGB observation.),
            'image2': Image(shape=(224, 224, 3), dtype=uint8, description=Another camera RGB observation from different view point.),
            'joint_state': Tensor(shape=(14,), dtype=float32, description=Robot joint state, consists of [7x robot joint angles, 7x robot joint velocity].),
            'joint_trajectory': Tensor(shape=(21,), dtype=float32, description=Robot joint trajectory, consists of [7x robot joint angles, 7x robot joint velocity, 7x robot joint acceralation].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                             | Class        | Shape         | Dtype   | Description
:---------------------------------- | :----------- | :------------ | :------ | :----------
                                    | FeaturesDict |               |         |
episode_metadata                    | FeaturesDict |               |         |
episode_metadata/file_path          | Text         |               | string  | Path to the original data file.
steps                               | Dataset      |               |         |
steps/action                        | Tensor       | (7,)          | float32 | Robot action, consists of [3x EEF position, 3x EEF orientation yaw/pitch/roll, 1x gripper open/close position].
steps/discount                      | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                      | Tensor       |               | bool    |
steps/is_last                       | Tensor       |               | bool    |
steps/is_terminal                   | Tensor       |               | bool    |
steps/language_embedding            | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction          | Text         |               | string  | Language Instruction.
steps/observation                   | FeaturesDict |               |         |
steps/observation/end_effector_pose | Tensor       | (6,)          | float32 | Robot end effector pose, consists of [3x EEF position, 3x EEF orientation yaw/pitch/roll].
steps/observation/hand_image        | Image        | (224, 224, 3) | uint8   | Hand camera RGB observation.
steps/observation/image             | Image        | (224, 224, 3) | uint8   | Main camera RGB observation.
steps/observation/image2            | Image        | (224, 224, 3) | uint8   | Another camera RGB observation from different view point.
steps/observation/joint_state       | Tensor       | (14,)         | float32 | Robot joint state, consists of [7x robot joint angles, 7x robot joint velocity].
steps/observation/joint_trajectory  | Tensor       | (21,)         | float32 | Robot joint trajectory, consists of [7x robot joint angles, 7x robot joint velocity, 7x robot joint acceralation].
steps/reward                        | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/utokyo_xarm_pick_and_place_converted_externally_to_rlds-0.1.0.html";
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
@misc{matsushima2023weblab,
  title={Weblab xArm Dataset},
  author={Tatsuya Matsushima and Hiroki Furuta and Yusuke Iwasawa and Yutaka Matsuo},
  year={2023},
}
```

