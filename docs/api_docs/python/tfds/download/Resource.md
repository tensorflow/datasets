<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.Resource" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="extract_method"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="exists_locally"/>
</div>

# tfds.download.Resource

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/resource.py">View
source</a>

## Class `Resource`

Represents a resource to download, extract, or both.

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/resource.py">View
source</a>

``` python
__init__(
    url=None,
    extract_method=None,
    path=None
)
```

Resource constructor.

#### Args:

*   <b>`url`</b>: `str`, the URL at which to download the resource.
*   <b>`extract_method`</b>: `ExtractMethod` to be used to extract resource. If
    not set, will be guessed from downloaded file name `original_fname`.
*   <b>`path`</b>: `str`, path of resource on local disk. Can be None if
    resource has not be downloaded yet. In such case, `url` must be set.

## Properties

<h3 id="extract_method"><code>extract_method</code></h3>

Returns `ExtractMethod` to use on resource. Cannot be None.

## Methods

<h3 id="exists_locally"><code>exists_locally</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/resource.py">View
source</a>

``` python
@classmethod
exists_locally(
    cls,
    path
)
```

Returns whether the resource exists locally, at `resource.path`.
