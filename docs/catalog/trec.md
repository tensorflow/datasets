<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="trec" />
  <meta itemprop="description" content="The Text REtrieval Conference (TREC) Question Classification dataset contains 5500 labeled questions in training set and another 500 for test set. The dataset has 6 labels, 47 level-2 labels. Average length of each sentence is 10, vocabulary size of 8700.&#10;Data are collected from four sources: 4,500 English questions published by USC (Hovy et al., 2001), about 500 manually constructed questions for a few rare classes, 894 TREC 8 and TREC 9 questions, and also 500 questions from TREC 10 which serves as the test set.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;trec&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/trec" />
  <meta itemprop="sameAs" content="https://cogcomp.seas.upenn.edu/Data/QA/QC/" />
  <meta itemprop="citation" content="@inproceedings{li-roth-2002-learning,&#10;    title = &quot;Learning Question Classifiers&quot;,&#10;    author = &quot;Li, Xin  and&#10;      Roth, Dan&quot;,&#10;    booktitle = &quot;{COLING} 2002: The 19th International Conference on Computational Linguistics&quot;,&#10;    year = &quot;2002&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/C02-1150&quot;,&#10;}&#10;@inproceedings{hovy-etal-2001-toward,&#10;    title = &quot;Toward Semantics-Based Answer Pinpointing&quot;,&#10;    author = &quot;Hovy, Eduard  and&#10;      Gerber, Laurie  and&#10;      Hermjakob, Ulf  and&#10;      Lin, Chin-Yew  and&#10;      Ravichandran, Deepak&quot;,&#10;    booktitle = &quot;Proceedings of the First International Conference on Human Language Technology Research&quot;,&#10;    year = &quot;2001&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/H01-1069&quot;,&#10;}" />
</div>

# `trec`

*   **Description**:

The Text REtrieval Conference (TREC) Question Classification dataset contains
5500 labeled questions in training set and another 500 for test set. The dataset
has 6 labels, 47 level-2 labels. Average length of each sentence is 10,
vocabulary size of 8700. Data are collected from four sources: 4,500 English
questions published by USC (Hovy et al., 2001), about 500 manually constructed
questions for a few rare classes, 894 TREC 8 and TREC 9 questions, and also 500
questions from TREC 10 which serves as the test set.

*   **Homepage**:
    [https://cogcomp.seas.upenn.edu/Data/QA/QC/](https://cogcomp.seas.upenn.edu/Data/QA/QC/)

*   **Source code**:
    [`tfds.text.trec.Trec`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/trec/trec.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `350.79 KiB`

*   **Dataset size**: `636.90 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 500
`'train'` | 5,452

*   **Features**:

```python
FeaturesDict({
    'label-coarse': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    'label-fine': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@inproceedings{li-roth-2002-learning,
    title = "Learning Question Classifiers",
    author = "Li, Xin  and
      Roth, Dan",
    booktitle = "{COLING} 2002: The 19th International Conference on Computational Linguistics",
    year = "2002",
    url = "https://www.aclweb.org/anthology/C02-1150",
}
@inproceedings{hovy-etal-2001-toward,
    title = "Toward Semantics-Based Answer Pinpointing",
    author = "Hovy, Eduard  and
      Gerber, Laurie  and
      Hermjakob, Ulf  and
      Lin, Chin-Yew  and
      Ravichandran, Deepak",
    booktitle = "Proceedings of the First International Conference on Human Language Technology Research",
    year = "2001",
    url = "https://www.aclweb.org/anthology/H01-1069",
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/trec-1.0.0.html";
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