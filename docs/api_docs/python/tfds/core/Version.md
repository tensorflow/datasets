<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.Version" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="major"/>
<meta itemprop="property" content="minor"/>
<meta itemprop="property" content="patch"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="match"/>
<meta itemprop="property" content="LATEST"/>
</div>

# tfds.core.Version

## Class `Version`

Dataset version MAJOR.MINOR.PATCH.

Defined in [`core/utils/version.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py).

<!-- Placeholder for "Used in" -->


<h2 id="__new__"><code>__new__</code></h2>

``` python
@staticmethod
__new__(
    cls,
    *args,
    **kwargs
)
```

## Properties

<h3 id="major"><code>major</code></h3>

<h3 id="minor"><code>minor</code></h3>

<h3 id="patch"><code>patch</code></h3>

## Methods

<h3 id="match"><code>match</code></h3>

```python
match(other_version)
```

Returns True if other_version matches.

#### Args:

*   <b>`other_version`</b>: string, of the form "x[.y[.x]]" where {x,y,z} can be
    a number or a wildcard.

## Class Members

<h3 id="LATEST"><code>LATEST</code></h3>

