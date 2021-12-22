<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_lt" />
  <meta itemprop="description" content="ImageNet-LT is a subset of original ImageNet ILSVRC 2012 dataset.&#10;The training set is subsampled such that the number of images per class&#10;follows a long-tailed distribution. The class with the maximum number of images&#10;contains 1,280 examples, whereas the class with the minumum number of images&#10;contains only 5 examples. The dataset also has a balanced validation set,&#10;which is also a subset of the ImageNet ILSVRC 2012 training set and contains&#10;20 images per class. The test set of this dataset is the same as the validation&#10;set of the original ImageNet ILSVRC 2012 dataset.&#10;&#10;The original ImageNet ILSVRC 2012 dataset must be downloaded manually, and&#10;its path should be set with --manual_dir in order to generate this dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_lt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_lt" />
  <meta itemprop="sameAs" content="https://github.com/zhmiao/OpenLongTailRecognition-OLTR" />
  <meta itemprop="citation" content="\&#10;@inproceedings{openlongtailrecognition,&#10;  title={Large-Scale Long-Tailed Recognition in an Open World},&#10;  author={Liu, Ziwei and Miao, Zhongqi and Zhan, Xiaohang and Wang, Jiayun and Gong, Boqing and Yu, Stella X.},&#10;  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;  year={2019},&#10;  url={https://github.com/zhmiao/OpenLongTailRecognition-OLTR}&#10;}" />
</div>

# `imagenet_lt`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

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

*   **Homepage**:
    [https://github.com/zhmiao/OpenLongTailRecognition-OLTR](https://github.com/zhmiao/OpenLongTailRecognition-OLTR)

*   **Source code**:
    [`tfds.image_classification.imagenet_lt.ImagenetLt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet_lt/imagenet_lt.py)

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

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

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
\
@inproceedings{openlongtailrecognition,
  title={Large-Scale Long-Tailed Recognition in an Open World},
  author={Liu, Ziwei and Miao, Zhongqi and Zhan, Xiaohang and Wang, Jiayun and Gong, Boqing and Yu, Stella X.},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2019},
  url={https://github.com/zhmiao/OpenLongTailRecognition-OLTR}
}
```

