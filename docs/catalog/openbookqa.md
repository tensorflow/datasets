<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="openbookqa" />
  <meta itemprop="description" content="The dataset contains 5,957 4-way multiple choice questions. Additionally, they&#10;provide 5,167 crowd-sourced common knowledge facts, and an expanded version of&#10;the train/dev/test questions where each question is associated with its&#10;originating core fact, a human accuracy score, a clarity score, and an&#10;anonymized crowd-worker ID.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;openbookqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/openbookqa" />
  <meta itemprop="sameAs" content="https://leaderboard.allenai.org/open_book_qa/submissions/get-started" />
  <meta itemprop="citation" content="@article{mihaylov2018can,&#10;  title={Can a suit of armor conduct electricity? a new dataset for open book question answering},&#10;  author={Mihaylov, Todor and Clark, Peter and Khot, Tushar and Sabharwal, Ashish},&#10;  journal={arXiv preprint arXiv:1809.02789},&#10;  year={2018}&#10;}" />
</div>

# `openbookqa`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The dataset contains 5,957 4-way multiple choice questions. Additionally, they
provide 5,167 crowd-sourced common knowledge facts, and an expanded version of
the train/dev/test questions where each question is associated with its
originating core fact, a human accuracy score, a clarity score, and an
anonymized crowd-worker ID.

*   **Homepage**:
    [https://leaderboard.allenai.org/open_book_qa/submissions/get-started](https://leaderboard.allenai.org/open_book_qa/submissions/get-started)
*   **Source code**:
    [`tfds.text.openbookqa.Openbookqa`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/openbookqa.py)
*   **Versions**:
    *   **`0.1.0`** (default): No release notes.
*   **Download size**: `1.38 MiB`
*   **Dataset size**: `2.40 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 500
'train'      | 4,957
'validation' | 500

*   **Features**:

```python
FeaturesDict({
    'answerKey': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
    'clarity': tf.float32,
    'fact1': Text(shape=(), dtype=tf.string),
    'humanScore': tf.float32,
    'question': FeaturesDict({
        'choice_A': Text(shape=(), dtype=tf.string),
        'choice_B': Text(shape=(), dtype=tf.string),
        'choice_C': Text(shape=(), dtype=tf.string),
        'choice_D': Text(shape=(), dtype=tf.string),
        'stem': Text(shape=(), dtype=tf.string),
    }),
    'turkIdAnonymized': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('question', 'answerKey')`
*   **Citation**:

```
@article{mihaylov2018can,
  title={Can a suit of armor conduct electricity? a new dataset for open book question answering},
  author={Mihaylov, Todor and Clark, Peter and Khot, Tushar and Sabharwal, Ashish},
  journal={arXiv preprint arXiv:1809.02789},
  year={2018}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
