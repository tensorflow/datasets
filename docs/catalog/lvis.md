<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lvis" />
  <meta itemprop="description" content="LVIS: A dataset for large vocabulary instance segmentation.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lvis&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/lvis-1.2.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lvis" />
  <meta itemprop="sameAs" content="https://www.lvisdataset.org/" />
  <meta itemprop="citation" content="@inproceedings{gupta2019lvis,&#10;  title={{LVIS}: A Dataset for Large Vocabulary Instance Segmentation},&#10;  author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},&#10;  booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},&#10;  year={2019}&#10;}" />
</div>

# `lvis`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=lvis">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

LVIS: A dataset for large vocabulary instance segmentation.

*   **Homepage**: [https://www.lvisdataset.org/](https://www.lvisdataset.org/)

*   **Source code**:
    [`tfds.object_detection.lvis.Lvis`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/object_detection/lvis/lvis.py)

*   **Versions**:

    *   `1.1.0`: Added fields `neg_category_ids` and
        `not_exhaustive_category_ids`.
    *   **`1.2.0`** (default): Added class names.

*   **Download size**: `25.35 GiB`

*   **Dataset size**: `22.29 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 19,822
`'train'`      | 100,170
`'validation'` | 19,809

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/id': tf.int64,
    'neg_category_ids': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=1203)),
    'not_exhaustive_category_ids': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=1203)),
    'objects': Sequence({
        'area': tf.int64,
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': tf.int64,
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1203),
        'segmentation': Image(shape=(None, None, 1), dtype=tf.uint8),
    }),
})
```

*   **Feature documentation**:

Feature                     | Class                | Shape           | Dtype      | Description
:-------------------------- | :------------------- | :-------------- | :--------- | :----------
                            | FeaturesDict         |                 |            |
image                       | Image                | (None, None, 3) | tf.uint8   |
image/id                    | Tensor               |                 | tf.int64   |
neg_category_ids            | Sequence(ClassLabel) | (None,)         | tf.int64   |
not_exhaustive_category_ids | Sequence(ClassLabel) | (None,)         | tf.int64   |
objects                     | Sequence             |                 |            |
objects/area                | Tensor               |                 | tf.int64   |
objects/bbox                | BBoxFeature          | (4,)            | tf.float32 |
objects/id                  | Tensor               |                 | tf.int64   |
objects/label               | ClassLabel           |                 | tf.int64   |
objects/segmentation        | Image                | (None, None, 1) | tf.uint8   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/lvis-1.2.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lvis-1.2.0.html";
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
@inproceedings{gupta2019lvis,
  title={{LVIS}: A Dataset for Large Vocabulary Instance Segmentation},
  author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},
  booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},
  year={2019}
}
```

