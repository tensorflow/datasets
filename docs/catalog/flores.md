<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="flores" />
  <meta itemprop="description" content="Evaluation datasets for low-resource machine translation: Nepali-English and Sinhala-English.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('flores', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/flores" />
  <meta itemprop="sameAs" content="https://github.com/facebookresearch/flores/" />
  <meta itemprop="citation" content="@misc{guzmn2019new,&#10;    title={Two New Evaluation Datasets for Low-Resource Machine Translation: Nepali-English and Sinhala-English},&#10;    author={Francisco Guzman and Peng-Jen Chen and Myle Ott and Juan Pino and Guillaume Lample and Philipp Koehn and Vishrav Chaudhary and Marc'Aurelio Ranzato},&#10;    year={2019},&#10;    eprint={1902.01382},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `flores`

Evaluation datasets for low-resource machine translation: Nepali-English and
Sinhala-English.

*   URL:
    [https://github.com/facebookresearch/flores/](https://github.com/facebookresearch/flores/)
*   `DatasetBuilder`:
    [`tfds.translate.flores.Flores`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/flores.py)

`flores` is configured with `tfds.translate.flores.FloresConfig` and has the
following configurations predefined (defaults to the first one):

*   `neen_plain_text` (`v0.0.3`) (`Size: 984.65 KiB`): Translation dataset from
    ne to en, uses encoder plain_text.

*   `sien_plain_text` (`v0.0.3`) (`Size: 984.65 KiB`): Translation dataset from
    si to en, uses encoder plain_text.

## `flores/neen_plain_text`
Translation dataset from ne to en, uses encoder plain_text.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,394
TEST       | 2,835
VALIDATION | 2,559

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ne': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/facebookresearch/flores/](https://github.com/facebookresearch/flores/)

### Supervised keys (for `as_supervised=True`)
`(u'ne', u'en')`

## `flores/sien_plain_text`
Translation dataset from si to en, uses encoder plain_text.

Versions:

*   **`0.0.3`** (default):
*   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,664
VALIDATION | 2,898
TEST       | 2,766

### Features
```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'si': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/facebookresearch/flores/](https://github.com/facebookresearch/flores/)

### Supervised keys (for `as_supervised=True`)
`(u'si', u'en')`

## Citation
```
@misc{guzmn2019new,
    title={Two New Evaluation Datasets for Low-Resource Machine Translation: Nepali-English and Sinhala-English},
    author={Francisco Guzman and Peng-Jen Chen and Myle Ott and Juan Pino and Guillaume Lample and Philipp Koehn and Vishrav Chaudhary and Marc'Aurelio Ranzato},
    year={2019},
    eprint={1902.01382},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
