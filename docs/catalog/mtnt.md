<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mtnt" />
  <meta itemprop="description" content="MTNT: Machine Translation of Noisy Text&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mtnt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mtnt" />
  <meta itemprop="sameAs" content="https://pmichel31415.github.io/mtnt/index.html" />
  <meta itemprop="citation" content="@InProceedings{michel2018mtnt,&#10;  author    = {Michel, Paul  and  Neubig, Graham},&#10;  title     = {MTNT: A Testbed for Machine Translation of Noisy Text},&#10;  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing}&#10;}" />
</div>

# `mtnt`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

MTNT: Machine Translation of Noisy Text

*   **Homepage**:
    [https://pmichel31415.github.io/mtnt/index.html](https://pmichel31415.github.io/mtnt/index.html)

*   **Source code**:
    [`tfds.translate.mtnt.Mtnt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/mtnt/mtnt.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'dst': Text(shape=(), dtype=tf.string),
    'src': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype     | Description
:------ | :----------- | :---- | :-------- | :----------
        | FeaturesDict |       |           |
dst     | Text         |       | tf.string |
src     | Text         |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('src', 'dst')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@InProceedings{michel2018mtnt,
  author    = {Michel, Paul  and  Neubig, Graham},
  title     = {MTNT: A Testbed for Machine Translation of Noisy Text},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing}
}
```


## mtnt/en-fr (default config)

## mtnt/en-ja

## mtnt/fr-en
