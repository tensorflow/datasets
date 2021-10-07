<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wiki_bio" />
  <meta itemprop="description" content="WikiBio is constructed using Wikipedia biography pages, it contains the first&#10;paragraph and the infobox tokenized.&#10;The dataset follows a standarized table format.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wiki_bio&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wiki_bio" />
  <meta itemprop="sameAs" content="https://github.com/DavidGrangier/wikipedia-biography-dataset" />
  <meta itemprop="citation" content="@inproceedings{lebret-etal-2016-neural,&#10;    title = &quot;Neural Text Generation from Structured Data with Application to the Biography Domain&quot;,&#10;    author = &quot;Lebret, R{&#x27;e}mi  and&#10;      Grangier, David  and&#10;      Auli, Michael&quot;,&#10;    booktitle = &quot;Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = nov,&#10;    year = &quot;2016&quot;,&#10;    address = &quot;Austin, Texas&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/D16-1128&quot;,&#10;    doi = &quot;10.18653/v1/D16-1128&quot;,&#10;    pages = &quot;1203--1213&quot;,&#10;}" />
</div>

# `wiki_bio`


*   **Description**:

WikiBio is constructed using Wikipedia biography pages, it contains the first
paragraph and the infobox tokenized. The dataset follows a standarized table
format.

*   **Homepage**:
    [https://github.com/DavidGrangier/wikipedia-biography-dataset](https://github.com/DavidGrangier/wikipedia-biography-dataset)

*   **Source code**:
    [`tfds.structured.WikiBio`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/wiki_bio.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `318.53 MiB`

*   **Dataset size**: `795.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 72,831
`'train'`      | 582,659
`'validation'` | 72,831

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
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_bio-0.1.0.html";
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
@inproceedings{lebret-etal-2016-neural,
    title = "Neural Text Generation from Structured Data with Application to the Biography Domain",
    author = "Lebret, R{'e}mi  and
      Grangier, David  and
      Auli, Michael",
    booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2016",
    address = "Austin, Texas",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D16-1128",
    doi = "10.18653/v1/D16-1128",
    pages = "1203--1213",
}
```
