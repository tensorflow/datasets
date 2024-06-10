<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="pet_finder" />
  <meta itemprop="description" content="Dataset with images from 5 classes (see config name for information on the&#10;specific class)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;pet_finder&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/pet_finder-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/pet_finder" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/petfinder-adoption-prediction/data" />
  <meta itemprop="citation" content="@ONLINE {kaggle-petfinder-adoption-prediction,&#10;    author = &quot;Kaggle and PetFinder.my&quot;,&#10;    title  = &quot;PetFinder.my Adoption Prediction&quot;,&#10;    month  = &quot;april&quot;,&#10;    year   = &quot;2019&quot;,&#10;    url    = &quot;https://www.kaggle.com/c/petfinder-adoption-prediction/data/&quot;&#10;}" />
</div>

# `pet_finder`


*   **Description**:

Dataset with images from 5 classes (see config name for information on the
specific class)

*   **Homepage**:
    [https://www.kaggle.com/c/petfinder-adoption-prediction/data](https://www.kaggle.com/c/petfinder-adoption-prediction/data)

*   **Source code**:
    [`tfds.datasets.pet_finder.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/pet_finder/pet_finder_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.94 GiB`

*   **Dataset size**: `1.90 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 14,465
`'train'` | 58,311

*   **Feature structure**:

```python
FeaturesDict({
    'PetID': Text(shape=(), dtype=string),
    'attributes': FeaturesDict({
        'Age': int64,
        'Breed1': int64,
        'Breed2': int64,
        'Color1': int64,
        'Color2': int64,
        'Color3': int64,
        'Dewormed': int64,
        'Fee': int64,
        'FurLength': int64,
        'Gender': int64,
        'Health': int64,
        'MaturitySize': int64,
        'Quantity': int64,
        'State': int64,
        'Sterilized': int64,
        'Type': int64,
        'Vaccinated': int64,
        'VideoAmt': int64,
    }),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=5),
})
```

*   **Feature documentation**:

Feature                 | Class        | Shape           | Dtype  | Description
:---------------------- | :----------- | :-------------- | :----- | :----------
                        | FeaturesDict |                 |        |
PetID                   | Text         |                 | string |
attributes              | FeaturesDict |                 |        |
attributes/Age          | Tensor       |                 | int64  |
attributes/Breed1       | Tensor       |                 | int64  |
attributes/Breed2       | Tensor       |                 | int64  |
attributes/Color1       | Tensor       |                 | int64  |
attributes/Color2       | Tensor       |                 | int64  |
attributes/Color3       | Tensor       |                 | int64  |
attributes/Dewormed     | Tensor       |                 | int64  |
attributes/Fee          | Tensor       |                 | int64  |
attributes/FurLength    | Tensor       |                 | int64  |
attributes/Gender       | Tensor       |                 | int64  |
attributes/Health       | Tensor       |                 | int64  |
attributes/MaturitySize | Tensor       |                 | int64  |
attributes/Quantity     | Tensor       |                 | int64  |
attributes/State        | Tensor       |                 | int64  |
attributes/Sterilized   | Tensor       |                 | int64  |
attributes/Type         | Tensor       |                 | int64  |
attributes/Vaccinated   | Tensor       |                 | int64  |
attributes/VideoAmt     | Tensor       |                 | int64  |
image                   | Image        | (None, None, 3) | uint8  |
image/filename          | Text         |                 | string |
label                   | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('attributes', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/pet_finder-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/pet_finder-1.0.0.html";
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
@ONLINE {kaggle-petfinder-adoption-prediction,
    author = "Kaggle and PetFinder.my",
    title  = "PetFinder.my Adoption Prediction",
    month  = "april",
    year   = "2019",
    url    = "https://www.kaggle.com/c/petfinder-adoption-prediction/data/"
}
```

