<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dlr_sara_grid_clamp_converted_externally_to_rlds" />
  <meta itemprop="description" content="place grid clamp onto grids on table&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dlr_sara_grid_clamp_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dlr_sara_grid_clamp_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://www.researchsquare.com/article/rs-3289569/v1" />
  <meta itemprop="citation" content="@article{padalkar2023guided,&#10;  title={A guided reinforcement learning approach using shared control templates for learning manipulation skills in the real world},&#10;  author={Padalkar, Abhishek and Quere, Gabriel and Raffin, Antonin and Silv{\&#x27;e}rio, Jo{\~a}o and Stulp, Freek},&#10;  journal={Research square preprint rs-3289569/v1},&#10;  year={2023}&#10;}" />
</div>

# `dlr_sara_grid_clamp_converted_externally_to_rlds`


*   **Description**:

place grid clamp onto grids on table

*   **Homepage**:
    [https://www.researchsquare.com/article/rs-3289569/v1](https://www.researchsquare.com/article/rs-3289569/v1)

*   **Source code**:
    [`tfds.robotics.rtx.DlrSaraGridClampConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `1.65 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 107

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(480, 640, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(12,), dtype=float32, description=Robot state, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler("zxy") Class, 6x robot EEF wrench].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape         | Dtype   | Description
:------------------------- | :----------- | :------------ | :------ | :----------
                           | FeaturesDict |               |         |
episode_metadata           | FeaturesDict |               |         |
episode_metadata/file_path | Text         |               | string  | Path to the original data file.
steps                      | Dataset      |               |         |
steps/action               | Tensor       | (7,)          | float32 | Robot action, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].
steps/discount             | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |               | bool    |
steps/is_last              | Tensor       |               | bool    |
steps/is_terminal          | Tensor       |               | bool    |
steps/language_embedding   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |               | string  | Pour into the mug.
steps/observation          | FeaturesDict |               |         |
steps/observation/image    | Image        | (480, 640, 3) | uint8   | Main camera RGB observation.
steps/observation/state    | Tensor       | (12,)         | float32 | Robot state, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler("zxy") Class, 6x robot EEF wrench].
steps/reward               | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dlr_sara_grid_clamp_converted_externally_to_rlds-0.1.0.html";
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
@article{padalkar2023guided,
  title={A guided reinforcement learning approach using shared control templates for learning manipulation skills in the real world},
  author={Padalkar, Abhishek and Quere, Gabriel and Raffin, Antonin and Silv{\'e}rio, Jo{\~a}o and Stulp, Freek},
  journal={Research square preprint rs-3289569/v1},
  year={2023}
}
```

