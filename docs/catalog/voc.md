<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="voc" />
  <meta itemprop="description" content="This dataset contains the data from the PASCAL Visual Object Classes Challenge,&#10;corresponding to the Classification and Detection competitions.&#10;&#10;In the Classification competition, the goal is to predict the set of labels&#10;contained in the image, while in the Detection competition the goal is to&#10;predict the bounding box and label of each individual object.&#10;WARNING: As per the official dataset, the test set of VOC2012 does not contain&#10;annotations.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;voc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/voc-2007-5.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/voc" />
  <meta itemprop="sameAs" content="http://host.robots.ox.ac.uk/pascal/VOC/voc2007/" />
  <meta itemprop="citation" content="@misc{pascal-voc-2007,&#10;    author = &quot;Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.&quot;,&#10;    title = &quot;The {PASCAL} {V}isual {O}bject {C}lasses {C}hallenge 2007 {(VOC2007)} {R}esults&quot;,&#10;   howpublished = &quot;http://www.pascal-network.org/challenges/VOC/voc2007/workshop/index.html&quot;}" />
</div>

# `voc`


*   **Description**:

This dataset contains the data from the PASCAL Visual Object Classes Challenge,
corresponding to the Classification and Detection competitions.

In the Classification competition, the goal is to predict the set of labels
contained in the image, while in the Detection competition the goal is to
predict the bounding box and label of each individual object. WARNING: As per
the official dataset, the test set of VOC2012 does not contain annotations.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/pascal-voc-2007">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Source code**:
    [`tfds.object_detection.Voc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/object_detection/voc.py)

*   **Versions**:

    *   **`5.0.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'labels': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=20)),
    'labels_no_difficult': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=20)),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=float32),
        'is_difficult': bool,
        'is_truncated': bool,
        'label': ClassLabel(shape=(), dtype=int64, num_classes=20),
        'pose': ClassLabel(shape=(), dtype=int64, num_classes=5),
    }),
})
```

*   **Feature documentation**:

Feature              | Class                | Shape           | Dtype   | Description
:------------------- | :------------------- | :-------------- | :------ | :----------
                     | FeaturesDict         |                 |         |
image                | Image                | (None, None, 3) | uint8   |
image/filename       | Text                 |                 | string  |
labels               | Sequence(ClassLabel) | (None,)         | int64   |
labels_no_difficult  | Sequence(ClassLabel) | (None,)         | int64   |
objects              | Sequence             |                 |         |
objects/bbox         | BBoxFeature          | (4,)            | float32 |
objects/is_difficult | Tensor               |                 | bool    |
objects/is_truncated | Tensor               |                 | bool    |
objects/label        | ClassLabel           |                 | int64   |
objects/pose         | ClassLabel           |                 | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`


## voc/2007 (default config)

*   **Config description**: This dataset contains the data from the PASCAL
    Visual Object Classes Challenge 2007, a.k.a. VOC2007.

A total of 9963 images are included in this dataset, where each image contains a
set of objects, out of 20 different classes, making a total of 24640 annotated
objects.

*   **Homepage**:
    [http://host.robots.ox.ac.uk/pascal/VOC/voc2007/](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/)

*   **Download size**: `868.85 MiB`

*   **Dataset size**: `837.73 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,952
`'train'`      | 2,501
`'validation'` | 2,510

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/voc-2007-5.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/voc-2007-5.0.0.html";
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
@misc{pascal-voc-2007,
    author = "Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.",
    title = "The {PASCAL} {V}isual {O}bject {C}lasses {C}hallenge 2007 {(VOC2007)} {R}esults",
    howpublished = "http://www.pascal-network.org/challenges/VOC/voc2007/workshop/index.html"}
```

## voc/2012

*   **Config description**: This dataset contains the data from the PASCAL
    Visual Object Classes Challenge 2012, a.k.a. VOC2012.

A total of 11540 images are included in this dataset, where each image contains
a set of objects, out of 20 different classes, making a total of 27450 annotated
objects.

*   **Homepage**:
    [http://host.robots.ox.ac.uk/pascal/VOC/voc2012/](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/)

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `2.44 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,991
`'train'`      | 5,717
`'validation'` | 5,823

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/voc-2012-5.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/voc-2012-5.0.0.html";
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
@misc{pascal-voc-2012,
    author = "Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.",
    title = "The {PASCAL} {V}isual {O}bject {C}lasses {C}hallenge 2012 {(VOC2012)} {R}esults",
    howpublished = "http://www.pascal-network.org/challenges/VOC/voc2012/workshop/index.html"}
```
