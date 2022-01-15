<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quality" />
  <meta itemprop="description" content="QuALITY, a multiple-choice, long-reading comprehension dataset.&#10;&#10;We provide only the raw version.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;quality&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quality" />
  <meta itemprop="sameAs" content="https://github.com/nyu-mll/quality" />
  <meta itemprop="citation" content="@article{pang2021quality,&#10;  title={{QuALITY}: Question Answering with Long Input Texts, Yes!},&#10;  author={Pang, Richard Yuanzhe and Parrish, Alicia and Joshi, Nitish and Nangia, Nikita and Phang, Jason and Chen, Angelica and Padmakumar, Vishakh and Ma, Johnny and Thompson, Jana and He, He and Bowman, Samuel R.},&#10;  journal={arXiv preprint arXiv:2112.08608},&#10;  year={2021}&#10;}" />
</div>

# `quality`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

QuALITY, a multiple-choice, long-reading comprehension dataset.

We provide only the raw version.

*   **Homepage**:
    [https://github.com/nyu-mll/quality](https://github.com/nyu-mll/quality)

*   **Source code**:
    [`tfds.text.quality.Quality`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/quality/quality.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `17.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 230
`'test'`  | 232
`'train'` | 300

*   **Features**:

```python
FeaturesDict({
    'article': Text(shape=(), dtype=tf.string),
    'article_id': Text(shape=(), dtype=tf.string),
    'difficults': Sequence(tf.bool),
    'gold_labels': Sequence(tf.int32),
    'options': Sequence(Sequence(Text(shape=(), dtype=tf.string))),
    'question_ids': Sequence(Text(shape=(), dtype=tf.string)),
    'questions': Sequence(Text(shape=(), dtype=tf.string)),
    'set_unique_id': Text(shape=(), dtype=tf.string),
    'source': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
    'topic': Text(shape=(), dtype=tf.string),
    'url': Text(shape=(), dtype=tf.string),
    'writer_id': Text(shape=(), dtype=tf.string),
    'writer_labels': Sequence(tf.int32),
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
    Missing.

*   **Citation**:

```
@article{pang2021quality,
  title={{QuALITY}: Question Answering with Long Input Texts, Yes!},
  author={Pang, Richard Yuanzhe and Parrish, Alicia and Joshi, Nitish and Nangia, Nikita and Phang, Jason and Chen, Angelica and Padmakumar, Vishakh and Ma, Johnny and Thompson, Jana and He, He and Bowman, Samuel R.},
  journal={arXiv preprint arXiv:2112.08608},
  year={2021}
}
```


## quality/raw (default config)

*   **Config description**: Raw with HTML.

*   **Dataset size**: `22.18 MiB`

## quality/stripped

*   **Config description**: Stripped of HTML.

*   **Dataset size**: `20.73 MiB`
