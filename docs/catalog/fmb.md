<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="fmb" />
  <meta itemprop="description" content="Our dataset consists of objects in diverse appearance and geometry. It requires multi-stage and multi-modal fine motor skills to successfully assemble the pegs onto a unfixed board in a randomized scene. We collected a total of 22,550 trajectories across two different tasks on a Franka Panda arm. We record the trajectories from 2 global views and 2 wrist views. Each view contains both RGB and depth map.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;fmb&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/fmb" />
  <meta itemprop="sameAs" content="https://functional-manipulation-benchmark.github.io/" />
  <meta itemprop="citation" content="https://doi.org/10.48550/arXiv.2401.08553" />
</div>

# `fmb`


*   **Description**:

Our dataset consists of objects in diverse appearance and geometry. It requires
multi-stage and multi-modal fine motor skills to successfully assemble the pegs
onto a unfixed board in a randomized scene. We collected a total of 22,550
trajectories across two different tasks on a Franka Panda arm. We record the
trajectories from 2 global views and 2 wrist views. Each view contains both RGB
and depth map.

*   **Homepage**:
    [https://functional-manipulation-benchmark.github.io/](https://functional-manipulation-benchmark.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.Fmb`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `356.63 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,804

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'episode_language_embedding': Tensor(shape=(512,), dtype=float32),
        'episode_language_instruction': string,
        'episode_task': string,
        'file_path': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': string,
        'observation': FeaturesDict({
            'color_id': Scalar(shape=(), dtype=uint8),
            'eef_force': Tensor(shape=(3,), dtype=float32),
            'eef_pose': Tensor(shape=(7,), dtype=float32),
            'eef_torque': Tensor(shape=(3,), dtype=float32),
            'eef_vel': Tensor(shape=(6,), dtype=float32),
            'image_side_1': Image(shape=(256, 256, 3), dtype=uint8),
            'image_side_1_depth': Tensor(shape=(256, 256), dtype=float32),
            'image_side_2': Image(shape=(256, 256, 3), dtype=uint8),
            'image_side_2_depth': Tensor(shape=(256, 256), dtype=float32),
            'image_wrist_1': Image(shape=(256, 256, 3), dtype=uint8),
            'image_wrist_1_depth': Tensor(shape=(256, 256), dtype=float32),
            'image_wrist_2': Image(shape=(256, 256, 3), dtype=uint8),
            'image_wrist_2_depth': Tensor(shape=(256, 256), dtype=float32),
            'joint_pos': Tensor(shape=(7,), dtype=float32),
            'joint_vel': Tensor(shape=(7,), dtype=float32),
            'length': string,
            'object_id': Scalar(shape=(), dtype=uint8),
            'primitive': string,
            'shape_id': Scalar(shape=(), dtype=uint8),
            'size': string,
            'state_gripper_pose': Scalar(shape=(), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                       | Class        | Shape         | Dtype   | Description
:-------------------------------------------- | :----------- | :------------ | :------ | :----------
                                              | FeaturesDict |               |         |
episode_metadata                              | FeaturesDict |               |         |
episode_metadata/episode_language_embedding   | Tensor       | (512,)        | float32 |
episode_metadata/episode_language_instruction | Tensor       |               | string  |
episode_metadata/episode_task                 | Tensor       |               | string  |
episode_metadata/file_path                    | Tensor       |               | string  |
steps                                         | Dataset      |               |         |
steps/action                                  | Tensor       | (7,)          | float32 |
steps/discount                                | Scalar       |               | float32 |
steps/is_first                                | Tensor       |               | bool    |
steps/is_last                                 | Tensor       |               | bool    |
steps/is_terminal                             | Tensor       |               | bool    |
steps/language_embedding                      | Tensor       | (512,)        | float32 |
steps/language_instruction                    | Tensor       |               | string  |
steps/observation                             | FeaturesDict |               |         |
steps/observation/color_id                    | Scalar       |               | uint8   |
steps/observation/eef_force                   | Tensor       | (3,)          | float32 |
steps/observation/eef_pose                    | Tensor       | (7,)          | float32 |
steps/observation/eef_torque                  | Tensor       | (3,)          | float32 |
steps/observation/eef_vel                     | Tensor       | (6,)          | float32 |
steps/observation/image_side_1                | Image        | (256, 256, 3) | uint8   |
steps/observation/image_side_1_depth          | Tensor       | (256, 256)    | float32 |
steps/observation/image_side_2                | Image        | (256, 256, 3) | uint8   |
steps/observation/image_side_2_depth          | Tensor       | (256, 256)    | float32 |
steps/observation/image_wrist_1               | Image        | (256, 256, 3) | uint8   |
steps/observation/image_wrist_1_depth         | Tensor       | (256, 256)    | float32 |
steps/observation/image_wrist_2               | Image        | (256, 256, 3) | uint8   |
steps/observation/image_wrist_2_depth         | Tensor       | (256, 256)    | float32 |
steps/observation/joint_pos                   | Tensor       | (7,)          | float32 |
steps/observation/joint_vel                   | Tensor       | (7,)          | float32 |
steps/observation/length                      | Tensor       |               | string  |
steps/observation/object_id                   | Scalar       |               | uint8   |
steps/observation/primitive                   | Tensor       |               | string  |
steps/observation/shape_id                    | Scalar       |               | uint8   |
steps/observation/size                        | Tensor       |               | string  |
steps/observation/state_gripper_pose          | Scalar       |               | float32 |
steps/reward                                  | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/fmb-0.1.0.html";
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
https://doi.org/10.48550/arXiv.2401.08553
```

