<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="taco_play" />
  <meta itemprop="description" content="Franka arm interacting with kitchen&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;taco_play&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/taco_play" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/datasets/oiermees/taco-robot" />
  <meta itemprop="citation" content="@inproceedings{rosete2022tacorl,&#10;author = {Erick Rosete-Beas and Oier Mees and Gabriel Kalweit and Joschka Boedecker and Wolfram Burgard},&#10;title = {Latent Plans for Task Agnostic Offline Reinforcement Learning},&#10;journal = {Proceedings of the 6th Conference on Robot Learning (CoRL)},&#10;year = {2022}&#10;}&#10;@inproceedings{mees23hulc2,&#10;title={Grounding  Language  with  Visual  Affordances  over  Unstructured  Data},&#10;author={Oier Mees and Jessica Borja-Diaz and Wolfram Burgard},&#10;booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},&#10;year={2023},&#10;address = {London, UK}&#10;}" />
</div>

# `taco_play`


*   **Description**:

Franka arm interacting with kitchen

*   **Homepage**:
    [https://www.kaggle.com/datasets/oiermees/taco-robot](https://www.kaggle.com/datasets/oiermees/taco-robot)

*   **Source code**:
    [`tfds.robotics.rtx.TacoPlay`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `47.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 361
`'train'` | 3,242

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'actions': Tensor(shape=(7,), dtype=float32, description=absolute desired values for gripper pose (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)),
            'rel_actions_gripper': Tensor(shape=(7,), dtype=float32, description=relative actions for gripper pose in the gripper camera frame (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)),
            'rel_actions_world': Tensor(shape=(7,), dtype=float32, description=relative actions for gripper pose in the robot base frame (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)),
            'terminate_episode': float32,
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'depth_gripper': Tensor(shape=(84, 84), dtype=float32),
            'depth_static': Tensor(shape=(150, 200), dtype=float32),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'rgb_gripper': Image(shape=(84, 84, 3), dtype=uint8),
            'rgb_static': Image(shape=(150, 200, 3), dtype=uint8, description=RGB static image of shape. (150, 200, 3). Subsampled from (200,200, 3) image.),
            'robot_obs': Tensor(shape=(15,), dtype=float32, description=EE position (3), EE orientation in euler angles (3), gripper width (1), joint positions (7), gripper action (1)),
            'structured_language_instruction': string,
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
steps/action/actions                              | Tensor       | (7,)          | float32 | absolute desired values for gripper pose (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)
steps/action/rel_actions_gripper                  | Tensor       | (7,)          | float32 | relative actions for gripper pose in the gripper camera frame (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)
steps/action/rel_actions_world                    | Tensor       | (7,)          | float32 | relative actions for gripper pose in the robot base frame (first 6 dimensions are x, y, z, yaw, pitch, roll), last dimension is open_gripper (-1 is open gripper, 1 is close)
steps/action/terminate_episode                    | Tensor       |               | float32 |
steps/is_first                                    | Tensor       |               | bool    |
steps/is_last                                     | Tensor       |               | bool    |
steps/is_terminal                                 | Tensor       |               | bool    |
steps/observation                                 | FeaturesDict |               |         |
steps/observation/depth_gripper                   | Tensor       | (84, 84)      | float32 |
steps/observation/depth_static                    | Tensor       | (150, 200)    | float32 |
steps/observation/natural_language_embedding      | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction    | Tensor       |               | string  | Natural language instruction is a natural language instruction randomly sampled based on potential task synonyms derived from the structured language task. For example, 'turn blue light off' may map to 'switch the blue color light to off'.
steps/observation/rgb_gripper                     | Image        | (84, 84, 3)   | uint8   |
steps/observation/rgb_static                      | Image        | (150, 200, 3) | uint8   | RGB static image of shape. (150, 200, 3). Subsampled from (200,200, 3) image.
steps/observation/robot_obs                       | Tensor       | (15,)         | float32 | EE position (3), EE orientation in euler angles (3), gripper width (1), joint positions (7), gripper action (1)
steps/observation/structured_language_instruction | Tensor       |               | string  | One of 25 possible structured language instructions, see list in https://arxiv.org/pdf/2210.01911.pdf Table 2.
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/taco_play-0.1.0.html";
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
@inproceedings{rosete2022tacorl,
author = {Erick Rosete-Beas and Oier Mees and Gabriel Kalweit and Joschka Boedecker and Wolfram Burgard},
title = {Latent Plans for Task Agnostic Offline Reinforcement Learning},
journal = {Proceedings of the 6th Conference on Robot Learning (CoRL)},
year = {2022}
}
@inproceedings{mees23hulc2,
title={Grounding  Language  with  Visual  Affordances  over  Unstructured  Data},
author={Oier Mees and Jessica Borja-Diaz and Wolfram Burgard},
booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
year={2023},
address = {London, UK}
}
```

