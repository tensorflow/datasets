<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="voxforge" />
  <meta itemprop="description" content="VoxForge is a language classification dataset. It consists of user submitted&#10;audio clips submitted to the website. In this release, data from 6 languages&#10;is collected - English, Spanish, French, German, Russian, and Italian.&#10;Since the website is constantly updated, and for the sake of reproducibility,&#10;this release contains only recordings submitted prior to 2020-01-01.&#10;The samples are splitted between train, validation and testing so that samples&#10;from each speaker belongs to exactly one split.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;voxforge&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/voxforge" />
  <meta itemprop="sameAs" content="http://www.voxforge.org/" />
  <meta itemprop="citation" content="@article{maclean2018voxforge,&#10;  title={Voxforge},&#10;  author={MacLean, Ken},&#10;  journal={Ken MacLean.[Online]. Available: http://www.voxforge.org/home.[Acedido em 2012]},&#10;  year={2018}&#10;}" />
</div>

# `voxforge`

Warning: Manual download required. See instructions below.

*   **Description**:

VoxForge is a language classification dataset. It consists of user submitted
audio clips submitted to the website. In this release, data from 6 languages is
collected - English, Spanish, French, German, Russian, and Italian. Since the
website is constantly updated, and for the sake of reproducibility, this release
contains only recordings submitted prior to 2020-01-01. The samples are splitted
between train, validation and testing so that samples from each speaker belongs
to exactly one split.

*   **Homepage**: [http://www.voxforge.org/](http://www.voxforge.org/)

*   **Source code**:
    [`tfds.audio.Voxforge`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/voxforge.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    VoxForge requires manual download of the audio archives. The complete list of
    archives can be found in https://storage.googleapis.com/tfds-data/downloads/voxforge/voxforge_urls.txt. It can be downloaded using the following command:
    wget -i voxforge_urls.txt -x
    Note that downloading and building the dataset locally requires ~100GB disk
    space (but only ~60GB will be used permanently).

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    'speaker_id': tf.string,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{maclean2018voxforge,
  title={Voxforge},
  author={MacLean, Ken},
  journal={Ken MacLean.[Online]. Available: http://www.voxforge.org/home.[Acedido em 2012]},
  year={2018}
}
```
