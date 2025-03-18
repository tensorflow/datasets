<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="qm9" />
  <meta itemprop="description" content="QM9 consists of computed geometric, energetic, electronic, and thermodynamic&#10;properties for 134k stable small organic molecules made up of C, H, O, N, and F.&#10;As usual, we remove the uncharacterized molecules and provide the remaining&#10;130,831.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;qm9&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/qm9" />
  <meta itemprop="sameAs" content="https://doi.org/10.6084/m9.figshare.c.978904.v5" />
  <meta itemprop="citation" content="@article{ramakrishnan2014quantum,&#10;  title={Quantum chemistry structures and properties of 134 kilo molecules},&#10;  author={Ramakrishnan, Raghunathan and Dral, Pavlo O and Rupp, Matthias and von Lilienfeld, O Anatole},&#10;  journal={Scientific Data},&#10;  volume={1},&#10;  year={2014},&#10;  publisher={Nature Publishing Group}&#10;}" />
</div>

# `qm9`


*   **Description**:

QM9 consists of computed geometric, energetic, electronic, and thermodynamic
properties for 134k stable small organic molecules made up of C, H, O, N, and F.
As usual, we remove the uncharacterized molecules and provide the remaining
130,831.

*   **Homepage**:
    [https://doi.org/10.6084/m9.figshare.c.978904.v5](https://doi.org/10.6084/m9.figshare.c.978904.v5)

*   **Source code**:
    [`tfds.datasets.qm9.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/qm9/qm9_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `82.62 MiB`

*   **Dataset size**: `177.16 MiB`

*   **Feature structure**:

```python
FeaturesDict({
    'A': float32,
    'B': float32,
    'C': float32,
    'Cv': float32,
    'G': float32,
    'G_atomization': float32,
    'H': float32,
    'H_atomization': float32,
    'InChI': string,
    'InChI_relaxed': string,
    'Mulliken_charges': Tensor(shape=(29,), dtype=float32),
    'SMILES': string,
    'SMILES_relaxed': string,
    'U': float32,
    'U0': float32,
    'U0_atomization': float32,
    'U_atomization': float32,
    'alpha': float32,
    'charges': Tensor(shape=(29,), dtype=int64),
    'frequencies': Tensor(shape=(None,), dtype=float32),
    'gap': float32,
    'homo': float32,
    'index': int64,
    'lumo': float32,
    'mu': float32,
    'num_atoms': int64,
    'positions': Tensor(shape=(29, 3), dtype=float32),
    'r2': float32,
    'tag': string,
    'zpve': float32,
})
```

*   **Feature documentation**:

Feature          | Class        | Shape   | Dtype   | Description
:--------------- | :----------- | :------ | :------ | :----------
                 | FeaturesDict |         |         |
A                | Tensor       |         | float32 |
B                | Tensor       |         | float32 |
C                | Tensor       |         | float32 |
Cv               | Tensor       |         | float32 |
G                | Tensor       |         | float32 |
G_atomization    | Tensor       |         | float32 |
H                | Tensor       |         | float32 |
H_atomization    | Tensor       |         | float32 |
InChI            | Tensor       |         | string  |
InChI_relaxed    | Tensor       |         | string  |
Mulliken_charges | Tensor       | (29,)   | float32 |
SMILES           | Tensor       |         | string  |
SMILES_relaxed   | Tensor       |         | string  |
U                | Tensor       |         | float32 |
U0               | Tensor       |         | float32 |
U0_atomization   | Tensor       |         | float32 |
U_atomization    | Tensor       |         | float32 |
alpha            | Tensor       |         | float32 |
charges          | Tensor       | (29,)   | int64   |
frequencies      | Tensor       | (None,) | float32 |
gap              | Tensor       |         | float32 |
homo             | Tensor       |         | float32 |
index            | Tensor       |         | int64   |
lumo             | Tensor       |         | float32 |
mu               | Tensor       |         | float32 |
num_atoms        | Tensor       |         | int64   |
positions        | Tensor       | (29, 3) | float32 |
r2               | Tensor       |         | float32 |
tag              | Tensor       |         | string  |
zpve             | Tensor       |         | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{ramakrishnan2014quantum,
  title={Quantum chemistry structures and properties of 134 kilo molecules},
  author={Ramakrishnan, Raghunathan and Dral, Pavlo O and Rupp, Matthias and von Lilienfeld, O Anatole},
  journal={Scientific Data},
  volume={1},
  year={2014},
  publisher={Nature Publishing Group}
}
```


## qm9/original (default config)

*   **Config description**: QM9 does not define any splits. So this variant puts
    the full QM9 dataset in the train split, in the original order (no
    shuffling).

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 130,831

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/qm9-original-1.0.0.html";
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

## qm9/cormorant

*   **Config description**: Dataset split used by Cormorant. 100,000 train,
    17,748 validation, and 13,083 test samples. Splitting happens after
    shuffling with seed 0. Paper: https://arxiv.org/abs/1906.04015. Split:
    https://github.com/risilab/cormorant/blob/master/src/cormorant/data/prepare/qm9.py

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 13,083
`'train'`      | 100,000
`'validation'` | 17,748

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/qm9-cormorant-1.0.0.html";
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

## qm9/dimenet

*   **Config description**: Dataset split used by DimeNet. 110,000 train, 10,000
    validation, and 10,831 test samples. Splitting happens after shuffling with
    seed 42. Paper: https://arxiv.org/abs/2003.03123. Split:
    https://github.com/gasteigerjo/dimenet/blob/master/dimenet/training/data_provider.py

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,831
`'train'`      | 110,000
`'validation'` | 10,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/qm9-dimenet-1.0.0.html";
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