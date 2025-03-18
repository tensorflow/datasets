<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="berkeley_autolab_ur5" />
  <meta itemprop="description" content="UR5 performing cloth manipulation, pick place etc tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;berkeley_autolab_ur5&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/berkeley_autolab_ur5" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/berkeley-ur5/home" />
  <meta itemprop="citation" content="@misc{BerkeleyUR5Website,&#10;  title = {Berkeley {UR5} Demonstration Dataset},&#10;  author = {Lawrence Yunliang Chen and Simeon Adebola and Ken Goldberg},&#10;  howpublished = {https://sites.google.com/view/berkeley-ur5/home},&#10;}" />
</div>

# `berkeley_autolab_ur5`


*   **Description**:

UR5 performing cloth manipulation, pick place etc tasks

*   **Homepage**:
    [https://sites.google.com/view/berkeley-ur5/home](https://sites.google.com/view/berkeley-ur5/home)

*   **Source code**:
    [`tfds.robotics.rtx.BerkeleyAutolabUr5`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `76.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 104
`'train'` | 896

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
            'hand_image': Image(shape=(480, 640, 3), dtype=uint8),
            'image': Image(shape=(480, 640, 3), dtype=uint8),
            'image_with_depth': Image(shape=(480, 640, 1), dtype=float32),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'robot_state': Tensor(shape=(15,), dtype=float32, description=Explanation of the robot state can be found at https://sites.google.com/corp/view/berkeley-ur5),
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
steps/observation/hand_image                   | Image        | (480, 640, 3) | uint8   |
steps/observation/image                        | Image        | (480, 640, 3) | uint8   |
steps/observation/image_with_depth             | Image        | (480, 640, 1) | float32 |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
steps/observation/robot_state                  | Tensor       | (15,)         | float32 | Explanation of the robot state can be found at https://sites.google.com/corp/view/berkeley-ur5
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/berkeley_autolab_ur5-0.1.0.html";
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
@misc{BerkeleyUR5Website,
  title = {Berkeley {UR5} Demonstration Dataset},
  author = {Lawrence Yunliang Chen and Simeon Adebola and Ken Goldberg},
  howpublished = {https://sites.google.com/view/berkeley-ur5/home},
}
```

