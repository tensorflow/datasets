<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="open_images_challenge2019_detection" />
  <meta itemprop="description" content="Open Images is a collaborative release of ~9 million images annotated with&#10;image-level labels, object bounding boxes, object segmentation masks, and visual&#10;relationships. This uniquely large and diverse dataset is designed to spur state&#10;of the art advances in analyzing and understanding images.&#10;&#10;This contains the data from thee Object Detection track of the competition. The&#10;goal in this track is to predict a tight bounding box around all object&#10;instances of 500 classes.&#10;&#10;The images are annotated with positive image-level labels, indicating certain&#10;object classes are present, and with negative image-level labels, indicating&#10;certain classes are absent. In the competition, all other unannotated classes&#10;are excluded from evaluation in that image. For each positive image-level label&#10;in an image, every instance of that object class in the image was annotated.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;open_images_challenge2019_detection&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/open_images_challenge2019_detection-200k-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/open_images_challenge2019_detection" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/openimages/web/challenge2019.html" />
  <meta itemprop="citation" content="" />
</div>

# `open_images_challenge2019_detection`


*   **Description**:

Open Images is a collaborative release of ~9 million images annotated with
image-level labels, object bounding boxes, object segmentation masks, and visual
relationships. This uniquely large and diverse dataset is designed to spur state
of the art advances in analyzing and understanding images.

This contains the data from thee Object Detection track of the competition. The
goal in this track is to predict a tight bounding box around all object
instances of 500 classes.

The images are annotated with positive image-level labels, indicating certain
object classes are present, and with negative image-level labels, indicating
certain classes are absent. In the competition, all other unannotated classes
are excluded from evaluation in that image. For each positive image-level label
in an image, every instance of that object class in the image was annotated.

*   **Homepage**:
    [https://storage.googleapis.com/openimages/web/challenge2019.html](https://storage.googleapis.com/openimages/web/challenge2019.html)

*   **Source code**:
    [`tfds.datasets.open_images_challenge2019_detection.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/open_images_challenge2019_detection/open_images_challenge2019_detection_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `534.63 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 99,999
`'train'`      | 1,743,042
`'validation'` | 41,620

*   **Feature structure**:

```python
FeaturesDict({
    'bobjects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=float32),
        'is_group_of': bool,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=500),
    }),
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'objects': Sequence({
        'confidence': float32,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=500),
        'source': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature              | Class        | Shape           | Dtype   | Description
:------------------- | :----------- | :-------------- | :------ | :----------
                     | FeaturesDict |                 |         |
bobjects             | Sequence     |                 |         |
bobjects/bbox        | BBoxFeature  | (4,)            | float32 |
bobjects/is_group_of | Tensor       |                 | bool    |
bobjects/label       | ClassLabel   |                 | int64   |
id                   | Text         |                 | string  |
image                | Image        | (None, None, 3) | uint8   |
objects              | Sequence     |                 |         |
objects/confidence   | Tensor       |                 | float32 |
objects/label        | ClassLabel   |                 | int64   |
objects/source       | Text         |                 | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:


## open_images_challenge2019_detection/200k (default config)

*   **Config description**: Images have at most 200,000 pixels, at 72 JPEG
    quality.

*   **Dataset size**: `59.06 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/open_images_challenge2019_detection-200k-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/open_images_challenge2019_detection-200k-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## open_images_challenge2019_detection/300k

*   **Config description**: Images have at most 300,000 pixels, at 72 JPEG
    quality.

*   **Dataset size**: `80.10 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/open_images_challenge2019_detection-300k-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/open_images_challenge2019_detection-300k-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->