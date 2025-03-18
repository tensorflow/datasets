<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rlu_control_suite" />
  <meta itemprop="description" content="RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL&#10;Unplugged is designed around the following considerations: to facilitate ease of&#10;use, we provide the datasets with a unified API which makes it easy for the&#10;practitioner to work with all data in the suite once a general pipeline has been&#10;established.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;&#10;DeepMind Control Suite [Tassa et al., 2018](https://arxiv.org/abs/1801.00690)&#10;is a set of control tasks implemented in MuJoCo&#10;[Todorov et al., 2012](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf).&#10;We consider a subset of the tasks provided in the suite that cover a wide range&#10;of difficulties.&#10;&#10;Most of the datasets in this domain are generated using D4PG. For the&#10;environments Manipulator insert ball and Manipulator insert peg we use V-MPO&#10;[Song et al., 2020](https://arxiv.org/abs/1909.12238) to generate the data as&#10;D4PG is unable to solve these tasks. We release datasets for 9 control suite&#10;tasks. For details on how the dataset was generated, please refer to the paper.&#10;&#10;DeepMind Control Suite is a traditional continuous action RL benchmark.&#10;In particular, we recommend you test your approach in DeepMind Control Suite if&#10;you are interested in comparing against other state of the art offline RL&#10;methods.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rlu_control_suite&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rlu_control_suite" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged" />
  <meta itemprop="citation" content="@inproceedings{gulcehre2020rl,&#10; title = {RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning},&#10; author = {Gulcehre, Caglar and Wang, Ziyu and Novikov, Alexander and Paine, Thomas and G&#x27;{o}mez, Sergio and Zolna, Konrad and Agarwal, Rishabh and Merel, Josh S and Mankowitz, Daniel J and Paduraru, Cosmin and Dulac-Arnold, Gabriel and Li, Jerry and Norouzi, Mohammad and Hoffman, Matthew and Heess, Nicolas and de Freitas, Nando},&#10; booktitle = {Advances in Neural Information Processing Systems},&#10; pages = {7248--7259},&#10; volume = {33},&#10; year = {2020}&#10;}" />
</div>

# `rlu_control_suite`


*   **Description**:

RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

DeepMind Control Suite [Tassa et al., 2018](https://arxiv.org/abs/1801.00690) is
a set of control tasks implemented in MuJoCo
[Todorov et al., 2012](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf).
We consider a subset of the tasks provided in the suite that cover a wide range
of difficulties.

Most of the datasets in this domain are generated using D4PG. For the
environments Manipulator insert ball and Manipulator insert peg we use V-MPO
[Song et al., 2020](https://arxiv.org/abs/1909.12238) to generate the data as
D4PG is unable to solve these tasks. We release datasets for 9 control suite
tasks. For details on how the dataset was generated, please refer to the paper.

DeepMind Control Suite is a traditional continuous action RL benchmark. In
particular, we recommend you test your approach in DeepMind Control Suite if you
are interested in comparing against other state of the art offline RL methods.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged)

*   **Source code**:
    [`tfds.rl_unplugged.rlu_control_suite.RluControlSuite`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rl_unplugged/rlu_control_suite/rlu_control_suite.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{gulcehre2020rl,
 title = {RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning},
 author = {Gulcehre, Caglar and Wang, Ziyu and Novikov, Alexander and Paine, Thomas and G'{o}mez, Sergio and Zolna, Konrad and Agarwal, Rishabh and Merel, Josh S and Mankowitz, Daniel J and Paduraru, Cosmin and Dulac-Arnold, Gabriel and Li, Jerry and Norouzi, Mohammad and Hoffman, Matthew and Heess, Nicolas and de Freitas, Nando},
 booktitle = {Advances in Neural Information Processing Systems},
 pages = {7248--7259},
 volume = {33},
 year = {2020}
}
```


## rlu_control_suite/cartpole_swingup (default config)

*   **Dataset size**: `2.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 40

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=float32),
            'velocity': Tensor(shape=(2,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_id                 | Tensor       |       | int64   |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (1,)  | float32 |
steps/discount             | Tensor       |       | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (3,)  | float32 |
steps/observation/velocity | Tensor       | (2,)  | float32 |
steps/reward               | Tensor       |       | float32 |
timestamp                  | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-cartpole_swingup-1.0.0.html";
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

## rlu_control_suite/cheetah_run

*   **Dataset size**: `36.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 300

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(8,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape | Dtype   | Description
:------------------------- | :----------- | :---- | :------ | :----------
                           | FeaturesDict |       |         |
episode_id                 | Tensor       |       | int64   |
steps                      | Dataset      |       |         |
steps/action               | Tensor       | (6,)  | float32 |
steps/discount             | Tensor       |       | float32 |
steps/is_first             | Tensor       |       | bool    |
steps/is_last              | Tensor       |       | bool    |
steps/is_terminal          | Tensor       |       | bool    |
steps/observation          | FeaturesDict |       |         |
steps/observation/position | Tensor       | (8,)  | float32 |
steps/observation/velocity | Tensor       | (9,)  | float32 |
steps/reward               | Tensor       |       | float32 |
timestamp                  | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-cheetah_run-1.0.0.html";
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

## rlu_control_suite/finger_turn_hard

*   **Dataset size**: `47.61 MiB`

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
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(2,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'dist_to_target': Tensor(shape=(1,), dtype=float32),
            'position': Tensor(shape=(4,), dtype=float32),
            'target_position': Tensor(shape=(2,), dtype=float32),
            'velocity': Tensor(shape=(3,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                           | Class        | Shape | Dtype   | Description
:-------------------------------- | :----------- | :---- | :------ | :----------
                                  | FeaturesDict |       |         |
episode_id                        | Tensor       |       | int64   |
steps                             | Dataset      |       |         |
steps/action                      | Tensor       | (2,)  | float32 |
steps/discount                    | Tensor       |       | float32 |
steps/is_first                    | Tensor       |       | bool    |
steps/is_last                     | Tensor       |       | bool    |
steps/is_terminal                 | Tensor       |       | bool    |
steps/observation                 | FeaturesDict |       |         |
steps/observation/dist_to_target  | Tensor       | (1,)  | float32 |
steps/observation/position        | Tensor       | (4,)  | float32 |
steps/observation/target_position | Tensor       | (2,)  | float32 |
steps/observation/velocity        | Tensor       | (3,)  | float32 |
steps/reward                      | Tensor       |       | float32 |
timestamp                         | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-finger_turn_hard-1.0.0.html";
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

## rlu_control_suite/fish_swim

*   **Dataset size**: `32.81 MiB`

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
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(5,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'joint_angles': Tensor(shape=(7,), dtype=float32),
            'target': Tensor(shape=(3,), dtype=float32),
            'upright': Tensor(shape=(1,), dtype=float32),
            'velocity': Tensor(shape=(13,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_id                     | Tensor       |       | int64   |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (5,)  | float32 |
steps/discount                 | Tensor       |       | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/joint_angles | Tensor       | (7,)  | float32 |
steps/observation/target       | Tensor       | (3,)  | float32 |
steps/observation/upright      | Tensor       | (1,)  | float32 |
steps/observation/velocity     | Tensor       | (13,) | float32 |
steps/reward                   | Tensor       |       | float32 |
timestamp                      | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-fish_swim-1.0.0.html";
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

## rlu_control_suite/humanoid_run

*   **Dataset size**: `1.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,000

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=float32),
        'discount': float32,
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
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape | Dtype   | Description
:------------------------------- | :----------- | :---- | :------ | :----------
                                 | FeaturesDict |       |         |
episode_id                       | Tensor       |       | int64   |
steps                            | Dataset      |       |         |
steps/action                     | Tensor       | (21,) | float32 |
steps/discount                   | Tensor       |       | float32 |
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
steps/reward                     | Tensor       |       | float32 |
timestamp                        | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-humanoid_run-1.0.0.html";
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

## rlu_control_suite/manipulator_insert_ball

*   **Dataset size**: `385.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(5,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'arm_pos': Tensor(shape=(16,), dtype=float32),
            'arm_vel': Tensor(shape=(8,), dtype=float32),
            'hand_pos': Tensor(shape=(4,), dtype=float32),
            'object_pos': Tensor(shape=(4,), dtype=float32),
            'object_vel': Tensor(shape=(3,), dtype=float32),
            'target_pos': Tensor(shape=(4,), dtype=float32),
            'touch': Tensor(shape=(5,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
episode_id                   | Tensor       |       | int64   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (5,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | FeaturesDict |       |         |
steps/observation/arm_pos    | Tensor       | (16,) | float32 |
steps/observation/arm_vel    | Tensor       | (8,)  | float32 |
steps/observation/hand_pos   | Tensor       | (4,)  | float32 |
steps/observation/object_pos | Tensor       | (4,)  | float32 |
steps/observation/object_vel | Tensor       | (3,)  | float32 |
steps/observation/target_pos | Tensor       | (4,)  | float32 |
steps/observation/touch      | Tensor       | (5,)  | float32 |
steps/reward                 | Tensor       |       | float32 |
timestamp                    | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-manipulator_insert_ball-1.0.0.html";
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

## rlu_control_suite/manipulator_insert_peg

*   **Dataset size**: `385.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,500

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(5,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'arm_pos': Tensor(shape=(16,), dtype=float32),
            'arm_vel': Tensor(shape=(8,), dtype=float32),
            'hand_pos': Tensor(shape=(4,), dtype=float32),
            'object_pos': Tensor(shape=(4,), dtype=float32),
            'object_vel': Tensor(shape=(3,), dtype=float32),
            'target_pos': Tensor(shape=(4,), dtype=float32),
            'touch': Tensor(shape=(5,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                      | Class        | Shape | Dtype   | Description
:--------------------------- | :----------- | :---- | :------ | :----------
                             | FeaturesDict |       |         |
episode_id                   | Tensor       |       | int64   |
steps                        | Dataset      |       |         |
steps/action                 | Tensor       | (5,)  | float32 |
steps/discount               | Tensor       |       | float32 |
steps/is_first               | Tensor       |       | bool    |
steps/is_last                | Tensor       |       | bool    |
steps/is_terminal            | Tensor       |       | bool    |
steps/observation            | FeaturesDict |       |         |
steps/observation/arm_pos    | Tensor       | (16,) | float32 |
steps/observation/arm_vel    | Tensor       | (8,)  | float32 |
steps/observation/hand_pos   | Tensor       | (4,)  | float32 |
steps/observation/object_pos | Tensor       | (4,)  | float32 |
steps/observation/object_vel | Tensor       | (3,)  | float32 |
steps/observation/target_pos | Tensor       | (4,)  | float32 |
steps/observation/touch      | Tensor       | (5,)  | float32 |
steps/reward                 | Tensor       |       | float32 |
timestamp                    | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-manipulator_insert_peg-1.0.0.html";
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

## rlu_control_suite/walker_stand

*   **Dataset size**: `31.78 MiB`

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
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_id                     | Tensor       |       | int64   |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       |       | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       |       | float32 |
timestamp                      | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-walker_stand-1.0.0.html";
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

## rlu_control_suite/walker_walk

*   **Dataset size**: `31.78 MiB`

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
    'episode_id': int64,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32),
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=float32),
            'orientations': Tensor(shape=(14,), dtype=float32),
            'velocity': Tensor(shape=(9,), dtype=float32),
        }),
        'reward': float32,
    }),
    'timestamp': int64,
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
episode_id                     | Tensor       |       | int64   |
steps                          | Dataset      |       |         |
steps/action                   | Tensor       | (6,)  | float32 |
steps/discount                 | Tensor       |       | float32 |
steps/is_first                 | Tensor       |       | bool    |
steps/is_last                  | Tensor       |       | bool    |
steps/is_terminal              | Tensor       |       | bool    |
steps/observation              | FeaturesDict |       |         |
steps/observation/height       | Tensor       | (1,)  | float32 |
steps/observation/orientations | Tensor       | (14,) | float32 |
steps/observation/velocity     | Tensor       | (9,)  | float32 |
steps/reward                   | Tensor       |       | float32 |
timestamp                      | Tensor       |       | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_control_suite-walker_walk-1.0.0.html";
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