<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="qasc" />
  <meta itemprop="description" content="QASC is a question-answering dataset with a focus on sentence composition. It consists of 9,980 8-way multiple-choice&#10;questions about grade school science (8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;qasc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/qasc" />
  <meta itemprop="sameAs" content="https://allenai.org/data/qasc" />
  <meta itemprop="citation" content="@article{allenai:qasc,&#10;      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},&#10;      title     = {QASC: A Dataset for Question Answering via Sentence Composition},&#10;      journal   = {arXiv:1910.11473v2},&#10;      year      = {2020},&#10;}" />
</div>

# `qasc`


*   **Description**:

QASC is a question-answering dataset with a focus on sentence composition. It
consists of 9,980 8-way multiple-choice questions about grade school science
(8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.

*   **Homepage**: [https://allenai.org/data/qasc](https://allenai.org/data/qasc)

*   **Source code**:
    [`tfds.question_answering.qasc.Qasc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/qasc/qasc.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `1.54 MiB`

*   **Dataset size**: `6.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Features**:

```python
FeaturesDict({
    'answerKey': Text(shape=(), dtype=tf.string),
    'choices': Sequence({
        'label': Text(shape=(), dtype=tf.string),
        'text': Text(shape=(), dtype=tf.string),
    }),
    'combinedfact': Text(shape=(), dtype=tf.string),
    'fact1': Text(shape=(), dtype=tf.string),
    'fact2': Text(shape=(), dtype=tf.string),
    'formatted_question': Text(shape=(), dtype=tf.string),
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

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/qasc-0.1.0.html";
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
@article{allenai:qasc,
      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},
      title     = {QASC: A Dataset for Question Answering via Sentence Composition},
      journal   = {arXiv:1910.11473v2},
      year      = {2020},
}
```
