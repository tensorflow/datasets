<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="open_images_v4" />
  <meta itemprop="description" content="Open Images is a dataset of ~9M images that have been annotated with image-level&#10;labels and object bounding boxes.&#10;&#10;The training set of V4 contains 14.6M bounding boxes for 600 object classes on&#10;1.74M images, making it the largest existing dataset with object location&#10;annotations. The boxes have been largely manually drawn by professional&#10;annotators to ensure accuracy and consistency. The images are very diverse and&#10;often contain complex scenes with several objects (8.4 per image on average).&#10;Moreover, the dataset is annotated with image-level labels spanning thousands of&#10;classes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;open_images_v4&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/open_images_v4-original-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/open_images_v4" />
  <meta itemprop="sameAs" content="https://storage.googleapis.com/openimages/web/index.html" />
  <meta itemprop="citation" content="@article{OpenImages,&#10;  author = {Alina Kuznetsova and&#10;            Hassan Rom and&#10;            Neil Alldrin and&#10;            Jasper Uijlings and&#10;            Ivan Krasin and&#10;            Jordi Pont-Tuset and&#10;            Shahab Kamali and&#10;            Stefan Popov and&#10;            Matteo Malloci and&#10;            Tom Duerig and&#10;            Vittorio Ferrari},&#10;  title = {The Open Images Dataset V4: Unified image classification,&#10;           object detection, and visual relationship detection at scale},&#10;  year = {2018},&#10;  journal = {arXiv:1811.00982}&#10;}&#10;@article{OpenImages2,&#10;  author = {Krasin, Ivan and&#10;            Duerig, Tom and&#10;            Alldrin, Neil and&#10;            Ferrari, Vittorio&#10;            and Abu-El-Haija, Sami and&#10;            Kuznetsova, Alina and&#10;            Rom, Hassan and&#10;            Uijlings, Jasper and&#10;            Popov, Stefan and&#10;            Kamali, Shahab and&#10;            Malloci, Matteo and&#10;            Pont-Tuset, Jordi and&#10;            Veit, Andreas and&#10;            Belongie, Serge and&#10;            Gomes, Victor and&#10;            Gupta, Abhinav and&#10;            Sun, Chen and&#10;            Chechik, Gal and&#10;            Cai, David and&#10;            Feng, Zheyun and&#10;            Narayanan, Dhyanesh and&#10;            Murphy, Kevin},&#10;  title = {OpenImages: A public dataset for large-scale multi-label and&#10;           multi-class image classification.},&#10;  journal = {Dataset available from&#10;             https://storage.googleapis.com/openimages/web/index.html},&#10;  year={2017}&#10;}" />
</div>

# `open_images_v4`


*   **Description**:

Open Images is a dataset of ~9M images that have been annotated with image-level
labels and object bounding boxes.

The training set of V4 contains 14.6M bounding boxes for 600 object classes on
1.74M images, making it the largest existing dataset with object location
annotations. The boxes have been largely manually drawn by professional
annotators to ensure accuracy and consistency. The images are very diverse and
often contain complex scenes with several objects (8.4 per image on average).
Moreover, the dataset is annotated with image-level labels spanning thousands of
classes.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/open-images-v4">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html)

*   **Source code**:
    [`tfds.datasets.open_images_v4.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/open_images_v4/open_images_v4_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `565.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 125,436
`'train'`      | 1,743,042
`'validation'` | 41,620

*   **Feature structure**:

```python
FeaturesDict({
    'bobjects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=float32),
        'is_depiction': int8,
        'is_group_of': int8,
        'is_inside': int8,
        'is_occluded': int8,
        'is_truncated': int8,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=601),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=6),
    }),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'objects': Sequence({
        'confidence': int32,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=19995),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=6),
    }),
    'objects_trainable': Sequence({
        'confidence': int32,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=7186),
        'source': ClassLabel(shape=(), dtype=int64, num_classes=6),
    }),
})
```

*   **Feature documentation**:

| Feature                      | Class        | Shape  | Dtype   | Description |
| :--------------------------- | :----------- | :----- | :------ | :---------- |
|                              | FeaturesDict |        |         |             |
| bobjects                     | Sequence     |        |         |             |
| bobjects/bbox                | BBoxFeature  | (4,)   | float32 |             |
| bobjects/is_depiction        | Tensor       |        | int8    |             |
| bobjects/is_group_of         | Tensor       |        | int8    |             |
| bobjects/is_inside           | Tensor       |        | int8    |             |
| bobjects/is_occluded         | Tensor       |        | int8    |             |
| bobjects/is_truncated        | Tensor       |        | int8    |             |
| bobjects/label               | ClassLabel   |        | int64   |             |
| bobjects/source              | ClassLabel   |        | int64   |             |
| image                        | Image        | (None, | uint8   |             |
:                              :              : None,  :         :             :
:                              :              : 3)     :         :             :
| image/filename               | Text         |        | string  |             |
| objects                      | Sequence     |        |         |             |
| objects/confidence           | Tensor       |        | int32   |             |
| objects/label                | ClassLabel   |        | int64   |             |
| objects/source               | ClassLabel   |        | int64   |             |
| objects_trainable            | Sequence     |        |         |             |
| objects_trainable/confidence | Tensor       |        | int32   |             |
| objects_trainable/label      | ClassLabel   |        | int64   |             |
| objects_trainable/source     | ClassLabel   |        | int64   |             |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@article{OpenImages,
  author = {Alina Kuznetsova and
            Hassan Rom and
            Neil Alldrin and
            Jasper Uijlings and
            Ivan Krasin and
            Jordi Pont-Tuset and
            Shahab Kamali and
            Stefan Popov and
            Matteo Malloci and
            Tom Duerig and
            Vittorio Ferrari},
  title = {The Open Images Dataset V4: Unified image classification,
           object detection, and visual relationship detection at scale},
  year = {2018},
  journal = {arXiv:1811.00982}
}
@article{OpenImages2,
  author = {Krasin, Ivan and
            Duerig, Tom and
            Alldrin, Neil and
            Ferrari, Vittorio
            and Abu-El-Haija, Sami and
            Kuznetsova, Alina and
            Rom, Hassan and
            Uijlings, Jasper and
            Popov, Stefan and
            Kamali, Shahab and
            Malloci, Matteo and
            Pont-Tuset, Jordi and
            Veit, Andreas and
            Belongie, Serge and
            Gomes, Victor and
            Gupta, Abhinav and
            Sun, Chen and
            Chechik, Gal and
            Cai, David and
            Feng, Zheyun and
            Narayanan, Dhyanesh and
            Murphy, Kevin},
  title = {OpenImages: A public dataset for large-scale multi-label and
           multi-class image classification.},
  journal = {Dataset available from
             https://storage.googleapis.com/openimages/web/index.html},
  year={2017}
}
```


## open_images_v4/original (default config)

*   **Config description**: Images at their original resolution and quality.

*   **Dataset size**: `562.42 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/open_images_v4-original-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/open_images_v4-original-2.0.0.html";
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

## open_images_v4/300k

*   **Config description**: Images have roughly 300,000 pixels, at 72 JPEG
    quality.

*   **Dataset size**: `81.92 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/open_images_v4-300k-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/open_images_v4-300k-2.0.0.html";
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

## open_images_v4/200k

*   **Config description**: Images have roughly 200,000 pixels, at 72 JPEG
    quality.

*   **Dataset size**: `60.70 GiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/open_images_v4-200k-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/open_images_v4-200k-2.0.0.html";
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