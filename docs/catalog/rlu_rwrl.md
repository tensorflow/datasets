<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rlu_rwrl" />
  <meta itemprop="description" content="RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL&#10;Unplugged is designed around the following considerations: to facilitate ease of&#10;use, we provide the datasets with a unified API which makes it easy for the&#10;practitioner to work with all data in the suite once a general pipeline has been&#10;established.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;&#10;Examples in the dataset represent SAR transitions stored when running a&#10;partially online trained agent as described in https://arxiv.org/abs/1904.12901.&#10;We follow the RLDS dataset format, as specified in&#10;https://github.com/google-research/rlds#dataset-format.&#10;&#10;&#10;We release 40 datasets on 8 tasks in total -- with no combined challenge and&#10;easy combined challenge on the cartpole, walker, quadruped, and humanoid tasks.&#10;Each task contains 5 different sizes of datasets, 1%, 5%, 20%, 40%, and 100%.&#10;Note that the smaller dataset is not guaranteed to be a subset of the larger&#10;ones. For details on how the dataset was generated, please refer to the paper.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rlu_rwrl&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rlu_rwrl" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged" />
  <meta itemprop="citation" content="@misc{gulcehre2020rl,&#10;    title={RL Unplugged: Benchmarks for Offline Reinforcement Learning},&#10;    author={Caglar Gulcehre and Ziyu Wang and Alexander Novikov and Tom Le Paine&#10;        and  Sergio Gómez Colmenarejo and Konrad Zolna and Rishabh Agarwal and&#10;        Josh Merel and Daniel Mankowitz and Cosmin Paduraru and Gabriel&#10;        Dulac-Arnold and Jerry Li and Mohammad Norouzi and Matt Hoffman and&#10;        Ofir Nachum and George Tucker and Nicolas Heess and Nando deFreitas},&#10;    year={2020},&#10;    eprint={2006.13888},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `rlu_rwrl`


*   **Description**:

RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

Examples in the dataset represent SAR transitions stored when running a
partially online trained agent as described in https://arxiv.org/abs/1904.12901.
We follow the RLDS dataset format, as specified in
https://github.com/google-research/rlds#dataset-format.

We release 40 datasets on 8 tasks in total -- with no combined challenge and
easy combined challenge on the cartpole, walker, quadruped, and humanoid tasks.
Each task contains 5 different sizes of datasets, 1%, 5%, 20%, 40%, and 100%.
Note that the smaller dataset is not guaranteed to be a subset of the larger
ones. For details on how the dataset was generated, please refer to the paper.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged)

*   **Source code**:
    [`tfds.rl_unplugged.rlu_rwrl.RluRwrl`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rl_unplugged/rlu_rwrl/rlu_rwrl.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Fixes a bug in RLU RWRL dataset where there are
        duplicated episode ids in one of the humanoid datasets.

*   **Download size**: `Unknown size`

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{gulcehre2020rl,
    title={RL Unplugged: Benchmarks for Offline Reinforcement Learning},
    author={Caglar Gulcehre and Ziyu Wang and Alexander Novikov and Tom Le Paine
        and  Sergio Gómez Colmenarejo and Konrad Zolna and Rishabh Agarwal and
        Josh Merel and Daniel Mankowitz and Cosmin Paduraru and Gabriel
        Dulac-Arnold and Jerry Li and Mohammad Norouzi and Matt Hoffman and
        Ofir Nachum and George Tucker and Nicolas Heess and Nando deFreitas},
    year={2020},
    eprint={2006.13888},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```


## rlu_rwrl/cartpole_swingup_combined_challenge_none_1_percent (default config)

*   **Dataset size**: `172.43 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_none_1_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_none_5_percent

*   **Dataset size**: `862.13 KiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_none_5_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_none_20_percent

*   **Dataset size**: `3.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_none_20_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_none_40_percent

*   **Dataset size**: `6.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_none_40_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_none_100_percent

*   **Dataset size**: `16.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_none_100_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_none_1_percent

*   **Dataset size**: `1.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_none_1_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_none_5_percent

*   **Dataset size**: `8.86 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_none_5_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_none_20_percent

*   **Dataset size**: `35.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_none_20_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_none_40_percent

*   **Dataset size**: `70.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_none_40_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_none_100_percent

*   **Dataset size**: `177.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_none_100_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_none_1_percent

*   **Dataset size**: `6.27 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_none_1_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_none_5_percent

*   **Dataset size**: `31.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 250

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_none_5_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_none_20_percent

*   **Dataset size**: `125.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_none_20_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_none_40_percent

*   **Dataset size**: `250.75 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_none_40_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_none_100_percent

*   **Dataset size**: `626.86 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_none_100_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_none_1_percent

*   **Dataset size**: `69.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_none_1_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_none_5_percent

*   **Dataset size**: `346.98 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_none_5_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_none_20_percent

*   **Dataset size**: `1.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_none_20_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_none_40_percent

*   **Dataset size**: `2.71 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_none_40_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_none_100_percent

*   **Dataset size**: `6.78 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_none_100_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_1_percent

*   **Dataset size**: `369.84 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/dummy-0  | Tensor       | (1,)  | float32 |
steps/observation/dummy-1  | Tensor       | (1,)  | float32 |
steps/observation/dummy-2  | Tensor       | (1,)  | float32 |
steps/observation/dummy-3  | Tensor       | (1,)  | float32 |
steps/observation/dummy-4  | Tensor       | (1,)  | float32 |
steps/observation/dummy-5  | Tensor       | (1,)  | float32 |
steps/observation/dummy-6  | Tensor       | (1,)  | float32 |
steps/observation/dummy-7  | Tensor       | (1,)  | float32 |
steps/observation/dummy-8  | Tensor       | (1,)  | float32 |
steps/observation/dummy-9  | Tensor       | (1,)  | float32 |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_easy_1_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_5_percent

*   **Dataset size**: `1.81 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/dummy-0  | Tensor       | (1,)  | float32 |
steps/observation/dummy-1  | Tensor       | (1,)  | float32 |
steps/observation/dummy-2  | Tensor       | (1,)  | float32 |
steps/observation/dummy-3  | Tensor       | (1,)  | float32 |
steps/observation/dummy-4  | Tensor       | (1,)  | float32 |
steps/observation/dummy-5  | Tensor       | (1,)  | float32 |
steps/observation/dummy-6  | Tensor       | (1,)  | float32 |
steps/observation/dummy-7  | Tensor       | (1,)  | float32 |
steps/observation/dummy-8  | Tensor       | (1,)  | float32 |
steps/observation/dummy-9  | Tensor       | (1,)  | float32 |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_easy_5_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_20_percent

*   **Dataset size**: `7.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/dummy-0  | Tensor       | (1,)  | float32 |
steps/observation/dummy-1  | Tensor       | (1,)  | float32 |
steps/observation/dummy-2  | Tensor       | (1,)  | float32 |
steps/observation/dummy-3  | Tensor       | (1,)  | float32 |
steps/observation/dummy-4  | Tensor       | (1,)  | float32 |
steps/observation/dummy-5  | Tensor       | (1,)  | float32 |
steps/observation/dummy-6  | Tensor       | (1,)  | float32 |
steps/observation/dummy-7  | Tensor       | (1,)  | float32 |
steps/observation/dummy-8  | Tensor       | (1,)  | float32 |
steps/observation/dummy-9  | Tensor       | (1,)  | float32 |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_easy_20_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_40_percent

*   **Dataset size**: `14.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/dummy-0  | Tensor       | (1,)  | float32 |
steps/observation/dummy-1  | Tensor       | (1,)  | float32 |
steps/observation/dummy-2  | Tensor       | (1,)  | float32 |
steps/observation/dummy-3  | Tensor       | (1,)  | float32 |
steps/observation/dummy-4  | Tensor       | (1,)  | float32 |
steps/observation/dummy-5  | Tensor       | (1,)  | float32 |
steps/observation/dummy-6  | Tensor       | (1,)  | float32 |
steps/observation/dummy-7  | Tensor       | (1,)  | float32 |
steps/observation/dummy-8  | Tensor       | (1,)  | float32 |
steps/observation/dummy-9  | Tensor       | (1,)  | float32 |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_easy_40_percent-1.0.1.html";
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

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_100_percent

*   **Dataset size**: `36.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_return             | Tensor       |       | float32 |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       | (1,)  | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/dummy-0  | Tensor       | (1,)  | float32 |
steps/observation/dummy-1  | Tensor       | (1,)  | float32 |
steps/observation/dummy-2  | Tensor       | (1,)  | float32 |
steps/observation/dummy-3  | Tensor       | (1,)  | float32 |
steps/observation/dummy-4  | Tensor       | (1,)  | float32 |
steps/observation/dummy-5  | Tensor       | (1,)  | float32 |
steps/observation/dummy-6  | Tensor       | (1,)  | float32 |
steps/observation/dummy-7  | Tensor       | (1,)  | float32 |
steps/observation/dummy-8  | Tensor       | (1,)  | float32 |
steps/observation/dummy-9  | Tensor       | (1,)  | float32 |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-cartpole_swingup_combined_challenge_easy_100_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_easy_1_percent

*   **Dataset size**: `1.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/dummy-0          | Tensor       | (1,)  | float32 |
steps/observation/dummy-1          | Tensor       | (1,)  | float32 |
steps/observation/dummy-2          | Tensor       | (1,)  | float32 |
steps/observation/dummy-3          | Tensor       | (1,)  | float32 |
steps/observation/dummy-4          | Tensor       | (1,)  | float32 |
steps/observation/dummy-5          | Tensor       | (1,)  | float32 |
steps/observation/dummy-6          | Tensor       | (1,)  | float32 |
steps/observation/dummy-7          | Tensor       | (1,)  | float32 |
steps/observation/dummy-8          | Tensor       | (1,)  | float32 |
steps/observation/dummy-9          | Tensor       | (1,)  | float32 |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_easy_1_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_easy_5_percent

*   **Dataset size**: `9.83 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/dummy-0          | Tensor       | (1,)  | float32 |
steps/observation/dummy-1          | Tensor       | (1,)  | float32 |
steps/observation/dummy-2          | Tensor       | (1,)  | float32 |
steps/observation/dummy-3          | Tensor       | (1,)  | float32 |
steps/observation/dummy-4          | Tensor       | (1,)  | float32 |
steps/observation/dummy-5          | Tensor       | (1,)  | float32 |
steps/observation/dummy-6          | Tensor       | (1,)  | float32 |
steps/observation/dummy-7          | Tensor       | (1,)  | float32 |
steps/observation/dummy-8          | Tensor       | (1,)  | float32 |
steps/observation/dummy-9          | Tensor       | (1,)  | float32 |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_easy_5_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_easy_20_percent

*   **Dataset size**: `39.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/dummy-0          | Tensor       | (1,)  | float32 |
steps/observation/dummy-1          | Tensor       | (1,)  | float32 |
steps/observation/dummy-2          | Tensor       | (1,)  | float32 |
steps/observation/dummy-3          | Tensor       | (1,)  | float32 |
steps/observation/dummy-4          | Tensor       | (1,)  | float32 |
steps/observation/dummy-5          | Tensor       | (1,)  | float32 |
steps/observation/dummy-6          | Tensor       | (1,)  | float32 |
steps/observation/dummy-7          | Tensor       | (1,)  | float32 |
steps/observation/dummy-8          | Tensor       | (1,)  | float32 |
steps/observation/dummy-9          | Tensor       | (1,)  | float32 |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_easy_20_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_easy_40_percent

*   **Dataset size**: `78.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/dummy-0          | Tensor       | (1,)  | float32 |
steps/observation/dummy-1          | Tensor       | (1,)  | float32 |
steps/observation/dummy-2          | Tensor       | (1,)  | float32 |
steps/observation/dummy-3          | Tensor       | (1,)  | float32 |
steps/observation/dummy-4          | Tensor       | (1,)  | float32 |
steps/observation/dummy-5          | Tensor       | (1,)  | float32 |
steps/observation/dummy-6          | Tensor       | (1,)  | float32 |
steps/observation/dummy-7          | Tensor       | (1,)  | float32 |
steps/observation/dummy-8          | Tensor       | (1,)  | float32 |
steps/observation/dummy-9          | Tensor       | (1,)  | float32 |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_easy_40_percent-1.0.1.html";
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

## rlu_rwrl/quadruped_walk_combined_challenge_easy_100_percent

*   **Dataset size**: `196.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'egocentric_state': Tensor(shape=(44,), dtype=float32),
            'force_torque': Tensor(shape=(24,), dtype=float32),
            'imu': Tensor(shape=(6,), dtype=float32),
            'torso_upright': Tensor(shape=(1,), dtype=float32),
            'torso_velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                            | Class        | Shape | Dtype   | Description
:--------------------------------- | :----------- | :---- | :------ | :----------
                                   | FeaturesDict |       |         |
episode_return                     | Tensor       |       | float32 |
steps                              | Dataset      |       |         |
steps/action                       | Tensor       | (12,) | float32 |
steps/discount                     | Tensor       | (1,)  | float32 |
steps/is_first                     | Tensor       |       | bool    |
steps/is_last                      | Tensor       |       | bool    |
steps/is_terminal                  | Tensor       |       | bool    |
steps/observation                  | FeaturesDict |       |         |
steps/observation/dummy-0          | Tensor       | (1,)  | float32 |
steps/observation/dummy-1          | Tensor       | (1,)  | float32 |
steps/observation/dummy-2          | Tensor       | (1,)  | float32 |
steps/observation/dummy-3          | Tensor       | (1,)  | float32 |
steps/observation/dummy-4          | Tensor       | (1,)  | float32 |
steps/observation/dummy-5          | Tensor       | (1,)  | float32 |
steps/observation/dummy-6          | Tensor       | (1,)  | float32 |
steps/observation/dummy-7          | Tensor       | (1,)  | float32 |
steps/observation/dummy-8          | Tensor       | (1,)  | float32 |
steps/observation/dummy-9          | Tensor       | (1,)  | float32 |
steps/observation/egocentric_state | Tensor       | (44,) | float32 |
steps/observation/force_torque     | Tensor       | (24,) | float32 |
steps/observation/imu              | Tensor       | (6,)  | float32 |
steps/observation/torso_upright    | Tensor       | (1,)  | float32 |
steps/observation/torso_velocity   | Tensor       | (3,)  | float32 |
steps/reward                       | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-quadruped_walk_combined_challenge_easy_100_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_easy_1_percent

*   **Dataset size**: `8.20 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/dummy-0      | Tensor       | (1,)  | float32 |
steps/observation/dummy-1      | Tensor       | (1,)  | float32 |
steps/observation/dummy-2      | Tensor       | (1,)  | float32 |
steps/observation/dummy-3      | Tensor       | (1,)  | float32 |
steps/observation/dummy-4      | Tensor       | (1,)  | float32 |
steps/observation/dummy-5      | Tensor       | (1,)  | float32 |
steps/observation/dummy-6      | Tensor       | (1,)  | float32 |
steps/observation/dummy-7      | Tensor       | (1,)  | float32 |
steps/observation/dummy-8      | Tensor       | (1,)  | float32 |
steps/observation/dummy-9      | Tensor       | (1,)  | float32 |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_easy_1_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_easy_5_percent

*   **Dataset size**: `40.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 250

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/dummy-0      | Tensor       | (1,)  | float32 |
steps/observation/dummy-1      | Tensor       | (1,)  | float32 |
steps/observation/dummy-2      | Tensor       | (1,)  | float32 |
steps/observation/dummy-3      | Tensor       | (1,)  | float32 |
steps/observation/dummy-4      | Tensor       | (1,)  | float32 |
steps/observation/dummy-5      | Tensor       | (1,)  | float32 |
steps/observation/dummy-6      | Tensor       | (1,)  | float32 |
steps/observation/dummy-7      | Tensor       | (1,)  | float32 |
steps/observation/dummy-8      | Tensor       | (1,)  | float32 |
steps/observation/dummy-9      | Tensor       | (1,)  | float32 |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_easy_5_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_easy_20_percent

*   **Dataset size**: `163.93 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/dummy-0      | Tensor       | (1,)  | float32 |
steps/observation/dummy-1      | Tensor       | (1,)  | float32 |
steps/observation/dummy-2      | Tensor       | (1,)  | float32 |
steps/observation/dummy-3      | Tensor       | (1,)  | float32 |
steps/observation/dummy-4      | Tensor       | (1,)  | float32 |
steps/observation/dummy-5      | Tensor       | (1,)  | float32 |
steps/observation/dummy-6      | Tensor       | (1,)  | float32 |
steps/observation/dummy-7      | Tensor       | (1,)  | float32 |
steps/observation/dummy-8      | Tensor       | (1,)  | float32 |
steps/observation/dummy-9      | Tensor       | (1,)  | float32 |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_easy_20_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_easy_40_percent

*   **Dataset size**: `327.86 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/dummy-0      | Tensor       | (1,)  | float32 |
steps/observation/dummy-1      | Tensor       | (1,)  | float32 |
steps/observation/dummy-2      | Tensor       | (1,)  | float32 |
steps/observation/dummy-3      | Tensor       | (1,)  | float32 |
steps/observation/dummy-4      | Tensor       | (1,)  | float32 |
steps/observation/dummy-5      | Tensor       | (1,)  | float32 |
steps/observation/dummy-6      | Tensor       | (1,)  | float32 |
steps/observation/dummy-7      | Tensor       | (1,)  | float32 |
steps/observation/dummy-8      | Tensor       | (1,)  | float32 |
steps/observation/dummy-9      | Tensor       | (1,)  | float32 |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_easy_40_percent-1.0.1.html";
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

## rlu_rwrl/walker_walk_combined_challenge_easy_100_percent

*   **Dataset size**: `819.65 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_return                 | Tensor       |       | float32 |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       | (1,)  | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/dummy-0      | Tensor       | (1,)  | float32 |
steps/observation/dummy-1      | Tensor       | (1,)  | float32 |
steps/observation/dummy-2      | Tensor       | (1,)  | float32 |
steps/observation/dummy-3      | Tensor       | (1,)  | float32 |
steps/observation/dummy-4      | Tensor       | (1,)  | float32 |
steps/observation/dummy-5      | Tensor       | (1,)  | float32 |
steps/observation/dummy-6      | Tensor       | (1,)  | float32 |
steps/observation/dummy-7      | Tensor       | (1,)  | float32 |
steps/observation/dummy-8      | Tensor       | (1,)  | float32 |
steps/observation/dummy-9      | Tensor       | (1,)  | float32 |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-walker_walk_combined_challenge_easy_100_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_easy_1_percent

*   **Dataset size**: `77.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/dummy-0        | Tensor       | (1,)  | float32 |
steps/observation/dummy-1        | Tensor       | (1,)  | float32 |
steps/observation/dummy-2        | Tensor       | (1,)  | float32 |
steps/observation/dummy-3        | Tensor       | (1,)  | float32 |
steps/observation/dummy-4        | Tensor       | (1,)  | float32 |
steps/observation/dummy-5        | Tensor       | (1,)  | float32 |
steps/observation/dummy-6        | Tensor       | (1,)  | float32 |
steps/observation/dummy-7        | Tensor       | (1,)  | float32 |
steps/observation/dummy-8        | Tensor       | (1,)  | float32 |
steps/observation/dummy-9        | Tensor       | (1,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_easy_1_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_easy_5_percent

*   **Dataset size**: `385.54 MiB`

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
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/dummy-0        | Tensor       | (1,)  | float32 |
steps/observation/dummy-1        | Tensor       | (1,)  | float32 |
steps/observation/dummy-2        | Tensor       | (1,)  | float32 |
steps/observation/dummy-3        | Tensor       | (1,)  | float32 |
steps/observation/dummy-4        | Tensor       | (1,)  | float32 |
steps/observation/dummy-5        | Tensor       | (1,)  | float32 |
steps/observation/dummy-6        | Tensor       | (1,)  | float32 |
steps/observation/dummy-7        | Tensor       | (1,)  | float32 |
steps/observation/dummy-8        | Tensor       | (1,)  | float32 |
steps/observation/dummy-9        | Tensor       | (1,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_easy_5_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_easy_20_percent

*   **Dataset size**: `1.51 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/dummy-0        | Tensor       | (1,)  | float32 |
steps/observation/dummy-1        | Tensor       | (1,)  | float32 |
steps/observation/dummy-2        | Tensor       | (1,)  | float32 |
steps/observation/dummy-3        | Tensor       | (1,)  | float32 |
steps/observation/dummy-4        | Tensor       | (1,)  | float32 |
steps/observation/dummy-5        | Tensor       | (1,)  | float32 |
steps/observation/dummy-6        | Tensor       | (1,)  | float32 |
steps/observation/dummy-7        | Tensor       | (1,)  | float32 |
steps/observation/dummy-8        | Tensor       | (1,)  | float32 |
steps/observation/dummy-9        | Tensor       | (1,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_easy_20_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_easy_40_percent

*   **Dataset size**: `3.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/dummy-0        | Tensor       | (1,)  | float32 |
steps/observation/dummy-1        | Tensor       | (1,)  | float32 |
steps/observation/dummy-2        | Tensor       | (1,)  | float32 |
steps/observation/dummy-3        | Tensor       | (1,)  | float32 |
steps/observation/dummy-4        | Tensor       | (1,)  | float32 |
steps/observation/dummy-5        | Tensor       | (1,)  | float32 |
steps/observation/dummy-6        | Tensor       | (1,)  | float32 |
steps/observation/dummy-7        | Tensor       | (1,)  | float32 |
steps/observation/dummy-8        | Tensor       | (1,)  | float32 |
steps/observation/dummy-9        | Tensor       | (1,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_easy_40_percent-1.0.1.html";
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

## rlu_rwrl/humanoid_walk_combined_challenge_easy_100_percent

*   **Dataset size**: `7.53 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_return': float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': Tensor(shape=(1,), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=float32),
            'dummy-0': Tensor(shape=(1,), dtype=float32),
            'dummy-1': Tensor(shape=(1,), dtype=float32),
            'dummy-2': Tensor(shape=(1,), dtype=float32),
            'dummy-3': Tensor(shape=(1,), dtype=float32),
            'dummy-4': Tensor(shape=(1,), dtype=float32),
            'dummy-5': Tensor(shape=(1,), dtype=float32),
            'dummy-6': Tensor(shape=(1,), dtype=float32),
            'dummy-7': Tensor(shape=(1,), dtype=float32),
            'dummy-8': Tensor(shape=(1,), dtype=float32),
            'dummy-9': Tensor(shape=(1,), dtype=float32),
            'extremities': Tensor(shape=(12,), dtype=float32),
            'head_height': Tensor(shape=(1,), dtype=float32),
            'joint_angles': Tensor(shape=(21,), dtype=float32),
            'torso_vertical': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(27,), dtype=float32),
        }),
        'reward': Tensor(shape=(1,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_return                   | Tensor       |       | float32 |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       | (1,)  | float32 |
steps/is_first                   | Tensor       |       | bool    |
steps/is_last                    | Tensor       |       | bool    |
steps/is_terminal                | Tensor       |       | bool    |
steps/observation                | FeaturesDict |       |         |
steps/observation/com_velocity   | Tensor       | (3,)  | float32 |
steps/observation/dummy-0        | Tensor       | (1,)  | float32 |
steps/observation/dummy-1        | Tensor       | (1,)  | float32 |
steps/observation/dummy-2        | Tensor       | (1,)  | float32 |
steps/observation/dummy-3        | Tensor       | (1,)  | float32 |
steps/observation/dummy-4        | Tensor       | (1,)  | float32 |
steps/observation/dummy-5        | Tensor       | (1,)  | float32 |
steps/observation/dummy-6        | Tensor       | (1,)  | float32 |
steps/observation/dummy-7        | Tensor       | (1,)  | float32 |
steps/observation/dummy-8        | Tensor       | (1,)  | float32 |
steps/observation/dummy-9        | Tensor       | (1,)  | float32 |
steps/observation/extremities    | Tensor       | (12,) | float32 |
steps/observation/head_height    | Tensor       | (1,)  | float32 |
steps/observation/joint_angles   | Tensor       | (21,) | float32 |
steps/observation/torso_vertical | Tensor       | (3,)  | float32 |
steps/observation/velocity       | Tensor       | (27,) | float32 |
steps/reward                     | Tensor       | (1,)  | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_rwrl-humanoid_walk_combined_challenge_easy_100_percent-1.0.1.html";
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