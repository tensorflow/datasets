<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="caltech101" />
  <meta itemprop="description" content="Caltech-101 consists of pictures of objects belonging to 101 classes, plus one&#10;`background clutter` class. Each image is labelled with a single object. Each&#10;class contains roughly 40 to 800 images, totalling around 9k images. Images are&#10;of variable sizes, with typical edge lengths of 200-300 pixels. This version&#10;contains image-level labels only. The original dataset also contains bounding&#10;boxes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;caltech101&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/caltech101" />
  <meta itemprop="sameAs" content="https://doi.org/10.22002/D1.20086" />
  <meta itemprop="citation" content="@article{FeiFei2004LearningGV,&#10;  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},&#10;  author={Li Fei-Fei and Rob Fergus and Pietro Perona},&#10;  journal={Computer Vision and Pattern Recognition Workshop},&#10;  year={2004},&#10;}" />
</div>

# `caltech101`


Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

Caltech-101 consists of pictures of objects belonging to 101 classes, plus one
`background clutter` class. Each image is labelled with a single object. Each
class contains roughly 40 to 800 images, totalling around 9k images. Images are
of variable sizes, with typical edge lengths of 200-300 pixels. This version
contains image-level labels only. The original dataset also contains bounding
boxes.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/caltech-101">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://doi.org/10.22002/D1.20086](https://doi.org/10.22002/D1.20086)

*   **Source code**:
    [`tfds.datasets.caltech101.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/caltech101/caltech101_dataset_builder.py)

*   **Versions**:

    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   `3.0.1`: Website URL update
    *   **`3.0.2`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Download URL update

*   **Download size**: `131.05 MiB`

*   **Dataset size**: `132.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,084
`'train'` | 3,060

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/file_name': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=102),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape           | Dtype  | Description
:-------------- | :----------- | :-------------- | :----- | :----------
                | FeaturesDict |                 |        |
image           | Image        | (None, None, 3) | uint8  |
image/file_name | Text         |                 | string |
label           | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{FeiFei2004LearningGV,
  title={Learning Generative Visual Models from Few Training Examples: An Incremental Bayesian Approach Tested on 101 Object Categories},
  author={Li Fei-Fei and Rob Fergus and Pietro Perona},
  journal={Computer Vision and Pattern Recognition Workshop},
  year={2004},
}
```
