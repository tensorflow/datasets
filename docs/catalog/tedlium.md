<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tedlium" />
  <meta itemprop="description" content="The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled&#10;at 16kHz. It contains about 118 hours of speech.&#10;&#10;This is the TED-LIUM corpus release 1,&#10;licensed under Creative Commons BY-NC-ND 3.0&#10;(http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tedlium&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tedlium" />
  <meta itemprop="sameAs" content="https://www.openslr.org/7/" />
  <meta itemprop="citation" content="@inproceedings{rousseau2012tedlium,&#10;  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus.},&#10;  author={Rousseau, Anthony and Del{\&#x27;e}glise, Paul and Est{\`e}ve, Yannick},&#10;  booktitle={Conference on Language Resources and Evaluation (LREC)},&#10;  pages={125--129},&#10;  year={2012}&#10;}" />
</div>
# `tedlium`

*   **Description**:

The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled
at 16kHz. It contains about 118 hours of speech.

This is the TED-LIUM corpus release 1, licensed under Creative Commons BY-NC-ND
3.0 (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

*   **Homepage**: [https://www.openslr.org/7/](https://www.openslr.org/7/)
*   **Source code**:
    [`tfds.audio.tedlium.Tedlium`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/tedlium.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `19.82 GiB`
*   **Dataset size**: `39.23 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,469
'train'      | 56,803
'validation' | 591

*   **Features**:

```python
FeaturesDict({
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'id': tf.string,
    'speaker_id': tf.string,
    'speech': Audio(shape=(None,), dtype=tf.int64),
    'text': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('speech', 'text')`
*   **Citation**:

```
@inproceedings{rousseau2012tedlium,
  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus.},
  author={Rousseau, Anthony and Del{\'e}glise, Paul and Est{\`e}ve, Yannick},
  booktitle={Conference on Language Resources and Evaluation (LREC)},
  pages={125--129},
  year={2012}
}
```
