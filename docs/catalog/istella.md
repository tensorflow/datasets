<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="istella" />
  <meta itemprop="description" content="The Istella datasets are three large-scale Learning-to-Rank datasets released by&#10;Istella. Each dataset consists of query-document pairs represented as feature&#10;vectors and corresponding relevance judgment labels.&#10;&#10;The dataset contains three versions:&#10;&#10; * `main` (&quot;Istella LETOR&quot;): Containing 10,454,629 query-document pairs.&#10; * `s` (&quot;Istella-S LETOR&quot;): Containing 3,408,630 query-document pairs.&#10; * `x` (&quot;Istella-X LETOR&quot;): Containing 26,791,447 query-document pairs.&#10;&#10;You can specify whether to use the `main`, `s` or `x` version of the dataset as&#10;follows:&#10;&#10;```python&#10;ds = tfds.load(&quot;istella/main&quot;)&#10;ds = tfds.load(&quot;istella/s&quot;)&#10;ds = tfds.load(&quot;istella/x&quot;)&#10;```&#10;&#10;If only `istella` is specified, the `istella/main` option is selected by&#10;default:&#10;&#10;```python&#10;# This is the same as `tfds.load(&quot;istella/main&quot;)`&#10;ds = tfds.load(&quot;istella&quot;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;istella&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/istella" />
  <meta itemprop="sameAs" content="http://quickrank.isti.cnr.it/istella-dataset/" />
  <meta itemprop="citation" content="@article{10.1145/2987380,&#10;  author = {Dato, Domenico and Lucchese, Claudio and Nardini, Franco Maria and Orlando, Salvatore and Perego, Raffaele and Tonellotto, Nicola and Venturini, Rossano},&#10;  title = {Fast Ranking with Additive Ensembles of Oblivious and Non-Oblivious Regression Trees},&#10;  year = {2016},&#10;  publisher = {ACM},&#10;  address = {New York, NY, USA},&#10;  volume = {35},&#10;  number = {2},&#10;  issn = {1046-8188},&#10;  url = {https://doi.org/10.1145/2987380},&#10;  doi = {10.1145/2987380},&#10;  journal = {ACM Transactions on Information Systems},&#10;  articleno = {15},&#10;  numpages = {31},&#10;}" />
</div>

# `istella`


*   **Description**:

The Istella datasets are three large-scale Learning-to-Rank datasets released by
Istella. Each dataset consists of query-document pairs represented as feature
vectors and corresponding relevance judgment labels.

The dataset contains three versions:

*   `main` ("Istella LETOR"): Containing 10,454,629 query-document pairs.
*   `s` ("Istella-S LETOR"): Containing 3,408,630 query-document pairs.
*   `x` ("Istella-X LETOR"): Containing 26,791,447 query-document pairs.

You can specify whether to use the `main`, `s` or `x` version of the dataset as
follows:

```python
ds = tfds.load("istella/main")
ds = tfds.load("istella/s")
ds = tfds.load("istella/x")
```

If only `istella` is specified, the `istella/main` option is selected by
default:

```python
# This is the same as `tfds.load("istella/main")`
ds = tfds.load("istella")
```

*   **Homepage**:
    [http://quickrank.isti.cnr.it/istella-dataset/](http://quickrank.isti.cnr.it/istella-dataset/)

*   **Source code**:
    [`tfds.ranking.istella.Istella`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/ranking/istella/istella.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.0.1`: Fix serialization to support float64.
    *   **`1.1.0`** (default): Bundle features into a single 'float_features'
        feature.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'float_features': Tensor(shape=(None, 220), dtype=tf.float64),
    'label': Tensor(shape=(None,), dtype=tf.float64),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype      | Description
:------------- | :----------- | :---------- | :--------- | :----------
               | FeaturesDict |             |            |
float_features | Tensor       | (None, 220) | tf.float64 |
label          | Tensor       | (None,)     | tf.float64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{10.1145/2987380,
  author = {Dato, Domenico and Lucchese, Claudio and Nardini, Franco Maria and Orlando, Salvatore and Perego, Raffaele and Tonellotto, Nicola and Venturini, Rossano},
  title = {Fast Ranking with Additive Ensembles of Oblivious and Non-Oblivious Regression Trees},
  year = {2016},
  publisher = {ACM},
  address = {New York, NY, USA},
  volume = {35},
  number = {2},
  issn = {1046-8188},
  url = {https://doi.org/10.1145/2987380},
  doi = {10.1145/2987380},
  journal = {ACM Transactions on Information Systems},
  articleno = {15},
  numpages = {31},
}
```


## istella/main (default config)

*   **Download size**: `1.20 GiB`

*   **Dataset size**: `1.10 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 9,799
`'train'` | 23,219

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-main-1.1.0.html";
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

## istella/s

*   **Download size**: `450.26 MiB`

*   **Dataset size**: `414.69 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,562
`'train'` | 19,245
`'vali'`  | 7,211

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-s-1.1.0.html";
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

## istella/x

*   **Download size**: `4.42 GiB`

*   **Dataset size**: `2.42 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-x-1.1.0.html";
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