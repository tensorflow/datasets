<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xtreme_xnli" />
  <meta itemprop="description" content="This dataset contains machine translations of MNLI into each of the XNLI&#10;languages. The translation data is provided by XTREME. Note that this is&#10;different from the machine translated data provided by the original XNLI paper.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xtreme_xnli&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xtreme_xnli" />
  <meta itemprop="sameAs" content="https://www.nyu.edu/projects/bowman/xnli/" />
  <meta itemprop="citation" content="@article{hu2020xtreme,&#10;      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},&#10;      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},&#10;      journal   = {CoRR},&#10;      volume    = {abs/2003.11080},&#10;      year      = {2020},&#10;      archivePrefix = {arXiv},&#10;      eprint    = {2003.11080}&#10;}" />
</div>

# `xtreme_xnli`


*   **Description**:

This dataset contains machine translations of MNLI into each of the XNLI
languages. The translation data is provided by XTREME. Note that this is
different from the machine translated data provided by the original XNLI paper.

*   **Homepage**:
    [https://www.nyu.edu/projects/bowman/xnli/](https://www.nyu.edu/projects/bowman/xnli/)

*   **Source code**:
    [`tfds.text.xtreme_xnli.XtremeXnli`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/xtreme_xnli/xtreme_xnli.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Download size**: `2.31 GiB`

*   **Dataset size**: `1.59 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 392,570

*   **Features**:

```python
FeaturesDict({
    'hypothesis': TranslationVariableLanguages({
        'language': Text(shape=(), dtype=tf.string),
        'translation': Text(shape=(), dtype=tf.string),
    }),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Translation({
        'ar': Text(shape=(), dtype=tf.string),
        'bg': Text(shape=(), dtype=tf.string),
        'de': Text(shape=(), dtype=tf.string),
        'el': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
        'es': Text(shape=(), dtype=tf.string),
        'fr': Text(shape=(), dtype=tf.string),
        'hi': Text(shape=(), dtype=tf.string),
        'ru': Text(shape=(), dtype=tf.string),
        'sw': Text(shape=(), dtype=tf.string),
        'th': Text(shape=(), dtype=tf.string),
        'tr': Text(shape=(), dtype=tf.string),
        'ur': Text(shape=(), dtype=tf.string),
        'vi': Text(shape=(), dtype=tf.string),
        'zh': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_xnli-1.1.0.html";
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
@article{hu2020xtreme,
      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},
      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},
      journal   = {CoRR},
      volume    = {abs/2003.11080},
      year      = {2020},
      archivePrefix = {arXiv},
      eprint    = {2003.11080}
}
```
