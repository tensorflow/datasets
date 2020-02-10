<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cfq" />
  <meta itemprop="description" content="&#10;The CFQ dataset (and it&#x27;s splits) for measuring compositional generalization.&#10;&#10;See https://arxiv.org/abs/1912.09713.pdf for background.&#10;&#10;Example usage:&#10;data = tfds.load(&#x27;cfq/mcd1&#x27;)&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cfq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cfq" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/cfq" />
  <meta itemprop="citation" content="&#10;@inproceedings{Lake2018GeneralizationWS,&#10;  title={Measuring Compositional Generalization: A Comprehensive Method on&#10;         Realistic Data},&#10;  author={Daniel Keysers, et al.},&#10;  booktitle={ICLR},&#10;  year={2020},&#10;  url={https://arxiv.org/abs/1912.09713.pdf},&#10;}&#10;" />
</div>
# `cfq`

The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   URL:
    [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)
*   `DatasetBuilder`:
    [`tfds.text.cfq.CFQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/cfq.py)

`cfq` is configured with `tfds.text.cfq.CFQConfig` and has the following
configurations predefined (defaults to the first one):

*   `mcd1` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset (and it's splits)
    for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `mcd2` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset (and it's splits)
    for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `mcd3` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset (and it's splits)
    for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `question_complexity_split` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset
    (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `question_pattern_split` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset
    (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `query_complexity_split` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset
    (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `query_pattern_split` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset (and
    it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   `random_split` (`v1.0.0`) (`Size: 255.20 MiB`): The CFQ dataset (and it's
    splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

## `cfq/mcd1`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,711
TRAIN | 95,743
TEST  | 11,968

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/mcd2`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,711
TRAIN | 95,743
TEST  | 11,968

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/mcd3`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,711
TRAIN | 95,743
TEST  | 11,968

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/question_complexity_split`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 109,339
TRAIN | 98,999
TEST  | 10,340

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/question_pattern_split`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,563
TRAIN | 95,654
TEST  | 11,909

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/query_complexity_split`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 110,166
TRAIN | 100,654
TEST  | 9,512

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/query_pattern_split`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,189
TRAIN | 94,600
TEST  | 12,589

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## `cfq/random_split`
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

Versions:

*   **`1.0.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 107,711
TRAIN | 95,744
TEST  | 11,967

### Features
```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)

### Supervised keys (for `as_supervised=True`)
`('question', 'query')`

## Citation
```
@inproceedings{Lake2018GeneralizationWS,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers, et al.},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
```

--------------------------------------------------------------------------------
