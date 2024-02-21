<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="iris" />
  <meta itemprop="description" content="This is perhaps the best known database to be found in the pattern recognition&#10;literature. Fisher&#x27;s paper is a classic in the field and is referenced&#10;frequently to this day. (See Duda &amp; Hart, for example.) The data set contains&#10;3 classes of 50 instances each, where each class refers to a type of iris&#10;plant. One class is linearly separable from the other 2; the latter are NOT&#10;linearly separable from each other.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;iris&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/iris" />
  <meta itemprop="sameAs" content="https://archive.ics.uci.edu/ml/datasets/iris" />
  <meta itemprop="citation" content="@misc{Dua:2019 ,&#10;author = &quot;Dua, Dheeru and Graff, Casey&quot;,&#10;year = &quot;2017&quot;,&#10;title = &quot;{UCI} Machine Learning Repository&quot;,&#10;url = &quot;http://archive.ics.uci.edu/ml&quot;,&#10;institution = &quot;University of California, Irvine, School of Information and Computer Sciences&quot;&#10;}" />
</div>

# `iris`


*   **Description**:

This is perhaps the best known database to be found in the pattern recognition
literature. Fisher's paper is a classic in the field and is referenced
frequently to this day. (See Duda & Hart, for example.) The data set contains 3
classes of 50 instances each, where each class refers to a type of iris plant.
One class is linearly separable from the other 2; the latter are NOT linearly
separable from each other.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/iris-1">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://archive.ics.uci.edu/ml/datasets/iris](https://archive.ics.uci.edu/ml/datasets/iris)

*   **Source code**:
    [`tfds.structured.Iris`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/iris.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `4.44 KiB`

*   **Dataset size**: `7.62 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 150

*   **Feature structure**:

```python
FeaturesDict({
    'features': Tensor(shape=(4,), dtype=float32),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype   | Description
:------- | :----------- | :---- | :------ | :----------
         | FeaturesDict |       |         |
features | Tensor       | (4,)  | float32 |
label    | ClassLabel   |       | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'label')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/iris-2.0.0.html";
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
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
}
```

