<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gtzan" />
  <meta itemprop="description" content="The dataset consists of 1000 audio tracks each 30 seconds long.&#10;It contains 10 genres, each represented by 100 tracks.&#10;The tracks are all 22050Hz Mono 16-bit audio files in .wav format.&#10;&#10;The genres are:&#10;&#10;* blues&#10;* classical&#10;* country&#10;* disco&#10;* hiphop&#10;* jazz&#10;* metal&#10;* pop&#10;* reggae&#10;* rock&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gtzan&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gtzan" />
  <meta itemprop="sameAs" content="http://marsyas.info/index.html" />
  <meta itemprop="citation" content="@misc{tzanetakis_essl_cook_2001,&#10;author    = &quot;Tzanetakis, George and Essl, Georg and Cook, Perry&quot;,&#10;title     = &quot;Automatic Musical Genre Classification Of Audio Signals&quot;,&#10;url       = &quot;http://ismir2001.ismir.net/pdf/tzanetakis.pdf&quot;,&#10;publisher = &quot;The International Society for Music Information Retrieval&quot;,&#10;year      = &quot;2001&quot;&#10;}" />
</div>

# `gtzan`


*   **Description**:

The dataset consists of 1000 audio tracks each 30 seconds long. It contains 10
genres, each represented by 100 tracks. The tracks are all 22050Hz Mono 16-bit
audio files in .wav format.

The genres are:

*   blues
*   classical
*   country
*   disco
*   hiphop
*   jazz
*   metal
*   pop
*   reggae
*   rock

*   **Homepage**:
    [http://marsyas.info/index.html](http://marsyas.info/index.html)

*   **Source code**:
    [`tfds.audio.gtzan.GTZAN`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/gtzan/gtzan.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.14 GiB`

*   **Dataset size**: `3.71 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'audio/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gtzan-1.0.0.html";
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
@misc{tzanetakis_essl_cook_2001,
author    = "Tzanetakis, George and Essl, Georg and Cook, Perry",
title     = "Automatic Musical Genre Classification Of Audio Signals",
url       = "http://ismir2001.ismir.net/pdf/tzanetakis.pdf",
publisher = "The International Society for Music Information Retrieval",
year      = "2001"
}
```
