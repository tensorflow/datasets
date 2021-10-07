<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="binary_alpha_digits" />
  <meta itemprop="description" content="Binary 20x16 digits of &#x27;0&#x27; through &#x27;9&#x27; and capital &#x27;A&#x27; through &#x27;Z&#x27;. 39 examples of each class.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;binary_alpha_digits&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/binary_alpha_digits-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/binary_alpha_digits" />
  <meta itemprop="sameAs" content="https://cs.nyu.edu/~roweis/data/" />
  <meta itemprop="citation" content="&#10;" />
</div>

# `binary_alpha_digits`


*   **Description**:

Binary 20x16 digits of '0' through '9' and capital 'A' through 'Z'. 39 examples
of each class.

*   **Homepage**:
    [https://cs.nyu.edu/~roweis/data/](https://cs.nyu.edu/~roweis/data/)

*   **Source code**:
    [`tfds.image_classification.BinaryAlphaDigits`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/binary_alpha_digits.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `519.83 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,404

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(20, 16, 1), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=36),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/binary_alpha_digits-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/binary_alpha_digits-1.0.0.html";
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

```
