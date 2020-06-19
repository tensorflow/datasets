<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="wordnet" />
  <meta itemprop="description" content="WordNet is a large lexical database of English. Nouns, verbs,&#10;adjectives and adverbs are grouped into sets of cognitive synonyms (synsets),&#10;each expressing a distinct concept. Synsets are interlinked by means of&#10;conceptual-semantic and lexical relations.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wordnet&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wordnet" />
  <meta itemprop="sameAs" content="https://wordnet.princeton.edu/" />
  <meta itemprop="citation" content="@article{10.1145/219717.219748,&#10;author = {Miller, George A.},&#10;title = {WordNet: A Lexical Database for English},&#10;year = {1995},&#10;issue_date = {Nov. 1995},&#10;publisher = {Association for Computing Machinery},&#10;address = {New York, NY, USA},&#10;volume = {38},&#10;number = {11},&#10;issn = {0001-0782},&#10;url = {https://doi.org/10.1145/219717.219748},&#10;doi = {10.1145/219717.219748},&#10;journal = {Commun. ACM},&#10;month = nov,&#10;pages = {39--41},&#10;numpages = {3}&#10;}&#10;&#10;@incollection{NIPS2013_5071,&#10;title = {Translating Embeddings for Modeling Multi-relational Data},&#10;author = {Bordes, Antoine and Usunier, Nicolas and Garcia-Duran, Alberto and Weston, Jason and Yakhnenko, Oksana},&#10;booktitle = {Advances in Neural Information Processing Systems 26},&#10;editor = {C. J. C. Burges and L. Bottou and M. Welling and Z. Ghahramani and K. Q. Weinberger},&#10;pages = {2787--2795},&#10;year = {2013},&#10;publisher = {Curran Associates, Inc.},&#10;url = {http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf}&#10;}" />
</div>

# `wordnet`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

WordNet is a large lexical database of English. Nouns, verbs, adjectives and
adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a
distinct concept. Synsets are interlinked by means of conceptual-semantic and
lexical relations.

*   **Homepage**:
    [https://wordnet.princeton.edu/](https://wordnet.princeton.edu/)
*   **Source code**:
    [`tfds.text.wordnet.Wordnet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wordnet.py)
*   **Versions**:
    *   **`0.1.0`** (default): No release notes.
*   **Download size**: `3.99 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Features**:

```python
FeaturesDict({
    'lhs': Text(shape=(), dtype=tf.string),
    'relation': Text(shape=(), dtype=tf.string),
    'rhs': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## wordnet/WN18 (default config)

*   **Config description**: This WORDNET TENSOR DATA consists of a collection of
    triplets (synset, relation_type, triplet) extracted from WordNet 3.0
    (http://wordnet.princeton.edu). This data set can be seen as a 3-mode tensor
    depicting ternary relationships between synsets. See
    https://everest.hds.utc.fr/doku.php?id=en:transe.

*   **Dataset size**: `11.07 MiB`

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 5,000
'train'      | 141,442
'validation' | 5,000

*   **Citation**:

```
@article{10.1145/219717.219748,
author = {Miller, George A.},
title = {WordNet: A Lexical Database for English},
year = {1995},
issue_date = {Nov. 1995},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {38},
number = {11},
issn = {0001-0782},
url = {https://doi.org/10.1145/219717.219748},
doi = {10.1145/219717.219748},
journal = {Commun. ACM},
month = nov,
pages = {39--41},
numpages = {3}
}

@incollection{NIPS2013_5071,
title = {Translating Embeddings for Modeling Multi-relational Data},
author = {Bordes, Antoine and Usunier, Nicolas and Garcia-Duran, Alberto and Weston, Jason and Yakhnenko, Oksana},
booktitle = {Advances in Neural Information Processing Systems 26},
editor = {C. J. C. Burges and L. Bottou and M. Welling and Z. Ghahramani and K. Q. Weinberger},
pages = {2787--2795},
year = {2013},
publisher = {Curran Associates, Inc.},
url = {http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf}
}
```

## wordnet/WN18RR

*   **Config description**: Same as WN18 but fixes test leakage through inverse
    relations. See https://github.com/TimDettmers/ConvE.

*   **Dataset size**: `7.02 MiB`

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 3,134
'train'      | 86,835
'validation' | 3,034

*   **Citation**:

```
@article{10.1145/219717.219748,
author = {Miller, George A.},
title = {WordNet: A Lexical Database for English},
year = {1995},
issue_date = {Nov. 1995},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {38},
number = {11},
issn = {0001-0782},
url = {https://doi.org/10.1145/219717.219748},
doi = {10.1145/219717.219748},
journal = {Commun. ACM},
month = nov,
pages = {39--41},
numpages = {3}
}

@inproceedings{dettmers2018conve,
    Author = {Dettmers, Tim and Pasquale, Minervini and Pontus, Stenetorp and Riedel, Sebastian},
    Booktitle = {Proceedings of the 32th AAAI Conference on Artificial Intelligence},
    Title = {Convolutional 2D Knowledge Graph Embeddings},
    Url = {https://arxiv.org/abs/1707.01476},
    Year = {2018},
        pages  = {1811--1818},
    Month = {February}
}
```
