<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="berkeley_gnm_sac_son" />
  <meta itemprop="description" content="office navigation&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;berkeley_gnm_sac_son&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/berkeley_gnm_sac_son" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/SACSoN-review" />
  <meta itemprop="citation" content="@article{hirose2023sacson,&#10;  title={SACSoN: Scalable Autonomous Data Collection for Social Navigation},&#10;  author={Hirose, Noriaki and Shah, Dhruv and Sridhar, Ajay and Levine, Sergey},&#10;  journal={arXiv preprint arXiv:2306.01874},&#10;  year={2023}&#10;}" />
</div>

# `berkeley_gnm_sac_son`


*   **Description**:

office navigation

*   **Homepage**:
    [https://sites.google.com/view/SACSoN-review](https://sites.google.com/view/SACSoN-review)

*   **Source code**:
    [`tfds.robotics.rtx.BerkeleyGnmSacSon`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `7.00 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,955

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(2,), dtype=float64, description=Robot action, consists of 2x position),
        'action_angle': Tensor(shape=(3,), dtype=float64, description=Robot action, consists of 2x position, 1x yaw),
        'discount': Scalar(shape=(), dtype=float64, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(120, 160, 3), dtype=uint8, description=Main camera RGB observation.),
            'position': Tensor(shape=(2,), dtype=float64, description=Robot position),
            'state': Tensor(shape=(3,), dtype=float64, description=Robot state, consists of [2x position, 1x yaw]),
            'yaw': Tensor(shape=(1,), dtype=float64, description=Robot yaw),
        }),
        'reward': Scalar(shape=(), dtype=float64, description=Reward if provided, 1 on final step for demos.),
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
steps/action               | Tensor       | (2,)          | float64 | Robot action, consists of 2x position
steps/action_angle         | Tensor       | (3,)          | float64 | Robot action, consists of 2x position, 1x yaw
steps/discount             | Scalar       |               | float64 | Discount if provided, default to 1.
steps/is_first             | Tensor       |               | bool    |
steps/is_last              | Tensor       |               | bool    |
steps/is_terminal          | Tensor       |               | bool    |
steps/language_embedding   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |               | string  | Language Instruction.
steps/observation          | FeaturesDict |               |         |
steps/observation/image    | Image        | (120, 160, 3) | uint8   | Main camera RGB observation.
steps/observation/position | Tensor       | (2,)          | float64 | Robot position
steps/observation/state    | Tensor       | (3,)          | float64 | Robot state, consists of [2x position, 1x yaw]
steps/observation/yaw      | Tensor       | (1,)          | float64 | Robot yaw
steps/reward               | Scalar       |               | float64 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/berkeley_gnm_sac_son-0.1.0.html";
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
@article{hirose2023sacson,
  title={SACSoN: Scalable Autonomous Data Collection for Social Navigation},
  author={Hirose, Noriaki and Shah, Dhruv and Sridhar, Ajay and Levine, Sergey},
  journal={arXiv preprint arXiv:2306.01874},
  year={2023}
}
```

