<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="clinc_oos" />
  <meta itemprop="description" content="Task-oriented dialog systems need to know when a query falls outside their range of supported intents, but current text classification corpora only define label sets that cover every example. We introduce a new dataset that includes queries that are out-of-scope (OOS), i.e., queries that do not fall into any of the system&#x27;s supported intents. This poses a new challenge because models cannot assume that every query at inference time belongs to a system-supported intent class. Our dataset also covers 150 intent classes over 10 domains, capturing the breadth that a production task-oriented agent must handle. It offers a way of more rigorously and realistically benchmarking text classification in task-driven dialog systems.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;clinc_oos&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/clinc_oos" />
  <meta itemprop="sameAs" content="https://github.com/clinc/oos-eval/" />
  <meta itemprop="citation" content="@inproceedings{larson-etal-2019-evaluation,&#10;    title = &quot;An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction&quot;,&#10;    author = &quot;Larson, Stefan  and&#10;      Mahendran, Anish  and&#10;      Peper, Joseph J.  and&#10;      Clarke, Christopher  and&#10;      Lee, Andrew  and&#10;      Hill, Parker  and&#10;      Kummerfeld, Jonathan K.  and&#10;      Leach, Kevin  and&#10;      Laurenzano, Michael A.  and&#10;      Tang, Lingjia  and&#10;      Mars, Jason&quot;,&#10;    booktitle = &quot;Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)&quot;,&#10;    month = nov,&#10;    year = &quot;2019&quot;,&#10;    address = &quot;Hong Kong, China&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/D19-1131&quot;,&#10;    doi = &quot;10.18653/v1/D19-1131&quot;,&#10;    pages = &quot;1311--1316&quot;,&#10;}" />
</div>

# `clinc_oos`


*   **Description**:

Task-oriented dialog systems need to know when a query falls outside their range
of supported intents, but current text classification corpora only define label
sets that cover every example. We introduce a new dataset that includes queries
that are out-of-scope (OOS), i.e., queries that do not fall into any of the
system's supported intents. This poses a new challenge because models cannot
assume that every query at inference time belongs to a system-supported intent
class. Our dataset also covers 150 intent classes over 10 domains, capturing the
breadth that a production task-oriented agent must handle. It offers a way of
more rigorously and realistically benchmarking text classification in
task-driven dialog systems.

*   **Homepage**:
    [https://github.com/clinc/oos-eval/](https://github.com/clinc/oos-eval/)

*   **Source code**:
    [`tfds.text.ClincOOS`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/clinc_oos.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `256.01 KiB`

*   **Dataset size**: `3.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split              | Examples
:----------------- | -------:
`'test'`           | 4,500
`'test_oos'`       | 1,000
`'train'`          | 15,000
`'train_oos'`      | 100
`'validation'`     | 3,000
`'validation_oos'` | 100

*   **Features**:

```python
FeaturesDict({
    'domain': tf.int32,
    'domain_name': Text(shape=(), dtype=tf.string),
    'intent': tf.int32,
    'intent_name': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'intent')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/clinc_oos-0.1.0.html";
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
@inproceedings{larson-etal-2019-evaluation,
    title = "An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction",
    author = "Larson, Stefan  and
      Mahendran, Anish  and
      Peper, Joseph J.  and
      Clarke, Christopher  and
      Lee, Andrew  and
      Hill, Parker  and
      Kummerfeld, Jonathan K.  and
      Leach, Kevin  and
      Laurenzano, Michael A.  and
      Tang, Lingjia  and
      Mars, Jason",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1131",
    doi = "10.18653/v1/D19-1131",
    pages = "1311--1316",
}
```
