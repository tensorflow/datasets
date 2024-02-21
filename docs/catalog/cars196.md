<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cars196" />
  <meta itemprop="description" content="The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cars196&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/cars196-2.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cars196" />
  <meta itemprop="sameAs" content="https://ai.stanford.edu/~jkrause/cars/car_dataset.html" />
  <meta itemprop="citation" content="@inproceedings{KrauseStarkDengFei-Fei_3DRR2013,&#10;title = {3D Object Representations for Fine-Grained Categorization},&#10;booktitle = {4th International IEEE Workshop on  3D Representation and Recognition (3dRR-13)},&#10;year = {2013},&#10;address = {Sydney, Australia},&#10;author = {Jonathan Krause and Michael Stark and Jia Deng and Li Fei-Fei}&#10;}" />
</div>

# `cars196`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=cars196">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The Cars dataset contains 16,185 images of 196 classes of cars. The data is
split into 8,144 training images and 8,041 testing images, where each class has
been split roughly in a 50-50 split. Classes are typically at the level of Make,
Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/stanford-cars">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://ai.stanford.edu/~jkrause/cars/car_dataset.html](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)

*   **Source code**:
    [`tfds.image_classification.Cars196`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cars196.py)

*   **Versions**:

    *   `2.0.0`: Initial release
    *   `2.0.1`: Website URL update
    *   **`2.1.0`** (default): Fixing bug
        https://github.com/tensorflow/datasets/issues/3927

*   **Download size**: `1.82 GiB`

*   **Dataset size**: `1.85 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 8,041
`'train'` | 8,144

*   **Feature structure**:

```python
FeaturesDict({
    'bbox': BBoxFeature(shape=(4,), dtype=float32),
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=196),
})
```

*   **Feature documentation**:

Feature | Class        | Shape           | Dtype   | Description
:------ | :----------- | :-------------- | :------ | :----------
        | FeaturesDict |                 |         |
bbox    | BBoxFeature  | (4,)            | float32 |
id      | Text         |                 | string  |
image   | Image        | (None, None, 3) | uint8   |
label   | ClassLabel   |                 | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cars196-2.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cars196-2.1.0.html";
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
@inproceedings{KrauseStarkDengFei-Fei_3DRR2013,
title = {3D Object Representations for Fine-Grained Categorization},
booktitle = {4th International IEEE Workshop on  3D Representation and Recognition (3dRR-13)},
year = {2013},
address = {Sydney, Australia},
author = {Jonathan Krause and Michael Stark and Jia Deng and Li Fei-Fei}
}
```

