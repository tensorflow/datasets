<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wine_quality" />
  <meta itemprop="description" content="Two datasets were created, using red and white wine samples.&#10;The inputs include objective tests (e.g. PH values) and the output is based on sensory data&#10;(median of at least 3 evaluations made by wine experts).&#10;Each expert graded the wine quality&#10;between 0 (very bad) and 10 (very excellent).&#10;Several data mining methods were applied to model&#10;these datasets under a regression approach. The support vector machine model achieved the&#10;best results. Several metrics were computed: MAD, confusion matrix for a fixed error tolerance (T),&#10;etc. Also, we plot the relative importances of the input variables (as measured by a sensitivity&#10;analysis procedure).&#10;&#10;The two datasets are related to red and white variants of the Portuguese &quot;Vinho Verde&quot; wine.&#10;For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].&#10;Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables&#10;are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).&#10;&#10;Number of Instances: red wine - 1599; white wine - 4898&#10;&#10;Input variables (based on physicochemical tests):&#10;&#10;1. fixed acidity&#10;2. volatile acidity&#10;3. citric acid&#10;4. residual sugar&#10;5. chlorides&#10;6. free sulfur dioxide&#10;7. total sulfur dioxide&#10;8. density&#10;9. pH&#10;10. sulphates&#10;11. alcohol&#10;&#10;Output variable (based on sensory data):&#10;&#10;12. quality (score between 0 and 10)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wine_quality&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wine_quality" />
  <meta itemprop="sameAs" content="https://archive.ics.uci.edu/ml/datasets/wine+quality" />
  <meta itemprop="citation" content="@ONLINE {cortezpaulo;cerdeiraantonio;almeidafernando;matostelmo;reisjose1999,&#10;    author = &quot;Cortez, Paulo; Cerdeira, Antonio; Almeida,Fernando;  Matos, Telmo;  Reis, Jose&quot;,&#10;    title  = &quot;Modeling wine preferences by data mining from physicochemical properties.&quot;,&#10;    year   = &quot;2009&quot;,&#10;    url    = &quot;https://archive.ics.uci.edu/ml/datasets/wine+quality&quot;&#10;}" />
</div>

# `wine_quality`

*   **Description**:

Two datasets were created, using red and white wine samples. The inputs include
objective tests (e.g. PH values) and the output is based on sensory data (median
of at least 3 evaluations made by wine experts). Each expert graded the wine
quality between 0 (very bad) and 10 (very excellent). Several data mining
methods were applied to model these datasets under a regression approach. The
support vector machine model achieved the best results. Several metrics were
computed: MAD, confusion matrix for a fixed error tolerance (T), etc. Also, we
plot the relative importances of the input variables (as measured by a
sensitivity analysis procedure).

The two datasets are related to red and white variants of the Portuguese "Vinho
Verde" wine. For more details, consult: http://www.vinhoverde.pt/en/ or the
reference [Cortez et al., 2009]. Due to privacy and logistic issues, only
physicochemical (inputs) and sensory (the output) variables are available (e.g.
there is no data about grape types, wine brand, wine selling price, etc.).

Number of Instances: red wine - 1599; white wine - 4898

Input variables (based on physicochemical tests):

1.  fixed acidity
2.  volatile acidity
3.  citric acid
4.  residual sugar
5.  chlorides
6.  free sulfur dioxide
7.  total sulfur dioxide
8.  density
9.  pH
10. sulphates
11. alcohol

Output variable (based on sensory data):

1.  quality (score between 0 and 10)

*   **Homepage**:
    [https://archive.ics.uci.edu/ml/datasets/wine+quality](https://archive.ics.uci.edu/ml/datasets/wine+quality)

*   **Source code**:
    [`tfds.structured.wine_quality.WineQuality`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/wine_quality/wine_quality.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'features': FeaturesDict({
        'alcohol': tf.float32,
        'chlorides': tf.float32,
        'citric acid': tf.float32,
        'density': tf.float32,
        'fixed acidity': tf.float32,
        'free sulfur dioxide': tf.float32,
        'pH': tf.float32,
        'residual sugar': tf.float32,
        'sulphates': tf.float64,
        'total sulfur dioxide': tf.float32,
        'volatile acidity': tf.float32,
    }),
    'quality': tf.int32,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'quality')`

*   **Citation**:

```
@ONLINE {cortezpaulo;cerdeiraantonio;almeidafernando;matostelmo;reisjose1999,
    author = "Cortez, Paulo; Cerdeira, Antonio; Almeida,Fernando;  Matos, Telmo;  Reis, Jose",
    title  = "Modeling wine preferences by data mining from physicochemical properties.",
    year   = "2009",
    url    = "https://archive.ics.uci.edu/ml/datasets/wine+quality"
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## wine_quality/white (default config)

*   **Config description**: White Wine

*   **Download size**: `258.23 KiB`

*   **Dataset size**: `1.87 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,898

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wine_quality-white-1.0.0.html";
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

## wine_quality/red

*   **Config description**: Red Wine

*   **Download size**: `82.23 KiB`

*   **Dataset size**: `626.17 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,599

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wine_quality-red-1.0.0.html";
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