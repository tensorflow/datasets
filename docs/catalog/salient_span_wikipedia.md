<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="salient_span_wikipedia" />
  <meta itemprop="description" content="Wikipedia sentences with labeled salient spans.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;salient_span_wikipedia&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/salient_span_wikipedia" />
  <meta itemprop="sameAs" content="https://www.tensorflow.org/datasets/catalog/salient_span_wikipedia" />
  <meta itemprop="citation" content="@article{guu2020realm,&#10;    title={REALM: Retrieval-Augmented Language Model Pre-Training},&#10;    author={Kelvin Guu and Kenton Lee and Zora Tung and Panupong Pasupat and Ming-Wei Chang},&#10;    year={2020},&#10;    journal = {arXiv e-prints},&#10;    archivePrefix = {arXiv},&#10;    eprint={2002.08909},&#10;}" />
</div>

# `salient_span_wikipedia`


*   **Description**:

Wikipedia sentences with labeled salient spans.

*   **Homepage**:
    [https://www.tensorflow.org/datasets/catalog/salient_span_wikipedia](https://www.tensorflow.org/datasets/catalog/salient_span_wikipedia)

*   **Source code**:
    [`tfds.datasets.salient_span_wikipedia.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/salient_span_wikipedia/salient_span_wikipedia_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{guu2020realm,
    title={REALM: Retrieval-Augmented Language Model Pre-Training},
    author={Kelvin Guu and Kenton Lee and Zora Tung and Panupong Pasupat and Ming-Wei Chang},
    year={2020},
    journal = {arXiv e-prints},
    archivePrefix = {arXiv},
    eprint={2002.08909},
}
```


## salient_span_wikipedia/sentences (default config)

*   **Config description**: Examples are individual sentences containing
    entities.

*   **Dataset size**: `20.57 GiB`

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 82,291,706

*   **Feature structure**:

```python
FeaturesDict({
    'spans': Sequence({
        'limit': int32,
        'start': int32,
        'type': string,
    }),
    'text': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape | Dtype  | Description
:---------- | :----------- | :---- | :----- | :----------
            | FeaturesDict |       |        |
spans       | Sequence     |       |        |
spans/limit | Tensor       |       | int32  |
spans/start | Tensor       |       | int32  |
spans/type  | Tensor       |       | string |
text        | Text         |       | string |
title       | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/salient_span_wikipedia-sentences-1.0.0.html";
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

## salient_span_wikipedia/documents

*   **Config description**: Examples re full documents.

*   **Dataset size**: `16.52 GiB`

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 13,353,718

*   **Feature structure**:

```python
FeaturesDict({
    'sentences': Sequence({
        'limit': int32,
        'start': int32,
    }),
    'spans': Sequence({
        'limit': int32,
        'start': int32,
        'type': string,
    }),
    'text': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype  | Description
:-------------- | :----------- | :---- | :----- | :----------
                | FeaturesDict |       |        |
sentences       | Sequence     |       |        |
sentences/limit | Tensor       |       | int32  |
sentences/start | Tensor       |       | int32  |
spans           | Sequence     |       |        |
spans/limit     | Tensor       |       | int32  |
spans/start     | Tensor       |       | int32  |
spans/type      | Tensor       |       | string |
text            | Text         |       | string |
title           | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/salient_span_wikipedia-documents-1.0.0.html";
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