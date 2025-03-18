<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_robocook_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka preparing dumplings with various tools&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stanford_robocook_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_robocook_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://hshi74.github.io/robocook/" />
  <meta itemprop="citation" content="@article{shi2023robocook,&#10;  title={RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools},&#10;  author={Shi, Haochen and Xu, Huazhe and Clarke, Samuel and Li, Yunzhu and Wu, Jiajun},&#10;  journal={arXiv preprint arXiv:2306.14447},&#10;  year={2023}&#10;}" />
</div>

# `stanford_robocook_converted_externally_to_rlds`


*   **Description**:

Franka preparing dumplings with various tools

*   **Homepage**:
    [https://hshi74.github.io/robocook/](https://hshi74.github.io/robocook/)

*   **Source code**:
    [`tfds.robotics.rtx.StanfordRobocookConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `124.59 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,460

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'extrinsics_1': Tensor(shape=(4, 4), dtype=float32, description=Camera 1 Extrinsic Matrix.),
        'extrinsics_2': Tensor(shape=(4, 4), dtype=float32, description=Camera 2 Extrinsic Matrix.),
        'extrinsics_3': Tensor(shape=(4, 4), dtype=float32, description=Camera 3 Extrinsic Matrix.),
        'extrinsics_4': Tensor(shape=(4, 4), dtype=float32, description=Camera 4 Extrinsic Matrix.),
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x robot end-effector velocities, 3x robot end-effector angular velocities, 1x gripper velocity].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'depth_1': Tensor(shape=(256, 256), dtype=float32, description=Camera 1 Depth observation.),
            'depth_2': Tensor(shape=(256, 256), dtype=float32, description=Camera 2 Depth observation.),
            'depth_3': Tensor(shape=(256, 256), dtype=float32, description=Camera 3 Depth observation.),
            'depth_4': Tensor(shape=(256, 256), dtype=float32, description=Camera 4 Depth observation.),
            'image_1': Image(shape=(256, 256, 3), dtype=uint8, description=Camera 1 RGB observation.),
            'image_2': Image(shape=(256, 256, 3), dtype=uint8, description=Camera 2 RGB observation.),
            'image_3': Image(shape=(256, 256, 3), dtype=uint8, description=Camera 3 RGB observation.),
            'image_4': Image(shape=(256, 256, 3), dtype=uint8, description=Camera 4 RGB observation.),
            'state': Tensor(shape=(7,), dtype=float32, description=Robot state, consists of [3x robot end-effector position, 3x robot end-effector euler angles, 1x gripper position].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape         | Dtype   | Description
:---------------------------- | :----------- | :------------ | :------ | :----------
                              | FeaturesDict |               |         |
episode_metadata              | FeaturesDict |               |         |
episode_metadata/extrinsics_1 | Tensor       | (4, 4)        | float32 | Camera 1 Extrinsic Matrix.
episode_metadata/extrinsics_2 | Tensor       | (4, 4)        | float32 | Camera 2 Extrinsic Matrix.
episode_metadata/extrinsics_3 | Tensor       | (4, 4)        | float32 | Camera 3 Extrinsic Matrix.
episode_metadata/extrinsics_4 | Tensor       | (4, 4)        | float32 | Camera 4 Extrinsic Matrix.
episode_metadata/file_path    | Text         |               | string  | Path to the original data file.
steps                         | Dataset      |               |         |
steps/action                  | Tensor       | (7,)          | float32 | Robot action, consists of [3x robot end-effector velocities, 3x robot end-effector angular velocities, 1x gripper velocity].
steps/discount                | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                | Tensor       |               | bool    |
steps/is_last                 | Tensor       |               | bool    |
steps/is_terminal             | Tensor       |               | bool    |
steps/language_embedding      | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction    | Text         |               | string  | Language Instruction.
steps/observation             | FeaturesDict |               |         |
steps/observation/depth_1     | Tensor       | (256, 256)    | float32 | Camera 1 Depth observation.
steps/observation/depth_2     | Tensor       | (256, 256)    | float32 | Camera 2 Depth observation.
steps/observation/depth_3     | Tensor       | (256, 256)    | float32 | Camera 3 Depth observation.
steps/observation/depth_4     | Tensor       | (256, 256)    | float32 | Camera 4 Depth observation.
steps/observation/image_1     | Image        | (256, 256, 3) | uint8   | Camera 1 RGB observation.
steps/observation/image_2     | Image        | (256, 256, 3) | uint8   | Camera 2 RGB observation.
steps/observation/image_3     | Image        | (256, 256, 3) | uint8   | Camera 3 RGB observation.
steps/observation/image_4     | Image        | (256, 256, 3) | uint8   | Camera 4 RGB observation.
steps/observation/state       | Tensor       | (7,)          | float32 | Robot state, consists of [3x robot end-effector position, 3x robot end-effector euler angles, 1x gripper position].
steps/reward                  | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/stanford_robocook_converted_externally_to_rlds-0.1.0.html";
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
@article{shi2023robocook,
  title={RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools},
  author={Shi, Haochen and Xu, Huazhe and Clarke, Samuel and Li, Yunzhu and Wu, Jiajun},
  journal={arXiv preprint arXiv:2306.14447},
  year={2023}
}
```

