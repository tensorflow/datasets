<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__setitem__"/>
<meta itemprop="property" content="add"/>
<meta itemprop="property" content="from_json_data"/>
<meta itemprop="property" content="to_json_data"/>
<meta itemprop="property" content="update"/>
</div>

# tfds.core.SplitDict

## Class `SplitDict`





Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

Split info object.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```





## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(key)
```



<h3 id="__setitem__"><code>__setitem__</code></h3>

``` python
__setitem__(
    key,
    value
)
```



<h3 id="add"><code>add</code></h3>

``` python
add(split_info)
```

Add the split info.

<h3 id="from_json_data"><code>from_json_data</code></h3>

``` python
from_json_data(split_data)
```

Restore the splits info from the written metadata file.

<h3 id="to_json_data"><code>to_json_data</code></h3>

``` python
to_json_data()
```

Export the metadata for json export.

<h3 id="update"><code>update</code></h3>

``` python
update(other)
```





