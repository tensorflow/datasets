<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.ReadConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__ne__"/>
</div>

# tfds.ReadConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/read_config.py">View
source</a>

## Class `ReadConfig`

Configures input reading pipeline.

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`options`</b>: `tf.data.Options()`, dataset options. Those options are
    added to the default values defined in `tfrecord_reader.py`. Note that when
    `shuffle_files` is True and no seed is defined, experimental_deterministic
    will be set to False internally, unless it is defined here.
*   <b>`shuffle_seed`</b>: `tf.int64`, seeds forwarded to
    `tf.data.Dataset.shuffle` when `shuffle_files=True`.
*   <b>`shuffle_reshuffle_each_iteration`</b>: `bool`, forwarded to
    `tf.data.Dataset.shuffle` when `shuffle_files=True`.
*   <b>`interleave_parallel_reads`</b>: `int`, forwarded to
    `tf.data.Dataset.interleave`. Default to 16.
*   <b>`interleave_block_length`</b>: `int`, forwarded to
    `tf.data.Dataset.interleave`. Default to 16.
*   <b>`experimental_interleave_sort_fn`</b>: Function with signature
    `List[FileDict] -> List[FileDict]`, which takes the list of `dict(file: str,
    take: int, skip: int)` and returns the modified version to read. This can be
    used to sort/shuffle the shards to read in a custom order, instead of
    relying on `shuffle_files=True`.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    options=NOTHING,
    shuffle_seed=attr_dict['shuffle_seed'].default,
    shuffle_reshuffle_each_iteration=attr_dict['shuffle_reshuffle_each_iteration'].default,
    interleave_parallel_reads=attr_dict['interleave_parallel_reads'].default,
    interleave_block_length=attr_dict['interleave_block_length'].default,
    experimental_interleave_sort_fn=attr_dict['experimental_interleave_sort_fn'].default
)
```

## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

```python
__eq__(other)
```

<h3 id="__ge__"><code>__ge__</code></h3>

```python
__ge__(other)
```

Automatically created by attrs.

<h3 id="__gt__"><code>__gt__</code></h3>

```python
__gt__(other)
```

Automatically created by attrs.

<h3 id="__le__"><code>__le__</code></h3>

```python
__le__(other)
```

Automatically created by attrs.

<h3 id="__lt__"><code>__lt__</code></h3>

```python
__lt__(other)
```

Automatically created by attrs.

<h3 id="__ne__"><code>__ne__</code></h3>

```python
__ne__(other)
```

Check equality and either forward a NotImplemented or return the result negated.
