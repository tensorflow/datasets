<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.DownloadManager" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="download_sizes"/>
<meta itemprop="property" content="manual_dir"/>
<meta itemprop="property" content="recorded_download_checksums"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="download"/>
<meta itemprop="property" content="download_and_extract"/>
<meta itemprop="property" content="extract"/>
<meta itemprop="property" content="iter_archive"/>
</div>

# tfds.download.DownloadManager

## Class `DownloadManager`





Defined in [`core/download/download_manager.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/download_manager.py).

Manages the download and extraction of files, as well as caching.

Downloaded files are cached under `download_dir`. The file name is:
  - if there is a sha256 associated with the url: "${sha256_of_content}s".
  - otherwise: "url.%(sha256_of_url)s".

The sha256 of content (if any) associated to each URL are given through the
`checksum_file` given to constructor.

When a file is downloaded, a "%{fname}s.INFO.json" file is created next to it.
This INFO file contains the following information:
{"dataset_names": ["name1", "name2"],
 "urls": ["http://url.of/downloaded_file"]}
The INFO files are used by `create_checksum_files.py` script.

Extracted files/dirs are stored under `extract_dir`. The file name or
directory name is the same as the original name, prefixed with the extraction
method. E.g. "${extract_dir}/ZIP.%(sha256_of_zipped_content)s" or
             "${extract_dir}/TAR.url.%(sha256_of_url)s".

The function members accept either plain value, or values wrapped into list
or dict. Giving a data structure will parallelize the downloads.

Example of usage:

```
# Sequential download: str -> str
train_dir = dl_manager.download_and_extract('https://abc.org/train.tar.gz')
test_dir = dl_manager.download_and_extract('https://abc.org/test.tar.gz')

# Parallel download: list -> list
image_files = dl_manager.download(
    ['https://a.org/1.jpg', 'https://a.org/2.jpg', ...])

# Parallel download: dict -> dict
data_dirs = dl_manager.download_and_extract({
   'train': 'https://abc.org/train.zip',
   'test': 'https://abc.org/test.zip',
})
data_dirs['train']
data_dirs['test']
```

For more customization on the download/extraction (ex: passwords, output_name,
...), you can pass a <a href="../../tfds/download/Resource.md"><code>tfds.download.Resource</code></a> as argument.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dataset_name,
    download_dir=None,
    extract_dir=None,
    manual_dir=None,
    checksums=None,
    force_download=False,
    force_extraction=False
)
```

Download manager constructor.

#### Args:

* <b>`dataset_name`</b>: `str`, name of dataset this instance will be used for.
* <b>`download_dir`</b>: `str`, path to directory where downloads are stored.
* <b>`extract_dir`</b>: `str`, path to directory where artifacts are extracted.
* <b>`manual_dir`</b>: `str`, path to manually downloaded/extracted data directory.
* <b>`checksums`</b>: `dict<str url, str sha256>`, url to sha256 of resource.
    Only URLs present are checked.
* <b>`force_download`</b>: `bool`, default to False. If True, always [re]download.
* <b>`force_extraction`</b>: `bool`, default to False. If True, always [re]extract.



## Properties

<h3 id="download_sizes"><code>download_sizes</code></h3>

Returns sizes (in bytes) for downloaded urls.

<h3 id="manual_dir"><code>manual_dir</code></h3>

Returns the directory containing the manually extracted data.

<h3 id="recorded_download_checksums"><code>recorded_download_checksums</code></h3>

Returns checksums for downloaded urls.



## Methods

<h3 id="download"><code>download</code></h3>

``` python
download(
    url_or_urls,
    async_=False
)
```

Download given url(s).

#### Args:

* <b>`url_or_urls`</b>: url or `list`/`dict` of urls to download and extract. Each
    url can be a `str` or <a href="../../tfds/download/Resource.md"><code>tfds.download.Resource</code></a>.
* <b>`async_`</b>: `bool`, default to False. If True, returns promise on result.


#### Returns:

downloaded_path(s): `str`, The downloaded paths matching the given input
  url_or_urls.

<h3 id="download_and_extract"><code>download_and_extract</code></h3>

``` python
download_and_extract(
    url_or_urls,
    async_=False
)
```

Download and extract given url_or_urls.

Is roughly equivalent to:

```
extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
```

#### Args:

* <b>`url_or_urls`</b>: url or `list`/`dict` of urls to download and extract. Each
    url can be a `str` or <a href="../../tfds/download/Resource.md"><code>tfds.download.Resource</code></a>.
* <b>`async_`</b>: `bool`, defaults to False. If True, returns promise on result.

If not explicitly specified in `Resource`, the extraction method will
automatically be deduced from downloaded file name.


#### Returns:

extracted_path(s): `str`, extracted paths of given URL(s).

<h3 id="extract"><code>extract</code></h3>

``` python
extract(
    path_or_paths,
    async_=False
)
```

Extract given path(s).

#### Args:

* <b>`path_or_paths`</b>: path or `list`/`dict` of path of file to extract. Each
    path can be a `str` or <a href="../../tfds/download/Resource.md"><code>tfds.download.Resource</code></a>.
* <b>`async_`</b>: `bool`, default to False. If True, returns promise on result.

If not explicitly specified in `Resource`, the extraction method is deduced
from downloaded file name.


#### Returns:

extracted_path(s): `str`, The extracted paths matching the given input
  path_or_paths.

<h3 id="iter_archive"><code>iter_archive</code></h3>

``` python
iter_archive(resource)
```

Returns iterator over files within archive.

**Important Note**: caller should read files as they are yielded.
Reading out of order is slow.

#### Args:

* <b>`resource`</b>: path to archive or <a href="../../tfds/download/Resource.md"><code>tfds.download.Resource</code></a>.


#### Returns:

Generator yielding tuple (path_within_archive, file_obj).



