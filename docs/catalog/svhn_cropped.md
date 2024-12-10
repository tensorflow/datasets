<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="svhn_cropped" />
  <meta itemprop="description" content="The Street View House Numbers (SVHN) Dataset is an image digit recognition&#10;dataset of over 600,000 digit images coming from real world data. Images are&#10;cropped to 32x32.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;svhn_cropped&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/svhn_cropped-3.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/svhn_cropped" />
  <meta itemprop="sameAs" content="http://ufldl.stanford.edu/housenumbers/" />
  <meta itemprop="citation" content="&quot;&quot;&quot;Street View House Numbers (SVHN) Dataset, cropped version.&quot;&quot;&quot;&#10;&#10;@article{Netzer2011,&#10;author = {Netzer, Yuval and Wang, Tao and Coates, Adam and Bissacco, Alessandro and Wu, Bo and Ng, Andrew Y},&#10;booktitle = {Advances in Neural Information Processing Systems ({NIPS})},&#10;title = {Reading Digits in Natural Images with Unsupervised Feature Learning},&#10;year = {2011}&#10;}" />
</div>

# `svhn_cropped`


*   **Description**:

The Street View House Numbers (SVHN) Dataset is an image digit recognition
dataset of over 600,000 digit images coming from real world data. Images are
cropped to 32x32.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/svhn">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://ufldl.stanford.edu/housenumbers/](http://ufldl.stanford.edu/housenumbers/)

*   **Source code**:
    [`tfds.datasets.svhn_cropped.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/svhn_cropped/svhn_cropped_dataset_builder.py)

*   **Versions**:

    *   **`3.1.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `1.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'extra'` | 531,131
`'test'`  | 26,032
`'train'` | 73,257

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(32, 32, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=10),
})
```

*   **Feature documentation**:

Feature | Class        | Shape       | Dtype  | Description
:------ | :----------- | :---------- | :----- | :----------
        | FeaturesDict |             |        |
id      | Text         |             | string |
image   | Image        | (32, 32, 3) | uint8  |
label   | ClassLabel   |             | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/svhn_cropped-3.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/svhn_cropped-3.1.0.html";
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
"""Street View House Numbers (SVHN) Dataset, cropped version."""

@article{Netzer2011,
author = {Netzer, Yuval and Wang, Tao and Coates, Adam and Bissacco, Alessandro and Wu, Bo and Ng, Andrew Y},
booktitle = {Advances in Neural Information Processing Systems ({NIPS})},
title = {Reading Digits in Natural Images with Unsupervised Feature Learning},
year = {2011}
}
```

