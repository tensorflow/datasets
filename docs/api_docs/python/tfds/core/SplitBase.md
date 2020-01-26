<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitBase" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="get_read_instruction"/>
<meta itemprop="property" content="subsplit"/>
</div>

# tfds.core.SplitBase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

## Class `SplitBase`

Abstract base class for Split compositionality.

<!-- Placeholder for "Used in" -->

See the
[guide on splits](https://github.com/tensorflow/datasets/tree/master/docs/splits.md)
for more information.

There are three parts to the composition:
  1) The splits are composed (defined, merged, split,...) together before
     calling the `.as_dataset()` function. This is done with the `__add__`,
     `__getitem__`, which return a tree of `SplitBase` (whose leaf
     are the `NamedSplit` objects)

```
  split = tfds.Split.TRAIN + tfds.Split.TEST.subsplit(tfds.percent[:50])
```

  2) The `SplitBase` is forwarded to the `.as_dataset()` function
     to be resolved into actual read instruction. This is done by the
     `.get_read_instruction()` method which takes the real dataset splits
     (name, number of shards,...) and parse the tree to return a
     `SplitReadInstruction()` object

  ```
  read_instruction = split.get_read_instruction(self.info.splits)
  ```

  3) The `SplitReadInstruction` is then used in the `tf.data.Dataset` pipeline
     to define which files to read and how to skip examples within file.

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

Parse the descriptor tree and compile all read instructions together.

#### Args:

* <b>`split_dict`</b>: `dict`, The `dict[split_name, SplitInfo]` of the dataset


#### Returns:

* <b>`split_read_instruction`</b>: `SplitReadInstruction`

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
