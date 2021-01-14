<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cherry_blossoms" />
  <meta itemprop="description" content="Historical phenological data for cherry tree flowering at Kyoto City.&#10;&#10;This data was collected from diaries and chronicles dating back to the 9th&#10;century. Data from the 9th to the 14th century were collected by Aono and Saito&#10;(2010;  International Journal of Biometeorology, 54, 211-219), while the 15th&#10;to 21st  century were collected by Aono and Kazui (2008; International Journal&#10;of  Climatology, 28, 905-914).&#10;&#10;All dates are expressed in the Gregorian calendar.&#10;&#10;&#10;Number of instances: 1216&#10;&#10;Variables:&#10;&#10;1. year: Year CE  (int)&#10;2. doy: Day of year of first bloom. Day 89 is April 1. Day 119 is May 1. (float)&#10;3. temp: March temperature estimate (float)&#10;4. temp_upper: Upper 95% bound for estimate (float)&#10;5. temp_lower: Lower 95% bound for estimate (float)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cherry_blossoms&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cherry_blossoms" />
  <meta itemprop="sameAs" content="http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/" />
  <meta itemprop="citation" content="@ONLINE {&#10;    author = &quot;Aono, Yasuyuki&quot;,&#10;    title  = &quot;Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions)&quot;,&#10;    year   = &quot;2012&quot;,&#10;    url    = &quot;http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/&quot;&#10;}" />
</div>

# `cherry_blossoms`

*   **Description**:

Historical phenological data for cherry tree flowering at Kyoto City.

This data was collected from diaries and chronicles dating back to the 9th
century. Data from the 9th to the 14th century were collected by Aono and Saito
(2010; International Journal of Biometeorology, 54, 211-219), while the 15th to
21st century were collected by Aono and Kazui (2008; International Journal of
Climatology, 28, 905-914).

All dates are expressed in the Gregorian calendar.

Number of instances: 1216

Variables:

1.  year: Year CE (int)
2.  doy: Day of year of first bloom. Day 89 is April 1. Day 119 is May 1.
    (float)
3.  temp: March temperature estimate (float)
4.  temp_upper: Upper 95% bound for estimate (float)
5.  temp_lower: Lower 95% bound for estimate (float)

*   **Homepage**:
    [http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/](http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/)

*   **Source code**:
    [`tfds.structured.cherry_blossoms.CherryBlossoms`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/cherry_blossoms/cherry_blossoms.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `26.90 KiB`

*   **Dataset size**: `119.84 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,215

*   **Features**:

```python
FeaturesDict({
    'doy': tf.float32,
    'temp': tf.float32,
    'temp_lower': tf.float32,
    'temp_upper': tf.float32,
    'year': tf.int32,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@ONLINE {
    author = "Aono, Yasuyuki",
    title  = "Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions)",
    year   = "2012",
    url    = "http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/"
}
```

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cherry_blossoms-1.0.0.html";
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