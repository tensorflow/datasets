<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="accentdb" />
  <meta itemprop="description" content="AccentDB is a multi-pairwise parallel corpus of structured and labelled&#10;accented speech. It contains speech samples from speakers of 4 non-native&#10;accents of English (8 speakers, 4 Indian languages); and also has a compilation&#10;of 4 native accents of English (4 countries, 13 speakers) and a metropolitan&#10;Indian accent (2 speakers). The dataset available here corresponds to release&#10;titled accentdb_extended on https://accentdb.github.io/#dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;accentdb&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/accentdb" />
  <meta itemprop="sameAs" content="https://accentdb.github.io/" />
  <meta itemprop="citation" content="@InProceedings{ahamad-anand-bhargava:2020:LREC,&#10;  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},&#10;  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},&#10;  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},&#10;  month          = {May},&#10;  year           = {2020},&#10;  address        = {Marseille, France},&#10;  publisher      = {European Language Resources Association},&#10;  pages     = {5353--5360},&#10;  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}&#10;}" />
</div>

# `accentdb`


*   **Description**:

AccentDB is a multi-pairwise parallel corpus of structured and labelled accented
speech. It contains speech samples from speakers of 4 non-native accents of
English (8 speakers, 4 Indian languages); and also has a compilation of 4 native
accents of English (4 countries, 13 speakers) and a metropolitan Indian accent
(2 speakers). The dataset available here corresponds to release titled
accentdb_extended on https://accentdb.github.io/#dataset.

*   **Homepage**: [https://accentdb.github.io/](https://accentdb.github.io/)

*   **Source code**:
    [`tfds.audio.Accentdb`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/accentdb.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `3.56 GiB`

*   **Dataset size**: `19.47 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 17,313

*   **Features**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=9),
    'speaker_id': tf.string,
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/accentdb-1.0.0.html";
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
@InProceedings{ahamad-anand-bhargava:2020:LREC,
  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},
  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},
  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},
  month          = {May},
  year           = {2020},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5353--5360},
  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}
}
```
