<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech_birds2010" />
  <meta itemprop="description" content="Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos &#10;of 200 bird species (mostly North American). The total number of &#10;categories of birds is 200 and there are 6033 images in the 2010 &#10;dataset and 11,788 images in the 2011 dataset.&#10;Annotations include bounding boxes, segmentation labels.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;caltech_birds2010&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech_birds2010" />
  <meta itemprop="sameAs" content="https://www.vision.caltech.edu/datasets/cub_200_2011/" />
  <meta itemprop="citation" content="@techreport{WelinderEtal2010,&#10;Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},&#10;Institution = {California Institute of Technology},&#10;Number = {CNS-TR-2010-001},&#10;Title = {{Caltech-UCSD Birds 200}},&#10;Year = {2010}&#10;}" />
</div>

# `caltech_birds2010`


*   **Description**:

Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos of 200 bird
species (mostly North American). The total number of categories of birds is 200
and there are 6033 images in the 2010 dataset and 11,788 images in the 2011
dataset. Annotations include bounding boxes, segmentation labels.

*   **Homepage**:
    [https://www.vision.caltech.edu/datasets/cub_200_2011/](https://www.vision.caltech.edu/datasets/cub_200_2011/)

*   **Source code**:
    [`tfds.image_classification.CaltechBirds2010`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/caltech_birds.py)

*   **Versions**:

    *   **`0.1.1`** (default): No release notes.

*   **Download size**: `659.14 MiB`

*   **Dataset size**: `659.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 3,033
`'train'` | 3,000

*   **Feature structure**:

```python
FeaturesDict({
    'bbox': BBoxFeature(shape=(4,), dtype=float32),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=200),
    'label_name': Text(shape=(), dtype=string),
    'segmentation_mask': Image(shape=(None, None, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape           | Dtype   | Description
:---------------- | :----------- | :-------------- | :------ | :----------
                  | FeaturesDict |                 |         |
bbox              | BBoxFeature  | (4,)            | float32 |
image             | Image        | (None, None, 3) | uint8   |
image/filename    | Text         |                 | string  |
label             | ClassLabel   |                 | int64   |
label_name        | Text         |                 | string  |
segmentation_mask | Image        | (None, None, 1) | uint8   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/caltech_birds2010-0.1.1.html";
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
@techreport{WelinderEtal2010,
Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},
Institution = {California Institute of Technology},
Number = {CNS-TR-2010-001},
Title = {{Caltech-UCSD Birds 200}},
Year = {2010}
}
```

