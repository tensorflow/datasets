<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rock_paper_scissors" />
  <meta itemprop="description" content="Images of hands playing rock, paper, scissor game." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rock_paper_scissors" />
  <meta itemprop="sameAs" content="http://laurencemoroney.com/rock-paper-scissors-dataset" />
</div>

# `rock_paper_scissors`

Images of hands playing rock, paper, scissor game.

*   URL:
    [http://laurencemoroney.com/rock-paper-scissors-dataset](http://laurencemoroney.com/rock-paper-scissors-dataset)
*   `DatasetBuilder`:
    [`tfds.image.rock_paper_scissors.RockPaperScissors`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/rock_paper_scissors.py)
*   Versions:

    *   **`1.0.0`** (default):
    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)

*   Size: `219.53 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(300, 300, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 2,892
TRAIN | 2,520
TEST  | 372

## Urls

*   [http://laurencemoroney.com/rock-paper-scissors-dataset](http://laurencemoroney.com/rock-paper-scissors-dataset)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@ONLINE {rps,
author = "Laurence Moroney",
title = "Rock, Paper, Scissors Dataset",
month = "feb",
year = "2019",
url = "http://laurencemoroney.com/rock-paper-scissors-dataset"
}
```

--------------------------------------------------------------------------------
