<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_mujoco_walker2d" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_mujoco_walker2d&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_mujoco_walker2d" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl-anonymous" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_mujoco_walker2d`


*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/d4rl">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Config description**: See more details about the task and its versions in
    https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym

*   **Homepage**:
    [https://sites.google.com/view/d4rl-anonymous](https://sites.google.com/view/d4rl-anonymous)

*   **Source code**:
    [`tfds.d4rl.d4rl_mujoco_walker2d.D4rlMujocoWalker2d`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_mujoco_walker2d/d4rl_mujoco_walker2d.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.1.0`: Added is_last.
    *   **`1.2.0`** (default): Updated to take into account the next
        observation.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{fu2020d4rl,
    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},
    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
    year={2020},
    eprint={2004.07219},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```


## d4rl_mujoco_walker2d/v0-expert (default config)

*   **Download size**: `78.41 MiB`

*   **Dataset size**: `98.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,628

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (6,)  | float32 |
steps/discount    | Tensor       |       | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (17,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v0-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v0-medium

*   **Download size**: `80.83 MiB`

*   **Dataset size**: `99.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,315

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (6,)  | float32 |
steps/discount    | Tensor       |       | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (17,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v0-medium-1.2.0.html";
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

## d4rl_mujoco_walker2d/v0-medium-expert

*   **Download size**: `159.24 MiB`

*   **Dataset size**: `198.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,943

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (6,)  | float32 |
steps/discount    | Tensor       |       | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (17,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v0-medium-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v0-mixed

*   **Download size**: `8.42 MiB`

*   **Dataset size**: `10.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 501

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (6,)  | float32 |
steps/discount    | Tensor       |       | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (17,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v0-mixed-1.2.0.html";
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

## d4rl_mujoco_walker2d/v0-random

*   **Download size**: `78.41 MiB`

*   **Dataset size**: `112.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50,988

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (6,)  | float32 |
steps/discount    | Tensor       |       | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (17,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v0-random-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-expert

*   **Download size**: `143.06 MiB`

*   **Dataset size**: `452.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,003

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 17), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(9,), dtype=float32),
            'qvel': Tensor(shape=(9,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape      | Dtype   | Description
:---------------------------- | :----------- | :--------- | :------ | :----------
                              | FeaturesDict |            |         |
algorithm                     | Tensor       |            | string  |
iteration                     | Tensor       |            | int32   |
policy                        | FeaturesDict |            |         |
policy/fc0                    | FeaturesDict |            |         |
policy/fc0/bias               | Tensor       | (256,)     | float32 |
policy/fc0/weight             | Tensor       | (256, 17)  | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (6,)       | float32 |
policy/last_fc/weight         | Tensor       | (6, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (6,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (6, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (6,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float32 |
steps/infos/qpos              | Tensor       | (9,)       | float32 |
steps/infos/qvel              | Tensor       | (9,)       | float32 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (17,)      | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-medium

*   **Download size**: `144.23 MiB`

*   **Dataset size**: `510.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,207

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 17), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(9,), dtype=float32),
            'qvel': Tensor(shape=(9,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape      | Dtype   | Description
:---------------------------- | :----------- | :--------- | :------ | :----------
                              | FeaturesDict |            |         |
algorithm                     | Tensor       |            | string  |
iteration                     | Tensor       |            | int32   |
policy                        | FeaturesDict |            |         |
policy/fc0                    | FeaturesDict |            |         |
policy/fc0/bias               | Tensor       | (256,)     | float32 |
policy/fc0/weight             | Tensor       | (256, 17)  | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (6,)       | float32 |
policy/last_fc/weight         | Tensor       | (6, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (6,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (6, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (6,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float32 |
steps/infos/qpos              | Tensor       | (9,)       | float32 |
steps/infos/qvel              | Tensor       | (9,)       | float32 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (17,)      | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-medium-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-medium-expert

*   **Download size**: `286.69 MiB`

*   **Dataset size**: `342.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,209

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(9,), dtype=float32),
            'qvel': Tensor(shape=(9,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float32 |
steps/infos/qpos             | Tensor       | (9,)  | float32 |
steps/infos/qvel             | Tensor       | (9,)  | float32 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-medium-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-medium-replay

*   **Download size**: `84.37 MiB`

*   **Dataset size**: `52.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,093

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float64),
        'discount': float64,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float64),
        'reward': float64,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
algorithm                    | Tensor       |       | string  |
iteration                    | Tensor       |       | int32   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float64 |
steps/discount               | Tensor       |       | float64 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float64 |
steps/reward                 | Tensor       |       | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-medium-replay-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-full-replay

*   **Download size**: `278.95 MiB`

*   **Dataset size**: `171.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,888

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float64),
        'discount': float64,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float64),
        'reward': float64,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
algorithm                    | Tensor       |       | string  |
iteration                    | Tensor       |       | int32   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float64 |
steps/discount               | Tensor       |       | float64 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float64 |
steps/reward                 | Tensor       |       | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-full-replay-1.2.0.html";
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

## d4rl_mujoco_walker2d/v1-random

*   **Download size**: `132.36 MiB`

*   **Dataset size**: `192.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,790

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(9,), dtype=float32),
            'qvel': Tensor(shape=(9,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float32 |
steps/infos/qpos             | Tensor       | (9,)  | float32 |
steps/infos/qvel             | Tensor       | (9,)  | float32 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v1-random-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-expert

*   **Download size**: `219.89 MiB`

*   **Dataset size**: `452.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,001

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 17), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape      | Dtype   | Description
:---------------------------- | :----------- | :--------- | :------ | :----------
                              | FeaturesDict |            |         |
algorithm                     | Tensor       |            | string  |
iteration                     | Tensor       |            | int32   |
policy                        | FeaturesDict |            |         |
policy/fc0                    | FeaturesDict |            |         |
policy/fc0/bias               | Tensor       | (256,)     | float32 |
policy/fc0/weight             | Tensor       | (256, 17)  | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (6,)       | float32 |
policy/last_fc/weight         | Tensor       | (6, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (6,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (6, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (6,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float64 |
steps/infos/qpos              | Tensor       | (9,)       | float64 |
steps/infos/qvel              | Tensor       | (9,)       | float64 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (17,)      | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-full-replay

*   **Download size**: `271.91 MiB`

*   **Dataset size**: `171.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,888

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
algorithm                    | Tensor       |       | string  |
iteration                    | Tensor       |       | int32   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-full-replay-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-medium

*   **Download size**: `221.50 MiB`

*   **Dataset size**: `505.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,191

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 17), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=float32),
            'weight': Tensor(shape=(6, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape      | Dtype   | Description
:---------------------------- | :----------- | :--------- | :------ | :----------
                              | FeaturesDict |            |         |
algorithm                     | Tensor       |            | string  |
iteration                     | Tensor       |            | int32   |
policy                        | FeaturesDict |            |         |
policy/fc0                    | FeaturesDict |            |         |
policy/fc0/bias               | Tensor       | (256,)     | float32 |
policy/fc0/weight             | Tensor       | (256, 17)  | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (6,)       | float32 |
policy/last_fc/weight         | Tensor       | (6, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (6,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (6, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (6,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float64 |
steps/infos/qpos              | Tensor       | (9,)       | float64 |
steps/infos/qvel              | Tensor       | (9,)       | float64 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (17,)      | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-medium-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-medium-expert

*   **Download size**: `440.79 MiB`

*   **Dataset size**: `342.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,191

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-medium-expert-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-medium-replay

*   **Download size**: `82.32 MiB`

*   **Dataset size**: `52.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,093

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
algorithm                    | Tensor       |       | string  |
iteration                    | Tensor       |       | int32   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-medium-replay-1.2.0.html";
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

## d4rl_mujoco_walker2d/v2-random

*   **Download size**: `206.10 MiB`

*   **Dataset size**: `192.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,908

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(9,), dtype=float64),
            'qvel': Tensor(shape=(9,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(17,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (6,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/infos                  | FeaturesDict |       |         |
steps/infos/action_log_probs | Tensor       |       | float64 |
steps/infos/qpos             | Tensor       | (9,)  | float64 |
steps/infos/qvel             | Tensor       | (9,)  | float64 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | Tensor       | (17,) | float32 |
steps/reward                 | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_walker2d-v2-random-1.2.0.html";
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