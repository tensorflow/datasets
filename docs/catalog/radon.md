<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="radon" />
  <meta itemprop="description" content="Radon is a radioactive gas that enters homes through contact&#10;points with the ground. It is a carcinogen that is the primary cause of lung&#10;cancer in non-smokers. Radon levels vary greatly from household to household.&#10;This dataset contains measured radon levels in U.S homes by county and state.&#10;The &#x27;activity&#x27; label is the measured radon concentration in pCi/L. Important&#10;predictors are &#x27;floor&#x27; (the floor of the house in which the measurement was&#10;taken), &#x27;county&#x27; (the U.S. county in which the house is located), and &#x27;Uppm&#x27; (a&#10;measurement of uranium level of the soil by county).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;radon&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/radon" />
  <meta itemprop="sameAs" content="http://www.stat.columbia.edu/~gelman/arm/examples/radon/" />
  <meta itemprop="citation" content="@book{GelmanHill:2007,&#10;  author = {Gelman, Andrew and Hill, Jennifer},&#10;  title = {Data Analysis Using Regression and Multilevel/Hierarchical Models},&#10;  publisher = {Cambridge University Press},&#10;  series = {Analytical methods for social research},&#10;  year = 2007&#10;}" />
</div>

# `radon`


*   **Description**:

Radon is a radioactive gas that enters homes through contact points with the
ground. It is a carcinogen that is the primary cause of lung cancer in
non-smokers. Radon levels vary greatly from household to household. This dataset
contains measured radon levels in U.S homes by county and state. The 'activity'
label is the measured radon concentration in pCi/L. Important predictors are
'floor' (the floor of the house in which the measurement was taken), 'county'
(the U.S. county in which the house is located), and 'Uppm' (a measurement of
uranium level of the soil by county).

*   **Homepage**:
    [http://www.stat.columbia.edu/~gelman/arm/examples/radon/](http://www.stat.columbia.edu/~gelman/arm/examples/radon/)

*   **Source code**:
    [`tfds.structured.Radon`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/radon.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.71 MiB`

*   **Dataset size**: `9.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,573

*   **Features**:

```python
FeaturesDict({
    'activity': tf.float32,
    'features': FeaturesDict({
        'Uppm': tf.float32,
        'adjwt': tf.float32,
        'basement': tf.string,
        'cntyfips': tf.int32,
        'county': tf.string,
        'dupflag': tf.int32,
        'floor': tf.int32,
        'idnum': tf.int32,
        'lat': tf.float32,
        'lon': tf.float32,
        'pcterr': tf.float32,
        'region': tf.int32,
        'rep': tf.int32,
        'room': tf.int32,
        'startdt': tf.int32,
        'starttm': tf.int32,
        'state': tf.string,
        'state2': tf.string,
        'stfips': tf.int32,
        'stopdt': tf.int32,
        'stoptm': tf.int32,
        'stratum': tf.int32,
        'typebldg': tf.int32,
        'wave': tf.int32,
        'windoor': tf.string,
        'zip': tf.int32,
        'zipflag': tf.int32,
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'activity')`

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/radon-1.0.0.html";
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
@book{GelmanHill:2007,
  author = {Gelman, Andrew and Hill, Jennifer},
  title = {Data Analysis Using Regression and Multilevel/Hierarchical Models},
  publisher = {Cambridge University Press},
  series = {Analytical methods for social research},
  year = 2007
}
```
