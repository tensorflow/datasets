# Splits

All `DatasetBuilder`s expose various data subsets defined as
[`tfds.Split`](api_docs/python/tfds/Split.md)s (typically `tfds.Split.TRAIN` and
`tfds.Split.TEST`). A given dataset's splits are defined in
[`tfds.DatasetBuilder.info.splits`](api_docs/python/tfds/core/DatasetBuilder.md#info)
and are accessible through [`tfds.load`](api_docs/python/tfds/load.md) and
[`tfds.DatasetBuilder.as_dataset`](api_docs/python/tfds/core/DatasetBuilder.md#as_dataset),
both of which take `split=` as a keyword argument.

`tfds` enables you to further manipulate splits by combining them or
subsplitting them up. The resulting splits can be passed to `tfds.load` or
`tfds.DatasetBuilder.as_dataset`.

## Add splits together

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

## Subsplit

You have 3 options for how to get a thinner slice of the data than the
base splits, all based on `tfds.Split.subsplit`.

*Warning*: TensorFlow Datasets does not currently guarantee the order of the
data on disk when data is generated. Therefore, if you regenerate the data, the
subsplits may no longer be the same.

*Warning*: If the `total_number_examples % 100 != 0`, then remainder examples
may not be evenly distributed among subsplits.

### Specify number of subsplits

```py
train_half_1, train_half_2 = tfds.Split.TRAIN.subsplit(k=2)

dataset = tfds.load("mnist", split=train_half_1)
```

### Specify a percentage slice

```py
first_10_percent = tfds.Split.TRAIN.subsplit(tfds.percent[:10])
last_2_percent = tfds.Split.TRAIN.subsplit(tfds.percent[-2:])
middle_50_percent = tfds.Split.TRAIN.subsplit(tfds.percent[25:75])

dataset = tfds.load("mnist", split=middle_50_percent)
```

### Specifying weights

```py
half, quarter1, quarter2 = tfds.Split.TRAIN.subsplit(weighted=[2, 1, 1])

dataset = tfds.load("mnist", split=half)
```

## Composing split, adding, and subsplitting

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

## Dataset using non-conventional named split

For dataset using splits not in `tfds.Split.{TRAIN,VALIDATION,TEST}`, you can
still use the subsplit API by defining the custom named split with
`tfds.Split('custom_split')`. For instance:

```py
split = tfds.Split('test2015') + tfds.Split.TEST
ds = tfds.load('coco2014', split= split)
```
