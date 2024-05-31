<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="patch_camelyon" />
  <meta itemprop="description" content="The PatchCamelyon benchmark is a new and challenging image classification&#10;dataset. It consists of 327.680 color images (96 x 96px) extracted from&#10;histopathologic scans of lymph node sections. Each image is annoted with a&#10;binary label indicating presence of metastatic tissue. PCam provides a new&#10;benchmark for machine learning models: bigger than CIFAR10, smaller than&#10;Imagenet, trainable on a single GPU.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;patch_camelyon&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/patch_camelyon-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/patch_camelyon" />
  <meta itemprop="sameAs" content="https://patchcamelyon.grand-challenge.org/" />
  <meta itemprop="citation" content="@misc{b_s_veeling_j_linmans_j_winkens_t_cohen_2018_2546921,&#10;  author       = {B. S. Veeling, J. Linmans, J. Winkens, T. Cohen, M. Welling},&#10;  title        = {Rotation Equivariant CNNs for Digital Pathology},&#10;  month        = sep,&#10;  year         = 2018,&#10;  doi          = {10.1007/978-3-030-00934-2_24},&#10;  url          = {https://doi.org/10.1007/978-3-030-00934-2_24}&#10;}" />
</div>

# `patch_camelyon`


*   **Description**:

The PatchCamelyon benchmark is a new and challenging image classification
dataset. It consists of 327.680 color images (96 x 96px) extracted from
histopathologic scans of lymph node sections. Each image is annoted with a
binary label indicating presence of metastatic tissue. PCam provides a new
benchmark for machine learning models: bigger than CIFAR10, smaller than
Imagenet, trainable on a single GPU.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/pcam">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://patchcamelyon.grand-challenge.org/](https://patchcamelyon.grand-challenge.org/)

*   **Source code**:
    [`tfds.datasets.patch_camelyon.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/patch_camelyon/patch_camelyon_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `7.48 GiB`

*   **Dataset size**: `7.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 32,768
`'train'`      | 262,144
`'validation'` | 32,768

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(96, 96, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature | Class        | Shape       | Dtype  | Description
:------ | :----------- | :---------- | :----- | :----------
        | FeaturesDict |             |        |
id      | Text         |             | string |
image   | Image        | (96, 96, 3) | uint8  |
label   | ClassLabel   |             | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/patch_camelyon-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/patch_camelyon-2.0.0.html";
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
@misc{b_s_veeling_j_linmans_j_winkens_t_cohen_2018_2546921,
  author       = {B. S. Veeling, J. Linmans, J. Winkens, T. Cohen, M. Welling},
  title        = {Rotation Equivariant CNNs for Digital Pathology},
  month        = sep,
  year         = 2018,
  doi          = {10.1007/978-3-030-00934-2_24},
  url          = {https://doi.org/10.1007/978-3-030-00934-2_24}
}
```

