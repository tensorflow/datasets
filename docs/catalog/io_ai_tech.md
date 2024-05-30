<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="io_ai_tech" />
  <meta itemprop="description" content="&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;io_ai_tech&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/io_ai_tech" />
  <meta itemprop="sameAs" content="https://github.com/ioai-tech/rlds_dataset_builder" />
  <meta itemprop="citation" content="" />
</div>

# `io_ai_tech`


*   **Description**:

*   **Homepage**:
    [https://github.com/ioai-tech/rlds_dataset_builder](https://github.com/ioai-tech/rlds_dataset_builder)

*   **Source code**:
    [`tfds.robotics.rtx.IoAiTech`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `89.63 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,847

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
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
            'depth': Image(shape=(720, 1280, 1), dtype=uint8),
            'fisheye_camera_extrinsic': Tensor(shape=(4, 4), dtype=float32),
            'fisheye_camera_intrinsic': Tensor(shape=(3, 3), dtype=float32),
            'image': Image(shape=(360, 640, 3), dtype=uint8),
            'image_fisheye': Image(shape=(640, 800, 3), dtype=uint8),
            'image_left_side': Image(shape=(360, 640, 3), dtype=uint8),
            'image_right_side': Image(shape=(360, 640, 3), dtype=uint8),
            'left_camera_extrinsic': Tensor(shape=(4, 4), dtype=float32),
            'left_camera_intrinsic': Tensor(shape=(3, 3), dtype=float32),
            'main_camera_intrinsic': Tensor(shape=(3, 3), dtype=float32),
            'right_camera_extrinsic': Tensor(shape=(4, 4), dtype=float32),
            'right_camera_intrinsic': Tensor(shape=(3, 3), dtype=float32),
            'state': Tensor(shape=(8,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape          | Dtype   | Description
:----------------------------------------- | :----------- | :------------- | :------ | :----------
                                           | FeaturesDict |                |         |
episode_metadata                           | FeaturesDict |                |         |
episode_metadata/file_path                 | Tensor       |                | string  |
steps                                      | Dataset      |                |         |
steps/action                               | Tensor       | (7,)           | float32 |
steps/discount                             | Scalar       |                | float32 |
steps/is_first                             | Tensor       |                | bool    |
steps/is_last                              | Tensor       |                | bool    |
steps/is_terminal                          | Tensor       |                | bool    |
steps/language_embedding                   | Tensor       | (512,)         | float32 |
steps/language_instruction                 | Tensor       |                | string  |
steps/observation                          | FeaturesDict |                |         |
steps/observation/depth                    | Image        | (720, 1280, 1) | uint8   |
steps/observation/fisheye_camera_extrinsic | Tensor       | (4, 4)         | float32 |
steps/observation/fisheye_camera_intrinsic | Tensor       | (3, 3)         | float32 |
steps/observation/image                    | Image        | (360, 640, 3)  | uint8   |
steps/observation/image_fisheye            | Image        | (640, 800, 3)  | uint8   |
steps/observation/image_left_side          | Image        | (360, 640, 3)  | uint8   |
steps/observation/image_right_side         | Image        | (360, 640, 3)  | uint8   |
steps/observation/left_camera_extrinsic    | Tensor       | (4, 4)         | float32 |
steps/observation/left_camera_intrinsic    | Tensor       | (3, 3)         | float32 |
steps/observation/main_camera_intrinsic    | Tensor       | (3, 3)         | float32 |
steps/observation/right_camera_extrinsic   | Tensor       | (4, 4)         | float32 |
steps/observation/right_camera_intrinsic   | Tensor       | (3, 3)         | float32 |
steps/observation/state                    | Tensor       | (8,)           | float32 |
steps/reward                               | Scalar       |                | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/io_ai_tech-0.1.0.html";
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

