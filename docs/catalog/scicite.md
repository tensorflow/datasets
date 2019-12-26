<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scicite" />
  <meta itemprop="description" content="&#10;This is a dataset for classifying citation intents in academic papers.&#10;The main citation intent label for each Json object is specified with the label&#10;key while the citation context is specified in with a context key. Example:&#10;{&#10; 'string': 'In chacma baboons, male-infant relationships can be linked to both&#10;    formation of friendships and paternity success [30,31].'&#10; 'sectionName': 'Introduction',&#10; 'label': 'background',&#10; 'citingPaperId': '7a6b2d4b405439',&#10; 'citedPaperId': '9d1abadc55b5e0',&#10; ...&#10; }&#10;You may obtain the full information about the paper using the provided paper ids&#10;with the Semantic Scholar API (https://api.semanticscholar.org/).&#10;The labels are:&#10;Method, Background, Result&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('scicite', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scicite" />
  <meta itemprop="sameAs" content="https://github.com/allenai/scicite" />
  <meta itemprop="citation" content="&#10;@InProceedings{Cohan2019Structural,&#10;  author={Arman Cohan and Waleed Ammar and Madeleine Van Zuylen and Field Cady},&#10;  title={Structural Scaffolds for Citation Intent Classification in Scientific Publications},&#10;  booktitle=&quot;NAACL&quot;,&#10;  year=&quot;2019&quot;&#10;}&#10;" />
</div>
# `scicite`

This is a dataset for classifying citation intents in academic papers. The main
citation intent label for each Json object is specified with the label key while
the citation context is specified in with a context key. Example: { 'string':
'In chacma baboons, male-infant relationships can be linked to both formation of
friendships and paternity success [30,31].' 'sectionName': 'Introduction',
'label': 'background', 'citingPaperId': '7a6b2d4b405439', 'citedPaperId':
'9d1abadc55b5e0', ... } You may obtain the full information about the paper
using the provided paper ids with the Semantic Scholar API
(https://api.semanticscholar.org/). The labels are: Method, Background, Result

*   URL:
    [https://github.com/allenai/scicite](https://github.com/allenai/scicite)
*   `DatasetBuilder`:
    [`tfds.text.scicite.Scicite`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/scicite.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

*   Size: `22.12 MiB`

## Features
```python
FeaturesDict({
    'citeEnd': Tensor(shape=(), dtype=tf.int64),
    'citeStart': Tensor(shape=(), dtype=tf.int64),
    'citedPaperId': Text(shape=(), dtype=tf.string),
    'citingPaperId': Text(shape=(), dtype=tf.string),
    'excerpt_index': Tensor(shape=(), dtype=tf.int32),
    'id': Text(shape=(), dtype=tf.string),
    'isKeyCitation': Tensor(shape=(), dtype=tf.bool),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'label2': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
    'label2_confidence': Tensor(shape=(), dtype=tf.float32),
    'label_confidence': Tensor(shape=(), dtype=tf.float32),
    'sectionName': Text(shape=(), dtype=tf.string),
    'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=7),
    'string': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 10,969
TRAIN      | 8,194
TEST       | 1,859
VALIDATION | 916

## Homepage

*   [https://github.com/allenai/scicite](https://github.com/allenai/scicite)

## Supervised keys (for `as_supervised=True`)
`(u'string', u'label')`

## Citation
```
@InProceedings{Cohan2019Structural,
  author={Arman Cohan and Waleed Ammar and Madeleine Van Zuylen and Field Cady},
  title={Structural Scaffolds for Citation Intent Classification in Scientific Publications},
  booktitle="NAACL",
  year="2019"
}
```

--------------------------------------------------------------------------------
