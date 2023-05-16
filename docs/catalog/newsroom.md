<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="newsroom" />
  <meta itemprop="description" content="NEWSROOM is a large dataset for training and evaluating summarization systems.&#10;It contains 1.3 million articles and summaries written by authors and editors in&#10;the newsrooms of 38 major publications.&#10;&#10;Dataset features includes:&#10;&#10;- text: Input news text.&#10;- summary: Summary for the news.&#10;&#10;And additional features:&#10;&#10;- title: news title.&#10;- url: url of the news.&#10;- date: date of the article.&#10;- density: extractive density.&#10;- coverage: extractive coverage.&#10;- compression: compression ratio.&#10;- density_bin: low, medium, high.&#10;- coverage_bin: extractive, abstractive.&#10;- compression_bin: low, medium, high.&#10;&#10;This dataset can be downloaded upon requests. Unzip all the contents&#10;&quot;train.jsonl, dev.jsonl, test.jsonl&quot; to the tfds folder.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;newsroom&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/newsroom" />
  <meta itemprop="sameAs" content="https://summari.es" />
  <meta itemprop="citation" content="@article{Grusky_2018,&#10;   title={Newsroom: A Dataset of 1.3 Million Summaries with Diverse Extractive Strategies},&#10;   url={http://dx.doi.org/10.18653/v1/n18-1065},&#10;   DOI={10.18653/v1/n18-1065},&#10;   journal={Proceedings of the 2018 Conference of the North American Chapter of&#10;          the Association for Computational Linguistics: Human Language&#10;          Technologies, Volume 1 (Long Papers)},&#10;   publisher={Association for Computational Linguistics},&#10;   author={Grusky, Max and Naaman, Mor and Artzi, Yoav},&#10;   year={2018}&#10;}" />
</div>

# `newsroom`


Warning: Manual download required. See instructions below.

*   **Description**:

NEWSROOM is a large dataset for training and evaluating summarization systems.
It contains 1.3 million articles and summaries written by authors and editors in
the newsrooms of 38 major publications.

Dataset features includes:

-   text: Input news text.
-   summary: Summary for the news.

And additional features:

-   title: news title.
-   url: url of the news.
-   date: date of the article.
-   density: extractive density.
-   coverage: extractive coverage.
-   compression: compression ratio.
-   density_bin: low, medium, high.
-   coverage_bin: extractive, abstractive.
-   compression_bin: low, medium, high.

This dataset can be downloaded upon requests. Unzip all the contents
"train.jsonl, dev.jsonl, test.jsonl" to the tfds folder.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/newsroom">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://summari.es](https://summari.es)

*   **Source code**:
    [`tfds.datasets.newsroom.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/newsroom/newsroom_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `5.13 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    You should download the dataset from https://summari.es/download/
    The webpage requires registration.
    After downloading, please put dev.jsonl, test.jsonl and train.jsonl
    files in the manual_dir.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 108,862
`'train'`      | 995,041
`'validation'` | 108,837

*   **Feature structure**:

```python
FeaturesDict({
    'compression': float32,
    'compression_bin': Text(shape=(), dtype=string),
    'coverage': float32,
    'coverage_bin': Text(shape=(), dtype=string),
    'date': Text(shape=(), dtype=string),
    'density': float32,
    'density_bin': Text(shape=(), dtype=string),
    'summary': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype   | Description
:-------------- | :----------- | :---- | :------ | :----------
                | FeaturesDict |       |         |
compression     | Tensor       |       | float32 |
compression_bin | Text         |       | string  |
coverage        | Tensor       |       | float32 |
coverage_bin    | Text         |       | string  |
date            | Text         |       | string  |
density         | Tensor       |       | float32 |
density_bin     | Text         |       | string  |
summary         | Text         |       | string  |
text            | Text         |       | string  |
title           | Text         |       | string  |
url             | Text         |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'summary')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/newsroom-1.0.0.html";
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
@article{Grusky_2018,
   title={Newsroom: A Dataset of 1.3 Million Summaries with Diverse Extractive Strategies},
   url={http://dx.doi.org/10.18653/v1/n18-1065},
   DOI={10.18653/v1/n18-1065},
   journal={Proceedings of the 2018 Conference of the North American Chapter of
          the Association for Computational Linguistics: Human Language
          Technologies, Volume 1 (Long Papers)},
   publisher={Association for Computational Linguistics},
   author={Grusky, Max and Naaman, Mor and Artzi, Yoav},
   year={2018}
}
```

