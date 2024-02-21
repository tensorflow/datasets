<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="siscore" />
  <meta itemprop="description" content="SI-Score (Synthetic Interventions on Scenes for Robustness Evaluation) is a&#10;dataset to evaluate robustness of image classification models to changes in&#10;object size, location and rotation angle.&#10;&#10;In SI-SCORE, we take objects and backgrounds and systematically vary object&#10;size, location and rotation angle so we can study the effect of changing these&#10;factors on model performance. The image label space is the ImageNet&#10;label space (1k classes) for easy evaluation of models.&#10;&#10;More information about the dataset can be found at&#10;https://github.com/google-research/si-score.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;siscore&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/siscore-rotation-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/siscore" />
  <meta itemprop="sameAs" content="https://github.com/google-research/si-score" />
  <meta itemprop="citation" content="@misc{djolonga2020robustness,&#10;      title={On Robustness and Transferability of Convolutional Neural Networks},&#10;      author={Josip Djolonga and Jessica Yung and Michael Tschannen and Rob Romijnders and Lucas Beyer and Alexander Kolesnikov and Joan Puigcerver and Matthias Minderer and Alexander D&#x27;Amour and Dan Moldovan and Sylvain Gelly and Neil Houlsby and Xiaohua Zhai and Mario Lucic},&#10;      year={2020},&#10;      eprint={2007.08558},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CV}&#10;}" />
</div>

# `siscore`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=siscore">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

SI-Score (Synthetic Interventions on Scenes for Robustness Evaluation) is a
dataset to evaluate robustness of image classification models to changes in
object size, location and rotation angle.

In SI-SCORE, we take objects and backgrounds and systematically vary object
size, location and rotation angle so we can study the effect of changing these
factors on model performance. The image label space is the ImageNet label space
(1k classes) for easy evaluation of models.

More information about the dataset can be found at
https://github.com/google-research/si-score.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/si-score">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/google-research/si-score](https://github.com/google-research/si-score)

*   **Source code**:
    [`tfds.datasets.siscore.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/siscore/siscore_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'dataset_label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image_id': int64,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape           | Dtype | Description
:------------ | :----------- | :-------------- | :---- | :----------
              | FeaturesDict |                 |       |
dataset_label | ClassLabel   |                 | int64 |
image         | Image        | (None, None, 3) | uint8 |
image_id      | Tensor       |                 | int64 |
label         | ClassLabel   |                 | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@misc{djolonga2020robustness,
      title={On Robustness and Transferability of Convolutional Neural Networks},
      author={Josip Djolonga and Jessica Yung and Michael Tschannen and Rob Romijnders and Lucas Beyer and Alexander Kolesnikov and Joan Puigcerver and Matthias Minderer and Alexander D'Amour and Dan Moldovan and Sylvain Gelly and Neil Houlsby and Xiaohua Zhai and Mario Lucic},
      year={2020},
      eprint={2007.08558},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


## siscore/rotation (default config)

*   **Config description**: factor of variation: rotation

*   **Download size**: `1.40 GiB`

*   **Dataset size**: `1.40 GiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 39,540

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/siscore-rotation-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/siscore-rotation-1.0.0.html";
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

## siscore/size

*   **Config description**: factor of variation: size

*   **Download size**: `3.25 GiB`

*   **Dataset size**: `3.27 GiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 92,884

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/siscore-size-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/siscore-size-1.0.0.html";
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

## siscore/location

*   **Config description**: factor of variation: location

*   **Download size**: `18.21 GiB`

*   **Dataset size**: `18.31 GiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 541,548

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/siscore-location-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/siscore-location-1.0.0.html";
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