<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="titanic" />
  <meta itemprop="description" content="Dataset describing the survival status of individual passengers on the Titanic.&#10;Missing values in the original dataset are represented using ?. Float and int&#10;missing values are replaced with -1, string missing values are replaced with&#10;&#x27;Unknown&#x27;.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;titanic&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/titanic" />
  <meta itemprop="sameAs" content="https://www.openml.org/d/40945" />
  <meta itemprop="citation" content="@ONLINE {titanic,&#10;author = &quot;Frank E. Harrell Jr., Thomas Cason&quot;,&#10;title  = &quot;Titanic dataset&quot;,&#10;month  = &quot;oct&quot;,&#10;year   = &quot;2017&quot;,&#10;url    = &quot;https://www.openml.org/d/40945&quot;&#10;}" />
</div>

# `titanic`


*   **Description**:

Dataset describing the survival status of individual passengers on the Titanic.
Missing values in the original dataset are represented using ?. Float and int
missing values are replaced with -1, string missing values are replaced with
'Unknown'.

*   **Homepage**:
    [https://www.openml.org/d/40945](https://www.openml.org/d/40945)

*   **Source code**:
    [`tfds.datasets.titanic.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/titanic/titanic_dataset_builder.py)

*   **Versions**:

    *   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   `3.0.0`: Use a standard flat dictionary of features for the dataset. Use
        `as_supervised=True` to split the dataset into a `(features_dict,
        survived)` tuple.
    *   **`4.0.0`** (default): Fix inverted labels which were inverted in the
        3.0.0.

*   **Download size**: `114.98 KiB`

*   **Dataset size**: `382.58 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,309

*   **Feature structure**:

```python
FeaturesDict({
    'age': float32,
    'boat': string,
    'body': int32,
    'cabin': string,
    'embarked': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'fare': float32,
    'home.dest': string,
    'name': string,
    'parch': int32,
    'pclass': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'sex': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'sibsp': int32,
    'survived': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'ticket': string,
})
```

*   **Feature documentation**:

Feature   | Class        | Shape | Dtype   | Description
:-------- | :----------- | :---- | :------ | :----------
          | FeaturesDict |       |         |
age       | Tensor       |       | float32 |
boat      | Tensor       |       | string  |
body      | Tensor       |       | int32   |
cabin     | Tensor       |       | string  |
embarked  | ClassLabel   |       | int64   |
fare      | Tensor       |       | float32 |
home.dest | Tensor       |       | string  |
name      | Tensor       |       | string  |
parch     | Tensor       |       | int32   |
pclass    | ClassLabel   |       | int64   |
sex       | ClassLabel   |       | int64   |
sibsp     | Tensor       |       | int32   |
survived  | ClassLabel   |       | int64   |
ticket    | Tensor       |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'age': 'age', 'boat': 'boat', 'body': 'body', 'cabin': 'cabin',
    'embarked': 'embarked', 'fare': 'fare', 'home.dest': 'home.dest', 'name':
    'name', 'parch': 'parch', 'pclass': 'pclass', 'sex': 'sex', 'sibsp':
    'sibsp', 'ticket': 'ticket'}, 'survived')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/titanic-4.0.0.html";
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
@ONLINE {titanic,
author = "Frank E. Harrell Jr., Thomas Cason",
title  = "Titanic dataset",
month  = "oct",
year   = "2017",
url    = "https://www.openml.org/d/40945"
}
```

