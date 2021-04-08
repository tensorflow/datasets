<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="coqa" />
  <meta itemprop="description" content="CoQA: A Conversational Question Answering Challenge&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;coqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/coqa" />
  <meta itemprop="sameAs" content="https://stanfordnlp.github.io/coqa/" />
  <meta itemprop="citation" content="@misc{reddy2018coqa,&#10;    title={CoQA: A Conversational Question Answering Challenge},&#10;    author={Siva Reddy and Danqi Chen and Christopher D. Manning},&#10;    year={2018},&#10;    eprint={1808.07042},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `coqa`

*   **Description**:

CoQA: A Conversational Question Answering Challenge

*   **Homepage**:
    [https://stanfordnlp.github.io/coqa/](https://stanfordnlp.github.io/coqa/)

*   **Source code**:
    [`tfds.question_answering.coqa.Coqa`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/coqa/coqa.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `55.40 MiB`

*   **Dataset size**: `18.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 500
`'train'` | 7,199

*   **Features**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_end': tf.int32,
        'answer_start': tf.int32,
        'input_text': Text(shape=(), dtype=tf.string),
    }),
    'questions': Sequence(Text(shape=(), dtype=tf.string)),
    'source': Text(shape=(), dtype=tf.string),
    'story': Text(shape=(), dtype=tf.string),
})
```

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
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/coqa-1.0.0.html";
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

*   **Citation**:

```
@misc{reddy2018coqa,
    title={CoQA: A Conversational Question Answering Challenge},
    author={Siva Reddy and Danqi Chen and Christopher D. Manning},
    year={2018},
    eprint={1808.07042},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
