<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_lt" />
  <meta itemprop="description" content="ImageNet-LT is a subset of original ImageNet ILSVRC 2012 dataset. The training&#10;set is subsampled such that the number of images per class follows a long-tailed&#10;distribution. The class with the maximum number of images contains 1,280&#10;examples, whereas the class with the minumum number of images contains only 5&#10;examples. The dataset also has a balanced validation set, which is also a subset&#10;of the ImageNet ILSVRC 2012 training set and contains 20 images per class. The&#10;test set of this dataset is the same as the validation set of the original&#10;ImageNet ILSVRC 2012 dataset.&#10;&#10;The original ImageNet ILSVRC 2012 dataset must be downloaded manually, and its&#10;path should be set with --manual_dir in order to generate this dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_lt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_lt-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_lt" />
  <meta itemprop="sameAs" content="https://github.com/zhmiao/OpenLongTailRecognition-OLTR" />
  <meta itemprop="citation" content="\&#10;@inproceedings{openlongtailrecognition,&#10;  title={Large-Scale Long-Tailed Recognition in an Open World},&#10;  author={Liu, Ziwei and Miao, Zhongqi and Zhan, Xiaohang and Wang, Jiayun and Gong, Boqing and Yu, Stella X.},&#10;  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;  year={2019},&#10;  url={https://github.com/zhmiao/OpenLongTailRecognition-OLTR}&#10;}" />
</div>

# `imagenet_lt`


Warning: Manual download required. See instructions below.

*   **Description**:

ImageNet-LT is a subset of original ImageNet ILSVRC 2012 dataset. The training
set is subsampled such that the number of images per class follows a long-tailed
distribution. The class with the maximum number of images contains 1,280
examples, whereas the class with the minumum number of images contains only 5
examples. The dataset also has a balanced validation set, which is also a subset
of the ImageNet ILSVRC 2012 training set and contains 20 images per class. The
test set of this dataset is the same as the validation set of the original
ImageNet ILSVRC 2012 dataset.

The original ImageNet ILSVRC 2012 dataset must be downloaded manually, and its
path should be set with --manual_dir in order to generate this dataset.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/imagenet-lt">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/zhmiao/OpenLongTailRecognition-OLTR](https://github.com/zhmiao/OpenLongTailRecognition-OLTR)

*   **Source code**:
    [`tfds.datasets.imagenet_lt.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagenet_lt/imagenet_lt_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `5.21 MiB`

*   **Dataset size**: `20.92 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: ILSVRC2012_img_train.tar and
    ILSVRC2012_img_val.tar.
    You need to register on http://www.image-net.org/download-images in order
    to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 50,000
`'train'`      | 115,846
`'validation'` | 20,000

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

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_lt-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_lt-1.0.0.html";
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
\
@inproceedings{openlongtailrecognition,
  title={Large-Scale Long-Tailed Recognition in an Open World},
  author={Liu, Ziwei and Miao, Zhongqi and Zhan, Xiaohang and Wang, Jiayun and Gong, Boqing and Yu, Stella X.},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2019},
  url={https://github.com/zhmiao/OpenLongTailRecognition-OLTR}
}
```

