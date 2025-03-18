<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet2012_fewshot" />
  <meta itemprop="description" content="Imagenet2012Fewshot is a subset of original ImageNet ILSVRC 2012 dataset. The&#10;dataset share the *same* validation set as the original ImageNet ILSVRC 2012&#10;dataset. However, the training set is subsampled in a label balanced fashion. In&#10;`5shot` configuration, 5 images per label, or 5000 images are sampled; and in&#10;`10shot` configuration, 10 images per label, or 10000 images are sampled.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet2012_fewshot&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_fewshot-1shot-5.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet2012_fewshot" />
  <meta itemprop="sameAs" content="http://image-net.org/" />
  <meta itemprop="citation" content="@article{ILSVRC15,&#10;  Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},&#10;  Title = {{ImageNet Large Scale Visual Recognition Challenge}},&#10;  Year = {2015},&#10;  journal   = {International Journal of Computer Vision (IJCV)},&#10;  doi = {10.1007/s11263-015-0816-y},&#10;  volume={115},&#10;  number={3},&#10;  pages={211-252}&#10;}" />
</div>

# `imagenet2012_fewshot`


Warning: Manual download required. See instructions below.

*   **Description**:

Imagenet2012Fewshot is a subset of original ImageNet ILSVRC 2012 dataset. The
dataset share the *same* validation set as the original ImageNet ILSVRC 2012
dataset. However, the training set is subsampled in a label balanced fashion. In
`5shot` configuration, 5 images per label, or 5000 images are sampled; and in
`10shot` configuration, 10 images per label, or 10000 images are sampled.

*   **Homepage**: [http://image-net.org/](http://image-net.org/)

*   **Source code**:
    [`tfds.datasets.imagenet2012_fewshot.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagenet2012_fewshot/imagenet2012_fewshot_dataset_builder.py)

*   **Versions**:

    *   `2.0.0`: Fix validation labels.
    *   `2.0.1`: Encoding fix. No changes from user point of view.
    *   `3.0.0`: Fix colorization on ~12 images (CMYK -> RGB). Fix format for
        consistency (convert the single png image to Jpeg). Faster generation
        reading directly from the archive.

    *   `4.0.0`: (unpublished)

    *   `5.0.0`: New split API (https://tensorflow.org/datasets/splits)

    *   **`5.0.1`** (default): No release notes.

    *   `5.1.0`: Added test split.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: ILSVRC2012_img_train.tar and
    ILSVRC2012_img_val.tar.
    You need to register on https://image-net.org/download-images in order
    to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape           | Dtype  | Description
:-------- | :----------- | :-------------- | :----- | :----------
          | FeaturesDict |                 |        |
file_name | Text         |                 | string |
image     | Image        | (None, None, 3) | uint8  |
label     | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@article{ILSVRC15,
  Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
  Title = {{ImageNet Large Scale Visual Recognition Challenge}},
  Year = {2015},
  journal   = {International Journal of Computer Vision (IJCV)},
  doi = {10.1007/s11263-015-0816-y},
  volume={115},
  number={3},
  pages={211-252}
}
```


## imagenet2012_fewshot/1shot (default config)

*   **Config description**: 1shot of total ImageNet training set.

*   **Dataset size**: `6.46 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 1,000
`'tune'`       | 1,000
`'validation'` | 50,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_fewshot-1shot-5.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet2012_fewshot-1shot-5.0.1.html";
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

## imagenet2012_fewshot/5shot

*   **Config description**: 5shot of total ImageNet training set.

*   **Dataset size**: `6.88 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 5,000
`'tune'`       | 1,000
`'validation'` | 50,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_fewshot-5shot-5.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet2012_fewshot-5shot-5.0.1.html";
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

## imagenet2012_fewshot/10shot

*   **Config description**: 10shot of total ImageNet training set.

*   **Dataset size**: `7.42 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 10,000
`'tune'`       | 1,000
`'validation'` | 50,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_fewshot-10shot-5.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet2012_fewshot-10shot-5.0.1.html";
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