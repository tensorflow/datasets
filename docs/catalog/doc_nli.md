<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="doc_nli" />
  <meta itemprop="description" content="DocNLI is a large-scale dataset for document-level natural language inference&#10;(NLI). DocNLI is transformed from a broad range of NLP problems and covers&#10;multiple genres of text. The premises always stay in the document granularity,&#10;whereas the hypotheses vary in length from single sentences to passages with&#10;hundreds of words. In contrast to some existing sentence-level NLI datasets,&#10;DocNLI has pretty limited artifacts.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;doc_nli&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/doc_nli" />
  <meta itemprop="sameAs" content="https://github.com/salesforce/DocNLI/" />
  <meta itemprop="citation" content="@inproceedings{yin-etal-2021-docnli,&#10;    title={DocNLI: A Large-scale Dataset for Document-level Natural Language Inference},&#10;    author={Wenpeng Yin and Dragomir Radev and Caiming Xiong},&#10;    booktitle = &quot;Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021&quot;,&#10;    month = aug,&#10;    year = &quot;2021&quot;,&#10;    address = &quot;Bangkok, Thailand&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;}" />
</div>

# `doc_nli`


*   **Description**:

DocNLI is a large-scale dataset for document-level natural language inference
(NLI). DocNLI is transformed from a broad range of NLP problems and covers
multiple genres of text. The premises always stay in the document granularity,
whereas the hypotheses vary in length from single sentences to passages with
hundreds of words. In contrast to some existing sentence-level NLI datasets,
DocNLI has pretty limited artifacts.

*   **Homepage**:
    [https://github.com/salesforce/DocNLI/](https://github.com/salesforce/DocNLI/)

*   **Source code**:
    [`tfds.text.docnli.DocNLI`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/docnli/docnli.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `313.89 MiB`

*   **Dataset size**: `3.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 267,086
`'train'`      | 942,314
`'validation'` | 234,258

*   **Features**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'premise': Text(shape=(), dtype=tf.string),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/doc_nli-1.0.0.html";
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
@inproceedings{yin-etal-2021-docnli,
    title={DocNLI: A Large-scale Dataset for Document-level Natural Language Inference},
    author={Wenpeng Yin and Dragomir Radev and Caiming Xiong},
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
}
```
