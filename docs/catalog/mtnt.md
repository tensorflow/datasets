<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mtnt" />
  <meta itemprop="description" content="MTNT: Machine Translation of Noisy Text&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mtnt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mtnt" />
  <meta itemprop="sameAs" content="https://pmichel31415.github.io/mtnt/index.html" />
  <meta itemprop="citation" content="@InProceedings{michel2018mtnt,&#10;  author    = {Michel, Paul  and  Neubig, Graham},&#10;  title     = {MTNT: A Testbed for Machine Translation of Noisy Text},&#10;  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing}&#10;}" />
</div>

# `mtnt`


*   **Description**:

MTNT: Machine Translation of Noisy Text

*   **Homepage**:
    [https://pmichel31415.github.io/mtnt/index.html](https://pmichel31415.github.io/mtnt/index.html)

*   **Source code**:
    [`tfds.translate.mtnt.Mtnt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/mtnt/mtnt.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `35.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'dst': Text(shape=(), dtype=tf.string),
    'src': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype     | Description
:------ | :----------- | :---- | :-------- | :----------
        | FeaturesDict |       |           |
dst     | Text         |       | tf.string |
src     | Text         |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('src', 'dst')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@InProceedings{michel2018mtnt,
  author    = {Michel, Paul  and  Neubig, Graham},
  title     = {MTNT: A Testbed for Machine Translation of Noisy Text},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing}
}
```


## mtnt/en-fr (default config)

*   **Dataset size**: `11.33 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,020
`'train'` | 35,692
`'valid'` | 811

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mtnt-en-fr-1.0.0.html";
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

## mtnt/en-ja

*   **Dataset size**: `4.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 946
`'train'` | 5,746
`'valid'` | 892

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mtnt-en-ja-1.0.0.html";
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

## mtnt/fr-en

*   **Dataset size**: `8.28 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,022
`'train'` | 18,942
`'valid'` | 876

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mtnt-fr-en-1.0.0.html";
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