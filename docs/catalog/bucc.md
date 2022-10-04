<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bucc" />
  <meta itemprop="description" content="Identifying parallel sentences in comparable corpora. Given two&#10;sentence-split monolingual corpora, participant systems are expected&#10;to identify pairs of sentences that are translations of each other.&#10;&#10;The BUCC mining task is a shared task on parallel sentence extraction from two&#10;monolingual corpora with a subset of them assumed to be parallel, and that has&#10;been available since 2016. For each language pair, the shared task provides a&#10;monolingual corpus for each language and a gold mapping list containing true&#10;translation pairs. These pairs are the ground truth. The task is to construct a&#10;list of translation pairs from the monolingual corpora. The constructed list is&#10;compared to the ground truth, and evaluated in terms of the F1 measure.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bucc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bucc" />
  <meta itemprop="sameAs" content="https://comparable.limsi.fr/bucc2018/" />
  <meta itemprop="citation" content="@inproceedings{zweigenbaum2018overview,&#10;  title={Overview of the third BUCC shared task: Spotting parallel sentences  in comparable corpora},&#10;  author={Zweigenbaum, Pierre and Sharoff, Serge and Rapp, Reinhard},&#10;  booktitle={Proceedings of 11th Workshop on Building and Using Comparable Corpora},&#10;  pages={39--42},&#10;  year={2018}&#10;}" />
</div>

# `bucc`


*   **Description**:

Identifying parallel sentences in comparable corpora. Given two sentence-split
monolingual corpora, participant systems are expected to identify pairs of
sentences that are translations of each other.

The BUCC mining task is a shared task on parallel sentence extraction from two
monolingual corpora with a subset of them assumed to be parallel, and that has
been available since 2016. For each language pair, the shared task provides a
monolingual corpus for each language and a gold mapping list containing true
translation pairs. These pairs are the ground truth. The task is to construct a
list of translation pairs from the monolingual corpora. The constructed list is
compared to the ground truth, and evaluated in terms of the F1 measure.

*   **Homepage**:
    [https://comparable.limsi.fr/bucc2018/](https://comparable.limsi.fr/bucc2018/)

*   **Source code**:
    [`tfds.translate.bucc.Bucc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/bucc/bucc.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'source_id': Text(shape=(), dtype=tf.string),
    'source_sentence': Text(shape=(), dtype=tf.string),
    'target_id': Text(shape=(), dtype=tf.string),
    'target_sentence': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype     | Description
:-------------- | :----------- | :---- | :-------- | :----------
                | FeaturesDict |       |           |
source_id       | Text         |       | tf.string |
source_sentence | Text         |       | tf.string |
target_id       | Text         |       | tf.string |
target_sentence | Text         |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{zweigenbaum2018overview,
  title={Overview of the third BUCC shared task: Spotting parallel sentences  in comparable corpora},
  author={Zweigenbaum, Pierre and Sharoff, Serge and Rapp, Reinhard},
  booktitle={Proceedings of 11th Workshop on Building and Using Comparable Corpora},
  pages={39--42},
  year={2018}
}
```


## bucc/bucc_de (default config)

*   **Download size**: `29.30 MiB`

*   **Dataset size**: `3.21 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,580
`'validation'` | 1,038

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bucc-bucc_de-1.0.0.html";
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

## bucc/bucc_fr

*   **Download size**: `21.65 MiB`

*   **Dataset size**: `2.90 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,086
`'validation'` | 929

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bucc-bucc_fr-1.0.0.html";
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

## bucc/bucc_zh

*   **Download size**: `6.79 MiB`

*   **Dataset size**: `615.20 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,899
`'validation'` | 257

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bucc-bucc_zh-1.0.0.html";
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

## bucc/bucc_ru

*   **Download size**: `39.44 MiB`

*   **Dataset size**: `6.36 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 14,435
`'validation'` | 2,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bucc-bucc_ru-1.0.0.html";
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