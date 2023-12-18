<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kuka" />
  <meta itemprop="description" content="Bin picking and rearrangement tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;kuka&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kuka" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/1806.10293" />
  <meta itemprop="citation" content="@article{kalashnikov2018qt,&#10;  title={Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation},&#10;  author={Kalashnikov, Dmitry and Irpan, Alex and Pastor, Peter and Ibarz, Julian and Herzog, Alexander and Jang, Eric and Quillen, Deirdre and Holly, Ethan and Kalakrishnan, Mrinal and Vanhoucke, Vincent and others},&#10;  journal={arXiv preprint arXiv:1806.10293},&#10;  year={2018}&#10;}" />
</div>

# `kuka`


*   **Description**:

Bin picking and rearrangement tasks

*   **Homepage**:
    [https://arxiv.org/abs/1806.10293](https://arxiv.org/abs/1806.10293)

*   **Source code**:
    [`tfds.robotics.rtx.Kuka`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `779.81 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 580,392

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'base_displacement_vector': Tensor(shape=(2,), dtype=float32),
            'base_displacement_vertical_rotation': Tensor(shape=(1,), dtype=float32),
            'gripper_closedness_action': Tensor(shape=(1,), dtype=float32),
            'rotation_delta': Tensor(shape=(3,), dtype=float32),
            'terminate_episode': Tensor(shape=(3,), dtype=int32),
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'clip_function_input/base_pose_tool_reached': Tensor(shape=(7,), dtype=float32),
            'clip_function_input/workspace_bounds': Tensor(shape=(3, 3), dtype=float32),
            'gripper_closed': Tensor(shape=(1,), dtype=float32),
            'height_to_bottom': Tensor(shape=(1,), dtype=float32),
            'image': Image(shape=(512, 640, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'task_id': Tensor(shape=(1,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
    'success': bool,
})
```

*   **Feature documentation**:

Feature                                                      | Class        | Shape         | Dtype   | Description
:----------------------------------------------------------- | :----------- | :------------ | :------ | :----------
                                                             | FeaturesDict |               |         |
steps                                                        | Dataset      |               |         |
steps/action                                                 | FeaturesDict |               |         |
steps/action/base_displacement_vector                        | Tensor       | (2,)          | float32 |
steps/action/base_displacement_vertical_rotation             | Tensor       | (1,)          | float32 |
steps/action/gripper_closedness_action                       | Tensor       | (1,)          | float32 |
steps/action/rotation_delta                                  | Tensor       | (3,)          | float32 |
steps/action/terminate_episode                               | Tensor       | (3,)          | int32   |
steps/action/world_vector                                    | Tensor       | (3,)          | float32 |
steps/is_first                                               | Tensor       |               | bool    |
steps/is_last                                                | Tensor       |               | bool    |
steps/is_terminal                                            | Tensor       |               | bool    |
steps/observation                                            | FeaturesDict |               |         |
steps/observation/clip_function_input/base_pose_tool_reached | Tensor       | (7,)          | float32 |
steps/observation/clip_function_input/workspace_bounds       | Tensor       | (3, 3)        | float32 |
steps/observation/gripper_closed                             | Tensor       | (1,)          | float32 |
steps/observation/height_to_bottom                           | Tensor       | (1,)          | float32 |
steps/observation/image                                      | Image        | (512, 640, 3) | uint8   |
steps/observation/natural_language_embedding                 | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction               | Tensor       |               | string  |
steps/observation/task_id                                    | Tensor       | (1,)          | float32 |
steps/reward                                                 | Scalar       |               | float32 |
success                                                      | Tensor       |               | bool    |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/kuka-0.1.0.html";
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
@article{kalashnikov2018qt,
  title={Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation},
  author={Kalashnikov, Dmitry and Irpan, Alex and Pastor, Peter and Ibarz, Julian and Herzog, Alexander and Jang, Eric and Quillen, Deirdre and Holly, Ethan and Kalakrishnan, Mrinal and Vanhoucke, Vincent and others},
  journal={arXiv preprint arXiv:1806.10293},
  year={2018}
}
```

