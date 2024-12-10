<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_kuka_multimodal_dataset_converted_externally_to_rlds" />
  <meta itemprop="description" content="Kuka iiwa peg insertion with force feedback&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stanford_kuka_multimodal_dataset_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_kuka_multimodal_dataset_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/visionandtouch" />
  <meta itemprop="citation" content="@inproceedings{lee2019icra,&#10;  title={Making sense of vision and touch: Self-supervised learning of multimodal representations for contact-rich tasks},&#10;  author={Lee, Michelle A and Zhu, Yuke and Srinivasan, Krishnan and Shah, Parth and Savarese, Silvio and Fei-Fei, Li and  Garg, Animesh and Bohg, Jeannette},&#10;  booktitle={2019 IEEE International Conference on Robotics and Automation (ICRA)},&#10;  year={2019},&#10;  url={https://arxiv.org/abs/1810.10191}&#10;}" />
</div>

# `stanford_kuka_multimodal_dataset_converted_externally_to_rlds`


*   **Description**:

Kuka iiwa peg insertion with force feedback

*   **Homepage**:
    [https://sites.google.com/view/visionandtouch](https://sites.google.com/view/visionandtouch)

*   **Source code**:
    [`tfds.robotics.rtx.StanfordKukaMultimodalDatasetConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `31.98 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
    }),
    'steps': Dataset({
        'action': Tensor(shape=(4,), dtype=float32, description=Robot action, consists of [3x EEF position, 1x gripper open/close].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'contact': Tensor(shape=(50,), dtype=float32, description=Robot contact information.),
            'depth_image': Tensor(shape=(128, 128, 1), dtype=float32, description=Main depth camera observation.),
            'ee_forces_continuous': Tensor(shape=(50, 6), dtype=float32, description=Robot end-effector forces.),
            'ee_orientation': Tensor(shape=(4,), dtype=float32, description=Robot end-effector orientation quaternion.),
            'ee_orientation_vel': Tensor(shape=(3,), dtype=float32, description=Robot end-effector orientation velocity.),
            'ee_position': Tensor(shape=(3,), dtype=float32, description=Robot end-effector position.),
            'ee_vel': Tensor(shape=(3,), dtype=float32, description=Robot end-effector velocity.),
            'ee_yaw': Tensor(shape=(4,), dtype=float32, description=Robot end-effector yaw.),
            'ee_yaw_delta': Tensor(shape=(4,), dtype=float32, description=Robot end-effector yaw delta.),
            'image': Image(shape=(128, 128, 3), dtype=uint8, description=Main camera RGB observation.),
            'joint_pos': Tensor(shape=(7,), dtype=float32, description=Robot joint positions.),
            'joint_vel': Tensor(shape=(7,), dtype=float32, description=Robot joint velocities.),
            'optical_flow': Tensor(shape=(128, 128, 2), dtype=float32, description=Optical flow.),
            'state': Tensor(shape=(8,), dtype=float32, description=Robot proprioceptive information, [7x joint pos, 1x gripper open/close].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                                | Class        | Shape         | Dtype   | Description
:------------------------------------- | :----------- | :------------ | :------ | :----------
                                       | FeaturesDict |               |         |
episode_metadata                       | FeaturesDict |               |         |
steps                                  | Dataset      |               |         |
steps/action                           | Tensor       | (4,)          | float32 | Robot action, consists of [3x EEF position, 1x gripper open/close].
steps/discount                         | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                         | Tensor       |               | bool    |
steps/is_last                          | Tensor       |               | bool    |
steps/is_terminal                      | Tensor       |               | bool    |
steps/language_embedding               | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction             | Text         |               | string  | Language Instruction.
steps/observation                      | FeaturesDict |               |         |
steps/observation/contact              | Tensor       | (50,)         | float32 | Robot contact information.
steps/observation/depth_image          | Tensor       | (128, 128, 1) | float32 | Main depth camera observation.
steps/observation/ee_forces_continuous | Tensor       | (50, 6)       | float32 | Robot end-effector forces.
steps/observation/ee_orientation       | Tensor       | (4,)          | float32 | Robot end-effector orientation quaternion.
steps/observation/ee_orientation_vel   | Tensor       | (3,)          | float32 | Robot end-effector orientation velocity.
steps/observation/ee_position          | Tensor       | (3,)          | float32 | Robot end-effector position.
steps/observation/ee_vel               | Tensor       | (3,)          | float32 | Robot end-effector velocity.
steps/observation/ee_yaw               | Tensor       | (4,)          | float32 | Robot end-effector yaw.
steps/observation/ee_yaw_delta         | Tensor       | (4,)          | float32 | Robot end-effector yaw delta.
steps/observation/image                | Image        | (128, 128, 3) | uint8   | Main camera RGB observation.
steps/observation/joint_pos            | Tensor       | (7,)          | float32 | Robot joint positions.
steps/observation/joint_vel            | Tensor       | (7,)          | float32 | Robot joint velocities.
steps/observation/optical_flow         | Tensor       | (128, 128, 2) | float32 | Optical flow.
steps/observation/state                | Tensor       | (8,)          | float32 | Robot proprioceptive information, [7x joint pos, 1x gripper open/close].
steps/reward                           | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/stanford_kuka_multimodal_dataset_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{lee2019icra,
  title={Making sense of vision and touch: Self-supervised learning of multimodal representations for contact-rich tasks},
  author={Lee, Michelle A and Zhu, Yuke and Srinivasan, Krishnan and Shah, Parth and Savarese, Silvio and Fei-Fei, Li and  Garg, Animesh and Bohg, Jeannette},
  booktitle={2019 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2019},
  url={https://arxiv.org/abs/1810.10191}
}
```

