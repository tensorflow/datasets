<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="plex_robosuite" />
  <meta itemprop="description" content="A dataset of high-qualty demonstration trajectories for Robosuite&#x27;s Door, Stack, PickPlaceMilk, PickPlaceBread, PickPlaceCereal, and NutAssemblyRound tasks, 75 demonstrations per each.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;plex_robosuite&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/plex_robosuite" />
  <meta itemprop="sameAs" content="https://microsoft.github.io/PLEX/" />
  <meta itemprop="citation" content="https://doi.org/10.48550/arXiv.2303.08789" />
</div>

# `plex_robosuite`


*   **Description**:

A dataset of high-qualty demonstration trajectories for Robosuite's Door, Stack,
PickPlaceMilk, PickPlaceBread, PickPlaceCereal, and NutAssemblyRound tasks, 75
demonstrations per each.

*   **Homepage**:
    [https://microsoft.github.io/PLEX/](https://microsoft.github.io/PLEX/)

*   **Source code**:
    [`tfds.robotics.rtx.PlexRobosuite`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `1.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 402
`'val'`   | 48

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'episode_id': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float64),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': string,
        'observation': FeaturesDict({
            'image': Image(shape=(128, 128, 3), dtype=uint8),
            'state': Tensor(shape=(32,), dtype=float64),
            'wrist_image': Image(shape=(128, 128, 3), dtype=uint8),
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
episode_metadata/episode_id   | Tensor       |               | string  |
steps                         | Dataset      |               |         |
steps/action                  | Tensor       | (7,)          | float64 |
steps/discount                | Scalar       |               | float32 |
steps/is_first                | Tensor       |               | bool    |
steps/is_last                 | Tensor       |               | bool    |
steps/is_terminal             | Tensor       |               | bool    |
steps/language_embedding      | Tensor       | (512,)        | float32 |
steps/language_instruction    | Tensor       |               | string  |
steps/observation             | FeaturesDict |               |         |
steps/observation/image       | Image        | (128, 128, 3) | uint8   |
steps/observation/state       | Tensor       | (32,)         | float64 |
steps/observation/wrist_image | Image        | (128, 128, 3) | uint8   |
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/plex_robosuite-0.1.0.html";
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
https://doi.org/10.48550/arXiv.2303.08789
```

