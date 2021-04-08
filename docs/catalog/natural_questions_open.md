<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="natural_questions_open" />
  <meta itemprop="description" content="The NQ-Open task, introduced by Lee et.al. 2019, is an open domain question answering benchmark that is derived from Natural Questions. The goal is to predict an English answer string for an input English question. All questions can be answered using the contents of English Wikipedia.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;natural_questions_open&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/natural_questions_open" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/natural-questions/tree/master/nq_open" />
  <meta itemprop="citation" content="@inproceedings{orqa,&#10;title = {Latent Retrieval for Weakly Supervised Open Domain Question Answering},&#10;author = {Lee, Kenton and Chang, Ming-Wei and Toutanova, Kristina},&#10;year = {2019},&#10;month = {01},&#10;pages = {6086-6096},&#10;booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},&#10;doi = {10.18653/v1/P19-1612}&#10;}&#10;&#10;@article{47761,&#10;title = {Natural Questions: a Benchmark for Question Answering Research},&#10;author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},&#10;year = {2019},&#10;journal = {Transactions of the Association of Computational Linguistics}&#10;}" />
</div>

# `natural_questions_open`

*   **Description**:

The NQ-Open task, introduced by Lee et.al. 2019, is an open domain question
answering benchmark that is derived from Natural Questions. The goal is to
predict an English answer string for an input English question. All questions
can be answered using the contents of English Wikipedia.

*   **Homepage**:
    [https://github.com/google-research-datasets/natural-questions/tree/master/nq_open](https://github.com/google-research-datasets/natural-questions/tree/master/nq_open)

*   **Source code**:
    [`tfds.question_answering.NaturalQuestionsOpen`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/natural_questions_open.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `8.50 MiB`

*   **Dataset size**: `8.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 87,925
`'validation'` | 3,610

*   **Features**:

```python
FeaturesDict({
    'answer': Sequence(tf.string),
    'question': tf.string,
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/natural_questions_open-1.0.0.html";
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
@inproceedings{orqa,
title = {Latent Retrieval for Weakly Supervised Open Domain Question Answering},
author = {Lee, Kenton and Chang, Ming-Wei and Toutanova, Kristina},
year = {2019},
month = {01},
pages = {6086-6096},
booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
doi = {10.18653/v1/P19-1612}
}

@article{47761,
title = {Natural Questions: a Benchmark for Question Answering Research},
author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
year = {2019},
journal = {Transactions of the Association of Computational Linguistics}
}
```
