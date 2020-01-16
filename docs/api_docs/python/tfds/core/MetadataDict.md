<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.MetadataDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="fromkeys"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.core.MetadataDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

<!-- Equality marker -->
## Class `MetadataDict`

A <a href="../../tfds/core/Metadata.md"><code>tfds.core.Metadata</code></a>
object that acts as a `dict`.

Inherits From: [`Metadata`](../../tfds/core/Metadata.md)

<!-- Placeholder for "Used in" -->

By default, the metadata will be serialized as JSON.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

<h2 id="__new__"><code>__new__</code></h2>

```python
__new__(
    type,
    *args,
    **kwargs
)
```

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

<h3 id="fromkeys"><code>fromkeys</code></h3>

```python
fromkeys(
    type,
    iterable,
    value
)
```

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

```python
load_metadata(data_dir)
```

Restore the metadata.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

```python
save_metadata(data_dir)
```

Save the metadata.
