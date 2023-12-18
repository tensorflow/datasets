<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cats_vs_dogs" />
  <meta itemprop="description" content="A large set of images of cats and dogs. There are 1738 corrupted images that are dropped.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cats_vs_dogs&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/cats_vs_dogs-4.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cats_vs_dogs" />
  <meta itemprop="sameAs" content="https://www.microsoft.com/en-us/download/details.aspx?id=54765" />
  <meta itemprop="citation" content="@Inproceedings (Conference){asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization,&#10;author = {Elson, Jeremy and Douceur, John (JD) and Howell, Jon and Saul, Jared},&#10;title = {Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization},&#10;booktitle = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},&#10;year = {2007},&#10;month = {October},&#10;publisher = {Association for Computing Machinery, Inc.},&#10;url = {https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/},&#10;edition = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},&#10;}" />
</div>

# `cats_vs_dogs`


*   **Description**:

A large set of images of cats and dogs. There are 1738 corrupted images that are
dropped.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/cats-vs-dogs">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.microsoft.com/en-us/download/details.aspx?id=54765](https://www.microsoft.com/en-us/download/details.aspx?id=54765)

*   **Source code**:
    [`tfds.image_classification.CatsVsDogs`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cats_vs_dogs.py)

*   **Versions**:

    *   `4.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   **`4.0.1`** (default): Recoding images in generator to fix corrupt JPEG
        data warnings (https://github.com/tensorflow/datasets/issues/2188)

*   **Download size**: `786.67 MiB`

*   **Dataset size**: `1.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 23,262

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape           | Dtype  | Description
:------------- | :----------- | :-------------- | :----- | :----------
               | FeaturesDict |                 |        |
image          | Image        | (None, None, 3) | uint8  |
image/filename | Text         |                 | string |
label          | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cats_vs_dogs-4.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cats_vs_dogs-4.0.1.html";
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
@Inproceedings (Conference){asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization,
author = {Elson, Jeremy and Douceur, John (JD) and Howell, Jon and Saul, Jared},
title = {Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image Categorization},
booktitle = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
year = {2007},
month = {October},
publisher = {Association for Computing Machinery, Inc.},
url = {https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/},
edition = {Proceedings of 14th ACM Conference on Computer and Communications Security (CCS)},
}
```

