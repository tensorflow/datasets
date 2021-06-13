<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_a" />
  <meta itemprop="description" content="ImageNet-A is a set of images labelled with ImageNet labels that were obtained&#10;by collecting new data and keeping only those images that ResNet-50 models fail&#10;to correctly classify. For more details please refer to the paper.&#10;&#10;The label space is the same as that of ImageNet2012. Each example is&#10;represented as a dictionary with the following keys:&#10;&#10;* &#x27;image&#x27;: The image, a (H, W, 3)-tensor.&#10;* &#x27;label&#x27;: An integer in the range [0, 1000).&#10;* &#x27;file_name&#x27;: A unique sting identifying the example within the dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_a&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_a-0.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_a" />
  <meta itemprop="sameAs" content="https://github.com/hendrycks/natural-adv-examples" />
  <meta itemprop="citation" content="@article{hendrycks2019nae,&#10;  title={Natural Adversarial Examples},&#10;  author={Dan Hendrycks and Kevin Zhao and Steven Basart and Jacob Steinhardt and Dawn Song},&#10;  journal={arXiv preprint arXiv:1907.07174},&#10;  year={2019}&#10;}" />
</div>

# `imagenet_a`

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=imagenet_a">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

ImageNet-A is a set of images labelled with ImageNet labels that were obtained
by collecting new data and keeping only those images that ResNet-50 models fail
to correctly classify. For more details please refer to the paper.

The label space is the same as that of ImageNet2012. Each example is represented
as a dictionary with the following keys:

*   'image': The image, a (H, W, 3)-tensor.
*   'label': An integer in the range [0, 1000).
*   'file_name': A unique sting identifying the example within the dataset.

*   **Homepage**:
    [https://github.com/hendrycks/natural-adv-examples](https://github.com/hendrycks/natural-adv-examples)

*   **Source code**:
    [`tfds.image_classification.ImagenetA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet_a.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `655.70 MiB`

*   **Dataset size**: `650.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 7,500

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_a-0.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_a-0.1.0.html";
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
@article{hendrycks2019nae,
  title={Natural Adversarial Examples},
  author={Dan Hendrycks and Kevin Zhao and Steven Basart and Jacob Steinhardt and Dawn Song},
  journal={arXiv preprint arXiv:1907.07174},
  year={2019}
}
```
