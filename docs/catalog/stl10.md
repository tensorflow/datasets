<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stl10" />
  <meta itemprop="description" content="The STL-10 dataset is an image recognition dataset for developing unsupervised&#10;feature learning, deep learning, self-taught learning algorithms. It is inspired&#10;by the CIFAR-10 dataset but with some modifications. In particular, each class&#10;has fewer labeled training examples than in CIFAR-10, but a very large set of &#10;unlabeled examples is provided to learn image models prior to supervised&#10;training. The primary challenge is to make use of the unlabeled data (which&#10;comes from a similar but different distribution from the labeled data) to build&#10;a useful prior. All images were acquired from labeled examples on ImageNet.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stl10&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stl10" />
  <meta itemprop="sameAs" content="http://ai.stanford.edu/~acoates/stl10/" />
  <meta itemprop="citation" content="@inproceedings{coates2011stl10,&#10;  title={{An Analysis of Single Layer Networks in Unsupervised Feature Learning}},&#10;  author={Coates, Adam and Ng, Andrew and Lee, Honglak},&#10;  booktitle={AISTATS},&#10;  year={2011},&#10;  note = {\url{https://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf}},&#10;}" />
</div>
# `stl10`

*   **Description**:

The STL-10 dataset is an image recognition dataset for developing unsupervised
feature learning, deep learning, self-taught learning algorithms. It is inspired
by the CIFAR-10 dataset but with some modifications. In particular, each class
has fewer labeled training examples than in CIFAR-10, but a very large set of
unlabeled examples is provided to learn image models prior to supervised
training. The primary challenge is to make use of the unlabeled data (which
comes from a similar but different distribution from the labeled data) to build
a useful prior. All images were acquired from labeled examples on ImageNet.

*   **Homepage**:
    [http://ai.stanford.edu/~acoates/stl10/](http://ai.stanford.edu/~acoates/stl10/)
*   **Source code**:
    [`tfds.image_classification.stl10.Stl10`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/stl10.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `2.46 GiB`
*   **Dataset size**: `1.86 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 8,000
'train'      | 5,000
'unlabelled' | 100,000

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(96, 96, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`
*   **Citation**:

```
@inproceedings{coates2011stl10,
  title={{An Analysis of Single Layer Networks in Unsupervised Feature Learning}},
  author={Coates, Adam and Ng, Andrew and Lee, Honglak},
  booktitle={AISTATS},
  year={2011},
  note = {\url{https://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf}},
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
