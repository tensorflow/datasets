<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="snli" />
  <meta itemprop="description" content="The SNLI corpus (version 1.0) is a collection of 570k human-written English&#10;sentence pairs manually labeled for balanced classification with the labels&#10;entailment, contradiction, and neutral, supporting the task of natural language&#10;inference (NLI), also known as recognizing textual entailment (RTE).&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('snli', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/snli" />
  <meta itemprop="sameAs" content="https://nlp.stanford.edu/projects/snli/" />
  <meta itemprop="citation" content="@inproceedings{snli:emnlp2015,&#10;    Author = {Bowman, Samuel R. and Angeli, Gabor and Potts, Christopher, and Manning, Christopher D.},&#10;    Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},&#10;  Publisher = {Association for Computational Linguistics},&#10;   Title = {A large annotated corpus for learning natural language inference},&#10;    Year = {2015}&#10;}&#10;" />
</div>

# `snli`

The SNLI corpus (version 1.0) is a collection of 570k human-written English
sentence pairs manually labeled for balanced classification with the labels
entailment, contradiction, and neutral, supporting the task of natural language
inference (NLI), also known as recognizing textual entailment (RTE).

*   URL:
    [https://nlp.stanford.edu/projects/snli/](https://nlp.stanford.edu/projects/snli/)
*   `DatasetBuilder`:
    [`tfds.text.snli.Snli`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/snli.py)

`snli` is configured with `tfds.core.dataset_builder.BuilderConfig` and has the
following configurations predefined (defaults to the first one):

*   `plain_text` (`v0.0.1`) (`Size: 90.17 MiB`): Plain text import of SNLI

## `snli/plain_text`
Plain text import of SNLI

Versions:

*   **`0.0.1`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 570,152
TRAIN      | 550,152
TEST       | 10,000
VALIDATION | 10,000

### Features
```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://nlp.stanford.edu/projects/snli/](https://nlp.stanford.edu/projects/snli/)

## Citation

```
@inproceedings{snli:emnlp2015,
    Author = {Bowman, Samuel R. and Angeli, Gabor and Potts, Christopher, and Manning, Christopher D.},
    Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    Publisher = {Association for Computational Linguistics},
    Title = {A large annotated corpus for learning natural language inference},
    Year = {2015}
}
```

--------------------------------------------------------------------------------
