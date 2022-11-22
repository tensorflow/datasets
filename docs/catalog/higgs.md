<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="higgs" />
  <meta itemprop="description" content="The data has been produced using Monte Carlo simulations.&#10;The first 21 features (columns 2-22) are kinematic properties&#10;measured by the particle detectors in the accelerator.&#10;The last seven features are functions of the first 21 features;&#10;these are high-level features derived by physicists to help&#10;discriminate between the two classes. There is an interest&#10;in using deep learning methods to obviate the need for physicists&#10;to manually develop such features. Benchmark results using&#10;Bayesian Decision Trees from a standard physics package and&#10;5-layer neural networks are presented in the original paper.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;higgs&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/higgs" />
  <meta itemprop="sameAs" content="https://archive.ics.uci.edu/ml/datasets/HIGGS" />
  <meta itemprop="citation" content="@article{Baldi:2014kfa,&#10;      author         = &quot;Baldi, Pierre and Sadowski, Peter and Whiteson, Daniel&quot;,&#10;      title          = &quot;{Searching for Exotic Particles in High-Energy Physics&#10;                        with Deep Learning}&quot;,&#10;      journal        = &quot;Nature Commun.&quot;,&#10;      volume         = &quot;5&quot;,&#10;      year           = &quot;2014&quot;,&#10;      pages          = &quot;4308&quot;,&#10;      doi            = &quot;10.1038/ncomms5308&quot;,&#10;      eprint         = &quot;1402.4735&quot;,&#10;      archivePrefix  = &quot;arXiv&quot;,&#10;      primaryClass   = &quot;hep-ph&quot;,&#10;      SLACcitation   = &quot;%%CITATION = ARXIV:1402.4735;%%&quot;&#10;}" />
</div>

# `higgs`


*   **Description**:

The data has been produced using Monte Carlo simulations. The first 21 features
(columns 2-22) are kinematic properties measured by the particle detectors in
the accelerator. The last seven features are functions of the first 21 features;
these are high-level features derived by physicists to help discriminate between
the two classes. There is an interest in using deep learning methods to obviate
the need for physicists to manually develop such features. Benchmark results
using Bayesian Decision Trees from a standard physics package and 5-layer neural
networks are presented in the original paper.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/higgs-data-set">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://archive.ics.uci.edu/ml/datasets/HIGGS](https://archive.ics.uci.edu/ml/datasets/HIGGS)

*   **Source code**:
    [`tfds.structured.Higgs`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/higgs.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `2.62 GiB`

*   **Dataset size**: `6.88 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 11,000,000

*   **Feature structure**:

```python
FeaturesDict({
    'class_label': float32,
    'jet_1_b-tag': float64,
    'jet_1_eta': float64,
    'jet_1_phi': float64,
    'jet_1_pt': float64,
    'jet_2_b-tag': float64,
    'jet_2_eta': float64,
    'jet_2_phi': float64,
    'jet_2_pt': float64,
    'jet_3_b-tag': float64,
    'jet_3_eta': float64,
    'jet_3_phi': float64,
    'jet_3_pt': float64,
    'jet_4_b-tag': float64,
    'jet_4_eta': float64,
    'jet_4_phi': float64,
    'jet_4_pt': float64,
    'lepton_eta': float64,
    'lepton_pT': float64,
    'lepton_phi': float64,
    'm_bb': float64,
    'm_jj': float64,
    'm_jjj': float64,
    'm_jlv': float64,
    'm_lv': float64,
    'm_wbb': float64,
    'm_wwbb': float64,
    'missing_energy_magnitude': float64,
    'missing_energy_phi': float64,
})
```

*   **Feature documentation**:

Feature                  | Class        | Shape | Dtype   | Description
:----------------------- | :----------- | :---- | :------ | :----------
                         | FeaturesDict |       |         |
class_label              | Tensor       |       | float32 |
jet_1_b-tag              | Tensor       |       | float64 |
jet_1_eta                | Tensor       |       | float64 |
jet_1_phi                | Tensor       |       | float64 |
jet_1_pt                 | Tensor       |       | float64 |
jet_2_b-tag              | Tensor       |       | float64 |
jet_2_eta                | Tensor       |       | float64 |
jet_2_phi                | Tensor       |       | float64 |
jet_2_pt                 | Tensor       |       | float64 |
jet_3_b-tag              | Tensor       |       | float64 |
jet_3_eta                | Tensor       |       | float64 |
jet_3_phi                | Tensor       |       | float64 |
jet_3_pt                 | Tensor       |       | float64 |
jet_4_b-tag              | Tensor       |       | float64 |
jet_4_eta                | Tensor       |       | float64 |
jet_4_phi                | Tensor       |       | float64 |
jet_4_pt                 | Tensor       |       | float64 |
lepton_eta               | Tensor       |       | float64 |
lepton_pT                | Tensor       |       | float64 |
lepton_phi               | Tensor       |       | float64 |
m_bb                     | Tensor       |       | float64 |
m_jj                     | Tensor       |       | float64 |
m_jjj                    | Tensor       |       | float64 |
m_jlv                    | Tensor       |       | float64 |
m_lv                     | Tensor       |       | float64 |
m_wbb                    | Tensor       |       | float64 |
m_wwbb                   | Tensor       |       | float64 |
missing_energy_magnitude | Tensor       |       | float64 |
missing_energy_phi       | Tensor       |       | float64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/higgs-2.0.0.html";
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

*   **Citation**:

```
@article{Baldi:2014kfa,
      author         = "Baldi, Pierre and Sadowski, Peter and Whiteson, Daniel",
      title          = "{Searching for Exotic Particles in High-Energy Physics
                        with Deep Learning}",
      journal        = "Nature Commun.",
      volume         = "5",
      year           = "2014",
      pages          = "4308",
      doi            = "10.1038/ncomms5308",
      eprint         = "1402.4735",
      archivePrefix  = "arXiv",
      primaryClass   = "hep-ph",
      SLACcitation   = "%%CITATION = ARXIV:1402.4735;%%"
}
```

