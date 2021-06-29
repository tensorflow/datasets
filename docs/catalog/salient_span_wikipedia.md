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
    [`tfds.text.SalientSpanWikipedia`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/salient_span_wikipedia.py)

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

*   **Features**:

```python
FeaturesDict({
    'spans': Sequence({
        'limit': tf.int32,
        'start': tf.int32,
        'type': tf.string,
    }),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/salient_span_wikipedia-sentences-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
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

*   **Features**:

```python
FeaturesDict({
    'sentences': Sequence({
        'limit': tf.int32,
        'start': tf.int32,
    }),
    'spans': Sequence({
        'limit': tf.int32,
        'start': tf.int32,
        'type': tf.string,
    }),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/salient_span_wikipedia-documents-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->