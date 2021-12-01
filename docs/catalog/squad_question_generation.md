<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="squad_question_generation" />
  <meta itemprop="description" content="Question generation using squad dataset and data split described in &#x27;Neural&#10;Question Generation from Text: A Preliminary Study&#x27; (Zhou et al, 2017).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;squad_question_generation&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/squad_question_generation" />
  <meta itemprop="sameAs" content="https://github.com/magic282/NQG" />
  <meta itemprop="citation" content="@article{zhou2017neural,&#10;  title={Neural Question Generation from Text: A Preliminary Study},&#10;  author={Zhou, Qingyu and Yang, Nan and Wei, Furu and Tan, Chuanqi and Bao, Hangbo and Zhou, Ming},&#10;  journal={arXiv preprint arXiv:1704.01792},&#10;  year={2017}&#10;}&#10;@article{2016arXiv160605250R,&#10;       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},&#10;                 Konstantin and {Liang}, Percy},&#10;        title = &quot;{SQuAD: 100,000+ Questions for Machine Comprehension of Text}&quot;,&#10;      journal = {arXiv e-prints},&#10;         year = 2016,&#10;          eid = {arXiv:1606.05250},&#10;        pages = {arXiv:1606.05250},&#10;archivePrefix = {arXiv},&#10;       eprint = {1606.05250},&#10;}" />
</div>

# `squad_question_generation`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Question generation using squad dataset and data split described in 'Neural
Question Generation from Text: A Preliminary Study' (Zhou et al, 2017).

*   **Homepage**:
    [https://github.com/magic282/NQG](https://github.com/magic282/NQG)

*   **Source code**:
    [`tfds.text.squad_question_generation.SquadQuestionGeneration`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/squad_question_generation/squad_question_generation.py)

*   **Versions**:

    *   `1.0.0`: Initial build with unique SQuAD QAS ids in each split, using
        passage-level context.

    *   **`2.0.0`** (default): Matches the original split of (Zhou et al, 2017),
        allows both sentence- and passage-level contexts, and uses answers from
        (Zhou et al, 2017).

*   **Download size**: `62.52 MiB`

*   **Dataset size**: `111.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,964
`'train'`      | 86,635
`'validation'` | 8,965

*   **Features**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'context_passage': Text(shape=(), dtype=tf.string),
    'context_sentence': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('context_passage', 'question')`

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/squad_question_generation-2.0.0.html";
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
@article{zhou2017neural,
  title={Neural Question Generation from Text: A Preliminary Study},
  author={Zhou, Qingyu and Yang, Nan and Wei, Furu and Tan, Chuanqi and Bao, Hangbo and Zhou, Ming},
  journal={arXiv preprint arXiv:1704.01792},
  year={2017}
}
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
```

