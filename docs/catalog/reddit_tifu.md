<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit_tifu" />
  <meta itemprop="description" content="Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu.&#10;As defined in the publication, styel &quot;short&quot; uses title as summary and&#10;&quot;long&quot; uses tldr as summary.&#10;&#10;Features includes:&#10;  - document: post text without tldr.&#10;  - tldr: tldr line.&#10;  - title: trimmed title without tldr.&#10;  - ups: upvotes.&#10;  - score: score.&#10;  - num_comments: number of comments.&#10;  - upvote_ratio: upvote ratio.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;reddit_tifu&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit_tifu" />
  <meta itemprop="sameAs" content="https://github.com/ctr4si/MMN" />
  <meta itemprop="citation" content="@misc{kim2018abstractive,&#10;    title={Abstractive Summarization of Reddit Posts with Multi-level Memory Networks},&#10;    author={Byeongchang Kim and Hyunwoo Kim and Gunhee Kim},&#10;    year={2018},&#10;    eprint={1811.00783},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `reddit_tifu`

*   **Description**:

Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu. As defined in
the publication, styel "short" uses title as summary and "long" uses tldr as
summary.

Features includes: - document: post text without tldr. - tldr: tldr line. -
title: trimmed title without tldr. - ups: upvotes. - score: score. -
num_comments: number of comments. - upvote_ratio: upvote ratio.

*   **Homepage**: [https://github.com/ctr4si/MMN](https://github.com/ctr4si/MMN)

*   **Source code**:
    [`tfds.summarization.RedditTifu`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/reddit_tifu.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Download size**: `639.54 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Features**:

```python
FeaturesDict({
    'documents': Text(shape=(), dtype=tf.string),
    'num_comments': tf.float32,
    'score': tf.float32,
    'title': Text(shape=(), dtype=tf.string),
    'tldr': Text(shape=(), dtype=tf.string),
    'ups': tf.float32,
    'upvote_ratio': tf.float32,
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{kim2018abstractive,
    title={Abstractive Summarization of Reddit Posts with Multi-level Memory Networks},
    author={Byeongchang Kim and Hyunwoo Kim and Gunhee Kim},
    year={2018},
    eprint={1811.00783},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## reddit_tifu/short (default config)

*   **Config description**: Using title as summary.

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,740

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('documents', 'title')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit_tifu-short-1.1.0.html";
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

## reddit_tifu/long

*   **Config description**: Using TLDR as summary.

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,139

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('documents', 'tldr')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit_tifu-long-1.1.0.html";
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