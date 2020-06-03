<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="covid19sum" />
  <meta itemprop="description" content="CORD-19 is a resource of over 45,000 scholarly articles, including over 33,000&#10;with full text, about COVID-19, SARS-CoV-2, and related coronaviruses.&#10;&#10;To help organizing information in scientific literatures of COVID-19 through&#10;abstractive summarization. This dataset parse those articles to pairs of&#10;document and summaries of full_text-abstract or introduction-abstract.&#10;&#10;Features includes strings of: abstract, full_text, sha (hash of pdf),&#10;source_x (source of publication), title, doi (digital object identifier),&#10;license, authors, publish_time, journal, url.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;covid19sum&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/covid19sum" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge" />
  <meta itemprop="citation" content="@ONLINE {CORD-19-research-challenge,&#10;    author = &quot;An AI challenge with AI2, CZI, MSR, Georgetown, NIH &amp; The White House&quot;,&#10;    title  = &quot;COVID-19 Open Research Dataset Challenge (CORD-19)&quot;,&#10;    month  = &quot;april&quot;,&#10;    year   = &quot;2020&quot;,&#10;    url    = &quot;https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge&quot;&#10;}" />
</div>

# `covid19sum`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

Warning: Manual download required. See instructions below.

*   **Description**:

CORD-19 is a resource of over 45,000 scholarly articles, including over 33,000
with full text, about COVID-19, SARS-CoV-2, and related coronaviruses.

To help organizing information in scientific literatures of COVID-19 through
abstractive summarization. This dataset parse those articles to pairs of
document and summaries of full_text-abstract or introduction-abstract.

Features includes strings of: abstract, full_text, sha (hash of pdf), source_x
(source of publication), title, doi (digital object identifier), license,
authors, publish_time, journal, url.

*   **Homepage**:
    [https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
*   **Source code**:
    [`tfds.summarization.covid19sum.Covid19sum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/covid19sum.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Manual download instructions**: This dataset requires you to download the
    source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/manual/`):<br/>
    This dataset need to be manually downloaded through kaggle api:
    `kaggle datasets download allen-institute-for-ai/CORD-19-research-challenge`
    Place the downloaded zip file in the manual folder
    (defaults to ~/tensorflow_datasets/manual/).
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'abstract': tf.string,
    'authors': tf.string,
    'body_text': Sequence({
        'section': tf.string,
        'text': tf.string,
    }),
    'doi': tf.string,
    'journal': tf.string,
    'license': tf.string,
    'publish_time': tf.string,
    'sha': tf.string,
    'source_x': tf.string,
    'title': tf.string,
    'url': tf.string,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('body_text', 'abstract')`
*   **Citation**:

```
@ONLINE {CORD-19-research-challenge,
    author = "An AI challenge with AI2, CZI, MSR, Georgetown, NIH & The White House",
    title  = "COVID-19 Open Research Dataset Challenge (CORD-19)",
    month  = "april",
    year   = "2020",
    url    = "https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge"
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
