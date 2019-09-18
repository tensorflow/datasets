<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gap" />
  <meta itemprop="description" content="&#10;GAP is a gender-balanced dataset containing 8,908 coreference-labeled pairs of &#10;(ambiguous pronoun, antecedent name), sampled from Wikipedia and released by &#10;Google AI Language for the evaluation of coreference resolution in practical &#10;applications.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gap" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/gap-coreference" />
</div>

# `gap`

GAP is a gender-balanced dataset containing 8,908 coreference-labeled pairs of
(ambiguous pronoun, antecedent name), sampled from Wikipedia and released by
Google AI Language for the evaluation of coreference resolution in practical
applications.

*   URL:
    [https://github.com/google-research-datasets/gap-coreference](https://github.com/google-research-datasets/gap-coreference)
*   `DatasetBuilder`:
    [`tfds.text.gap.Gap`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/gap.py)
*   Version: `v0.1.0`
*   Size: `2.29 MiB`

## Features
```python
FeaturesDict({
    'A': Text(shape=(), dtype=tf.string),
    'A-coref': Tensor(shape=(), dtype=tf.bool),
    'A-offset': Tensor(shape=(), dtype=tf.int32),
    'B': Text(shape=(), dtype=tf.string),
    'B-coref': Tensor(shape=(), dtype=tf.bool),
    'B-offset': Tensor(shape=(), dtype=tf.int32),
    'ID': Text(shape=(), dtype=tf.string),
    'Pronoun': Text(shape=(), dtype=tf.string),
    'Pronoun-offset': Tensor(shape=(), dtype=tf.int32),
    'Text': Text(shape=(), dtype=tf.string),
    'URL': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 4,454
TRAIN      | 2,000
TEST       | 2,000
VALIDATION | 454

## Urls

*   [https://github.com/google-research-datasets/gap-coreference](https://github.com/google-research-datasets/gap-coreference)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
```
@article{DBLP:journals/corr/abs-1810-05201,
  author    = {Kellie Webster and
               Marta Recasens and
               Vera Axelrod and
               Jason Baldridge},
  title     = {Mind the {GAP:} {A} Balanced Corpus of Gendered Ambiguous Pronouns},
  journal   = {CoRR},
  volume    = {abs/1810.05201},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.05201},
  archivePrefix = {arXiv},
  eprint    = {1810.05201},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1810-05201},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
