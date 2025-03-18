<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="berkeley_cable_routing" />
  <meta itemprop="description" content="Routing cable into clamps on table top&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;berkeley_cable_routing&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/berkeley_cable_routing" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/cablerouting/home" />
  <meta itemprop="citation" content="@article{luo2023multistage,&#10;  author    = {Jianlan Luo and Charles Xu and Xinyang Geng and Gilbert Feng and Kuan Fang and Liam Tan and Stefan Schaal and Sergey Levine},&#10;  title     = {Multi-Stage Cable Routing through Hierarchical Imitation Learning},&#10;  journal   = {arXiv pre-print},&#10;  year      = {2023},&#10;  url       = {https://arxiv.org/abs/2307.08927},&#10;}" />
</div>

# `berkeley_cable_routing`


*   **Description**:

Routing cable into clamps on table top

*   **Homepage**:
    [https://sites.google.com/view/cablerouting/home](https://sites.google.com/view/cablerouting/home)

*   **Source code**:
    [`tfds.robotics.rtx.BerkeleyCableRouting`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `4.67 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 165
`'train'` | 1,482

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'rotation_delta': Tensor(shape=(3,), dtype=float32, description=Angular velocity about the z axis.),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32, description=Velocity in XYZ.),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'image': Image(shape=(128, 128, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'robot_state': Tensor(shape=(7,), dtype=float32),
            'top_image': Image(shape=(128, 128, 3), dtype=uint8),
            'wrist225_image': Image(shape=(128, 128, 3), dtype=uint8),
            'wrist45_image': Image(shape=(128, 128, 3), dtype=uint8),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                        | Class        | Shape         | Dtype   | Description
:--------------------------------------------- | :----------- | :------------ | :------ | :----------
                                               | FeaturesDict |               |         |
steps                                          | Dataset      |               |         |
steps/action                                   | FeaturesDict |               |         |
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 | Angular velocity about the z axis.
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 | Velocity in XYZ.
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/image                        | Image        | (128, 128, 3) | uint8   |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
steps/observation/robot_state                  | Tensor       | (7,)          | float32 |
steps/observation/top_image                    | Image        | (128, 128, 3) | uint8   |
steps/observation/wrist225_image               | Image        | (128, 128, 3) | uint8   |
steps/observation/wrist45_image                | Image        | (128, 128, 3) | uint8   |
steps/reward                                   | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/berkeley_cable_routing-0.1.0.html";
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
@article{luo2023multistage,
  author    = {Jianlan Luo and Charles Xu and Xinyang Geng and Gilbert Feng and Kuan Fang and Liam Tan and Stefan Schaal and Sergey Levine},
  title     = {Multi-Stage Cable Routing through Hierarchical Imitation Learning},
  journal   = {arXiv pre-print},
  year      = {2023},
  url       = {https://arxiv.org/abs/2307.08927},
}
```

