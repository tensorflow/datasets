<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="criteo" />
  <meta itemprop="description" content="# Criteo Uplift Modeling Dataset&#10;This dataset is released along with the paper:&#10;“A Large Scale Benchmark for Uplift Modeling”&#10;Eustache Diemert, Artem Betlei, Christophe Renaudin; (Criteo AI Lab), Massih-Reza Amini (LIG, Grenoble INP)&#10;&#10;This work was published in: AdKDD 2018 Workshop, in conjunction with KDD 2018.&#10;&#10;### Data description&#10;This dataset is constructed by assembling data resulting from several incrementality tests, a particular randomized trial procedure where a random part of the population is prevented from being targeted by advertising. it consists of 25M rows, each one representing a user with 11 features, a treatment indicator and 2 labels (visits and conversions).&#10;&#10;### Fields&#10;Here is a detailed description of the fields (they are comma-separated in the file):&#10;&#10;- f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11: feature values (dense, float)&#10;- treatment: treatment group (1 = treated, 0 = control)&#10;- conversion: whether a conversion occured for this user (binary, label)&#10;- visit: whether a visit occured for this user (binary, label)&#10;- exposure: treatment effect, whether the user has been effectively exposed (binary)&#10;&#10;### Key figures&#10;&#10;- Format: CSV&#10;- Size: 459MB (compressed)&#10;- Rows: 25,309,483&#10;- Average Visit Rate: .04132&#10;- Average Conversion Rate: .00229&#10;- Treatment Ratio: .846&#10;&#10;### Tasks&#10;&#10;The dataset was collected and prepared with uplift prediction in mind as the main task. Additionally we can foresee related usages such as but not limited to:&#10;&#10;- benchmark for causal inference&#10;- uplift modeling&#10;- interactions between features and treatment&#10;- heterogeneity of treatment&#10;- benchmark for observational causality methods&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;criteo&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/criteo" />
  <meta itemprop="sameAs" content="https://ailab.criteo.com/criteo-uplift-prediction-dataset/" />
  <meta itemprop="citation" content="@inproceedings{Diemert2018,&#10;author = {{Diemert Eustache, Betlei Artem} and Renaudin, Christophe and Massih-Reza, Amini},&#10;title={A Large Scale Benchmark for Uplift Modeling},&#10;publisher = {ACM},&#10;booktitle = {Proceedings of the AdKDD and TargetAd Workshop, KDD, London,United Kingdom, August, 20, 2018},&#10;year = {2018}&#10;}" />
</div>

# `criteo`


*   **Description**:

# Criteo Uplift Modeling Dataset

This dataset is released along with the paper: “A Large Scale Benchmark for
Uplift Modeling” Eustache Diemert, Artem Betlei, Christophe Renaudin; (Criteo AI
Lab), Massih-Reza Amini (LIG, Grenoble INP)

This work was published in: AdKDD 2018 Workshop, in conjunction with KDD 2018.

### Data description

This dataset is constructed by assembling data resulting from several
incrementality tests, a particular randomized trial procedure where a random
part of the population is prevented from being targeted by advertising. it
consists of 25M rows, each one representing a user with 11 features, a treatment
indicator and 2 labels (visits and conversions).

### Fields

Here is a detailed description of the fields (they are comma-separated in the
file):

-   f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11: feature values (dense,
    float)
-   treatment: treatment group (1 = treated, 0 = control)
-   conversion: whether a conversion occured for this user (binary, label)
-   visit: whether a visit occured for this user (binary, label)
-   exposure: treatment effect, whether the user has been effectively exposed
    (binary)

### Key figures

-   Format: CSV
-   Size: 459MB (compressed)
-   Rows: 25,309,483
-   Average Visit Rate: .04132
-   Average Conversion Rate: .00229
-   Treatment Ratio: .846

### Tasks

The dataset was collected and prepared with uplift prediction in mind as the
main task. Additionally we can foresee related usages such as but not limited
to:

-   benchmark for causal inference
-   uplift modeling
-   interactions between features and treatment
-   heterogeneity of treatment
-   benchmark for observational causality methods

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/criteo">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://ailab.criteo.com/criteo-uplift-prediction-dataset/](https://ailab.criteo.com/criteo-uplift-prediction-dataset/)

*   **Source code**:
    [`tfds.recommendation.criteo.Criteo`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/recommendation/criteo/criteo.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Fixed parsing of fields `conversion`, `visit` and
        `exposure`.

*   **Download size**: `297.00 MiB`

*   **Dataset size**: `3.55 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 13,979,592

*   **Feature structure**:

```python
FeaturesDict({
    'conversion': bool,
    'exposure': bool,
    'f0': float32,
    'f1': float32,
    'f10': float32,
    'f11': float32,
    'f2': float32,
    'f3': float32,
    'f4': float32,
    'f5': float32,
    'f6': float32,
    'f7': float32,
    'f8': float32,
    'f9': float32,
    'treatment': int64,
    'visit': bool,
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype   | Description
:--------- | :----------- | :---- | :------ | :----------
           | FeaturesDict |       |         |
conversion | Tensor       |       | bool    |
exposure   | Tensor       |       | bool    |
f0         | Tensor       |       | float32 |
f1         | Tensor       |       | float32 |
f10        | Tensor       |       | float32 |
f11        | Tensor       |       | float32 |
f2         | Tensor       |       | float32 |
f3         | Tensor       |       | float32 |
f4         | Tensor       |       | float32 |
f5         | Tensor       |       | float32 |
f6         | Tensor       |       | float32 |
f7         | Tensor       |       | float32 |
f8         | Tensor       |       | float32 |
f9         | Tensor       |       | float32 |
treatment  | Tensor       |       | int64   |
visit      | Tensor       |       | bool    |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'exposure': 'exposure', 'f0': 'f0', 'f1': 'f1', 'f10': 'f10', 'f11':
    'f11', 'f2': 'f2', 'f3': 'f3', 'f4': 'f4', 'f5': 'f5', 'f6': 'f6', 'f7':
    'f7', 'f8': 'f8', 'f9': 'f9', 'treatment': 'treatment'}, 'visit')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/criteo-1.0.1.html";
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
@inproceedings{Diemert2018,
author = {{Diemert Eustache, Betlei Artem} and Renaudin, Christophe and Massih-Reza, Amini},
title={A Large Scale Benchmark for Uplift Modeling},
publisher = {ACM},
booktitle = {Proceedings of the AdKDD and TargetAd Workshop, KDD, London,United Kingdom, August, 20, 2018},
year = {2018}
}
```

