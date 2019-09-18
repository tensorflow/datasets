<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="omniglot" />
  <meta itemprop="description" content="Omniglot data set for one-shot learning. This dataset contains 1623 different&#10;handwritten characters from 50 different alphabets.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/omniglot" />
  <meta itemprop="sameAs" content="https://github.com/brendenlake/omniglot/" />
</div>

# `omniglot`

Omniglot data set for one-shot learning. This dataset contains 1623 different
handwritten characters from 50 different alphabets.

*   URL:
    [https://github.com/brendenlake/omniglot/](https://github.com/brendenlake/omniglot/)
*   `DatasetBuilder`:
    [`tfds.image.omniglot.Omniglot`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/omniglot.py)
*   Version: `v1.0.0`
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

## Urls

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
