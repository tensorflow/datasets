<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="spoken_digit" />
  <meta itemprop="description" content="A free audio dataset of spoken digits. Think MNIST for audio.&#10;&#10;A simple audio/speech dataset consisting of recordings of spoken digits in wav files at 8kHz.&#10;The recordings are trimmed so that they have near minimal silence at the beginnings and ends.&#10;&#10;5 speakers&#10;2,500 recordings (50 of each digit per speaker)&#10;English pronunciations&#10;&#10;Files are named in the following format: {digitLabel}_{speakerName}_{index}.wav&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;spoken_digit&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/spoken_digit" />
  <meta itemprop="sameAs" content="https://github.com/Jakobovski/free-spoken-digit-dataset" />
  <meta itemprop="citation" content="@ONLINE {Free Spoken Digit Dataset,&#10;    author = &quot;Zohar Jackson&quot;,&#10;    title  = &quot;Spoken_Digit&quot;,&#10;    year   = &quot;2016&quot;,&#10;    url    = &quot;https://github.com/Jakobovski/free-spoken-digit-dataset&quot;&#10;}" />
</div>

# `spoken_digit`

*   **Description**:

A free audio dataset of spoken digits. Think MNIST for audio.

A simple audio/speech dataset consisting of recordings of spoken digits in wav
files at 8kHz. The recordings are trimmed so that they have near minimal silence
at the beginnings and ends.

5 speakers 2,500 recordings (50 of each digit per speaker) English
pronunciations

Files are named in the following format: {digitLabel}_{speakerName}_{index}.wav

*   **Homepage**:
    [https://github.com/Jakobovski/free-spoken-digit-dataset](https://github.com/Jakobovski/free-spoken-digit-dataset)

*   **Source code**:
    [`tfds.audio.spoken_digit.SpokenDigit`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/spoken_digit/spoken_digit.py)

*   **Versions**:

    *   **`1.0.9`** (default): No release notes.

*   **Download size**: `11.42 MiB`

*   **Dataset size**: `45.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,500

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
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/spoken_digit-1.0.9.html";
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
@ONLINE {Free Spoken Digit Dataset,
    author = "Zohar Jackson",
    title  = "Spoken_Digit",
    year   = "2016",
    url    = "https://github.com/Jakobovski/free-spoken-digit-dataset"
}
```
