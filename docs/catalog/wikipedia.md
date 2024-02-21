<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia" />
  <meta itemprop="description" content="Wikipedia dataset containing cleaned articles of all languages.&#10;The datasets are built from the Wikipedia dump&#10;(https://dumps.wikimedia.org/) with one split per language. Each example&#10;contains the content of one full Wikipedia article with cleaning to strip&#10;markdown and unwanted sections (references, etc.).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikipedia&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia" />
  <meta itemprop="sameAs" content="https://dumps.wikimedia.org" />
  <meta itemprop="citation" content="@ONLINE {wikidump,&#10;    author = &quot;Wikimedia Foundation&quot;,&#10;    title  = &quot;Wikimedia Downloads&quot;,&#10;    url    = &quot;https://dumps.wikimedia.org&quot;&#10;}" />
</div>

# `wikipedia`


*   **Description**:

Wikipedia dataset containing cleaned articles of all languages. The datasets are
built from the Wikipedia dump (https://dumps.wikimedia.org/) with one split per
language. Each example contains the content of one full Wikipedia article with
cleaning to strip markdown and unwanted sections (references, etc.).

*   **Homepage**: [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

*   **Source code**:
    [`tfds.text.Wikipedia`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia.py)

*   **Versions**:

    *   **`1.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Feature structure**:

```python
FeaturesDict({
    'text': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype  | Description
:------ | :----------- | :---- | :----- | :----------
        | FeaturesDict |       |        |
text    | Text         |       | string |
title   | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@ONLINE {wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
```


## wikipedia/20230201.aa (default config)

*   **Config description**: Wikipedia dataset for aa, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

## wikipedia/20230201.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ab-1.0.0.html";
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

## wikipedia/20230201.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ace-1.0.0.html";
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

## wikipedia/20230201.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ady-1.0.0.html";
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

## wikipedia/20230201.af

*   **Config description**: Wikipedia dataset for af, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.af-1.0.0.html";
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

## wikipedia/20230201.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ak-1.0.0.html";
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

## wikipedia/20230201.als

*   **Config description**: Wikipedia dataset for als, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.als-1.0.0.html";
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

## wikipedia/20230201.am

*   **Config description**: Wikipedia dataset for am, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.am-1.0.0.html";
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

## wikipedia/20230201.an

*   **Config description**: Wikipedia dataset for an, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.an-1.0.0.html";
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

## wikipedia/20230201.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ang-1.0.0.html";
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

## wikipedia/20230201.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ar-1.0.0.html";
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

## wikipedia/20230201.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.arc-1.0.0.html";
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

## wikipedia/20230201.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.arz-1.0.0.html";
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

## wikipedia/20230201.as

*   **Config description**: Wikipedia dataset for as, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.as-1.0.0.html";
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

## wikipedia/20230201.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ast-1.0.0.html";
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

## wikipedia/20230201.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.atj-1.0.0.html";
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

## wikipedia/20230201.av

*   **Config description**: Wikipedia dataset for av, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.av-1.0.0.html";
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

## wikipedia/20230201.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ay-1.0.0.html";
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

## wikipedia/20230201.az

*   **Config description**: Wikipedia dataset for az, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.az-1.0.0.html";
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

## wikipedia/20230201.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.azb-1.0.0.html";
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

## wikipedia/20230201.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

## wikipedia/20230201.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bar-1.0.0.html";
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

## wikipedia/20230201.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bcl-1.0.0.html";
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

## wikipedia/20230201.be

*   **Config description**: Wikipedia dataset for be, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.be-1.0.0.html";
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

## wikipedia/20230201.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bg-1.0.0.html";
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

## wikipedia/20230201.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bh-1.0.0.html";
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

## wikipedia/20230201.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bi-1.0.0.html";
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

## wikipedia/20230201.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bjn-1.0.0.html";
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

## wikipedia/20230201.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bm-1.0.0.html";
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

## wikipedia/20230201.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bn-1.0.0.html";
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

## wikipedia/20230201.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bo-1.0.0.html";
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

## wikipedia/20230201.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bpy-1.0.0.html";
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

## wikipedia/20230201.br

*   **Config description**: Wikipedia dataset for br, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.br-1.0.0.html";
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

## wikipedia/20230201.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bs-1.0.0.html";
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

## wikipedia/20230201.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bug-1.0.0.html";
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

## wikipedia/20230201.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.bxr-1.0.0.html";
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

## wikipedia/20230201.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ca-1.0.0.html";
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

## wikipedia/20230201.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cdo-1.0.0.html";
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

## wikipedia/20230201.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ce-1.0.0.html";
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

## wikipedia/20230201.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ceb-1.0.0.html";
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

## wikipedia/20230201.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ch-1.0.0.html";
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

## wikipedia/20230201.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cho-1.0.0.html";
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

## wikipedia/20230201.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.chr-1.0.0.html";
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

## wikipedia/20230201.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.chy-1.0.0.html";
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

## wikipedia/20230201.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ckb-1.0.0.html";
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

## wikipedia/20230201.co

*   **Config description**: Wikipedia dataset for co, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.co-1.0.0.html";
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

## wikipedia/20230201.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cr-1.0.0.html";
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

## wikipedia/20230201.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.crh-1.0.0.html";
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

## wikipedia/20230201.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cs-1.0.0.html";
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

## wikipedia/20230201.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.csb-1.0.0.html";
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

## wikipedia/20230201.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cu-1.0.0.html";
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

## wikipedia/20230201.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cv-1.0.0.html";
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

## wikipedia/20230201.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.cy-1.0.0.html";
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

## wikipedia/20230201.da

*   **Config description**: Wikipedia dataset for da, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.da-1.0.0.html";
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

## wikipedia/20230201.de

*   **Config description**: Wikipedia dataset for de, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.de-1.0.0.html";
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

## wikipedia/20230201.din

*   **Config description**: Wikipedia dataset for din, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.din-1.0.0.html";
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

## wikipedia/20230201.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.diq-1.0.0.html";
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

## wikipedia/20230201.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.dsb-1.0.0.html";
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

## wikipedia/20230201.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.dty-1.0.0.html";
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

## wikipedia/20230201.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.dv-1.0.0.html";
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

## wikipedia/20230201.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.dz-1.0.0.html";
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

## wikipedia/20230201.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ee-1.0.0.html";
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

## wikipedia/20230201.el

*   **Config description**: Wikipedia dataset for el, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.el-1.0.0.html";
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

## wikipedia/20230201.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.eml-1.0.0.html";
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

## wikipedia/20230201.en

*   **Config description**: Wikipedia dataset for en, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.en-1.0.0.html";
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

## wikipedia/20230201.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.eo-1.0.0.html";
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

## wikipedia/20230201.es

*   **Config description**: Wikipedia dataset for es, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.es-1.0.0.html";
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

## wikipedia/20230201.et

*   **Config description**: Wikipedia dataset for et, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.et-1.0.0.html";
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

## wikipedia/20230201.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.eu-1.0.0.html";
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

## wikipedia/20230201.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ext-1.0.0.html";
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

## wikipedia/20230201.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fa-1.0.0.html";
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

## wikipedia/20230201.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ff-1.0.0.html";
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

## wikipedia/20230201.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fi-1.0.0.html";
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

## wikipedia/20230201.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fj-1.0.0.html";
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

## wikipedia/20230201.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fo-1.0.0.html";
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

## wikipedia/20230201.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fr-1.0.0.html";
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

## wikipedia/20230201.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.frp-1.0.0.html";
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

## wikipedia/20230201.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.frr-1.0.0.html";
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

## wikipedia/20230201.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fur-1.0.0.html";
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

## wikipedia/20230201.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.fy-1.0.0.html";
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

## wikipedia/20230201.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ga-1.0.0.html";
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

## wikipedia/20230201.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gag-1.0.0.html";
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

## wikipedia/20230201.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gan-1.0.0.html";
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

## wikipedia/20230201.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gd-1.0.0.html";
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

## wikipedia/20230201.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gl-1.0.0.html";
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

## wikipedia/20230201.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.glk-1.0.0.html";
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

## wikipedia/20230201.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gn-1.0.0.html";
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

## wikipedia/20230201.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gom-1.0.0.html";
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

## wikipedia/20230201.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gor-1.0.0.html";
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

## wikipedia/20230201.got

*   **Config description**: Wikipedia dataset for got, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.got-1.0.0.html";
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

## wikipedia/20230201.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gu-1.0.0.html";
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

## wikipedia/20230201.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.gv-1.0.0.html";
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

## wikipedia/20230201.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ha-1.0.0.html";
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

## wikipedia/20230201.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.hak-1.0.0.html";
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

## wikipedia/20230201.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.haw-1.0.0.html";
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

## wikipedia/20230201.he

*   **Config description**: Wikipedia dataset for he, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.he-1.0.0.html";
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

## wikipedia/20230201.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.hi-1.0.0.html";
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

## wikipedia/20230201.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.hif-1.0.0.html";
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

## wikipedia/20230201.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ho-1.0.0.html";
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

## wikipedia/20230201.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.hr-1.0.0.html";
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

## wikipedia/20230201.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.hsb-1.0.0.html";
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

## wikipedia/20230201.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20230201.ht-1.0.0.html";
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

## wikipedia/20230201.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.id

*   **Config description**: Wikipedia dataset for id, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.io

*   **Config description**: Wikipedia dataset for io, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.is

*   **Config description**: Wikipedia dataset for is, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.it

*   **Config description**: Wikipedia dataset for it, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.km

*   **Config description**: Wikipedia dataset for km, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.la

*   **Config description**: Wikipedia dataset for la, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.li

*   **Config description**: Wikipedia dataset for li, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.min

*   **Config description**: Wikipedia dataset for min, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.my

*   **Config description**: Wikipedia dataset for my, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.na

*   **Config description**: Wikipedia dataset for na, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.new

*   **Config description**: Wikipedia dataset for new, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.no

*   **Config description**: Wikipedia dataset for no, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.om

*   **Config description**: Wikipedia dataset for om, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.or

*   **Config description**: Wikipedia dataset for or, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.os

*   **Config description**: Wikipedia dataset for os, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.se

*   **Config description**: Wikipedia dataset for se, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.si

*   **Config description**: Wikipedia dataset for si, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.so

*   **Config description**: Wikipedia dataset for so, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.st

*   **Config description**: Wikipedia dataset for st, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.su

*   **Config description**: Wikipedia dataset for su, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.te

*   **Config description**: Wikipedia dataset for te, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.th

*   **Config description**: Wikipedia dataset for th, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.to

*   **Config description**: Wikipedia dataset for to, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.war

*   **Config description**: Wikipedia dataset for war, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.za

*   **Config description**: Wikipedia dataset for za, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20230201
    dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20230201.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20230201 dump.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20220620 dump.

*   **Download size**: `45.22 KiB`

*   **Dataset size**: `3.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20220620 dump.

*   **Download size**: `2.39 MiB`

*   **Dataset size**: `3.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,397

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20220620
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `4.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,778

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20220620
    dump.

*   **Download size**: `1004.23 KiB`

*   **Dataset size**: `522.19 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 582

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.af

*   **Config description**: Wikipedia dataset for af, parsed from 20220620 dump.

*   **Download size**: `122.32 MiB`

*   **Dataset size**: `207.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 126,990

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20220620 dump.

*   **Download size**: `618.99 KiB`

*   **Dataset size**: `761.42 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 688

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.als

*   **Config description**: Wikipedia dataset for als, parsed from 20220620
    dump.

*   **Download size**: `55.96 MiB`

*   **Dataset size**: `74.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.am

*   **Config description**: Wikipedia dataset for am, parsed from 20220620 dump.

*   **Download size**: `7.91 MiB`

*   **Dataset size**: `20.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,701

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.an

*   **Config description**: Wikipedia dataset for an, parsed from 20220620 dump.

*   **Download size**: `37.72 MiB`

*   **Dataset size**: `52.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 57,562

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20220620
    dump.

*   **Download size**: `4.52 MiB`

*   **Dataset size**: `2.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,649

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20220620 dump.

*   **Download size**: `1.44 GiB`

*   **Dataset size**: `2.78 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,179,406

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20220620
    dump.

*   **Download size**: `1.12 MiB`

*   **Dataset size**: `868.77 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,598

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20220620
    dump.

*   **Download size**: `216.55 MiB`

*   **Dataset size**: `1.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,601,331

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.as

*   **Config description**: Wikipedia dataset for as, parsed from 20220620 dump.

*   **Download size**: `32.06 MiB`

*   **Dataset size**: `70.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,548

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20220620
    dump.

*   **Download size**: `221.35 MiB`

*   **Dataset size**: `456.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 141,302

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20220620
    dump.

*   **Download size**: `692.29 KiB`

*   **Dataset size**: `351.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 535

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.av

*   **Config description**: Wikipedia dataset for av, parsed from 20220620 dump.

*   **Download size**: `7.08 MiB`

*   **Dataset size**: `4.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,692

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20220620 dump.

*   **Download size**: `2.47 MiB`

*   **Dataset size**: `4.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,404

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.az

*   **Config description**: Wikipedia dataset for az, parsed from 20220620 dump.

*   **Download size**: `229.12 MiB`

*   **Dataset size**: `383.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 218,285

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20220620
    dump.

*   **Download size**: `97.93 MiB`

*   **Dataset size**: `161.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 269,716

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20220620 dump.

*   **Download size**: `88.71 MiB`

*   **Dataset size**: `257.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,501

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20220620
    dump.

*   **Download size**: `35.40 MiB`

*   **Dataset size**: `41.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 47,548

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20220620
    dump.

*   **Download size**: `5.05 MiB`

*   **Dataset size**: `6.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,196

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20220620
    dump.

*   **Download size**: `14.67 MiB`

*   **Dataset size**: `14.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,387

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.be

*   **Config description**: Wikipedia dataset for be, parsed from 20220620 dump.

*   **Download size**: `252.43 MiB`

*   **Dataset size**: `530.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 219,500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20220620
    dump.

*   **Download size**: `96.33 MiB`

*   **Dataset size**: `213.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 113,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20220620 dump.

*   **Download size**: `396.21 MiB`

*   **Dataset size**: `992.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 407,551

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20220620 dump.

*   **Download size**: `16.47 MiB`

*   **Dataset size**: `12.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,992

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20220620 dump.

*   **Download size**: `597.62 KiB`

*   **Dataset size**: `333.71 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,492

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20220620
    dump.

*   **Download size**: `4.93 MiB`

*   **Dataset size**: `4.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,078

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20220620 dump.

*   **Download size**: `683.58 KiB`

*   **Dataset size**: `394.17 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,179

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20220620 dump.

*   **Download size**: `291.30 MiB`

*   **Dataset size**: `781.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202,398

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20220620 dump.

*   **Download size**: `13.66 MiB`

*   **Dataset size**: `119.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,891

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20220620
    dump.

*   **Download size**: `5.27 MiB`

*   **Dataset size**: `37.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,586

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.br

*   **Config description**: Wikipedia dataset for br, parsed from 20220620 dump.

*   **Download size**: `55.30 MiB`

*   **Dataset size**: `77.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 83,938

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20220620 dump.

*   **Download size**: `138.13 MiB`

*   **Dataset size**: `180.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20220620
    dump.

*   **Download size**: `2.11 MiB`

*   **Dataset size**: `2.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20220620
    dump.

*   **Download size**: `5.07 MiB`

*   **Dataset size**: `6.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,592

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20220620 dump.

*   **Download size**: `1.04 GiB`

*   **Dataset size**: `1.72 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 807,863

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20220620
    dump.

*   **Download size**: `3.35 MiB`

*   **Dataset size**: `2.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20220620
    dump.

*   **Download size**: `4.71 MiB`

*   **Dataset size**: `4.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,912

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20220620 dump.

*   **Download size**: `77.35 MiB`

*   **Dataset size**: `432.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 479,298

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20220620
    dump.

*   **Download size**: `2.04 GiB`

*   **Dataset size**: `4.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 6,126,575

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20220620 dump.

*   **Download size**: `748.23 KiB`

*   **Dataset size**: `167.50 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 565

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20220620
    dump.

*   **Download size**: `26.95 KiB`

*   **Dataset size**: `7.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20220620
    dump.

*   **Download size**: `692.01 KiB`

*   **Dataset size**: `680.68 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,081

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20220620
    dump.

*   **Download size**: `383.76 KiB`

*   **Dataset size**: `123.19 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 826

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20220620
    dump.

*   **Download size**: `44.22 MiB`

*   **Dataset size**: `76.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50,725

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.co

*   **Config description**: Wikipedia dataset for co, parsed from 20220620 dump.

*   **Download size**: `4.98 MiB`

*   **Dataset size**: `7.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,070

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20220620 dump.

*   **Download size**: `304.75 KiB`

*   **Dataset size**: `36.79 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 180

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20220620
    dump.

*   **Download size**: `6.95 MiB`

*   **Dataset size**: `6.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,273

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20220620 dump.

*   **Download size**: `998.37 MiB`

*   **Dataset size**: `1.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 660,764

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20220620
    dump.

*   **Download size**: `2.28 MiB`

*   **Dataset size**: `3.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,826

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20220620 dump.

*   **Download size**: `779.31 KiB`

*   **Dataset size**: `996.07 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,242

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20220620 dump.

*   **Download size**: `31.43 MiB`

*   **Dataset size**: `71.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 54,006

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20220620 dump.

*   **Download size**: `85.25 MiB`

*   **Dataset size**: `124.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 177,789

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.da

*   **Config description**: Wikipedia dataset for da, parsed from 20220620 dump.

*   **Download size**: `388.66 MiB`

*   **Dataset size**: `502.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 281,262

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.de

*   **Config description**: Wikipedia dataset for de, parsed from 20220620 dump.

*   **Download size**: `6.17 GiB`

*   **Dataset size**: `8.60 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,536,830

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.din

*   **Config description**: Wikipedia dataset for din, parsed from 20220620
    dump.

*   **Download size**: `559.45 KiB`

*   **Dataset size**: `530.66 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 507

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20220620
    dump.

*   **Download size**: `11.87 MiB`

*   **Dataset size**: `17.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20220620
    dump.

*   **Download size**: `3.86 MiB`

*   **Dataset size**: `3.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,587

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20220620
    dump.

*   **Download size**: `7.12 MiB`

*   **Dataset size**: `6.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,604

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20220620 dump.

*   **Download size**: `4.55 MiB`

*   **Dataset size**: `12.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,326

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20220620 dump.

*   **Download size**: `705.88 KiB`

*   **Dataset size**: `3.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 428

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20220620 dump.

*   **Download size**: `540.72 KiB`

*   **Dataset size**: `247.82 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 653

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.el

*   **Config description**: Wikipedia dataset for el, parsed from 20220620 dump.

*   **Download size**: `460.85 MiB`

*   **Dataset size**: `1.16 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 293,042

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20220620
    dump.

*   **Download size**: `9.34 MiB`

*   **Dataset size**: `3.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,211

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.en

*   **Config description**: Wikipedia dataset for en, parsed from 20220620 dump.

*   **Download size**: `19.50 GiB`

*   **Dataset size**: `19.14 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 6,525,137

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20220620 dump.

*   **Download size**: `314.80 MiB`

*   **Dataset size**: `474.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 443,682

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.es

*   **Config description**: Wikipedia dataset for es, parsed from 20220620 dump.

*   **Download size**: `3.79 GiB`

*   **Dataset size**: `5.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,142,937

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.et

*   **Config description**: Wikipedia dataset for et, parsed from 20220620 dump.

*   **Download size**: `245.98 MiB`

*   **Dataset size**: `403.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 354,071

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20220620 dump.

*   **Download size**: `258.08 MiB`

*   **Dataset size**: `487.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 502,222

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20220620
    dump.

*   **Download size**: `2.64 MiB`

*   **Dataset size**: `3.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,767

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20220620 dump.

*   **Download size**: `1.01 GiB`

*   **Dataset size**: `1.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,714,891

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20220620 dump.

*   **Download size**: `654.87 KiB`

*   **Dataset size**: `683.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 738

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20220620 dump.

*   **Download size**: `821.05 MiB`

*   **Dataset size**: `1.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 732,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20220620
    dump.

*   **Download size**: `2.58 MiB`

*   **Dataset size**: `4.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,222

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20220620 dump.

*   **Download size**: `988.65 KiB`

*   **Dataset size**: `544.66 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,277

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20220620 dump.

*   **Download size**: `14.82 MiB`

*   **Dataset size**: `14.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20220620 dump.

*   **Download size**: `5.32 GiB`

*   **Dataset size**: `7.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,432,896

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20220620
    dump.

*   **Download size**: `4.00 MiB`

*   **Dataset size**: `3.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,795

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20220620
    dump.

*   **Download size**: `12.21 MiB`

*   **Dataset size**: `9.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 17,780

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20220620
    dump.

*   **Download size**: `2.57 MiB`

*   **Dataset size**: `3.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,059

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20220620 dump.

*   **Download size**: `61.36 MiB`

*   **Dataset size**: `115.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,785

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20220620 dump.

*   **Download size**: `33.72 MiB`

*   **Dataset size**: `53.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,138

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20220620
    dump.

*   **Download size**: `2.19 MiB`

*   **Dataset size**: `2.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,122

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20220620
    dump.

*   **Download size**: `4.21 MiB`

*   **Dataset size**: `2.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,594

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20220620 dump.

*   **Download size**: `9.49 MiB`

*   **Dataset size**: `13.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20220620 dump.

*   **Download size**: `301.24 MiB`

*   **Dataset size**: `446.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 254,505

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20220620
    dump.

*   **Download size**: `2.69 MiB`

*   **Dataset size**: `5.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,925

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20220620 dump.

*   **Download size**: `4.30 MiB`

*   **Dataset size**: `6.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,731

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20220620
    dump.

*   **Download size**: `6.67 MiB`

*   **Dataset size**: `29.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20220620
    dump.

*   **Download size**: `3.84 MiB`

*   **Dataset size**: `5.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,706

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.got

*   **Config description**: Wikipedia dataset for got, parsed from 20220620
    dump.

*   **Download size**: `733.66 KiB`

*   **Dataset size**: `1.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 979

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20220620 dump.

*   **Download size**: `32.14 MiB`

*   **Dataset size**: `111.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,082

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20220620 dump.

*   **Download size**: `6.19 MiB`

*   **Dataset size**: `4.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,413

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20220620 dump.

*   **Download size**: `21.81 MiB`

*   **Dataset size**: `39.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 17,463

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20220620
    dump.

*   **Download size**: `4.03 MiB`

*   **Dataset size**: `4.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20220620
    dump.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `1.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.he

*   **Config description**: Wikipedia dataset for he, parsed from 20220620 dump.

*   **Download size**: `800.49 MiB`

*   **Dataset size**: `1.69 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 501,548

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20220620 dump.

*   **Download size**: `185.43 MiB`

*   **Dataset size**: `582.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 190,774

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20220620
    dump.

*   **Download size**: `5.33 MiB`

*   **Dataset size**: `4.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20220620 dump.

*   **Download size**: `19.22 KiB`

*   **Dataset size**: `3.27 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20220620 dump.

*   **Download size**: `295.14 MiB`

*   **Dataset size**: `411.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 248,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20220620
    dump.

*   **Download size**: `11.08 MiB`

*   **Dataset size**: `14.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20220620 dump.

*   **Download size**: `18.26 MiB`

*   **Dataset size**: `49.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,383

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20220620 dump.

*   **Download size**: `994.41 MiB`

*   **Dataset size**: `1.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 708,658

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20220620 dump.

*   **Download size**: `400.92 MiB`

*   **Dataset size**: `1.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 646,281

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20220620 dump.

*   **Download size**: `9.61 MiB`

*   **Dataset size**: `12.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21,210

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.id

*   **Config description**: Wikipedia dataset for id, parsed from 20220620 dump.

*   **Download size**: `799.18 MiB`

*   **Dataset size**: `1002.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,180,714

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20220620 dump.

*   **Download size**: `3.28 MiB`

*   **Dataset size**: `5.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20220620 dump.

*   **Download size**: `11.01 MiB`

*   **Dataset size**: `19.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20220620 dump.

*   **Download size**: `31.88 KiB`

*   **Dataset size**: `8.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20220620 dump.

*   **Download size**: `306.62 KiB`

*   **Dataset size**: `119.28 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 760

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20220620
    dump.

*   **Download size**: `18.43 MiB`

*   **Dataset size**: `15.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20220620
    dump.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `2.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,781

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.io

*   **Config description**: Wikipedia dataset for io, parsed from 20220620 dump.

*   **Download size**: `15.45 MiB`

*   **Dataset size**: `32.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 34,849

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.is

*   **Config description**: Wikipedia dataset for is, parsed from 20220620 dump.

*   **Download size**: `52.48 MiB`

*   **Dataset size**: `80.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 77,629

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.it

*   **Config description**: Wikipedia dataset for it, parsed from 20220620 dump.

*   **Download size**: `3.32 GiB`

*   **Dataset size**: `4.29 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,152,760

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20220620 dump.

*   **Download size**: `373.91 KiB`

*   **Dataset size**: `202.76 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 711

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20220620 dump.

*   **Download size**: `3.53 GiB`

*   **Dataset size**: `6.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,652,577

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20220620
    dump.

*   **Download size**: `954.42 KiB`

*   **Dataset size**: `1.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,747

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20220620
    dump.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `2.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20220620 dump.

*   **Download size**: `53.90 MiB`

*   **Dataset size**: `65.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 88,980

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20220620 dump.

*   **Download size**: `181.18 MiB`

*   **Dataset size**: `621.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 201,554

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20220620
    dump.

*   **Download size**: `1.51 MiB`

*   **Dataset size**: `1.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,281

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20220620
    dump.

*   **Download size**: `3.93 MiB`

*   **Dataset size**: `3.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,508

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20220620
    dump.

*   **Download size**: `1.73 MiB`

*   **Dataset size**: `2.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,634

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20220620
    dump.

*   **Download size**: `1.43 MiB`

*   **Dataset size**: `3.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,916

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20220620 dump.

*   **Download size**: `517.54 KiB`

*   **Dataset size**: `307.28 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,304

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20220620 dump.

*   **Download size**: `460.30 KiB`

*   **Dataset size**: `397.67 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,630

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20220620 dump.

*   **Download size**: `17.46 KiB`

*   **Dataset size**: `4.93 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20220620 dump.

*   **Download size**: `129.67 MiB`

*   **Dataset size**: `442.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 275,494

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20220620 dump.

*   **Download size**: `556.04 KiB`

*   **Dataset size**: `303.69 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 295

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.km

*   **Config description**: Wikipedia dataset for km, parsed from 20220620 dump.

*   **Download size**: `24.29 MiB`

*   **Dataset size**: `93.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,695

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20220620 dump.

*   **Download size**: `80.71 MiB`

*   **Dataset size**: `348.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,033

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20220620 dump.

*   **Download size**: `868.62 MiB`

*   **Dataset size**: `1.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,277,154

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20220620
    dump.

*   **Download size**: `2.41 MiB`

*   **Dataset size**: `4.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,961

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20220620
    dump.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `4.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,345

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20220620 dump.

*   **Download size**: `2.88 MiB`

*   **Dataset size**: `592.76 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,193

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20220620
    dump.

*   **Download size**: `3.34 MiB`

*   **Dataset size**: `2.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,450

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20220620 dump.

*   **Download size**: `27.76 MiB`

*   **Dataset size**: `36.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,938

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20220620 dump.

*   **Download size**: `3.82 MiB`

*   **Dataset size**: `8.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,852

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20220620 dump.

*   **Download size**: `3.43 MiB`

*   **Dataset size**: `3.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,784

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20220620 dump.

*   **Download size**: `37.03 MiB`

*   **Dataset size**: `154.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 80,738

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.la

*   **Config description**: Wikipedia dataset for la, parsed from 20220620 dump.

*   **Download size**: `95.60 MiB`

*   **Dataset size**: `136.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 137,048

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20220620
    dump.

*   **Download size**: `3.52 MiB`

*   **Dataset size**: `4.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,949

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20220620 dump.

*   **Download size**: `51.86 MiB`

*   **Dataset size**: `82.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,716

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20220620
    dump.

*   **Download size**: `1.78 MiB`

*   **Dataset size**: `703.36 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,592

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20220620
    dump.

*   **Download size**: `6.19 MiB`

*   **Dataset size**: `9.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,746

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20220620
    dump.

*   **Download size**: `4.10 MiB`

*   **Dataset size**: `8.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,770

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20220620 dump.

*   **Download size**: `1.93 MiB`

*   **Dataset size**: `4.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,611

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.li

*   **Config description**: Wikipedia dataset for li, parsed from 20220620 dump.

*   **Download size**: `15.81 MiB`

*   **Dataset size**: `27.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,182

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20220620
    dump.

*   **Download size**: `6.97 MiB`

*   **Dataset size**: `9.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20220620
    dump.

*   **Download size**: `25.73 MiB`

*   **Dataset size**: `35.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 60,094

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20220620 dump.

*   **Download size**: `2.09 MiB`

*   **Dataset size**: `1.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,407

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20220620 dump.

*   **Download size**: `5.48 MiB`

*   **Dataset size**: `13.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,021

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20220620
    dump.

*   **Download size**: `23.98 KiB`

*   **Dataset size**: `107 bytes`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20220620 dump.

*   **Download size**: `203.00 MiB`

*   **Dataset size**: `306.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 231,492

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20220620
    dump.

*   **Download size**: `926.60 KiB`

*   **Dataset size**: `867.47 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,016

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20220620 dump.

*   **Download size**: `162.74 MiB`

*   **Dataset size**: `200.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 113,939

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20220620
    dump.

*   **Download size**: `12.25 MiB`

*   **Dataset size**: `18.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,026

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20220620
    dump.

*   **Download size**: `4.80 MiB`

*   **Dataset size**: `4.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,128

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20220620
    dump.

*   **Download size**: `4.01 MiB`

*   **Dataset size**: `2.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20220620 dump.

*   **Download size**: `29.72 MiB`

*   **Dataset size**: `67.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 132,584

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20220620 dump.

*   **Download size**: `28.61 KiB`

*   **Dataset size**: `11.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20220620
    dump.

*   **Download size**: `6.45 MiB`

*   **Dataset size**: `17.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,654

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20220620 dump.

*   **Download size**: `2.17 MiB`

*   **Dataset size**: `3.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,458

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.min

*   **Config description**: Wikipedia dataset for min, parsed from 20220620
    dump.

*   **Download size**: `32.67 MiB`

*   **Dataset size**: `102.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 229,488

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20220620 dump.

*   **Download size**: `202.46 MiB`

*   **Dataset size**: `558.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 173,105

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20220620 dump.

*   **Download size**: `164.14 MiB`

*   **Dataset size**: `427.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 145,312

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20220620 dump.

*   **Download size**: `36.40 MiB`

*   **Dataset size**: `82.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 26,307

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20220620 dump.

*   **Download size**: `69.63 MiB`

*   **Dataset size**: `224.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 140,718

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20220620
    dump.

*   **Download size**: `3.33 MiB`

*   **Dataset size**: `8.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,823

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20220620 dump.

*   **Download size**: `285.64 MiB`

*   **Dataset size**: `370.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 406,579

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20220620 dump.

*   **Download size**: `12.31 MiB`

*   **Dataset size**: `19.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,106

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20220620
    dump.

*   **Download size**: `15.06 KiB`

*   **Dataset size**: `875 bytes`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20220620
    dump.

*   **Download size**: `9.27 MiB`

*   **Dataset size**: `18.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,460

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.my

*   **Config description**: Wikipedia dataset for my, parsed from 20220620 dump.

*   **Download size**: `56.21 MiB`

*   **Dataset size**: `256.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 105,760

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20220620
    dump.

*   **Download size**: `11.17 MiB`

*   **Dataset size**: `9.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,689

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20220620
    dump.

*   **Download size**: `7.56 MiB`

*   **Dataset size**: `11.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,262

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.na

*   **Config description**: Wikipedia dataset for na, parsed from 20220620 dump.

*   **Download size**: `707.01 KiB`

*   **Dataset size**: `381.16 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,682

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20220620
    dump.

*   **Download size**: `4.92 MiB`

*   **Dataset size**: `3.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,798

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20220620
    dump.

*   **Download size**: `5.43 MiB`

*   **Dataset size**: `6.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,383

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20220620
    dump.

*   **Download size**: `43.27 MiB`

*   **Dataset size**: `87.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 91,692

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20220620
    dump.

*   **Download size**: `8.36 MiB`

*   **Dataset size**: `12.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,453

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20220620 dump.

*   **Download size**: `40.89 MiB`

*   **Dataset size**: `93.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 32,590

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.new

*   **Config description**: Wikipedia dataset for new, parsed from 20220620
    dump.

*   **Download size**: `17.36 MiB`

*   **Dataset size**: `140.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 73,019

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20220620 dump.

*   **Download size**: `92.18 KiB`

*   **Dataset size**: `66.12 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20220620 dump.

*   **Download size**: `1.66 GiB`

*   **Dataset size**: `2.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,606,249

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20220620 dump.

*   **Download size**: `149.76 MiB`

*   **Dataset size**: `222.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 239,952

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.no

*   **Config description**: Wikipedia dataset for no, parsed from 20220620 dump.

*   **Download size**: `707.72 MiB`

*   **Dataset size**: `967.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 914,633

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20220620
    dump.

*   **Download size**: `1.24 MiB`

*   **Dataset size**: `837.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,612

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20220620
    dump.

*   **Download size**: `1.99 MiB`

*   **Dataset size**: `2.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,875

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20220620
    dump.

*   **Download size**: `2.58 MiB`

*   **Dataset size**: `2.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,569

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20220620 dump.

*   **Download size**: `5.35 MiB`

*   **Dataset size**: `12.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,455

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20220620 dump.

*   **Download size**: `2.11 MiB`

*   **Dataset size**: `1.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,042

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20220620 dump.

*   **Download size**: `77.75 MiB`

*   **Dataset size**: `113.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 96,491

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20220620
    dump.

*   **Download size**: `2.15 MiB`

*   **Dataset size**: `2.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,895

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.om

*   **Config description**: Wikipedia dataset for om, parsed from 20220620 dump.

*   **Download size**: `1.47 MiB`

*   **Dataset size**: `2.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,186

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.or

*   **Config description**: Wikipedia dataset for or, parsed from 20220620 dump.

*   **Download size**: `30.85 MiB`

*   **Dataset size**: `64.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,228

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.os

*   **Config description**: Wikipedia dataset for os, parsed from 20220620 dump.

*   **Download size**: `14.61 MiB`

*   **Dataset size**: `11.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,618

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20220620 dump.

*   **Download size**: `55.75 MiB`

*   **Dataset size**: `150.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,283

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20220620
    dump.

*   **Download size**: `1.73 MiB`

*   **Dataset size**: `1.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,976

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20220620
    dump.

*   **Download size**: `9.18 MiB`

*   **Dataset size**: `7.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,860

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20220620
    dump.

*   **Download size**: `2.22 MiB`

*   **Dataset size**: `2.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,560

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20220620
    dump.

*   **Download size**: `5.24 MiB`

*   **Dataset size**: `5.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20220620
    dump.

*   **Download size**: `1.20 MiB`

*   **Dataset size**: `1.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20220620
    dump.

*   **Download size**: `3.67 MiB`

*   **Dataset size**: `3.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,984

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20220620 dump.

*   **Download size**: `683.35 KiB`

*   **Dataset size**: `970.64 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,062

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20220620
    dump.

*   **Download size**: `810.93 KiB`

*   **Dataset size**: `254.49 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 929

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20220620 dump.

*   **Download size**: `2.17 GiB`

*   **Dataset size**: `2.65 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,895,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20220620
    dump.

*   **Download size**: `14.32 MiB`

*   **Dataset size**: `31.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 67,584

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20220620
    dump.

*   **Download size**: `89.96 MiB`

*   **Dataset size**: `255.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 75,225

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20220620
    dump.

*   **Download size**: `587.71 KiB`

*   **Dataset size**: `638.65 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 541

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20220620 dump.

*   **Download size**: `32.21 MiB`

*   **Dataset size**: `73.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,390

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20220620 dump.

*   **Download size**: `1.97 GiB`

*   **Dataset size**: `2.45 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,558,114

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20220620 dump.

*   **Download size**: `12.93 MiB`

*   **Dataset size**: `16.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,780

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20220620 dump.

*   **Download size**: `7.20 MiB`

*   **Dataset size**: `17.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,927

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20220620
    dump.

*   **Download size**: `575.79 KiB`

*   **Dataset size**: `350.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 754

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20220620 dump.

*   **Download size**: `883.75 KiB`

*   **Dataset size**: `406.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 753

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20220620 dump.

*   **Download size**: `585.89 MiB`

*   **Dataset size**: `758.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 431,837

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20220620
    dump.

*   **Download size**: `1.09 MiB`

*   **Dataset size**: `1.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,336

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20220620
    dump.

*   **Download size**: `6.41 MiB`

*   **Dataset size**: `6.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20220620 dump.

*   **Download size**: `4.56 GiB`

*   **Dataset size**: `9.00 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,006,938

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20220620
    dump.

*   **Download size**: `6.29 MiB`

*   **Dataset size**: `11.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,004

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20220620 dump.

*   **Download size**: `4.51 MiB`

*   **Dataset size**: `4.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20220620 dump.

*   **Download size**: `16.11 MiB`

*   **Dataset size**: `61.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 22,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20220620
    dump.

*   **Download size**: `15.46 MiB`

*   **Dataset size**: `42.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,245

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20220620
    dump.

*   **Download size**: `13.03 MiB`

*   **Dataset size**: `29.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,279

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20220620 dump.

*   **Download size**: `7.38 MiB`

*   **Dataset size**: `11.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,466

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20220620
    dump.

*   **Download size**: `12.22 MiB`

*   **Dataset size**: `16.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,591

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20220620
    dump.

*   **Download size**: `57.20 MiB`

*   **Dataset size**: `46.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 40,637

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20220620 dump.

*   **Download size**: `19.65 MiB`

*   **Dataset size**: `34.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 22,393

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.se

*   **Config description**: Wikipedia dataset for se, parsed from 20220620 dump.

*   **Download size**: `3.98 MiB`

*   **Dataset size**: `3.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,682

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20220620 dump.

*   **Download size**: `367.62 KiB`

*   **Dataset size**: `116.16 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 547

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20220620 dump.

*   **Download size**: `432.85 MiB`

*   **Dataset size**: `831.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,940,273

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.si

*   **Config description**: Wikipedia dataset for si, parsed from 20220620 dump.

*   **Download size**: `46.16 MiB`

*   **Dataset size**: `122.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20220620
    dump.

*   **Download size**: `240.42 MiB`

*   **Dataset size**: `250.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 212,585

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20220620 dump.

*   **Download size**: `293.23 MiB`

*   **Dataset size**: `377.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 261,341

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20220620 dump.

*   **Download size**: `259.06 MiB`

*   **Dataset size**: `401.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 213,134

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20220620 dump.

*   **Download size**: `928.26 KiB`

*   **Dataset size**: `817.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,126

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20220620 dump.

*   **Download size**: `4.14 MiB`

*   **Dataset size**: `7.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,578

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.so

*   **Config description**: Wikipedia dataset for so, parsed from 20220620 dump.

*   **Download size**: `11.42 MiB`

*   **Dataset size**: `12.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,005

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20220620 dump.

*   **Download size**: `103.12 MiB`

*   **Dataset size**: `171.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 118,180

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20220620 dump.

*   **Download size**: `903.80 MiB`

*   **Dataset size**: `1.74 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,153,469

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20220620
    dump.

*   **Download size**: `655.74 KiB`

*   **Dataset size**: `607.60 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,280

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20220620 dump.

*   **Download size**: `875.15 KiB`

*   **Dataset size**: `509.74 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 587

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.st

*   **Config description**: Wikipedia dataset for st, parsed from 20220620 dump.

*   **Download size**: `2.26 MiB`

*   **Dataset size**: `742.07 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 998

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20220620
    dump.

*   **Download size**: `3.52 MiB`

*   **Dataset size**: `4.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,543

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.su

*   **Config description**: Wikipedia dataset for su, parsed from 20220620 dump.

*   **Download size**: `27.31 MiB`

*   **Dataset size**: `42.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 68,098

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20220620 dump.

*   **Download size**: `1.43 GiB`

*   **Dataset size**: `2.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 4,276,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20220620 dump.

*   **Download size**: `41.82 MiB`

*   **Dataset size**: `64.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 73,964

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20220620
    dump.

*   **Download size**: `13.47 MiB`

*   **Dataset size**: `18.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 56,591

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20220620 dump.

*   **Download size**: `191.30 MiB`

*   **Dataset size**: `710.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 182,598

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20220620
    dump.

*   **Download size**: `4.53 MiB`

*   **Dataset size**: `9.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,850

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.te

*   **Config description**: Wikipedia dataset for te, parsed from 20220620 dump.

*   **Download size**: `126.77 MiB`

*   **Dataset size**: `635.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 103,548

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20220620
    dump.

*   **Download size**: `1.34 MiB`

*   **Dataset size**: `1.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,638

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20220620 dump.

*   **Download size**: `49.23 MiB`

*   **Dataset size**: `124.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 116,122

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.th

*   **Config description**: Wikipedia dataset for th, parsed from 20220620 dump.

*   **Download size**: `338.86 MiB`

*   **Dataset size**: `904.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 270,315

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20220620 dump.

*   **Download size**: `811.06 KiB`

*   **Dataset size**: `404.59 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 388

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20220620 dump.

*   **Download size**: `5.81 MiB`

*   **Dataset size**: `11.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,558

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20220620 dump.

*   **Download size**: `67.10 MiB`

*   **Dataset size**: `73.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,898

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20220620 dump.

*   **Download size**: `1.61 MiB`

*   **Dataset size**: `1.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 864

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.to

*   **Config description**: Wikipedia dataset for to, parsed from 20220620 dump.

*   **Download size**: `886.72 KiB`

*   **Dataset size**: `968.03 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,778

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20220620
    dump.

*   **Download size**: `1.51 MiB`

*   **Dataset size**: `438.38 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,731

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20220620 dump.

*   **Download size**: `761.13 MiB`

*   **Dataset size**: `883.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 758,043

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20220620 dump.

*   **Download size**: `1.76 MiB`

*   **Dataset size**: `735.07 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 730

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20220620 dump.

*   **Download size**: `105.25 MiB`

*   **Dataset size**: `474.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 461,299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20220620
    dump.

*   **Download size**: `534.00 KiB`

*   **Dataset size**: `572.43 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,833

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20220620 dump.

*   **Download size**: `2.37 MiB`

*   **Dataset size**: `2.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,113

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20220620 dump.

*   **Download size**: `569.95 KiB`

*   **Dataset size**: `281.62 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,342

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20220620
    dump.

*   **Download size**: `5.10 MiB`

*   **Dataset size**: `12.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,089

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20220620
    dump.

*   **Download size**: `3.65 MiB`

*   **Dataset size**: `6.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,336

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20220620 dump.

*   **Download size**: `8.14 MiB`

*   **Dataset size**: `37.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,920

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20220620 dump.

*   **Download size**: `1.86 GiB`

*   **Dataset size**: `4.16 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,778,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20220620 dump.

*   **Download size**: `192.55 MiB`

*   **Dataset size**: `328.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 367,085

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20220620 dump.

*   **Download size**: `92.94 MiB`

*   **Dataset size**: `145.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 214,458

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20220620 dump.

*   **Download size**: `323.40 KiB`

*   **Dataset size**: `277.52 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 715

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20220620
    dump.

*   **Download size**: `27.17 MiB`

*   **Dataset size**: `34.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 77,580

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20220620
    dump.

*   **Download size**: `7.74 MiB`

*   **Dataset size**: `10.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,203

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20220620 dump.

*   **Download size**: `889.55 MiB`

*   **Dataset size**: `1.43 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,501,068

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20220620
    dump.

*   **Download size**: `7.32 MiB`

*   **Dataset size**: `10.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,129

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20220620 dump.

*   **Download size**: `25.70 MiB`

*   **Dataset size**: `80.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 121,979

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20220620 dump.

*   **Download size**: `7.43 MiB`

*   **Dataset size**: `10.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,573

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.war

*   **Config description**: Wikipedia dataset for war, parsed from 20220620
    dump.

*   **Download size**: `264.27 MiB`

*   **Dataset size**: `413.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,265,837

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20220620 dump.

*   **Download size**: `2.03 MiB`

*   **Dataset size**: `3.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,697

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20220620
    dump.

*   **Download size**: `15.82 MiB`

*   **Dataset size**: `21.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 44,777

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20220620
    dump.

*   **Download size**: `1.90 MiB`

*   **Dataset size**: `1.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,815

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20220620 dump.

*   **Download size**: `1.66 MiB`

*   **Dataset size**: `1.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20220620
    dump.

*   **Download size**: `12.85 MiB`

*   **Dataset size**: `32.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,767

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20220620 dump.

*   **Download size**: `13.01 MiB`

*   **Dataset size**: `34.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,715

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20220620 dump.

*   **Download size**: `15.42 MiB`

*   **Dataset size**: `13.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 34,392

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.za

*   **Config description**: Wikipedia dataset for za, parsed from 20220620 dump.

*   **Download size**: `804.71 KiB`

*   **Dataset size**: `691.83 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,505

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20220620
    dump.

*   **Download size**: `2.72 MiB`

*   **Dataset size**: `4.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,872

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20220620 dump.

*   **Download size**: `2.41 GiB`

*   **Dataset size**: `2.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,870,276

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20220620 dump.

*   **Download size**: `15.29 MiB`

*   **Dataset size**: `11.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,639

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20220620 dump.

*   **Download size**: `75.95 MiB`

*   **Dataset size**: `131.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 449,458

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20220620
    dump.

*   **Download size**: `88.38 MiB`

*   **Dataset size**: `89.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 124,159

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20220620.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20220620 dump.

*   **Download size**: `4.72 MiB`

*   **Dataset size**: `5.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,839

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20201201 dump.

*   **Download size**: `45.29 KiB`

*   **Dataset size**: `3.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20201201 dump.

*   **Download size**: `1.80 MiB`

*   **Dataset size**: `2.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,136

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20201201
    dump.

*   **Download size**: `3.17 MiB`

*   **Dataset size**: `3.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,561

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20201201
    dump.

*   **Download size**: `457.46 KiB`

*   **Dataset size**: `515.14 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 562

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.af

*   **Config description**: Wikipedia dataset for af, parsed from 20201201 dump.

*   **Download size**: `111.81 MiB`

*   **Dataset size**: `192.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 117,154

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20201201 dump.

*   **Download size**: `680.35 KiB`

*   **Dataset size**: `732.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,424

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.als

*   **Config description**: Wikipedia dataset for als, parsed from 20201201
    dump.

*   **Download size**: `52.48 MiB`

*   **Dataset size**: `70.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,826

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.am

*   **Config description**: Wikipedia dataset for am, parsed from 20201201 dump.

*   **Download size**: `7.12 MiB`

*   **Dataset size**: `17.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,502

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.an

*   **Config description**: Wikipedia dataset for an, parsed from 20201201 dump.

*   **Download size**: `34.56 MiB`

*   **Dataset size**: `48.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 53,071

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20201201
    dump.

*   **Download size**: `4.32 MiB`

*   **Dataset size**: `2.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20201201 dump.

*   **Download size**: `1.22 GiB`

*   **Dataset size**: `2.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,049,549

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20201201
    dump.

*   **Download size**: `1.09 MiB`

*   **Dataset size**: `851.19 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,534

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20201201
    dump.

*   **Download size**: `153.51 MiB`

*   **Dataset size**: `851.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,182,669

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.as

*   **Config description**: Wikipedia dataset for as, parsed from 20201201 dump.

*   **Download size**: `24.77 MiB`

*   **Dataset size**: `48.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,643

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20201201
    dump.

*   **Download size**: `218.95 MiB`

*   **Dataset size**: `447.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 116,833

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20201201
    dump.

*   **Download size**: `602.22 KiB`

*   **Dataset size**: `756.58 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,424

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.av

*   **Config description**: Wikipedia dataset for av, parsed from 20201201 dump.

*   **Download size**: `5.27 MiB`

*   **Dataset size**: `3.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,173

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20201201 dump.

*   **Download size**: `2.26 MiB`

*   **Dataset size**: `4.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,253

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.az

*   **Config description**: Wikipedia dataset for az, parsed from 20201201 dump.

*   **Download size**: `200.75 MiB`

*   **Dataset size**: `344.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 203,051

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20201201
    dump.

*   **Download size**: `91.79 MiB`

*   **Dataset size**: `156.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 265,450

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20201201 dump.

*   **Download size**: `72.92 MiB`

*   **Dataset size**: `207.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 61,290

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20201201
    dump.

*   **Download size**: `33.42 MiB`

*   **Dataset size**: `41.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 46,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20201201
    dump.

*   **Download size**: `4.91 MiB`

*   **Dataset size**: `6.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20201201
    dump.

*   **Download size**: `10.22 MiB`

*   **Dataset size**: `10.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,763

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.be

*   **Config description**: Wikipedia dataset for be, parsed from 20201201 dump.

*   **Download size**: `224.26 MiB`

*   **Dataset size**: `465.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 198,957

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20201201
    dump.

*   **Download size**: `84.30 MiB`

*   **Dataset size**: `187.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 103,888

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20201201 dump.

*   **Download size**: `362.31 MiB`

*   **Dataset size**: `909.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 387,980

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20201201 dump.

*   **Download size**: `14.57 MiB`

*   **Dataset size**: `11.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,395

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20201201 dump.

*   **Download size**: `461.56 KiB`

*   **Dataset size**: `306.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,406

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20201201
    dump.

*   **Download size**: `3.44 MiB`

*   **Dataset size**: `3.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,790

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20201201 dump.

*   **Download size**: `602.51 KiB`

*   **Dataset size**: `353.23 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 754

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20201201 dump.

*   **Download size**: `223.59 MiB`

*   **Dataset size**: `594.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 156,991

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20201201 dump.

*   **Download size**: `13.32 MiB`

*   **Dataset size**: `117.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,670

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20201201
    dump.

*   **Download size**: `5.23 MiB`

*   **Dataset size**: `39.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,475

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.br

*   **Config description**: Wikipedia dataset for br, parsed from 20201201 dump.

*   **Download size**: `52.28 MiB`

*   **Dataset size**: `74.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,725

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20201201 dump.

*   **Download size**: `117.25 MiB`

*   **Dataset size**: `159.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 190,059

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20201201
    dump.

*   **Download size**: `1.84 MiB`

*   **Dataset size**: `2.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,424

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20201201
    dump.

*   **Download size**: `3.29 MiB`

*   **Dataset size**: `5.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,665

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20201201 dump.

*   **Download size**: `947.73 MiB`

*   **Dataset size**: `1.57 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 740,415

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20201201
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `3.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,479

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20201201
    dump.

*   **Download size**: `4.46 MiB`

*   **Dataset size**: `4.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,879

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20201201 dump.

*   **Download size**: `60.74 MiB`

*   **Dataset size**: `323.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 349,688

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20201201
    dump.

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `3.69 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,377,442

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20201201 dump.

*   **Download size**: `723.85 KiB`

*   **Dataset size**: `168.11 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 544

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20201201
    dump.

*   **Download size**: `27.02 KiB`

*   **Dataset size**: `7.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20201201
    dump.

*   **Download size**: `659.67 KiB`

*   **Dataset size**: `641.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 969

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20201201
    dump.

*   **Download size**: `353.22 KiB`

*   **Dataset size**: `116.82 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 783

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20201201
    dump.

*   **Download size**: `31.97 MiB`

*   **Dataset size**: `55.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.co

*   **Config description**: Wikipedia dataset for co, parsed from 20201201 dump.

*   **Download size**: `4.56 MiB`

*   **Dataset size**: `6.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,617

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20201201 dump.

*   **Download size**: `287.29 KiB`

*   **Dataset size**: `65.23 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 135

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20201201
    dump.

*   **Download size**: `4.79 MiB`

*   **Dataset size**: `3.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,237

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20201201 dump.

*   **Download size**: `882.62 MiB`

*   **Dataset size**: `1.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 603,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20201201
    dump.

*   **Download size**: `2.19 MiB`

*   **Dataset size**: `3.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,727

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20201201 dump.

*   **Download size**: `695.33 KiB`

*   **Dataset size**: `706.87 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,592

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20201201 dump.

*   **Download size**: `25.37 MiB`

*   **Dataset size**: `63.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,049

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20201201 dump.

*   **Download size**: `78.15 MiB`

*   **Dataset size**: `114.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 173,604

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.da

*   **Config description**: Wikipedia dataset for da, parsed from 20201201 dump.

*   **Download size**: `356.47 MiB`

*   **Dataset size**: `471.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 263,308

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.de

*   **Config description**: Wikipedia dataset for de, parsed from 20201201 dump.

*   **Download size**: `5.58 GiB`

*   **Dataset size**: `7.85 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,229,667

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.din

*   **Config description**: Wikipedia dataset for din, parsed from 20201201
    dump.

*   **Download size**: `506.05 KiB`

*   **Dataset size**: `486.08 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 303

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20201201
    dump.

*   **Download size**: `11.05 MiB`

*   **Dataset size**: `16.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,014

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20201201
    dump.

*   **Download size**: `3.81 MiB`

*   **Dataset size**: `3.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,541

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20201201
    dump.

*   **Download size**: `6.95 MiB`

*   **Dataset size**: `6.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,584

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20201201 dump.

*   **Download size**: `4.36 MiB`

*   **Dataset size**: `12.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,271

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20201201 dump.

*   **Download size**: `386.98 KiB`

*   **Dataset size**: `800.32 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 290

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20201201 dump.

*   **Download size**: `478.59 KiB`

*   **Dataset size**: `217.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 385

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.el

*   **Config description**: Wikipedia dataset for el, parsed from 20201201 dump.

*   **Download size**: `390.18 MiB`

*   **Dataset size**: `1008.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 259,509

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20201201
    dump.

*   **Download size**: `8.58 MiB`

*   **Dataset size**: `3.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,658

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.en

*   **Config description**: Wikipedia dataset for en, parsed from 20201201 dump.

*   **Download size**: `17.70 GiB`

*   **Dataset size**: `17.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 6,210,110

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20201201 dump.

*   **Download size**: `281.09 MiB`

*   **Dataset size**: `427.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 398,951

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.es

*   **Config description**: Wikipedia dataset for es, parsed from 20201201 dump.

*   **Download size**: `3.38 GiB`

*   **Dataset size**: `4.84 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,943,343

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.et

*   **Config description**: Wikipedia dataset for et, parsed from 20201201 dump.

*   **Download size**: `223.58 MiB`

*   **Dataset size**: `369.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 328,713

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20201201 dump.

*   **Download size**: `214.93 MiB`

*   **Dataset size**: `417.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 463,673

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20201201
    dump.

*   **Download size**: `2.55 MiB`

*   **Dataset size**: `3.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,536

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20201201 dump.

*   **Download size**: `850.45 MiB`

*   **Dataset size**: `1.45 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,427,541

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20201201 dump.

*   **Download size**: `516.43 KiB`

*   **Dataset size**: `524.57 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20201201 dump.

*   **Download size**: `744.51 MiB`

*   **Dataset size**: `964.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 682,734

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20201201
    dump.

*   **Download size**: `2.16 MiB`

*   **Dataset size**: `3.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,266

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20201201 dump.

*   **Download size**: `781.90 KiB`

*   **Dataset size**: `456.89 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,118

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20201201 dump.

*   **Download size**: `14.37 MiB`

*   **Dataset size**: `13.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,453

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20201201 dump.

*   **Download size**: `4.75 GiB`

*   **Dataset size**: `6.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,274,691

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20201201
    dump.

*   **Download size**: `2.60 MiB`

*   **Dataset size**: `1.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,125

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20201201
    dump.

*   **Download size**: `9.78 MiB`

*   **Dataset size**: `6.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,251

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20201201
    dump.

*   **Download size**: `2.45 MiB`

*   **Dataset size**: `3.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,658

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20201201 dump.

*   **Download size**: `53.07 MiB`

*   **Dataset size**: `100.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 44,749

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20201201 dump.

*   **Download size**: `29.73 MiB`

*   **Dataset size**: `46.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 61,009

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20201201
    dump.

*   **Download size**: `2.07 MiB`

*   **Dataset size**: `2.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,021

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20201201
    dump.

*   **Download size**: `3.91 MiB`

*   **Dataset size**: `2.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,525

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20201201 dump.

*   **Download size**: `8.95 MiB`

*   **Dataset size**: `12.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,270

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20201201 dump.

*   **Download size**: `268.72 MiB`

*   **Dataset size**: `397.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 226,449

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20201201
    dump.

*   **Download size**: `2.16 MiB`

*   **Dataset size**: `4.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,001

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20201201 dump.

*   **Download size**: `3.81 MiB`

*   **Dataset size**: `5.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,887

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20201201
    dump.

*   **Download size**: `6.70 MiB`

*   **Dataset size**: `29.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,482

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20201201
    dump.

*   **Download size**: `3.02 MiB`

*   **Dataset size**: `4.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,335

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.got

*   **Config description**: Wikipedia dataset for got, parsed from 20201201
    dump.

*   **Download size**: `699.97 KiB`

*   **Dataset size**: `1.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 955

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20201201 dump.

*   **Download size**: `29.64 MiB`

*   **Dataset size**: `108.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,449

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20201201 dump.

*   **Download size**: `5.47 MiB`

*   **Dataset size**: `4.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,036

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20201201 dump.

*   **Download size**: `5.19 MiB`

*   **Dataset size**: `7.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,017

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20201201
    dump.

*   **Download size**: `3.84 MiB`

*   **Dataset size**: `4.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,053

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20201201
    dump.

*   **Download size**: `1.05 MiB`

*   **Dataset size**: `1.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,516

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.he

*   **Config description**: Wikipedia dataset for he, parsed from 20201201 dump.

*   **Download size**: `690.54 MiB`

*   **Dataset size**: `1.48 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 454,321

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20201201 dump.

*   **Download size**: `166.88 MiB`

*   **Dataset size**: `545.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 178,324

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20201201
    dump.

*   **Download size**: `4.88 MiB`

*   **Dataset size**: `4.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,118

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20201201 dump.

*   **Download size**: `19.30 KiB`

*   **Dataset size**: `3.27 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20201201 dump.

*   **Download size**: `277.38 MiB`

*   **Dataset size**: `408.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 254,662

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20201201
    dump.

*   **Download size**: `10.84 MiB`

*   **Dataset size**: `14.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,025

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20201201 dump.

*   **Download size**: `14.88 MiB`

*   **Dataset size**: `42.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 61,756

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20201201 dump.

*   **Download size**: `909.08 MiB`

*   **Dataset size**: `1.25 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 673,740

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20201201 dump.

*   **Download size**: `357.39 MiB`

*   **Dataset size**: `967.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 627,523

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20201201 dump.

*   **Download size**: `9.15 MiB`

*   **Dataset size**: `11.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,254

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.id

*   **Config description**: Wikipedia dataset for id, parsed from 20201201 dump.

*   **Download size**: `658.39 MiB`

*   **Dataset size**: `865.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,077,758

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20201201 dump.

*   **Download size**: `2.18 MiB`

*   **Dataset size**: `3.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,272

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20201201 dump.

*   **Download size**: `2.14 MiB`

*   **Dataset size**: `2.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,426

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20201201 dump.

*   **Download size**: `31.96 KiB`

*   **Dataset size**: `8.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20201201 dump.

*   **Download size**: `257.86 KiB`

*   **Dataset size**: `93.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 668

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20201201
    dump.

*   **Download size**: `18.14 MiB`

*   **Dataset size**: `15.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,390

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20201201
    dump.

*   **Download size**: `2.98 MiB`

*   **Dataset size**: `1.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,017

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.io

*   **Config description**: Wikipedia dataset for io, parsed from 20201201 dump.

*   **Download size**: `13.81 MiB`

*   **Dataset size**: `30.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,448

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.is

*   **Config description**: Wikipedia dataset for is, parsed from 20201201 dump.

*   **Download size**: `47.31 MiB`

*   **Dataset size**: `73.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 73,114

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.it

*   **Config description**: Wikipedia dataset for it, parsed from 20201201 dump.

*   **Download size**: `3.03 GiB`

*   **Dataset size**: `3.91 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,001,603

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20201201 dump.

*   **Download size**: `311.91 KiB`

*   **Dataset size**: `148.25 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 587

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20201201 dump.

*   **Download size**: `3.14 GiB`

*   **Dataset size**: `5.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,529,692

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20201201
    dump.

*   **Download size**: `925.16 KiB`

*   **Dataset size**: `1.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20201201
    dump.

*   **Download size**: `1.13 MiB`

*   **Dataset size**: `2.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,330

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20201201 dump.

*   **Download size**: `46.35 MiB`

*   **Dataset size**: `57.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,598

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20201201 dump.

*   **Download size**: `159.31 MiB`

*   **Dataset size**: `543.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 182,623

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20201201
    dump.

*   **Download size**: `1.44 MiB`

*   **Dataset size**: `1.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,197

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20201201
    dump.

*   **Download size**: `3.55 MiB`

*   **Dataset size**: `3.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20201201
    dump.

*   **Download size**: `1.69 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,607

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20201201
    dump.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `3.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,915

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20201201 dump.

*   **Download size**: `484.12 KiB`

*   **Dataset size**: `292.64 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,271

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20201201 dump.

*   **Download size**: `390.92 KiB`

*   **Dataset size**: `309.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20201201 dump.

*   **Download size**: `17.54 KiB`

*   **Dataset size**: `4.93 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20201201 dump.

*   **Download size**: `120.88 MiB`

*   **Dataset size**: `424.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 270,628

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20201201 dump.

*   **Download size**: `654.67 KiB`

*   **Dataset size**: `447.23 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 867

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.km

*   **Config description**: Wikipedia dataset for km, parsed from 20201201 dump.

*   **Download size**: `25.74 MiB`

*   **Dataset size**: `150.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,995

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20201201 dump.

*   **Download size**: `76.13 MiB`

*   **Dataset size**: `333.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 27,325

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20201201 dump.

*   **Download size**: `747.33 MiB`

*   **Dataset size**: `1.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,139,678

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20201201
    dump.

*   **Download size**: `2.26 MiB`

*   **Dataset size**: `4.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,967

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20201201
    dump.

*   **Download size**: `3.25 MiB`

*   **Dataset size**: `4.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,341

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20201201 dump.

*   **Download size**: `363.64 KiB`

*   **Dataset size**: `199.02 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 509

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20201201
    dump.

*   **Download size**: `3.18 MiB`

*   **Dataset size**: `2.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,409

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20201201 dump.

*   **Download size**: `21.18 MiB`

*   **Dataset size**: `28.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,802

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20201201 dump.

*   **Download size**: `3.58 MiB`

*   **Dataset size**: `8.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,790

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20201201 dump.

*   **Download size**: `2.42 MiB`

*   **Dataset size**: `2.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,524

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20201201 dump.

*   **Download size**: `34.15 MiB`

*   **Dataset size**: `147.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,798

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.la

*   **Config description**: Wikipedia dataset for la, parsed from 20201201 dump.

*   **Download size**: `89.33 MiB`

*   **Dataset size**: `128.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 134,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20201201
    dump.

*   **Download size**: `3.41 MiB`

*   **Dataset size**: `4.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,957

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20201201 dump.

*   **Download size**: `49.54 MiB`

*   **Dataset size**: `78.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,562

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20201201
    dump.

*   **Download size**: `1.39 MiB`

*   **Dataset size**: `644.30 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,554

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20201201
    dump.

*   **Download size**: `4.75 MiB`

*   **Dataset size**: `8.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20201201
    dump.

*   **Download size**: `4.00 MiB`

*   **Dataset size**: `8.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,647

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20201201 dump.

*   **Download size**: `1.69 MiB`

*   **Dataset size**: `3.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,405

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.li

*   **Config description**: Wikipedia dataset for li, parsed from 20201201 dump.

*   **Download size**: `15.16 MiB`

*   **Dataset size**: `26.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,238

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20201201
    dump.

*   **Download size**: `3.94 MiB`

*   **Dataset size**: `5.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,441

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20201201
    dump.

*   **Download size**: `24.17 MiB`

*   **Dataset size**: `32.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 51,386

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20201201 dump.

*   **Download size**: `1.94 MiB`

*   **Dataset size**: `1.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,294

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20201201 dump.

*   **Download size**: `4.56 MiB`

*   **Dataset size**: `12.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,536

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20201201
    dump.

*   **Download size**: `6.94 MiB`

*   **Dataset size**: `4.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,216

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20201201 dump.

*   **Download size**: `188.31 MiB`

*   **Dataset size**: `293.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 226,648

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20201201
    dump.

*   **Download size**: `900.39 KiB`

*   **Dataset size**: `860.83 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,005

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20201201 dump.

*   **Download size**: `145.93 MiB`

*   **Dataset size**: `179.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 104,487

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20201201
    dump.

*   **Download size**: `11.77 MiB`

*   **Dataset size**: `18.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,891

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20201201
    dump.

*   **Download size**: `4.65 MiB`

*   **Dataset size**: `4.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,882

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20201201
    dump.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `1.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20201201 dump.

*   **Download size**: `27.85 MiB`

*   **Dataset size**: `63.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 129,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20201201 dump.

*   **Download size**: `28.69 KiB`

*   **Dataset size**: `11.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20201201
    dump.

*   **Download size**: `6.15 MiB`

*   **Dataset size**: `16.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20201201 dump.

*   **Download size**: `2.04 MiB`

*   **Dataset size**: `3.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,203

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.min

*   **Config description**: Wikipedia dataset for min, parsed from 20201201
    dump.

*   **Download size**: `29.45 MiB`

*   **Dataset size**: `99.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 228,196

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20201201 dump.

*   **Download size**: `166.60 MiB`

*   **Dataset size**: `465.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 150,831

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20201201 dump.

*   **Download size**: `143.17 MiB`

*   **Dataset size**: `369.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 131,128

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20201201 dump.

*   **Download size**: `32.25 MiB`

*   **Dataset size**: `73.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,077

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20201201 dump.

*   **Download size**: `58.88 MiB`

*   **Dataset size**: `170.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 112,917

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20201201
    dump.

*   **Download size**: `3.20 MiB`

*   **Dataset size**: `8.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,810

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20201201 dump.

*   **Download size**: `250.50 MiB`

*   **Dataset size**: `341.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 386,945

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20201201 dump.

*   **Download size**: `9.06 MiB`

*   **Dataset size**: `13.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,967

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20201201
    dump.

*   **Download size**: `15.13 KiB`

*   **Dataset size**: `875 bytes`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20201201
    dump.

*   **Download size**: `9.19 MiB`

*   **Dataset size**: `18.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.my

*   **Config description**: Wikipedia dataset for my, parsed from 20201201 dump.

*   **Download size**: `42.95 MiB`

*   **Dataset size**: `195.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 54,562

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20201201
    dump.

*   **Download size**: `9.65 MiB`

*   **Dataset size**: `8.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,155

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20201201
    dump.

*   **Download size**: `6.80 MiB`

*   **Dataset size**: `11.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,599

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.na

*   **Config description**: Wikipedia dataset for na, parsed from 20201201 dump.

*   **Download size**: `531.75 KiB`

*   **Dataset size**: `357.01 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,576

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20201201
    dump.

*   **Download size**: `4.51 MiB`

*   **Dataset size**: `7.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,714

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20201201
    dump.

*   **Download size**: `5.31 MiB`

*   **Dataset size**: `5.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20201201
    dump.

*   **Download size**: `42.06 MiB`

*   **Dataset size**: `85.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 87,896

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20201201
    dump.

*   **Download size**: `7.29 MiB`

*   **Dataset size**: `11.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,429

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20201201 dump.

*   **Download size**: `37.50 MiB`

*   **Dataset size**: `88.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 32,310

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.new

*   **Config description**: Wikipedia dataset for new, parsed from 20201201
    dump.

*   **Download size**: `17.27 MiB`

*   **Dataset size**: `140.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 72,998

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20201201 dump.

*   **Download size**: `92.26 KiB`

*   **Dataset size**: `66.12 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20201201 dump.

*   **Download size**: `1.53 GiB`

*   **Dataset size**: `2.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,523,440

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20201201 dump.

*   **Download size**: `139.43 MiB`

*   **Dataset size**: `208.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 231,090

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.no

*   **Config description**: Wikipedia dataset for no, parsed from 20201201 dump.

*   **Download size**: `649.54 MiB`

*   **Dataset size**: `890.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 847,202

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20201201
    dump.

*   **Download size**: `1.16 MiB`

*   **Dataset size**: `810.66 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,792

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20201201
    dump.

*   **Download size**: `1.86 MiB`

*   **Dataset size**: `2.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,541

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20201201
    dump.

*   **Download size**: `2.29 MiB`

*   **Dataset size**: `2.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,282

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20201201 dump.

*   **Download size**: `4.32 MiB`

*   **Dataset size**: `10.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,855

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20201201 dump.

*   **Download size**: `1.45 MiB`

*   **Dataset size**: `963.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 850

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20201201 dump.

*   **Download size**: `75.53 MiB`

*   **Dataset size**: `111.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 94,068

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20201201
    dump.

*   **Download size**: `1.95 MiB`

*   **Dataset size**: `2.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,508

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.om

*   **Config description**: Wikipedia dataset for om, parsed from 20201201 dump.

*   **Download size**: `1.26 MiB`

*   **Dataset size**: `1.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,163

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.or

*   **Config description**: Wikipedia dataset for or, parsed from 20201201 dump.

*   **Download size**: `28.60 MiB`

*   **Dataset size**: `59.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,029

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.os

*   **Config description**: Wikipedia dataset for os, parsed from 20201201 dump.

*   **Download size**: `9.08 MiB`

*   **Dataset size**: `9.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,964

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20201201 dump.

*   **Download size**: `49.00 MiB`

*   **Dataset size**: `129.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 44,984

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20201201
    dump.

*   **Download size**: `1.66 MiB`

*   **Dataset size**: `1.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,942

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20201201
    dump.

*   **Download size**: `9.11 MiB`

*   **Dataset size**: `7.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,794

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20201201
    dump.

*   **Download size**: `1.50 MiB`

*   **Dataset size**: `2.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,179

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20201201
    dump.

*   **Download size**: `4.89 MiB`

*   **Dataset size**: `4.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,113

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20201201
    dump.

*   **Download size**: `1.16 MiB`

*   **Dataset size**: `1.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,424

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20201201
    dump.

*   **Download size**: `3.51 MiB`

*   **Dataset size**: `3.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,933

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20201201 dump.

*   **Download size**: `631.83 KiB`

*   **Dataset size**: `2.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,074

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20201201
    dump.

*   **Download size**: `750.70 KiB`

*   **Dataset size**: `230.96 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 844

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20201201 dump.

*   **Download size**: `1.98 GiB`

*   **Dataset size**: `2.46 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,765,088

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20201201
    dump.

*   **Download size**: `13.90 MiB`

*   **Dataset size**: `30.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,115

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20201201
    dump.

*   **Download size**: `72.45 MiB`

*   **Dataset size**: `209.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 64,698

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20201201
    dump.

*   **Download size**: `549.36 KiB`

*   **Dataset size**: `590.82 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 532

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20201201 dump.

*   **Download size**: `21.45 MiB`

*   **Dataset size**: `46.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,138

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20201201 dump.

*   **Download size**: `1.79 GiB`

*   **Dataset size**: `2.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,491,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20201201 dump.

*   **Download size**: `12.49 MiB`

*   **Dataset size**: `15.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,387

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20201201 dump.

*   **Download size**: `6.92 MiB`

*   **Dataset size**: `16.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,863

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20201201
    dump.

*   **Download size**: `553.83 KiB`

*   **Dataset size**: `396.09 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 733

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20201201 dump.

*   **Download size**: `815.81 KiB`

*   **Dataset size**: `361.36 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 713

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20201201 dump.

*   **Download size**: `502.59 MiB`

*   **Dataset size**: `693.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 414,477

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20201201
    dump.

*   **Download size**: `1002.33 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20201201
    dump.

*   **Download size**: `6.20 MiB`

*   **Dataset size**: `6.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,375

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20201201 dump.

*   **Download size**: `4.02 GiB`

*   **Dataset size**: `8.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,732,016

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20201201
    dump.

*   **Download size**: `5.41 MiB`

*   **Dataset size**: `9.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20201201 dump.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `1.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20201201 dump.

*   **Download size**: `15.19 MiB`

*   **Dataset size**: `58.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 22,040

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20201201
    dump.

*   **Download size**: `13.61 MiB`

*   **Dataset size**: `35.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,796

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20201201
    dump.

*   **Download size**: `10.00 MiB`

*   **Dataset size**: `23.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,480

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20201201 dump.

*   **Download size**: `6.11 MiB`

*   **Dataset size**: `9.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20201201
    dump.

*   **Download size**: `12.05 MiB`

*   **Dataset size**: `16.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,416

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20201201
    dump.

*   **Download size**: `57.27 MiB`

*   **Dataset size**: `47.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,615

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20201201 dump.

*   **Download size**: `17.62 MiB`

*   **Dataset size**: `31.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20,282

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.se

*   **Config description**: Wikipedia dataset for se, parsed from 20201201 dump.

*   **Download size**: `3.88 MiB`

*   **Dataset size**: `3.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,561

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20201201 dump.

*   **Download size**: `313.06 KiB`

*   **Dataset size**: `93.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 295

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20201201 dump.

*   **Download size**: `423.87 MiB`

*   **Dataset size**: `822.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,935,417

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.si

*   **Config description**: Wikipedia dataset for si, parsed from 20201201 dump.

*   **Download size**: `41.32 MiB`

*   **Dataset size**: `112.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 27,846

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20201201
    dump.

*   **Download size**: `193.55 MiB`

*   **Dataset size**: `197.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 177,615

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20201201 dump.

*   **Download size**: `275.53 MiB`

*   **Dataset size**: `356.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 253,372

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20201201 dump.

*   **Download size**: `228.16 MiB`

*   **Dataset size**: `360.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20201201 dump.

*   **Download size**: `839.52 KiB`

*   **Dataset size**: `750.10 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,023

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20201201 dump.

*   **Download size**: `2.97 MiB`

*   **Dataset size**: `4.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.so

*   **Config description**: Wikipedia dataset for so, parsed from 20201201 dump.

*   **Download size**: `9.13 MiB`

*   **Dataset size**: `9.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,979

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20201201 dump.

*   **Download size**: `92.58 MiB`

*   **Dataset size**: `153.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 111,846

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20201201 dump.

*   **Download size**: `825.89 MiB`

*   **Dataset size**: `1.58 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,116,253

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20201201
    dump.

*   **Download size**: `655.77 KiB`

*   **Dataset size**: `614.35 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,253

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20201201 dump.

*   **Download size**: `827.67 KiB`

*   **Dataset size**: `490.69 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 554

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.st

*   **Config description**: Wikipedia dataset for st, parsed from 20201201 dump.

*   **Download size**: `673.61 KiB`

*   **Dataset size**: `580.35 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,136

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20201201
    dump.

*   **Download size**: `3.44 MiB`

*   **Dataset size**: `4.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,510

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.su

*   **Config description**: Wikipedia dataset for su, parsed from 20201201 dump.

*   **Download size**: `25.46 MiB`

*   **Dataset size**: `40.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,493

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20201201 dump.

*   **Download size**: `1.67 GiB`

*   **Dataset size**: `2.79 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,750,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20201201 dump.

*   **Download size**: `33.18 MiB`

*   **Dataset size**: `52.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 60,185

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20201201
    dump.

*   **Download size**: `11.88 MiB`

*   **Dataset size**: `17.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 53,270

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20201201 dump.

*   **Download size**: `165.13 MiB`

*   **Dataset size**: `632.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 167,112

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20201201
    dump.

*   **Download size**: `3.64 MiB`

*   **Dataset size**: `7.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,684

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.te

*   **Config description**: Wikipedia dataset for te, parsed from 20201201 dump.

*   **Download size**: `110.19 MiB`

*   **Dataset size**: `591.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 94,652

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20201201
    dump.

*   **Download size**: `1.25 MiB`

*   **Dataset size**: `1.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,602

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20201201 dump.

*   **Download size**: `42.76 MiB`

*   **Dataset size**: `110.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 105,298

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.th

*   **Config description**: Wikipedia dataset for th, parsed from 20201201 dump.

*   **Download size**: `290.74 MiB`

*   **Dataset size**: `823.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 245,869

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20201201 dump.

*   **Download size**: `533.37 KiB`

*   **Dataset size**: `376.02 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 369

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20201201 dump.

*   **Download size**: `5.03 MiB`

*   **Dataset size**: `10.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,122

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20201201 dump.

*   **Download size**: `61.86 MiB`

*   **Dataset size**: `66.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 64,930

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20201201 dump.

*   **Download size**: `1.42 MiB`

*   **Dataset size**: `1.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.to

*   **Config description**: Wikipedia dataset for to, parsed from 20201201 dump.

*   **Download size**: `818.38 KiB`

*   **Dataset size**: `921.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,628

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20201201
    dump.

*   **Download size**: `1.45 MiB`

*   **Dataset size**: `408.34 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,656

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20201201 dump.

*   **Download size**: `613.30 MiB`

*   **Dataset size**: `724.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 624,333

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20201201 dump.

*   **Download size**: `1.59 MiB`

*   **Dataset size**: `713.63 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 713

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20201201 dump.

*   **Download size**: `75.07 MiB`

*   **Dataset size**: `248.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 278,882

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20201201
    dump.

*   **Download size**: `352.25 KiB`

*   **Dataset size**: `231.66 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 718

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20201201 dump.

*   **Download size**: `449.69 KiB`

*   **Dataset size**: `339.91 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 782

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20201201 dump.

*   **Download size**: `517.96 KiB`

*   **Dataset size**: `260.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20201201
    dump.

*   **Download size**: `4.59 MiB`

*   **Dataset size**: `11.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20201201
    dump.

*   **Download size**: `3.39 MiB`

*   **Dataset size**: `6.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,191

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20201201 dump.

*   **Download size**: `7.70 MiB`

*   **Dataset size**: `36.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,258

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20201201 dump.

*   **Download size**: `1.60 GiB`

*   **Dataset size**: `3.66 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,611,728

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20201201 dump.

*   **Download size**: `162.89 MiB`

*   **Dataset size**: `264.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 350,090

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20201201 dump.

*   **Download size**: `67.47 MiB`

*   **Dataset size**: `99.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 158,823

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20201201 dump.

*   **Download size**: `283.99 KiB`

*   **Dataset size**: `219.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 446

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20201201
    dump.

*   **Download size**: `21.88 MiB`

*   **Dataset size**: `28.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 71,790

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20201201
    dump.

*   **Download size**: `6.30 MiB`

*   **Dataset size**: `9.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,027

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20201201 dump.

*   **Download size**: `793.00 MiB`

*   **Dataset size**: `1.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,465,721

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20201201
    dump.

*   **Download size**: `7.03 MiB`

*   **Dataset size**: `10.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,778

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20201201 dump.

*   **Download size**: `24.97 MiB`

*   **Dataset size**: `80.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 125,494

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20201201 dump.

*   **Download size**: `8.29 MiB`

*   **Dataset size**: `12.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,373

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.war

*   **Config description**: Wikipedia dataset for war, parsed from 20201201
    dump.

*   **Download size**: `263.43 MiB`

*   **Dataset size**: `412.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,264,845

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20201201 dump.

*   **Download size**: `1.97 MiB`

*   **Dataset size**: `3.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,664

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20201201
    dump.

*   **Download size**: `15.28 MiB`

*   **Dataset size**: `20.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,762

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20201201
    dump.

*   **Download size**: `1.71 MiB`

*   **Dataset size**: `1.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,801

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20201201 dump.

*   **Download size**: `1.52 MiB`

*   **Dataset size**: `1.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,373

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20201201
    dump.

*   **Download size**: `11.13 MiB`

*   **Dataset size**: `26.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,061

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20201201 dump.

*   **Download size**: `12.62 MiB`

*   **Dataset size**: `33.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,227

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20201201 dump.

*   **Download size**: `14.22 MiB`

*   **Dataset size**: `12.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 33,548

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.za

*   **Config description**: Wikipedia dataset for za, parsed from 20201201 dump.

*   **Download size**: `791.45 KiB`

*   **Dataset size**: `721.42 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,496

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20201201
    dump.

*   **Download size**: `2.56 MiB`

*   **Dataset size**: `4.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,599

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20201201 dump.

*   **Download size**: `2.05 GiB`

*   **Dataset size**: `2.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,670,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20201201 dump.

*   **Download size**: `14.89 MiB`

*   **Dataset size**: `10.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,237

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20201201 dump.

*   **Download size**: `73.64 MiB`

*   **Dataset size**: `130.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 448,229

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20201201
    dump.

*   **Download size**: `67.14 MiB`

*   **Dataset size**: `71.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 103,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20201201 dump.

*   **Download size**: `2.43 MiB`

*   **Dataset size**: `2.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20200301 dump.

*   **Download size**: `44.96 KiB`

*   **Dataset size**: `3.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20200301 dump.

*   **Download size**: `1.74 MiB`

*   **Dataset size**: `2.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,108

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20200301
    dump.

*   **Download size**: `2.93 MiB`

*   **Dataset size**: `3.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,501

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20200301
    dump.

*   **Download size**: `394.09 KiB`

*   **Dataset size**: `505.97 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 553

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20200301 dump.

*   **Download size**: `99.17 MiB`

*   **Dataset size**: `179.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 110,483

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20200301 dump.

*   **Download size**: `462.66 KiB`

*   **Dataset size**: `247.24 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 993

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20200301
    dump.

*   **Download size**: `51.03 MiB`

*   **Dataset size**: `68.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,318

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20200301 dump.

*   **Download size**: `6.82 MiB`

*   **Dataset size**: `16.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20200301 dump.

*   **Download size**: `32.94 MiB`

*   **Dataset size**: `46.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50,774

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20200301
    dump.

*   **Download size**: `4.13 MiB`

*   **Dataset size**: `2.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,249

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20200301 dump.

*   **Download size**: `1.08 GiB`

*   **Dataset size**: `2.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,972,799

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20200301
    dump.

*   **Download size**: `1.03 MiB`

*   **Dataset size**: `778.26 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,305

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20200301
    dump.

*   **Download size**: `36.61 MiB`

*   **Dataset size**: `115.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 157,001

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20200301 dump.

*   **Download size**: `21.48 MiB`

*   **Dataset size**: `40.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,509

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20200301
    dump.

*   **Download size**: `217.68 MiB`

*   **Dataset size**: `445.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 108,220

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20200301
    dump.

*   **Download size**: `546.89 KiB`

*   **Dataset size**: `664.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,175

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20200301 dump.

*   **Download size**: `4.47 MiB`

*   **Dataset size**: `3.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,075

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20200301 dump.

*   **Download size**: `2.19 MiB`

*   **Dataset size**: `4.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,039

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20200301 dump.

*   **Download size**: `181.30 MiB`

*   **Dataset size**: `317.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 175,038

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20200301
    dump.

*   **Download size**: `76.38 MiB`

*   **Dataset size**: `131.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 208,456

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20200301 dump.

*   **Download size**: `64.46 MiB`

*   **Dataset size**: `181.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 56,822

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20200301
    dump.

*   **Download size**: `32.17 MiB`

*   **Dataset size**: `40.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 46,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20200301
    dump.

*   **Download size**: `4.82 MiB`

*   **Dataset size**: `6.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,665

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20200301
    dump.

*   **Download size**: `7.59 MiB`

*   **Dataset size**: `8.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,581

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20200301 dump.

*   **Download size**: `208.69 MiB`

*   **Dataset size**: `433.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 185,758

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20200301
    dump.

*   **Download size**: `79.73 MiB`

*   **Dataset size**: `178.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 99,513

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20200301 dump.

*   **Download size**: `344.69 MiB`

*   **Dataset size**: `866.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 377,391

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20200301 dump.

*   **Download size**: `13.79 MiB`

*   **Dataset size**: `10.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,035

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20200301 dump.

*   **Download size**: `444.50 KiB`

*   **Dataset size**: `298.56 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,392

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20200301
    dump.

*   **Download size**: `2.68 MiB`

*   **Dataset size**: `2.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,431

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20200301 dump.

*   **Download size**: `464.48 KiB`

*   **Dataset size**: `351.32 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 745

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20200301 dump.

*   **Download size**: `183.92 MiB`

*   **Dataset size**: `482.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 119,216

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20200301 dump.

*   **Download size**: `13.17 MiB`

*   **Dataset size**: `116.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,575

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20200301
    dump.

*   **Download size**: `5.11 MiB`

*   **Dataset size**: `39.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,416

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20200301 dump.

*   **Download size**: `50.39 MiB`

*   **Dataset size**: `72.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 77,940

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20200301 dump.

*   **Download size**: `110.31 MiB`

*   **Dataset size**: `150.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 185,885

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20200301
    dump.

*   **Download size**: `1.82 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,411

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20200301
    dump.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `5.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,653

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20200301 dump.

*   **Download size**: `899.00 MiB`

*   **Dataset size**: `1.50 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 698,894

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20200301
    dump.

*   **Download size**: `1.86 MiB`

*   **Dataset size**: `2.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20200301
    dump.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `3.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,785

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20200301 dump.

*   **Download size**: `49.70 MiB`

*   **Dataset size**: `254.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 259,152

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20200301
    dump.

*   **Download size**: `1.84 GiB`

*   **Dataset size**: `3.68 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,378,741

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20200301 dump.

*   **Download size**: `707.12 KiB`

*   **Dataset size**: `167.80 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 541

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20200301
    dump.

*   **Download size**: `26.88 KiB`

*   **Dataset size**: `7.44 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20200301
    dump.

*   **Download size**: `644.28 KiB`

*   **Dataset size**: `629.37 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 962

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20200301
    dump.

*   **Download size**: `340.35 KiB`

*   **Dataset size**: `116.39 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 780

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20200301
    dump.

*   **Download size**: `26.96 MiB`

*   **Dataset size**: `46.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,695

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20200301 dump.

*   **Download size**: `3.54 MiB`

*   **Dataset size**: `5.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,465

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20200301 dump.

*   **Download size**: `271.60 KiB`

*   **Dataset size**: `31.60 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 120

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20200301
    dump.

*   **Download size**: `4.38 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,093

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20200301 dump.

*   **Download size**: `825.14 MiB`

*   **Dataset size**: `1.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 574,136

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20200301
    dump.

*   **Download size**: `2.13 MiB`

*   **Dataset size**: `3.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,696

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20200301 dump.

*   **Download size**: `665.69 KiB`

*   **Dataset size**: `672.01 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20200301 dump.

*   **Download size**: `23.37 MiB`

*   **Dataset size**: `59.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 45,907

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20200301 dump.

*   **Download size**: `69.14 MiB`

*   **Dataset size**: `100.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 147,899

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20200301 dump.

*   **Download size**: `341.55 MiB`

*   **Dataset size**: `457.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 257,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20200301 dump.

*   **Download size**: `5.32 GiB`

*   **Dataset size**: `7.52 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,104,703

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20200301
    dump.

*   **Download size**: `490.49 KiB`

*   **Dataset size**: `462.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20200301
    dump.

*   **Download size**: `8.36 MiB`

*   **Dataset size**: `7.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,255

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20200301
    dump.

*   **Download size**: `3.73 MiB`

*   **Dataset size**: `3.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,495

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20200301
    dump.

*   **Download size**: `6.52 MiB`

*   **Dataset size**: `5.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,559

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20200301 dump.

*   **Download size**: `4.35 MiB`

*   **Dataset size**: `12.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,262

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20200301 dump.

*   **Download size**: `377.61 KiB`

*   **Dataset size**: `799.74 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 294

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20200301 dump.

*   **Download size**: `460.80 KiB`

*   **Dataset size**: `207.60 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 381

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20200301 dump.

*   **Download size**: `359.36 MiB`

*   **Dataset size**: `937.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 244,313

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20200301
    dump.

*   **Download size**: `8.14 MiB`

*   **Dataset size**: `3.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,208

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20200301 dump.

*   **Download size**: `16.73 GiB`

*   **Dataset size**: `17.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 6,033,151

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20200301 dump.

*   **Download size**: `264.90 MiB`

*   **Dataset size**: `405.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 379,859

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20200301 dump.

*   **Download size**: `3.16 GiB`

*   **Dataset size**: `4.58 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,837,472

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20200301 dump.

*   **Download size**: `211.83 MiB`

*   **Dataset size**: `352.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 317,330

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20200301 dump.

*   **Download size**: `195.51 MiB`

*   **Dataset size**: `386.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 437,022

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20200301
    dump.

*   **Download size**: `2.50 MiB`

*   **Dataset size**: `3.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20200301 dump.

*   **Download size**: `769.97 MiB`

*   **Dataset size**: `1.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,316,555

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20200301 dump.

*   **Download size**: `417.26 KiB`

*   **Dataset size**: `280.51 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 313

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20200301 dump.

*   **Download size**: `703.73 MiB`

*   **Dataset size**: `923.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 656,462

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20200301
    dump.

*   **Download size**: `2.06 MiB`

*   **Dataset size**: `3.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,132

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20200301 dump.

*   **Download size**: `400.67 KiB`

*   **Dataset size**: `278.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 853

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20200301 dump.

*   **Download size**: `14.07 MiB`

*   **Dataset size**: `13.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,325

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20200301 dump.

*   **Download size**: `4.46 GiB`

*   **Dataset size**: `6.00 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,186,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20200301
    dump.

*   **Download size**: `2.19 MiB`

*   **Dataset size**: `1.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,937

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20200301
    dump.

*   **Download size**: `8.73 MiB`

*   **Dataset size**: `5.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,448

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20200301
    dump.

*   **Download size**: `2.33 MiB`

*   **Dataset size**: `3.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,563

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20200301 dump.

*   **Download size**: `49.88 MiB`

*   **Dataset size**: `94.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,510

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20200301 dump.

*   **Download size**: `27.12 MiB`

*   **Dataset size**: `43.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 58,490

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20200301
    dump.

*   **Download size**: `2.04 MiB`

*   **Dataset size**: `2.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,011

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20200301
    dump.

*   **Download size**: `3.85 MiB`

*   **Dataset size**: `2.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,513

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20200301 dump.

*   **Download size**: `8.72 MiB`

*   **Dataset size**: `12.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,158

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20200301 dump.

*   **Download size**: `254.09 MiB`

*   **Dataset size**: `376.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 215,685

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20200301
    dump.

*   **Download size**: `2.02 MiB`

*   **Dataset size**: `4.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,784

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20200301 dump.

*   **Download size**: `3.50 MiB`

*   **Dataset size**: `5.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,493

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20200301
    dump.

*   **Download size**: `6.24 MiB`

*   **Dataset size**: `29.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,436

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20200301
    dump.

*   **Download size**: `1.67 MiB`

*   **Dataset size**: `2.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,006

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20200301
    dump.

*   **Download size**: `673.14 KiB`

*   **Dataset size**: `1.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 940

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20200301 dump.

*   **Download size**: `28.55 MiB`

*   **Dataset size**: `106.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,103

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20200301 dump.

*   **Download size**: `5.36 MiB`

*   **Dataset size**: `4.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,020

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20200301 dump.

*   **Download size**: `2.54 MiB`

*   **Dataset size**: `3.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,856

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20200301
    dump.

*   **Download size**: `3.74 MiB`

*   **Dataset size**: `3.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,894

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20200301
    dump.

*   **Download size**: `1.50 MiB`

*   **Dataset size**: `2.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,308

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20200301 dump.

*   **Download size**: `626.91 MiB`

*   **Dataset size**: `1.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 424,381

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20200301 dump.

*   **Download size**: `151.17 MiB`

*   **Dataset size**: `520.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 168,552

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20200301
    dump.

*   **Download size**: `4.62 MiB`

*   **Dataset size**: `4.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,054

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20200301 dump.

*   **Download size**: `19.24 KiB`

*   **Dataset size**: `3.27 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20200301 dump.

*   **Download size**: `261.83 MiB`

*   **Dataset size**: `389.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 243,050

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20200301
    dump.

*   **Download size**: `10.63 MiB`

*   **Dataset size**: `14.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,878

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20200301 dump.

*   **Download size**: `13.19 MiB`

*   **Dataset size**: `38.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 59,271

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20200301 dump.

*   **Download size**: `863.44 MiB`

*   **Dataset size**: `1.19 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 654,141

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20200301 dump.

*   **Download size**: `309.20 MiB`

*   **Dataset size**: `846.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 589,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20200301 dump.

*   **Download size**: `8.64 MiB`

*   **Dataset size**: `11.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,556

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20200301 dump.

*   **Download size**: `595.70 MiB`

*   **Dataset size**: `809.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,033,265

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20200301 dump.

*   **Download size**: `1.85 MiB`

*   **Dataset size**: `2.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,766

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20200301 dump.

*   **Download size**: `1.13 MiB`

*   **Dataset size**: `1.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,797

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20200301 dump.

*   **Download size**: `31.73 KiB`

*   **Dataset size**: `8.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20200301 dump.

*   **Download size**: `251.48 KiB`

*   **Dataset size**: `94.27 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 669

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20200301
    dump.

*   **Download size**: `16.98 MiB`

*   **Dataset size**: `14.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,221

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20200301
    dump.

*   **Download size**: `2.15 MiB`

*   **Dataset size**: `1.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,597

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20200301 dump.

*   **Download size**: `13.17 MiB`

*   **Dataset size**: `29.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20200301 dump.

*   **Download size**: `44.88 MiB`

*   **Dataset size**: `70.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 70,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20200301 dump.

*   **Download size**: `2.85 GiB`

*   **Dataset size**: `3.72 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,907,437

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20200301 dump.

*   **Download size**: `292.01 KiB`

*   **Dataset size**: `153.39 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 512

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20200301 dump.

*   **Download size**: `2.95 GiB`

*   **Dataset size**: `5.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,459,322

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20200301
    dump.

*   **Download size**: `908.86 KiB`

*   **Dataset size**: `1.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,708

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20200301
    dump.

*   **Download size**: `1.09 MiB`

*   **Dataset size**: `2.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,320

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20200301 dump.

*   **Download size**: `42.41 MiB`

*   **Dataset size**: `54.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 75,864

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20200301 dump.

*   **Download size**: `142.65 MiB`

*   **Dataset size**: `480.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 170,803

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20200301
    dump.

*   **Download size**: `1.38 MiB`

*   **Dataset size**: `1.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,183

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20200301
    dump.

*   **Download size**: `2.99 MiB`

*   **Dataset size**: `2.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,612

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20200301
    dump.

*   **Download size**: `1.67 MiB`

*   **Dataset size**: `2.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,611

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20200301
    dump.

*   **Download size**: `1.33 MiB`

*   **Dataset size**: `3.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,797

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20200301 dump.

*   **Download size**: `452.75 KiB`

*   **Dataset size**: `255.06 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,242

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20200301 dump.

*   **Download size**: `377.70 KiB`

*   **Dataset size**: `310.31 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20200301 dump.

*   **Download size**: `17.46 KiB`

*   **Dataset size**: `4.93 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20200301 dump.

*   **Download size**: `116.81 MiB`

*   **Dataset size**: `417.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 269,235

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20200301 dump.

*   **Download size**: `874.37 KiB`

*   **Dataset size**: `574.59 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,708

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20200301 dump.

*   **Download size**: `23.63 MiB`

*   **Dataset size**: `132.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,773

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20200301 dump.

*   **Download size**: `73.08 MiB`

*   **Dataset size**: `323.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 26,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20200301 dump.

*   **Download size**: `685.64 MiB`

*   **Dataset size**: `1.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,053,176

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20200301
    dump.

*   **Download size**: `2.18 MiB`

*   **Dataset size**: `4.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20200301
    dump.

*   **Download size**: `3.20 MiB`

*   **Dataset size**: `4.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,329

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20200301 dump.

*   **Download size**: `331.45 KiB`

*   **Dataset size**: `153.64 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 443

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20200301
    dump.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `2.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,375

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20200301 dump.

*   **Download size**: `18.20 MiB`

*   **Dataset size**: `24.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 34,513

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20200301 dump.

*   **Download size**: `3.46 MiB`

*   **Dataset size**: `8.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,759

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20200301 dump.

*   **Download size**: `1.92 MiB`

*   **Dataset size**: `1.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,027

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20200301 dump.

*   **Download size**: `33.38 MiB`

*   **Dataset size**: `146.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,687

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20200301 dump.

*   **Download size**: `85.88 MiB`

*   **Dataset size**: `123.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 132,256

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20200301
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `4.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,943

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20200301 dump.

*   **Download size**: `47.48 MiB`

*   **Dataset size**: `75.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 63,849

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20200301
    dump.

*   **Download size**: `1.30 MiB`

*   **Dataset size**: `643.83 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,549

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20200301
    dump.

*   **Download size**: `4.42 MiB`

*   **Dataset size**: `8.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,448

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20200301
    dump.

*   **Download size**: `3.65 MiB`

*   **Dataset size**: `7.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,308

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20200301 dump.

*   **Download size**: `1.59 MiB`

*   **Dataset size**: `3.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,365

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20200301 dump.

*   **Download size**: `14.58 MiB`

*   **Dataset size**: `25.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,721

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20200301
    dump.

*   **Download size**: `3.02 MiB`

*   **Dataset size**: `4.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,543

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20200301
    dump.

*   **Download size**: `21.87 MiB`

*   **Dataset size**: `28.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 45,704

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20200301 dump.

*   **Download size**: `1.89 MiB`

*   **Dataset size**: `1.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,265

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20200301 dump.

*   **Download size**: `4.24 MiB`

*   **Dataset size**: `11.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,463

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20200301
    dump.

*   **Download size**: `5.55 MiB`

*   **Dataset size**: `3.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,953

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20200301 dump.

*   **Download size**: `182.22 MiB`

*   **Dataset size**: `286.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 223,184

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20200301
    dump.

*   **Download size**: `878.96 KiB`

*   **Dataset size**: `860.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20200301 dump.

*   **Download size**: `137.56 MiB`

*   **Dataset size**: `170.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100,641

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20200301
    dump.

*   **Download size**: `11.43 MiB`

*   **Dataset size**: `18.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,774

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20200301
    dump.

*   **Download size**: `4.55 MiB`

*   **Dataset size**: `4.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,680

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20200301
    dump.

*   **Download size**: `1.14 MiB`

*   **Dataset size**: `1.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20200301 dump.

*   **Download size**: `26.66 MiB`

*   **Dataset size**: `61.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 128,813

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20200301 dump.

*   **Download size**: `28.59 KiB`

*   **Dataset size**: `11.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20200301
    dump.

*   **Download size**: `5.90 MiB`

*   **Dataset size**: `16.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,302

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20200301 dump.

*   **Download size**: `1.99 MiB`

*   **Dataset size**: `3.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,187

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20200301
    dump.

*   **Download size**: `27.69 MiB`

*   **Dataset size**: `98.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 227,688

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20200301 dump.

*   **Download size**: `152.75 MiB`

*   **Dataset size**: `432.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 145,820

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20200301 dump.

*   **Download size**: `130.77 MiB`

*   **Dataset size**: `340.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 123,672

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20200301 dump.

*   **Download size**: `30.40 MiB`

*   **Dataset size**: `71.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 24,252

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20200301 dump.

*   **Download size**: `53.71 MiB`

*   **Dataset size**: `149.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 101,310

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20200301
    dump.

*   **Download size**: `3.10 MiB`

*   **Dataset size**: `8.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,831

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20200301 dump.

*   **Download size**: `228.62 MiB`

*   **Dataset size**: `318.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 373,578

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20200301 dump.

*   **Download size**: `8.53 MiB`

*   **Dataset size**: `12.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,748

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20200301
    dump.

*   **Download size**: `15.08 KiB`

*   **Dataset size**: `875 bytes`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20200301
    dump.

*   **Download size**: `9.09 MiB`

*   **Dataset size**: `18.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,332

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20200301 dump.

*   **Download size**: `37.69 MiB`

*   **Dataset size**: `177.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,451

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20200301
    dump.

*   **Download size**: `8.87 MiB`

*   **Dataset size**: `7.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,566

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20200301
    dump.

*   **Download size**: `6.63 MiB`

*   **Dataset size**: `11.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20200301 dump.

*   **Download size**: `495.83 KiB`

*   **Dataset size**: `334.74 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,319

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20200301
    dump.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `7.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,672

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20200301
    dump.

*   **Download size**: `5.15 MiB`

*   **Dataset size**: `5.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,191

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20200301
    dump.

*   **Download size**: `37.74 MiB`

*   **Dataset size**: `75.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,024

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20200301
    dump.

*   **Download size**: `6.92 MiB`

*   **Dataset size**: `10.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,976

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20200301 dump.

*   **Download size**: `32.89 MiB`

*   **Dataset size**: `86.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 34,609

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20200301
    dump.

*   **Download size**: `16.96 MiB`

*   **Dataset size**: `140.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 72,895

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20200301 dump.

*   **Download size**: `91.98 KiB`

*   **Dataset size**: `66.12 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20200301 dump.

*   **Download size**: `1.45 GiB`

*   **Dataset size**: `2.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,464,920

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20200301 dump.

*   **Download size**: `132.55 MiB`

*   **Dataset size**: `200.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 225,543

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20200301 dump.

*   **Download size**: `619.74 MiB`

*   **Dataset size**: `861.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 822,320

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20200301
    dump.

*   **Download size**: `1.14 MiB`

*   **Dataset size**: `810.05 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,790

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20200301
    dump.

*   **Download size**: `1.74 MiB`

*   **Dataset size**: `2.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20200301
    dump.

*   **Download size**: `2.26 MiB`

*   **Dataset size**: `2.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,248

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20200301 dump.

*   **Download size**: `3.48 MiB`

*   **Dataset size**: `8.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,199

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20200301 dump.

*   **Download size**: `1.29 MiB`

*   **Dataset size**: `752.91 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 630

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20200301 dump.

*   **Download size**: `73.98 MiB`

*   **Dataset size**: `110.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 95,125

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20200301
    dump.

*   **Download size**: `1.80 MiB`

*   **Dataset size**: `2.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20200301 dump.

*   **Download size**: `1.10 MiB`

*   **Dataset size**: `1.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,099

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20200301 dump.

*   **Download size**: `26.72 MiB`

*   **Dataset size**: `55.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20200301 dump.

*   **Download size**: `7.76 MiB`

*   **Dataset size**: `9.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,078

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20200301 dump.

*   **Download size**: `45.93 MiB`

*   **Dataset size**: `118.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,772

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20200301
    dump.

*   **Download size**: `1.32 MiB`

*   **Dataset size**: `2.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,052

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20200301
    dump.

*   **Download size**: `8.19 MiB`

*   **Dataset size**: `7.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,729

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20200301
    dump.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `1.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,116

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20200301
    dump.

*   **Download size**: `4.54 MiB`

*   **Dataset size**: `4.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,839

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20200301
    dump.

*   **Download size**: `1.12 MiB`

*   **Dataset size**: `1.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20200301
    dump.

*   **Download size**: `3.39 MiB`

*   **Dataset size**: `3.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,886

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20200301 dump.

*   **Download size**: `606.15 KiB`

*   **Dataset size**: `2.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,068

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20200301
    dump.

*   **Download size**: `726.58 KiB`

*   **Dataset size**: `213.73 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20200301 dump.

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `2.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,694,759

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20200301
    dump.

*   **Download size**: `13.59 MiB`

*   **Dataset size**: `30.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,817

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20200301
    dump.

*   **Download size**: `38.95 MiB`

*   **Dataset size**: `97.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 57,145

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20200301
    dump.

*   **Download size**: `536.03 KiB`

*   **Dataset size**: `588.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 527

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20200301 dump.

*   **Download size**: `16.28 MiB`

*   **Dataset size**: `36.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,100

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20200301 dump.

*   **Download size**: `1.69 GiB`

*   **Dataset size**: `2.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,451,953

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20200301 dump.

*   **Download size**: `11.85 MiB`

*   **Dataset size**: `15.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20200301 dump.

*   **Download size**: `6.50 MiB`

*   **Dataset size**: `15.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,796

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20200301
    dump.

*   **Download size**: `530.59 KiB`

*   **Dataset size**: `367.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 709

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20200301 dump.

*   **Download size**: `796.83 KiB`

*   **Dataset size**: `347.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 701

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20200301 dump.

*   **Download size**: `478.19 MiB`

*   **Dataset size**: `661.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 405,150

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20200301
    dump.

*   **Download size**: `963.66 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,253

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20200301
    dump.

*   **Download size**: `5.98 MiB`

*   **Dataset size**: `6.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,297

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20200301 dump.

*   **Download size**: `3.77 GiB`

*   **Dataset size**: `7.62 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,592,128

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20200301
    dump.

*   **Download size**: `4.78 MiB`

*   **Dataset size**: `8.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,035

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20200301 dump.

*   **Download size**: `908.39 KiB`

*   **Dataset size**: `977.34 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,961

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20200301 dump.

*   **Download size**: `14.82 MiB`

*   **Dataset size**: `56.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21,969

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20200301
    dump.

*   **Download size**: `12.32 MiB`

*   **Dataset size**: `32.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,941

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20200301
    dump.

*   **Download size**: `6.21 MiB`

*   **Dataset size**: `13.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,060

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20200301 dump.

*   **Download size**: `5.01 MiB`

*   **Dataset size**: `7.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,567

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20200301
    dump.

*   **Download size**: `11.88 MiB`

*   **Dataset size**: `16.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20200301
    dump.

*   **Download size**: `61.94 MiB`

*   **Dataset size**: `54.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 56,522

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20200301 dump.

*   **Download size**: `15.68 MiB`

*   **Dataset size**: `28.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,865

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20200301 dump.

*   **Download size**: `3.66 MiB`

*   **Dataset size**: `3.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20200301 dump.

*   **Download size**: `299.28 KiB`

*   **Dataset size**: `95.17 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 290

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20200301 dump.

*   **Download size**: `412.87 MiB`

*   **Dataset size**: `814.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,930,504

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20200301 dump.

*   **Download size**: `38.91 MiB`

*   **Dataset size**: `106.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 26,983

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20200301
    dump.

*   **Download size**: `172.58 MiB`

*   **Dataset size**: `181.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 155,877

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20200301 dump.

*   **Download size**: `265.58 MiB`

*   **Dataset size**: `345.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 249,815

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20200301 dump.

*   **Download size**: `214.19 MiB`

*   **Dataset size**: `341.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 197,474

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20200301 dump.

*   **Download size**: `723.35 KiB`

*   **Dataset size**: `677.25 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 976

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20200301 dump.

*   **Download size**: `2.43 MiB`

*   **Dataset size**: `3.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,381

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20200301 dump.

*   **Download size**: `8.45 MiB`

*   **Dataset size**: `9.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,987

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20200301 dump.

*   **Download size**: `83.93 MiB`

*   **Dataset size**: `140.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 106,777

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20200301 dump.

*   **Download size**: `778.54 MiB`

*   **Dataset size**: `1.51 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,091,798

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20200301
    dump.

*   **Download size**: `644.18 KiB`

*   **Dataset size**: `620.41 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,249

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20200301 dump.

*   **Download size**: `795.23 KiB`

*   **Dataset size**: `469.17 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 533

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20200301 dump.

*   **Download size**: `558.97 KiB`

*   **Dataset size**: `332.01 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 753

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20200301
    dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `4.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20200301 dump.

*   **Download size**: `24.10 MiB`

*   **Dataset size**: `39.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,709

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20200301 dump.

*   **Download size**: `1.68 GiB`

*   **Dataset size**: `2.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,993,395

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20200301 dump.

*   **Download size**: `30.67 MiB`

*   **Dataset size**: `48.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 55,913

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20200301
    dump.

*   **Download size**: `11.53 MiB`

*   **Dataset size**: `17.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 52,672

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20200301 dump.

*   **Download size**: `154.80 MiB`

*   **Dataset size**: `604.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 161,622

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20200301
    dump.

*   **Download size**: `2.81 MiB`

*   **Dataset size**: `6.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,536

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20200301 dump.

*   **Download size**: `102.37 MiB`

*   **Dataset size**: `556.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 93,223

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20200301
    dump.

*   **Download size**: `1.25 MiB`

*   **Dataset size**: `1.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,600

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20200301 dump.

*   **Download size**: `39.93 MiB`

*   **Dataset size**: `106.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 101,637

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20200301 dump.

*   **Download size**: `271.37 MiB`

*   **Dataset size**: `789.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 235,109

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20200301 dump.

*   **Download size**: `365.94 KiB`

*   **Dataset size**: `369.20 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 347

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20200301 dump.

*   **Download size**: `4.61 MiB`

*   **Dataset size**: `9.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,869

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20200301 dump.

*   **Download size**: `54.88 MiB`

*   **Dataset size**: `61.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 75,676

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20200301 dump.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `1.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 828

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20200301 dump.

*   **Download size**: `797.75 KiB`

*   **Dataset size**: `911.82 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,623

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20200301
    dump.

*   **Download size**: `1.43 MiB`

*   **Dataset size**: `399.11 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,639

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20200301 dump.

*   **Download size**: `534.01 MiB`

*   **Dataset size**: `662.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 575,697

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20200301 dump.

*   **Download size**: `1.43 MiB`

*   **Dataset size**: `701.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 697

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20200301 dump.

*   **Download size**: `58.06 MiB`

*   **Dataset size**: `134.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 130,169

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20200301
    dump.

*   **Download size**: `333.38 KiB`

*   **Dataset size**: `212.55 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 708

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20200301 dump.

*   **Download size**: `413.61 KiB`

*   **Dataset size**: `290.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 766

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20200301 dump.

*   **Download size**: `502.60 KiB`

*   **Dataset size**: `249.88 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,285

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20200301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `7.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,879

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20200301
    dump.

*   **Download size**: `3.21 MiB`

*   **Dataset size**: `5.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,067

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20200301 dump.

*   **Download size**: `5.94 MiB`

*   **Dataset size**: `27.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,247

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20200301 dump.

*   **Download size**: `1.45 GiB`

*   **Dataset size**: `3.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,347,474

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20200301 dump.

*   **Download size**: `143.42 MiB`

*   **Dataset size**: `222.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 342,368

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20200301 dump.

*   **Download size**: `62.85 MiB`

*   **Dataset size**: `94.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 154,674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20200301 dump.

*   **Download size**: `278.29 KiB`

*   **Dataset size**: `210.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 450

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20200301
    dump.

*   **Download size**: `11.77 MiB`

*   **Dataset size**: `14.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 22,587

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20200301
    dump.

*   **Download size**: `5.58 MiB`

*   **Dataset size**: `8.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,767

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20200301 dump.

*   **Download size**: `708.12 MiB`

*   **Dataset size**: `1.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,435,673

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20200301
    dump.

*   **Download size**: `6.85 MiB`

*   **Dataset size**: `10.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,564

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20200301 dump.

*   **Download size**: `24.16 MiB`

*   **Dataset size**: `80.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 124,186

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20200301 dump.

*   **Download size**: `9.23 MiB`

*   **Dataset size**: `14.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,047

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20200301
    dump.

*   **Download size**: `257.48 MiB`

*   **Dataset size**: `412.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,264,120

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20200301 dump.

*   **Download size**: `1.84 MiB`

*   **Dataset size**: `3.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,604

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20200301
    dump.

*   **Download size**: `12.24 MiB`

*   **Dataset size**: `16.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,773

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20200301
    dump.

*   **Download size**: `1.66 MiB`

*   **Dataset size**: `1.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,797

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20200301 dump.

*   **Download size**: `1.38 MiB`

*   **Dataset size**: `1.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,342

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20200301
    dump.

*   **Download size**: `10.50 MiB`

*   **Dataset size**: `25.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20200301 dump.

*   **Download size**: `12.02 MiB`

*   **Dataset size**: `32.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 24,376

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20200301 dump.

*   **Download size**: `12.32 MiB`

*   **Dataset size**: `10.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 32,530

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20200301 dump.

*   **Download size**: `772.04 KiB`

*   **Dataset size**: `708.21 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,491

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20200301
    dump.

*   **Download size**: `2.52 MiB`

*   **Dataset size**: `4.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,575

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20200301 dump.

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `1.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,577,556

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20200301 dump.

*   **Download size**: `14.44 MiB`

*   **Dataset size**: `9.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,897

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20200301 dump.

*   **Download size**: `55.69 MiB`

*   **Dataset size**: `79.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 280,886

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20200301
    dump.

*   **Download size**: `57.83 MiB`

*   **Dataset size**: `61.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 77,025

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20200301 dump.

*   **Download size**: `1.81 MiB`

*   **Dataset size**: `1.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,562

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20190301 dump.

*   **Download size**: `44.09 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20190301 dump.

*   **Download size**: `1.31 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,053

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20190301
    dump.

*   **Download size**: `2.66 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,264

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20190301
    dump.

*   **Download size**: `349.43 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 547

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20190301 dump.

*   **Download size**: `84.13 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 92,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20190301 dump.

*   **Download size**: `377.84 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 628

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20190301
    dump.

*   **Download size**: `46.90 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 27,705

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20190301 dump.

*   **Download size**: `6.54 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,231

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20190301 dump.

*   **Download size**: `31.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 47,536

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20190301
    dump.

*   **Download size**: `3.77 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,135

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20190301 dump.

*   **Download size**: `805.82 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,272,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20190301
    dump.

*   **Download size**: `952.49 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,272

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20190301
    dump.

*   **Download size**: `20.32 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 28,136

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20190301 dump.

*   **Download size**: `19.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,435

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20190301
    dump.

*   **Download size**: `216.68 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 106,275

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20190301
    dump.

*   **Download size**: `467.05 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,005

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20190301 dump.

*   **Download size**: `3.61 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,918

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20190301 dump.

*   **Download size**: `2.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,773

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20190301 dump.

*   **Download size**: `163.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 161,901

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20190301
    dump.

*   **Download size**: `50.59 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 159,459

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20190301 dump.

*   **Download size**: `55.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 51,934

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20190301
    dump.

*   **Download size**: `30.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 42,237

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20190301
    dump.

*   **Download size**: `4.61 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,344

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20190301
    dump.

*   **Download size**: `6.18 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,025

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20190301 dump.

*   **Download size**: `192.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 164,589

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20190301
    dump.

*   **Download size**: `74.77 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 93,527

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20190301 dump.

*   **Download size**: `326.20 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 362,723

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20190301 dump.

*   **Download size**: `13.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,725

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20190301 dump.

*   **Download size**: `424.88 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20190301
    dump.

*   **Download size**: `2.09 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,476

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20190301 dump.

*   **Download size**: `447.98 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 729

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20190301 dump.

*   **Download size**: `145.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 87,566

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20190301 dump.

*   **Download size**: `12.41 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,301

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20190301
    dump.

*   **Download size**: `5.05 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20190301 dump.

*   **Download size**: `49.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 76,055

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20190301 dump.

*   **Download size**: `103.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 181,802

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20190301
    dump.

*   **Download size**: `1.76 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,378

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20190301
    dump.

*   **Download size**: `3.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,594

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20190301 dump.

*   **Download size**: `849.65 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 650,189

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20190301
    dump.

*   **Download size**: `1.84 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,289

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20190301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,422

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20190301 dump.

*   **Download size**: `43.89 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 213,978

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20190301
    dump.

*   **Download size**: `1.79 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,379,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20190301 dump.

*   **Download size**: `684.97 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 496

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20190301
    dump.

*   **Download size**: `25.99 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20190301
    dump.

*   **Download size**: `651.25 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 947

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20190301
    dump.

*   **Download size**: `325.90 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 773

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20190301
    dump.

*   **Download size**: `22.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 23,099

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20190301 dump.

*   **Download size**: `3.38 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,232

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20190301 dump.

*   **Download size**: `259.71 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 118

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20190301
    dump.

*   **Download size**: `4.01 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,341

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20190301 dump.

*   **Download size**: `759.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 539,754

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20190301
    dump.

*   **Download size**: `2.03 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,620

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20190301 dump.

*   **Download size**: `631.49 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,463

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20190301 dump.

*   **Download size**: `22.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 44,865

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20190301 dump.

*   **Download size**: `64.37 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 142,397

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20190301 dump.

*   **Download size**: `323.53 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 244,767

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20190301 dump.

*   **Download size**: `4.97 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,925,588

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20190301
    dump.

*   **Download size**: `457.06 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 228

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20190301
    dump.

*   **Download size**: `7.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20190301
    dump.

*   **Download size**: `3.54 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,438

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20190301
    dump.

*   **Download size**: `4.95 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,323

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20190301 dump.

*   **Download size**: `4.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,156

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20190301 dump.

*   **Download size**: `360.01 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 286

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20190301 dump.

*   **Download size**: `434.14 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 368

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20190301 dump.

*   **Download size**: `324.40 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 224,159

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20190301
    dump.

*   **Download size**: `7.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,957

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20190301 dump.

*   **Download size**: `15.72 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,824,596

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20190301 dump.

*   **Download size**: `245.73 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 353,663

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20190301 dump.

*   **Download size**: `2.93 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,728,167

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20190301 dump.

*   **Download size**: `196.03 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 288,641

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20190301 dump.

*   **Download size**: `180.35 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 400,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20190301
    dump.

*   **Download size**: `2.40 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20190301 dump.

*   **Download size**: `693.84 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,201,990

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20190301 dump.

*   **Download size**: `387.75 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 298

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20190301 dump.

*   **Download size**: `656.44 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 619,207

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20190301
    dump.

*   **Download size**: `2.00 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,050

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20190301 dump.

*   **Download size**: `262.98 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 507

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20190301 dump.

*   **Download size**: `13.67 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20190301 dump.

*   **Download size**: `4.14 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,087,215

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20190301
    dump.

*   **Download size**: `2.03 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,262

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20190301
    dump.

*   **Download size**: `7.88 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,706

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20190301
    dump.

*   **Download size**: `2.29 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,508

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20190301 dump.

*   **Download size**: `45.52 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 41,573

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20190301 dump.

*   **Download size**: `24.78 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 56,252

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20190301
    dump.

*   **Download size**: `2.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,034

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20190301
    dump.

*   **Download size**: `3.82 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20190301 dump.

*   **Download size**: `8.51 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,891

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20190301 dump.

*   **Download size**: `235.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 203,961

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20190301
    dump.

*   **Download size**: `1.91 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20190301 dump.

*   **Download size**: `3.37 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,337

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20190301
    dump.

*   **Download size**: `6.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,259

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20190301
    dump.

*   **Download size**: `1.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,467

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20190301
    dump.

*   **Download size**: `604.10 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 715

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20190301 dump.

*   **Download size**: `27.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 28,607

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20190301 dump.

*   **Download size**: `5.32 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,996

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20190301 dump.

*   **Download size**: `1.62 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,795

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20190301
    dump.

*   **Download size**: `3.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20190301
    dump.

*   **Download size**: `1017.76 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20190301 dump.

*   **Download size**: `572.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 393,436

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20190301 dump.

*   **Download size**: `137.86 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 156,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20190301
    dump.

*   **Download size**: `4.57 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,036

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20190301 dump.

*   **Download size**: `18.37 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20190301 dump.

*   **Download size**: `246.05 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 228,044

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20190301
    dump.

*   **Download size**: `10.38 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,693

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20190301 dump.

*   **Download size**: `10.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 56,093

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20190301 dump.

*   **Download size**: `810.17 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 625,614

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20190301 dump.

*   **Download size**: `277.53 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 575,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20190301 dump.

*   **Download size**: `7.85 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,780

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20190301 dump.

*   **Download size**: `523.94 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 947,627

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20190301 dump.

*   **Download size**: `1.70 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,403

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20190301 dump.

*   **Download size**: `1.00 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20190301 dump.

*   **Download size**: `30.88 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20190301 dump.

*   **Download size**: `238.12 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 647

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20190301
    dump.

*   **Download size**: `15.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 11,808

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20190301
    dump.

*   **Download size**: `1.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 932

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20190301 dump.

*   **Download size**: `12.56 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,629

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20190301 dump.

*   **Download size**: `41.86 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,219

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20190301 dump.

*   **Download size**: `2.66 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,800,218

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20190301 dump.

*   **Download size**: `284.06 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 510

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20190301 dump.

*   **Download size**: `2.74 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,382,683

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20190301
    dump.

*   **Download size**: `895.29 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,692

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20190301
    dump.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,301

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20190301 dump.

*   **Download size**: `39.32 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 72,893

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20190301 dump.

*   **Download size**: `131.78 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 161,290

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20190301
    dump.

*   **Download size**: `1.35 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,192

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20190301
    dump.

*   **Download size**: `3.62 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,415

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20190301
    dump.

*   **Download size**: `1.65 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,608

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20190301
    dump.

*   **Download size**: `1.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,706

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20190301 dump.

*   **Download size**: `439.26 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,240

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20190301 dump.

*   **Download size**: `370.78 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,482

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20190301 dump.

*   **Download size**: `16.58 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20190301 dump.

*   **Download size**: `113.46 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 266,609

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20190301 dump.

*   **Download size**: `862.51 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,713

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20190301 dump.

*   **Download size**: `21.92 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,889

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20190301 dump.

*   **Download size**: `69.62 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 24,679

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20190301 dump.

*   **Download size**: `625.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 980,493

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20190301
    dump.

*   **Download size**: `2.12 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,964

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20190301
    dump.

*   **Download size**: `3.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,317

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20190301 dump.

*   **Download size**: `309.15 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 399

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20190301
    dump.

*   **Download size**: `3.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20190301 dump.

*   **Download size**: `17.09 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,811

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20190301 dump.

*   **Download size**: `3.36 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,733

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20190301 dump.

*   **Download size**: `1.71 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,913

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20190301 dump.

*   **Download size**: `33.13 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 79,311

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20190301 dump.

*   **Download size**: `82.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 130,161

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20190301
    dump.

*   **Download size**: `3.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,261

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20190301 dump.

*   **Download size**: `45.70 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 61,607

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20190301
    dump.

*   **Download size**: `1.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,545

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20190301
    dump.

*   **Download size**: `4.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20190301
    dump.

*   **Download size**: `2.81 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,741

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20190301 dump.

*   **Download size**: `1.58 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20190301 dump.

*   **Download size**: `13.86 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,155

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20190301
    dump.

*   **Download size**: `2.73 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,281

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20190301
    dump.

*   **Download size**: `21.34 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,911

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20190301 dump.

*   **Download size**: `1.83 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,192

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20190301 dump.

*   **Download size**: `3.44 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,074

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20190301
    dump.

*   **Download size**: `4.71 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,774

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20190301 dump.

*   **Download size**: `174.73 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 217,121

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20190301
    dump.

*   **Download size**: `798.18 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 920

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20190301 dump.

*   **Download size**: `127.47 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 91,567

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20190301
    dump.

*   **Download size**: `10.80 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,523

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20190301
    dump.

*   **Download size**: `4.49 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20190301
    dump.

*   **Download size**: `1.04 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,344

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20190301 dump.

*   **Download size**: `25.64 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 126,066

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20190301 dump.

*   **Download size**: `27.71 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20190301
    dump.

*   **Download size**: `5.69 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 12,204

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20190301 dump.

*   **Download size**: `1.96 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,174

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20190301
    dump.

*   **Download size**: `25.05 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 226,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20190301 dump.

*   **Download size**: `140.69 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 138,779

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20190301 dump.

*   **Download size**: `117.24 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 112,979

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20190301 dump.

*   **Download size**: `28.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 23,195

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20190301 dump.

*   **Download size**: `49.58 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 95,825

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20190301
    dump.

*   **Download size**: `3.01 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,826

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20190301 dump.

*   **Download size**: `205.79 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 357,957

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20190301 dump.

*   **Download size**: `8.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,610

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20190301
    dump.

*   **Download size**: `14.20 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20190301
    dump.

*   **Download size**: `8.95 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,279

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20190301 dump.

*   **Download size**: `34.60 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 46,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20190301
    dump.

*   **Download size**: `7.79 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,077

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20190301
    dump.

*   **Download size**: `6.47 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 18,184

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20190301 dump.

*   **Download size**: `480.57 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20190301
    dump.

*   **Download size**: `4.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20190301
    dump.

*   **Download size**: `5.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,167

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20190301
    dump.

*   **Download size**: `33.28 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 45,754

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20190301
    dump.

*   **Download size**: `6.67 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,644

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20190301 dump.

*   **Download size**: `29.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 33,465

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20190301
    dump.

*   **Download size**: `16.91 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 72,872

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20190301 dump.

*   **Download size**: `91.11 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20190301 dump.

*   **Download size**: `1.38 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,409,491

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20190301 dump.

*   **Download size**: `126.01 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 213,859

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20190301 dump.

*   **Download size**: `610.74 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 783,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20190301
    dump.

*   **Download size**: `1.12 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,780

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20190301
    dump.

*   **Download size**: `1.56 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,048

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20190301
    dump.

*   **Download size**: `2.20 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,075

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20190301 dump.

*   **Download size**: `2.52 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,105

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20190301 dump.

*   **Download size**: `1.18 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 566

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20190301 dump.

*   **Download size**: `70.97 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 91,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20190301
    dump.

*   **Download size**: `1.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20190301 dump.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,054

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20190301 dump.

*   **Download size**: `24.90 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 28,368

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20190301 dump.

*   **Download size**: `7.31 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,490

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20190301 dump.

*   **Download size**: `40.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 40,578

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20190301
    dump.

*   **Download size**: `1.29 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,042

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20190301
    dump.

*   **Download size**: `8.17 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,721

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20190301
    dump.

*   **Download size**: `1.33 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,126

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20190301
    dump.

*   **Download size**: `4.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,485

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20190301
    dump.

*   **Download size**: `1.10 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,331

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20190301
    dump.

*   **Download size**: `3.22 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20190301 dump.

*   **Download size**: `586.77 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,057

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20190301
    dump.

*   **Download size**: `654.11 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 748

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20190301 dump.

*   **Download size**: `1.76 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,610,189

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20190301
    dump.

*   **Download size**: `13.42 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 65,551

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20190301
    dump.

*   **Download size**: `24.31 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50,764

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20190301
    dump.

*   **Download size**: `533.84 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 521

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20190301 dump.

*   **Download size**: `14.09 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,554

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20190301 dump.

*   **Download size**: `1.58 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,393,069

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20190301 dump.

*   **Download size**: `11.42 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 29,495

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20190301 dump.

*   **Download size**: `5.85 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20190301
    dump.

*   **Download size**: `509.61 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 693

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20190301 dump.

*   **Download size**: `779.25 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 696

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20190301 dump.

*   **Download size**: `449.49 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 393,012

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20190301
    dump.

*   **Download size**: `931.23 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,245

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20190301
    dump.

*   **Download size**: `5.98 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,288

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20190301 dump.

*   **Download size**: `3.51 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,449,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20190301
    dump.

*   **Download size**: `4.11 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,526

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20190301 dump.

*   **Download size**: `904.81 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,950

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20190301 dump.

*   **Download size**: `14.29 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 21,846

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20190301
    dump.

*   **Download size**: `11.88 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,504

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20190301
    dump.

*   **Download size**: `2.36 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,036

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20190301 dump.

*   **Download size**: `4.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,214

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20190301
    dump.

*   **Download size**: `11.83 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,330

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20190301
    dump.

*   **Download size**: `57.80 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 53,525

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20190301 dump.

*   **Download size**: `12.62 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 16,930

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20190301 dump.

*   **Download size**: `3.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,127

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20190301 dump.

*   **Download size**: `286.02 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 281

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20190301 dump.

*   **Download size**: `406.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,923,606

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20190301 dump.

*   **Download size**: `36.84 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25,922

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20190301
    dump.

*   **Download size**: `156.11 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 143,427

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20190301 dump.

*   **Download size**: `254.37 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 244,877

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20190301 dump.

*   **Download size**: `201.41 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 191,938

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20190301 dump.

*   **Download size**: `678.46 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 957

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20190301 dump.

*   **Download size**: `2.02 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,656

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20190301 dump.

*   **Download size**: `8.17 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,587

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20190301 dump.

*   **Download size**: `77.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 102,156

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20190301 dump.

*   **Download size**: `725.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,043,191

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20190301
    dump.

*   **Download size**: `634.21 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,234

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20190301 dump.

*   **Download size**: `737.58 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 495

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20190301 dump.

*   **Download size**: `482.27 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 605

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20190301
    dump.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 4,477

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20190301 dump.

*   **Download size**: `20.52 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,393

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20190301 dump.

*   **Download size**: `1.64 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,950,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20190301 dump.

*   **Download size**: `27.60 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 48,434

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20190301
    dump.

*   **Download size**: `4.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 8,603

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20190301 dump.

*   **Download size**: `141.07 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 154,505

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20190301
    dump.

*   **Download size**: `2.33 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20190301 dump.

*   **Download size**: `113.16 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 91,857

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20190301
    dump.

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,556

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20190301 dump.

*   **Download size**: `36.95 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 96,808

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20190301 dump.

*   **Download size**: `254.00 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 224,144

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20190301 dump.

*   **Download size**: `309.72 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 304

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20190301 dump.

*   **Download size**: `4.50 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 6,743

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20190301 dump.

*   **Download size**: `50.85 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 76,905

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20190301 dump.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 751

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20190301 dump.

*   **Download size**: `775.10 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,577

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20190301
    dump.

*   **Download size**: `1.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,523

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20190301 dump.

*   **Download size**: `497.19 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 548,768

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20190301 dump.

*   **Download size**: `1.39 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 665

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20190301 dump.

*   **Download size**: `53.23 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 120,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20190301
    dump.

*   **Download size**: `309.58 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 638

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20190301 dump.

*   **Download size**: `345.96 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 697

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20190301 dump.

*   **Download size**: `485.56 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,279

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20190301
    dump.

*   **Download size**: `2.60 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,563

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20190301
    dump.

*   **Download size**: `2.94 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,768

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20190301 dump.

*   **Download size**: `5.64 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,908

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20190301 dump.

*   **Download size**: `1.28 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,131,279

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20190301 dump.

*   **Download size**: `129.57 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 330,776

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20190301 dump.

*   **Download size**: `60.85 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 149,537

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20190301 dump.

*   **Download size**: `257.59 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 337

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20190301
    dump.

*   **Download size**: `10.65 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,433

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20190301
    dump.

*   **Download size**: `4.59 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,230

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20190301 dump.

*   **Download size**: `623.74 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,377,623

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20190301
    dump.

*   **Download size**: `6.58 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 7,233

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20190301 dump.

*   **Download size**: `23.80 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 122,640

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20190301 dump.

*   **Download size**: `8.75 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 15,283

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20190301
    dump.

*   **Download size**: `256.72 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,263,705

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20190301 dump.

*   **Download size**: `1.54 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,336

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20190301
    dump.

*   **Download size**: `9.08 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 19,269

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20190301
    dump.

*   **Download size**: `1.64 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,794

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20190301 dump.

*   **Download size**: `1.26 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,004

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20190301
    dump.

*   **Download size**: `9.40 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14,297

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20190301 dump.

*   **Download size**: `11.56 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 23,430

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20190301 dump.

*   **Download size**: `11.55 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 31,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20190301 dump.

*   **Download size**: `735.93 KiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,404

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20190301
    dump.

*   **Download size**: `2.47 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20190301 dump.

*   **Download size**: `1.71 GiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,482,100

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20190301 dump.

*   **Download size**: `13.37 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 10,173

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20190301 dump.

*   **Download size**: `50.30 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 233,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20190301
    dump.

*   **Download size**: `52.41 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 70,666

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20190301 dump.

*   **Download size**: `1.50 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,184

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.
