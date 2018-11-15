<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.DownloadManager" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="manual_dir"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="download"/>
<meta itemprop="property" content="download_and_extract"/>
<meta itemprop="property" content="execute_and_cache"/>
<meta itemprop="property" content="extract"/>
</div>

# tfds.download.DownloadManager

## Class `DownloadManager`





Defined in [`core/download/download_manager.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/download_manager.py).

Class which manages the download and extraction of data.

This has the following advantage:
 * Remove the boilerplate code common to each dataset as now the user only
   has to provide urls.
 * Allow multiple download backends (local and cloud). Otherwise the user
   may be tempted to use standard Python function (ex: tarfile) which may
   not be compatible with one of the backend.
 * Allow to launch multiple download in parallel.
 * Better ressources management (ex: a same url used by multiple
   datasets is downloaded/extracted only once).

The function members accept either plain value, or values wrapped into list
or dict. Giving a data structure will parallelize the downloads.

Example:

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

For more customization on the download/extraction (ex: passwords, output_name,
...), you can give UrlInfo() or ExtractInfo() instead of plain string.

It is also possible to use the download manager to process a custom function
with the same guaranties/features than download and extraction.

  # The "/vocab/en-fr" path is cached and can be reused accros run. If
  # the path already exists, the cached value is re-used
  vocab_dir = dl_manager.execute_and_cache(generate_vocab_fn, '/vocab/en-fr')

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cache_dir,
    manual_dir=None,
    mode=None
)
```

Download manager constructor.

#### Args:

* <b>`cache_dir`</b>: `str`, Cache directory where all downloads, extractions and
    other artifacts are stored.
* <b>`manual_dir`</b>: `str`, Directory containing manually downloaded data. Default
    to cache_dir.
  mode (GenerateMode): Mode to FORCE_REDOWNLOAD, REUSE_CACHE_IF_EXISTS or
    REUSE_DATASET_IF_EXISTS. Default to REUSE_DATASET_IF_EXISTS.



## Properties

<h3 id="manual_dir"><code>manual_dir</code></h3>

Returns the directory containing the manually extracted data.



## Methods

<h3 id="download"><code>download</code></h3>

``` python
download(urls_info)
```

Downloads the given urls.

If one of the download already exists, the cached value will be reused.

#### Args:

urls_info (UrlInfo): The url to download. If a string is passed, it will
  automatically be converted into UrlInfo object


#### Returns:

downloaded_filepaths (str): The downloaded files paths

<h3 id="download_and_extract"><code>download_and_extract</code></h3>

``` python
download_and_extract(urls_info)
```

Convinience method to perform download+extract in a single command.

As most downloads are imediatelly followed by an extraction, this
function avoid some boilerplate code. It is equivalent to:
  extracted_dirs = dl_manager.extract(dl_manager.download(urls_info))

#### Args:

urls_info (UrlInfo): Same input as .download()


#### Returns:

extracted_dir (str): Same output as .extract()

<h3 id="execute_and_cache"><code>execute_and_cache</code></h3>

``` python
execute_and_cache(
    process_fn,
    cache_key
)
```

Execute the function and cache the associated path.

This function executes the process_fn using a custom cached directory given
by the key. This allow to use the download manager to cache and share
additional data like vocabulary or other intermediate artifacts.

The key are shared between datasets which allow re-using data from other
datasets but also increase the risk of name collision. A good practice
is to add the dataset name as prefix of the key.

  vocab_cache_key = os.path.join(self.name, 'vocab/en-fr')
  vocab_dir = dl_manager.execute_and_cache(
      generate_vocab_fn,
      cache_key=vocab_cache_key,
  )

#### Args:

process_fn (fct): Function with signature "(cache_dir) -> None" which
  takes as input a directory on which storing the additional data.
cache_key (str): Key of the cache to store the data. If the key already
  exists, the process_fn isn't used and the previously cached dir is
  reused.


#### Returns:

cache_dir (str): The directory on which the additional data has been
  written.

<h3 id="extract"><code>extract</code></h3>

``` python
extract(extracts_info)
```

Extract the given path.

If one of the extraction already exists, the cached value will be reused.

#### Args:

extracts_info (ExtractInfo): The path to extract. If a string is passed,
  it will automatically be converted into ExtractInfo object


#### Returns:

extracted_dirs (str): The downloaded files



