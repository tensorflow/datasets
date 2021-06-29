<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quickdraw_bitmap" />
  <meta itemprop="description" content="The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The bitmap dataset contains these drawings converted from vector format into 28x28 grayscale images&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;quickdraw_bitmap&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/quickdraw_bitmap-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quickdraw_bitmap" />
  <meta itemprop="sameAs" content="https://github.com/googlecreativelab/quickdraw-dataset" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/HaE17,&#10;  author    = {David Ha and&#10;               Douglas Eck},&#10;  title     = {A Neural Representation of Sketch Drawings},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1704.03477},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1704.03477},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1704.03477},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:30 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/HaE17},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `quickdraw_bitmap`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=quickdraw_bitmap">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The Quick Draw Dataset is a collection of 50 million drawings across 345
categories, contributed by players of the game Quick, Draw!. The bitmap dataset
contains these drawings converted from vector format into 28x28 grayscale images

*   **Homepage**:
    [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)

*   **Source code**:
    [`tfds.image_classification.QuickdrawBitmap`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/quickdraw.py)

*   **Versions**:

    *   **`3.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `36.82 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 50,426,266

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=345),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/quickdraw_bitmap-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/quickdraw_bitmap-3.0.0.html";
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

*   **Citation**:

```
@article{DBLP:journals/corr/HaE17,
  author    = {David Ha and
               Douglas Eck},
  title     = {A Neural Representation of Sketch Drawings},
  journal   = {CoRR},
  volume    = {abs/1704.03477},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.03477},
  archivePrefix = {arXiv},
  eprint    = {1704.03477},
  timestamp = {Mon, 13 Aug 2018 16:48:30 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/HaE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
