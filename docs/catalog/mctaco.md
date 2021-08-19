<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mctaco" />
  <meta itemprop="description" content="MC-TACO is a dataset of 13k question-answer pairs that require temporal&#10;commonsense comprehension. The dataset contains five temporal properties:&#10;&#10;1. duration (how long an event takes)&#10;2. temporal ordering (typical order of events)&#10;3. typical time (when an event occurs)&#10;4. frequency (how often an event occurs)&#10;5. stationarity (whether a state is maintained for a very long time or indefinitely)&#10;&#10;We hope that this dataset can promote the future exploration of this&#10; particular class of reasoning problems.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mctaco&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mctaco" />
  <meta itemprop="sameAs" content="https://github.com/CogComp/MCTACO" />
  <meta itemprop="citation" content="@inproceedings{ZKNR19,&#10;    author = {Ben Zhou, Daniel Khashabi, Qiang Ning and Dan Roth},&#10;    title = {&quot;Going on a vacation&quot; takes longer than &quot;Going for a walk&quot;: A Study of Temporal Commonsense Understanding },&#10;    booktitle = {EMNLP},&#10;    year = {2019},&#10;}" />
</div>

# `mctaco`


*   **Description**:

MC-TACO is a dataset of 13k question-answer pairs that require temporal
commonsense comprehension. The dataset contains five temporal properties:

1.  duration (how long an event takes)
2.  temporal ordering (typical order of events)
3.  typical time (when an event occurs)
4.  frequency (how often an event occurs)
5.  stationarity (whether a state is maintained for a very long time or
    indefinitely)

We hope that this dataset can promote the future exploration of this particular
class of reasoning problems.

*   **Homepage**:
    [https://github.com/CogComp/MCTACO](https://github.com/CogComp/MCTACO)

*   **Source code**:
    [`tfds.question_answering.Mctaco`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/mctaco.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `2.27 MiB`

*   **Dataset size**: `3.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,442
`'validation'` | 3,783

*   **Features**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'question': Text(shape=(), dtype=tf.string),
    'sentence': Text(shape=(), dtype=tf.string),
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
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mctaco-1.0.0.html";
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
@inproceedings{ZKNR19,
    author = {Ben Zhou, Daniel Khashabi, Qiang Ning and Dan Roth},
    title = {"Going on a vacation" takes longer than "Going for a walk": A Study of Temporal Commonsense Understanding },
    booktitle = {EMNLP},
    year = {2019},
}
```
