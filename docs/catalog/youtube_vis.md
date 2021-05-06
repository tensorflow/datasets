<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="youtube_vis" />
  <meta itemprop="description" content="Youtube-vis is a video instance segmentation dataset. It contains 2,883&#10;high-resolution YouTube videos, a per-pixel category label set including 40&#10;common objects such as person, animals and vehicles, 4,883 unique video&#10;instances, and 131k high-quality manual annotations.&#10;&#10;The YouTube-VIS dataset is split into 2,238 training videos, 302 validation&#10;videos and 343 test videos.&#10;&#10;No files were removed or altered during preprocessing.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;youtube_vis&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/youtube_vis" />
  <meta itemprop="sameAs" content="https://youtube-vos.org/dataset/vis/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1905-04804,&#10;  author    = {Linjie Yang and&#10;               Yuchen Fan and&#10;               Ning Xu},&#10;  title     = {Video Instance Segmentation},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1905.04804},&#10;  year      = {2019},&#10;  url       = {http://arxiv.org/abs/1905.04804},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1905.04804},&#10;  timestamp = {Tue, 28 May 2019 12:48:08 +0200},&#10;  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-04804.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `youtube_vis`

Warning: Manual download required. See instructions below.

*   **Description**:

Youtube-vis is a video instance segmentation dataset. It contains 2,883
high-resolution YouTube videos, a per-pixel category label set including 40
common objects such as person, animals and vehicles, 4,883 unique video
instances, and 131k high-quality manual annotations.

The YouTube-VIS dataset is split into 2,238 training videos, 302 validation
videos and 343 test videos.

No files were removed or altered during preprocessing.

*   **Homepage**:
    [https://youtube-vos.org/dataset/vis/](https://youtube-vos.org/dataset/vis/)

*   **Source code**:
    [`tfds.video.youtube_vis.YoutubeVis`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/youtube_vis/youtube_vis.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Please download all files for the 2019 version of the dataset
    (test_all_frames.zip, test.json, train_all_frames.zip, train.json,
    valid_all_frames.zip, valid.json) from the youtube-vis website
    and move them to ~/tensorflow_datasets/downloads/manual/.

Note that the dataset landing page is located at
https://youtube-vos.org/dataset/vis/, and it will then redirect you to a page on
https://competitions.codalab.org where you can download the 2019 version of the
dataset. You will need to make an account on codalab to download the data. Note
that at the time of writing this, you will need to bypass a "Connection not
secure" warning when accessing codalab.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{DBLP:journals/corr/abs-1905-04804,
  author    = {Linjie Yang and
               Yuchen Fan and
               Ning Xu},
  title     = {Video Instance Segmentation},
  journal   = {CoRR},
  volume    = {abs/1905.04804},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.04804},
  archivePrefix = {arXiv},
  eprint    = {1905.04804},
  timestamp = {Tue, 28 May 2019 12:48:08 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-04804.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## youtube_vis/full (default config)

*   **Config description**: The full resolution version of the dataset, with all
    frames, including those without labels, included.

*   **Dataset size**: `33.31 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 343
`'train'`      | 2,238
`'validation'` | 302

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(None, None, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(None, None, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-full-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/480_640_full

*   **Config description**: All images are bilinearly resized to 480 X 640 with
    all frames included.

*   **Dataset size**: `130.02 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 343
`'train'`      | 2,238
`'validation'` | 302

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(480, 640, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(480, 640, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-480_640_full-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/480_640_only_frames_with_labels

*   **Config description**: All images are bilinearly resized to 480 X 640 with
    only frames with labels included.

*   **Dataset size**: `26.27 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 343
`'train'`      | 2,238
`'validation'` | 302

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(480, 640, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(480, 640, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-480_640_only_frames_with_labels-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/only_frames_with_labels

*   **Config description**: Only images with labels included at their native
    resolution.

*   **Dataset size**: `6.91 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 343
`'train'`      | 2,238
`'validation'` | 302

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(None, None, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(None, None, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-only_frames_with_labels-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/full_train_split

*   **Config description**: The full resolution version of the dataset, with all
    frames, including those without labels, included. The val and test splits
    are manufactured from the training data.

*   **Dataset size**: `26.09 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 200
`'train'`      | 1,838
`'validation'` | 200

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(None, None, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(None, None, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-full_train_split-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/480_640_full_train_split

*   **Config description**: All images are bilinearly resized to 480 X 640 with
    all frames included. The val and test splits are manufactured from the
    training data.

*   **Dataset size**: `101.57 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 200
`'train'`      | 1,838
`'validation'` | 200

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(480, 640, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(480, 640, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-480_640_full_train_split-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/480_640_only_frames_with_labels_train_split

*   **Config description**: All images are bilinearly resized to 480 X 640 with
    only frames with labels included. The val and test splits are manufactured
    from the training data.

*   **Dataset size**: `20.55 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 200
`'train'`      | 1,838
`'validation'` | 200

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(480, 640, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(480, 640, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-480_640_only_frames_with_labels_train_split-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## youtube_vis/only_frames_with_labels_train_split

*   **Config description**: Only images with labels included at their native
    resolution. The val and test splits are manufactured from the training data.

*   **Dataset size**: `5.46 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 200
`'train'`      | 1,838
`'validation'` | 200

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'height': tf.int32,
        'num_frames': tf.int32,
        'video_name': tf.string,
        'width': tf.int32,
    }),
    'tracks': Sequence({
        'areas': Sequence(tf.float32),
        'bboxes': Sequence(BBoxFeature(shape=(4,), dtype=tf.float32)),
        'category': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
        'frames': Sequence(tf.int32),
        'is_crowd': tf.bool,
        'segmentations': Video(Image(shape=(None, None, 1), dtype=tf.uint8)),
    }),
    'video': Video(Image(shape=(None, None, 3), dtype=tf.uint8)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/youtube_vis-only_frames_with_labels_train_split-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->