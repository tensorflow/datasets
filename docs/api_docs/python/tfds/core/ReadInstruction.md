<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.ReadInstruction" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_spec"/>
<meta itemprop="property" content="to_absolute"/>
</div>

# tfds.core.ReadInstruction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/tfrecords_reader.py">View
source</a>

## Class `ReadInstruction`

Reading instruction for a dataset.

<!-- Placeholder for "Used in" -->

#### Examples of usage:

```
# The following lines are equivalent:
ds = tfds.load('mnist', split='test[:33%]')
ds = tfds.load('mnist', split=ReadInstruction.from_spec('test[:33%]'))
ds = tfds.load('mnist', split=ReadInstruction('test', to=33, unit='%'))
ds = tfds.load('mnist', split=ReadInstruction(
    'test', from_=0, to=33, unit='%'))

# The following lines are equivalent:
ds = tfds.load('mnist', split='test[:33%]+train[1:-1]')
ds = tfds.load('mnist', split=ReadInstruction.from_spec(
    'test[:33%]+train[1:-1]'))
ds = tfds.load('mnist', split=(
    ReadInstruction.('test', to=33, unit='%') +
    ReadInstruction.('train', from_=1, to=-1, unit='abs')))

# 10-fold validation:
tests = tfds.load(
    'mnist',
    [ReadInstruction('train', from_=k, to=k+10, unit='%')
     for k in range(0, 100, 10)])
trains = tfds.load(
    'mnist',
    [RI('train', to=k, unit='%') + RI('train', from_=k+10, unit='%')
     for k in range(0, 100, 10)])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/tfrecords_reader.py">View
source</a>

```python
__init__(
    split_name,
    rounding='closest',
    from_=None,
    to=None,
    unit=None
)
```

Initialize ReadInstruction.

#### Args:

split_name (str): name of the split to read. Eg: 'train'. rounding (str): The
rounding behaviour to use when percent slicing is used. Ignored when slicing
with absolute indices. Possible values: - 'closest' (default): The specified
percentages are rounded to the closest value. Use this if you want specified
percents to be as much exact as possible. - 'pct1_dropremainder': the specified
percentages are treated as multiple of 1%. Use this option if you want
consistency. Eg: len(5%) == 5 * len(1%). Using this option, one might not be
able to use the full set of examples, if the number of those is not a multiple
of 100. from_ (int): to (int): alternative way of specifying slicing boundaries.
If any of {from_, to, unit} argument is used, slicing cannot be specified as
string. unit (str): optional, one of: '%': to set the slicing unit as percents
of the split size. 'abs': to set the slicing unit as absolute numbers.

## Methods

<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/tfrecords_reader.py">View
source</a>

```python
__add__(other)
```

Returns a new ReadInstruction obj, result of appending other to self.

<h3 id="from_spec"><code>from_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/tfrecords_reader.py">View
source</a>

```python
@classmethod
from_spec(
    cls,
    spec
)
```

Creates a ReadInstruction instance out of a string spec.

#### Args:

spec (str): split(s) + optional slice(s) to read. A slice can be specified,
using absolute numbers (int) or percentages (int). E.g. `test`: test split.
`test + validation`: test split + validation split. `test[10:]`: test split,
minus its first 10 records. `test[:10%]`: first 10% records of test split.
`test[:-5%]+train[40%:60%]`: first 95% of test + middle 20% of train.

#### Returns:

ReadInstruction instance.

<h3 id="to_absolute"><code>to_absolute</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/tfrecords_reader.py">View
source</a>

```python
to_absolute(name2len)
```

Translate instruction into a list of absolute instructions.

Those absolute instructions are then to be added together.

#### Args:

*   <b>`name2len`</b>: dict associating split names to number of examples.

#### Returns:

list of _AbsoluteInstruction instances (corresponds to the + in spec).
