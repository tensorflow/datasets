<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gov_report" />
  <meta itemprop="description" content="Government report dataset consists of reports written by government research&#10; agencies including Congressional Research Service and U.S. Government&#10; Accountability Office.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gov_report&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gov_report" />
  <meta itemprop="sameAs" content="https://gov-report-data.github.io/" />
  <meta itemprop="citation" content="@inproceedings{&#10;anonymous2022efficiently,&#10;title={Efficiently Modeling Long Sequences with Structured State Spaces},&#10;author={Anonymous},&#10;booktitle={Submitted to The Tenth International Conference on Learning Representations },&#10;year={2022},&#10;url={https://openreview.net/forum?id=uYLFoz1vlAC},&#10;note={under review}&#10;}" />
</div>

# `gov_report`


*   **Description**:

Government report dataset consists of reports written by government research
agencies including Congressional Research Service and U.S. Government
Accountability Office.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/govreport">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://gov-report-data.github.io/](https://gov-report-data.github.io/)

*   **Source code**:
    [`tfds.summarization.gov_report.GovReport`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/gov_report/gov_report.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `320.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{
anonymous2022efficiently,
title={Efficiently Modeling Long Sequences with Structured State Spaces},
author={Anonymous},
booktitle={Submitted to The Tenth International Conference on Learning Representations },
year={2022},
url={https://openreview.net/forum?id=uYLFoz1vlAC},
note={under review}
}
```


## gov_report/crs_whitespace (default config)

*   **Config description**: CRS report with summary. Structures flattened and
    joined by whitespace. This is the format used by original paper

*   **Dataset size**: `349.76 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 362
`'train'`      | 6,514
`'validation'` | 362

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'reports': Text(shape=(), dtype=string),
    'summary': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape | Dtype  | Description
:------------ | :----------- | :---- | :----- | :----------
              | FeaturesDict |       |        |
id            | Text         |       | string |
released_date | Text         |       | string |
reports       | Text         |       | string |
summary       | Text         |       | string |
title         | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('reports', 'summary')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-crs_whitespace-1.0.0.html";
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

## gov_report/gao_whitespace

*   **Config description**: GAO report with highlight Structures flattened and
    joined by whitespace. This is the format used by original paper

*   **Dataset size**: `690.24 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 611
`'train'`      | 11,005
`'validation'` | 612

*   **Feature structure**:

```python
FeaturesDict({
    'fastfact': Text(shape=(), dtype=string),
    'highlight': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'published_date': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'report': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape | Dtype  | Description
:------------- | :----------- | :---- | :----- | :----------
               | FeaturesDict |       |        |
fastfact       | Text         |       | string |
highlight      | Text         |       | string |
id             | Text         |       | string |
published_date | Text         |       | string |
released_date  | Text         |       | string |
report         | Text         |       | string |
title          | Text         |       | string |
url            | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('report', 'highlight')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-gao_whitespace-1.0.0.html";
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

## gov_report/crs_html

*   **Config description**: CRS report with summary. Structures flattened and
    joined by newline while add html tags. Tags are only added for
    secition_title in a format like `<h2>xxx<h2>`.

*   **Dataset size**: `351.25 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 362
`'train'`      | 6,514
`'validation'` | 362

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'reports': Text(shape=(), dtype=string),
    'summary': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape | Dtype  | Description
:------------ | :----------- | :---- | :----- | :----------
              | FeaturesDict |       |        |
id            | Text         |       | string |
released_date | Text         |       | string |
reports       | Text         |       | string |
summary       | Text         |       | string |
title         | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('reports', 'summary')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-crs_html-1.0.0.html";
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

## gov_report/gao_html

*   **Config description**: GAO report with highlight Structures flattened and
    joined by newline while add html tags. Tags are only added for
    secition_title in a format like `<h2>xxx<h2>`.

*   **Dataset size**: `692.72 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 611
`'train'`      | 11,005
`'validation'` | 612

*   **Feature structure**:

```python
FeaturesDict({
    'fastfact': Text(shape=(), dtype=string),
    'highlight': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'published_date': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'report': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape | Dtype  | Description
:------------- | :----------- | :---- | :----- | :----------
               | FeaturesDict |       |        |
fastfact       | Text         |       | string |
highlight      | Text         |       | string |
id             | Text         |       | string |
published_date | Text         |       | string |
released_date  | Text         |       | string |
report         | Text         |       | string |
title          | Text         |       | string |
url            | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('report', 'highlight')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-gao_html-1.0.0.html";
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

## gov_report/crs_json

*   **Config description**: CRS report with summary. Structures represented as
    raw json.

*   **Dataset size**: `361.92 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 362
`'train'`      | 6,514
`'validation'` | 362

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'reports': Text(shape=(), dtype=string),
    'summary': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape | Dtype  | Description
:------------ | :----------- | :---- | :----- | :----------
              | FeaturesDict |       |        |
id            | Text         |       | string |
released_date | Text         |       | string |
reports       | Text         |       | string |
summary       | Text         |       | string |
title         | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('reports', 'summary')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-crs_json-1.0.0.html";
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

## gov_report/gao_json

*   **Config description**: GAO report with highlight Structures represented as
    raw json.

*   **Dataset size**: `712.82 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 611
`'train'`      | 11,005
`'validation'` | 612

*   **Feature structure**:

```python
FeaturesDict({
    'fastfact': Text(shape=(), dtype=string),
    'highlight': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'published_date': Text(shape=(), dtype=string),
    'released_date': Text(shape=(), dtype=string),
    'report': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape | Dtype  | Description
:------------- | :----------- | :---- | :----- | :----------
               | FeaturesDict |       |        |
fastfact       | Text         |       | string |
highlight      | Text         |       | string |
id             | Text         |       | string |
published_date | Text         |       | string |
released_date  | Text         |       | string |
report         | Text         |       | string |
title          | Text         |       | string |
url            | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('report', 'highlight')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gov_report-gao_json-1.0.0.html";
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