<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="smallnorb" />
  <meta itemprop="description" content="This database is intended for experiments in 3D object recognition from shape.&#10;It contains images of 50 toys belonging to 5 generic categories: four-legged&#10;animals, human figures, airplanes, trucks, and cars. The objects were imaged by&#10;two cameras under 6 lighting conditions, 9 elevations (30 to 70 degrees every 5&#10;degrees), and 18 azimuths (0 to 340 every 20 degrees).&#10;&#10;The training set is composed of 5 instances of each category (instances 4, 6, 7,&#10;8 and 9), and the test set of the remaining 5 instances (instances 0, 1, 2, 3,&#10;and 5).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;smallnorb&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/smallnorb" />
  <meta itemprop="sameAs" content="https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/" />
  <meta itemprop="citation" content="@article{LeCun2004LearningMF,&#10;  title={Learning methods for generic object recognition with invariance to pose and lighting},&#10;  author={Yann LeCun and Fu Jie Huang and L{\&#x27;e}on Bottou},&#10;  journal={Proceedings of the 2004 IEEE Computer Society Conference on Computer Vision and Pattern Recognition},&#10;  year={2004},&#10;  volume={2},&#10;  pages={II-104 Vol.2}&#10;}" />
</div>

# `smallnorb`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=smallnorb">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

This database is intended for experiments in 3D object recognition from shape.
It contains images of 50 toys belonging to 5 generic categories: four-legged
animals, human figures, airplanes, trucks, and cars. The objects were imaged by
two cameras under 6 lighting conditions, 9 elevations (30 to 70 degrees every 5
degrees), and 18 azimuths (0 to 340 every 20 degrees).

The training set is composed of 5 instances of each category (instances 4, 6, 7,
8 and 9), and the test set of the remaining 5 instances (instances 0, 1, 2, 3,
and 5).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/smallnorb">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/](https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/)

*   **Source code**:
    [`tfds.datasets.smallnorb.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/smallnorb/smallnorb_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)
    *   `2.1.0`: No release notes.

*   **Download size**: `250.60 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 24,300
`'train'` | 24,300

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(96, 96, 1), dtype=uint8),
    'image2': Image(shape=(96, 96, 1), dtype=uint8),
    'instance': ClassLabel(shape=(), dtype=int64, num_classes=10),
    'label_azimuth': ClassLabel(shape=(), dtype=int64, num_classes=18),
    'label_category': ClassLabel(shape=(), dtype=int64, num_classes=5),
    'label_elevation': ClassLabel(shape=(), dtype=int64, num_classes=9),
    'label_lighting': ClassLabel(shape=(), dtype=int64, num_classes=6),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape       | Dtype | Description
:-------------- | :----------- | :---------- | :---- | :----------
                | FeaturesDict |             |       |
image           | Image        | (96, 96, 1) | uint8 |
image2          | Image        | (96, 96, 1) | uint8 |
instance        | ClassLabel   |             | int64 |
label_azimuth   | ClassLabel   |             | int64 |
label_category  | ClassLabel   |             | int64 |
label_elevation | ClassLabel   |             | int64 |
label_lighting  | ClassLabel   |             | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label_category')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/smallnorb-2.0.0.html";
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
@article{LeCun2004LearningMF,
  title={Learning methods for generic object recognition with invariance to pose and lighting},
  author={Yann LeCun and Fu Jie Huang and L{\'e}on Bottou},
  journal={Proceedings of the 2004 IEEE Computer Society Conference on Computer Vision and Pattern Recognition},
  year={2004},
  volume={2},
  pages={II-104 Vol.2}
}
```

