<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="domainnet" />
  <meta itemprop="description" content="The DomainNet dataset consists of images from six distinct domains, including&#10;photos (real), painting, clipart, quickdraw, infograph and sketch. Per domain&#10;there are 48K - 172K images (600K in total) categorized into 345 classes.&#10;&#10;In this TFDS version of DomainNet the cleaned version is used.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;domainnet&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/domainnet" />
  <meta itemprop="sameAs" content="http://ai.bu.edu/DomainNet/" />
  <meta itemprop="citation" content="@inproceedings{peng2019moment,&#10;  title={Moment matching for multi-source domain adaptation},&#10;  author={Peng, Xingchao and Bai, Qinxun and Xia, Xide and Huang, Zijun and Saenko, Kate and Wang, Bo},&#10;  booktitle={Proceedings of the IEEE International Conference on Computer Vision},&#10;  pages={1406--1415},&#10;  year={2019}&#10;}" />
</div>

# `domainnet`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The DomainNet dataset consists of images from six distinct domains, including
photos (real), painting, clipart, quickdraw, infograph and sketch. Per domain
there are 48K - 172K images (600K in total) categorized into 345 classes.

In this TFDS version of DomainNet the cleaned version is used.

*   **Homepage**: [http://ai.bu.edu/DomainNet/](http://ai.bu.edu/DomainNet/)

*   **Source code**:
    [`tfds.image_classification.domainnet.Domainnet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/domainnet/domainnet.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=345),
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
@inproceedings{peng2019moment,
  title={Moment matching for multi-source domain adaptation},
  author={Peng, Xingchao and Bai, Qinxun and Xia, Xide and Huang, Zijun and Saenko, Kate and Wang, Bo},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={1406--1415},
  year={2019}
}
```

## domainnet/real (default config)

## domainnet/painting

## domainnet/clipart

## domainnet/quickdraw

## domainnet/infograph

## domainnet/sketch
