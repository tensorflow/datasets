<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="uc_merced" />
  <meta itemprop="description" content="UC Merced is a 21 class land use remote sensing image dataset, with 100 images&#10;per class. The images were manually extracted from large images from the USGS&#10;National Map Urban Area Imagery collection for various urban areas around the&#10;country. The pixel resolution of this public domain imagery is 0.3 m.&#10;&#10;While most images are 256x256 pixels, there are 44 images with different shape.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;uc_merced&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/uc_merced-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/uc_merced" />
  <meta itemprop="sameAs" content="http://weegee.vision.ucmerced.edu/datasets/landuse.html" />
  <meta itemprop="citation" content="@InProceedings{Nilsback08,&#10;   author = &quot;Yang, Yi and Newsam, Shawn&quot;,&#10;   title = &quot;Bag-Of-Visual-Words and Spatial Extensions for Land-Use Classification&quot;,&#10;   booktitle = &quot;ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM GIS)&quot;,&#10;   year = &quot;2010&quot;,&#10;}" />
</div>

# `uc_merced`

*   **Description**:

UC Merced is a 21 class land use remote sensing image dataset, with 100 images
per class. The images were manually extracted from large images from the USGS
National Map Urban Area Imagery collection for various urban areas around the
country. The pixel resolution of this public domain imagery is 0.3 m.

While most images are 256x256 pixels, there are 44 images with different shape.

*   **Homepage**:
    [http://weegee.vision.ucmerced.edu/datasets/landuse.html](http://weegee.vision.ucmerced.edu/datasets/landuse.html)

*   **Source code**:
    [`tfds.image_classification.UcMerced`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/uc_merced.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `317.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,100

*   **Features**:

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=21),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@InProceedings{Nilsback08,
   author = "Yang, Yi and Newsam, Shawn",
   title = "Bag-Of-Visual-Words and Spatial Extensions for Land-Use Classification",
   booktitle = "ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM GIS)",
   year = "2010",
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/uc_merced-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/uc_merced-2.0.0.html";
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