<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="titanic" />
  <meta itemprop="description" content="Dataset describing the survival status of individual passengers on the Titanic. Missing values in the original dataset are represented using ?. Float and int missing values are replaced with -1, string missing values are replaced with &#x27;Unknown&#x27;.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;titanic&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/titanic" />
  <meta itemprop="sameAs" content="https://www.openml.org/d/40945" />
  <meta itemprop="citation" content="@ONLINE {titanic,&#10;author = &quot;Frank E. Harrell Jr., Thomas Cason&quot;,&#10;title  = &quot;Titanic dataset&quot;,&#10;month  = &quot;oct&quot;,&#10;year   = &quot;2017&quot;,&#10;url    = &quot;https://www.openml.org/d/40945&quot;&#10;}" />
</div>
# `titanic`

*   **Description**:

Dataset describing the survival status of individual passengers on the Titanic. Missing values in the original dataset are represented using ?. Float and int missing values are replaced with -1, string missing values are replaced with 'Unknown'.

*   **Homepage**: [https://www.openml.org/d/40945](https://www.openml.org/d/40945)

*   **Source code**: [`tfds.structured.Titanic`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/titanic.py)

*   **Versions**:

    * **`2.0.0`** (default): No release notes.

*   **Download size**: `114.98 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached** ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)): Unknown

*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1,309

*   **Features**:

```python
FeaturesDict({
    'features': FeaturesDict({
        'age': tf.float32,
        'boat': tf.string,
        'body': tf.int32,
        'cabin': tf.string,
        'embarked': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
        'fare': tf.float32,
        'home.dest': tf.string,
        'name': tf.string,
        'parch': tf.int32,
        'pclass': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
        'sex': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'sibsp': tf.int32,
        'ticket': tf.string,
    }),
    'survived': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

*   **Supervised keys** (See [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)): `('features', 'survived')`

*   **Citation**:

```
@ONLINE {titanic,
author = "Frank E. Harrell Jr., Thomas Cason",
title  = "Titanic dataset",
month  = "oct",
year   = "2017",
url    = "https://www.openml.org/d/40945"
}
```

*   **Figure** ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)): Not supported.

*   **Examples** ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>

<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>

<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/titanic-2.0.0.html";
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
