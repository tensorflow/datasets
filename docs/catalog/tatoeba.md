<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tatoeba" />
  <meta itemprop="description" content="This data is extracted from the Tatoeba corpus, dated Saturday 2018/11/17.&#10;&#10;For each languages, we have selected 1000 English sentences and their&#10;translations, if available. Please check this paper for a description of the&#10;languages, their families and  scripts as well as baseline results.&#10;&#10;Please note that the English sentences are not identical for all language pairs.&#10;This means that the results are not directly comparable across languages.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tatoeba&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tatoeba" />
  <meta itemprop="sameAs" content="http://opus.nlpl.eu/Tatoeba.php" />
  <meta itemprop="citation" content="@article{tatoeba,&#10;          title={Massively Multilingual Sentence Embeddings for Zero-Shot&#10;                   Cross-Lingual Transfer and Beyond},&#10;          author={Mikel, Artetxe and Holger, Schwenk,},&#10;          journal={arXiv:1812.10464v2},&#10;          year={2018}&#10;}&#10;&#10;@InProceedings{TIEDEMANN12.463,&#10;  author = {J{&quot;o}rg}rg Tiedemann},&#10;  title = {Parallel Data, Tools and Interfaces in OPUS},&#10;  booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC&#x27;12)},&#10;  year = {2012},&#10;  month = {may},&#10;  date = {23-25},&#10;  address = {Istanbul, Turkey},&#10;  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},&#10;  publisher = {European Language Resources Association (ELRA)},&#10;  isbn = {978-2-9517408-7-7},&#10;  language = {english}&#10;}" />
</div>

# `tatoeba`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

This data is extracted from the Tatoeba corpus, dated Saturday 2018/11/17.

For each languages, we have selected 1000 English sentences and their
translations, if available. Please check this paper for a description of the
languages, their families and scripts as well as baseline results.

Please note that the English sentences are not identical for all language pairs.
This means that the results are not directly comparable across languages.

*   **Homepage**:
    [http://opus.nlpl.eu/Tatoeba.php](http://opus.nlpl.eu/Tatoeba.php)

*   **Source code**:
    [`tfds.translate.tatoeba.Tatoeba`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/tatoeba/tatoeba.py)

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
    'source_language': Text(shape=(), dtype=tf.string),
    'source_sentence': Text(shape=(), dtype=tf.string),
    'target_language': Text(shape=(), dtype=tf.string),
    'target_sentence': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype     | Description
:-------------- | :----------- | :---- | :-------- | :----------
                | FeaturesDict |       |           |
source_language | Text         |       | tf.string |
source_sentence | Text         |       | tf.string |
target_language | Text         |       | tf.string |
target_sentence | Text         |       | tf.string |

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
@article{tatoeba,
          title={Massively Multilingual Sentence Embeddings for Zero-Shot
                   Cross-Lingual Transfer and Beyond},
          author={Mikel, Artetxe and Holger, Schwenk,},
          journal={arXiv:1812.10464v2},
          year={2018}
}

@InProceedings{TIEDEMANN12.463,
  author = {J{"o}rg}rg Tiedemann},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
  year = {2012},
  month = {may},
  date = {23-25},
  address = {Istanbul, Turkey},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {978-2-9517408-7-7},
  language = {english}
}
```


## tatoeba/tatoeba_af (default config)

## tatoeba/tatoeba_ar

## tatoeba/tatoeba_bg

## tatoeba/tatoeba_bn

## tatoeba/tatoeba_de

## tatoeba/tatoeba_el

## tatoeba/tatoeba_es

## tatoeba/tatoeba_et

## tatoeba/tatoeba_eu

## tatoeba/tatoeba_fa

## tatoeba/tatoeba_fi

## tatoeba/tatoeba_fr

## tatoeba/tatoeba_he

## tatoeba/tatoeba_hi

## tatoeba/tatoeba_hu

## tatoeba/tatoeba_id

## tatoeba/tatoeba_it

## tatoeba/tatoeba_ja

## tatoeba/tatoeba_jv

## tatoeba/tatoeba_ka

## tatoeba/tatoeba_kk

## tatoeba/tatoeba_ko

## tatoeba/tatoeba_ml

## tatoeba/tatoeba_mr

## tatoeba/tatoeba_nl

## tatoeba/tatoeba_pt

## tatoeba/tatoeba_ru

## tatoeba/tatoeba_sw

## tatoeba/tatoeba_ta

## tatoeba/tatoeba_te

## tatoeba/tatoeba_th

## tatoeba/tatoeba_tl

## tatoeba/tatoeba_tr

## tatoeba/tatoeba_ur

## tatoeba/tatoeba_vi

## tatoeba/tatoeba_zh
