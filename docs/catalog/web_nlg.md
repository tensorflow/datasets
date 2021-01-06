<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="web_nlg" />
  <meta itemprop="description" content="The data contains sets of 1 to 7 triples of the form subject-predicate-object&#10;extracted from (DBpedia)[https://wiki.dbpedia.org/] and natural language text&#10;that&#x27;s a verbalisation of these triples.&#10;The test data spans 15 different domains where only 10 appear in the training&#10;data.&#10;The dataset follows a standarized table format.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;web_nlg&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/web_nlg" />
  <meta itemprop="sameAs" content="https://webnlg-challenge.loria.fr/challenge_2017/" />
  <meta itemprop="citation" content="@inproceedings{gardent2017creating,&#10;    title = &quot;&quot;Creating Training Corpora for {NLG} Micro-Planners&quot;&quot;,&#10;    author = &quot;&quot;Gardent, Claire  and&#10;      Shimorina, Anastasia  and&#10;      Narayan, Shashi  and&#10;      Perez-Beltrachini, Laura&quot;&quot;,&#10;    booktitle = &quot;&quot;Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)&quot;&quot;,&#10;    month = jul,&#10;    year = &quot;&quot;2017&quot;&quot;,&#10;    address = &quot;&quot;Vancouver, Canada&quot;&quot;,&#10;    publisher = &quot;&quot;Association for Computational Linguistics&quot;&quot;,&#10;    doi = &quot;&quot;10.18653/v1/P17-1017&quot;&quot;,&#10;    pages = &quot;&quot;179--188&quot;&quot;,&#10;    url = &quot;&quot;https://www.aclweb.org/anthology/P17-1017.pdf&quot;&quot;&#10;}" />
</div>

# `web_nlg`

*   **Description**:

The data contains sets of 1 to 7 triples of the form subject-predicate-object
extracted from (DBpedia)[https://wiki.dbpedia.org/] and natural language text
that's a verbalisation of these triples. The test data spans 15 different
domains where only 10 appear in the training data. The dataset follows a
standarized table format.

*   **Homepage**:
    [https://webnlg-challenge.loria.fr/challenge_2017/](https://webnlg-challenge.loria.fr/challenge_2017/)

*   **Source code**:
    [`tfds.structured.web_nlg.WebNlg`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/web_nlg/web_nlg.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `19.76 MiB`

*   **Dataset size**: `13.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split           | Examples
:-------------- | -------:
`'test_all'`    | 4,928
`'test_unseen'` | 2,433
`'train'`       | 18,102
`'validation'`  | 2,268

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

*   **Citation**:

```
@inproceedings{gardent2017creating,
    title = ""Creating Training Corpora for {NLG} Micro-Planners"",
    author = ""Gardent, Claire  and
      Shimorina, Anastasia  and
      Narayan, Shashi  and
      Perez-Beltrachini, Laura"",
    booktitle = ""Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)"",
    month = jul,
    year = ""2017"",
    address = ""Vancouver, Canada"",
    publisher = ""Association for Computational Linguistics"",
    doi = ""10.18653/v1/P17-1017"",
    pages = ""179--188"",
    url = ""https://www.aclweb.org/anthology/P17-1017.pdf""
}
```

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_nlg-0.1.0.html";
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