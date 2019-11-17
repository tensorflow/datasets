<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xnli" />
  <meta itemprop="description" content="XNLI is a subset of a few thousand examples from MNLI which has been translated&#10;into a 14 different languages (some low-ish resource). As with MNLI, the goal is&#10;to predict textual entailment (does sentence A imply/contradict/neither sentence&#10;B) and is a classification task (given two sentences, predict one of three&#10;labels).&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('xnli', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xnli" />
  <meta itemprop="sameAs" content="https://www.nyu.edu/projects/bowman/xnli/" />
  <meta itemprop="citation" content="@InProceedings{conneau2018xnli,&#10;  author = &quot;Conneau, Alexis&#10;                 and Rinott, Ruty&#10;                 and Lample, Guillaume&#10;                 and Williams, Adina&#10;                 and Bowman, Samuel R.&#10;                 and Schwenk, Holger&#10;                 and Stoyanov, Veselin&quot;,&#10;  title = &quot;XNLI: Evaluating Cross-lingual Sentence Representations&quot;,&#10;  booktitle = &quot;Proceedings of the 2018 Conference on Empirical Methods&#10;               in Natural Language Processing&quot;,&#10;  year = &quot;2018&quot;,&#10;  publisher = &quot;Association for Computational Linguistics&quot;,&#10;  location = &quot;Brussels, Belgium&quot;,&#10;}" />
</div>
# `xnli`

XNLI is a subset of a few thousand examples from MNLI which has been translated
into a 14 different languages (some low-ish resource). As with MNLI, the goal is
to predict textual entailment (does sentence A imply/contradict/neither sentence
B) and is a classification task (given two sentences, predict one of three
labels).

*   URL:
    [https://www.nyu.edu/projects/bowman/xnli/](https://www.nyu.edu/projects/bowman/xnli/)
*   `DatasetBuilder`:
    [`tfds.text.xnli.Xnli`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/xnli.py)

`xnli` is configured with `tfds.core.dataset_builder.BuilderConfig` and has the
following configurations predefined (defaults to the first one):

*   `plain_text` (`v0.0.1`) (`Size: 17.04 MiB`): Plain text import of XNLI

## `xnli/plain_text`
Plain text import of XNLI

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 7,500
TEST       | 5,010
VALIDATION | 2,490

### Features
```python
FeaturesDict({
    'hypothesis': TranslationVariableLanguages({
        'language': Text(shape=(), dtype=tf.string),
        'translation': Text(shape=(), dtype=tf.string),
    }),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Translation({
        'ar': Text(shape=(), dtype=tf.string),
        'bg': Text(shape=(), dtype=tf.string),
        'de': Text(shape=(), dtype=tf.string),
        'el': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
        'es': Text(shape=(), dtype=tf.string),
        'fr': Text(shape=(), dtype=tf.string),
        'hi': Text(shape=(), dtype=tf.string),
        'ru': Text(shape=(), dtype=tf.string),
        'sw': Text(shape=(), dtype=tf.string),
        'th': Text(shape=(), dtype=tf.string),
        'tr': Text(shape=(), dtype=tf.string),
        'ur': Text(shape=(), dtype=tf.string),
        'vi': Text(shape=(), dtype=tf.string),
        'zh': Text(shape=(), dtype=tf.string),
    }),
})
```

### Homepage

*   [https://www.nyu.edu/projects/bowman/xnli/](https://www.nyu.edu/projects/bowman/xnli/)

## Citation
```
@InProceedings{conneau2018xnli,
  author = "Conneau, Alexis
                 and Rinott, Ruty
                 and Lample, Guillaume
                 and Williams, Adina
                 and Bowman, Samuel R.
                 and Schwenk, Holger
                 and Stoyanov, Veselin",
  title = "XNLI: Evaluating Cross-lingual Sentence Representations",
  booktitle = "Proceedings of the 2018 Conference on Empirical Methods
               in Natural Language Processing",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  location = "Brussels, Belgium",
}
```

--------------------------------------------------------------------------------
