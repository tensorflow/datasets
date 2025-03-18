<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="maniskill_dataset_converted_externally_to_rlds" />
  <meta itemprop="description" content="Simulated Franka performing various manipulation tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;maniskill_dataset_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/maniskill_dataset_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://github.com/haosulab/ManiSkill2" />
  <meta itemprop="citation" content="@inproceedings{gu2023maniskill2,&#10;  title={ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills},&#10;  author={Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and Yuan, Xiaodi and Xie, Pengwei and Huang, Zhiao and Chen, Rui and Su, Hao},&#10;  booktitle={International Conference on Learning Representations},&#10;  year={2023}&#10;}" />
</div>

# `maniskill_dataset_converted_externally_to_rlds`


*   **Description**:

Simulated Franka performing various manipulation tasks

*   **Homepage**:
    [https://github.com/haosulab/ManiSkill2](https://github.com/haosulab/ManiSkill2)

*   **Source code**:
    [`tfds.robotics.rtx.ManiskillDatasetConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `151.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,213

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'episode_id': Text(shape=(), dtype=string),
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x end effector delta target position, 3x end effector delta target orientation in axis-angle format, 1x gripper target position (mimic for two fingers)]. For delta target position, an action of -1 maps to a robot movement of -0.1m, and action of 1 maps to a movement of 0.1m. For delta target orientation, its encoded angle is mapped to a range of [-0.1rad, 0.1rad] for robot execution. For example, an action of [1, 0, 0] means rotating along the x-axis by 0.1 rad. For gripper target position, an action of -1 means close, and an action of 1 means open.),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'base_pose': Tensor(shape=(7,), dtype=float32, description=Robot base pose in the world frame, consists of [x, y, z, qw, qx, qy, qz]. The first three dimensions represent xyz positions in meters. The last four dimensions are the quaternion representation of rotation.),
            'depth': Image(shape=(256, 256, 1), dtype=uint16, description=Main camera Depth observation. Divide the depth value by 2**10 to get the depth in meters.),
            'image': Image(shape=(256, 256, 3), dtype=uint8, description=Main camera RGB observation.),
            'main_camera_cam2world_gl': Tensor(shape=(4, 4), dtype=float32, description=Transformation from the main camera frame to the world frame in OpenGL/Blender convention.),
            'main_camera_extrinsic_cv': Tensor(shape=(4, 4), dtype=float32, description=Main camera extrinsic matrix in OpenCV convention.),
            'main_camera_intrinsic_cv': Tensor(shape=(3, 3), dtype=float32, description=Main camera intrinsic matrix in OpenCV convention.),
            'state': Tensor(shape=(18,), dtype=float32, description=Robot state, consists of [7x robot joint angles, 2x gripper position, 7x robot joint angle velocity, 2x gripper velocity]. Angle in radians, position in meters.),
            'target_object_or_part_final_pose': Tensor(shape=(7,), dtype=float32, description=The final pose towards which the target object or object part needs be manipulated, consists of [x, y, z, qw, qx, qy, qz]. The pose is represented in the world frame. An episode is considered successful if the target object or object part is manipulated to this pose.),
            'target_object_or_part_final_pose_valid': Tensor(shape=(7,), dtype=uint8, description=Whether each dimension of target_object_or_part_final_pose is valid in an environment. 1 = valid; 0 = invalid (in which case one should ignore the corresponding dimensions in target_object_or_part_final_pose). "Invalid" means that there is no success check on the final pose of target object or object part in the corresponding dimensions.),
            'target_object_or_part_initial_pose': Tensor(shape=(7,), dtype=float32, description=The initial pose of the target object or object part to be manipulated, consists of [x, y, z, qw, qx, qy, qz]. The pose is represented in the world frame. This variable is used to specify the target object or object part when multiple objects or object parts are present in an environment),
            'target_object_or_part_initial_pose_valid': Tensor(shape=(7,), dtype=uint8, description=Whether each dimension of target_object_or_part_initial_pose is valid in an environment. 1 = valid; 0 = invalid (in which case one should ignore the corresponding dimensions in target_object_or_part_initial_pose).),
            'tcp_pose': Tensor(shape=(7,), dtype=float32, description=Robot tool-center-point pose in the world frame, consists of [x, y, z, qw, qx, qy, qz]. Tool-center-point is the center between the two gripper fingers.),
            'wrist_camera_cam2world_gl': Tensor(shape=(4, 4), dtype=float32, description=Transformation from the wrist camera frame to the world frame in OpenGL/Blender convention.),
            'wrist_camera_extrinsic_cv': Tensor(shape=(4, 4), dtype=float32, description=Wrist camera extrinsic matrix in OpenCV convention.),
            'wrist_camera_intrinsic_cv': Tensor(shape=(3, 3), dtype=float32, description=Wrist camera intrinsic matrix in OpenCV convention.),
            'wrist_depth': Image(shape=(256, 256, 1), dtype=uint16, description=Wrist camera Depth observation. Divide the depth value by 2**10 to get the depth in meters.),
            'wrist_image': Image(shape=(256, 256, 3), dtype=uint8, description=Wrist camera RGB observation.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                                                    | Class        | Shape         | Dtype   | Description
:--------------------------------------------------------- | :----------- | :------------ | :------ | :----------
                                                           | FeaturesDict |               |         |
episode_metadata                                           | FeaturesDict |               |         |
episode_metadata/episode_id                                | Text         |               | string  | Episode ID.
episode_metadata/file_path                                 | Text         |               | string  | Path to the original data file.
steps                                                      | Dataset      |               |         |
steps/action                                               | Tensor       | (7,)          | float32 | Robot action, consists of [3x end effector delta target position, 3x end effector delta target orientation in axis-angle format, 1x gripper target position (mimic for two fingers)]. For delta target position, an action of -1 maps to a robot movement of -0.1m, and action of 1 maps to a movement of 0.1m. For delta target orientation, its encoded angle is mapped to a range of [-0.1rad, 0.1rad] for robot execution. For example, an action of [1, 0, 0] means rotating along the x-axis by 0.1 rad. For gripper target position, an action of -1 means close, and an action of 1 means open.
steps/discount                                             | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                                             | Tensor       |               | bool    |
steps/is_last                                              | Tensor       |               | bool    |
steps/is_terminal                                          | Tensor       |               | bool    |
steps/language_embedding                                   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction                                 | Text         |               | string  | Language Instruction.
steps/observation                                          | FeaturesDict |               |         |
steps/observation/base_pose                                | Tensor       | (7,)          | float32 | Robot base pose in the world frame, consists of [x, y, z, qw, qx, qy, qz]. The first three dimensions represent xyz positions in meters. The last four dimensions are the quaternion representation of rotation.
steps/observation/depth                                    | Image        | (256, 256, 1) | uint16  | Main camera Depth observation. Divide the depth value by 2**10 to get the depth in meters.
steps/observation/image                                    | Image        | (256, 256, 3) | uint8   | Main camera RGB observation.
steps/observation/main_camera_cam2world_gl                 | Tensor       | (4, 4)        | float32 | Transformation from the main camera frame to the world frame in OpenGL/Blender convention.
steps/observation/main_camera_extrinsic_cv                 | Tensor       | (4, 4)        | float32 | Main camera extrinsic matrix in OpenCV convention.
steps/observation/main_camera_intrinsic_cv                 | Tensor       | (3, 3)        | float32 | Main camera intrinsic matrix in OpenCV convention.
steps/observation/state                                    | Tensor       | (18,)         | float32 | Robot state, consists of [7x robot joint angles, 2x gripper position, 7x robot joint angle velocity, 2x gripper velocity]. Angle in radians, position in meters.
steps/observation/target_object_or_part_final_pose         | Tensor       | (7,)          | float32 | The final pose towards which the target object or object part needs be manipulated, consists of [x, y, z, qw, qx, qy, qz]. The pose is represented in the world frame. An episode is considered successful if the target object or object part is manipulated to this pose.
steps/observation/target_object_or_part_final_pose_valid   | Tensor       | (7,)          | uint8   | Whether each dimension of target_object_or_part_final_pose is valid in an environment. 1 = valid; 0 = invalid (in which case one should ignore the corresponding dimensions in target_object_or_part_final_pose). "Invalid" means that there is no success check on the final pose of target object or object part in the corresponding dimensions.
steps/observation/target_object_or_part_initial_pose       | Tensor       | (7,)          | float32 | The initial pose of the target object or object part to be manipulated, consists of [x, y, z, qw, qx, qy, qz]. The pose is represented in the world frame. This variable is used to specify the target object or object part when multiple objects or object parts are present in an environment
steps/observation/target_object_or_part_initial_pose_valid | Tensor       | (7,)          | uint8   | Whether each dimension of target_object_or_part_initial_pose is valid in an environment. 1 = valid; 0 = invalid (in which case one should ignore the corresponding dimensions in target_object_or_part_initial_pose).
steps/observation/tcp_pose                                 | Tensor       | (7,)          | float32 | Robot tool-center-point pose in the world frame, consists of [x, y, z, qw, qx, qy, qz]. Tool-center-point is the center between the two gripper fingers.
steps/observation/wrist_camera_cam2world_gl                | Tensor       | (4, 4)        | float32 | Transformation from the wrist camera frame to the world frame in OpenGL/Blender convention.
steps/observation/wrist_camera_extrinsic_cv                | Tensor       | (4, 4)        | float32 | Wrist camera extrinsic matrix in OpenCV convention.
steps/observation/wrist_camera_intrinsic_cv                | Tensor       | (3, 3)        | float32 | Wrist camera intrinsic matrix in OpenCV convention.
steps/observation/wrist_depth                              | Image        | (256, 256, 1) | uint16  | Wrist camera Depth observation. Divide the depth value by 2**10 to get the depth in meters.
steps/observation/wrist_image                              | Image        | (256, 256, 3) | uint8   | Wrist camera RGB observation.
steps/reward                                               | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/maniskill_dataset_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{gu2023maniskill2,
  title={ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills},
  author={Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and Yuan, Xiaodi and Xie, Pengwei and Huang, Zhiao and Chen, Rui and Su, Hao},
  booktitle={International Conference on Learning Representations},
  year={2023}
}
```

