<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="imagenet_v2" />
  <meta itemprop="description" content="ImageNet-v2 is an ImageNet test set (10 per class) collected by closely&#10;following the original labelling protocol. Each image has been labelled by&#10;at least 10 MTurk workers, possibly more, and depending on the strategy used to&#10;select which images to include among the 10 chosen for the given class there are&#10;three different versions of the dataset. Please refer to section four of the&#10;paper for more details on how the different variants were compiled.&#10;&#10;The label space is the same as that of ImageNet2012. Each example is&#10;represented as a dictionary with the following keys:&#10;&#10;* &#x27;image&#x27;: The image, a (H, W, 3)-tensor.&#10;* &#x27;label&#x27;: An integer in the range [0, 1000).&#10;* &#x27;file_name&#x27;: A unique sting identifying the example within the dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_v2&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_v2" />
  <meta itemprop="sameAs" content="https://github.com/modestyachts/ImageNetV2" />
  <meta itemprop="citation" content="@inproceedings{recht2019imagenet,&#10;  title={Do ImageNet Classifiers Generalize to ImageNet?},&#10;  author={Recht, Benjamin and Roelofs, Rebecca and Schmidt, Ludwig and Shankar, Vaishaal},&#10;  booktitle={International Conference on Machine Learning},&#10;  pages={5389--5400},&#10;  year={2019}&#10;}" />
</div>

# `imagenet_v2`

*   **Description**:

ImageNet-v2 is an ImageNet test set (10 per class) collected by closely
following the original labelling protocol. Each image has been labelled by at
least 10 MTurk workers, possibly more, and depending on the strategy used to
select which images to include among the 10 chosen for the given class there are
three different versions of the dataset. Please refer to section four of the
paper for more details on how the different variants were compiled.

The label space is the same as that of ImageNet2012. Each example is represented
as a dictionary with the following keys:

*   'image': The image, a (H, W, 3)-tensor.
*   'label': An integer in the range [0, 1000).
*   'file_name': A unique sting identifying the example within the dataset.

*   **Config description**: ImageNet-v2 is an ImageNet test set (10 per class)
    collected by closely following the original labelling protocol. Each image
    has been labelled by at least 10 MTurk workers, possibly more, and depending
    on the strategy used to select which images to include among the 10 chosen
    for the given class there are three different versions of the dataset.
    Please refer to section four of the paper for more details on how the
    different variants were compiled.

The label space is the same as that of ImageNet2012. Each example is represented
as a dictionary with the following keys:

*   'image': The image, a (H, W, 3)-tensor.
*   'label': An integer in the range [0, 1000).
*   'file_name': A unique sting identifying the example within the dataset.

*   **Homepage**:
    [https://github.com/modestyachts/ImageNetV2](https://github.com/modestyachts/ImageNetV2)

*   **Source code**:
    [`tfds.image_classification.ImagenetV2`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet_v2.py)

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
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@inproceedings{recht2019imagenet,
  title={Do ImageNet Classifiers Generalize to ImageNet?},
  author={Recht, Benjamin and Roelofs, Rebecca and Schmidt, Ludwig and Shankar, Vaishaal},
  booktitle={International Conference on Machine Learning},
  pages={5389--5400},
  year={2019}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

## imagenet_v2/matched-frequency (default config)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

## imagenet_v2/threshold-0.7

*   **Versions**:

    *   **`0.1.1`** (default): No release notes.

## imagenet_v2/topimages

*   **Versions**:

    *   **`0.1.1`** (default): No release notes.
