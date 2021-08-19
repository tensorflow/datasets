<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gref" />
  <meta itemprop="description" content="The Google RefExp dataset is a collection of text descriptions of objects in&#10;images which builds on the publicly available MS-COCO dataset. Whereas the&#10;image captions in MS-COCO apply to the entire image, this dataset focuses on&#10;text descriptions that allow one to uniquely identify a single object or region&#10;within an image. See more details in this paper: Generation and Comprehension&#10;of Unambiguous Object Descriptions.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gref&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/gref-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gref" />
  <meta itemprop="sameAs" content="https://github.com/mjhucla/Google_Refexp_toolbox" />
  <meta itemprop="citation" content="@inproceedings{mao2016generation,&#10;  title={Generation and Comprehension of Unambiguous Object Descriptions},&#10;  author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},&#10;  booktitle={CVPR},&#10;  year={2016}&#10;}" />
</div>

# `gref`


Warning: Manual download required. See instructions below.

*   **Description**:

The Google RefExp dataset is a collection of text descriptions of objects in
images which builds on the publicly available MS-COCO dataset. Whereas the image
captions in MS-COCO apply to the entire image, this dataset focuses on text
descriptions that allow one to uniquely identify a single object or region
within an image. See more details in this paper: Generation and Comprehension of
Unambiguous Object Descriptions.

*   **Homepage**:
    [https://github.com/mjhucla/Google_Refexp_toolbox](https://github.com/mjhucla/Google_Refexp_toolbox)

*   **Source code**:
    [`tfds.vision_language.gref.Gref`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/gref/gref.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `4.60 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Follow instructions at https://github.com/mjhucla/Google_Refexp_toolbox
    to download and pre-process the data into aligned format with COCO.
    The directory contains 2 files and one folder:

*   google_refexp_train_201511_coco_aligned_catg.json

*   google_refexp_val_201511_coco_aligned_catg.json

*   coco_train2014/

The coco_train2014 folder contains all of COCO 2014 training images.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 24,698
`'validation'` | 4,650

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/id': tf.int64,
    'objects': Sequence({
        'area': tf.int64,
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': tf.int64,
        'label': tf.int64,
        'label_name': ClassLabel(shape=(), dtype=tf.int64, num_classes=80),
        'refexp': Sequence({
            'raw': Text(shape=(), dtype=tf.string),
            'referent': Text(shape=(), dtype=tf.string),
            'refexp_id': tf.int64,
            'tokens': Sequence(Text(shape=(), dtype=tf.string)),
        }),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/gref-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gref-1.0.0.html";
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
@inproceedings{mao2016generation,
  title={Generation and Comprehension of Unambiguous Object Descriptions},
  author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},
  booktitle={CVPR},
  year={2016}
}
```
