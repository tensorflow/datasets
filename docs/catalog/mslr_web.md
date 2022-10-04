<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mslr_web" />
  <meta itemprop="description" content="MSLR-WEB are two large-scale Learning-to-Rank datasets released by Microsoft&#10;Research. The first dataset (called &quot;30k&quot;) contains 30,000 queries and the&#10;second dataset (called &quot;10k&quot;) contains 10,000 queries. Each dataset consists of&#10;query-document pairs represented as feature vectors and corresponding relevance&#10;judgment labels.&#10;&#10;You can specify whether to use the &quot;10k&quot; or &quot;30k&quot; version of the dataset, and a&#10;corresponding fold, as follows:&#10;&#10;```python&#10;ds = tfds.load(&quot;mslr_web/30k_fold1&quot;)&#10;```&#10;&#10;If only `mslr_web` is specified, the `mslr_web/10k_fold1` option is selected by&#10;default:&#10;&#10;```python&#10;# This is the same as `tfds.load(&quot;mslr_web/10k_fold1&quot;)`&#10;ds = tfds.load(&quot;mslr_web&quot;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mslr_web&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mslr_web" />
  <meta itemprop="sameAs" content="https://www.microsoft.com/en-us/research/project/mslr/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/QinL13,&#10;  author    = {Tao Qin and Tie{-}Yan Liu},&#10;  title     = {Introducing {LETOR} 4.0 Datasets},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1306.2597},&#10;  year      = {2013},&#10;  url       = {http://arxiv.org/abs/1306.2597},&#10;  timestamp = {Mon, 01 Jul 2013 20:31:25 +0200},&#10;  biburl    = {http://dblp.uni-trier.de/rec/bib/journals/corr/QinL13},&#10;  bibsource = {dblp computer science bibliography, http://dblp.org}&#10;}" />
</div>

# `mslr_web`


*   **Description**:

MSLR-WEB are two large-scale Learning-to-Rank datasets released by Microsoft
Research. The first dataset (called "30k") contains 30,000 queries and the
second dataset (called "10k") contains 10,000 queries. Each dataset consists of
query-document pairs represented as feature vectors and corresponding relevance
judgment labels.

You can specify whether to use the "10k" or "30k" version of the dataset, and a
corresponding fold, as follows:

```python
ds = tfds.load("mslr_web/30k_fold1")
```

If only `mslr_web` is specified, the `mslr_web/10k_fold1` option is selected by
default:

```python
# This is the same as `tfds.load("mslr_web/10k_fold1")`
ds = tfds.load("mslr_web")
```

*   **Homepage**:
    [https://www.microsoft.com/en-us/research/project/mslr/](https://www.microsoft.com/en-us/research/project/mslr/)

*   **Source code**:
    [`tfds.ranking.mslr_web.MslrWeb`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/ranking/mslr_web/mslr_web.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.1.0`** (default): Bundle features into a single 'float_features'
        feature.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'float_features': Tensor(shape=(None, 136), dtype=tf.float64),
    'label': Tensor(shape=(None,), dtype=tf.float64),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype      | Description
:------------- | :----------- | :---------- | :--------- | :----------
               | FeaturesDict |             |            |
float_features | Tensor       | (None, 136) | tf.float64 |
label          | Tensor       | (None,)     | tf.float64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{DBLP:journals/corr/QinL13,
  author    = {Tao Qin and Tie{-}Yan Liu},
  title     = {Introducing {LETOR} 4.0 Datasets},
  journal   = {CoRR},
  volume    = {abs/1306.2597},
  year      = {2013},
  url       = {http://arxiv.org/abs/1306.2597},
  timestamp = {Mon, 01 Jul 2013 20:31:25 +0200},
  biburl    = {http://dblp.uni-trier.de/rec/bib/journals/corr/QinL13},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
```


## mslr_web/10k_fold1 (default config)

*   **Download size**: `1.15 GiB`

*   **Dataset size**: `307.64 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-10k_fold1-1.1.0.html";
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

## mslr_web/10k_fold2

*   **Download size**: `1.15 GiB`

*   **Dataset size**: `307.64 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-10k_fold2-1.1.0.html";
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

## mslr_web/10k_fold3

*   **Download size**: `1.15 GiB`

*   **Dataset size**: `307.64 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-10k_fold3-1.1.0.html";
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

## mslr_web/10k_fold4

*   **Download size**: `1.15 GiB`

*   **Dataset size**: `307.64 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-10k_fold4-1.1.0.html";
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

## mslr_web/10k_fold5

*   **Download size**: `1.15 GiB`

*   **Dataset size**: `307.64 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-10k_fold5-1.1.0.html";
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

## mslr_web/30k_fold1

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `956.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,306
`'train'` | 18,919
`'vali'`  | 6,306

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-30k_fold1-1.1.0.html";
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

## mslr_web/30k_fold2

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `956.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,307
`'train'` | 18,918
`'vali'`  | 6,306

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-30k_fold2-1.1.0.html";
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

## mslr_web/30k_fold3

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `956.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,306
`'train'` | 18,918
`'vali'`  | 6,307

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-30k_fold3-1.1.0.html";
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

## mslr_web/30k_fold4

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `956.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,306
`'train'` | 18,919
`'vali'`  | 6,306

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-30k_fold4-1.1.0.html";
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

## mslr_web/30k_fold5

*   **Download size**: `3.59 GiB`

*   **Dataset size**: `956.41 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,306
`'train'` | 18,919
`'vali'`  | 6,306

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mslr_web-30k_fold5-1.1.0.html";
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