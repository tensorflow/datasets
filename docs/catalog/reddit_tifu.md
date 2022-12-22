<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit_tifu" />
  <meta itemprop="description" content="Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu. As defined in&#10;the publication, style &quot;short&quot; uses title as summary and &quot;long&quot; uses tldr as&#10;summary.&#10;&#10;Features includes:&#10;&#10;  - document: post text without tldr.&#10;  - tldr: tldr line.&#10;  - title: trimmed title without tldr.&#10;  - ups: upvotes.&#10;  - score: score.&#10;  - num_comments: number of comments.&#10;  - upvote_ratio: upvote ratio.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;reddit_tifu&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit_tifu" />
  <meta itemprop="sameAs" content="https://github.com/ctr4si/MMN" />
  <meta itemprop="citation" content="@misc{kim2018abstractive,&#10;    title={Abstractive Summarization of Reddit Posts with Multi-level Memory Networks},&#10;    author={Byeongchang Kim and Hyunwoo Kim and Gunhee Kim},&#10;    year={2018},&#10;    eprint={1811.00783},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `reddit_tifu`


*   **Description**:

Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu. As defined in
the publication, style "short" uses title as summary and "long" uses tldr as
summary.

Features includes:

-   document: post text without tldr.
-   tldr: tldr line.
-   title: trimmed title without tldr.
-   ups: upvotes.
-   score: score.
-   num_comments: number of comments.
-   upvote_ratio: upvote ratio.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/reddit-tifu">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://github.com/ctr4si/MMN](https://github.com/ctr4si/MMN)

*   **Source code**:
    [`tfds.datasets.reddit_tifu.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/reddit_tifu/reddit_tifu_dataset_builder.py)

*   **Versions**:

    *   `1.1.0`: Remove empty document and summary strings.
    *   `1.1.1`: Add train, dev and test (80/10/10) splits which are used in
        PEGASUS (https://arxiv.org/abs/1912.08777) in a separate config. These
        were created randomly using the tfds split function and are being
        released to ensure that results on Reddit Tifu Long are reproducible and
        comparable.Also add `id` to the datapoints.
    *   **`1.1.2`** (default): Corrected splits uploaded.

*   **Feature structure**:

```python
FeaturesDict({
    'documents': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'num_comments': float32,
    'score': float32,
    'title': Text(shape=(), dtype=string),
    'tldr': Text(shape=(), dtype=string),
    'ups': float32,
    'upvote_ratio': float32,
})
```

*   **Feature documentation**:

Feature      | Class        | Shape | Dtype   | Description
:----------- | :----------- | :---- | :------ | :----------
             | FeaturesDict |       |         |
documents    | Text         |       | string  |
id           | Text         |       | string  |
num_comments | Tensor       |       | float32 |
score        | Tensor       |       | float32 |
title        | Text         |       | string  |
tldr         | Text         |       | string  |
ups          | Tensor       |       | float32 |
upvote_ratio | Tensor       |       | float32 |

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

*   **Download size**: `639.54 MiB`

*   **Dataset size**: `141.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

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
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit_tifu-short-1.1.2.html";
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

## reddit_tifu/long

*   **Config description**: Using TLDR as summary.

*   **Download size**: `639.54 MiB`

*   **Dataset size**: `93.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

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
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit_tifu-long-1.1.2.html";
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

## reddit_tifu/long_split

*   **Config description**: Using TLDR as summary and return train/test/dev
    splits.

*   **Download size**: `639.94 MiB`

*   **Dataset size**: `93.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,214
`'train'`      | 33,711
`'validation'` | 4,214

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('documents', 'tldr')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/reddit_tifu-long_split-1.1.2.html";
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