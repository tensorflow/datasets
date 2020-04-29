<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="samsum" />
  <meta itemprop="description" content="SAMSum Corpus contains over 16k chat dialogues with manually annotated&#10;summaries.&#10;&#10;There are two features:&#10;&#10;  - dialogue: text of dialogue.&#10;  - summary: human written summary of the dialogue.&#10;  - id: id of a example.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;samsum&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/samsum" />
  <meta itemprop="sameAs" content="https://arxiv.org/src/1911.12237v2/anc" />
  <meta itemprop="citation" content="@article{gliwa2019samsum,&#10;  title={SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization},&#10;  author={Gliwa, Bogdan and Mochol, Iwona and Biesek, Maciej and Wawer, Aleksander},&#10;  journal={arXiv preprint arXiv:1911.12237},&#10;  year={2019}&#10;}" />
</div>
# `samsum`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

Warning: Manual download required. See instructions below.

*   **Description**:

SAMSum Corpus contains over 16k chat dialogues with manually annotated
summaries.

There are two features:

-   dialogue: text of dialogue.
-   summary: human written summary of the dialogue.
-   id: id of a example.

*   **Homepage**:
    [https://arxiv.org/src/1911.12237v2/anc](https://arxiv.org/src/1911.12237v2/anc)

*   **Source code**:
    [`tfds.summarization.samsum.Samsum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/samsum.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to download the
    source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/manual/`):<br/>
    Download https://arxiv.org/src/1911.12237v2/anc/corpus.7z, decompress and
    place train.json, val.json and test.json in the manual follder.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'dialogue': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'summary': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('dialogue', 'summary')`
*   **Citation**:

```
@article{gliwa2019samsum,
  title={SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization},
  author={Gliwa, Bogdan and Mochol, Iwona and Biesek, Maciej and Wawer, Aleksander},
  journal={arXiv preprint arXiv:1911.12237},
  year={2019}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
