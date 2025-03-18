<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mt_opt" />
  <meta itemprop="description" content="Datasets for the [MT-Opt paper](https://arxiv.org/abs/2104.08212).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mt_opt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mt_opt" />
  <meta itemprop="sameAs" content="https://karolhausman.github.io/mt-opt/" />
  <meta itemprop="citation" content="@misc{kalashnikov2021mtopt,&#10;      title={MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale},&#10;      author={Dmitry Kalashnikov and Jacob Varley and Yevgen Chebotar and Benjamin Swanson and Rico Jonschkowski and Chelsea Finn and Sergey Levine and Karol Hausman},&#10;      year={2021},&#10;      eprint={2104.08212},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.RO}&#10;}" />
</div>

# `mt_opt`


*   **Description**:

Datasets for the [MT-Opt paper](https://arxiv.org/abs/2104.08212).

*   **Homepage**:
    [https://karolhausman.github.io/mt-opt/](https://karolhausman.github.io/mt-opt/)

*   **Source code**:
    [`tfds.robotics.mt_opt.MtOpt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/mt_opt/mt_opt.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{kalashnikov2021mtopt,
      title={MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale},
      author={Dmitry Kalashnikov and Jacob Varley and Yevgen Chebotar and Benjamin Swanson and Rico Jonschkowski and Chelsea Finn and Sergey Levine and Karol Hausman},
      year={2021},
      eprint={2104.08212},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```


## mt_opt/rlds (default config)

*   **Config description**: This dataset contains task episodes collected across
    afleet of real robots. It follows the
    [RLDS format](https://github.com/google-research/rlds)to represent steps and
    episodes.

*   **Dataset size**: `4.38 TiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 920,165

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': string,
    'skill': uint8,
    'steps': Dataset({
        'action': FeaturesDict({
            'close_gripper': bool,
            'open_gripper': bool,
            'target_pose': Tensor(shape=(7,), dtype=float32),
            'terminate': bool,
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'gripper_closed': bool,
            'height_to_bottom': float32,
            'image': Image(shape=(512, 640, 3), dtype=uint8),
            'state_dense': Tensor(shape=(7,), dtype=float32),
        }),
    }),
    'task_code': string,
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape         | Dtype   | Description
:--------------------------------- | :----------- | :------------ | :------ | :----------
                                   | FeaturesDict |               |         |
episode_id                         | Tensor       |               | string  |
skill                              | Tensor       |               | uint8   |
steps                              | Dataset      |               |         |
steps/action                       | FeaturesDict |               |         |
steps/action/close_gripper         | Tensor       |               | bool    |
steps/action/open_gripper          | Tensor       |               | bool    |
steps/action/target_pose           | Tensor       | (7,)          | float32 |
steps/action/terminate             | Tensor       |               | bool    |
steps/is_first                     | Tensor       |               | bool    |
steps/is_last                      | Tensor       |               | bool    |
steps/is_terminal                  | Tensor       |               | bool    |
steps/observation                  | FeaturesDict |               |         |
steps/observation/gripper_closed   | Tensor       |               | bool    |
steps/observation/height_to_bottom | Tensor       |               | float32 |
steps/observation/image            | Image        | (512, 640, 3) | uint8   |
steps/observation/state_dense      | Tensor       | (7,)          | float32 |
task_code                          | Tensor       |               | string  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mt_opt-rlds-1.0.0.html";
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

## mt_opt/sd

*   **Config description**: The success detectors dataset that contains human
    curated definitions of tasks completion.

*   **Dataset size**: `548.56 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 94,636
`'train'` | 380,234

*   **Feature structure**:

```python
FeaturesDict({
    'image_0': Image(shape=(512, 640, 3), dtype=uint8),
    'image_1': Image(shape=(480, 640, 3), dtype=uint8),
    'image_2': Image(shape=(480, 640, 3), dtype=uint8),
    'success': bool,
    'task_code': string,
})
```

*   **Feature documentation**:

Feature   | Class        | Shape         | Dtype  | Description
:-------- | :----------- | :------------ | :----- | :----------
          | FeaturesDict |               |        |
image_0   | Image        | (512, 640, 3) | uint8  |
image_1   | Image        | (480, 640, 3) | uint8  |
image_2   | Image        | (480, 640, 3) | uint8  |
success   | Tensor       |               | bool   |
task_code | Tensor       |               | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mt_opt-sd-1.0.0.html";
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