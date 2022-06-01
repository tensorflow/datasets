<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="pass" />
  <meta itemprop="description" content="PASS is a large-scale image dataset that does not include any humans,&#10;human parts, or other personally identifiable information.&#10;It that can be used for high-quality self-supervised pretraining while significantly reducing privacy concerns.&#10;&#10;PASS contains 1,439,589 images without any labels sourced from YFCC-100M.&#10;&#10;All images in this dataset are licenced under the CC-BY licence, as is the dataset itself.&#10;For YFCC-100M see  http://www.multimediacommons.org/.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;pass&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/pass" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/pass/" />
  <meta itemprop="citation" content="@Article{asano21pass,&#10;author = &quot;Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi&quot;,&#10;title = &quot;PASS: An ImageNet replacement for self-supervised pretraining without humans&quot;,&#10;journal = &quot;NeurIPS Track on Datasets and Benchmarks&quot;,&#10;year = &quot;2021&quot;&#10;}" />
</div>

# `pass`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=pass">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

PASS is a large-scale image dataset that does not include any humans, human
parts, or other personally identifiable information. It that can be used for
high-quality self-supervised pretraining while significantly reducing privacy
concerns.

PASS contains 1,439,589 images without any labels sourced from YFCC-100M.

All images in this dataset are licenced under the CC-BY licence, as is the
dataset itself. For YFCC-100M see http://www.multimediacommons.org/.

*   **Homepage**:
    [https://www.robots.ox.ac.uk/~vgg/data/pass/](https://www.robots.ox.ac.uk/~vgg/data/pass/)

*   **Source code**:
    [`tfds.image.pass_dataset.PASS`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/pass_dataset/pass_dataset.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `2.0.0`: v2: Removed 472 images from v1 as they contained humans. Also
        added metadata: datetaken and GPS.
    *   **`3.0.0`** (default): v3: Removed 131 images from v2 as they contained
        humans/tattos.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/creator_uname': Text(shape=(), dtype=tf.string),
    'image/date_taken': Text(shape=(), dtype=tf.string),
    'image/gps_lat': tf.float32,
    'image/gps_lon': tf.float32,
    'image/hash': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature             | Class        | Shape           | Dtype      | Description
:------------------ | :----------- | :-------------- | :--------- | :----------
                    | FeaturesDict |                 |            |
image               | Image        | (None, None, 3) | tf.uint8   |
image/creator_uname | Text         |                 | tf.string  |
image/date_taken    | Text         |                 | tf.string  |
image/gps_lat       | Tensor       |                 | tf.float32 |
image/gps_lon       | Tensor       |                 | tf.float32 |
image/hash          | Text         |                 | tf.string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@Article{asano21pass,
author = "Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi",
title = "PASS: An ImageNet replacement for self-supervised pretraining without humans",
journal = "NeurIPS Track on Datasets and Benchmarks",
year = "2021"
}
```

