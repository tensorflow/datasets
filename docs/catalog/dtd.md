<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dtd" />
  <meta itemprop="description" content="The Describable Textures Dataset (DTD) is an evolving collection of textural&#10;images in the wild, annotated with a series of human-centric attributes,&#10;inspired by the perceptual properties of textures. This data is made available&#10;to the computer vision community for research purposes.&#10;&#10;The &quot;label&quot; of each example is its &quot;key attribute&quot; (see the official website).&#10;The official release of the dataset defines a 10-fold cross-validation&#10;partition. Our TRAIN/TEST/VALIDATION splits are those of the first fold.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dtd&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/dtd-3.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dtd" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html" />
  <meta itemprop="citation" content="@InProceedings{cimpoi14describing,&#10;Author    = {M. Cimpoi and S. Maji and I. Kokkinos and S. Mohamed and A. Vedaldi},&#10;Title     = {Describing Textures in the Wild},&#10;Booktitle = {Proceedings of the {IEEE} Conf. on Computer Vision and Pattern Recognition ({CVPR})},&#10;Year      = {2014}}" />
</div>

# `dtd`


*   **Description**:

The Describable Textures Dataset (DTD) is an evolving collection of textural
images in the wild, annotated with a series of human-centric attributes,
inspired by the perceptual properties of textures. This data is made available
to the computer vision community for research purposes.

The "label" of each example is its "key attribute" (see the official website).
The official release of the dataset defines a 10-fold cross-validation
partition. Our TRAIN/TEST/VALIDATION splits are those of the first fold.

*   **Homepage**:
    [https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html](https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html)

*   **Source code**:
    [`tfds.image_classification.Dtd`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/dtd.py)

*   **Versions**:

    *   **`3.0.1`** (default): No release notes.

*   **Download size**: `596.28 MiB`

*   **Dataset size**: `603.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,880
`'train'`      | 1,880
`'validation'` | 1,880

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=47),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/dtd-3.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dtd-3.0.1.html";
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
@InProceedings{cimpoi14describing,
Author    = {M. Cimpoi and S. Maji and I. Kokkinos and S. Mohamed and A. Vedaldi},
Title     = {Describing Textures in the Wild},
Booktitle = {Proceedings of the {IEEE} Conf. on Computer Vision and Pattern Recognition ({CVPR})},
Year      = {2014}}
```
