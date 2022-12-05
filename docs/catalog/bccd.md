<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bccd" />
  <meta itemprop="description" content="BCCD Dataset is a small-scale dataset for blood cells detection.&#10;&#10;Thanks the original data and annotations from cosmicad and akshaylamba. The&#10;original dataset is re-organized into VOC format. BCCD Dataset is under MIT&#10;licence.&#10;&#10;Data preparation is important to use machine learning. In this project, the&#10;Faster R-CNN algorithm from keras-frcnn for Object Detection is used. From this&#10;dataset, nicolaschen1 developed two Python scripts to make preparation data (CSV&#10;file and images) for recognition of abnormalities in blood cells on medical&#10;images.&#10;&#10;export.py: it creates the file &quot;test.csv&quot; with all data needed: filename,&#10;class_name, x1,y1,x2,y2. plot.py: it plots the boxes for each image and save it&#10;in a new directory.&#10;&#10;Image Type : jpeg(JPEG) Width x Height : 640 x 480&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bccd&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/bccd-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bccd" />
  <meta itemprop="sameAs" content="https://github.com/Shenggan/BCCD_Dataset" />
  <meta itemprop="citation" content="@ONLINE {BCCD_Dataset,&#10;    author = &quot;Shenggan&quot;,&#10;    title  = &quot;BCCD Dataset&quot;,&#10;    year   = &quot;2017&quot;,&#10;    url    = &quot;https://github.com/Shenggan/BCCD_Dataset&quot;&#10;}" />
</div>

# `bccd`


*   **Description**:

BCCD Dataset is a small-scale dataset for blood cells detection.

Thanks the original data and annotations from cosmicad and akshaylamba. The
original dataset is re-organized into VOC format. BCCD Dataset is under MIT
licence.

Data preparation is important to use machine learning. In this project, the
Faster R-CNN algorithm from keras-frcnn for Object Detection is used. From this
dataset, nicolaschen1 developed two Python scripts to make preparation data (CSV
file and images) for recognition of abnormalities in blood cells on medical
images.

export.py: it creates the file "test.csv" with all data needed: filename,
class_name, x1,y1,x2,y2. plot.py: it plots the boxes for each image and save it
in a new directory.

Image Type : jpeg(JPEG) Width x Height : 640 x 480

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/bccd">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/Shenggan/BCCD_Dataset](https://github.com/Shenggan/BCCD_Dataset)

*   **Source code**:
    [`tfds.datasets.bccd.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/bccd/bccd_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `7.51 MiB`

*   **Dataset size**: `7.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 72
`'train'`      | 205
`'validation'` | 87

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(480, 640, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=float32),
        'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    }),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape         | Dtype   | Description
:------------- | :----------- | :------------ | :------ | :----------
               | FeaturesDict |               |         |
image          | Image        | (480, 640, 3) | uint8   |
image/filename | Text         |               | string  |
objects        | Sequence     |               |         |
objects/bbox   | BBoxFeature  | (4,)          | float32 |
objects/label  | ClassLabel   |               | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/bccd-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bccd-1.0.0.html";
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

*   **Citation**:

```
@ONLINE {BCCD_Dataset,
    author = "Shenggan",
    title  = "BCCD Dataset",
    year   = "2017",
    url    = "https://github.com/Shenggan/BCCD_Dataset"
}
```

