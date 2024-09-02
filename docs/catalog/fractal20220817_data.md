<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="fractal20220817_data" />
  <meta itemprop="description" content="Table-top manipulation with 17 objects&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;fractal20220817_data&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/fractal20220817_data" />
  <meta itemprop="sameAs" content="https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html" />
  <meta itemprop="citation" content="@article{brohan2022rt,&#10;  title={Rt-1: Robotics transformer for real-world control at scale},&#10;  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alex and Hsu, Jasmine and others},&#10;  journal={arXiv preprint arXiv:2212.06817},&#10;  year={2022}&#10;}" />
</div>

# `fractal20220817_data`


*   **Description**:

Table-top manipulation with 17 objects

*   **Homepage**:
    [https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html](https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html)

*   **Source code**:
    [`tfds.robotics.rtx.Fractal20220817Data`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `111.38 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 87,212

*   **Feature structure**:

```python
FeaturesDict({
    'aspects': FeaturesDict({
        'already_success': bool,
        'feasible': bool,
        'has_aspects': bool,
        'success': bool,
        'undesirable': bool,
    }),
    'attributes': FeaturesDict({
        'collection_mode': int64,
        'collection_mode_name': string,
        'data_type': int64,
        'data_type_name': string,
        'env': int64,
        'env_name': string,
        'location': int64,
        'location_name': string,
        'objects_family': int64,
        'objects_family_name': string,
        'task_family': int64,
        'task_family_name': string,
    }),
    'steps': Dataset({
        'action': FeaturesDict({
            'base_displacement_vector': Tensor(shape=(2,), dtype=float32),
            'base_displacement_vertical_rotation': Tensor(shape=(1,), dtype=float32),
            'gripper_closedness_action': Tensor(shape=(1,), dtype=float32, description=continuous gripper position),
            'rotation_delta': Tensor(shape=(3,), dtype=float32, description=rpy commanded orientation displacement, in base-relative frame),
            'terminate_episode': Tensor(shape=(3,), dtype=int32),
            'world_vector': Tensor(shape=(3,), dtype=float32, description=commanded end-effector displacement, in base-relative frame),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'base_pose_tool_reached': Tensor(shape=(7,), dtype=float32, description=end-effector base-relative position+quaternion pose),
            'gripper_closed': Tensor(shape=(1,), dtype=float32),
            'gripper_closedness_commanded': Tensor(shape=(1,), dtype=float32, description=continuous gripper position),
            'height_to_bottom': Tensor(shape=(1,), dtype=float32, description=height of end-effector from ground),
            'image': Image(shape=(256, 320, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'orientation_box': Tensor(shape=(2, 3), dtype=float32),
            'orientation_start': Tensor(shape=(4,), dtype=float32),
            'robot_orientation_positions_box': Tensor(shape=(3, 3), dtype=float32),
            'rotation_delta_to_go': Tensor(shape=(3,), dtype=float32, description=rotational displacement from current orientation to target),
            'src_rotation': Tensor(shape=(4,), dtype=float32),
            'vector_to_go': Tensor(shape=(3,), dtype=float32, description=displacement from current end-effector position to target),
            'workspace_bounds': Tensor(shape=(3, 3), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                           | Class        | Shape         | Dtype   | Description
:------------------------------------------------ | :----------- | :------------ | :------ | :----------
                                                  | FeaturesDict |               |         |
aspects                                           | FeaturesDict |               |         | Session Aspects for crowdcompute ratings
aspects/already_success                           | Tensor       |               | bool    |
aspects/feasible                                  | Tensor       |               | bool    |
aspects/has_aspects                               | Tensor       |               | bool    |
aspects/success                                   | Tensor       |               | bool    |
aspects/undesirable                               | Tensor       |               | bool    |
attributes                                        | FeaturesDict |               |         |
attributes/collection_mode                        | Tensor       |               | int64   |
attributes/collection_mode_name                   | Tensor       |               | string  |
attributes/data_type                              | Tensor       |               | int64   |
attributes/data_type_name                         | Tensor       |               | string  |
attributes/env                                    | Tensor       |               | int64   |
attributes/env_name                               | Tensor       |               | string  |
attributes/location                               | Tensor       |               | int64   |
attributes/location_name                          | Tensor       |               | string  |
attributes/objects_family                         | Tensor       |               | int64   |
attributes/objects_family_name                    | Tensor       |               | string  |
attributes/task_family                            | Tensor       |               | int64   |
attributes/task_family_name                       | Tensor       |               | string  |
steps                                             | Dataset      |               |         |
steps/action                                      | FeaturesDict |               |         |
steps/action/base_displacement_vector             | Tensor       | (2,)          | float32 |
steps/action/base_displacement_vertical_rotation  | Tensor       | (1,)          | float32 |
steps/action/gripper_closedness_action            | Tensor       | (1,)          | float32 | continuous gripper position
steps/action/rotation_delta                       | Tensor       | (3,)          | float32 | rpy commanded orientation displacement, in base-relative frame
steps/action/terminate_episode                    | Tensor       | (3,)          | int32   |
steps/action/world_vector                         | Tensor       | (3,)          | float32 | commanded end-effector displacement, in base-relative frame
steps/is_first                                    | Tensor       |               | bool    |
steps/is_last                                     | Tensor       |               | bool    |
steps/is_terminal                                 | Tensor       |               | bool    |
steps/observation                                 | FeaturesDict |               |         |
steps/observation/base_pose_tool_reached          | Tensor       | (7,)          | float32 | end-effector base-relative position+quaternion pose
steps/observation/gripper_closed                  | Tensor       | (1,)          | float32 |
steps/observation/gripper_closedness_commanded    | Tensor       | (1,)          | float32 | continuous gripper position
steps/observation/height_to_bottom                | Tensor       | (1,)          | float32 | height of end-effector from ground
steps/observation/image                           | Image        | (256, 320, 3) | uint8   |
steps/observation/natural_language_embedding      | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction    | Tensor       |               | string  |
steps/observation/orientation_box                 | Tensor       | (2, 3)        | float32 |
steps/observation/orientation_start               | Tensor       | (4,)          | float32 |
steps/observation/robot_orientation_positions_box | Tensor       | (3, 3)        | float32 |
steps/observation/rotation_delta_to_go            | Tensor       | (3,)          | float32 | rotational displacement from current orientation to target
steps/observation/src_rotation                    | Tensor       | (4,)          | float32 |
steps/observation/vector_to_go                    | Tensor       | (3,)          | float32 | displacement from current end-effector position to target
steps/observation/workspace_bounds                | Tensor       | (3, 3)        | float32 |
steps/reward                                      | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/fractal20220817_data-0.1.0.html";
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
@article{brohan2022rt,
  title={Rt-1: Robotics transformer for real-world control at scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alex and Hsu, Jasmine and others},
  journal={arXiv preprint arXiv:2212.06817},
  year={2022}
}
```

