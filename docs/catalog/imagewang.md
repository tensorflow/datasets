<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagewang" />
  <meta itemprop="description" content="Imagewang contains Imagenette and Imagewoof combined Image网 (pronounced&#10;&quot;Imagewang&quot;; 网 means &quot;net&quot; in Chinese) contains Imagenette and Imagewoof&#10;combined, but with some twists that make it into a tricky semi-supervised&#10;unbalanced classification problem:&#10;&#10;*   The validation set is the same as Imagewoof (i.e. 30% of Imagewoof images);&#10;    there are no Imagenette images in the validation set (they&#x27;re all in the&#10;    training set)&#10;*   Only 10% of Imagewoof images are in the training set!&#10;*   The remaining are in the unsup (&quot;unsupervised&quot;) directory, and you can not&#10;    use their labels in training!&#10;*   It&#x27;s even hard to type and hard to say!&#10;&#10;The dataset comes in three variants:&#10;&#10;*   Full size&#10;*   320 px&#10;*   160 px&#10;&#10;This dataset consists of the Imagenette dataset {size} variant.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagewang&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagewang-full-size-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagewang" />
  <meta itemprop="sameAs" content="https://github.com/fastai/imagenette" />
  <meta itemprop="citation" content="@misc{imagewang,&#10;  author    = &quot;Jeremy Howard&quot;,&#10;  title     = &quot;Imagewang&quot;,&#10;  url       = &quot;https://github.com/fastai/imagenette/&quot;&#10;}" />
</div>

# `imagewang`


*   **Description**:

Imagewang contains Imagenette and Imagewoof combined Image网 (pronounced
"Imagewang"; 网 means "net" in Chinese) contains Imagenette and Imagewoof
combined, but with some twists that make it into a tricky semi-supervised
unbalanced classification problem:

*   The validation set is the same as Imagewoof (i.e. 30% of Imagewoof images);
    there are no Imagenette images in the validation set (they're all in the
    training set)
*   Only 10% of Imagewoof images are in the training set!
*   The remaining are in the unsup ("unsupervised") directory, and you can not
    use their labels in training!
*   It's even hard to type and hard to say!

The dataset comes in three variants:

*   Full size
*   320 px
*   160 px

This dataset consists of the Imagenette dataset {size} variant.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/imagewang">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Config description**: Imagewang contains Imagenette and Imagewoof
    combined.

*   **Homepage**:
    [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette)

*   **Source code**:
    [`tfds.datasets.imagewang.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagewang/imagewang_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): No release notes.

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 14,669
`'validation'` | 3,929

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=20),
})
```

*   **Feature documentation**:

Feature | Class        | Shape           | Dtype | Description
:------ | :----------- | :-------------- | :---- | :----------
        | FeaturesDict |                 |       |
image   | Image        | (None, None, 3) | uint8 |
label   | ClassLabel   |                 | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@misc{imagewang,
  author    = "Jeremy Howard",
  title     = "Imagewang",
  url       = "https://github.com/fastai/imagenette/"
}
```


## imagewang/full-size (default config)

*   **Download size**: `2.70 GiB`

*   **Dataset size**: `1.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagewang-full-size-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagewang-full-size-2.0.0.html";
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

## imagewang/320px

*   **Download size**: `638.80 MiB`

*   **Dataset size**: `460.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagewang-320px-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagewang-320px-2.0.0.html";
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

## imagewang/160px

*   **Download size**: `182.63 MiB`

*   **Dataset size**: `140.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagewang-160px-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagewang-160px-2.0.0.html";
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