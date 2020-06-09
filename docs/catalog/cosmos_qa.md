<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="cosmos_qa" />
  <meta itemprop="description" content="Cosmos QA is a large-scale dataset of 35.6K problems that require&#10; commonsense-based reading comprehension, formulated as multiple-choice&#10; questions. It focuses on reading between the lines over a diverse collection&#10; of people&#x27;s everyday narratives, asking questions concerning on the likely&#10; causes or effects of events that require reasoning beyond the exact text&#10; spans in the context.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cosmos_qa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cosmos_qa" />
  <meta itemprop="sameAs" content="https://wilburone.github.io/cosmos/" />
  <meta itemprop="citation" content="@inproceedings{huang-etal-2019-cosmos,&#10;    title = &quot;Cosmos {QA}: Machine Reading Comprehension with Contextual Commonsense Reasoning&quot;,&#10;    author = &quot;Huang, Lifu  and&#10;      Le Bras, Ronan  and&#10;      Bhagavatula, Chandra  and&#10;      Choi, Yejin&quot;,&#10;    booktitle = &quot;Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)&quot;,&#10;    year = &quot;2019&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/D19-1243&quot;&#10;}" />
</div>

# `cosmos_qa`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Cosmos QA is a large-scale dataset of 35.6K problems that require
commonsense-based reading comprehension, formulated as multiple-choice
questions. It focuses on reading between the lines over a diverse collection of
people's everyday narratives, asking questions concerning on the likely causes
or effects of events that require reasoning beyond the exact text spans in the
context.

*   **Homepage**:
    [https://wilburone.github.io/cosmos/](https://wilburone.github.io/cosmos/)
*   **Source code**:
    [`tfds.question_answering.cosmos_qa.CosmosQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/cosmos_qa.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `23.27 MiB`
*   **Dataset size**: `27.09 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 6,963
'train'      | 25,262
'validation' | 2,985

*   **Features**:

```python
FeaturesDict({
    'answer0': Text(shape=(), dtype=tf.string),
    'answer1': Text(shape=(), dtype=tf.string),
    'answer2': Text(shape=(), dtype=tf.string),
    'answer3': Text(shape=(), dtype=tf.string),
    'context': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
    'question': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```
@inproceedings{huang-etal-2019-cosmos,
    title = "Cosmos {QA}: Machine Reading Comprehension with Contextual Commonsense Reasoning",
    author = "Huang, Lifu  and
      Le Bras, Ronan  and
      Bhagavatula, Chandra  and
      Choi, Yejin",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    year = "2019",
    url = "https://www.aclweb.org/anthology/D19-1243"
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
