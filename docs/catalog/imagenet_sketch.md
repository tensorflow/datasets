<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_sketch" />
  <meta itemprop="description" content="ImageNet-Sketch consists of 50,889 black and white sketch images, 50 for each of&#10;the 1000 ImageNet classes. These images were originally collected from Google&#10;Image Search for &quot;sketch of __&quot;. 100 images were collected and then manually&#10;filtered. For classes with fewer than 50 good images, additional images were&#10;constructed by flip or rotation.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_sketch&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_sketch-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_sketch" />
  <meta itemprop="sameAs" content="https://github.com/HaohanWang/ImageNet-Sketch" />
  <meta itemprop="citation" content="@inproceedings{wang2019learning,&#10;        title={Learning Robust Global Representations by Penalizing Local Predictive Power},&#10;        author={Wang, Haohan and Ge, Songwei and Lipton, Zachary and Xing, Eric P},&#10;        booktitle={Advances in Neural Information Processing Systems},&#10;        pages={10506--10518},&#10;        year={2019}&#10;}" />
</div>

# `imagenet_sketch`


*   **Description**:

ImageNet-Sketch consists of 50,889 black and white sketch images, 50 for each of
the 1000 ImageNet classes. These images were originally collected from Google
Image Search for "sketch of __". 100 images were collected and then manually
filtered. For classes with fewer than 50 good images, additional images were
constructed by flip or rotation.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/imagenet-sketch">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/HaohanWang/ImageNet-Sketch](https://github.com/HaohanWang/ImageNet-Sketch)

*   **Source code**:
    [`tfds.datasets.imagenet_sketch.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagenet_sketch/imagenet_sketch_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `7.07 GiB`

*   **Dataset size**: `7.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 50,889

*   **Feature structure**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape           | Dtype  | Description
:-------- | :----------- | :-------------- | :----- | :----------
          | FeaturesDict |                 |        |
file_name | Text         |                 | string |
image     | Image        | (None, None, 3) | uint8  |
label     | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_sketch-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_sketch-1.0.0.html";
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
@inproceedings{wang2019learning,
        title={Learning Robust Global Representations by Penalizing Local Predictive Power},
        author={Wang, Haohan and Ge, Songwei and Lipton, Zachary and Xing, Eric P},
        booktitle={Advances in Neural Information Processing Systems},
        pages={10506--10518},
        year={2019}
}
```

