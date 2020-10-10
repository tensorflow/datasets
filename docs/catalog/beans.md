<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="beans" />
  <meta itemprop="description" content="Beans is a dataset of images of beans taken in the field using smartphone&#10;cameras. It consists of 3 classes: 2 disease classes and the healthy class.&#10;Diseases depicted include Angular Leaf Spot and Bean Rust. Data was annotated&#10;by experts from the National Crops Resources Research Institute (NaCRRI) in&#10;Uganda and collected by the Makerere AI research lab.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;beans&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/beans-0.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/beans" />
  <meta itemprop="sameAs" content="https://github.com/AI-Lab-Makerere/ibean/" />
  <meta itemprop="citation" content="@ONLINE {beansdata,&#10;    author=&quot;Makerere AI Lab&quot;,&#10;    title=&quot;Bean disease dataset&quot;,&#10;    month=&quot;January&quot;,&#10;    year=&quot;2020&quot;,&#10;    url=&quot;https://github.com/AI-Lab-Makerere/ibean/&quot;&#10;}" />
</div>
# `beans`

*   **Description**:

Beans is a dataset of images of beans taken in the field using smartphone
cameras. It consists of 3 classes: 2 disease classes and the healthy class.
Diseases depicted include Angular Leaf Spot and Bean Rust. Data was annotated
by experts from the National Crops Resources Research Institute (NaCRRI) in
Uganda and collected by the Makerere AI research lab.

*   **Homepage**: [https://github.com/AI-Lab-Makerere/ibean/](https://github.com/AI-Lab-Makerere/ibean/)

*   **Source code**: [`tfds.image_classification.Beans`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/beans.py)

*   **Versions**:

    * **`0.1.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `171.63 MiB`

*   **Auto-cached** ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)): Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 128
`'train'` | 1,034
`'validation'` | 133

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(500, 500, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

*   **Supervised keys** (See [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)): `('image', 'label')`

*   **Citation**:

```
@ONLINE {beansdata,
    author="Makerere AI Lab",
    title="Bean disease dataset",
    month="January",
    year="2020",
    url="https://github.com/AI-Lab-Makerere/ibean/"
}
```

*   **Figure** ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/beans-0.1.0.png" alt="Visualization" width="500px">

*   **Examples** ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>

<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>

<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/beans-0.1.0.html";
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
