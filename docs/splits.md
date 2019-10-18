# Splits and slicing

All `DatasetBuilder`s expose various data subsets defined as splits (eg:
`train`, `test`). When constructing a `tf.data.Dataset` instance using either
`tfds.load()` or `tfds.DatasetBuilder.as_dataset()`, one can specify which
split(s) to retrieve. It is also possible to retrieve slice(s) of split(s)
as well as combinations of those.

 * [Two APIs: S3 and legacy](#two-apis-s3-and-legacy)
 * [S3 slicing API](#s3-slicing-api)
   * [Examples](#examples)
   * [Percentage slicing and rounding](#percentage-slicing-and-rounding)
   * [Reproducibility](#reproducibility)
 * [Legacy slicing API](#legacy-slicing-api)
   * [Adding splits together](#adding-splits-together)
   * [Subsplit](#subsplit)
     * [Specifying number of subsplits](#specifying-number-of-subsplits)
     * [Specifying a percentage slice](#specifying-a-percentage-slice)
     * [Specifying weights](#specifying-weights)
   * [Composing split, adding, and subsplitting](#composing-split-adding-and-subsplitting)
   * [Dataset using non-conventional named split](#dataset-using-non-conventional-named-split)

## Two APIs: S3 and legacy

Each versioned dataset either implements the new S3 API, or the legacy API,
which will eventually be retired. New datasets (except Beam ones for now) all
implement S3, and we're slowly rolling it out to all datasets.
If the dataset you're interested in implements S3, use S3.

To find out whether a dataset implements S3, look at the dataset's source code
(specifically see if the `tfds.core.Version` object is constructed with
`experiments={tfds.core.Experiment.S3: False}`; if not, then you can use S3
with that version because it defaults to `True`). Or you can call:

```
ds_builder.version.implements(tfds.core.Experiment.S3)
```

## S3 slicing API

Slicing instructions are specified in `tfds.load` or `tfds.DatasetBuilder.as_dataset`.

Instructions can be provided as either strings or  `ReadInstruction`s.
Strings are more compact and
readable for simple cases, while `ReadInstruction`s provide more options
and might be easier to use with variable slicing parameters.

### Examples

Examples using the string API:

```py
# The full `train` split.
train_ds = tfds.load('mnist:3.*.*', split='train')

# The full `train` split and the full `test` split as two distinct datasets.
train_ds, test_ds = tfds.load('mnist:3.*.*', split=['train', 'test'])

# The full `train` and `test` splits, concatenated together.
train_test_ds = tfds.load('mnist:3.*.*', split='train+test')

# From record 10 (included) to record 20 (excluded) of `train` split.
train_10_20_ds = tfds.load('mnist:3.*.*', split='train[10:20]')

# The first 10% of train split.
train_10pct_ds = tfds.load('mnist:3.*.*', split='train[:10%]')

# The first 10% of train + the last 80% of train.
train_10_80pct_ds = tfds.load('mnist:3.*.*', split='train[:10%]+train[-80%:]')

# 10-fold cross-validation (see also next section on rounding behavior):
# The validation datasets are each going to be 10%:
# [0%:10%], [10%:20%], ..., [90%:100%].
# And the training datasets are each going to be the complementary 90%:
# [10%:100%] (for a corresponding validation set of [0%:10%]),
# [0%:10%] + [20%:100%] (for a validation set of [10%:20%]), ...,
# [0%:90%] (for a validation set of [90%:100%]).
vals_ds = tfds.load('mnist:3.*.*', split=[
    'train[{}%:{}%]'.format(k, k+10) for k in range(0, 100, 10)
])
trains_ds = tfds.load('mnist:3.*.*', split=[
    'train[:{}%]+train[{}%:]'.format(k, k+10) for k in range(0, 100, 10)
])
```

Examples using the `ReadInstruction` API (equivalent as above):

```py
# The full `train` split.
train_ds = tfds.load('mnist:3.*.*', split=tfds.core.ReadInstruction('train'))

# The full `train` split and the full `test` split as two distinct datasets.
train_ds, test_ds = tfds.load('mnist:3.*.*', split=[
    tfds.core.ReadInstruction('train'),
    tfds.core.ReadInstruction('test'),
])

# The full `train` and `test` splits, concatenated together.
ri = tfds.core.ReadInstruction('train') + tfds.core.ReadInstruction('test')
train_test_ds = tfds.load('mnist:3.*.*', split=ri)

# From record 10 (included) to record 20 (excluded) of `train` split.
train_10_20_ds = tfds.load('mnist:3.*.*', split=tfds.core.ReadInstruction(
    'train', from_=10, to=20, unit='abs'))

# The first 10% of train split.
train_10_20_ds = tfds.load('mnist:3.*.*', split=tfds.core.ReadInstruction(
    'train', to=10, unit='%'))

# The first 10% of train + the last 80% of train.
ri = (tfds.core.ReadInstruction('train', to=10, unit='%') +
      tfds.core.ReadInstruction('train', from_=-80, unit='%'))
train_10_80pct_ds = tfds.load('mnist:3.*.*', split=ri)

# 10-fold cross-validation (see also next section on rounding behavior):
# The validation datasets are each going to be 10%:
# [0%:10%], [10%:20%], ..., [90%:100%].
# And the training datasets are each going to be the complementary 90%:
# [10%:100%] (for a corresponding validation set of [0%:10%]),
# [0%:10%] + [20%:100%] (for a validation set of [10%:20%]), ...,
# [0%:90%] (for a validation set of [90%:100%]).
vals_ds = tfds.load('mnist:3.*.*', [
    tfds.core.ReadInstruction('train', from_=k, to=k+10, unit='%')
    for k in range(0, 100, 10)])
trains_ds = tfds.load('mnist:3.*.*', [
    (tfds.core.ReadInstruction('train', to=k, unit='%') +
     tfds.core.ReadInstruction('train', from_=k+10, unit='%'))
    for k in range(0, 100, 10)])
```

### Percentage slicing and rounding

If a slice of a split is requested using the percent (`%`) unit, and the
requested slice boundaries do not divide evenly by `100`, then the default
behaviour it to round boundaries to the nearest integer (`closest`). This means
that some slices may contain more examples than others. For example:

```py
# Assuming "train" split contains 101 records.
# 100 records, from 0 to 100.
tfds.load("mnist:3.*.*", split="test[:99%]")
# 2 records, from 49 to 51.
tfds.load("mnist:3.*.*", split="test[49%:50%]")
```

Alternatively, the user can use the rounding `pct1_dropremainder`, so specified
percentage boundaries are treated as multiples of 1%. This option should be used
when consistency is needed (eg: `len(5%) == 5 * len(1%)`).

Example:

```py
# Records 0 (included) to 99 (excluded).
tfds.load("mnist:3.*.*", split="test[:99%]", rounding="pct1_dropremainder")
```

### Reproducibility

The S3 API guarantees that any given split slice (or `ReadInstruction`) will
always produce the same set of records on a given dataset, as long as the major
version of the dataset is constant.

For example, `tfds.load("mnist:3.0.0", split="train[10:20]")` and
`tfds.load("mnist:3.2.0", split="train[10:20]")` will always contain the same
elements - regardless of platform, architecture, etc. - even though some of
the records might have different values (eg: imgage encoding, label, ...).

## Legacy slicing API

Note: This will soon be deprecated. If the dataset you're interested in
implements S3, use S3 (see above).

[`tfds.Split`](api_docs/python/tfds/Split.md)s (typically `tfds.Split.TRAIN` and
`tfds.Split.TEST`). A given dataset's splits are defined in
[`tfds.DatasetBuilder.info.splits`](api_docs/python/tfds/core/DatasetBuilder.md#info)
and are accessible through [`tfds.load`](api_docs/python/tfds/load.md) and
[`tfds.DatasetBuilder.as_dataset`](api_docs/python/tfds/core/DatasetBuilder.md#as_dataset),
both of which take `split=` as a keyword argument.

`tfds` enables you to combine splits
subsplitting them up. The resulting splits can be passed to `tfds.load` or
`tfds.DatasetBuilder.as_dataset`.

### Add splits together

```py
combined_split = tfds.Split.TRAIN + tfds.Split.TEST

ds = tfds.load("mnist", split=combined_split)
```

Note that a special `tfds.Split.ALL` keyword exists to merge all splits
together:

```py
# `ds` will iterate over test, train and validation merged together
ds = tfds.load("mnist", split=tfds.Split.ALL)
```

### Subsplit

You have 3 options for how to get a thinner slice of the data than the
base splits, all based on `tfds.Split.subsplit`.

*Warning*: The legacy API does not guarantee the reproducibility of the subsplit
operations. Two different users working on the same dataset at the same version
and using the same subsplit instructions could end-up with two different sets
of examples. Also, if a user regenerates the data, the subsplits may no longer
be the same.

*Warning*: If the `total_number_examples % 100 != 0`, then remainder examples
may not be evenly distributed among subsplits.

#### Specifying number of subsplits

```py
train_half_1, train_half_2 = tfds.Split.TRAIN.subsplit(k=2)

dataset = tfds.load("mnist", split=train_half_1)
```

#### Specifying a percentage slice

```py
first_10_percent = tfds.Split.TRAIN.subsplit(tfds.percent[:10])
last_2_percent = tfds.Split.TRAIN.subsplit(tfds.percent[-2:])
middle_50_percent = tfds.Split.TRAIN.subsplit(tfds.percent[25:75])

dataset = tfds.load("mnist", split=middle_50_percent)
```

#### Specifying weights

```py
half, quarter1, quarter2 = tfds.Split.TRAIN.subsplit(weighted=[2, 1, 1])

dataset = tfds.load("mnist", split=half)
```

### Composing split, adding, and subsplitting

It's possible to compose the above operations:

```py
# Half of the TRAIN split plus the TEST split
split = tfds.Split.TRAIN.subsplit(tfds.percent[:50]) + tfds.Split.TEST

# Split the combined TRAIN and TEST splits into 2
first_half, second_half = (tfds.Split.TRAIN + tfds.Split.TEST).subsplit(k=2)
```

Note that a split cannot be added twice, and subsplitting can only happen once.
For example, these are invalid:

```py
# INVALID! TRAIN included twice
split = tfds.Split.TRAIN.subsplit(tfds.percent[:25]) + tfds.Split.TRAIN

# INVALID! Subsplit of subsplit
split = tfds.Split.TRAIN.subsplit(tfds.percent[0:25]).subsplit(k=2)

# INVALID! Subsplit of subsplit
split = (tfds.Split.TRAIN.subsplit(tfds.percent[:25]) +
         tfds.Split.TEST).subsplit(tfds.percent[0:50])
```

### Dataset using non-conventional named split

For dataset using splits not in `tfds.Split.{TRAIN,VALIDATION,TEST}`, you can
still use the subsplit API by defining the custom named split with
`tfds.Split('custom_split')`. For instance:

```py
split = tfds.Split('test2015') + tfds.Split.TEST
ds = tfds.load('coco2014', split=split)
```
