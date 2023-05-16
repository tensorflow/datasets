<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="booksum" />
  <meta itemprop="description" content="BookSum: A Collection of Datasets for Long-form Narrative Summarization&#10;&#10;This implementation currently only supports book and chapter summaries.&#10;&#10;GitHub: https://github.com/salesforce/booksum&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;booksum&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/booksum" />
  <meta itemprop="sameAs" content="https://github.com/salesforce/booksum" />
  <meta itemprop="citation" content="@article{kryscinski2021booksum,&#10;      title={BookSum: A Collection of Datasets for Long-form Narrative Summarization},&#10;      author={Wojciech Kry{\&#x27;s}ci{\&#x27;n}ski and Nazneen Rajani and Divyansh Agarwal and Caiming Xiong and Dragomir Radev},&#10;      year={2021},&#10;      eprint={2105.08209},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}" />
</div>

# `booksum`


Warning: Manual download required. See instructions below.

*   **Description**:

BookSum: A Collection of Datasets for Long-form Narrative Summarization

This implementation currently only supports book and chapter summaries.

GitHub: https://github.com/salesforce/booksum

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/booksum">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/salesforce/booksum](https://github.com/salesforce/booksum)

*   **Source code**:
    [`tfds.datasets.booksum.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/booksum/booksum_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    1) Go to https://github.com/salesforce/booksum, and run steps 1-3. Place the
    whole `booksum` git project in the manual folder.
    2) Download the chapterized books from https://storage.cloud.google.com/sfr-books-dataset-chapters-research/all_chapterized_books.zip
    and unzip to the manual folder.

The manual folder should contain the following directories:

```
- `booksum/`
- `all_chapterized_books/`
```

Note: Because the BookSum dataset is based on the availability of web-scraped
data and may be incomplete, the `_generate_examples` method will automatically
skip missing entries.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Feature structure**:

```python
FeaturesDict({
    'document': Text(shape=(), dtype=string),
    'summary': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype  | Description
:------- | :----------- | :---- | :----- | :----------
         | FeaturesDict |       |        |
document | Text         |       | string |
summary  | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('document', 'summary')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{kryscinski2021booksum,
      title={BookSum: A Collection of Datasets for Long-form Narrative Summarization},
      author={Wojciech Kry{\'s}ci{\'n}ski and Nazneen Rajani and Divyansh Agarwal and Caiming Xiong and Dragomir Radev},
      year={2021},
      eprint={2105.08209},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


## booksum/book (default config)

*   **Config description**: Book-level summarization

*   **Dataset size**: `208.81 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 46
`'train'`      | 312
`'validation'` | 45

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/booksum-book-1.0.0.html";
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

## booksum/chapter

*   **Config description**: chapter-level summarization

*   **Dataset size**: `216.71 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,083
`'train'`      | 6,524
`'validation'` | 891

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/booksum-chapter-1.0.0.html";
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