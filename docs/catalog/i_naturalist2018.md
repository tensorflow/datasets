<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="i_naturalist2018" />
  <meta itemprop="description" content="There are a total of 8,142 species in the dataset, with 437,513 training images,&#10;and 24,426 validation images. Each image has one ground truth label.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;i_naturalist2018&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/i_naturalist2018-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/i_naturalist2018" />
  <meta itemprop="sameAs" content="https://github.com/visipedia/inat_comp/tree/master/2018" />
  <meta itemprop="citation" content="\&#10;@misc{inaturalist18,&#10;    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2018}},&#10;    Title = {{iNaturalist} 2018 competition dataset.},&#10;    Year = {2018},&#10;    key = {{iNaturalist} 2018 competition dataset},&#10;    }" />
</div>

# `i_naturalist2018`


*   **Description**:

There are a total of 8,142 species in the dataset, with 437,513 training images,
and 24,426 validation images. Each image has one ground truth label.

*   **Homepage**:
    [https://github.com/visipedia/inat_comp/tree/master/2018](https://github.com/visipedia/inat_comp/tree/master/2018)

*   **Source code**:
    [`tfds.image_classification.i_naturalist2018.INaturalist2018`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/i_naturalist2018/i_naturalist2018.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `158.38 GiB`

*   **Dataset size**: `158.89 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 149,394
`'train'`      | 437,513
`'validation'` | 24,426

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=8142),
    'supercategory': ClassLabel(shape=(), dtype=int64, num_classes=14),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape           | Dtype  | Description
:------------ | :----------- | :-------------- | :----- | :----------
              | FeaturesDict |                 |        |
id            | Text         |                 | string |
image         | Image        | (None, None, 3) | uint8  |
label         | ClassLabel   |                 | int64  |
supercategory | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/i_naturalist2018-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/i_naturalist2018-1.0.0.html";
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
\
@misc{inaturalist18,
    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2018}},
    Title = {{iNaturalist} 2018 competition dataset.},
    Year = {2018},
    key = {{iNaturalist} 2018 competition dataset},
    }
```

