<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="davis" />
  <meta itemprop="description" content="The DAVIS 2017 video object segmentation dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;davis&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/davis" />
  <meta itemprop="sameAs" content="https://davischallenge.org/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/Pont-TusetPCASG17,&#10;  author    = {Jordi Pont{-}Tuset and&#10;               Federico Perazzi and&#10;               Sergi Caelles and&#10;               Pablo Arbelaez and&#10;               Alexander Sorkine{-}Hornung and&#10;               Luc Van Gool},&#10;  title     = {The 2017 {DAVIS} Challenge on Video Object Segmentation},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1704.00675},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1704.00675},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1704.00675},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:55 +0200},&#10;  biburl    = {https://dblp.org/rec/journals/corr/Pont-TusetPCASG17.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `davis`


*   **Description**:

The DAVIS 2017 video object segmentation dataset.

*   **Homepage**: [https://davischallenge.org/](https://davischallenge.org/)

*   **Source code**:
    [`tfds.video.davis.Davis`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/davis/davis.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `2.0.0`: Change instance ids to be 0, 1, 2, ...
    *   **`2.1.0`** (default): Fix instance ids order.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 60
`'validation'` | 30

*   **Features**:

```python
FeaturesDict({
    'metadata': FeaturesDict({
        'num_frames': tf.int64,
        'video_name': tf.string,
    }),
    'video': Sequence({
        'frames': Image(shape=(None, None, 3), dtype=tf.uint8),
        'segmentations': Image(shape=(None, None, 1), dtype=tf.uint8),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{DBLP:journals/corr/Pont-TusetPCASG17,
  author    = {Jordi Pont{-}Tuset and
               Federico Perazzi and
               Sergi Caelles and
               Pablo Arbelaez and
               Alexander Sorkine{-}Hornung and
               Luc Van Gool},
  title     = {The 2017 {DAVIS} Challenge on Video Object Segmentation},
  journal   = {CoRR},
  volume    = {abs/1704.00675},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.00675},
  archivePrefix = {arXiv},
  eprint    = {1704.00675},
  timestamp = {Mon, 13 Aug 2018 16:48:55 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/Pont-TusetPCASG17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## davis/480p (default config)

*   **Config description**: The 480p version of the dataset

*   **Download size**: `794.19 MiB`

*   **Dataset size**: `792.26 MiB`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/davis-480p-2.1.0.html";
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

## davis/full_resolution

*   **Config description**: The full resolution version of the dataset.

*   **Download size**: `2.75 GiB`

*   **Dataset size**: `2.78 GiB`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/davis-full_resolution-2.1.0.html";
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