<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="c4_wsrs" />
  <meta itemprop="description" content="A medical abbreviation expansion dataset which applies web-scale reverse&#10;substitution (wsrs) to the C4 dataset, which is a colossal, cleaned version of&#10;Common Crawl&#x27;s web crawl corpus.&#10;&#10;The original source is the Common Crawl dataset: https://commoncrawl.org&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;c4_wsrs&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/c4_wsrs" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/deciphering_clinical_abbreviations" />
  <meta itemprop="citation" content="" />
</div>

# `c4_wsrs`


*   **Description**:

A medical abbreviation expansion dataset which applies web-scale reverse
substitution (wsrs) to the C4 dataset, which is a colossal, cleaned version of
Common Crawl's web crawl corpus.

The original source is the Common Crawl dataset: https://commoncrawl.org

*   **Config description**: Default C4-WSRS dataset.

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/deciphering_clinical_abbreviations](https://github.com/google-research/google-research/tree/master/deciphering_clinical_abbreviations)

*   **Source code**:
    [`tfds.text.c4_wsrs.C4WSRS`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/c4_wsrs/c4_wsrs.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `143.01 KiB`

*   **Dataset size**: `5.84 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'train'`      | 9,575,852
`'validation'` | 991,422

*   **Feature structure**:

```python
FeaturesDict({
    'abbreviated_snippet': Text(shape=(), dtype=string),
    'original_snippet': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature             | Class        | Shape | Dtype  | Description
:------------------ | :----------- | :---- | :----- | :----------
                    | FeaturesDict |       |        |
abbreviated_snippet | Text         |       | string |
original_snippet    | Text         |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/c4_wsrs-default-1.0.0.html";
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


## c4_wsrs/default (default config)
