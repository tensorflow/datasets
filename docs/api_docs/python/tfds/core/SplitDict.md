<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="total_num_examples"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add"/>
<meta itemprop="property" content="copy"/>
<meta itemprop="property" content="from_proto"/>
<meta itemprop="property" content="to_proto"/>
<meta itemprop="property" content="update"/>
</div>

# tfds.core.SplitDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

## Class `SplitDict`

Split info object.

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__init__()
```

## Properties

<h3 id="total_num_examples"><code>total_num_examples</code></h3>

Return the total number of examples.

## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py">View
source</a>

``` python
__getitem__(key)
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
