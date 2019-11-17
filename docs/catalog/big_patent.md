<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="big_patent" />
  <meta itemprop="description" content="&#10;BIGPATENT, consisting of 1.3 million records of U.S. patent documents&#10;along with human written abstractive summaries.&#10;Each US patent application is filed under a Cooperative Patent Classification&#10;(CPC) code. There are nine such classification categories:&#10;A (Human Necessities), B (Performing Operations; Transporting),&#10;C (Chemistry; Metallurgy), D (Textiles; Paper), E (Fixed Constructions),&#10;F (Mechanical Engineering; Lightning; Heating; Weapons; Blasting),&#10;G (Physics), H (Electricity), and&#10;Y (General tagging of new or cross-sectional technology)&#10;&#10;There are two features:&#10;  - description: detailed description of patent.&#10;  - summary: Patent abastract.&#10;&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('big_patent', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/big_patent" />
  <meta itemprop="sameAs" content="https://evasharma.github.io/bigpatent/" />
  <meta itemprop="citation" content="&#10;@misc{sharma2019bigpatent,&#10;    title={BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization},&#10;    author={Eva Sharma and Chen Li and Lu Wang},&#10;    year={2019},&#10;    eprint={1906.03741},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `big_patent`

BIGPATENT, consisting of 1.3 million records of U.S. patent documents along with
human written abstractive summaries. Each US patent application is filed under a
Cooperative Patent Classification (CPC) code. There are nine such classification
categories: A (Human Necessities), B (Performing Operations; Transporting), C
(Chemistry; Metallurgy), D (Textiles; Paper), E (Fixed Constructions), F
(Mechanical Engineering; Lightning; Heating; Weapons; Blasting), G (Physics), H
(Electricity), and Y (General tagging of new or cross-sectional technology)

There are two features: - description: detailed description of patent. -
summary: Patent abastract.

*   URL:
    [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)
*   `DatasetBuilder`:
    [`tfds.summarization.big_patent.BigPatent`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/big_patent.py)

`big_patent` is configured with `tfds.summarization.big_patent.BigPatentConfig`
and has the following configurations predefined (defaults to the first one):

*   `all` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under all categories.

*   `a` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)a: Human Necessities

*   `b` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)b: Performing Operations; Transporting

*   `c` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)c: Chemistry; Metallurgy

*   `d` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)d: Textiles; Paper

*   `e` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)e: Fixed Constructions

*   `f` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)f: Mechanical Engineering; Lightning; Heating; Weapons;
    Blasting

*   `g` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)g: Physics

*   `h` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)h: Electricity

*   `y` (`v1.0.0`) (`Size: 6.01 GiB`): Patents under Cooperative Patent
    Classification (CPC)y: General tagging of new or cross-sectional technology

## `big_patent/all`
Patents under all categories.

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,341,362
TRAIN      | 1,207,222
TEST       | 67,072
VALIDATION | 67,068

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/a`
Patents under Cooperative Patent Classification (CPC)a: Human Necessities

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 193,483
TRAIN      | 174,134
TEST       | 9,675
VALIDATION | 9,674

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/b`

Patents under Cooperative Patent Classification (CPC)b: Performing Operations;
Transporting

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 179,467
TRAIN      | 161,520
TEST       | 8,974
VALIDATION | 8,973

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/c`
Patents under Cooperative Patent Classification (CPC)c: Chemistry; Metallurgy

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 112,269
TRAIN      | 101,042
TEST       | 5,614
VALIDATION | 5,613

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/d`
Patents under Cooperative Patent Classification (CPC)d: Textiles; Paper

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 11,294
TRAIN      | 10,164
TEST       | 565
VALIDATION | 565

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/e`
Patents under Cooperative Patent Classification (CPC)e: Fixed Constructions

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 38,271
TRAIN      | 34,443
TEST       | 1,914
VALIDATION | 1,914

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/f`

Patents under Cooperative Patent Classification (CPC)f: Mechanical Engineering;
Lightning; Heating; Weapons; Blasting

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 95,076
TRAIN      | 85,568
TEST       | 4,754
VALIDATION | 4,754

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/g`
Patents under Cooperative Patent Classification (CPC)g: Physics

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 287,706
TRAIN      | 258,935
TEST       | 14,386
VALIDATION | 14,385

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/h`
Patents under Cooperative Patent Classification (CPC)h: Electricity

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 285,577
TRAIN      | 257,019
TEST       | 14,279
VALIDATION | 14,279

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## `big_patent/y`

Patents under Cooperative Patent Classification (CPC)y: General tagging of new
or cross-sectional technology

Versions:

*   **`1.0.0`** (default):

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 138,219
TRAIN      | 124,397
TEST       | 6,911
VALIDATION | 6,911

### Features
```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

### Supervised keys (for `as_supervised=True`)
`(u'description', u'abstract')`

## Citation
```
@misc{sharma2019bigpatent,
    title={BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization},
    author={Eva Sharma and Chen Li and Lu Wang},
    year={2019},
    eprint={1906.03741},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
