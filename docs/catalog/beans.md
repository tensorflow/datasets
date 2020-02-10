<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="beans" />
  <meta itemprop="description" content="Beans is a dataset of images of beans taken in the field using smartphone&#10;cameras. It consists of 3 classes: 2 disease classes and the healthy class.&#10;Diseases depicted include Angular Leaf Spot and Bean Rust. Data was annotated&#10;by experts from the National Crops Resources Research Institute (NaCRRI) in&#10;Uganda and collected by the Makerere AI research lab.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;beans&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/beans" />
  <meta itemprop="sameAs" content="https://github.com/AI-Lab-Makerere/ibean/" />
  <meta itemprop="citation" content="@ONLINE {beansdata,&#10;    author=&quot;Makerere AI Lab&quot;,&#10;    title=&quot;Bean disease dataset&quot;,&#10;    month=&quot;January&quot;,&#10;    year=&quot;2020&quot;,&#10;    url=&quot;https://github.com/AI-Lab-Makerere/ibean/&quot;&#10;}&#10;" />
</div>
# `beans`

Beans is a dataset of images of beans taken in the field using smartphone
cameras. It consists of 3 classes: 2 disease classes and the healthy class.
Diseases depicted include Angular Leaf Spot and Bean Rust. Data was annotated by
experts from the National Crops Resources Research Institute (NaCRRI) in Uganda
and collected by the Makerere AI research lab.

*   URL:
    [https://github.com/AI-Lab-Makerere/ibean/](https://github.com/AI-Lab-Makerere/ibean/)
*   `DatasetBuilder`:
    [`tfds.image.beans.Beans`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/beans.py)
*   Version: `v0.1.0`
*   Versions:

    *   **`0.1.0`** (default):

*   Size: `171.63 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(500, 500, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 1,295
TRAIN      | 1,034
VALIDATION | 133
TEST       | 128

## Homepage

*   [https://github.com/AI-Lab-Makerere/ibean/](https://github.com/AI-Lab-Makerere/ibean/)

## Supervised keys (for `as_supervised=True`)
`('image', 'label')`

## Citation
```
@ONLINE {beansdata,
    author="Makerere AI Lab",
    title="Bean disease dataset",
    month="January",
    year="2020",
    url="https://github.com/AI-Lab-Makerere/ibean/"
}
```

--------------------------------------------------------------------------------
