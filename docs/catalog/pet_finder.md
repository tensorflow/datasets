<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="pet_finder" />
  <meta itemprop="description" content="Dataset with images from 5 classes (see config name for information on the specific class)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;pet_finder&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/pet_finder" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/petfinder-adoption-prediction/data" />
  <meta itemprop="citation" content="&#10;@ONLINE {kaggle-petfinder-adoption-prediction,&#10;    author = &quot;Kaggle and PetFinder.my&quot;,&#10;    title  = &quot;PetFinder.my Adoption Prediction&quot;,&#10;    month  = &quot;april&quot;,&#10;    year   = &quot;2019&quot;,&#10;    url    = &quot;https://www.kaggle.com/c/petfinder-adoption-prediction/data/&quot;&#10;}&#10;" />
</div>
# `pet_finder`

*   **Description**:

Dataset with images from 5 classes (see config name for information on the
specific class)

*   **Homepage**:
    [https://www.kaggle.com/c/petfinder-adoption-prediction/data](https://www.kaggle.com/c/petfinder-adoption-prediction/data)
*   **Source code**:
    [`tfds.image.pet_finder.PetFinder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/pet_finder.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `1.94 GiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 14,465
'train' | 58,311

*   **Features**:

```python
FeaturesDict({
    'PetID': Text(shape=(), dtype=tf.string),
    'attributes': FeaturesDict({
        'Age': Tensor(shape=(), dtype=tf.int64),
        'Breed1': Tensor(shape=(), dtype=tf.int64),
        'Breed2': Tensor(shape=(), dtype=tf.int64),
        'Color1': Tensor(shape=(), dtype=tf.int64),
        'Color2': Tensor(shape=(), dtype=tf.int64),
        'Color3': Tensor(shape=(), dtype=tf.int64),
        'Dewormed': Tensor(shape=(), dtype=tf.int64),
        'Fee': Tensor(shape=(), dtype=tf.int64),
        'FurLength': Tensor(shape=(), dtype=tf.int64),
        'Gender': Tensor(shape=(), dtype=tf.int64),
        'Health': Tensor(shape=(), dtype=tf.int64),
        'MaturitySize': Tensor(shape=(), dtype=tf.int64),
        'Quantity': Tensor(shape=(), dtype=tf.int64),
        'State': Tensor(shape=(), dtype=tf.int64),
        'Sterilized': Tensor(shape=(), dtype=tf.int64),
        'Type': Tensor(shape=(), dtype=tf.int64),
        'Vaccinated': Tensor(shape=(), dtype=tf.int64),
        'VideoAmt': Tensor(shape=(), dtype=tf.int64),
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=5),
})
```
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load)):
    `('attributes', 'label')`
*   **Citation**:

```
@ONLINE {kaggle-petfinder-adoption-prediction,
    author = "Kaggle and PetFinder.my",
    title  = "PetFinder.my Adoption Prediction",
    month  = "april",
    year   = "2019",
    url    = "https://www.kaggle.com/c/petfinder-adoption-prediction/data/"
}
```
