<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dementiabank" />
  <meta itemprop="description" content="DementiaBank is a medical domain task. It contains 117 people diagnosed with&#10;Alzheimer Disease, and 93 healthy people, reading a description of an image, and&#10;the task is to classify these groups.&#10;This release contains only the audio part of this dataset, without the text&#10;features.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dementiabank&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dementiabank" />
  <meta itemprop="sameAs" content="https://dementia.talkbank.org/" />
  <meta itemprop="citation" content="@article{boller2005dementiabank,&#10;  title={Dementiabank database guide},&#10;  author={Boller, Francois and Becker, James},&#10;  journal={University of Pittsburgh},&#10;  year={2005}&#10;}" />
</div>
# `dementiabank`

Warning: Manual download required. See instructions below.

*   **Description**:

DementiaBank is a medical domain task. It contains 117 people diagnosed with
Alzheimer Disease, and 93 healthy people, reading a description of an image, and
the task is to classify these groups. This release contains only the audio part
of this dataset, without the text features.

*   **Homepage**:
    [https://dementia.talkbank.org/](https://dementia.talkbank.org/)
*   **Source code**:
    [`tfds.audio.dementiabank.Dementiabank`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/dementiabank.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `Unknown size`
*   **Dataset size**: `17.71 GiB`
*   **Manual download instructions**: This dataset requires you to download the
    source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/manual/`):<br/>
    manual dir should contain 2 folders with mp3 files:

*   dementia/English/Pitt/Control/cookie

*   dementia/English/Pitt/Dementia/cookie

Which were downloaded from https://media.talkbank.org/dementia/English/Pitt/
This dataset requires registration for downloading. * **Auto-cached**
([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
No * **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 102
'train'      | 393
'validation' | 57

*   **Features**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'speaker_id': tf.string,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'label')`
*   **Citation**:

```
@article{boller2005dementiabank,
  title={Dementiabank database guide},
  author={Boller, Francois and Becker, James},
  journal={University of Pittsburgh},
  year={2005}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
