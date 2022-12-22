<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scientific_papers" />
  <meta itemprop="description" content="Scientific papers datasets contains two sets of long and structured documents.&#10;The datasets are obtained from ArXiv and PubMed OpenAccess repositories.&#10;&#10;Both &quot;arxiv&quot; and &quot;pubmed&quot; have two features:&#10;&#10;-   article: the body of the document, pagragraphs seperated by &quot;/n&quot;.&#10;-   abstract: the abstract of the document, pagragraphs seperated by &quot;/n&quot;.&#10;-   section_names: titles of sections, seperated by &quot;/n&quot;.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;scientific_papers&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scientific_papers" />
  <meta itemprop="sameAs" content="https://github.com/armancohan/long-summarization" />
  <meta itemprop="citation" content="@article{Cohan_2018,&#10;   title={A Discourse-Aware Attention Model for Abstractive Summarization of&#10;            Long Documents},&#10;   url={http://dx.doi.org/10.18653/v1/n18-2097},&#10;   DOI={10.18653/v1/n18-2097},&#10;   journal={Proceedings of the 2018 Conference of the North American Chapter of&#10;          the Association for Computational Linguistics: Human Language&#10;          Technologies, Volume 2 (Short Papers)},&#10;   publisher={Association for Computational Linguistics},&#10;   author={Cohan, Arman and Dernoncourt, Franck and Kim, Doo Soon and Bui, Trung and Kim, Seokhwan and Chang, Walter and Goharian, Nazli},&#10;   year={2018}&#10;}" />
</div>

# `scientific_papers`


*   **Description**:

Scientific papers datasets contains two sets of long and structured documents.
The datasets are obtained from ArXiv and PubMed OpenAccess repositories.

Both "arxiv" and "pubmed" have two features:

-   article: the body of the document, pagragraphs seperated by "/n".
-   abstract: the abstract of the document, pagragraphs seperated by "/n".
-   section_names: titles of sections, seperated by "/n".

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/arxiv-summarization-dataset">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/armancohan/long-summarization](https://github.com/armancohan/long-summarization)

*   **Source code**:
    [`tfds.datasets.scientific_papers.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/scientific_papers/scientific_papers_dataset_builder.py)

*   **Versions**:

    *   `1.1.0`: No release notes.
    *   **`1.1.1`** (default): No release notes.

*   **Download size**: `4.20 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=string),
    'article': Text(shape=(), dtype=string),
    'section_names': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape | Dtype  | Description
:------------ | :----------- | :---- | :----- | :----------
              | FeaturesDict |       |        |
abstract      | Text         |       | string |
article       | Text         |       | string |
section_names | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('article', 'abstract')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{Cohan_2018,
   title={A Discourse-Aware Attention Model for Abstractive Summarization of
            Long Documents},
   url={http://dx.doi.org/10.18653/v1/n18-2097},
   DOI={10.18653/v1/n18-2097},
   journal={Proceedings of the 2018 Conference of the North American Chapter of
          the Association for Computational Linguistics: Human Language
          Technologies, Volume 2 (Short Papers)},
   publisher={Association for Computational Linguistics},
   author={Cohan, Arman and Dernoncourt, Franck and Kim, Doo Soon and Bui, Trung and Kim, Seokhwan and Chang, Walter and Goharian, Nazli},
   year={2018}
}
```


## scientific_papers/arxiv (default config)

*   **Config description**: Documents from ArXiv repository.

*   **Dataset size**: `7.07 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,440
`'train'`      | 203,037
`'validation'` | 6,436

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scientific_papers-arxiv-1.1.1.html";
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

## scientific_papers/pubmed

*   **Config description**: Documents from PubMed repository.

*   **Dataset size**: `2.34 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,658
`'train'`      | 119,924
`'validation'` | 6,633

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scientific_papers-pubmed-1.1.1.html";
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