<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xnli" />
  <meta itemprop="description" content="XNLI is a subset of a few thousand examples from MNLI which has been translated&#10;into a 14 different languages (some low-ish resource). As with MNLI, the goal is&#10;to predict textual entailment (does sentence A imply/contradict/neither sentence&#10;B) and is a classification task (given two sentences, predict one of three&#10;labels).&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xnli" />
  <meta itemprop="sameAs" content="https://www.nyu.edu/projects/bowman/xnli/" />
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

`xnli` is configured with `tfds.text.xnli.BuilderConfig` and has the following
configurations predefined (defaults to the first one):

*   `plain_text` (`v0.0.1`) (`Size: 17.04 MiB`): Plain text import of XNLI

## `xnli/plain_text`

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

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 7,500
TEST       | 5,010
VALIDATION | 2,490

## Urls

*   [https://www.nyu.edu/projects/bowman/xnli/](https://www.nyu.edu/projects/bowman/xnli/)

## Supervised keys (for `as_supervised=True`)
`None`

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
