<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="vctk" />
  <meta itemprop="description" content="This CSTR VCTK Corpus includes speech data uttered by 110 English speakers with&#10;various accents. Each speaker reads out about 400 sentences, which were selected&#10;from a newspaper, the rainbow passage and an elicitation paragraph used for the&#10;speech accent archive.&#10;&#10;Note that the &#x27;p315&#x27; text was lost due to a hard disk error.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;vctk&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/vctk" />
  <meta itemprop="sameAs" content="https://doi.org/10.7488/ds/2645" />
  <meta itemprop="citation" content="@misc{yamagishi2019vctk,&#10;  author={Yamagishi, Junichi and Veaux, Christophe and MacDonald, Kirsten},&#10;  title={{CSTR VCTK Corpus}: English Multi-speaker Corpus for {CSTR} Voice Cloning Toolkit (version 0.92)},&#10;  publisher={University of Edinburgh. The Centre for Speech Technology Research (CSTR)},&#10;  year=2019,&#10;  doi={10.7488/ds/2645},&#10;}" />
</div>

# `vctk`


*   **Description**:

This CSTR VCTK Corpus includes speech data uttered by 110 English speakers with
various accents. Each speaker reads out about 400 sentences, which were selected
from a newspaper, the rainbow passage and an elicitation paragraph used for the
speech accent archive.

Note that the 'p315' text was lost due to a hard disk error.

*   **Homepage**:
    [https://doi.org/10.7488/ds/2645](https://doi.org/10.7488/ds/2645)

*   **Source code**:
    [`tfds.audio.Vctk`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/vctk.py)

*   **Versions**:

    *   **`1.0.0`** (default): VCTK release 0.92.0.

*   **Download size**: `10.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=13),
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'id': tf.string,
    'speaker': ClassLabel(shape=(), dtype=tf.int64, num_classes=110),
    'speech': Audio(shape=(None,), dtype=tf.int64),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'speech')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{yamagishi2019vctk,
  author={Yamagishi, Junichi and Veaux, Christophe and MacDonald, Kirsten},
  title={{CSTR VCTK Corpus}: English Multi-speaker Corpus for {CSTR} Voice Cloning Toolkit (version 0.92)},
  publisher={University of Edinburgh. The Centre for Speech Technology Research (CSTR)},
  year=2019,
  doi={10.7488/ds/2645},
}
```

## vctk/mic1 (default config)

*   **Config description**: Audio recorded using an omni-directional microphone
    (DPA 4035). Contains very low frequency noises.

    ```
          This is the same audio released in previous versions of VCTK:
          https://doi.org/10.7488/ds/1994
    ```

*   **Dataset size**: `39.87 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 44,455

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/vctk-mic1-1.0.0.html";
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

## vctk/mic2

*   **Config description**: Audio recorded using a small diaphragm condenser
    microphone with very wide bandwidth (Sennheiser MKH 800).

    ```
          Two speakers, p280 and p315 had technical issues of the audio
          recordings using MKH 800.
    ```

*   **Dataset size**: `38.86 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,873

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/vctk-mic2-1.0.0.html";
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