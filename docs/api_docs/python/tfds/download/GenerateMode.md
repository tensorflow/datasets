<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.GenerateMode" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="FORCE_REDOWNLOAD"/>
<meta itemprop="property" content="REUSE_CACHE_IF_EXISTS"/>
<meta itemprop="property" content="REUSE_DATASET_IF_EXISTS"/>
</div>

# tfds.download.GenerateMode

## Class `GenerateMode`

`Enum` for how to treat pre-existing downloads and data.

### Aliases:

* Class `tfds.GenerateMode`
* Class `tfds.download.GenerateMode`



Defined in [`core/download/util.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/util.py).

<!-- Placeholder for "Used in" -->

The default mode is `REUSE_DATASET_IF_EXISTS`, which will reuse both
raw downloads and the prepared dataset if they exist.

#### The generations modes:

|                                    | Downloads | Dataset |
| -----------------------------------|-----------|---------|
| `REUSE_DATASET_IF_EXISTS` (default)| Reuse     | Reuse   |
| `REUSE_CACHE_IF_EXISTS`            | Reuse     | Fresh   |
| `FORCE_REDOWNLOAD`                 | Fresh     | Fresh   |

## Class Members

*   `FORCE_REDOWNLOAD` <a id="FORCE_REDOWNLOAD"></a>
*   `REUSE_CACHE_IF_EXISTS` <a id="REUSE_CACHE_IF_EXISTS"></a>
*   `REUSE_DATASET_IF_EXISTS` <a id="REUSE_DATASET_IF_EXISTS"></a>
