<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asset" />
  <meta itemprop="description" content="ASSET is a dataset for evaluating Sentence Simplification systems with multiple rewriting transformations, as described in &quot;ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations.&quot; The corpus is composed of 2000 validation and 359 test original sentences that were each simplified 10 times by different annotators. The corpus also contains human judgments of meaning preservation, fluency and simplicity for the outputs of several automatic text simplification systems.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asset&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asset" />
  <meta itemprop="sameAs" content="https://github.com/facebookresearch/asset" />
  <meta itemprop="citation" content="@inproceedings{alva-manchego-etal-2020-asset,&#10;    title = &quot;{ASSET}: {A} Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations&quot;,&#10;    author = &quot;Alva-Manchego, Fernando  and&#10;      Martin, Louis  and&#10;      Bordes, Antoine  and&#10;      Scarton, Carolina  and&#10;      Sagot, Benoit  and&#10;      Specia, Lucia&quot;,&#10;    booktitle = &quot;Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics&quot;,&#10;    month = jul,&#10;    year = &quot;2020&quot;,&#10;    address = &quot;Online&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/2020.acl-main.424&quot;,&#10;    pages = &quot;4668--4679&quot;,&#10;}" />
</div>

# `asset`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

ASSET is a dataset for evaluating Sentence Simplification systems with multiple
rewriting transformations, as described in "ASSET: A Dataset for Tuning and
Evaluation of Sentence Simplification Models with Multiple Rewriting
Transformations." The corpus is composed of 2000 validation and 359 test
original sentences that were each simplified 10 times by different annotators.
The corpus also contains human judgments of meaning preservation, fluency and
simplicity for the outputs of several automatic text simplification systems.

*   **Homepage**:
    [https://github.com/facebookresearch/asset](https://github.com/facebookresearch/asset)

*   **Source code**:
    [`tfds.text_simplification.asset.Asset`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text_simplification/asset/asset.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{alva-manchego-etal-2020-asset,
    title = "{ASSET}: {A} Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations",
    author = "Alva-Manchego, Fernando  and
      Martin, Louis  and
      Bordes, Antoine  and
      Scarton, Carolina  and
      Sagot, Benoit  and
      Specia, Lucia",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.424",
    pages = "4668--4679",
}
```


## asset/simplification (default config)

*   **Config description**: A set of original sentences aligned with 10 possible
    simplifications for each.

*   **Dataset size**: `2.64 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 359
`'validation'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'original': Text(shape=(), dtype=tf.string),
    'simplifications': Sequence(Text(shape=(), dtype=tf.string)),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asset-simplification-1.0.0.html";
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

## asset/ratings

*   **Config description**: Human ratings of automatically produced text
    simplification.

*   **Dataset size**: `1.44 MiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'full'` | 4,500

*   **Features**:

```python
FeaturesDict({
    'aspect': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'original': Text(shape=(), dtype=tf.string),
    'original_sentence_id': tf.int32,
    'rating': tf.int32,
    'simplification': Text(shape=(), dtype=tf.string),
    'worker_id': tf.int32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asset-ratings-1.0.0.html";
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