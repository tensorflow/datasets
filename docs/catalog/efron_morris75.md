<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="efron_morris75" />
  <meta itemprop="description" content="The batting averages of 18 Major League Baseball players through their first 45&#10;at-bats of the 1970 season, along with their batting average for the remainder&#10;the season.&#10;&#10;The data has been modified from the table in the paper, as used for case studies&#10;using Stan and PyMC3, by adding columns explicitly listing the number of at-bats&#10;early in the season, as well as at-bats and hits for the full season.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;efron_morris75&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/efron_morris75" />
  <meta itemprop="sameAs" content="https://www.tensorflow.org/datasets/catalog/efron_morris75" />
  <meta itemprop="citation" content="@article{efron1975data,&#10;  title={Data analysis using Stein&#x27;s estimator and its generalizations},&#10;  author={Efron, Bradley and Morris, Carl},&#10;  journal={Journal of the American Statistical Association},&#10;  volume={70},&#10;  number={350},&#10;  pages={311--319},&#10;  year={1975},&#10;  publisher={Taylor \&amp; Francis}&#10;}" />
</div>

# `efron_morris75`


*   **Description**:

The batting averages of 18 Major League Baseball players through their first 45
at-bats of the 1970 season, along with their batting average for the remainder
the season.

The data has been modified from the table in the paper, as used for case studies
using Stan and PyMC3, by adding columns explicitly listing the number of at-bats
early in the season, as well as at-bats and hits for the full season.

*   **Homepage**:
    [https://www.tensorflow.org/datasets/catalog/efron_morris75](https://www.tensorflow.org/datasets/catalog/efron_morris75)

*   **Source code**:
    [`tfds.datasets.efron_morris75.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/efron_morris75/efron_morris75_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `1008 bytes`

*   **Dataset size**: `4.29 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18

*   **Feature structure**:

```python
FeaturesDict({
    'At-Bats': int32,
    'BattingAverage': float32,
    'FirstName': string,
    'Hits': int32,
    'LastName': string,
    'RemainingAt-Bats': int32,
    'RemainingAverage': float32,
    'SeasonAt-Bats': int32,
    'SeasonAverage': float32,
    'SeasonHits': int32,
})
```

*   **Feature documentation**:

Feature          | Class        | Shape | Dtype   | Description
:--------------- | :----------- | :---- | :------ | :----------
                 | FeaturesDict |       |         |
At-Bats          | Tensor       |       | int32   |
BattingAverage   | Tensor       |       | float32 |
FirstName        | Tensor       |       | string  |
Hits             | Tensor       |       | int32   |
LastName         | Tensor       |       | string  |
RemainingAt-Bats | Tensor       |       | int32   |
RemainingAverage | Tensor       |       | float32 |
SeasonAt-Bats    | Tensor       |       | int32   |
SeasonAverage    | Tensor       |       | float32 |
SeasonHits       | Tensor       |       | int32   |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/efron_morris75-1.0.0.html";
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
@article{efron1975data,
  title={Data analysis using Stein's estimator and its generalizations},
  author={Efron, Bradley and Morris, Carl},
  journal={Journal of the American Statistical Association},
  volume={70},
  number={350},
  pages={311--319},
  year={1975},
  publisher={Taylor \& Francis}
}
```

