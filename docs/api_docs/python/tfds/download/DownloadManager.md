<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.DownloadManager" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="manual_dir"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="download"/>
<meta itemprop="property" content="download_and_extract"/>
<meta itemprop="property" content="extract"/>
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

Example of usage:

  # Sequential download: str -> str
  train_dir = dl_manager.download_and_extract('https://abc.org/train.tar.gz')
  test_dir = dl_manager.download_and_extract('https://abc.org/test.tar.gz')

  # Parallel download: dict -> dict
  data_dirs = dl_manager.download_and_extract({
     'train': 'https://abc.org/train.zip',
     'test': 'https://abc.org/test.zip',
  })
  data_dirs['train']
  data_dirs['test']

For more customization on the download/extraction (ex: passwords, output_name,
...), you can pass UrlInfo() ExtractInfo() or UrlExtractInfo as arguments.

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
  `bool`, if True, validate checksums of files if url is
    present in the checksums file. If False, no checks are done.
* <b>`force_download`</b>: `bool`, default to False. If True, always [re]download.
* <b>`force_extraction`</b>: `bool`, default to False. If True, always [re]extract.



## Properties

<h3 id="manual_dir"><code>manual_dir</code></h3>

Returns the directory containing the manually extracted data.



## Methods

<h3 id="download"><code>download</code></h3>

``` python
download(
    urls,
    async_=False
)
```

Download given artifacts, returns {'name': 'path'} or 'path'.

#### Args:

* <b>`urls`</b>: A single URL (str or UrlInfo) or a `Dict[str, UrlInfo]`.
    The URL(s) to download.
* <b>`async_`</b>: `bool`, default to False. If True, returns promise on result.


#### Returns:

`str` or `Dict[str, str]`: path or {name: path}.

<h3 id="download_and_extract"><code>download_and_extract</code></h3>

``` python
download_and_extract(
    url_extract_info,
    async_=False
)
```

Downlaod and extract given resources, returns path or {name: path}.

#### Args:

* <b>`url_extract_info`</b>: `Dict[str, str|DownloadExtractInfo]` or a single
    str|DownloadExtractInfo.
* <b>`async_`</b>: `bool`, defaults to False. If True, returns promise on result.

If URL(s) are given (no `DownloadExtractInfo`), the extraction method is
guessed from the extension of file on URL path.


#### Returns:

`Dict[str, str]` or `str`: {'name': 'out_path'} or 'out_path' of
downloaded AND extracted resource.

<h3 id="extract"><code>extract</code></h3>

``` python
extract(
    paths,
    async_=False
)
```

Extract path(s).

#### Args:

* <b>`paths`</b>: `Dict[str, str|ExtractInfo]` or a single str|ExtractInfo.
* <b>`async_`</b>: `bool`, default to False. If True, returns promise on result.


#### Returns:

`Dict[str, str]` or `str`: {'name': 'out_path'} or 'out_path'.



