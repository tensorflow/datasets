<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="piqa" />
  <meta itemprop="description" content="Physical IQa: Physical Interaction QA, a new commonsense QA benchmark for naive physics&#10;reasoning focusing on how we interact with everyday objects in everyday situations. This&#10;dataset focuses on affordances of objects, i.e., what actions each physical object affords&#10;(e.g., it is possible to use a shoe as a doorstop), and what physical interactions a group&#10;of objects afford (e.g., it is possible to place an apple on top of a book, but not the&#10;other way around). The dataset requires reasoning about both the prototypical use of&#10;objects (e.g., shoes are used for walking) and non-prototypical but practically plausible&#10;use of objects (e.g., shoes can be used as a doorstop). The dataset includes 20,000 QA&#10;pairs that are either multiple-choice or true/false questions.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;piqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/piqa" />
  <meta itemprop="sameAs" content="https://leaderboard.allenai.org/physicaliqa/submissions/get-started" />
  <meta itemprop="citation" content="@inproceedings{Bisk2020,&#10;  author = {Yonatan Bisk and Rowan Zellers and&#10;            Ronan Le Bras and Jianfeng Gao&#10;            and Yejin Choi},&#10;  title = {PIQA: Reasoning about Physical Commonsense in&#10;           Natural Language},&#10;  booktitle = {Thirty-Fourth AAAI Conference on&#10;               Artificial Intelligence},&#10;  year = {2020},&#10;}" />
</div>

# `piqa`


*   **Description**:

Physical IQa: Physical Interaction QA, a new commonsense QA benchmark for naive
physics reasoning focusing on how we interact with everyday objects in everyday
situations. This dataset focuses on affordances of objects, i.e., what actions
each physical object affords (e.g., it is possible to use a shoe as a doorstop),
and what physical interactions a group of objects afford (e.g., it is possible
to place an apple on top of a book, but not the other way around). The dataset
requires reasoning about both the prototypical use of objects (e.g., shoes are
used for walking) and non-prototypical but practically plausible use of objects
(e.g., shoes can be used as a doorstop). The dataset includes 20,000 QA pairs
that are either multiple-choice or true/false questions.

*   **Homepage**:
    [https://leaderboard.allenai.org/physicaliqa/submissions/get-started](https://leaderboard.allenai.org/physicaliqa/submissions/get-started)

*   **Source code**:
    [`tfds.text.PIQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/piqa.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.74 MiB`

*   **Dataset size**: `5.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 16,113
`'validation'` | 1,838

*   **Features**:

```python
FeaturesDict({
    'goal': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sol1': Text(shape=(), dtype=tf.string),
    'sol2': Text(shape=(), dtype=tf.string),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/piqa-1.0.0.html";
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
@inproceedings{Bisk2020,
  author = {Yonatan Bisk and Rowan Zellers and
            Ronan Le Bras and Jianfeng Gao
            and Yejin Choi},
  title = {PIQA: Reasoning about Physical Commonsense in
           Natural Language},
  booktitle = {Thirty-Fourth AAAI Conference on
               Artificial Intelligence},
  year = {2020},
}
```
