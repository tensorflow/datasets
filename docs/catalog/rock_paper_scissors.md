<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rock_paper_scissors" />
  <meta itemprop="description" content="Images of hands playing rock, paper, scissor game.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('rock_paper_scissors', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rock_paper_scissors" />
  <meta itemprop="sameAs" content="http://laurencemoroney.com/rock-paper-scissors-dataset" />
  <meta itemprop="citation" content="@ONLINE {rps,&#10;author = &quot;Laurence Moroney&quot;,&#10;title = &quot;Rock, Paper, Scissors Dataset&quot;,&#10;month = &quot;feb&quot;,&#10;year = &quot;2019&quot;,&#10;url = &quot;http://laurencemoroney.com/rock-paper-scissors-dataset&quot;&#10;}&#10;" />
</div>
# `rock_paper_scissors`

Images of hands playing rock, paper, scissor game.

*   URL:
    [http://laurencemoroney.com/rock-paper-scissors-dataset](http://laurencemoroney.com/rock-paper-scissors-dataset)
*   `DatasetBuilder`:
    [`tfds.image.rock_paper_scissors.RockPaperScissors`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/rock_paper_scissors.py)
*   Version: `v1.0.0`
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

## Homepage

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
