<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="nsynth" />
  <meta itemprop="description" content="The NSynth Dataset is an audio dataset containing ~300k musical notes, each with&#10;a unique pitch, timbre, and envelope. Each note is annotated with three&#10;additional pieces of information based on a combination of human evaluation and&#10;heuristic algorithms: Source, Family, and Qualities.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;nsynth&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nsynth" />
  <meta itemprop="sameAs" content="https://g.co/magenta/nsynth-dataset" />
  <meta itemprop="citation" content="@InProceedings{pmlr-v70-engel17a,&#10;  title =     {Neural Audio Synthesis of Musical Notes with {W}ave{N}et Autoencoders},&#10;  author =     {Jesse Engel and Cinjon Resnick and Adam Roberts and Sander Dieleman and Mohammad Norouzi and Douglas Eck and Karen Simonyan},&#10;  booktitle =    {Proceedings of the 34th International Conference on Machine Learning},&#10;  pages =   {1068--1077},&#10;  year =      {2017},&#10;  editor =      {Doina Precup and Yee Whye Teh},&#10;  volume =     {70},&#10;  series =    {Proceedings of Machine Learning Research},&#10;  address =     {International Convention Centre, Sydney, Australia},&#10;  month =     {06--11 Aug},&#10;  publisher =     {PMLR},&#10;  pdf =     {http://proceedings.mlr.press/v70/engel17a/engel17a.pdf},&#10;  url =   {http://proceedings.mlr.press/v70/engel17a.html},&#10;}" />
</div>

# `nsynth`


*   **Description**:

The NSynth Dataset is an audio dataset containing ~300k musical notes, each with
a unique pitch, timbre, and envelope. Each note is annotated with three
additional pieces of information based on a combination of human evaluation and
heuristic algorithms: Source, Family, and Qualities.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/nsynth">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)

*   **Source code**:
    [`tfds.datasets.nsynth.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/nsynth/nsynth_dataset_builder.py)

*   **Versions**:

    *   `2.3.0`: New `loudness_db` feature in decibels (unormalized).
    *   `2.3.1`: F0 computed with normalization fix in CREPE.
    *   `2.3.2`: Use Audio feature.
    *   **`2.3.3`** (default): F0 computed with fix in CREPE wave normalization
        (https://github.com/marl/crepe/issues/49).

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
@InProceedings{pmlr-v70-engel17a,
  title =    {Neural Audio Synthesis of Musical Notes with {W}ave{N}et Autoencoders},
  author =   {Jesse Engel and Cinjon Resnick and Adam Roberts and Sander Dieleman and Mohammad Norouzi and Douglas Eck and Karen Simonyan},
  booktitle =    {Proceedings of the 34th International Conference on Machine Learning},
  pages =    {1068--1077},
  year =     {2017},
  editor =   {Doina Precup and Yee Whye Teh},
  volume =   {70},
  series =   {Proceedings of Machine Learning Research},
  address =      {International Convention Centre, Sydney, Australia},
  month =    {06--11 Aug},
  publisher =    {PMLR},
  pdf =      {http://proceedings.mlr.press/v70/engel17a/engel17a.pdf},
  url =      {http://proceedings.mlr.press/v70/engel17a.html},
}
```


## nsynth/full (default config)

*   **Config description**: Full NSynth Dataset is split into train, valid, and
    test sets, with no instruments overlapping between the train set and the
    valid/test sets.

*   **Download size**: `73.07 GiB`

*   **Dataset size**: `73.09 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 4,096
`'train'` | 289,205
`'valid'` | 12,678

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(64000,), dtype=float32),
    'id': string,
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=3),
    }),
    'pitch': ClassLabel(shape=(), dtype=int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': bool,
        'dark': bool,
        'distortion': bool,
        'fast_decay': bool,
        'long_release': bool,
        'multiphonic': bool,
        'nonlinear_env': bool,
        'percussive': bool,
        'reverb': bool,
        'tempo-synced': bool,
    }),
    'velocity': ClassLabel(shape=(), dtype=int64, num_classes=128),
})
```

*   **Feature documentation**:

Feature                 | Class        | Shape    | Dtype   | Description
:---------------------- | :----------- | :------- | :------ | :----------
                        | FeaturesDict |          |         |
audio                   | Audio        | (64000,) | float32 |
id                      | Tensor       |          | string  |
instrument              | FeaturesDict |          |         |
instrument/family       | ClassLabel   |          | int64   |
instrument/label        | ClassLabel   |          | int64   |
instrument/source       | ClassLabel   |          | int64   |
pitch                   | ClassLabel   |          | int64   |
qualities               | FeaturesDict |          |         |
qualities/bright        | Tensor       |          | bool    |
qualities/dark          | Tensor       |          | bool    |
qualities/distortion    | Tensor       |          | bool    |
qualities/fast_decay    | Tensor       |          | bool    |
qualities/long_release  | Tensor       |          | bool    |
qualities/multiphonic   | Tensor       |          | bool    |
qualities/nonlinear_env | Tensor       |          | bool    |
qualities/percussive    | Tensor       |          | bool    |
qualities/reverb        | Tensor       |          | bool    |
qualities/tempo-synced  | Tensor       |          | bool    |
velocity                | ClassLabel   |          | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/nsynth-full-2.3.3.html";
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

## nsynth/gansynth_subset

*   **Config description**: NSynth Dataset limited to acoustic instruments in
    the MIDI pitch interval [24, 84]. Uses alternate splits that have overlap in
    instruments (but not exact notes) between the train set and valid/test sets.
    This variant was originally introduced in the ICLR 2019 GANSynth paper
    (https://arxiv.org/abs/1902.08710).

*   **Download size**: `73.08 GiB`

*   **Dataset size**: `20.73 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 8,518
`'train'` | 60,788
`'valid'` | 17,469

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(64000,), dtype=float32),
    'id': string,
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=3),
    }),
    'pitch': ClassLabel(shape=(), dtype=int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': bool,
        'dark': bool,
        'distortion': bool,
        'fast_decay': bool,
        'long_release': bool,
        'multiphonic': bool,
        'nonlinear_env': bool,
        'percussive': bool,
        'reverb': bool,
        'tempo-synced': bool,
    }),
    'velocity': ClassLabel(shape=(), dtype=int64, num_classes=128),
})
```

*   **Feature documentation**:

Feature                 | Class        | Shape    | Dtype   | Description
:---------------------- | :----------- | :------- | :------ | :----------
                        | FeaturesDict |          |         |
audio                   | Audio        | (64000,) | float32 |
id                      | Tensor       |          | string  |
instrument              | FeaturesDict |          |         |
instrument/family       | ClassLabel   |          | int64   |
instrument/label        | ClassLabel   |          | int64   |
instrument/source       | ClassLabel   |          | int64   |
pitch                   | ClassLabel   |          | int64   |
qualities               | FeaturesDict |          |         |
qualities/bright        | Tensor       |          | bool    |
qualities/dark          | Tensor       |          | bool    |
qualities/distortion    | Tensor       |          | bool    |
qualities/fast_decay    | Tensor       |          | bool    |
qualities/long_release  | Tensor       |          | bool    |
qualities/multiphonic   | Tensor       |          | bool    |
qualities/nonlinear_env | Tensor       |          | bool    |
qualities/percussive    | Tensor       |          | bool    |
qualities/reverb        | Tensor       |          | bool    |
qualities/tempo-synced  | Tensor       |          | bool    |
velocity                | ClassLabel   |          | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/nsynth-gansynth_subset-2.3.3.html";
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

## nsynth/gansynth_subset.f0_and_loudness

*   **Config description**: NSynth Dataset limited to acoustic instruments in
    the MIDI pitch interval [24, 84]. Uses alternate splits that have overlap in
    instruments (but not exact notes) between the train set and valid/test sets.
    This variant was originally introduced in the ICLR 2019 GANSynth paper
    (https://arxiv.org/abs/1902.08710). This version additionally contains
    estimates for F0 using CREPE (Kim et al., 2018) and A-weighted perceptual
    loudness in decibels. Both signals are provided at a frame rate of 250Hz.

*   **Download size**: `73.08 GiB`

*   **Dataset size**: `22.03 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 8,518
`'train'` | 60,788
`'valid'` | 17,469

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(64000,), dtype=float32),
    'f0': FeaturesDict({
        'confidence': Tensor(shape=(1000,), dtype=float32),
        'hz': Tensor(shape=(1000,), dtype=float32),
        'midi': Tensor(shape=(1000,), dtype=float32),
    }),
    'id': string,
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=3),
    }),
    'loudness': FeaturesDict({
        'db': Tensor(shape=(1000,), dtype=float32),
    }),
    'pitch': ClassLabel(shape=(), dtype=int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': bool,
        'dark': bool,
        'distortion': bool,
        'fast_decay': bool,
        'long_release': bool,
        'multiphonic': bool,
        'nonlinear_env': bool,
        'percussive': bool,
        'reverb': bool,
        'tempo-synced': bool,
    }),
    'velocity': ClassLabel(shape=(), dtype=int64, num_classes=128),
})
```

*   **Feature documentation**:

Feature                 | Class        | Shape    | Dtype   | Description
:---------------------- | :----------- | :------- | :------ | :----------
                        | FeaturesDict |          |         |
audio                   | Audio        | (64000,) | float32 |
f0                      | FeaturesDict |          |         |
f0/confidence           | Tensor       | (1000,)  | float32 |
f0/hz                   | Tensor       | (1000,)  | float32 |
f0/midi                 | Tensor       | (1000,)  | float32 |
id                      | Tensor       |          | string  |
instrument              | FeaturesDict |          |         |
instrument/family       | ClassLabel   |          | int64   |
instrument/label        | ClassLabel   |          | int64   |
instrument/source       | ClassLabel   |          | int64   |
loudness                | FeaturesDict |          |         |
loudness/db             | Tensor       | (1000,)  | float32 |
pitch                   | ClassLabel   |          | int64   |
qualities               | FeaturesDict |          |         |
qualities/bright        | Tensor       |          | bool    |
qualities/dark          | Tensor       |          | bool    |
qualities/distortion    | Tensor       |          | bool    |
qualities/fast_decay    | Tensor       |          | bool    |
qualities/long_release  | Tensor       |          | bool    |
qualities/multiphonic   | Tensor       |          | bool    |
qualities/nonlinear_env | Tensor       |          | bool    |
qualities/percussive    | Tensor       |          | bool    |
qualities/reverb        | Tensor       |          | bool    |
qualities/tempo-synced  | Tensor       |          | bool    |
velocity                | ClassLabel   |          | int64   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/nsynth-gansynth_subset.f0_and_loudness-2.3.3.html";
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