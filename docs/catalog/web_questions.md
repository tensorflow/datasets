<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="web_questions" />
  <meta itemprop="description" content="This dataset consists of 6,642 question/answer pairs.&#10;The questions are supposed to be answerable by Freebase, a large knowledge graph.&#10;The questions are mostly centered around a single named entity.&#10;The questions are popular ones asked on the web (at least in 2013).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;web_questions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/web_questions" />
  <meta itemprop="sameAs" content="https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a" />
  <meta itemprop="citation" content="@inproceedings{berant-etal-2013-semantic,&#10;    title = &quot;Semantic Parsing on {F}reebase from Question-Answer Pairs&quot;,&#10;    author = &quot;Berant, Jonathan  and&#10;      Chou, Andrew  and&#10;      Frostig, Roy  and&#10;      Liang, Percy&quot;,&#10;    booktitle = &quot;Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = oct,&#10;    year = &quot;2013&quot;,&#10;    address = &quot;Seattle, Washington, USA&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/D13-1160&quot;,&#10;    pages = &quot;1533--1544&quot;,&#10;}" />
</div>
# `web_questions`

*   **Description**:

This dataset consists of 6,642 question/answer pairs. The questions are supposed
to be answerable by Freebase, a large knowledge graph. The questions are mostly
centered around a single named entity. The questions are popular ones asked on
the web (at least in 2013).

*   **Homepage**:
    [https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a](https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a)
*   **Source code**:
    [`tfds.text.web_questions.WebQuestions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/web_questions.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `1.21 MiB`
*   **Dataset size**: `983.88 KiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 2,032
'train' | 3,778

*   **Features**:

```python
FeaturesDict({
    'answers': Sequence(Text(shape=(), dtype=tf.string)),
    'question': Text(shape=(), dtype=tf.string),
    'url': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```
@inproceedings{berant-etal-2013-semantic,
    title = "Semantic Parsing on {F}reebase from Question-Answer Pairs",
    author = "Berant, Jonathan  and
      Chou, Andrew  and
      Frostig, Roy  and
      Liang, Percy",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1160",
    pages = "1533--1544",
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
