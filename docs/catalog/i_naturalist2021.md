<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="i_naturalist2021" />
  <meta itemprop="description" content="The iNaturalist dataset 2021 contains a total of 10,000 species. &#10;The full training dataset contains nearly 2.7M images. &#10;To make the dataset more accessible we have also created a &quot;mini&quot; training &#10;dataset with 50 examples per species for a total of 500K images. The full &#10;training `train` split overlaps with the `mini` split. The val set contains for&#10;each species 10 validation images (100K in total). There are a total of 500,000 &#10;test images in the `public_test` split (without ground-truth labels).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;i_naturalist2021&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/i_naturalist2021-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/i_naturalist2021" />
  <meta itemprop="sameAs" content="https://github.com/visipedia/inat_comp/tree/master/2021" />
  <meta itemprop="citation" content="\&#10;@misc{inaturalist21,&#10;    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2021}},&#10;    Title = {{iNaturalist} 2021 competition dataset.},&#10;    Year = {2021},&#10;    key = {{iNaturalist} 2021 competition dataset},&#10;    }" />
</div>

# `i_naturalist2021`


*   **Description**:

The iNaturalist dataset 2021 contains a total of 10,000 species. The full
training dataset contains nearly 2.7M images. To make the dataset more
accessible we have also created a "mini" training dataset with 50 examples per
species for a total of 500K images. The full training `train` split overlaps
with the `mini` split. The val set contains for each species 10 validation
images (100K in total). There are a total of 500,000 test images in the
`public_test` split (without ground-truth labels).

*   **Homepage**:
    [https://github.com/visipedia/inat_comp/tree/master/2021](https://github.com/visipedia/inat_comp/tree/master/2021)

*   **Source code**:
    [`tfds.image_classification.i_naturalist2021.INaturalist2021`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/i_naturalist2021/i_naturalist2021.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `316.54 GiB`

*   **Dataset size**: `318.38 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'mini'`  | 500,000
`'test'`  | 500,000
`'train'` | 2,686,843
`'val'`   | 100,000

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10000),
    'supercategory': ClassLabel(shape=(), dtype=tf.int64, num_classes=11),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape           | Dtype     | Description
:------------ | :----------- | :-------------- | :-------- | :----------
              | FeaturesDict |                 |           |
id            | Text         |                 | tf.string |
image         | Image        | (None, None, 3) | tf.uint8  |
label         | ClassLabel   |                 | tf.int64  |
supercategory | ClassLabel   |                 | tf.int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/i_naturalist2021-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/i_naturalist2021-1.0.0.html";
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
@misc{inaturalist21,
    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2021}},
    Title = {{iNaturalist} 2021 competition dataset.},
    Year = {2021},
    key = {{iNaturalist} 2021 competition dataset},
    }
```

