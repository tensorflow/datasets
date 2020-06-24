<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="opus" />
  <meta itemprop="description" content="OPUS is a collection of translated texts from the web.&#10;&#10;Create your own config to choose which data / language pair to load.&#10;&#10;```&#10;config = tfds.translate.opus.OpusConfig(&#10;    version=tfds.core.Version(&#x27;0.1.0&#x27;),&#10;    language_pair=(&quot;de&quot;, &quot;en&quot;),&#10;    subsets=[&quot;GNOME&quot;, &quot;EMEA&quot;]&#10;)&#10;builder = tfds.builder(&quot;opus&quot;, config=config)&#10;```&#10;&#10;medical documents&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;opus&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/opus" />
  <meta itemprop="sameAs" content="http://opus.nlpl.eu/" />
  <meta itemprop="citation" content="@inproceedings{Tiedemann2012ParallelData,&#10;  author = {Tiedemann, J},&#10;  title = {Parallel Data, Tools and Interfaces in OPUS},&#10;  booktitle = {LREC}&#10;  year = {2012}}" />
</div>

# `opus`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Homepage**: [http://opus.nlpl.eu/](http://opus.nlpl.eu/)
*   **Source code**:
    [`tfds.translate.opus.Opus`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/opus.py)
*   **Versions**:
    *   **`0.1.0`** (default): No release notes.
*   **Features**:

```python
Translation({
    'de': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('de', 'en')`
*   **Citation**:

```
@inproceedings{Tiedemann2012ParallelData,
  author = {Tiedemann, J},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {LREC}
  year = {2012}}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## opus/medical (default config)

*   **Description**:

OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```

medical documents

*   **Config description**: medical documents

*   **Download size**: `34.29 MiB`

*   **Dataset size**: `188.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 1,108,752

## opus/law

*   **Description**:

OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```

law documents

*   **Config description**: law documents

*   **Download size**: `46.99 MiB`

*   **Dataset size**: `214.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 719,372

## opus/koran

*   **Description**:

OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```

koran documents

*   **Config description**: koran documents

*   **Download size**: `35.42 MiB`

*   **Dataset size**: `117.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 537,128

## opus/IT

*   **Description**:

OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```

IT documents

*   **Config description**: IT documents

*   **Download size**: `10.33 MiB`

*   **Dataset size**: `42.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
'train' | 347,817

## opus/subtitles

*   **Description**:

OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```

subtitles documents

*   **Config description**: subtitles documents

*   **Download size**: `677.64 MiB`

*   **Dataset size**: `2.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | ---------:
'train' | 22,512,639
