<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="total_num_examples"/>
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="add"/>
<meta itemprop="property" content="copy"/>
<meta itemprop="property" content="from_proto"/>
<meta itemprop="property" content="fromkeys"/>
<meta itemprop="property" content="to_proto"/>
<meta itemprop="property" content="update"/>
</div>

# tfds.core.SplitDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

<!-- Equality marker -->
## Class `SplitDict`

Split info object.

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__init__()
```

Initialize self. See help(type(self)) for accurate signature.

<h2 id="__new__"><code>__new__</code></h2>

```python
__new__(
    type,
    *args,
    **kwargs
)
```

## Properties

<h3 id="total_num_examples"><code>total_num_examples</code></h3>

Return the total number of examples.

## Methods

<h3 id="__contains__"><code>__contains__</code></h3>

```python
__contains__(key)
```

<h3 id="__eq__"><code>__eq__</code></h3>

```python
__eq__(value)
```

<h3 id="__ge__"><code>__ge__</code></h3>

```python
__ge__(value)
```

<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__getitem__(key)
```

x.__getitem__(y) <==> x[y]

<h3 id="__gt__"><code>__gt__</code></h3>

```python
__gt__(value)
```

<h3 id="__iter__"><code>__iter__</code></h3>

```python
__iter__()
```

<h3 id="__le__"><code>__le__</code></h3>

```python
__le__(value)
```

<h3 id="__len__"><code>__len__</code></h3>

```python
__len__()
```

<h3 id="__lt__"><code>__lt__</code></h3>

```python
__lt__(value)
```

<h3 id="__ne__"><code>__ne__</code></h3>

```python
__ne__(value)
```

<h3 id="add"><code>add</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
add(split_info)
```

Add the split info.

<h3 id="copy"><code>copy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
copy()
```

D.copy() -> a shallow copy of D

<h3 id="from_proto"><code>from_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
@classmethod
from_proto(
    cls,
    repeated_split_infos
)
```

Returns a new SplitDict initialized from the `repeated_split_infos`.

<h3 id="fromkeys"><code>fromkeys</code></h3>

```python
fromkeys(
    type,
    iterable,
    value
)
```

<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
to_proto()
```

Returns a list of SplitInfo protos that we have.

<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/py_utils.py">View
source</a>

``` python
update(other)
```

D.update([E, ]**F) -> None. Update D from dict/iterable E and F. If E is present
and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and
lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this
is followed by: for k in F: D[k] = F[k]
