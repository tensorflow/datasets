<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="voxceleb" />
  <meta itemprop="description" content="An large scale dataset for speaker identification. This data is collected from&#10;over 1,251 speakers, with over 150k samples in total.&#10;This release contains the audio part of the voxceleb1.1 dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;voxceleb&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/voxceleb" />
  <meta itemprop="sameAs" content="http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html" />
  <meta itemprop="citation" content="@InProceedings{Nagrani17,&#10; author       = &quot;Nagrani, A. and Chung, J.~S. and Zisserman, A.&quot;,&#10; title        = &quot;VoxCeleb: a large-scale speaker identification dataset&quot;,&#10; booktitle    = &quot;INTERSPEECH&quot;,&#10;    year         = &quot;2017&quot;,&#10;}" />
</div>

# `voxceleb`

Warning: Manual download required. See instructions below.

*   **Description**:

An large scale dataset for speaker identification. This data is collected from
over 1,251 speakers, with over 150k samples in total. This release contains the
audio part of the voxceleb1.1 dataset.

*   **Homepage**:
    [http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html)
*   **Source code**:
    [`tfds.audio.voxceleb.Voxceleb`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/voxceleb.py)
*   **Versions**:
    *   **`1.1.1`** (default): No release notes.
*   **Download size**: `4.68 MiB`
*   **Dataset size**: `107.97 GiB`
*   **Manual download instructions**: This dataset requires you to download the
    source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/manual/`):<br/>
    manual_dir should contain the file vox_dev_wav.zip. The instructions for
    downloading this file are found in http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html. This dataset requires registration.
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 7,972
'train'      | 134,000
'validation' | 6,670

*   **Features**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1252),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'label')`
*   **Citation**:

```
@InProceedings{Nagrani17,
    author       = "Nagrani, A. and Chung, J.~S. and Zisserman, A.",
    title        = "VoxCeleb: a large-scale speaker identification dataset",
    booktitle    = "INTERSPEECH",
    year         = "2017",
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
