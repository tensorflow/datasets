<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="howell" />
  <meta itemprop="description" content="Demographic data from Kalahari !Kung San people collected by Nancy Howell&#10;&#10;Howell’s observations of the !Kung San were made by Howell in Botswana between&#10;August 1967 and May 1969. Fuller descriptions of the region and the people&#10;under study can be found in R. B. Lee and I. DeVore (eds), 1976, Kalahari&#10;Hunter-Gatherers: Studies of the !Kung San and Their Neighbors, Harvard&#10;University Press, Cambridge, Mass. And in N. Howell, 2000, Demography of the&#10;Dobe !Kung, Aldine de Gruyter, New York.&#10;&#10;Only columns on height, weight, age, and sex were kept. Rows with any&#10;null values were dropped.&#10;&#10;Number of instances: 544&#10;&#10;Variables:&#10;&#10;1. height in cm   (float)&#10;2. weight in kg   (float)&#10;3. age in years   (int)&#10;4. male indicator (int)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;howell&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/howell" />
  <meta itemprop="sameAs" content="https://tspace.library.utoronto.ca/handle/1807/10395" />
  <meta itemprop="citation" content="@ONLINE {&#10;    author = &quot;Howell, Nancy&quot;,&#10;    title  = &quot;Dobe !Kung Census of All Population.&quot;,&#10;    year   = &quot;2009&quot;,&#10;    url    = &quot;https://tspace.library.utoronto.ca/handle/1807/17973&quot;&#10;}" />
</div>

# `howell`


*   **Description**:

Demographic data from Kalahari !Kung San people collected by Nancy Howell

Howell’s observations of the !Kung San were made by Howell in Botswana between
August 1967 and May 1969. Fuller descriptions of the region and the people under
study can be found in R. B. Lee and I. DeVore (eds), 1976, Kalahari
Hunter-Gatherers: Studies of the !Kung San and Their Neighbors, Harvard
University Press, Cambridge, Mass. And in N. Howell, 2000, Demography of the
Dobe !Kung, Aldine de Gruyter, New York.

Only columns on height, weight, age, and sex were kept. Rows with any null
values were dropped.

Number of instances: 544

Variables:

1.  height in cm (float)
2.  weight in kg (float)
3.  age in years (int)
4.  male indicator (int)

*   **Homepage**:
    [https://tspace.library.utoronto.ca/handle/1807/10395](https://tspace.library.utoronto.ca/handle/1807/10395)

*   **Source code**:
    [`tfds.structured.howell.Howell`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/howell/howell.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `11.92 KiB`

*   **Dataset size**: `39.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 544

*   **Features**:

```python
FeaturesDict({
    'age': tf.float32,
    'height': tf.float32,
    'male': tf.int32,
    'weight': tf.float32,
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
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/howell-1.0.0.html";
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
@ONLINE {
    author = "Howell, Nancy",
    title  = "Dobe !Kung Census of All Population.",
    year   = "2009",
    url    = "https://tspace.library.utoronto.ca/handle/1807/17973"
}
```
