<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="webvid" />
  <meta itemprop="description" content="WebVid is a large-scale dataset of short videos &#10;with textual descriptions sourced from the web. &#10;The videos are diverse and rich in their content.&#10;&#10;WebVid-10M contains:&#10;&#10;10.7M video-caption pairs.&#10;52K total video hours.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;webvid&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/webvid" />
  <meta itemprop="sameAs" content="https://m-bain.github.io/webvid-dataset/" />
  <meta itemprop="citation" content="@misc{bain2021frozen,&#10;      title={Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval},&#10;      author={Max Bain and Arsha Nagrani and Gül Varol and Andrew Zisserman},&#10;      year={2021},&#10;      eprint={2104.00650},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CV}&#10;}" />
</div>

# `webvid`


Warning: Manual download required. See instructions below.

*   **Description**:

WebVid is a large-scale dataset of short videos with textual descriptions
sourced from the web. The videos are diverse and rich in their content.

WebVid-10M contains:

10.7M video-caption pairs. 52K total video hours.

*   **Homepage**:
    [https://m-bain.github.io/webvid-dataset/](https://m-bain.github.io/webvid-dataset/)

*   **Source code**:
    [`tfds.datasets.webvid.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/webvid/webvid_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Follow the download instructions in https://m-bain.github.io/webvid-dataset/
    to get the data. Place the csv files and the video directories in
    `manual_dir/webvid`, such that mp4 files are placed in
    `manual_dir/webvid/*/*_*/*.mp4`.

First directory typically being an arbitrary part directory (for sharded
downloading), second directory is the page directory (two numbers around
underscore), inside of which there is one or more mp4 files.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'caption': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
    'video': Video(Image(shape=(360, 640, 3), dtype=uint8)),
})
```

*   **Feature documentation**:

Feature | Class        | Shape               | Dtype  | Description
:------ | :----------- | :------------------ | :----- | :----------
        | FeaturesDict |                     |        |
caption | Text         |                     | string |
id      | Text         |                     | string |
url     | Text         |                     | string |
video   | Video(Image) | (None, 360, 640, 3) | uint8  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@misc{bain2021frozen,
      title={Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval},
      author={Max Bain and Arsha Nagrani and Gül Varol and Andrew Zisserman},
      year={2021},
      eprint={2104.00650},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

