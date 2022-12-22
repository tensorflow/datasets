<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="simpte" />
  <meta itemprop="description" content="Full name: Simulations for Personalized Treatment Effects&#10;&#10;Generated with the R&#x27;s Uplift package:&#10; https://rdrr.io/cran/uplift/man/sim_pte.html&#10;&#10;The package could be downloaded here:&#10; https://cran.r-project.org/src/contrib/Archive/uplift/&#10;&#10;Dataset generated in R version 4.1.2 with following code:&#10;&#10;```&#10;  library(uplift)&#10;&#10;  set.seed(123)&#10;&#10;  train &lt;- sim_pte(n = 1000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)&#10;  test &lt;- sim_pte(n = 2000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)&#10;&#10;  train$treat &lt;- ifelse(train$treat == 1, 2, 1)&#10;  test$treat &lt;- ifelse(test$treat == 1, 2, 1)&#10;&#10;  train$y &lt;- ifelse(train$y == 1, 2, 1)&#10;  test$y &lt;- ifelse(test$y == 1, 2, 1)&#10;&#10;  train$ts = NULL&#10;  test$ts = NULL&#10;```&#10;&#10;Parameters:&#10;&#10;  - `n` = number of samples&#10;  - `p` = number of predictors&#10;  - `ro` = covariance between predictors&#10;  - `sigma` = mutiplier of the error term&#10;  - `beta.den` = beta is mutiplied by 1/beta.den&#10;&#10;Creator: Leo Guelman leo.guelman@gmail.com&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;simpte&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/simpte" />
  <meta itemprop="sameAs" content="https://rdrr.io/cran/uplift/man/sim_pte.html" />
  <meta itemprop="citation" content="@misc{https://doi.org/10.48550/arxiv.1212.2995,&#10;  doi = {10.48550/ARXIV.1212.2995},&#10;  url = {https://arxiv.org/abs/1212.2995},&#10;  author = {Tian, Lu and Alizadeh, Ash and Gentles, Andrew and Tibshirani, Robert},&#10;  keywords = {Methodology (stat.ME), FOS: Computer and information sciences, FOS: Computer and information sciences},&#10;  title = {A Simple Method for Detecting Interactions between a Treatment and a Large Number of Covariates},&#10;  publisher = {arXiv},&#10;  year = {2012},&#10;  copyright = {arXiv.org perpetual, non-exclusive license}&#10;}" />
</div>

# `simpte`


Warning: Manual download required. See instructions below.

*   **Description**:

Full name: Simulations for Personalized Treatment Effects

Generated with the R's Uplift package:
https://rdrr.io/cran/uplift/man/sim_pte.html

The package could be downloaded here:
https://cran.r-project.org/src/contrib/Archive/uplift/

Dataset generated in R version 4.1.2 with following code:

```
  library(uplift)

  set.seed(123)

  train <- sim_pte(n = 1000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)
  test <- sim_pte(n = 2000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)

  train$treat <- ifelse(train$treat == 1, 2, 1)
  test$treat <- ifelse(test$treat == 1, 2, 1)

  train$y <- ifelse(train$y == 1, 2, 1)
  test$y <- ifelse(test$y == 1, 2, 1)

  train$ts = NULL
  test$ts = NULL
```

Parameters:

-   `n` = number of samples
-   `p` = number of predictors
-   `ro` = covariance between predictors
-   `sigma` = mutiplier of the error term
-   `beta.den` = beta is mutiplied by 1/beta.den

Creator: Leo Guelman leo.guelman@gmail.com

*   **Homepage**:
    [https://rdrr.io/cran/uplift/man/sim_pte.html](https://rdrr.io/cran/uplift/man/sim_pte.html)

*   **Source code**:
    [`tfds.datasets.simpte.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/simpte/simpte_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `1.04 MiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Please download training data: sim_pte_train.csv and test data:
    sim_pte_test.csv to ~/tensorflow_datasets/downloads/manual/.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 1,000

*   **Feature structure**:

```python
FeaturesDict({
    'X1': float32,
    'X10': float32,
    'X11': float32,
    'X12': float32,
    'X13': float32,
    'X14': float32,
    'X15': float32,
    'X16': float32,
    'X17': float32,
    'X18': float32,
    'X19': float32,
    'X2': float32,
    'X20': float32,
    'X3': float32,
    'X4': float32,
    'X5': float32,
    'X6': float32,
    'X7': float32,
    'X8': float32,
    'X9': float32,
    'treat': int32,
    'y': int32,
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype   | Description
:------ | :----------- | :---- | :------ | :----------
        | FeaturesDict |       |         |
X1      | Tensor       |       | float32 |
X10     | Tensor       |       | float32 |
X11     | Tensor       |       | float32 |
X12     | Tensor       |       | float32 |
X13     | Tensor       |       | float32 |
X14     | Tensor       |       | float32 |
X15     | Tensor       |       | float32 |
X16     | Tensor       |       | float32 |
X17     | Tensor       |       | float32 |
X18     | Tensor       |       | float32 |
X19     | Tensor       |       | float32 |
X2      | Tensor       |       | float32 |
X20     | Tensor       |       | float32 |
X3      | Tensor       |       | float32 |
X4      | Tensor       |       | float32 |
X5      | Tensor       |       | float32 |
X6      | Tensor       |       | float32 |
X7      | Tensor       |       | float32 |
X8      | Tensor       |       | float32 |
X9      | Tensor       |       | float32 |
treat   | Tensor       |       | int32   |
y       | Tensor       |       | int32   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'X1': 'X1', 'X10': 'X10', 'X11': 'X11', 'X12': 'X12', 'X13': 'X13',
    'X14': 'X14', 'X15': 'X15', 'X16': 'X16', 'X17': 'X17', 'X18': 'X18', 'X19':
    'X19', 'X2': 'X2', 'X20': 'X20', 'X3': 'X3', 'X4': 'X4', 'X5': 'X5', 'X6':
    'X6', 'X7': 'X7', 'X8': 'X8', 'X9': 'X9', 'treat': 'treat'}, 'y')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/simpte-1.0.0.html";
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
@misc{https://doi.org/10.48550/arxiv.1212.2995,
  doi = {10.48550/ARXIV.1212.2995},
  url = {https://arxiv.org/abs/1212.2995},
  author = {Tian, Lu and Alizadeh, Ash and Gentles, Andrew and Tibshirani, Robert},
  keywords = {Methodology (stat.ME), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {A Simple Method for Detecting Interactions between a Treatment and a Large Number of Covariates},
  publisher = {arXiv},
  year = {2012},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

