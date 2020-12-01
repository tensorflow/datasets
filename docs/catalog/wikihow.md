<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikihow" />
  <meta itemprop="description" content="WikiHow is a new large-scale dataset using the online WikiHow&#10;(http://www.wikihow.com/) knowledge base.&#10;&#10;There are two features:&#10;  - text: wikihow answers texts.&#10;  - headline: bold lines as summary.&#10;&#10;There are two separate versions:&#10;  - all: consisting of the concatenation of all paragraphs as the articles and&#10;         the bold lines as the reference summaries.&#10;  - sep: consisting of each paragraph and its summary.&#10;&#10;Download &quot;wikihowAll.csv&quot; and &quot;wikihowSep.csv&quot; from&#10;https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder&#10;https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.&#10;Train/validation/test splits are provided by the authors.&#10;Preprocessing is applied to remove short articles&#10;(abstract length &lt; 0.75 article length) and clean up extra commas.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikihow&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikihow" />
  <meta itemprop="sameAs" content="https://github.com/mahnazkoupaee/WikiHow-Dataset" />
  <meta itemprop="citation" content="@misc{koupaee2018wikihow,&#10;    title={WikiHow: A Large Scale Text Summarization Dataset},&#10;    author={Mahnaz Koupaee and William Yang Wang},&#10;    year={2018},&#10;    eprint={1810.09305},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `wikihow`

Warning: Manual download required. See instructions below.

*   **Description**:

WikiHow is a new large-scale dataset using the online WikiHow
(http://www.wikihow.com/) knowledge base.

There are two features: - text: wikihow answers texts. - headline: bold lines as
summary.

There are two separate versions: - all: consisting of the concatenation of all
paragraphs as the articles and the bold lines as the reference summaries. - sep:
consisting of each paragraph and its summary.

Download "wikihowAll.csv" and "wikihowSep.csv" from
https://github.com/mahnazkoupaee/WikiHow-Dataset and place them in manual folder
https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig.
Train/validation/test splits are provided by the authors. Preprocessing is
applied to remove short articles (abstract length < 0.75 article length) and
clean up extra commas.

*   **Homepage**:
    [https://github.com/mahnazkoupaee/WikiHow-Dataset](https://github.com/mahnazkoupaee/WikiHow-Dataset)

*   **Source code**:
    [`tfds.summarization.Wikihow`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/wikihow.py)

*   **Versions**:

    *   **`1.2.0`** (default): No release notes.

*   **Download size**: `5.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Links to files can be found on https://github.com/mahnazkoupaee/WikiHow-Dataset
    Please download both wikihowAll.csv and wikihowSep.csv.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'headline')`

*   **Citation**:

```
@misc{koupaee2018wikihow,
    title={WikiHow: A Large Scale Text Summarization Dataset},
    author={Mahnaz Koupaee and William Yang Wang},
    year={2018},
    eprint={1810.09305},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## wikihow/all (default config)

*   **Config description**: Use the concatenation of all paragraphs as the
    articles and the bold lines as the reference summaries

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 5,577
`'train'`      | 157,252
`'validation'` | 5,599

*   **Features**:

```python
FeaturesDict({
    'headline': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikihow-all-1.2.0.html";
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

## wikihow/sep

*   **Config description**: use each paragraph and its summary.

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 37,800
`'train'`      | 1,060,732
`'validation'` | 37,932

*   **Features**:

```python
FeaturesDict({
    'headline': Text(shape=(), dtype=tf.string),
    'overview': Text(shape=(), dtype=tf.string),
    'sectionLabel': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikihow-sep-1.2.0.html";
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