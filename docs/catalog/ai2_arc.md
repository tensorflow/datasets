<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ai2_arc" />
  <meta itemprop="description" content="A new dataset of 7,787 genuine grade-school level, multiple-choice science&#10;questions, assembled to encourage research in advanced question-answering.&#10;The dataset is partitioned into a Challenge Set and an Easy Set, where the&#10;former contains only questions answered incorrectly by both a retrieval-based&#10;algorithm and a word co-occurrence algorithm. We are also including a corpus&#10;of over 14 million science sentences relevant to the task, and an&#10;implementation of three neural baseline models for this dataset.&#10;We pose ARC as a challenge to the community.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ai2_arc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ai2_arc" />
  <meta itemprop="sameAs" content="https://allenai.org/data/arc" />
  <meta itemprop="citation" content="@article{allenai:arc,&#10;      author    = {Peter Clark  and Isaac Cowhey and Oren Etzioni and Tushar Khot and&#10;                    Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},&#10;      title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},&#10;      journal   = {arXiv:1803.05457v1},&#10;      year      = {2018},&#10;}" />
</div>

# `ai2_arc`


*   **Description**:

A new dataset of 7,787 genuine grade-school level, multiple-choice science
questions, assembled to encourage research in advanced question-answering. The
dataset is partitioned into a Challenge Set and an Easy Set, where the former
contains only questions answered incorrectly by both a retrieval-based algorithm
and a word co-occurrence algorithm. We are also including a corpus of over 14
million science sentences relevant to the task, and an implementation of three
neural baseline models for this dataset. We pose ARC as a challenge to the
community.

*   **Homepage**: [https://allenai.org/data/arc](https://allenai.org/data/arc)

*   **Source code**:
    [`tfds.question_answering.Ai2Arc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/ai2_arc.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `649.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'answerKey': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
    'choices': Sequence({
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
        'text': Text(shape=(), dtype=tf.string),
    }),
    'id': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{allenai:arc,
      author    = {Peter Clark  and Isaac Cowhey and Oren Etzioni and Tushar Khot and
                    Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
      title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
      journal   = {arXiv:1803.05457v1},
      year      = {2018},
}
```

## ai2_arc/ARC-Challenge (default config)

*   **Config description**: Challenge Set of 2590 "hard" questions (those that
    both a retrieval and a co-occurrence method fail to answer correctly)

*   **Dataset size**: `939.91 KiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,172
`'train'`      | 1,119
`'validation'` | 299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ai2_arc-ARC-Challenge-1.0.0.html";
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

## ai2_arc/ARC-Easy

*   **Config description**: Easy Set of 5197 questions for the ARC Challenge.

*   **Dataset size**: `1.63 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,376
`'train'`      | 2,251
`'validation'` | 570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ai2_arc-ARC-Easy-1.0.0.html";
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