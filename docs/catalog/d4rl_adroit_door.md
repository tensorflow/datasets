<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_adroit_door" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_adroit_door&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_adroit_door" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl-anonymous" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_adroit_door`


*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

*   **Config description**: See more details about the task and its versions in
    https://github.com/rail-berkeley/d4rl/wiki/Tasks#adroit

*   **Homepage**:
    [https://sites.google.com/view/d4rl-anonymous](https://sites.google.com/view/d4rl-anonymous)

*   **Source code**:
    [`tfds.d4rl.d4rl_adroit_door.D4rlAdroitDoor`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_adroit_door/d4rl_adroit_door.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.1.0`** (default): Added is_last.

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


## d4rl_adroit_door/v0-human (default config)

*   **Download size**: `2.97 MiB`

*   **Dataset size**: `3.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'qpos': Tensor(shape=(30,), dtype=float32),
            'qvel': Tensor(shape=(30,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (28,) | float32 |
steps/discount    | Tensor       |       | float32 |
steps/infos       | FeaturesDict |       |         |
steps/infos/qpos  | Tensor       | (30,) | float32 |
steps/infos/qvel  | Tensor       | (30,) | float32 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (39,) | float32 |
steps/reward      | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v0-human-1.1.0.html";
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

## d4rl_adroit_door/v0-cloned

*   **Download size**: `602.42 MiB`

*   **Dataset size**: `497.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,214

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float64,
        'infos': FeaturesDict({
            'qpos': Tensor(shape=(30,), dtype=float64),
            'qvel': Tensor(shape=(30,), dtype=float64),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float64),
        'reward': float64,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
steps             | Dataset      |       |         |
steps/action      | Tensor       | (28,) | float32 |
steps/discount    | Tensor       |       | float64 |
steps/infos       | FeaturesDict |       |         |
steps/infos/qpos  | Tensor       | (30,) | float64 |
steps/infos/qvel  | Tensor       | (30,) | float64 |
steps/is_first    | Tensor       |       | bool    |
steps/is_last     | Tensor       |       | bool    |
steps/is_terminal | Tensor       |       | bool    |
steps/observation | Tensor       | (39,) | float64 |
steps/reward      | Tensor       |       | float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v0-cloned-1.1.0.html";
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

## d4rl_adroit_door/v0-expert

*   **Download size**: `511.05 MiB`

*   **Dataset size**: `710.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,000

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_logstd': Tensor(shape=(28,), dtype=float32),
            'action_mean': Tensor(shape=(28,), dtype=float32),
            'qpos': Tensor(shape=(30,), dtype=float32),
            'qvel': Tensor(shape=(30,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                   | Class        | Shape | Dtype   | Description
:------------------------ | :----------- | :---- | :------ | :----------
                          | FeaturesDict |       |         |
steps                     | Dataset      |       |         |
steps/action              | Tensor       | (28,) | float32 |
steps/discount            | Tensor       |       | float32 |
steps/infos               | FeaturesDict |       |         |
steps/infos/action_logstd | Tensor       | (28,) | float32 |
steps/infos/action_mean   | Tensor       | (28,) | float32 |
steps/infos/qpos          | Tensor       | (30,) | float32 |
steps/infos/qvel          | Tensor       | (30,) | float32 |
steps/is_first            | Tensor       |       | bool    |
steps/is_last             | Tensor       |       | bool    |
steps/is_terminal         | Tensor       |       | bool    |
steps/observation         | Tensor       | (39,) | float32 |
steps/reward              | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v0-expert-1.1.0.html";
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

## d4rl_adroit_door/v1-human

*   **Download size**: `2.98 MiB`

*   **Dataset size**: `3.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'door_body_pos': Tensor(shape=(3,), dtype=float32),
            'qpos': Tensor(shape=(30,), dtype=float32),
            'qvel': Tensor(shape=(30,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                   | Class        | Shape | Dtype   | Description
:------------------------ | :----------- | :---- | :------ | :----------
                          | FeaturesDict |       |         |
steps                     | Dataset      |       |         |
steps/action              | Tensor       | (28,) | float32 |
steps/discount            | Tensor       |       | float32 |
steps/infos               | FeaturesDict |       |         |
steps/infos/door_body_pos | Tensor       | (3,)  | float32 |
steps/infos/qpos          | Tensor       | (30,) | float32 |
steps/infos/qvel          | Tensor       | (30,) | float32 |
steps/is_first            | Tensor       |       | bool    |
steps/is_last             | Tensor       |       | bool    |
steps/is_terminal         | Tensor       |       | bool    |
steps/observation         | Tensor       | (39,) | float32 |
steps/reward              | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v1-human-1.1.0.html";
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

## d4rl_adroit_door/v1-cloned

*   **Download size**: `280.72 MiB`

*   **Dataset size**: `1.85 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,358

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(39, 256), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=float32),
            'weight': Tensor(shape=(256, 256), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(28,), dtype=float32),
            'weight': Tensor(shape=(256, 28), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'door_body_pos': Tensor(shape=(3,), dtype=float32),
            'qpos': Tensor(shape=(30,), dtype=float32),
            'qvel': Tensor(shape=(30,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape      | Dtype   | Description
:------------------------- | :----------- | :--------- | :------ | :----------
                           | FeaturesDict |            |         |
algorithm                  | Tensor       |            | string  |
policy                     | FeaturesDict |            |         |
policy/fc0                 | FeaturesDict |            |         |
policy/fc0/bias            | Tensor       | (256,)     | float32 |
policy/fc0/weight          | Tensor       | (39, 256)  | float32 |
policy/fc1                 | FeaturesDict |            |         |
policy/fc1/bias            | Tensor       | (256,)     | float32 |
policy/fc1/weight          | Tensor       | (256, 256) | float32 |
policy/last_fc             | FeaturesDict |            |         |
policy/last_fc/bias        | Tensor       | (28,)      | float32 |
policy/last_fc/weight      | Tensor       | (256, 28)  | float32 |
policy/nonlinearity        | Tensor       |            | string  |
policy/output_distribution | Tensor       |            | string  |
steps                      | Dataset      |            |         |
steps/action               | Tensor       | (28,)      | float32 |
steps/discount             | Tensor       |            | float32 |
steps/infos                | FeaturesDict |            |         |
steps/infos/door_body_pos  | Tensor       | (3,)       | float32 |
steps/infos/qpos           | Tensor       | (30,)      | float32 |
steps/infos/qvel           | Tensor       | (30,)      | float32 |
steps/is_first             | Tensor       |            | bool    |
steps/is_last              | Tensor       |            | bool    |
steps/is_terminal          | Tensor       |            | bool    |
steps/observation          | Tensor       | (39,)      | float32 |
steps/reward               | Tensor       |            | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v1-cloned-1.1.0.html";
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

## d4rl_adroit_door/v1-expert

*   **Download size**: `511.22 MiB`

*   **Dataset size**: `803.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,000

*   **Feature structure**:

```python
FeaturesDict({
    'algorithm': string,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(32,), dtype=float32),
            'weight': Tensor(shape=(32, 39), dtype=float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(32,), dtype=float32),
            'weight': Tensor(shape=(32, 32), dtype=float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(28,), dtype=float32),
            'weight': Tensor(shape=(28, 32), dtype=float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(28,), dtype=float32),
            'weight': Tensor(shape=(28, 32), dtype=float32),
        }),
        'nonlinearity': string,
        'output_distribution': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(28,), dtype=float32),
        'discount': float32,
        'infos': FeaturesDict({
            'action_log_std': Tensor(shape=(28,), dtype=float32),
            'action_mean': Tensor(shape=(28,), dtype=float32),
            'door_body_pos': Tensor(shape=(3,), dtype=float32),
            'qpos': Tensor(shape=(30,), dtype=float32),
            'qvel': Tensor(shape=(30,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': Tensor(shape=(39,), dtype=float32),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape    | Dtype   | Description
:---------------------------- | :----------- | :------- | :------ | :----------
                              | FeaturesDict |          |         |
algorithm                     | Tensor       |          | string  |
policy                        | FeaturesDict |          |         |
policy/fc0                    | FeaturesDict |          |         |
policy/fc0/bias               | Tensor       | (32,)    | float32 |
policy/fc0/weight             | Tensor       | (32, 39) | float32 |
policy/fc1                    | FeaturesDict |          |         |
policy/fc1/bias               | Tensor       | (32,)    | float32 |
policy/fc1/weight             | Tensor       | (32, 32) | float32 |
policy/last_fc                | FeaturesDict |          |         |
policy/last_fc/bias           | Tensor       | (28,)    | float32 |
policy/last_fc/weight         | Tensor       | (28, 32) | float32 |
policy/last_fc_log_std        | FeaturesDict |          |         |
policy/last_fc_log_std/bias   | Tensor       | (28,)    | float32 |
policy/last_fc_log_std/weight | Tensor       | (28, 32) | float32 |
policy/nonlinearity           | Tensor       |          | string  |
policy/output_distribution    | Tensor       |          | string  |
steps                         | Dataset      |          |         |
steps/action                  | Tensor       | (28,)    | float32 |
steps/discount                | Tensor       |          | float32 |
steps/infos                   | FeaturesDict |          |         |
steps/infos/action_log_std    | Tensor       | (28,)    | float32 |
steps/infos/action_mean       | Tensor       | (28,)    | float32 |
steps/infos/door_body_pos     | Tensor       | (3,)     | float32 |
steps/infos/qpos              | Tensor       | (30,)    | float32 |
steps/infos/qvel              | Tensor       | (30,)    | float32 |
steps/is_first                | Tensor       |          | bool    |
steps/is_last                 | Tensor       |          | bool    |
steps/is_terminal             | Tensor       |          | bool    |
steps/observation             | Tensor       | (39,)    | float32 |
steps/reward                  | Tensor       |          | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_adroit_door-v1-expert-1.1.0.html";
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