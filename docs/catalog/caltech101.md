<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech101" />
  <meta itemprop="description" content="Caltech-101 consists of pictures of objects belonging to 101 classes, plus one&#10;`background clutter` class. Each image is labelled with a single object. Each&#10;class contains roughly 40 to 800 images, totalling around 9k images. Images are&#10;of variable sizes, with typical edge lengths of 200-300 pixels. This version&#10;contains image-level labels only. The original dataset also contains bounding&#10;boxes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;caltech101&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/caltech101-3.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech101" />
  <meta itemprop="sameAs" content="http://www.vision.caltech.edu/Image_Datasets/Caltech101/" />
  <meta itemprop="citation" content="@article{FeiFei2004LearningGV,&#10;  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},&#10;  author={Li Fei-Fei and Rob Fergus and Pietro Perona},&#10;  journal={Computer Vision and Pattern Recognition Workshop},&#10;  year={2004},&#10;}" />
</div>

# `caltech101`


*   **Description**:

Caltech-101 consists of pictures of objects belonging to 101 classes, plus one
`background clutter` class. Each image is labelled with a single object. Each
class contains roughly 40 to 800 images, totalling around 9k images. Images are
of variable sizes, with typical edge lengths of 200-300 pixels. This version
contains image-level labels only. The original dataset also contains bounding
boxes.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/caltech-101">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.vision.caltech.edu/Image_Datasets/Caltech101/](http://www.vision.caltech.edu/Image_Datasets/Caltech101/)

*   **Source code**:
    [`tfds.datasets.caltech101.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/caltech101/caltech101_dataset_builder.py)

*   **Versions**:

    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   **`3.0.1`** (default): Website URL update

*   **Download size**: `125.64 MiB`

*   **Dataset size**: `132.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,084
`'train'` | 3,060

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/file_name': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=102),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape           | Dtype  | Description
:-------------- | :----------- | :-------------- | :----- | :----------
                | FeaturesDict |                 |        |
image           | Image        | (None, None, 3) | uint8  |
image/file_name | Text         |                 | string |
label           | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/caltech101-3.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/caltech101-3.0.1.html";
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
@article{FeiFei2004LearningGV,
  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},
  author={Li Fei-Fei and Rob Fergus and Pietro Perona},
  journal={Computer Vision and Pattern Recognition Workshop},
  year={2004},
}
```

