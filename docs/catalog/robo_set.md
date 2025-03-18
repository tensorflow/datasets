<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robo_set" />
  <meta itemprop="description" content="Real dataset of a single robot arm demonstrating 12 non-trivial manipulation skills across 38 tasks, 7500 trajectories.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robo_set&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robo_set" />
  <meta itemprop="sameAs" content="https://robopen.github.io/" />
  <meta itemprop="citation" content="@misc{bharadhwaj2023roboagent, title={RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking}, author={Homanga Bharadhwaj and Jay Vakil and Mohit Sharma and Abhinav Gupta and Shubham Tulsiani and Vikash Kumar},  year={2023}, eprint={2309.01918}, archivePrefix={arXiv}, primaryClass={cs.RO} }" />
</div>

# `robo_set`


*   **Description**:

Real dataset of a single robot arm demonstrating 12 non-trivial manipulation
skills across 38 tasks, 7500 trajectories.

*   **Homepage**: [https://robopen.github.io/](https://robopen.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.RoboSet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `179.42 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,250

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': string,
        'trial_id': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_instruction': string,
        'observation': FeaturesDict({
            'image_left': Image(shape=(240, 424, 3), dtype=uint8),
            'image_right': Image(shape=(240, 424, 3), dtype=uint8),
            'image_top': Image(shape=(240, 424, 3), dtype=uint8),
            'image_wrist': Image(shape=(240, 424, 3), dtype=uint8),
            'state': Tensor(shape=(8,), dtype=float32),
            'state_velocity': Tensor(shape=(8,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape         | Dtype   | Description
:------------------------------- | :----------- | :------------ | :------ | :----------
                                 | FeaturesDict |               |         |
episode_metadata                 | FeaturesDict |               |         |
episode_metadata/file_path       | Tensor       |               | string  |
episode_metadata/trial_id        | Tensor       |               | string  |
steps                            | Dataset      |               |         |
steps/action                     | Tensor       | (8,)          | float32 |
steps/discount                   | Scalar       |               | float32 |
steps/is_first                   | Tensor       |               | bool    |
steps/is_last                    | Tensor       |               | bool    |
steps/is_terminal                | Tensor       |               | bool    |
steps/language_instruction       | Tensor       |               | string  |
steps/observation                | FeaturesDict |               |         |
steps/observation/image_left     | Image        | (240, 424, 3) | uint8   |
steps/observation/image_right    | Image        | (240, 424, 3) | uint8   |
steps/observation/image_top      | Image        | (240, 424, 3) | uint8   |
steps/observation/image_wrist    | Image        | (240, 424, 3) | uint8   |
steps/observation/state          | Tensor       | (8,)          | float32 |
steps/observation/state_velocity | Tensor       | (8,)          | float32 |
steps/reward                     | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/robo_set-0.1.0.html";
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
@misc{bharadhwaj2023roboagent, title={RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking}, author={Homanga Bharadhwaj and Jay Vakil and Mohit Sharma and Abhinav Gupta and Shubham Tulsiani and Vikash Kumar},  year={2023}, eprint={2309.01918}, archivePrefix={arXiv}, primaryClass={cs.RO} }
```

