<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="coil100" />
  <meta itemprop="description" content="The dataset contains 7200 color images of 100 objects (72 images per object).&#10;The objects have a wide variety of complex geometric and reflectance&#10;characteristics. The objects were placed on a motorized turntable against a&#10;black background. The turntable was rotated through 360 degrees to vary object&#10;pose with respect to a fxed color camera. Images of the objects were taken at&#10;pose intervals of 5 degrees.This corresponds to 72 poses per object&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;coil100&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/coil100-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/coil100" />
  <meta itemprop="sameAs" content="http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php" />
  <meta itemprop="citation" content="@article{nene1996columbia,&#10;  title={Columbia object image library (coil-20)},&#10;  author={Nene, Sameer A and Nayar, Shree K and Murase, Hiroshi and others},&#10;  year={1996},&#10;  publisher={Technical report CUCS-005-96}&#10;}" />
</div>

# `coil100`


*   **Description**:

The dataset contains 7200 color images of 100 objects (72 images per object).
The objects have a wide variety of complex geometric and reflectance
characteristics. The objects were placed on a motorized turntable against a
black background. The turntable was rotated through 360 degrees to vary object
pose with respect to a fxed color camera. Images of the objects were taken at
pose intervals of 5 degrees.This corresponds to 72 poses per object

*   **Homepage**:
    [http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php](http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php)

*   **Source code**:
    [`tfds.datasets.coil100.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/coil100/coil100_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release
    *   **`2.0.0`** (default): Change features (`object_id` is now `ClassLabel`,
        rename `label` -> `angle_label`, add `angle`)

*   **Download size**: `124.63 MiB`

*   **Dataset size**: `124.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,200

*   **Feature structure**:

```python
FeaturesDict({
    'angle': int64,
    'angle_label': ClassLabel(shape=(), dtype=int64, num_classes=72),
    'image': Image(shape=(128, 128, 3), dtype=uint8),
    'object_id': ClassLabel(shape=(), dtype=int64, num_classes=100),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape         | Dtype | Description
:---------- | :----------- | :------------ | :---- | :----------
            | FeaturesDict |               |       |
angle       | Tensor       |               | int64 |
angle_label | ClassLabel   |               | int64 |
image       | Image        | (128, 128, 3) | uint8 |
object_id   | ClassLabel   |               | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'angle_label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/coil100-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/coil100-2.0.0.html";
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
@article{nene1996columbia,
  title={Columbia object image library (coil-20)},
  author={Nene, Sameer A and Nayar, Shree K and Murase, Hiroshi and others},
  year={1996},
  publisher={Technical report CUCS-005-96}
}
```

