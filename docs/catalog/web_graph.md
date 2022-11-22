<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="web_graph" />
  <meta itemprop="description" content="This dataset contains a sparse graph representing web link structure for a&#10;small subset of the Web.&#10;&#10;Its a processed version of a single crawl performed by CommonCrawl in 2021&#10;where we strip everything and keep only the link-&gt;outlinks structure.&#10;The final dataset is basically int -&gt; List[int] format with each integer id&#10;representing a url.&#10;&#10;Also, in order to increase the value of this resource, we created 6 different&#10;version of WebGraph, each varying in the sparsity pattern and locale. We took&#10;the following processing steps, in order:&#10;&#10;- We started with WAT files from June 2021 crawl.&#10;- Since the outlinks in HTTP-Response-Metadata are stored as relative paths, we&#10;convert them to absolute paths using urllib after validating each link.&#10;- To study locale-specific graphs, we further filter based on 2 top level&#10;domains: ‘de’ and ‘in’, each producing a graph with an order of magnitude less&#10;number of nodes.&#10;- These graphs can still have arbitrary sparsity patterns and dangling links.&#10;Thus we further filter the nodes in each graph to have minimum of K ∈ [10, 50]&#10;inlinks and outlinks. Note that we only do this processing once, thus this is&#10;still an approximation i.e. the resulting graph might have nodes with less than&#10;K links.&#10;- Using both locale and count filters, we finalize 6 versions of WebGraph&#10;dataset, summarized in the folling table.&#10;&#10;| Version      | Top level domain | Min count | Num nodes | Num edges |&#10;| -----------  | ---------------- | --------- | --------- | --------- |&#10;| sparse       |                  | 10        | 365.4M    | 30B       |&#10;| dense        |                  | 50        | 136.5M    | 22B       |&#10;| de-sparse    | de               | 10        | 19.7M     | 1.19B     |&#10;| de-dense     | de               | 50        | 5.7M      | 0.82B     |&#10;| in-sparse    | in               | 10        | 1.5M      | 0.14B     |&#10;| in-dense     | in               | 50        | 0.5M      | 0.12B     |&#10;&#10;All versions of the dataset have following features:&#10;&#10;- &quot;row_tag&quot;: a unique identifier of the row (source link).&#10;- &quot;col_tag&quot;: a list of unique identifiers of non-zero columns (dest outlinks).&#10;- &quot;gt_tag&quot;: a list of unique identifiers of non-zero columns used as ground&#10;truth (dest outlinks), empty for train/train_t splits.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;web_graph&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/web_graph" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/2112.02194" />
  <meta itemprop="citation" content="@article{mehta2021alx,&#10;    title={ALX: Large Scale Matrix Factorization on TPUs},&#10;    author={Harsh Mehta and Steffen Rendle and Walid Krichene and Li Zhang},&#10;    year={2021},&#10;    eprint={2112.02194},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `web_graph`


*   **Description**:

This dataset contains a sparse graph representing web link structure for a small
subset of the Web.

Its a processed version of a single crawl performed by CommonCrawl in 2021 where
we strip everything and keep only the link->outlinks structure. The final
dataset is basically int -> List[int] format with each integer id representing a
url.

Also, in order to increase the value of this resource, we created 6 different
version of WebGraph, each varying in the sparsity pattern and locale. We took
the following processing steps, in order:

-   We started with WAT files from June 2021 crawl.
-   Since the outlinks in HTTP-Response-Metadata are stored as relative paths,
    we convert them to absolute paths using urllib after validating each link.
-   To study locale-specific graphs, we further filter based on 2 top level
    domains: ‘de’ and ‘in’, each producing a graph with an order of magnitude
    less number of nodes.
-   These graphs can still have arbitrary sparsity patterns and dangling links.
    Thus we further filter the nodes in each graph to have minimum of K ∈ [10,
    50] inlinks and outlinks. Note that we only do this processing once, thus
    this is still an approximation i.e. the resulting graph might have nodes
    with less than K links.
-   Using both locale and count filters, we finalize 6 versions of WebGraph
    dataset, summarized in the folling table.

Version   | Top level domain | Min count | Num nodes | Num edges
--------- | ---------------- | --------- | --------- | ---------
sparse    |                  | 10        | 365.4M    | 30B
dense     |                  | 50        | 136.5M    | 22B
de-sparse | de               | 10        | 19.7M     | 1.19B
de-dense  | de               | 50        | 5.7M      | 0.82B
in-sparse | in               | 10        | 1.5M      | 0.14B
in-dense  | in               | 50        | 0.5M      | 0.12B

All versions of the dataset have following features:

-   "row_tag": a unique identifier of the row (source link).
-   "col_tag": a list of unique identifiers of non-zero columns (dest outlinks).
-   "gt_tag": a list of unique identifiers of non-zero columns used as ground
    truth (dest outlinks), empty for train/train_t splits.

*   **Homepage**:
    [https://arxiv.org/abs/2112.02194](https://arxiv.org/abs/2112.02194)

*   **Source code**:
    [`tfds.structured.web_graph.WebGraph`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/web_graph/web_graph.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'col_tag': Sequence(int64),
    'gt_tag': Sequence(int64),
    'row_tag': int64,
})
```

*   **Feature documentation**:

Feature | Class            | Shape   | Dtype | Description
:------ | :--------------- | :------ | :---- | :----------
        | FeaturesDict     |         |       |
col_tag | Sequence(Tensor) | (None,) | int64 |
gt_tag  | Sequence(Tensor) | (None,) | int64 |
row_tag | Tensor           |         | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{mehta2021alx,
    title={ALX: Large Scale Matrix Factorization on TPUs},
    author={Harsh Mehta and Steffen Rendle and Walid Krichene and Li Zhang},
    year={2021},
    eprint={2112.02194},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```


## web_graph/sparse (default config)

*   **Config description**: WebGraph-sparse contains around 30B edges and around
    365M nodes.

*   **Dataset size**: `273.38 GiB`

*   **Splits**:

Split       | Examples
:---------- | ----------:
`'test'`    | 39,871,321
`'train'`   | 372,049,054
`'train_t'` | 410,867,007

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-sparse-1.0.0.html";
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

## web_graph/dense

*   **Config description**: WebGraph-dense contains around 22B edges and around
    136.5M nodes.

*   **Dataset size**: `170.87 GiB`

*   **Splits**:

Split       | Examples
:---------- | ----------:
`'test'`    | 13,256,496
`'train'`   | 122,815,749
`'train_t'` | 136,019,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-dense-1.0.0.html";
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

## web_graph/de-sparse

*   **Config description**: WebGraph-de-sparse contains around 1.19B edges and
    around 19.7M nodes.

*   **Dataset size**: `10.25 GiB`

*   **Splits**:

Split       | Examples
:---------- | ---------:
`'test'`    | 1,903,443
`'train'`   | 17,688,633
`'train_t'` | 19,566,045

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-de-sparse-1.0.0.html";
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

## web_graph/de-dense

*   **Config description**: WebGraph-de-dense contains around 0.82B edges and
    around 5.7M nodes.

*   **Dataset size**: `5.90 GiB`

*   **Splits**:

Split       | Examples
:---------- | --------:
`'test'`    | 553,270
`'train'`   | 5,118,902
`'train_t'` | 5,672,473

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-de-dense-1.0.0.html";
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

## web_graph/in-sparse

*   **Config description**: WebGraph-de-sparse contains around 0.14B edges and
    around 1.5M nodes.

*   **Dataset size**: `960.57 MiB`

*   **Splits**:

Split       | Examples
:---------- | --------:
`'test'`    | 140,313
`'train'`   | 1,309,063
`'train_t'` | 1,445,042

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-in-sparse-1.0.0.html";
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

## web_graph/in-dense

*   **Config description**: WebGraph-de-dense contains around 0.12B edges and
    around 0.5M nodes.

*   **Dataset size**: `711.72 MiB`

*   **Splits**:

Split       | Examples
:---------- | -------:
`'test'`    | 47,894
`'train'`   | 443,786
`'train_t'` | 491,634

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_graph-in-dense-1.0.0.html";
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