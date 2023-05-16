<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit" />
  <meta itemprop="description" content="This corpus contains preprocessed posts from the Reddit dataset. The dataset&#10;consists of 3,848,330 posts with an average length of 270 words for content, and&#10;28 words for the summary.&#10;&#10;Features includes strings: author, body, normalizedBody, content, summary,&#10;subreddit, subreddit_id. Content is used as document and summary is used as&#10;summary.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;reddit&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit" />
  <meta itemprop="sameAs" content="https://github.com/webis-de/webis-tldr-17-corpus" />
  <meta itemprop="citation" content="@inproceedings{volske-etal-2017-tl,&#10;    title = &quot;{TL};{DR}: Mining {R}eddit to Learn Automatic Summarization&quot;,&#10;    author = {V{\&quot;o}lske, Michael  and&#10;      Potthast, Martin  and&#10;      Syed, Shahbaz  and&#10;      Stein, Benno},&#10;    booktitle = &quot;Proceedings of the Workshop on New Frontiers in Summarization&quot;,&#10;    month = sep,&#10;    year = &quot;2017&quot;,&#10;    address = &quot;Copenhagen, Denmark&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/W17-4508&quot;,&#10;    doi = &quot;10.18653/v1/W17-4508&quot;,&#10;    pages = &quot;59--63&quot;,&#10;    abstract = &quot;Recent advances in automatic text summarization have used deep neural networks to generate high-quality abstractive summaries, but the performance of these models strongly depends on large amounts of suitable training data. We propose a new method for mining social media for author-provided summaries, taking advantage of the common practice of appending a {``}TL;DR{&#x27;&#x27;} to long posts. A case study using a large Reddit crawl yields the Webis-TLDR-17 dataset, complementing existing corpora primarily from the news genre. Our technique is likely applicable to other social media sites and general web crawls.&quot;,&#10;}" />
</div>

# `reddit`


*   **Description**:

This corpus contains preprocessed posts from the Reddit dataset. The dataset
consists of 3,848,330 posts with an average length of 270 words for content, and
28 words for the summary.

Features includes strings: author, body, normalizedBody, content, summary,
subreddit, subreddit_id. Content is used as document and summary is used as
summary.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/reddit">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/webis-de/webis-tldr-17-corpus](https://github.com/webis-de/webis-tldr-17-corpus)

*   **Source code**:
    [`tfds.datasets.reddit.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/reddit/reddit_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `2.93 GiB`

*   **Dataset size**: `18.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,848,330

*   **Feature structure**:

```python
FeaturesDict({
    'author': string,
    'body': string,
    'content': string,
    'id': string,
    'normalizedBody': string,
    'subreddit': string,
    'subreddit_id': string,
    'summary': string,
})
```

*   **Feature documentation**:

Feature        | Class        | Shape | Dtype  | Description
:------------- | :----------- | :---- | :----- | :----------
               | FeaturesDict |       |        |
author         | Tensor       |       | string |
body           | Tensor       |       | string |
content        | Tensor       |       | string |
id             | Tensor       |       | string |
normalizedBody | Tensor       |       | string |
subreddit      | Tensor       |       | string |
subreddit_id   | Tensor       |       | string |
summary        | Tensor       |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('content', 'summary')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{volske-etal-2017-tl,
    title = "{TL};{DR}: Mining {R}eddit to Learn Automatic Summarization",
    author = {V{\"o}lske, Michael  and
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

