<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="clic" />
  <meta itemprop="description" content="CLIC is a dataset for the Challenge on Learned Image Compression 2020 lossy&#10;image compression track. These images contain a mix of the professional and&#10;mobile datasets used to train and benchmark rate-distortion performance. The&#10;dataset contains both RGB and grayscale images. This may require special&#10;handling if a grayscale image is processed as a 1 channel Tensor and a 3 channel&#10;Tensor is expected.&#10;&#10;This dataset does *NOT* contain the data from the P-Frame challenge (YUV image&#10;frames).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;clic&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/clic-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/clic" />
  <meta itemprop="sameAs" content="https://www.compression.cc/" />
  <meta itemprop="citation" content="@misc{CLIC2020,&#10;  title = {Workshop and Challenge on Learned Image Compression (CLIC2020)},&#10;  author = {George Toderici, Wenzhe Shi, Radu Timofte, Lucas Theis,&#10;            Johannes Balle, Eirikur Agustsson, Nick Johnston, Fabian Mentzer},&#10;  url = {http://www.compression.cc},&#10;  year={2020},&#10;  organization={CVPR}&#10;}" />
</div>

# `clic`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=clic">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

CLIC is a dataset for the Challenge on Learned Image Compression 2020 lossy
image compression track. These images contain a mix of the professional and
mobile datasets used to train and benchmark rate-distortion performance. The
dataset contains both RGB and grayscale images. This may require special
handling if a grayscale image is processed as a 1 channel Tensor and a 3 channel
Tensor is expected.

This dataset does *NOT* contain the data from the P-Frame challenge (YUV image
frames).

*   **Homepage**: [https://www.compression.cc/](https://www.compression.cc/)

*   **Source code**:
    [`tfds.image.CLIC`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/clic.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `7.48 GiB`

*   **Dataset size**: `7.48 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 428
`'train'`      | 1,633
`'validation'` | 102

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/clic-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/clic-1.0.0.html";
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
@misc{CLIC2020,
  title = {Workshop and Challenge on Learned Image Compression (CLIC2020)},
  author = {George Toderici, Wenzhe Shi, Radu Timofte, Lucas Theis,
            Johannes Balle, Eirikur Agustsson, Nick Johnston, Fabian Mentzer},
  url = {http://www.compression.cc},
  year={2020},
  organization={CVPR}
}
```
