<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rock_you" />
  <meta itemprop="description" content="This dataset contains 14,344,391 passwords that were leaked or stolen from&#10;various sites. The author of this dataset states that &quot;I&#x27;m hosting them because&#10;it seems like nobody else does (hopefully it isn&#x27;t because hosting them is&#10;illegal :)). Naturally, I&#x27;m not the one who stole these; I simply found them&#10;online, removed any names/email addresses/etc.&quot;.&#10;&#10;This dataset is used to train Machine Learning models for password guessing&#10;and cracking.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rock_you&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rock_you" />
  <meta itemprop="sameAs" content="https://wiki.skullsecurity.org/Passwords" />
  <meta itemprop="citation" content="" />
</div>

# `rock_you`


*   **Description**:

This dataset contains 14,344,391 passwords that were leaked or stolen from
various sites. The author of this dataset states that "I'm hosting them because
it seems like nobody else does (hopefully it isn't because hosting them is
illegal :)). Naturally, I'm not the one who stole these; I simply found them
online, removed any names/email addresses/etc.".

This dataset is used to train Machine Learning models for password guessing and
cracking.

*   **Homepage**:
    [https://wiki.skullsecurity.org/Passwords](https://wiki.skullsecurity.org/Passwords)

*   **Source code**:
    [`tfds.structured.RockYou`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/rock_you.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `133.44 MiB`

*   **Dataset size**: `393.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 14,344,391

*   **Features**:

```python
FeaturesDict({
    'password': Text(shape=(), dtype=tf.string),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rock_you-1.0.0.html";
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
