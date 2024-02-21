<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imperialcollege_sawyer_wrist_cam" />
  <meta itemprop="description" content="Sawyer performing table top manipulation&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imperialcollege_sawyer_wrist_cam&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imperialcollege_sawyer_wrist_cam" />
  <meta itemprop="sameAs" content="--" />
  <meta itemprop="citation" content="--" />
</div>

# `imperialcollege_sawyer_wrist_cam`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Sawyer performing table top manipulation

*   **Homepage**: [--](--)

*   **Source code**:
    [`tfds.robotics.rtx.ImperialcollegeSawyerWristCam`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `81.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 170

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(64, 64, 3), dtype=uint8),
            'state': Tensor(shape=(1,), dtype=float32),
            'wrist_image': Image(shape=(64, 64, 3), dtype=uint8),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape       | Dtype   | Description
:---------------------------- | :----------- | :---------- | :------ | :----------
                              | FeaturesDict |             |         |
episode_metadata              | FeaturesDict |             |         |
episode_metadata/file_path    | Text         |             | string  | Path to the original data file.
steps                         | Dataset      |             |         |
steps/action                  | Tensor       | (8,)        | float32 | Robot action, consists of 3x delta position in EEF frame, 3x delta ZYX euler angles, 1x gripper open/close, 1x terminate episode.
steps/discount                | Scalar       |             | float32 | Discount if provided, default to 1.
steps/is_first                | Tensor       |             | bool    |
steps/is_last                 | Tensor       |             | bool    |
steps/is_terminal             | Tensor       |             | bool    |
steps/language_embedding      | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction    | Text         |             | string  | Language Instruction.
steps/observation             | FeaturesDict |             |         |
steps/observation/image       | Image        | (64, 64, 3) | uint8   | Main camera RGB observation (same as wrist in our case).
steps/observation/state       | Tensor       | (1,)        | float32 | Gripper state (opened or closed)
steps/observation/wrist_image | Image        | (64, 64, 3) | uint8   | Wrist camera RGB observation.
steps/reward                  | Scalar       |             | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imperialcollege_sawyer_wrist_cam-0.1.0.html";
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
--
```

