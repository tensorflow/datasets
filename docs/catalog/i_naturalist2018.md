<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="i_naturalist2018" />
  <meta itemprop="description" content="There are a total of 8,142 species in the dataset, with 437,513 training images,&#10;and 24,426 validation images. Each image has one ground truth label.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;i_naturalist2018&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/i_naturalist2018" />
  <meta itemprop="sameAs" content="https://github.com/visipedia/inat_comp/tree/master/2018" />
  <meta itemprop="citation" content="\&#10;@misc{inaturalist18,&#10;    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2018}},&#10;    Title = {{iNaturalist} 2018 competition dataset.},&#10;    Year = {2018},&#10;    key = {{iNaturalist} 2018 competition dataset},&#10;    }" />
</div>

# `i_naturalist2018`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

There are a total of 8,142 species in the dataset, with 437,513 training images,
and 24,426 validation images. Each image has one ground truth label.

*   **Homepage**:
    [https://github.com/visipedia/inat_comp/tree/master/2018](https://github.com/visipedia/inat_comp/tree/master/2018)

*   **Source code**:
    [`tfds.image_classification.i_naturalist2018.INaturalist2018`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/i_naturalist2018/i_naturalist2018.py)

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
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=8142),
    'supercategory': ClassLabel(shape=(), dtype=tf.int64, num_classes=14),
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
@misc{inaturalist18,
    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2018}},
    Title = {{iNaturalist} 2018 competition dataset.},
    Year = {2018},
    key = {{iNaturalist} 2018 competition dataset},
    }
```
