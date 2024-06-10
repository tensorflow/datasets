<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dobbe" />
  <meta itemprop="description" content="&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dobbe&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dobbe" />
  <meta itemprop="sameAs" content="https://github.com/notmahi/dobb-e" />
  <meta itemprop="citation" content="@misc{shafiullah2023dobbe, title={On Bringing Robots Home}, author={Nur Muhammad Mahi Shafiullah and Anant Rai and Haritheja Etukuru and Yiqian Liu and Ishan Misra and Soumith Chintala and Lerrel Pinto}, year={2023}, eprint={2311.16098}, archivePrefix={arXiv}, primaryClass={cs.RO} }" />
</div>

# `dobbe`


*   **Description**:

*   **Homepage**:
    [https://github.com/notmahi/dobb-e](https://github.com/notmahi/dobb-e)

*   **Source code**:
    [`tfds.robotics.rtx.Dobbe`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `21.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,208

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
            'gripper': Tensor(shape=(1,), dtype=float32),
            'quat': Tensor(shape=(4,), dtype=float32),
            'rot': Tensor(shape=(3,), dtype=float32),
            'state': Tensor(shape=(7,), dtype=float32),
            'wrist_image': Image(shape=(256, 256, 3), dtype=uint8),
            'xyz': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape         | Dtype   | Description
:---------------------------- | :----------- | :------------ | :------ | :----------
                              | FeaturesDict |               |         |
episode_metadata              | FeaturesDict |               |         |
episode_metadata/file_path    | Tensor       |               | string  |
steps                         | Dataset      |               |         |
steps/action                  | Tensor       | (7,)          | float32 |
steps/discount                | Scalar       |               | float32 |
steps/is_first                | Tensor       |               | bool    |
steps/is_last                 | Tensor       |               | bool    |
steps/is_terminal             | Tensor       |               | bool    |
steps/language_embedding      | Tensor       | (512,)        | float32 |
steps/language_instruction    | Tensor       |               | string  |
steps/observation             | FeaturesDict |               |         |
steps/observation/gripper     | Tensor       | (1,)          | float32 |
steps/observation/quat        | Tensor       | (4,)          | float32 |
steps/observation/rot         | Tensor       | (3,)          | float32 |
steps/observation/state       | Tensor       | (7,)          | float32 |
steps/observation/wrist_image | Image        | (256, 256, 3) | uint8   |
steps/observation/xyz         | Tensor       | (3,)          | float32 |
steps/reward                  | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dobbe-0.1.0.html";
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
@misc{shafiullah2023dobbe, title={On Bringing Robots Home}, author={Nur Muhammad Mahi Shafiullah and Anant Rai and Haritheja Etukuru and Yiqian Liu and Ishan Misra and Soumith Chintala and Lerrel Pinto}, year={2023}, eprint={2311.16098}, archivePrefix={arXiv}, primaryClass={cs.RO} }
```

