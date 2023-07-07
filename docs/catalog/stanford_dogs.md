<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_dogs" />
  <meta itemprop="description" content="The Stanford Dogs dataset contains images of 120 breeds of dogs from around the&#10;world. This dataset has been built using images and annotation from ImageNet for&#10;the task of fine-grained image categorization. There are 20,580 images, out of&#10;which 12,000 are used for training and 8580 for testing. Class labels and&#10;bounding box annotations are provided for all the 12,000 images.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stanford_dogs&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/stanford_dogs-0.2.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_dogs" />
  <meta itemprop="sameAs" content="http://vision.stanford.edu/aditya86/ImageNetDogs/main.html" />
  <meta itemprop="citation" content="@inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,&#10;author = &quot;Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and&#10;          Li Fei-Fei&quot;,&#10;title = &quot;Novel Dataset for Fine-Grained Image Categorization&quot;,&#10;booktitle = &quot;First Workshop on Fine-Grained Visual Categorization,&#10;             IEEE Conference on Computer Vision and Pattern Recognition&quot;,&#10;year = &quot;2011&quot;,&#10;month = &quot;June&quot;,&#10;address = &quot;Colorado Springs, CO&quot;,&#10;}&#10;@inproceedings{imagenet_cvpr09,&#10;        AUTHOR = {Deng, J. and Dong, W. and Socher, R. and Li, L.-J. and&#10;                  Li, K. and Fei-Fei, L.},&#10;        TITLE = {{ImageNet: A Large-Scale Hierarchical Image Database}},&#10;        BOOKTITLE = {CVPR09},&#10;        YEAR = {2009},&#10;        BIBSOURCE = &quot;http://www.image-net.org/papers/imagenet_cvpr09.bib&quot;}" />
</div>

# `stanford_dogs`


*   **Description**:

The Stanford Dogs dataset contains images of 120 breeds of dogs from around the
world. This dataset has been built using images and annotation from ImageNet for
the task of fine-grained image categorization. There are 20,580 images, out of
which 12,000 are used for training and 8580 for testing. Class labels and
bounding box annotations are provided for all the 12,000 images.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/stanford-dogs">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://vision.stanford.edu/aditya86/ImageNetDogs/main.html](http://vision.stanford.edu/aditya86/ImageNetDogs/main.html)

*   **Source code**:
    [`tfds.datasets.stanford_dogs.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/stanford_dogs/stanford_dogs_dataset_builder.py)

*   **Versions**:

    *   **`0.2.0`** (default): No release notes.

*   **Download size**: `778.12 MiB`

*   **Dataset size**: `744.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 8,580
`'train'` | 12,000

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=120),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape           | Dtype   | Description
:------------- | :----------- | :-------------- | :------ | :----------
               | FeaturesDict |                 |         |
image          | Image        | (None, None, 3) | uint8   |
image/filename | Text         |                 | string  |
label          | ClassLabel   |                 | int64   |
objects        | Sequence     |                 |         |
objects/bbox   | BBoxFeature  | (4,)            | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/stanford_dogs-0.2.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/stanford_dogs-0.2.0.html";
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
@inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,
author = "Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and
          Li Fei-Fei",
title = "Novel Dataset for Fine-Grained Image Categorization",
booktitle = "First Workshop on Fine-Grained Visual Categorization,
             IEEE Conference on Computer Vision and Pattern Recognition",
year = "2011",
month = "June",
address = "Colorado Springs, CO",
}
@inproceedings{imagenet_cvpr09,
        AUTHOR = {Deng, J. and Dong, W. and Socher, R. and Li, L.-J. and
                  Li, K. and Fei-Fei, L.},
        TITLE = {{ImageNet: A Large-Scale Hierarchical Image Database}},
        BOOKTITLE = {CVPR09},
        YEAR = {2009},
        BIBSOURCE = "http://www.image-net.org/papers/imagenet_cvpr09.bib"}
```

