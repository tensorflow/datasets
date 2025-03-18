<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_mujoco_ant" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_mujoco_ant&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_mujoco_ant" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl-anonymous" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_mujoco_ant`


*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Config description**: See more details about the task and its versions in
    https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym

*   **Homepage**:
    [https://sites.google.com/view/d4rl-anonymous](https://sites.google.com/view/d4rl-anonymous)

*   **Source code**:
    [`tfds.d4rl.d4rl_mujoco_ant.D4rlMujocoAnt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_mujoco_ant/d4rl_mujoco_ant.py)

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


## d4rl_mujoco_ant/v0-expert (default config)

*   **Download size**: `131.34 MiB`

*   **Dataset size**: `464.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,288

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape  | Dtype   | Description
:---------------- | :----------- | :----- | :------ | :----------
                  | FeaturesDict |        |         |
steps             | Dataset      |        |         |
steps/action      | Tensor       | (8,)   | float32 |
steps/discount    | Tensor       |        | float32 |
steps/is_first    | Tensor       |        | bool    |
steps/is_last     | Tensor       |        | bool    |
steps/is_terminal | Tensor       |        | bool    |
steps/observation | Tensor       | (111,) | float32 |
steps/reward      | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v0-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v0-medium

*   **Download size**: `131.39 MiB`

*   **Dataset size**: `464.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,122

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape  | Dtype   | Description
:---------------- | :----------- | :----- | :------ | :----------
                  | FeaturesDict |        |         |
steps             | Dataset      |        |         |
steps/action      | Tensor       | (8,)   | float32 |
steps/discount    | Tensor       |        | float32 |
steps/is_first    | Tensor       |        | bool    |
steps/is_last     | Tensor       |        | bool    |
steps/is_terminal | Tensor       |        | bool    |
steps/observation | Tensor       | (111,) | float32 |
steps/reward      | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v0-medium-1.2.0.html";
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

## d4rl_mujoco_ant/v0-medium-expert

*   **Download size**: `262.73 MiB`

*   **Dataset size**: `929.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,410

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape  | Dtype   | Description
:---------------- | :----------- | :----- | :------ | :----------
                  | FeaturesDict |        |         |
steps             | Dataset      |        |         |
steps/action      | Tensor       | (8,)   | float32 |
steps/discount    | Tensor       |        | float32 |
steps/is_first    | Tensor       |        | bool    |
steps/is_last     | Tensor       |        | bool    |
steps/is_terminal | Tensor       |        | bool    |
steps/observation | Tensor       | (111,) | float32 |
steps/reward      | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v0-medium-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v0-mixed

*   **Download size**: `104.63 MiB`

*   **Dataset size**: `464.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,320

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape  | Dtype   | Description
:---------------- | :----------- | :----- | :------ | :----------
                  | FeaturesDict |        |         |
steps             | Dataset      |        |         |
steps/action      | Tensor       | (8,)   | float32 |
steps/discount    | Tensor       |        | float32 |
steps/is_first    | Tensor       |        | bool    |
steps/is_last     | Tensor       |        | bool    |
steps/is_terminal | Tensor       |        | bool    |
steps/observation | Tensor       | (111,) | float32 |
steps/reward      | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v0-mixed-1.2.0.html";
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

## d4rl_mujoco_ant/v0-random

*   **Download size**: `139.50 MiB`

*   **Dataset size**: `464.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,377

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape  | Dtype   | Description
:---------------- | :----------- | :----- | :------ | :----------
                  | FeaturesDict |        |         |
steps             | Dataset      |        |         |
steps/action      | Tensor       | (8,)   | float32 |
steps/discount    | Tensor       |        | float32 |
steps/is_first    | Tensor       |        | bool    |
steps/is_last     | Tensor       |        | bool    |
steps/is_terminal | Tensor       |        | bool    |
steps/observation | Tensor       | (111,) | float32 |
steps/reward      | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v0-random-1.2.0.html";
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

## d4rl_mujoco_ant/v1-expert

*   **Download size**: `220.72 MiB`

*   **Dataset size**: `968.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,033

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 111), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(15,), dtype=float32),
            'qvel': Tensor(shape=(14,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
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
policy/fc0/weight             | Tensor       | (256, 111) | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (8,)       | float32 |
policy/last_fc/weight         | Tensor       | (8, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (8,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (8, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (8,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float32 |
steps/infos/qpos              | Tensor       | (15,)      | float32 |
steps/infos/qvel              | Tensor       | (14,)      | float32 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (111,)     | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v1-medium

*   **Download size**: `222.39 MiB`

*   **Dataset size**: `1023.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,179

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 111), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(15,), dtype=float32),
            'qvel': Tensor(shape=(14,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
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
policy/fc0/weight             | Tensor       | (256, 111) | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (8,)       | float32 |
policy/last_fc/weight         | Tensor       | (8, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (8,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (8, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (8,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float32 |
steps/infos/qpos              | Tensor       | (15,)      | float32 |
steps/infos/qvel              | Tensor       | (14,)      | float32 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (111,)     | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-medium-1.2.0.html";
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

## d4rl_mujoco_ant/v1-medium-expert

*   **Download size**: `442.25 MiB`

*   **Dataset size**: `1.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,211

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(15,), dtype=float32),
            'qvel': Tensor(shape=(14,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float32 |
steps/infos/qpos             | Tensor       | (15,)  | float32 |
steps/infos/qvel             | Tensor       | (14,)  | float32 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-medium-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v1-medium-replay

*   **Download size**: `132.05 MiB`

*   **Dataset size**: `175.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 485

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float64),
        'discount': float64,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float64),
        'reward': float64,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
algorithm                    | Tensor       |        | string  |
iteration                    | Tensor       |        | int32   |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float64 |
steps/discount               | Tensor       |        | float64 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float64 |
steps/reward                 | Tensor       |        | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-medium-replay-1.2.0.html";
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

## d4rl_mujoco_ant/v1-full-replay

*   **Download size**: `437.57 MiB`

*   **Dataset size**: `580.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,319

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float64),
        'discount': float64,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float64),
        'reward': float64,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
algorithm                    | Tensor       |        | string  |
iteration                    | Tensor       |        | int32   |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float64 |
steps/discount               | Tensor       |        | float64 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float64 |
steps/reward                 | Tensor       |        | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-full-replay-1.2.0.html";
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

## d4rl_mujoco_ant/v1-random

*   **Download size**: `225.18 MiB`

*   **Dataset size**: `583.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,741

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float32,
            'qpos': Tensor(shape=(15,), dtype=float32),
            'qvel': Tensor(shape=(14,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float32 |
steps/infos/qpos             | Tensor       | (15,)  | float32 |
steps/infos/qvel             | Tensor       | (14,)  | float32 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v1-random-1.2.0.html";
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

## d4rl_mujoco_ant/v2-expert

*   **Download size**: `355.94 MiB`

*   **Dataset size**: `969.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,035

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 111), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
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
policy/fc0/weight             | Tensor       | (256, 111) | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (8,)       | float32 |
policy/last_fc/weight         | Tensor       | (8, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (8,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (8, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (8,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float64 |
steps/infos/qpos              | Tensor       | (15,)      | float64 |
steps/infos/qvel              | Tensor       | (14,)      | float64 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (111,)     | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v2-full-replay

*   **Download size**: `428.57 MiB`

*   **Dataset size**: `580.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,319

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
algorithm                    | Tensor       |        | string  |
iteration                    | Tensor       |        | int32   |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-full-replay-1.2.0.html";
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

## d4rl_mujoco_ant/v2-medium

*   **Download size**: `358.81 MiB`

*   **Dataset size**: `1.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,203

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 111), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=float32),
            'weight': Tensor(shape=(8, 256), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
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
policy/fc0/weight             | Tensor       | (256, 111) | float32 |
policy/fc1                    | FeaturesDict |            |         |
policy/fc1/bias               | Tensor       | (256,)     | float32 |
policy/fc1/weight             | Tensor       | (256, 256) | float32 |
policy/last_fc                | FeaturesDict |            |         |
policy/last_fc/bias           | Tensor       | (8,)       | float32 |
policy/last_fc/weight         | Tensor       | (8, 256)   | float32 |
policy/last_fc_log_std        | FeaturesDict |            |         |
policy/last_fc_log_std/bias   | Tensor       | (8,)       | float32 |
policy/last_fc_log_std/weight | Tensor       | (8, 256)   | float32 |
policy/nonlinearity           | Tensor       |            | string  |
policy/output_distribution    | Tensor       |            | string  |
steps                         | Dataset      |            |         |
steps/action                  | Tensor       | (8,)       | float32 |
steps/discount                | Tensor       |            | float32 |
steps/infos                   | FeaturesDict |            |         |
steps/infos/action_log_probs  | Tensor       |            | float64 |
steps/infos/qpos              | Tensor       | (15,)      | float64 |
steps/infos/qvel              | Tensor       | (14,)      | float64 |
steps/is_first                | Tensor       |            | bool    |
steps/is_last                 | Tensor       |            | bool    |
steps/is_terminal             | Tensor       |            | bool    |
steps/observation             | Tensor       | (111,)     | float32 |
steps/reward                  | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-medium-1.2.0.html";
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

## d4rl_mujoco_ant/v2-medium-expert

*   **Download size**: `713.67 MiB`

*   **Dataset size**: `1.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,237

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-medium-expert-1.2.0.html";
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

## d4rl_mujoco_ant/v2-medium-replay

*   **Download size**: `130.16 MiB`

*   **Dataset size**: `175.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 485

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'iteration': int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
algorithm                    | Tensor       |        | string  |
iteration                    | Tensor       |        | int32   |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-medium-replay-1.2.0.html";
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

## d4rl_mujoco_ant/v2-random

*   **Download size**: `366.66 MiB`

*   **Dataset size**: `583.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,822

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_probs': float64,
            'qpos': Tensor(shape=(15,), dtype=float64),
            'qvel': Tensor(shape=(14,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(111,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape  | Dtype   | Description
:--------------------------- | :----------- | :----- | :------ | :----------
                             | FeaturesDict |        |         |
steps                        | Dataset      |        |         |
steps/action                 | Tensor       | (8,)   | float32 |
steps/discount               | Tensor       |        | float32 |
steps/infos                  | FeaturesDict |        |         |
steps/infos/action_log_probs | Tensor       |        | float64 |
steps/infos/qpos             | Tensor       | (15,)  | float64 |
steps/infos/qvel             | Tensor       | (14,)  | float64 |
steps/is_first               | Tensor       |        | bool    |
steps/is_last                | Tensor       |        | bool    |
steps/is_terminal            | Tensor       |        | bool    |
steps/observation            | Tensor       | (111,) | float32 |
steps/reward                 | Tensor       |        | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_ant-v2-random-1.2.0.html";
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