<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dart" />
  <meta itemprop="description" content="DART (DAta Record to Text generation) contains RDF entity-relation annotated&#10;with sentence descriptions that cover all facts in the triple set. DART was&#10;constructed using existing datasets such as: WikiTableQuestions, WikiSQL, WebNLG&#10;and Cleaned E2E. The tables from WikiTableQuestions and WikiSQL were transformed&#10;to subject-predicate-object triples, and its text annotations were mainly&#10;collected from MTurk. The meaningful representations in E2E were also&#10;transformed to triples and its descriptions were used, some that couldn&#x27;t be&#10;transformed were dropped.&#10;&#10;The dataset splits of E2E and WebNLG are kept, and for the WikiTableQuestions&#10;and WikiSQL the Jaccard similarity is used to keep similar tables in the same&#10;set (train/dev/tes).&#10;&#10;This dataset is constructed following a standarized table format.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dart&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dart" />
  <meta itemprop="sameAs" content="https://github.com/Yale-LILY/dart" />
  <meta itemprop="citation" content="@article{radev2020dart,&#10;  title={DART: Open-Domain Structured Data Record to Text Generation},&#10;  author={Dragomir Radev and Rui Zhang and Amrit Rau and Abhinand Sivaprasad and Chiachun Hsieh and Nazneen Fatema Rajani and Xiangru Tang and Aadit Vyas and Neha Verma and Pranav Krishna and Yangxiaokang Liu and Nadia Irwanto and Jessica Pan and Faiaz Rahman and Ahmad Zaidi and Murori Mutuma and Yasin Tarabar and Ankit Gupta and Tao Yu and Yi Chern Tan and Xi Victoria Lin and Caiming Xiong and Richard Socher},&#10;  journal={arXiv preprint arXiv:2007.02871},&#10;  year={2020}" />
</div>

# `dart`

*   **Description**:

DART (DAta Record to Text generation) contains RDF entity-relation annotated
with sentence descriptions that cover all facts in the triple set. DART was
constructed using existing datasets such as: WikiTableQuestions, WikiSQL, WebNLG
and Cleaned E2E. The tables from WikiTableQuestions and WikiSQL were transformed
to subject-predicate-object triples, and its text annotations were mainly
collected from MTurk. The meaningful representations in E2E were also
transformed to triples and its descriptions were used, some that couldn't be
transformed were dropped.

The dataset splits of E2E and WebNLG are kept, and for the WikiTableQuestions
and WikiSQL the Jaccard similarity is used to keep similar tables in the same
set (train/dev/tes).

This dataset is constructed following a standarized table format.

*   **Homepage**:
    [https://github.com/Yale-LILY/dart](https://github.com/Yale-LILY/dart)

*   **Source code**:
    [`tfds.structured.dart.Dart`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/dart/dart.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `249.71 MiB`

*   **Dataset size**: `38.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 12,552
`'train'`      | 62,659
`'validation'` | 6,980

*   **Features**:

```python
FeaturesDict({
    'input_text': FeaturesDict({
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dart-0.1.0.html";
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
@article{radev2020dart,
  title={DART: Open-Domain Structured Data Record to Text Generation},
  author={Dragomir Radev and Rui Zhang and Amrit Rau and Abhinand Sivaprasad and Chiachun Hsieh and Nazneen Fatema Rajani and Xiangru Tang and Aadit Vyas and Neha Verma and Pranav Krishna and Yangxiaokang Liu and Nadia Irwanto and Jessica Pan and Faiaz Rahman and Ahmad Zaidi and Murori Mutuma and Yasin Tarabar and Ankit Gupta and Tao Yu and Yi Chern Tan and Xi Victoria Lin and Caiming Xiong and Richard Socher},
  journal={arXiv preprint arXiv:2007.02871},
  year={2020}
```
