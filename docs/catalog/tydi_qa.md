<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tydi_qa" />
  <meta itemprop="description" content="TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs. The languages of TyDi QA are diverse with regard to their typology -- the set of linguistic features that each language expresses -- such that we expect models performing well on this set to generalize across a large number of the languages in the world. It contains language phenomena that would not be found in English-only corpora. To provide a realistic information-seeking task and avoid priming effects, questions are written by people who want to know the answer, but don’t know the answer yet, (unlike SQuAD and its descendents) and the data is collected directly in each language without the use of translation (unlike MLQA and XQuAD).&#10;&#10;For now, only the Gold passage (GoldP) task is available in TFDS.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tydi_qa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tydi_qa" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/tydiqa" />
  <meta itemprop="citation" content="@article{tydiqa,&#10;   title = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},&#10;  author = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}&#10;    year = {2020},&#10; journal = {Transactions of the Association for Computational Linguistics}&#10;}" />
</div>
# `tydi_qa`

*   **Description**:

TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs. The languages of TyDi QA are diverse with regard to their typology -- the set of linguistic features that each language expresses -- such that we expect models performing well on this set to generalize across a large number of the languages in the world. It contains language phenomena that would not be found in English-only corpora. To provide a realistic information-seeking task and avoid priming effects, questions are written by people who want to know the answer, but don’t know the answer yet, (unlike SQuAD and its descendents) and the data is collected directly in each language without the use of translation (unlike MLQA and XQuAD).

For now, only the Gold passage (GoldP) task is available in TFDS.

*   **Config description**: Gold passage (GoldP) task (https://github.com/google-research-datasets/tydiqa/tree/master/gold_passage_baseline).

*   **Homepage**: [https://github.com/google-research-datasets/tydiqa](https://github.com/google-research-datasets/tydiqa)

*   **Source code**: [`tfds.question_answering.TydiQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/tydi_qa.py)

*   **Versions**:

    * **`2.0.0`** (default): No release notes.

*   **Download size**: `62.32 MiB`

*   **Dataset size**: `65.22 MiB`

*   **Auto-cached** ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)): Yes

*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 49,881
`'validation'` | 5,077
`'validation-ar'` | 921
`'validation-bn'` | 113
`'validation-en'` | 440
`'validation-fi'` | 782
`'validation-id'` | 565
`'validation-ko'` | 276
`'validation-ru'` | 812
`'validation-sw'` | 499
`'validation-te'` | 669

*   **Features**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': tf.int32,
        'text': Text(shape=(), dtype=tf.string),
    }),
    'context': Text(shape=(), dtype=tf.string),
    'id': tf.string,
    'question': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)): `None`

*   **Citation**:

```
@article{tydiqa,
   title = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
  author = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
    year = {2020},
 journal = {Transactions of the Association for Computational Linguistics}
}
```

*   **Figure** ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)): Not supported.

*   **Examples** ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>

<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>

<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tydi_qa-goldp-2.0.0.html";
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

## tydi_qa/goldp (default config)
