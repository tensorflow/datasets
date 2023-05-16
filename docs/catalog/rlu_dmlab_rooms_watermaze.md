<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rlu_dmlab_rooms_watermaze" />
  <meta itemprop="description" content="RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL&#10;Unplugged is designed around the following considerations: to facilitate ease of&#10;use, we provide the datasets with a unified API which makes it easy for the&#10;practitioner to work with all data in the suite once a general pipeline has been&#10;established.&#10;&#10;The datasets follow the [RLDS format](https://github.com/google-research/rlds)&#10;to represent steps and episodes.&#10;&#10;&#10;DeepMind Lab dataset has several levels from the challenging, partially&#10;observable [Deepmind Lab suite](https://github.com/deepmind/lab). DeepMind Lab&#10;dataset is collected by training distributed R2D2 by [Kapturowski et al., 2018]&#10;(https://openreview.net/forum?id=r1lyTjAqYX) agents from scratch on individual&#10;tasks. We recorded the experience across all actors during entire training runs&#10;a few times for every task. The details of the dataset generation process is&#10;described in [Gulcehre et al., 2021](https://arxiv.org/abs/2103.09575).&#10;&#10;We release datasets for five different DeepMind Lab levels: `seekavoid_arena_01`,&#10;`explore_rewards_few`, `explore_rewards_many`, `rooms_watermaze`,&#10;`rooms_select_nonmatching_object`. We also release the snapshot datasets for&#10;`seekavoid_arena_01` level that we generated the datasets from a trained R2D2&#10;snapshot with different levels of epsilons for the epsilon-greedy algorithm&#10;when evaluating the agent in the environment.&#10;&#10;DeepMind Lab dataset is fairly large-scale. We recommend you to try it if you&#10;are interested in large-scale offline RL models with memory.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rlu_dmlab_rooms_watermaze&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rlu_dmlab_rooms_watermaze" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged" />
  <meta itemprop="citation" content="@article{gulcehre2021rbve,&#10;    title={Regularized Behavior Value Estimation},&#10;    author={{\c{C}}aglar G{\&quot;{u}}l{\c{c}}ehre and&#10;               Sergio G{\&#x27;{o}}mez Colmenarejo and&#10;               Ziyu Wang and&#10;               Jakub Sygnowski and&#10;               Thomas Paine and&#10;               Konrad Zolna and&#10;               Yutian Chen and&#10;               Matthew W. Hoffman and&#10;               Razvan Pascanu and&#10;               Nando de Freitas},&#10;    year={2021},&#10;    journal   = {CoRR},&#10;    url       = {https://arxiv.org/abs/2103.09575},&#10;    eprint={2103.09575},&#10;    archivePrefix={arXiv},&#10;}" />
</div>

# `rlu_dmlab_rooms_watermaze`


*   **Description**:

RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

DeepMind Lab dataset has several levels from the challenging, partially
observable [Deepmind Lab suite](https://github.com/deepmind/lab). DeepMind Lab
dataset is collected by training distributed R2D2 by
[Kapturowski et al., 2018](https://openreview.net/forum?id=r1lyTjAqYX) agents
from scratch on individual tasks. We recorded the experience across all actors
during entire training runs a few times for every task. The details of the
dataset generation process is described in
[Gulcehre et al., 2021](https://arxiv.org/abs/2103.09575).

We release datasets for five different DeepMind Lab levels:
`seekavoid_arena_01`, `explore_rewards_few`, `explore_rewards_many`,
`rooms_watermaze`, `rooms_select_nonmatching_object`. We also release the
snapshot datasets for `seekavoid_arena_01` level that we generated the datasets
from a trained R2D2 snapshot with different levels of epsilons for the
epsilon-greedy algorithm when evaluating the agent in the environment.

DeepMind Lab dataset is fairly large-scale. We recommend you to try it if you
are interested in large-scale offline RL models with memory.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged)

*   **Source code**:
    [`tfds.rl_unplugged.rlu_dmlab_rooms_watermaze.RluDmlabRoomsWatermaze`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rl_unplugged/rlu_dmlab_rooms_watermaze/rlu_dmlab_rooms_watermaze.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.1.0`: Added is_last.
    *   **`1.2.0`** (default): BGR -> RGB fix for pixel observations.

*   **Download size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'episode_id': int64,
    'episode_return': float32,
    'steps': Dataset({
        'action': int64,
        'discount': float32,
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'last_action': int64,
            'last_reward': float32,
            'pixels': Image(shape=(72, 96, 3), dtype=uint8),
        }),
        'reward': float32,
    }),
})
```

*   **Feature documentation**:

| Feature                       | Class        | Shape | Dtype   | Description |
| :---------------------------- | :----------- | :---- | :------ | :---------- |
|                               | FeaturesDict |       |         |             |
| episode_id                    | Tensor       |       | int64   |             |
| episode_return                | Tensor       |       | float32 |             |
| steps                         | Dataset      |       |         |             |
| steps/action                  | Tensor       |       | int64   |             |
| steps/discount                | Tensor       |       | float32 |             |
| steps/is_first                | Tensor       |       | bool    |             |
| steps/is_last                 | Tensor       |       | bool    |             |
| steps/is_terminal             | Tensor       |       | bool    |             |
| steps/observation             | FeaturesDict |       |         |             |
| steps/observation/last_action | Tensor       |       | int64   |             |
| steps/observation/last_reward | Tensor       |       | float32 |             |
| steps/observation/pixels      | Image        | (72,  | uint8   |             |
:                               :              : 96,   :         :             :
:                               :              : 3)    :         :             :
| steps/reward                  | Tensor       |       | float32 |             |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{gulcehre2021rbve,
    title={Regularized Behavior Value Estimation},
    author={{\c{C}}aglar G{\"{u}}l{\c{c}}ehre and
               Sergio G{\'{o}}mez Colmenarejo and
               Ziyu Wang and
               Jakub Sygnowski and
               Thomas Paine and
               Konrad Zolna and
               Yutian Chen and
               Matthew W. Hoffman and
               Razvan Pascanu and
               Nando de Freitas},
    year={2021},
    journal   = {CoRR},
    url       = {https://arxiv.org/abs/2103.09575},
    eprint={2103.09575},
    archivePrefix={arXiv},
}
```


## rlu_dmlab_rooms_watermaze/training_0 (default config)

*   **Dataset size**: `894.50 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,876

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_dmlab_rooms_watermaze-training_0-1.2.0.html";
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

## rlu_dmlab_rooms_watermaze/training_1

*   **Dataset size**: `898.74 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,922

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_dmlab_rooms_watermaze-training_1-1.2.0.html";
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

## rlu_dmlab_rooms_watermaze/training_2

*   **Dataset size**: `825.49 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,081

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rlu_dmlab_rooms_watermaze-training_2-1.2.0.html";
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