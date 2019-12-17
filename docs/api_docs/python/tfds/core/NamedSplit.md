<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.NamedSplit" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="get_read_instruction"/>
<meta itemprop="property" content="subsplit"/>
</div>

# tfds.core.NamedSplit

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

## Class `NamedSplit`

Descriptor corresponding to a named split (train, test, ...).

Inherits From: [`SplitBase`](../../tfds/core/SplitBase.md)

<!-- Placeholder for "Used in" -->

Each descriptor can be composed with other using addition or slice. Ex:

```
split = tfds.Split.TRAIN.subsplit(tfds.percent[0:25]) + tfds.Split.TEST
```

The resulting split will correspond to 25% of the train split merged with
100% of the test split.

#### Warning:

A split cannot be added twice, so the following will fail:

```
split = (
    tfds.Split.TRAIN.subsplit(tfds.percent[:25]) +
    tfds.Split.TRAIN.subsplit(tfds.percent[75:])
)  # Error
split = tfds.Split.TEST + tfds.Split.ALL  # Error
```

#### Warning:

The slices can be applied only one time. So the following are valid:

```
split = (
    tfds.Split.TRAIN.subsplit(tfds.percent[:25]) +
    tfds.Split.TEST.subsplit(tfds.percent[:50])
)
split = (tfds.Split.TRAIN + tfds.Split.TEST).subsplit(tfds.percent[:50])
```

  But not:

```
train = tfds.Split.TRAIN
test = tfds.Split.TEST
split = train.subsplit(tfds.percent[:25]).subsplit(tfds.percent[:25])
split = (train.subsplit(tfds.percent[:25]) + test).subsplit(tfds.percent[:50])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__init__(name)
```

## Methods

<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__add__(other)
```

Merging: tfds.Split.TRAIN + tfds.Split.TEST.

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__eq__(other)
```

Equality: tfds.Split.TRAIN == 'train'.

<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

```python
__ne__(other)
```

InEquality: tfds.Split.TRAIN != 'test'.

<h3 id="get_read_instruction"><code>get_read_instruction</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
get_read_instruction(split_dict)
```

<h3 id="subsplit"><code>subsplit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
subsplit(
    arg=None,
    k=None,
    percent=None,
    weighted=None
)
```

Divides this split into subsplits.

There are 3 ways to define subsplits, which correspond to the 3
arguments `k` (get `k` even subsplits), `percent` (get a slice of the
dataset with <a href="../../tfds/percent.md"><code>tfds.percent</code></a>), and `weighted` (get subsplits with proportions
specified by `weighted`).

#### Examples:

```
# 50% train, 50% test
train, test = split.subsplit(k=2)
# 50% train, 25% test, 25% validation
train, test, validation = split.subsplit(weighted=[2, 1, 1])
# Extract last 20%
subsplit = split.subsplit(tfds.percent[-20:])
```

Warning: k and weighted will be converted into percent which mean that values
below the percent will be rounded up or down. The final split may be bigger to
deal with remainders. For instance:

```
train, test, valid = split.subsplit(k=3)  # 33%, 33%, 34%
s1, s2, s3, s4 = split.subsplit(weighted=[2, 2, 1, 1])  # 33%, 33%, 16%, 18%
```

#### Args:

*   <b>`arg`</b>: If no kwargs are given, `arg` will be interpreted as one of
    `k`, `percent`, or `weighted` depending on the type. For example:
    `split.subsplit(10) # Equivalent to split.subsplit(k=10)
    split.subsplit(tfds.percent[:-20]) # percent=tfds.percent[:-20]
    split.subsplit([1, 1, 2]) # weighted=[1, 1, 2]`
*   <b>`k`</b>: `int` If set, subdivide the split into `k` equal parts.
*   <b>`percent`</b>: `tfds.percent slice`, return a single subsplit
    corresponding to a slice of the original split. For example:
    `split.subsplit(tfds.percent[-20:]) # Last 20% of the dataset`.
*   <b>`weighted`</b>: `list[int]`, return a list of subsplits whose proportions
    match the normalized sum of the list. For example:
    `split.subsplit(weighted=[1, 1, 2]) # 25%, 25%, 50%`.

#### Returns:

A subsplit or list of subsplits extracted from this split object.
