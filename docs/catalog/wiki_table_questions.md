<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wiki_table_questions" />
  <meta itemprop="description" content="The dataset contains pairs table-question, and the respective answer. The&#10;questions require multi-step reasoning and various data operations such as&#10;comparison, aggregation, and arithmetic computation. The tables were randomly&#10;selected among Wikipedia tables with at least 8 rows and 5 columns.&#10;&#10;(As per the documentation usage notes)&#10;&#10;- Dev: Mean accuracy over three (not five) splits of the training data. In other&#10;words, train on &#x27;split-{1,2,3}-train&#x27; and test on &#x27;split-{1,2,3}-dev&#x27;,&#10;respectively, then average the accuracy.&#10;&#10;- Test: Train on &#x27;train&#x27; and test on &#x27;test&#x27;.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wiki_table_questions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wiki_table_questions" />
  <meta itemprop="sameAs" content="https://ppasupat.github.io/WikiTableQuestions/#usage-notes" />
  <meta itemprop="citation" content="@inproceedings{pasupat-liang-2015-compositional,&#10;    title = &quot;Compositional Semantic Parsing on Semi-Structured Tables&quot;,&#10;    author = &quot;Pasupat, Panupong  and&#10;      Liang, Percy&quot;,&#10;    booktitle = &quot;Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)&quot;,&#10;    month = jul,&#10;    year = &quot;2015&quot;,&#10;    address = &quot;Beijing, China&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/P15-1142&quot;,&#10;    doi = &quot;10.3115/v1/P15-1142&quot;,&#10;    pages = &quot;1470--1480&quot;,&#10;}" />
</div>

# `wiki_table_questions`

*   **Description**:

The dataset contains pairs table-question, and the respective answer. The
questions require multi-step reasoning and various data operations such as
comparison, aggregation, and arithmetic computation. The tables were randomly
selected among Wikipedia tables with at least 8 rows and 5 columns.

(As per the documentation usage notes)

-   Dev: Mean accuracy over three (not five) splits of the training data. In
    other words, train on 'split-{1,2,3}-train' and test on 'split-{1,2,3}-dev',
    respectively, then average the accuracy.

-   Test: Train on 'train' and test on 'test'.

*   **Homepage**:
    [https://ppasupat.github.io/WikiTableQuestions/#usage-notes](https://ppasupat.github.io/WikiTableQuestions/#usage-notes)

*   **Source code**:
    [`tfds.structured.wiki_table_questions.WikiTableQuestions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/wiki_table_questions/wiki_table_questions.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `65.36 MiB`

*   **Dataset size**: `237.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split             | Examples
:---------------- | -------:
`'split-1-dev'`   | 2,810
`'split-1-train'` | 11,321
`'split-2-dev'`   | 2,838
`'split-2-train'` | 11,312
`'split-3-dev'`   | 2,838
`'split-3-train'` | 11,311
`'test'`          | 4,344
`'train'`         | 14,149

*   **Features**:

```python
FeaturesDict({
    'input_text': FeaturesDict({
        'context': tf.string,
        'table': Sequence({
            'column_header': tf.string,
            'content': tf.string,
            'row_number': tf.int16,
        }),
    }),
    'target_text': tf.string,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('input_text', 'target_text')`

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_table_questions-1.0.0.html";
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
@inproceedings{pasupat-liang-2015-compositional,
    title = "Compositional Semantic Parsing on Semi-Structured Tables",
    author = "Pasupat, Panupong  and
      Liang, Percy",
    booktitle = "Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = jul,
    year = "2015",
    address = "Beijing, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P15-1142",
    doi = "10.3115/v1/P15-1142",
    pages = "1470--1480",
}
```
