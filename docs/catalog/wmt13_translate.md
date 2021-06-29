<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt13_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wmt13_translate&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt13_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt13/translation-task.html" />
  <meta itemprop="citation" content="@InProceedings{bojar-EtAl:2013:WMT,&#10;  author    = {Bojar, Ondrej  and  Buck, Christian  and  Callison-Burch, Chris  and  Federmann, Christian  and  Haddow, Barry  and  Koehn, Philipp  and  Monz, Christof  and  Post, Matt  and  Soricut, Radu  and  Specia, Lucia},&#10;  title     = {Findings of the 2013 {Workshop on Statistical Machine Translation}},&#10;  booktitle = {Proceedings of the Eighth Workshop on Statistical Machine Translation},&#10;  month     = {August},&#10;  year      = {2013},&#10;  address   = {Sofia, Bulgaria},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {1--44},&#10;  url       = {http://www.aclweb.org/anthology/W13-2201}&#10;}" />
</div>

# `wmt13_translate`


Warning: Manual download required. See instructions below.

*   **Description**:

Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.

```
config = tfds.translate.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        tfds.Split.TRAIN: ["commoncrawl_frde"],
        tfds.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = tfds.builder("wmt_translate", config=config)
```

*   **Homepage**:
    [http://www.statmt.org/wmt13/translation-task.html](http://www.statmt.org/wmt13/translation-task.html)

*   **Source code**:
    [`tfds.translate.Wmt13Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt13.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Some of the wmt configs here, require a manual download.
    Please look into wmt.py to see the exact path (and file name) that has to
    be downloaded.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@InProceedings{bojar-EtAl:2013:WMT,
  author    = {Bojar, Ondrej  and  Buck, Christian  and  Callison-Burch, Chris  and  Federmann, Christian  and  Haddow, Barry  and  Koehn, Philipp  and  Monz, Christof  and  Post, Matt  and  Soricut, Radu  and  Specia, Lucia},
  title     = {Findings of the 2013 {Workshop on Statistical Machine Translation}},
  booktitle = {Proceedings of the Eighth Workshop on Statistical Machine Translation},
  month     = {August},
  year      = {2013},
  address   = {Sofia, Bulgaria},
  publisher = {Association for Computational Linguistics},
  pages     = {1--44},
  url       = {http://www.aclweb.org/anthology/W13-2201}
}
```

## wmt13_translate/cs-en (default config)

*   **Config description**: WMT 2013 cs-en translation task dataset.

*   **Download size**: `1.59 GiB`

*   **Dataset size**: `2.89 GiB`

*   **Splits**:

Split          | Examples
:------------- | ---------:
`'test'`       | 3,000
`'train'`      | 15,780,759
`'validation'` | 13,573

*   **Features**:

```python
Translation({
    'cs': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('cs', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt13_translate-cs-en-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## wmt13_translate/de-en

*   **Config description**: WMT 2013 de-en translation task dataset.

*   **Download size**: `1.59 GiB`

*   **Dataset size**: `1.36 GiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 3,000
`'train'`      | 4,485,758
`'validation'` | 13,573

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

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt13_translate-de-en-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## wmt13_translate/fr-en

*   **Config description**: WMT 2013 fr-en translation task dataset.

*   **Download size**: `6.21 GiB`

*   **Dataset size**: `14.64 GiB`

*   **Splits**:

Split          | Examples
:------------- | ---------:
`'test'`       | 3,000
`'train'`      | 40,810,860
`'validation'` | 13,573

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'fr': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('fr', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt13_translate-fr-en-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## wmt13_translate/es-en

*   **Config description**: WMT 2013 es-en translation task dataset.

*   **Download size**: `3.79 GiB`

*   **Dataset size**: `5.24 GiB`

*   **Splits**:

Split          | Examples
:------------- | ---------:
`'test'`       | 3,000
`'train'`      | 15,176,790
`'validation'` | 13,573

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'es': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('es', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt13_translate-es-en-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## wmt13_translate/ru-en

*   **Config description**: WMT 2013 ru-en translation task dataset.

*   **Download size**: `1010.20 MiB`

*   **Dataset size**: `833.67 MiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 3,000
`'train'`      | 2,471,670
`'validation'` | 3,003

*   **Features**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('ru', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt13_translate-ru-en-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->