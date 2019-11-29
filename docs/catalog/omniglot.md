<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="omniglot" />
  <meta itemprop="description" content="Omniglot data set for one-shot learning. This dataset contains 1623 different&#10;handwritten characters from 50 different alphabets.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('omniglot', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/omniglot" />
  <meta itemprop="sameAs" content="https://github.com/brendenlake/omniglot/" />
  <meta itemprop="citation" content="@article{lake2015human,&#10;  title={Human-level concept learning through probabilistic program induction},&#10;  author={Lake, Brenden M and Salakhutdinov, Ruslan and Tenenbaum, Joshua B},&#10;  journal={Science},&#10;  volume={350},&#10;  number={6266},&#10;  pages={1332--1338},&#10;  year={2015},&#10;  publisher={American Association for the Advancement of Science}&#10;}&#10;" />
</div>
# `omniglot`

Omniglot data set for one-shot learning. This dataset contains 1623 different
handwritten characters from 50 different alphabets.

*   URL:
    [https://github.com/brendenlake/omniglot/](https://github.com/brendenlake/omniglot/)
*   `DatasetBuilder`:
    [`tfds.image.omniglot.Omniglot`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/omniglot.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `17.95 MiB`

## Features
```python
FeaturesDict({
    'alphabet': ClassLabel(shape=(), dtype=tf.int64, num_classes=50),
    'alphabet_char_id': Tensor(shape=(), dtype=tf.int64),
    'image': Image(shape=(105, 105, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1623),
})
```

## Statistics

Split  | Examples
:----- | -------:
ALL    | 38,300
TRAIN  | 19,280
TEST   | 13,180
SMALL2 | 3,120
SMALL1 | 2,720

## Homepage

*   [https://github.com/brendenlake/omniglot/](https://github.com/brendenlake/omniglot/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{lake2015human,
  title={Human-level concept learning through probabilistic program induction},
  author={Lake, Brenden M and Salakhutdinov, Ruslan and Tenenbaum, Joshua B},
  journal={Science},
  volume={350},
  number={6266},
  pages={1332--1338},
  year={2015},
  publisher={American Association for the Advancement of Science}
}
```

--------------------------------------------------------------------------------
