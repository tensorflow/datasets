<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="columbia_cairlab_pusht_real" />
  <meta itemprop="description" content="UR5 planar pushing tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;columbia_cairlab_pusht_real&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/columbia_cairlab_pusht_real" />
  <meta itemprop="sameAs" content="https://github.com/columbia-ai-robotics/diffusion_policy" />
  <meta itemprop="citation" content="@inproceedings{chi2023diffusionpolicy,&#10;    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},&#10; author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},&#10;   booktitle={Proceedings of Robotics: Science and Systems (RSS)},&#10;    year={2023}&#10;}" />
</div>

# `columbia_cairlab_pusht_real`


*   **Description**:

UR5 planar pushing tasks

*   **Homepage**:
    [https://github.com/columbia-ai-robotics/diffusion_policy](https://github.com/columbia-ai-robotics/diffusion_policy)

*   **Source code**:
    [`tfds.robotics.rtx.ColumbiaCairlabPushtReal`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `2.80 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 14
`'train'` | 122

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'gripper_closedness_action': float32,
            'rotation_delta': Tensor(shape=(3,), dtype=float32, description=Delta change in roll, pitch, yaw.),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32, description=Delta change in XYZ.),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'image': Image(shape=(240, 320, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'robot_state': Tensor(shape=(2,), dtype=float32, description=Robot end effector XY state),
            'wrist_image': Image(shape=(240, 320, 3), dtype=uint8),
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
steps/action/gripper_closedness_action         | Tensor       |               | float32 | 1 if close gripper, -1 if open gripper, 0 if no change.
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 | Delta change in roll, pitch, yaw.
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 | Delta change in XYZ.
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/image                        | Image        | (240, 320, 3) | uint8   |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
steps/observation/robot_state                  | Tensor       | (2,)          | float32 | Robot end effector XY state
steps/observation/wrist_image                  | Image        | (240, 320, 3) | uint8   |
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/columbia_cairlab_pusht_real-0.1.0.html";
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
@inproceedings{chi2023diffusionpolicy,
    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
    author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
    booktitle={Proceedings of Robotics: Science and Systems (RSS)},
    year={2023}
}
```

