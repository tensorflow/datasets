<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="vgg_face2" />
  <meta itemprop="description" content="VGGFace2 is a large-scale face recognition dataset. Images are downloaded from Google Image Search and have large variations in pose, age, illumination, ethnicity and profession. VGGFace2 contains images from identities spanning a wide range of different ethnicities, accents, professions and ages. All face images are captured &quot;in the wild&quot;, with pose and emotion variations and different lighting and occlusion conditions. Face distribution for different identities is varied, from 87 to 843, with an average of 362 images for each subject.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;vgg_face2&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/vgg_face2-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/vgg_face2" />
  <meta itemprop="sameAs" content="http://zeus.robots.ox.ac.uk/vgg_face2/" />
  <meta itemprop="citation" content="@InProceedings{Cao18,&#10;author = &quot;Cao, Q. and Shen, L. and Xie, W. and Parkhi, O. M. and Zisserman, A.&quot;,&#10;title  = &quot;VGGFace2: A dataset for recognising faces across pose and age&quot;,&#10;booktitle = &quot;International Conference on Automatic Face and Gesture Recognition&quot;,&#10;year  = &quot;2018&quot;}" />
</div>

# `vgg_face2`

Warning: Manual download required. See instructions below.

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=vgg_face2">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

VGGFace2 is a large-scale face recognition dataset. Images are downloaded from
Google Image Search and have large variations in pose, age, illumination,
ethnicity and profession. VGGFace2 contains images from identities spanning a
wide range of different ethnicities, accents, professions and ages. All face
images are captured "in the wild", with pose and emotion variations and
different lighting and occlusion conditions. Face distribution for different
identities is varied, from 87 to 843, with an average of 362 images for each
subject.

*   **Homepage**:
    [http://zeus.robots.ox.ac.uk/vgg_face2/](http://zeus.robots.ox.ac.uk/vgg_face2/)

*   **Source code**:
    [`tfds.image_classification.VggFace2`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/vgg_face2.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: vggface2_test.tar.gz and
    vggface2_train.tar.gz.
    You need to register on http://zeus.robots.ox.ac.uk/vgg_face2/signup/ in
    order to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 169,396
`'train'` | 3,141,890

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=9131),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/vgg_face2-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/vgg_face2-1.0.0.html";
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
@InProceedings{Cao18,
author = "Cao, Q. and Shen, L. and Xie, W. and Parkhi, O. M. and Zisserman, A.",
title  = "VGGFace2: A dataset for recognising faces across pose and age",
booktitle = "International Conference on Automatic Face and Gesture Recognition",
year  = "2018"}
```
