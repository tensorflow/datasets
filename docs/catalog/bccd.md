<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bccd" />
  <meta itemprop="description" content="BCCD Dataset is a small-scale dataset for blood cells detection.&#10;&#10;Thanks the original data and annotations from cosmicad and akshaylamba.&#10;The original dataset is re-organized into VOC format.&#10;BCCD Dataset is under MIT licence.&#10;&#10;Data preparation is important to use machine learning.&#10;In this project, the Faster R-CNN algorithm from keras-frcnn for Object Detection is used.&#10;From this dataset, nicolaschen1 developed two Python scripts to make&#10;preparation data (CSV file and images) for recognition of abnormalities&#10;in blood cells on medical images.&#10;&#10;export.py: it creates the file &quot;test.csv&quot; with all data needed: filename, class_name, x1,y1,x2,y2.&#10;plot.py: it plots the boxes for each image and save it in a new directory.&#10;&#10;Image Type : jpeg(JPEG)&#10;Width x Height : 640 x 480&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bccd&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bccd" />
  <meta itemprop="sameAs" content="https://github.com/Shenggan/BCCD_Dataset" />
  <meta itemprop="citation" content="@ONLINE {BCCD_Dataset,&#10;    author = &quot;Shenggan&quot;,&#10;    title  = &quot;BCCD Dataset&quot;,&#10;    year   = &quot;2017&quot;,&#10;    url    = &quot;https://github.com/Shenggan/BCCD_Dataset&quot;&#10;}" />
</div>

# `bccd`

*   **Description**:

BCCD Dataset is a small-scale dataset for blood cells detection.

Thanks the original data and annotations from cosmicad and akshaylamba. The
original dataset is re-organized into VOC format. BCCD Dataset is under MIT
licence.

Data preparation is important to use machine learning. In this project, the
Faster R-CNN algorithm from keras-frcnn for Object Detection is used. From this
dataset, nicolaschen1 developed two Python scripts to make preparation data (CSV
file and images) for recognition of abnormalities in blood cells on medical
images.

export.py: it creates the file "test.csv" with all data needed: filename,
class_name, x1,y1,x2,y2. plot.py: it plots the boxes for each image and save it
in a new directory.

Image Type : jpeg(JPEG) Width x Height : 640 x 480

*   **Homepage**:
    [https://github.com/Shenggan/BCCD_Dataset](https://github.com/Shenggan/BCCD_Dataset)

*   **Source code**:
    [`tfds.image.bccd.BCCD`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/bccd/bccd.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

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
    'image': Image(shape=(480, 640, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'objects': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@ONLINE {BCCD_Dataset,
    author = "Shenggan",
    title  = "BCCD Dataset",
    year   = "2017",
    url    = "https://github.com/Shenggan/BCCD_Dataset"
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.
