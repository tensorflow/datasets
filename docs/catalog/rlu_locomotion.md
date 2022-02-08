<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rlu_locomotion" />
  <meta itemprop="description" content="RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL&#10;Unplugged is designed around the following considerations: to facilitate ease of&#10;use, we provide the datasets with a unified API which makes it easy for the&#10;practitioner to work with all data in the suite once a general pipeline has been&#10;established.&#10;&#10;&#10;These tasks are made up of the corridor locomotion tasks involving the CMU&#10;Humanoid, for which prior efforts have either used motion capture data&#10;[Merel et al., 2019a](https://arxiv.org/abs/1811.09656),&#10;[Merel et al., 2019b](https://arxiv.org/abs/1811.11711) or training from scratch&#10;[Song et al., 2020](https://arxiv.org/abs/1909.12238). In addition, the DM&#10;Locomotion repository contains a set of tasks adapted to be suited to a virtual&#10;rodent [Merel et al., 2020](https://arxiv.org/abs/1911.09451). We emphasize that&#10;the DM Locomotion tasks feature the combination of challenging high-DoF&#10;continuous control along with perception from rich egocentric observations.&#10;For details on how the dataset was generated, please refer to the paper.&#10;&#10;We recommend you to try offline RL methods on DeepMind Locomotion dataset, if&#10;you are interested in very challenging offline RL dataset with continuous action&#10;space.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rlu_locomotion&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rlu_locomotion" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged" />
  <meta itemprop="citation" content="@inproceedings{gulcehre2020rl,&#10; title = {RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning},&#10; author = {Gulcehre, Caglar and Wang, Ziyu and Novikov, Alexander and Paine, Thomas and G&#x27;{o}mez, Sergio and Zolna, Konrad and Agarwal, Rishabh and Merel, Josh S and Mankowitz, Daniel J and Paduraru, Cosmin and Dulac-Arnold, Gabriel and Li, Jerry and Norouzi, Mohammad and Hoffman, Matthew and Heess, Nicolas and de Freitas, Nando},&#10; booktitle = {Advances in Neural Information Processing Systems},&#10; pages = {7248--7259},&#10; volume = {33},&#10; year = {2020}&#10;}" />
</div>

# `rlu_locomotion`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

These tasks are made up of the corridor locomotion tasks involving the CMU
Humanoid, for which prior efforts have either used motion capture data
[Merel et al., 2019a](https://arxiv.org/abs/1811.09656),
[Merel et al., 2019b](https://arxiv.org/abs/1811.11711) or training from scratch
[Song et al., 2020](https://arxiv.org/abs/1909.12238). In addition, the DM
Locomotion repository contains a set of tasks adapted to be suited to a virtual
rodent [Merel et al., 2020](https://arxiv.org/abs/1911.09451). We emphasize that
the DM Locomotion tasks feature the combination of challenging high-DoF
continuous control along with perception from rich egocentric observations. For
details on how the dataset was generated, please refer to the paper.

We recommend you to try offline RL methods on DeepMind Locomotion dataset, if
you are interested in very challenging offline RL dataset with continuous action
space.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged)

*   **Source code**:
    [`tfds.rl_unplugged.rlu_locomotion.RluLocomotion`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rl_unplugged/rlu_locomotion/rlu_locomotion.py)

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
@inproceedings{gulcehre2020rl,
 title = {RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning},
 author = {Gulcehre, Caglar and Wang, Ziyu and Novikov, Alexander and Paine, Thomas and G'{o}mez, Sergio and Zolna, Konrad and Agarwal, Rishabh and Merel, Josh S and Mankowitz, Daniel J and Paduraru, Cosmin and Dulac-Arnold, Gabriel and Li, Jerry and Norouzi, Mohammad and Hoffman, Matthew and Heess, Nicolas and de Freitas, Nando},
 booktitle = {Advances in Neural Information Processing Systems},
 pages = {7248--7259},
 volume = {33},
 year = {2020}
}
```


## rlu_locomotion/humanoid_corridor (default config)

*   **Dataset size**: `1.88 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(56,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'body_height': Tensor(shape=(1,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'end_effectors_pos': Tensor(shape=(12,), dtype=tf.float32),
                'joints_pos': Tensor(shape=(56,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(56,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-humanoid_corridor-1.0.0.html";
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

## rlu_locomotion/humanoid_gaps

*   **Dataset size**: `4.57 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(56,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'body_height': Tensor(shape=(1,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'end_effectors_pos': Tensor(shape=(12,), dtype=tf.float32),
                'joints_pos': Tensor(shape=(56,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(56,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-humanoid_gaps-1.0.0.html";
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

## rlu_locomotion/humanoid_walls

*   **Dataset size**: `2.36 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(56,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'body_height': Tensor(shape=(1,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'end_effectors_pos': Tensor(shape=(12,), dtype=tf.float32),
                'joints_pos': Tensor(shape=(56,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(56,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-humanoid_walls-1.0.0.html";
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

## rlu_locomotion/rodent_bowl_escape

*   **Dataset size**: `16.46 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(38,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'appendages_pos': Tensor(shape=(15,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'joints_pos': Tensor(shape=(30,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(30,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_touch': Tensor(shape=(4,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'tendons_pos': Tensor(shape=(8,), dtype=tf.float32),
                'tendons_vel': Tensor(shape=(8,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-rodent_bowl_escape-1.0.0.html";
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

## rlu_locomotion/rodent_gaps

*   **Dataset size**: `8.90 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(38,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'appendages_pos': Tensor(shape=(15,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'joints_pos': Tensor(shape=(30,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(30,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_touch': Tensor(shape=(4,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'tendons_pos': Tensor(shape=(8,), dtype=tf.float32),
                'tendons_vel': Tensor(shape=(8,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-rodent_gaps-1.0.0.html";
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

## rlu_locomotion/rodent_mazes

*   **Dataset size**: `20.71 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(38,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'appendages_pos': Tensor(shape=(15,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'joints_pos': Tensor(shape=(30,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(30,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_touch': Tensor(shape=(4,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'tendons_pos': Tensor(shape=(8,), dtype=tf.float32),
                'tendons_vel': Tensor(shape=(8,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-rodent_mazes-1.0.0.html";
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

## rlu_locomotion/rodent_two_touch

*   **Dataset size**: `23.05 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'steps': Dataset({
        'action': Tensor(shape=(38,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'walker': FeaturesDict({
                'appendages_pos': Tensor(shape=(15,), dtype=tf.float32),
                'egocentric_camera': Image(shape=(64, 64, 3), dtype=tf.uint8),
                'joints_pos': Tensor(shape=(30,), dtype=tf.float32),
                'joints_vel': Tensor(shape=(30,), dtype=tf.float32),
                'sensors_accelerometer': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_gyro': Tensor(shape=(3,), dtype=tf.float32),
                'sensors_touch': Tensor(shape=(4,), dtype=tf.float32),
                'sensors_velocimeter': Tensor(shape=(3,), dtype=tf.float32),
                'tendons_pos': Tensor(shape=(8,), dtype=tf.float32),
                'tendons_vel': Tensor(shape=(8,), dtype=tf.float32),
                'world_zaxis': Tensor(shape=(3,), dtype=tf.float32),
            }),
        }),
        'reward': tf.float32,
    }),
    'timestamp': tf.int64,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_locomotion-rodent_two_touch-1.0.0.html";
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