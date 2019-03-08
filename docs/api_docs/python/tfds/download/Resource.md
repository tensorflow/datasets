<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.Resource" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="extract_fname"/>
<meta itemprop="property" content="extract_method"/>
<meta itemprop="property" content="extract_method_name"/>
<meta itemprop="property" content="fname"/>
<meta itemprop="property" content="info_path"/>
<meta itemprop="property" content="sha256"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="exists_locally"/>
<meta itemprop="property" content="write_info_file"/>
</div>

# tfds.download.Resource

## Class `Resource`





Defined in [`core/download/resource.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/resource.py).

Represents a resource to download, extract, or both.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    url=None,
    extract_method=None,
    path=None
)
```

Resource constructor.

#### Args:

* <b>`url`</b>: `str`, the URL at which to download the resource.
* <b>`extract_method`</b>: `ExtractMethod` to be used to extract resource. If
    not set, will be guessed from downloaded file name `original_fname`.
* <b>`path`</b>: `str`, path of resource on local disk. Can be None if resource has
    not be downloaded yet. In such case, `url` must be set.



## Properties

<h3 id="extract_fname"><code>extract_fname</code></h3>

Name of extracted archive (file or directory).

<h3 id="extract_method"><code>extract_method</code></h3>

Returns `ExtractMethod` to use on resource. Cannot be None.

<h3 id="extract_method_name"><code>extract_method_name</code></h3>

Returns the name (`str`) of the extraction method.

<h3 id="fname"><code>fname</code></h3>

Name of downloaded file (not as downloaded, but as stored).

<h3 id="info_path"><code>info_path</code></h3>

Returns path (`str`) of INFO file associated with resource.

<h3 id="sha256"><code>sha256</code></h3>





## Methods

<h3 id="exists_locally"><code>exists_locally</code></h3>

``` python
exists_locally()
```

Returns whether the resource exists locally, at `resource.path`.

<h3 id="write_info_file"><code>write_info_file</code></h3>

``` python
write_info_file(
    *args,
    **kwargs
)
```

Write the INFO file next to local file.

Although the method is synchronized, there is still a risk two processes
running at the same time overlap here. Risk accepted, since potentially lost
data (`dataset_name`) is only for human consumption.

#### Args:

* <b>`dataset_name`</b>: data used to dl the file.
* <b>`original_fname`</b>: name of file as downloaded.



