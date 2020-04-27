<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit" />
  <meta itemprop="description" content="This corpus contains preprocessed posts from the Reddit dataset.&#10;The dataset consists of 3,848,330 posts with an average length of 270 words for content,&#10;and 28 words for the summary.&#10;&#10;Features includes strings: author, body, normalizedBody, content, summary, subreddit, subreddit_id.&#10;Content is used as document and summary is used as summary.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;reddit&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit" />
  <meta itemprop="sameAs" content="https://github.com/webis-de/webis-tldr-17-corpus" />
  <meta itemprop="citation" content="@inproceedings{volske-etal-2017-tl,&#10;    title = &quot;{TL};{DR}: Mining {R}eddit to Learn Automatic Summarization&quot;,&#10;    author = {V{&quot;o}lske, Michael  and&#10;      Potthast, Martin  and&#10;      Syed, Shahbaz  and&#10;      Stein, Benno},&#10;    booktitle = &quot;Proceedings of the Workshop on New Frontiers in Summarization&quot;,&#10;    month = sep,&#10;    year = &quot;2017&quot;,&#10;    address = &quot;Copenhagen, Denmark&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/W17-4508&quot;,&#10;    doi = &quot;10.18653/v1/W17-4508&quot;,&#10;    pages = &quot;59--63&quot;,&#10;    abstract = &quot;Recent advances in automatic text summarization have used deep neural networks to generate high-quality abstractive summaries, but the performance of these models strongly depends on large amounts of suitable training data. We propose a new method for mining social media for author-provided summaries, taking advantage of the common practice of appending a {``}TL;DR{&#x27;&#x27;} to long posts. A case study using a large Reddit crawl yields the Webis-TLDR-17 dataset, complementing existing corpora primarily from the news genre. Our technique is likely applicable to other social media sites and general web crawls.&quot;,&#10;}" />
</div>
# `reddit`

*   **Description**:

This corpus contains preprocessed posts from the Reddit dataset. The dataset
consists of 3,848,330 posts with an average length of 270 words for content, and
28 words for the summary.

Features includes strings: author, body, normalizedBody, content, summary,
subreddit, subreddit_id. Content is used as document and summary is used as
summary.

*   **Homepage**:
    [https://github.com/webis-de/webis-tldr-17-corpus](https://github.com/webis-de/webis-tldr-17-corpus)
*   **Source code**:
    [`tfds.summarization.reddit.Reddit`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/reddit.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `2.93 GiB`
*   **Dataset size**: `18.09 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split   | Examples
:------ | --------:
'train' | 3,848,330

*   **Features**:

```python
FeaturesDict({
    'author': tf.string,
    'body': tf.string,
    'content': tf.string,
    'id': tf.string,
    'normalizedBody': tf.string,
    'subreddit': tf.string,
    'subreddit_id': tf.string,
    'summary': tf.string,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('content', 'summary')`
*   **Citation**:

```
@inproceedings{volske-etal-2017-tl,
    title = "{TL};{DR}: Mining {R}eddit to Learn Automatic Summarization",
    author = {V{"o}lske, Michael  and
      Potthast, Martin  and
      Syed, Shahbaz  and
      Stein, Benno},
    booktitle = "Proceedings of the Workshop on New Frontiers in Summarization",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W17-4508",
    doi = "10.18653/v1/W17-4508",
    pages = "59--63",
    abstract = "Recent advances in automatic text summarization have used deep neural networks to generate high-quality abstractive summaries, but the performance of these models strongly depends on large amounts of suitable training data. We propose a new method for mining social media for author-provided summaries, taking advantage of the common practice of appending a {``}TL;DR{''} to long posts. A case study using a large Reddit crawl yields the Webis-TLDR-17 dataset, complementing existing corpora primarily from the news genre. Our technique is likely applicable to other social media sites and general web crawls.",
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
