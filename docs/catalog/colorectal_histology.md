<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="colorectal_histology" />
  <meta itemprop="description" content="Classification of textures in colorectal cancer histology. Each example is a 150 x 150 x 3 RGB image of one of 8 classes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;colorectal_histology&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/colorectal_histology" />
  <meta itemprop="sameAs" content="https://zenodo.org/record/53169#.XGZemKwzbmG" />
  <meta itemprop="citation" content="@article{kather2016multi,&#10;  title={Multi-class texture analysis in colorectal cancer histology},&#10;  author={Kather, Jakob Nikolas and Weis, Cleo-Aron and Bianconi, Francesco and Melchers, Susanne M and Schad, Lothar R and Gaiser, Timo and Marx, Alexander and Z{&quot;o}llner, Frank Gerrit},&#10;  journal={Scientific reports},&#10;  volume={6},&#10;  pages={27988},&#10;  year={2016},&#10;  publisher={Nature Publishing Group}&#10;}" />
</div>
# `colorectal_histology`

*   **Description**:

Classification of textures in colorectal cancer histology. Each example is a 150
x 150 x 3 RGB image of one of 8 classes.

*   **Homepage**:
    [https://zenodo.org/record/53169#.XGZemKwzbmG](https://zenodo.org/record/53169#.XGZemKwzbmG)
*   **Source code**:
    [`tfds.image_classification.colorectal_histology.ColorectalHistology`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/colorectal_histology.py)
*   **Versions**:
    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)
*   **Download size**: `246.14 MiB`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 5,000

*   **Features**:

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(150, 150, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=8),
})
```
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`
*   **Citation**:

```
@article{kather2016multi,
  title={Multi-class texture analysis in colorectal cancer histology},
  author={Kather, Jakob Nikolas and Weis, Cleo-Aron and Bianconi, Francesco and Melchers, Susanne M and Schad, Lothar R and Gaiser, Timo and Marx, Alexander and Z{"o}llner, Frank Gerrit},
  journal={Scientific reports},
  volume={6},
  pages={27988},
  year={2016},
  publisher={Nature Publishing Group}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:

<img src="https://storage.googleapis.com/tfds-data/visualization/colorectal_histology-2.0.0.png" alt="Visualization" width="500px">
