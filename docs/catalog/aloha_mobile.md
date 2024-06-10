<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="aloha_mobile" />
  <meta itemprop="description" content="Real dataset. Imitating mobile manipulation tasks that are bimanual and require whole-body control.  50 demonstrations for each task.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;aloha_mobile&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/aloha_mobile" />
  <meta itemprop="sameAs" content="https://mobile-aloha.github.io" />
  <meta itemprop="citation" content="@inproceedings{fu2024mobile,author = {Fu, Zipeng and Zhao, Tony Z. and Finn, Chelsea},title = {Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation},booktitle = {arXiv},year = {2024},}" />
</div>

# `aloha_mobile`


*   **Description**:

Real dataset. Imitating mobile manipulation tasks that are bimanual and require
whole-body control. 50 demonstrations for each task.

*   **Homepage**:
    [https://mobile-aloha.github.io](https://mobile-aloha.github.io)

*   **Source code**:
    [`tfds.robotics.rtx.AlohaMobile`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `47.42 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 276

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(16,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_instruction': string,
        'observation': FeaturesDict({
            'cam_high': Image(shape=(480, 640, 3), dtype=uint8),
            'cam_left_wrist': Image(shape=(480, 640, 3), dtype=uint8),
            'cam_right_wrist': Image(shape=(480, 640, 3), dtype=uint8),
            'state': Tensor(shape=(14,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                           | Class        | Shape         | Dtype   | Description
:-------------------------------- | :----------- | :------------ | :------ | :----------
                                  | FeaturesDict |               |         |
episode_metadata                  | FeaturesDict |               |         |
episode_metadata/file_path        | Tensor       |               | string  |
steps                             | Dataset      |               |         |
steps/action                      | Tensor       | (16,)         | float32 |
steps/discount                    | Scalar       |               | float32 |
steps/is_first                    | Tensor       |               | bool    |
steps/is_last                     | Tensor       |               | bool    |
steps/is_terminal                 | Tensor       |               | bool    |
steps/language_instruction        | Tensor       |               | string  |
steps/observation                 | FeaturesDict |               |         |
steps/observation/cam_high        | Image        | (480, 640, 3) | uint8   |
steps/observation/cam_left_wrist  | Image        | (480, 640, 3) | uint8   |
steps/observation/cam_right_wrist | Image        | (480, 640, 3) | uint8   |
steps/observation/state           | Tensor       | (14,)         | float32 |
steps/reward                      | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/aloha_mobile-0.1.0.html";
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
@inproceedings{fu2024mobile,author = {Fu, Zipeng and Zhao, Tony Z. and Finn, Chelsea},title = {Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation},booktitle = {arXiv},year = {2024},}
```

