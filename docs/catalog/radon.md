<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="radon" />
  <meta itemprop="description" content="Radon is a radioactive gas that enters homes through contact points with the&#10;ground. It is a carcinogen that is the primary cause of lung cancer in&#10;non-smokers. Radon levels vary greatly from household to household. This dataset&#10;contains measured radon levels in U.S homes by county and state. The &#x27;activity&#x27;&#10;label is the measured radon concentration in pCi/L. Important predictors are&#10;&#x27;floor&#x27; (the floor of the house in which the measurement was taken), &#x27;county&#x27;&#10;(the U.S. county in which the house is located), and &#x27;Uppm&#x27; (a measurement of&#10;uranium level of the soil by county).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;radon&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/radon" />
  <meta itemprop="sameAs" content="http://www.stat.columbia.edu/~gelman/arm/examples/radon/" />
  <meta itemprop="citation" content="@book{GelmanHill:2007,&#10;  author = {Gelman, Andrew and Hill, Jennifer},&#10;  title = {Data Analysis Using Regression and Multilevel/Hierarchical Models},&#10;  publisher = {Cambridge University Press},&#10;  series = {Analytical methods for social research},&#10;  year = 2007&#10;}" />
</div>

# `radon`


*   **Description**:

Radon is a radioactive gas that enters homes through contact points with the
ground. It is a carcinogen that is the primary cause of lung cancer in
non-smokers. Radon levels vary greatly from household to household. This dataset
contains measured radon levels in U.S homes by county and state. The 'activity'
label is the measured radon concentration in pCi/L. Important predictors are
'floor' (the floor of the house in which the measurement was taken), 'county'
(the U.S. county in which the house is located), and 'Uppm' (a measurement of
uranium level of the soil by county).

*   **Homepage**:
    [http://www.stat.columbia.edu/~gelman/arm/examples/radon/](http://www.stat.columbia.edu/~gelman/arm/examples/radon/)

*   **Source code**:
    [`tfds.datasets.radon.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/radon/radon_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.71 MiB`

*   **Dataset size**: `9.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,573

*   **Feature structure**:

```python
FeaturesDict({
    'activity': float32,
    'features': FeaturesDict({
        'Uppm': float32,
        'adjwt': float32,
        'basement': string,
        'cntyfips': int32,
        'county': string,
        'dupflag': int32,
        'floor': int32,
        'idnum': int32,
        'lat': float32,
        'lon': float32,
        'pcterr': float32,
        'region': int32,
        'rep': int32,
        'room': int32,
        'startdt': int32,
        'starttm': int32,
        'state': string,
        'state2': string,
        'stfips': int32,
        'stopdt': int32,
        'stoptm': int32,
        'stratum': int32,
        'typebldg': int32,
        'wave': int32,
        'windoor': string,
        'zip': int32,
        'zipflag': int32,
    }),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
activity          | Tensor       |       | float32 |
features          | FeaturesDict |       |         |
features/Uppm     | Tensor       |       | float32 |
features/adjwt    | Tensor       |       | float32 |
features/basement | Tensor       |       | string  |
features/cntyfips | Tensor       |       | int32   |
features/county   | Tensor       |       | string  |
features/dupflag  | Tensor       |       | int32   |
features/floor    | Tensor       |       | int32   |
features/idnum    | Tensor       |       | int32   |
features/lat      | Tensor       |       | float32 |
features/lon      | Tensor       |       | float32 |
features/pcterr   | Tensor       |       | float32 |
features/region   | Tensor       |       | int32   |
features/rep      | Tensor       |       | int32   |
features/room     | Tensor       |       | int32   |
features/startdt  | Tensor       |       | int32   |
features/starttm  | Tensor       |       | int32   |
features/state    | Tensor       |       | string  |
features/state2   | Tensor       |       | string  |
features/stfips   | Tensor       |       | int32   |
features/stopdt   | Tensor       |       | int32   |
features/stoptm   | Tensor       |       | int32   |
features/stratum  | Tensor       |       | int32   |
features/typebldg | Tensor       |       | int32   |
features/wave     | Tensor       |       | int32   |
features/windoor  | Tensor       |       | string  |
features/zip      | Tensor       |       | int32   |
features/zipflag  | Tensor       |       | int32   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'activity')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/radon-1.0.0.html";
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
@book{GelmanHill:2007,
  author = {Gelman, Andrew and Hill, Jennifer},
  title = {Data Analysis Using Regression and Multilevel/Hierarchical Models},
  publisher = {Cambridge University Press},
  series = {Analytical methods for social research},
  year = 2007
}
```

