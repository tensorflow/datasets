<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="oxford_iiit_pet" />
  <meta itemprop="description" content="The Oxford-IIIT pet dataset is a 37 category pet image dataset with roughly 200&#10;images for each class. The images have large variations in scale, pose and&#10;lighting. All images have an associated ground truth annotation of breed and&#10;species. Additionally, head bounding boxes are provided for the training split,&#10;allowing using this dataset for simple object detection tasks. In the test&#10;split, the bounding boxes are empty.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;oxford_iiit_pet&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/oxford_iiit_pet" />
  <meta itemprop="sameAs" content="http://www.robots.ox.ac.uk/~vgg/data/pets/" />
  <meta itemprop="citation" content="@InProceedings{parkhi12a,&#10;  author       = &quot;Parkhi, O. M. and Vedaldi, A. and Zisserman, A. and Jawahar, C.~V.&quot;,&#10;  title        = &quot;Cats and Dogs&quot;,&#10;  booktitle    = &quot;IEEE Conference on Computer Vision and Pattern Recognition&quot;,&#10;  year         = &quot;2012&quot;,&#10;}" />
</div>

# `oxford_iiit_pet`


*   **Description**:

The Oxford-IIIT pet dataset is a 37 category pet image dataset with roughly 200
images for each class. The images have large variations in scale, pose and
lighting. All images have an associated ground truth annotation of breed and
species. Additionally, head bounding boxes are provided for the training split,
allowing using this dataset for simple object detection tasks. In the test
split, the bounding boxes are empty.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/oxford-iiit-pets">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.robots.ox.ac.uk/~vgg/data/pets/](http://www.robots.ox.ac.uk/~vgg/data/pets/)

*   **Source code**:
    [`tfds.datasets.oxford_iiit_pet.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/oxford_iiit_pet/oxford_iiit_pet_dataset_builder.py)

*   **Versions**:

    *   **`4.0.0`** (default): Add head bounding boxes. Fix corrupt images.
        Update dataset URL.

*   **Download size**: `773.52 MiB`

*   **Dataset size**: `773.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 3,669
`'train'` | 3,680

*   **Feature structure**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=string),
    'head_bbox': BBoxFeature(shape=(4,), dtype=float32),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=37),
    'segmentation_mask': Image(shape=(None, None, 1), dtype=uint8),
    'species': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape           | Dtype   | Description
:---------------- | :----------- | :-------------- | :------ | :----------
                  | FeaturesDict |                 |         |
file_name         | Text         |                 | string  |
head_bbox         | BBoxFeature  | (4,)            | float32 |
image             | Image        | (None, None, 3) | uint8   |
label             | ClassLabel   |                 | int64   |
segmentation_mask | Image        | (None, None, 1) | uint8   |
species           | ClassLabel   |                 | int64   |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/oxford_iiit_pet-4.0.0.html";
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
@InProceedings{parkhi12a,
  author       = "Parkhi, O. M. and Vedaldi, A. and Zisserman, A. and Jawahar, C.~V.",
  title        = "Cats and Dogs",
  booktitle    = "IEEE Conference on Computer Vision and Pattern Recognition",
  year         = "2012",
}
```

