<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="citrus_leaves" />
  <meta itemprop="description" content="The original citrus dataset contains 759 images of healthy and unhealthy citrus&#10;fruits and leaves. However, for now we only export 594 images of citrus leaves&#10;with the following labels: Black Spot, Canker, Greening, and Healthy. The&#10;exported images are in PNG format and have 256x256 pixels.&#10;&#10;NOTE: Leaf images with Melanose label were dropped due to very small count and&#10;other non-leaf images being present in the same directory.&#10;&#10;Dataset URL: https://data.mendeley.com/datasets/3f83gxmv57/2&#10;License: http://creativecommons.org/licenses/by/4.0&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;citrus_leaves&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/citrus_leaves-0.1.2.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/citrus_leaves" />
  <meta itemprop="sameAs" content="https://data.mendeley.com/datasets/3f83gxmv57/2" />
  <meta itemprop="citation" content="@article{rauf2019citrus,&#10;  title={A citrus fruits and leaves dataset for detection and classification of&#10;citrus diseases through machine learning},&#10;  author={Rauf, Hafiz Tayyab and Saleem, Basharat Ali and Lali, M Ikram Ullah&#10;and Khan, Muhammad Attique and Sharif, Muhammad and Bukhari, Syed Ahmad Chan},&#10;  journal={Data in brief},&#10;  volume={26},&#10;  pages={104340},&#10;  year={2019},&#10;  publisher={Elsevier}&#10;}" />
</div>

# `citrus_leaves`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=citrus_leaves">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The original citrus dataset contains 759 images of healthy and unhealthy citrus
fruits and leaves. However, for now we only export 594 images of citrus leaves
with the following labels: Black Spot, Canker, Greening, and Healthy. The
exported images are in PNG format and have 256x256 pixels.

NOTE: Leaf images with Melanose label were dropped due to very small count and
other non-leaf images being present in the same directory.

Dataset URL: https://data.mendeley.com/datasets/3f83gxmv57/2 License:
http://creativecommons.org/licenses/by/4.0

*   **Homepage**:
    [https://data.mendeley.com/datasets/3f83gxmv57/2](https://data.mendeley.com/datasets/3f83gxmv57/2)

*   **Source code**:
    [`tfds.image_classification.CitrusLeaves`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/citrus.py)

*   **Versions**:

    *   `0.1.1`: Citrus Leaves dataset
    *   **`0.1.2`** (default): Website URL update

*   **Download size**: `63.87 MiB`

*   **Dataset size**: `37.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 594

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=4),
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

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/citrus_leaves-0.1.2.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/citrus_leaves-0.1.2.html";
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
@article{rauf2019citrus,
  title={A citrus fruits and leaves dataset for detection and classification of
citrus diseases through machine learning},
  author={Rauf, Hafiz Tayyab and Saleem, Basharat Ali and Lali, M Ikram Ullah
and Khan, Muhammad Attique and Sharif, Muhammad and Bukhari, Syed Ahmad Chan},
  journal={Data in brief},
  volume={26},
  pages={104340},
  year={2019},
  publisher={Elsevier}
}
```

