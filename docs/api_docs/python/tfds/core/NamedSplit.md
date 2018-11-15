<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.NamedSplit" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_read_instruction"/>
</div>

# tfds.core.NamedSplit

## Class `NamedSplit`





Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

Descriptor corresponding to a named split (train, test,...).

Each descriptor can be composed with other using addition or slice. Ex:

  split = tfds.Split.TRAIN[0:25] + tfds.Split.TEST

The resulting split will correspond to 25% of the train split merged with
100% of the test split.

Warning:
  A split cannot be added twice, so the following will fail:

    split = tfds.Split.TRAIN[:25] + tfds.Split.TRAIN[75:]
    split = tfds.Split.TEST + tfds.Split.ALL

Warning:
  The slices can be applied only one time. So the following are valid:

    split = tfds.Split.TRAIN[0:25] + tfds.Split.TEST[0:50]
    split = (tfds.Split.TRAIN + tfds.Split.TEST)[0:50]

  But not:

    split = tfds.Split.TRAIN[0:25][0:25]
    split = (tfds.Split.TRAIN[:25] + tfds.Split.TEST)[0:50]

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(name)
```





## Methods

<h3 id="__add__"><code>__add__</code></h3>

``` python
__add__(other)
```

Merging: tfds.Split.TRAIN + tfds.Split.TEST.

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Equality: tfds.Split.TRAIN == 'train'.

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(slice_value)
```

Synthetic subsplit: tfds.Split.TRAIN[30:50].

<h3 id="get_read_instruction"><code>get_read_instruction</code></h3>

``` python
get_read_instruction(split_dict)
```





