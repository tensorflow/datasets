<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cnn_dailymail" />
  <meta itemprop="description" content="CNN/DailyMail non-anonymized summarization dataset.&#10;&#10;There are two features:&#10;  - article: text of news article, used as the document to be summarized&#10;  - highlights: joined text of highlights with &lt;s&gt; and &lt;/s&gt; around each&#10;    highlight, which is the target summary&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cnn_dailymail&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cnn_dailymail" />
  <meta itemprop="sameAs" content="https://github.com/abisee/cnn-dailymail" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/SeeLM17,&#10;  author    = {Abigail See and&#10;               Peter J. Liu and&#10;               Christopher D. Manning},&#10;  title     = {Get To The Point: Summarization with Pointer-Generator Networks},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1704.04368},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1704.04368},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1704.04368},&#10;  timestamp = {Mon, 13 Aug 2018 16:46:08 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/SeeLM17},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;&#10;@inproceedings{hermann2015teaching,&#10;  title={Teaching machines to read and comprehend},&#10;  author={Hermann, Karl Moritz and Kocisky, Tomas and Grefenstette, Edward and Espeholt, Lasse and Kay, Will and Suleyman, Mustafa and Blunsom, Phil},&#10;  booktitle={Advances in neural information processing systems},&#10;  pages={1693--1701},&#10;  year={2015}&#10;}" />
</div>

# `cnn_dailymail`

*   **Description**:

CNN/DailyMail non-anonymized summarization dataset.

There are two features: - article: text of news article, used as the document to
be summarized - highlights: joined text of highlights with <s> and </s> around
each highlight, which is the target summary

*   **Homepage**:
    [https://github.com/abisee/cnn-dailymail](https://github.com/abisee/cnn-dailymail)

*   **Source code**:
    [`tfds.summarization.CnnDailymail`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/cnn_dailymail.py)

*   **Versions**:

    *   `1.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   `2.0.0`: Separate target sentences with newline. (Having the model
        predict newline separators makes it easier to evaluate using
        summary-level ROUGE.)

    *   `3.0.0`: Using cased version.

    *   **`3.1.0`** (default): Removed BuilderConfig

*   **Download size**: `558.32 MiB`

*   **Dataset size**: `1.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 11,490
`'train'`      | 287,113
`'validation'` | 13,368

*   **Features**:

```python
FeaturesDict({
    'article': Text(shape=(), dtype=tf.string),
    'highlights': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('article', 'highlights')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cnn_dailymail-3.1.0.html";
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

*   **Citation**:

```
@article{DBLP:journals/corr/SeeLM17,
  author    = {Abigail See and
               Peter J. Liu and
               Christopher D. Manning},
  title     = {Get To The Point: Summarization with Pointer-Generator Networks},
  journal   = {CoRR},
  volume    = {abs/1704.04368},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.04368},
  archivePrefix = {arXiv},
  eprint    = {1704.04368},
  timestamp = {Mon, 13 Aug 2018 16:46:08 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SeeLM17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

@inproceedings{hermann2015teaching,
  title={Teaching machines to read and comprehend},
  author={Hermann, Karl Moritz and Kocisky, Tomas and Grefenstette, Edward and Espeholt, Lasse and Kay, Will and Suleyman, Mustafa and Blunsom, Phil},
  booktitle={Advances in neural information processing systems},
  pages={1693--1701},
  year={2015}
}
```
