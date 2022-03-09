<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tao" />
  <meta itemprop="description" content="The TAO dataset is a large video object detection dataset consisting of&#10;2,907 high resolution videos and 833 object categories. Note that this dataset&#10;requires at least 300 GB of free space to store.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tao&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tao" />
  <meta itemprop="sameAs" content="https://taodataset.org/" />
  <meta itemprop="citation" content="@article{Dave_2020,&#10;   title={TAO: A Large-Scale Benchmark for Tracking Any Object},&#10;   ISBN={9783030585587},&#10;   ISSN={1611-3349},&#10;   url={http://dx.doi.org/10.1007/978-3-030-58558-7_26},&#10;   DOI={10.1007/978-3-030-58558-7_26},&#10;   journal={Lecture Notes in Computer Science},&#10;   publisher={Springer International Publishing},&#10;   author={Dave, Achal and Khurana, Tarasha and Tokmakov, Pavel and Schmid, Cordelia and Ramanan, Deva},&#10;   year={2020},&#10;   pages={436-454}&#10;}" />
</div>

# `tao`


Warning: Manual download required. See instructions below.

*   **Description**:

The TAO dataset is a large video object detection dataset consisting of 2,907
high resolution videos and 833 object categories. Note that this dataset
requires at least 300 GB of free space to store.

*   **Homepage**: [https://taodataset.org/](https://taodataset.org/)

*   **Source code**:
    [`tfds.video.tao.Tao`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/tao/tao.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `113.96 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Some TAO files (HVACS and AVA videos) must be manually downloaded because
    a login to MOT is required. Please download and those data following
    the instructions at https://motchallenge.net/tao_download.php

Download this data and move the resulting .zip files to
~/tensorflow_datasets/downloads/manual/

If the data requiring manual download is not present, it will be skipped over
and only the data not requiring manual download will be used.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 500
`'validation'` | 988

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{Dave_2020,
   title={TAO: A Large-Scale Benchmark for Tracking Any Object},
   ISBN={9783030585587},
   ISSN={1611-3349},
   url={http://dx.doi.org/10.1007/978-3-030-58558-7_26},
   DOI={10.1007/978-3-030-58558-7_26},
   journal={Lecture Notes in Computer Science},
   publisher={Springer International Publishing},
   author={Dave, Achal and Khurana, Tarasha and Tokmakov, Pavel and Schmid, Cordelia and Ramanan, Deva},
   year={2020},
   pages={436-454}
}
```


## tao/480_640 (default config)

*   **Config description**: All images are bilinearly resized to 480 X 640

*   **Dataset size**: `482.30 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'dataset': tf.string,
        'height': tf.int32,
        'neg_category_ids': Tensor(shape=(None,), dtype=tf.int32),
        'not_exhaustive_category_ids': Tensor(shape=(None,), dtype=tf.int32),
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=363),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'scale_category': tf.string,
        'track_id': tf.int32,
    }),
    'video': Video(Image(shape=(480, 640, 3), dtype=tf.uint8)),
})
```

*   **Feature documentation**:

Feature                              | Class                 | Shape               | Dtype      | Description
:----------------------------------- | :-------------------- | :------------------ | :--------- | :----------
                                     | FeaturesDict          |                     |            |
metadata                             | FeaturesDict          |                     |            |
metadata/dataset                     | Tensor                |                     | tf.string  |
metadata/height                      | Tensor                |                     | tf.int32   |
metadata/neg_category_ids            | Tensor                | (None,)             | tf.int32   |
metadata/not_exhaustive_category_ids | Tensor                | (None,)             | tf.int32   |
metadata/num_frames                  | Tensor                |                     | tf.int32   |
metadata/video_name                  | Tensor                |                     | tf.string  |
metadata/width                       | Tensor                |                     | tf.int32   |
tracks                               | Sequence              |                     |            |
tracks/bboxes                        | Sequence(BBoxFeature) | (None, 4)           | tf.float32 |
tracks/category                      | ClassLabel            |                     | tf.int64   |
tracks/frames                        | Sequence(Tensor)      | (None,)             | tf.int32   |
tracks/is_crowd                      | Tensor                |                     | tf.bool    |
tracks/scale_category                | Tensor                |                     | tf.string  |
tracks/track_id                      | Tensor                |                     | tf.int32   |
video                                | Video(Image)          | (None, 480, 640, 3) | tf.uint8   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tao-480_640-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## tao/full_resolution

*   **Config description**: The full resolution version of the dataset.

*   **Dataset size**: `171.24 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'dataset': tf.string,
        'height': tf.int32,
        'neg_category_ids': Tensor(shape=(None,), dtype=tf.int32),
        'not_exhaustive_category_ids': Tensor(shape=(None,), dtype=tf.int32),
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=363),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'scale_category': tf.string,
        'track_id': tf.int32,
    }),
    'video': Video(Image(shape=(None, None, 3), dtype=tf.uint8)),
})
```

*   **Feature documentation**:

Feature                              | Class                 | Shape                 | Dtype      | Description
:----------------------------------- | :-------------------- | :-------------------- | :--------- | :----------
                                     | FeaturesDict          |                       |            |
metadata                             | FeaturesDict          |                       |            |
metadata/dataset                     | Tensor                |                       | tf.string  |
metadata/height                      | Tensor                |                       | tf.int32   |
metadata/neg_category_ids            | Tensor                | (None,)               | tf.int32   |
metadata/not_exhaustive_category_ids | Tensor                | (None,)               | tf.int32   |
metadata/num_frames                  | Tensor                |                       | tf.int32   |
metadata/video_name                  | Tensor                |                       | tf.string  |
metadata/width                       | Tensor                |                       | tf.int32   |
tracks                               | Sequence              |                       |            |
tracks/bboxes                        | Sequence(BBoxFeature) | (None, 4)             | tf.float32 |
tracks/category                      | ClassLabel            |                       | tf.int64   |
tracks/frames                        | Sequence(Tensor)      | (None,)               | tf.int32   |
tracks/is_crowd                      | Tensor                |                       | tf.bool    |
tracks/scale_category                | Tensor                |                       | tf.string  |
tracks/track_id                      | Tensor                |                       | tf.int32   |
video                                | Video(Image)          | (None, None, None, 3) | tf.uint8   |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tao-full_resolution-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->