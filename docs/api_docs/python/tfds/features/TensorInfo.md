<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.TensorInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="copy_from"/>
</div>

# tfds.features.TensorInfo

## Class `TensorInfo`

Structure containing info on the `tf.Tensor` shape/dtype.

Defined in [`core/features/feature.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/feature.py).

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    shape,
    dtype,
    default_value=None
)
```

Constructor.

#### Args:

*   <b>`shape`</b>: `tuple[int]`, shape of the tensor
*   <b>`dtype`</b>: Tensor dtype
*   <b>`default_value`</b>: Used for retrocompatibility with previous files if a
    new field is added to provide a default value when reading the file.

## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

```python
__eq__(other)
```

Equality.

<h3 id="copy_from"><code>copy_from</code></h3>

```python
@classmethod
copy_from(
    cls,
    tensor_info
)
```

Copy constructor.
