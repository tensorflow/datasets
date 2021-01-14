<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quac" />
  <meta itemprop="description" content="Question Answering in Context is a dataset for modeling, understanding,&#10;and participating in information seeking dialog. Data instances consist&#10;of an interactive dialog between two crowd workers: (1) a student who poses&#10;a sequence of freeform questions to learn as much as possible about a hidden&#10;Wikipedia text, and (2) a teacher who answers the questions by providing&#10;short excerpts (spans) from the text. QuAC introduces challenges not found&#10;in existing machine comprehension datasets: its questions are often more&#10;open-ended, unanswerable, or only meaningful within the dialog context.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;quac&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quac" />
  <meta itemprop="sameAs" content="https://quac.ai/" />
  <meta itemprop="citation" content="@article{choi2018quac,&#10;  title={Quac: Question answering in context},&#10;  author={Choi, Eunsol and He, He and Iyyer, Mohit and Yatskar, Mark and Yih, Wen-tau and Choi, Yejin and Liang, Percy and Zettlemoyer, Luke},&#10;  journal={arXiv preprint arXiv:1808.07036},&#10;  year={2018}&#10;}" />
</div>

# `quac`

*   **Description**:

Question Answering in Context is a dataset for modeling, understanding, and
participating in information seeking dialog. Data instances consist of an
interactive dialog between two crowd workers: (1) a student who poses a sequence
of freeform questions to learn as much as possible about a hidden Wikipedia
text, and (2) a teacher who answers the questions by providing short excerpts
(spans) from the text. QuAC introduces challenges not found in existing machine
comprehension datasets: its questions are often more open-ended, unanswerable,
or only meaningful within the dialog context.

*   **Homepage**: [https://quac.ai/](https://quac.ai/)

*   **Source code**:
    [`tfds.text.quac.Quac`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/quac/quac.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `73.47 MiB`

*   **Dataset size**: `298.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 83,568
`'validation'` | 7,354

*   **Features**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': tf.int32,
        'text': Text(shape=(), dtype=tf.string),
    }),
    'background': Text(shape=(), dtype=tf.string),
    'context': Text(shape=(), dtype=tf.string),
    'followup': Text(shape=(), dtype=tf.string),
    'orig_answer': FeaturesDict({
        'answer_start': tf.int32,
        'text': Text(shape=(), dtype=tf.string),
    }),
    'question': Text(shape=(), dtype=tf.string),
    'section_title': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
    'yesno': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('context', 'answers')`

*   **Citation**:

```
@article{choi2018quac,
  title={Quac: Question answering in context},
  author={Choi, Eunsol and He, He and Iyyer, Mohit and Yatskar, Mark and Yih, Wen-tau and Choi, Yejin and Liang, Percy and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:1808.07036},
  year={2018}
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/quac-1.0.0.html";
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