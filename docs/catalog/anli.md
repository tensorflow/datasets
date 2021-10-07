<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="anli" />
  <meta itemprop="description" content="Adversarial NLI (ANLI) is a large-scale NLI benchmark dataset, collected via an&#10;iterative, adversarial human-and-model-in-the-loop procedure.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;anli&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/anli" />
  <meta itemprop="sameAs" content="https://github.com/facebookresearch/anli" />
  <meta itemprop="citation" content="@inproceedings{Nie2019AdversarialNA,&#10;    title = &quot;Adversarial NLI: A New Benchmark for Natural Language Understanding&quot;,&#10;    author = &quot;Nie, Yixin and&#10;      Williams, Adina and&#10;      Dinan, Emily  and&#10;      Bansal, Mohit and&#10;      Weston, Jason and&#10;      Kiela, Douwe&quot;,&#10;      year=&quot;2019&quot;,&#10;    url =&quot;https://arxiv.org/abs/1910.14599&quot;&#10;}" />
</div>

# `anli`


*   **Description**:

Adversarial NLI (ANLI) is a large-scale NLI benchmark dataset, collected via an
iterative, adversarial human-and-model-in-the-loop procedure.

*   **Homepage**:
    [https://github.com/facebookresearch/anli](https://github.com/facebookresearch/anli)

*   **Source code**:
    [`tfds.text.Anli`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/anli.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `17.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'context': Text(shape=(), dtype=tf.string),
    'hypothesis': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'uid': Text(shape=(), dtype=tf.string),
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
@inproceedings{Nie2019AdversarialNA,
    title = "Adversarial NLI: A New Benchmark for Natural Language Understanding",
    author = "Nie, Yixin and
      Williams, Adina and
      Dinan, Emily  and
      Bansal, Mohit and
      Weston, Jason and
      Kiela, Douwe",
      year="2019",
    url ="https://arxiv.org/abs/1910.14599"
}
```

## anli/r1 (default config)

*   **Config description**: Round One

*   **Dataset size**: `9.04 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 16,946
`'validation'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/anli-r1-0.1.0.html";
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

## anli/r2

*   **Config description**: Round Two

*   **Dataset size**: `22.39 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 45,460
`'validation'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/anli-r2-0.1.0.html";
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

## anli/r3

*   **Config description**: Round Three

*   **Dataset size**: `47.03 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,200
`'train'`      | 100,459
`'validation'` | 1,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/anli-r3-0.1.0.html";
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