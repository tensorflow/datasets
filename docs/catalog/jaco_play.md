<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="jaco_play" />
  <meta itemprop="description" content="Jaco 2 pick place on table top&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;jaco_play&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/jaco_play" />
  <meta itemprop="sameAs" content="https://github.com/clvrai/clvr_jaco_play_dataset" />
  <meta itemprop="citation" content="@software{dass2023jacoplay,&#10;  author = {Dass, Shivin and Yapeter, Jullian and Zhang, Jesse and Zhang, Jiahui&#10;            and Pertsch, Karl and Nikolaidis, Stefanos and Lim, Joseph J.},&#10;  title = {CLVR Jaco Play Dataset},&#10;  url = {https://github.com/clvrai/clvr_jaco_play_dataset},&#10;  version = {1.0.0},&#10;  year = {2023}&#10;}" />
</div>

# `jaco_play`


*   **Description**:

Jaco 2 pick place on table top

*   **Homepage**:
    [https://github.com/clvrai/clvr_jaco_play_dataset](https://github.com/clvrai/clvr_jaco_play_dataset)

*   **Source code**:
    [`tfds.robotics.rtx.JacoPlay`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `9.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 109
`'train'` | 976

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'gripper_closedness_action': Tensor(shape=(1,), dtype=float32),
            'terminate_episode': Tensor(shape=(3,), dtype=int32),
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'end_effector_cartesian_pos': Tensor(shape=(7,), dtype=float32),
            'end_effector_cartesian_velocity': Tensor(shape=(6,), dtype=float32),
            'image': Image(shape=(224, 224, 3), dtype=uint8),
            'image_wrist': Image(shape=(224, 224, 3), dtype=uint8),
            'joint_pos': Tensor(shape=(8,), dtype=float32),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                           | Class        | Shape         | Dtype   | Description
:------------------------------------------------ | :----------- | :------------ | :------ | :----------
                                                  | FeaturesDict |               |         |
steps                                             | Dataset      |               |         |
steps/action                                      | FeaturesDict |               |         |
steps/action/gripper_closedness_action            | Tensor       | (1,)          | float32 |
steps/action/terminate_episode                    | Tensor       | (3,)          | int32   |
steps/action/world_vector                         | Tensor       | (3,)          | float32 |
steps/is_first                                    | Tensor       |               | bool    |
steps/is_last                                     | Tensor       |               | bool    |
steps/is_terminal                                 | Tensor       |               | bool    |
steps/observation                                 | FeaturesDict |               |         |
steps/observation/end_effector_cartesian_pos      | Tensor       | (7,)          | float32 |
steps/observation/end_effector_cartesian_velocity | Tensor       | (6,)          | float32 |
steps/observation/image                           | Image        | (224, 224, 3) | uint8   |
steps/observation/image_wrist                     | Image        | (224, 224, 3) | uint8   |
steps/observation/joint_pos                       | Tensor       | (8,)          | float32 |
steps/observation/natural_language_embedding      | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction    | Tensor       |               | string  |
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/jaco_play-0.1.0.html";
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
@software{dass2023jacoplay,
  author = {Dass, Shivin and Yapeter, Jullian and Zhang, Jesse and Zhang, Jiahui
            and Pertsch, Karl and Nikolaidis, Stefanos and Lim, Joseph J.},
  title = {CLVR Jaco Play Dataset},
  url = {https://github.com/clvrai/clvr_jaco_play_dataset},
  version = {1.0.0},
  year = {2023}
}
```

