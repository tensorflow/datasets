<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech_birds2011" />
  <meta itemprop="description" content="Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos &#10;of 200 bird species (mostly North American). The total number of &#10;categories of birds is 200 and there are 6033 images in the 2010 &#10;dataset and 11,788 images in the 2011 dataset.&#10;Annotations include bounding boxes, segmentation labels.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;caltech_birds2011&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech_birds2011" />
  <meta itemprop="sameAs" content="http://www.vision.caltech.edu/visipedia/CUB-200.html" />
  <meta itemprop="citation" content="@techreport{WelinderEtal2010,&#10;Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},&#10;Institution = {California Institute of Technology},&#10;Number = {CNS-TR-2010-001},&#10;Title = {{Caltech-UCSD Birds 200}},&#10;Year = {2010}&#10;}" />
</div>
# `caltech_birds2011`

*   **Description**:

Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos
of 200 bird species (mostly North American). The total number of
categories of birds is 200 and there are 6033 images in the 2010
dataset and 11,788 images in the 2011 dataset.
Annotations include bounding boxes, segmentation labels.

*   **Homepage**: [http://www.vision.caltech.edu/visipedia/CUB-200.html](http://www.vision.caltech.edu/visipedia/CUB-200.html)

*   **Source code**: [`tfds.image_classification.CaltechBirds2011`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/caltech_birds.py)

*   **Versions**:

    * **`0.1.1`** (default): No release notes.

*   **Download size**: `1.11 GiB`

*   **Dataset size**: `1.11 GiB`

*   **Auto-cached** ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)): No

*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5,794
`'train'` | 5,994

*   **Features**:

```python
FeaturesDict({
    'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=200),
    'label_name': Text(shape=(), dtype=tf.string),
    'segmentation_mask': Image(shape=(None, None, 1), dtype=tf.uint8),
})
```

*   **Supervised keys** (See [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)): `('image', 'label')`

*   **Citation**:

```
@techreport{WelinderEtal2010,
Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},
Institution = {California Institute of Technology},
Number = {CNS-TR-2010-001},
Title = {{Caltech-UCSD Birds 200}},
Year = {2010}
}
```

*   **Figure** ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)): Not supported.

*   **Examples** ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>

<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>

<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/caltech_birds2011-0.1.1.html";
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
