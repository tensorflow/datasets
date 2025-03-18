<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_mujoco_halfcheetah" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_mujoco_halfcheetah&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_mujoco_halfcheetah" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl-anonymous" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_mujoco_halfcheetah`


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
    [`tfds.d4rl.d4rl_mujoco_halfcheetah.D4rlMujocoHalfcheetah`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_mujoco_halfcheetah/d4rl_mujoco_halfcheetah.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.0.1`: Support for episode and step metadata, and unification of the
        reward shape across all the configs.
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


## d4rl_mujoco_halfcheetah/v0-expert (default config)

*   **Download size**: `83.44 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v0-medium

*   **Download size**: `82.92 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-medium-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v0-medium-expert

*   **Download size**: `166.36 MiB`

*   **Dataset size**: `196.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,004

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-medium-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v0-mixed

*   **Download size**: `8.60 MiB`

*   **Dataset size**: `9.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 101

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-mixed-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v0-random

*   **Download size**: `84.79 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-random-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-expert

*   **Download size**: `146.94 MiB`

*   **Dataset size**: `451.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium

*   **Download size**: `146.65 MiB`

*   **Dataset size**: `451.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium-expert

*   **Download size**: `293.00 MiB`

*   **Dataset size**: `342.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium-replay

*   **Download size**: `57.68 MiB`

*   **Dataset size**: `34.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-replay-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-full-replay

*   **Download size**: `285.01 MiB`

*   **Dataset size**: `171.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-full-replay-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v1-random

*   **Download size**: `145.19 MiB`

*   **Dataset size**: `171.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-random-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-expert

*   **Download size**: `226.46 MiB`

*   **Dataset size**: `451.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-full-replay

*   **Download size**: `277.88 MiB`

*   **Dataset size**: `171.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-full-replay-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium

*   **Download size**: `226.71 MiB`

*   **Dataset size**: `451.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium-expert

*   **Download size**: `452.58 MiB`

*   **Dataset size**: `342.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-expert-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium-replay

*   **Download size**: `56.69 MiB`

*   **Dataset size**: `34.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-replay-1.2.0.html";
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

## d4rl_mujoco_halfcheetah/v2-random

*   **Download size**: `226.34 MiB`

*   **Dataset size**: `171.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-random-1.2.0.html";
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