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

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype     | Description
:------ | :----------- | :---- | :-------- | :----------
        | FeaturesDict |       |           |
text    | Text         |       | tf.string |
title   | Text         |       | tf.string |

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


## wikipedia/20201201.aa (default config)

*   **Config description**: Wikipedia dataset for aa, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.aa-1.0.0.html";
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

## wikipedia/20201201.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ab-1.0.0.html";
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

## wikipedia/20201201.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ace-1.0.0.html";
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

## wikipedia/20201201.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ady-1.0.0.html";
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

## wikipedia/20201201.af

*   **Config description**: Wikipedia dataset for af, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.af-1.0.0.html";
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

## wikipedia/20201201.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ak-1.0.0.html";
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

## wikipedia/20201201.als

*   **Config description**: Wikipedia dataset for als, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.als-1.0.0.html";
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

## wikipedia/20201201.am

*   **Config description**: Wikipedia dataset for am, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.am-1.0.0.html";
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

## wikipedia/20201201.an

*   **Config description**: Wikipedia dataset for an, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.an-1.0.0.html";
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

## wikipedia/20201201.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ang-1.0.0.html";
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

## wikipedia/20201201.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ar-1.0.0.html";
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

## wikipedia/20201201.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.arc-1.0.0.html";
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

## wikipedia/20201201.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.arz-1.0.0.html";
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

## wikipedia/20201201.as

*   **Config description**: Wikipedia dataset for as, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.as-1.0.0.html";
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

## wikipedia/20201201.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ast-1.0.0.html";
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

## wikipedia/20201201.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.atj-1.0.0.html";
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

## wikipedia/20201201.av

*   **Config description**: Wikipedia dataset for av, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.av-1.0.0.html";
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

## wikipedia/20201201.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ay-1.0.0.html";
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

## wikipedia/20201201.az

*   **Config description**: Wikipedia dataset for az, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.az-1.0.0.html";
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

## wikipedia/20201201.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.azb-1.0.0.html";
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

## wikipedia/20201201.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ba-1.0.0.html";
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

## wikipedia/20201201.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bar-1.0.0.html";
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

## wikipedia/20201201.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bat-smg-1.0.0.html";
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

## wikipedia/20201201.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bcl-1.0.0.html";
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

## wikipedia/20201201.be

*   **Config description**: Wikipedia dataset for be, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.be-1.0.0.html";
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

## wikipedia/20201201.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.be-x-old-1.0.0.html";
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

## wikipedia/20201201.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bg-1.0.0.html";
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

## wikipedia/20201201.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bh-1.0.0.html";
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

## wikipedia/20201201.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bi-1.0.0.html";
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

## wikipedia/20201201.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bjn-1.0.0.html";
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

## wikipedia/20201201.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bm-1.0.0.html";
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

## wikipedia/20201201.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bn-1.0.0.html";
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

## wikipedia/20201201.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bo-1.0.0.html";
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

## wikipedia/20201201.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bpy-1.0.0.html";
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

## wikipedia/20201201.br

*   **Config description**: Wikipedia dataset for br, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.br-1.0.0.html";
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

## wikipedia/20201201.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bs-1.0.0.html";
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

## wikipedia/20201201.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bug-1.0.0.html";
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

## wikipedia/20201201.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.bxr-1.0.0.html";
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

## wikipedia/20201201.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ca-1.0.0.html";
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

## wikipedia/20201201.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cbk-zam-1.0.0.html";
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

## wikipedia/20201201.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cdo-1.0.0.html";
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

## wikipedia/20201201.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ce-1.0.0.html";
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

## wikipedia/20201201.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ceb-1.0.0.html";
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

## wikipedia/20201201.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ch-1.0.0.html";
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

## wikipedia/20201201.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cho-1.0.0.html";
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

## wikipedia/20201201.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.chr-1.0.0.html";
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

## wikipedia/20201201.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.chy-1.0.0.html";
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

## wikipedia/20201201.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ckb-1.0.0.html";
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

## wikipedia/20201201.co

*   **Config description**: Wikipedia dataset for co, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.co-1.0.0.html";
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

## wikipedia/20201201.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cr-1.0.0.html";
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

## wikipedia/20201201.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.crh-1.0.0.html";
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

## wikipedia/20201201.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cs-1.0.0.html";
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

## wikipedia/20201201.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.csb-1.0.0.html";
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

## wikipedia/20201201.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cu-1.0.0.html";
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

## wikipedia/20201201.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cv-1.0.0.html";
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

## wikipedia/20201201.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.cy-1.0.0.html";
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

## wikipedia/20201201.da

*   **Config description**: Wikipedia dataset for da, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.da-1.0.0.html";
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

## wikipedia/20201201.de

*   **Config description**: Wikipedia dataset for de, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.de-1.0.0.html";
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

## wikipedia/20201201.din

*   **Config description**: Wikipedia dataset for din, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.din-1.0.0.html";
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

## wikipedia/20201201.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.diq-1.0.0.html";
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

## wikipedia/20201201.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.dsb-1.0.0.html";
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

## wikipedia/20201201.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.dty-1.0.0.html";
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

## wikipedia/20201201.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.dv-1.0.0.html";
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

## wikipedia/20201201.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.dz-1.0.0.html";
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

## wikipedia/20201201.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ee-1.0.0.html";
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

## wikipedia/20201201.el

*   **Config description**: Wikipedia dataset for el, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.el-1.0.0.html";
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

## wikipedia/20201201.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.eml-1.0.0.html";
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

## wikipedia/20201201.en

*   **Config description**: Wikipedia dataset for en, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.en-1.0.0.html";
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

## wikipedia/20201201.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.eo-1.0.0.html";
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

## wikipedia/20201201.es

*   **Config description**: Wikipedia dataset for es, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.es-1.0.0.html";
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

## wikipedia/20201201.et

*   **Config description**: Wikipedia dataset for et, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.et-1.0.0.html";
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

## wikipedia/20201201.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.eu-1.0.0.html";
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

## wikipedia/20201201.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ext-1.0.0.html";
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

## wikipedia/20201201.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fa-1.0.0.html";
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

## wikipedia/20201201.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ff-1.0.0.html";
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

## wikipedia/20201201.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fi-1.0.0.html";
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

## wikipedia/20201201.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fiu-vro-1.0.0.html";
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

## wikipedia/20201201.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fj-1.0.0.html";
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

## wikipedia/20201201.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fo-1.0.0.html";
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

## wikipedia/20201201.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fr-1.0.0.html";
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

## wikipedia/20201201.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.frp-1.0.0.html";
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

## wikipedia/20201201.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.frr-1.0.0.html";
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

## wikipedia/20201201.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fur-1.0.0.html";
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

## wikipedia/20201201.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.fy-1.0.0.html";
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

## wikipedia/20201201.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ga-1.0.0.html";
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

## wikipedia/20201201.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gag-1.0.0.html";
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

## wikipedia/20201201.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gan-1.0.0.html";
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

## wikipedia/20201201.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gd-1.0.0.html";
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

## wikipedia/20201201.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gl-1.0.0.html";
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

## wikipedia/20201201.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.glk-1.0.0.html";
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

## wikipedia/20201201.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gn-1.0.0.html";
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

## wikipedia/20201201.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gom-1.0.0.html";
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

## wikipedia/20201201.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gor-1.0.0.html";
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

## wikipedia/20201201.got

*   **Config description**: Wikipedia dataset for got, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.got-1.0.0.html";
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

## wikipedia/20201201.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gu-1.0.0.html";
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

## wikipedia/20201201.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.gv-1.0.0.html";
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

## wikipedia/20201201.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.ha-1.0.0.html";
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

## wikipedia/20201201.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.hak-1.0.0.html";
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

## wikipedia/20201201.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.haw-1.0.0.html";
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

## wikipedia/20201201.he

*   **Config description**: Wikipedia dataset for he, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia-20201201.he-1.0.0.html";
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

## wikipedia/20201201.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.id

*   **Config description**: Wikipedia dataset for id, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.io

*   **Config description**: Wikipedia dataset for io, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.is

*   **Config description**: Wikipedia dataset for is, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.it

*   **Config description**: Wikipedia dataset for it, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.km

*   **Config description**: Wikipedia dataset for km, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.la

*   **Config description**: Wikipedia dataset for la, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.li

*   **Config description**: Wikipedia dataset for li, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.min

*   **Config description**: Wikipedia dataset for min, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.my

*   **Config description**: Wikipedia dataset for my, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.na

*   **Config description**: Wikipedia dataset for na, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.new

*   **Config description**: Wikipedia dataset for new, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.no

*   **Config description**: Wikipedia dataset for no, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.om

*   **Config description**: Wikipedia dataset for om, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.or

*   **Config description**: Wikipedia dataset for or, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.os

*   **Config description**: Wikipedia dataset for os, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.se

*   **Config description**: Wikipedia dataset for se, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.si

*   **Config description**: Wikipedia dataset for si, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.so

*   **Config description**: Wikipedia dataset for so, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.st

*   **Config description**: Wikipedia dataset for st, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.su

*   **Config description**: Wikipedia dataset for su, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.te

*   **Config description**: Wikipedia dataset for te, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.th

*   **Config description**: Wikipedia dataset for th, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.to

*   **Config description**: Wikipedia dataset for to, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.war

*   **Config description**: Wikipedia dataset for war, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.za

*   **Config description**: Wikipedia dataset for za, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20201201
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20201201.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20201201 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20200301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20200301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20200301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.aa

*   **Config description**: Wikipedia dataset for aa, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ab

*   **Config description**: Wikipedia dataset for ab, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ace

*   **Config description**: Wikipedia dataset for ace, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ady

*   **Config description**: Wikipedia dataset for ady, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.af

*   **Config description**: Wikipedia dataset for af, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ak

*   **Config description**: Wikipedia dataset for ak, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.als

*   **Config description**: Wikipedia dataset for als, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.am

*   **Config description**: Wikipedia dataset for am, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.an

*   **Config description**: Wikipedia dataset for an, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ang

*   **Config description**: Wikipedia dataset for ang, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ar

*   **Config description**: Wikipedia dataset for ar, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.arc

*   **Config description**: Wikipedia dataset for arc, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.arz

*   **Config description**: Wikipedia dataset for arz, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.as

*   **Config description**: Wikipedia dataset for as, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ast

*   **Config description**: Wikipedia dataset for ast, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.atj

*   **Config description**: Wikipedia dataset for atj, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.av

*   **Config description**: Wikipedia dataset for av, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ay

*   **Config description**: Wikipedia dataset for ay, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.az

*   **Config description**: Wikipedia dataset for az, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.azb

*   **Config description**: Wikipedia dataset for azb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ba

*   **Config description**: Wikipedia dataset for ba, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bar

*   **Config description**: Wikipedia dataset for bar, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bat-smg

*   **Config description**: Wikipedia dataset for bat-smg, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bcl

*   **Config description**: Wikipedia dataset for bcl, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.be

*   **Config description**: Wikipedia dataset for be, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.be-x-old

*   **Config description**: Wikipedia dataset for be-x-old, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bg

*   **Config description**: Wikipedia dataset for bg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bh

*   **Config description**: Wikipedia dataset for bh, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bi

*   **Config description**: Wikipedia dataset for bi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bjn

*   **Config description**: Wikipedia dataset for bjn, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bm

*   **Config description**: Wikipedia dataset for bm, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bn

*   **Config description**: Wikipedia dataset for bn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bo

*   **Config description**: Wikipedia dataset for bo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bpy

*   **Config description**: Wikipedia dataset for bpy, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.br

*   **Config description**: Wikipedia dataset for br, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bs

*   **Config description**: Wikipedia dataset for bs, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bug

*   **Config description**: Wikipedia dataset for bug, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.bxr

*   **Config description**: Wikipedia dataset for bxr, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ca

*   **Config description**: Wikipedia dataset for ca, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cbk-zam

*   **Config description**: Wikipedia dataset for cbk-zam, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cdo

*   **Config description**: Wikipedia dataset for cdo, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ce

*   **Config description**: Wikipedia dataset for ce, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ceb

*   **Config description**: Wikipedia dataset for ceb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ch

*   **Config description**: Wikipedia dataset for ch, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cho

*   **Config description**: Wikipedia dataset for cho, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.chr

*   **Config description**: Wikipedia dataset for chr, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.chy

*   **Config description**: Wikipedia dataset for chy, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ckb

*   **Config description**: Wikipedia dataset for ckb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.co

*   **Config description**: Wikipedia dataset for co, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cr

*   **Config description**: Wikipedia dataset for cr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.crh

*   **Config description**: Wikipedia dataset for crh, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cs

*   **Config description**: Wikipedia dataset for cs, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.csb

*   **Config description**: Wikipedia dataset for csb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cu

*   **Config description**: Wikipedia dataset for cu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cv

*   **Config description**: Wikipedia dataset for cv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.cy

*   **Config description**: Wikipedia dataset for cy, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.da

*   **Config description**: Wikipedia dataset for da, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.de

*   **Config description**: Wikipedia dataset for de, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.din

*   **Config description**: Wikipedia dataset for din, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.diq

*   **Config description**: Wikipedia dataset for diq, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dsb

*   **Config description**: Wikipedia dataset for dsb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dty

*   **Config description**: Wikipedia dataset for dty, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dv

*   **Config description**: Wikipedia dataset for dv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.dz

*   **Config description**: Wikipedia dataset for dz, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ee

*   **Config description**: Wikipedia dataset for ee, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.el

*   **Config description**: Wikipedia dataset for el, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eml

*   **Config description**: Wikipedia dataset for eml, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.en

*   **Config description**: Wikipedia dataset for en, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eo

*   **Config description**: Wikipedia dataset for eo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.es

*   **Config description**: Wikipedia dataset for es, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.et

*   **Config description**: Wikipedia dataset for et, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.eu

*   **Config description**: Wikipedia dataset for eu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ext

*   **Config description**: Wikipedia dataset for ext, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fa

*   **Config description**: Wikipedia dataset for fa, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ff

*   **Config description**: Wikipedia dataset for ff, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fi

*   **Config description**: Wikipedia dataset for fi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fiu-vro

*   **Config description**: Wikipedia dataset for fiu-vro, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fj

*   **Config description**: Wikipedia dataset for fj, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fo

*   **Config description**: Wikipedia dataset for fo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fr

*   **Config description**: Wikipedia dataset for fr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.frp

*   **Config description**: Wikipedia dataset for frp, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.frr

*   **Config description**: Wikipedia dataset for frr, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fur

*   **Config description**: Wikipedia dataset for fur, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.fy

*   **Config description**: Wikipedia dataset for fy, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ga

*   **Config description**: Wikipedia dataset for ga, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gag

*   **Config description**: Wikipedia dataset for gag, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gan

*   **Config description**: Wikipedia dataset for gan, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gd

*   **Config description**: Wikipedia dataset for gd, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gl

*   **Config description**: Wikipedia dataset for gl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.glk

*   **Config description**: Wikipedia dataset for glk, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gn

*   **Config description**: Wikipedia dataset for gn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gom

*   **Config description**: Wikipedia dataset for gom, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gor

*   **Config description**: Wikipedia dataset for gor, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.got

*   **Config description**: Wikipedia dataset for got, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gu

*   **Config description**: Wikipedia dataset for gu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.gv

*   **Config description**: Wikipedia dataset for gv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ha

*   **Config description**: Wikipedia dataset for ha, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hak

*   **Config description**: Wikipedia dataset for hak, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.haw

*   **Config description**: Wikipedia dataset for haw, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.he

*   **Config description**: Wikipedia dataset for he, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hi

*   **Config description**: Wikipedia dataset for hi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hif

*   **Config description**: Wikipedia dataset for hif, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ho

*   **Config description**: Wikipedia dataset for ho, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hr

*   **Config description**: Wikipedia dataset for hr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hsb

*   **Config description**: Wikipedia dataset for hsb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ht

*   **Config description**: Wikipedia dataset for ht, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hu

*   **Config description**: Wikipedia dataset for hu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.hy

*   **Config description**: Wikipedia dataset for hy, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ia

*   **Config description**: Wikipedia dataset for ia, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.id

*   **Config description**: Wikipedia dataset for id, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ie

*   **Config description**: Wikipedia dataset for ie, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ig

*   **Config description**: Wikipedia dataset for ig, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ii

*   **Config description**: Wikipedia dataset for ii, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ik

*   **Config description**: Wikipedia dataset for ik, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ilo

*   **Config description**: Wikipedia dataset for ilo, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.inh

*   **Config description**: Wikipedia dataset for inh, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.io

*   **Config description**: Wikipedia dataset for io, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.is

*   **Config description**: Wikipedia dataset for is, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.it

*   **Config description**: Wikipedia dataset for it, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.iu

*   **Config description**: Wikipedia dataset for iu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ja

*   **Config description**: Wikipedia dataset for ja, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jam

*   **Config description**: Wikipedia dataset for jam, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jbo

*   **Config description**: Wikipedia dataset for jbo, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.jv

*   **Config description**: Wikipedia dataset for jv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ka

*   **Config description**: Wikipedia dataset for ka, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kaa

*   **Config description**: Wikipedia dataset for kaa, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kab

*   **Config description**: Wikipedia dataset for kab, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kbd

*   **Config description**: Wikipedia dataset for kbd, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kbp

*   **Config description**: Wikipedia dataset for kbp, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kg

*   **Config description**: Wikipedia dataset for kg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ki

*   **Config description**: Wikipedia dataset for ki, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kj

*   **Config description**: Wikipedia dataset for kj, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kk

*   **Config description**: Wikipedia dataset for kk, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kl

*   **Config description**: Wikipedia dataset for kl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.km

*   **Config description**: Wikipedia dataset for km, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kn

*   **Config description**: Wikipedia dataset for kn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ko

*   **Config description**: Wikipedia dataset for ko, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.koi

*   **Config description**: Wikipedia dataset for koi, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.krc

*   **Config description**: Wikipedia dataset for krc, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ks

*   **Config description**: Wikipedia dataset for ks, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ksh

*   **Config description**: Wikipedia dataset for ksh, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ku

*   **Config description**: Wikipedia dataset for ku, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kv

*   **Config description**: Wikipedia dataset for kv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.kw

*   **Config description**: Wikipedia dataset for kw, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ky

*   **Config description**: Wikipedia dataset for ky, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.la

*   **Config description**: Wikipedia dataset for la, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lad

*   **Config description**: Wikipedia dataset for lad, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lb

*   **Config description**: Wikipedia dataset for lb, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lbe

*   **Config description**: Wikipedia dataset for lbe, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lez

*   **Config description**: Wikipedia dataset for lez, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lfn

*   **Config description**: Wikipedia dataset for lfn, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lg

*   **Config description**: Wikipedia dataset for lg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.li

*   **Config description**: Wikipedia dataset for li, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lij

*   **Config description**: Wikipedia dataset for lij, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lmo

*   **Config description**: Wikipedia dataset for lmo, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ln

*   **Config description**: Wikipedia dataset for ln, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lo

*   **Config description**: Wikipedia dataset for lo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lrc

*   **Config description**: Wikipedia dataset for lrc, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lt

*   **Config description**: Wikipedia dataset for lt, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ltg

*   **Config description**: Wikipedia dataset for ltg, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.lv

*   **Config description**: Wikipedia dataset for lv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mai

*   **Config description**: Wikipedia dataset for mai, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.map-bms

*   **Config description**: Wikipedia dataset for map-bms, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mdf

*   **Config description**: Wikipedia dataset for mdf, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mg

*   **Config description**: Wikipedia dataset for mg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mh

*   **Config description**: Wikipedia dataset for mh, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mhr

*   **Config description**: Wikipedia dataset for mhr, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mi

*   **Config description**: Wikipedia dataset for mi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.min

*   **Config description**: Wikipedia dataset for min, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mk

*   **Config description**: Wikipedia dataset for mk, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ml

*   **Config description**: Wikipedia dataset for ml, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mn

*   **Config description**: Wikipedia dataset for mn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mr

*   **Config description**: Wikipedia dataset for mr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mrj

*   **Config description**: Wikipedia dataset for mrj, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ms

*   **Config description**: Wikipedia dataset for ms, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mt

*   **Config description**: Wikipedia dataset for mt, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mus

*   **Config description**: Wikipedia dataset for mus, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mwl

*   **Config description**: Wikipedia dataset for mwl, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.my

*   **Config description**: Wikipedia dataset for my, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.myv

*   **Config description**: Wikipedia dataset for myv, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.mzn

*   **Config description**: Wikipedia dataset for mzn, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.na

*   **Config description**: Wikipedia dataset for na, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nah

*   **Config description**: Wikipedia dataset for nah, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nap

*   **Config description**: Wikipedia dataset for nap, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nds

*   **Config description**: Wikipedia dataset for nds, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nds-nl

*   **Config description**: Wikipedia dataset for nds-nl, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ne

*   **Config description**: Wikipedia dataset for ne, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.new

*   **Config description**: Wikipedia dataset for new, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ng

*   **Config description**: Wikipedia dataset for ng, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nl

*   **Config description**: Wikipedia dataset for nl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nn

*   **Config description**: Wikipedia dataset for nn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.no

*   **Config description**: Wikipedia dataset for no, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nov

*   **Config description**: Wikipedia dataset for nov, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nrm

*   **Config description**: Wikipedia dataset for nrm, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nso

*   **Config description**: Wikipedia dataset for nso, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.nv

*   **Config description**: Wikipedia dataset for nv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ny

*   **Config description**: Wikipedia dataset for ny, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.oc

*   **Config description**: Wikipedia dataset for oc, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.olo

*   **Config description**: Wikipedia dataset for olo, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.om

*   **Config description**: Wikipedia dataset for om, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.or

*   **Config description**: Wikipedia dataset for or, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.os

*   **Config description**: Wikipedia dataset for os, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pa

*   **Config description**: Wikipedia dataset for pa, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pag

*   **Config description**: Wikipedia dataset for pag, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pam

*   **Config description**: Wikipedia dataset for pam, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pap

*   **Config description**: Wikipedia dataset for pap, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pcd

*   **Config description**: Wikipedia dataset for pcd, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pdc

*   **Config description**: Wikipedia dataset for pdc, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pfl

*   **Config description**: Wikipedia dataset for pfl, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pi

*   **Config description**: Wikipedia dataset for pi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pih

*   **Config description**: Wikipedia dataset for pih, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pl

*   **Config description**: Wikipedia dataset for pl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pms

*   **Config description**: Wikipedia dataset for pms, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pnb

*   **Config description**: Wikipedia dataset for pnb, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pnt

*   **Config description**: Wikipedia dataset for pnt, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ps

*   **Config description**: Wikipedia dataset for ps, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.pt

*   **Config description**: Wikipedia dataset for pt, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.qu

*   **Config description**: Wikipedia dataset for qu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rm

*   **Config description**: Wikipedia dataset for rm, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rmy

*   **Config description**: Wikipedia dataset for rmy, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rn

*   **Config description**: Wikipedia dataset for rn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ro

*   **Config description**: Wikipedia dataset for ro, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.roa-rup

*   **Config description**: Wikipedia dataset for roa-rup, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.roa-tara

*   **Config description**: Wikipedia dataset for roa-tara, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ru

*   **Config description**: Wikipedia dataset for ru, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rue

*   **Config description**: Wikipedia dataset for rue, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.rw

*   **Config description**: Wikipedia dataset for rw, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sa

*   **Config description**: Wikipedia dataset for sa, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sah

*   **Config description**: Wikipedia dataset for sah, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sat

*   **Config description**: Wikipedia dataset for sat, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sc

*   **Config description**: Wikipedia dataset for sc, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.scn

*   **Config description**: Wikipedia dataset for scn, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sco

*   **Config description**: Wikipedia dataset for sco, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sd

*   **Config description**: Wikipedia dataset for sd, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.se

*   **Config description**: Wikipedia dataset for se, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sg

*   **Config description**: Wikipedia dataset for sg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sh

*   **Config description**: Wikipedia dataset for sh, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.si

*   **Config description**: Wikipedia dataset for si, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.simple

*   **Config description**: Wikipedia dataset for simple, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sk

*   **Config description**: Wikipedia dataset for sk, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sl

*   **Config description**: Wikipedia dataset for sl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sm

*   **Config description**: Wikipedia dataset for sm, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sn

*   **Config description**: Wikipedia dataset for sn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.so

*   **Config description**: Wikipedia dataset for so, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sq

*   **Config description**: Wikipedia dataset for sq, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sr

*   **Config description**: Wikipedia dataset for sr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.srn

*   **Config description**: Wikipedia dataset for srn, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ss

*   **Config description**: Wikipedia dataset for ss, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.st

*   **Config description**: Wikipedia dataset for st, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.stq

*   **Config description**: Wikipedia dataset for stq, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.su

*   **Config description**: Wikipedia dataset for su, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sv

*   **Config description**: Wikipedia dataset for sv, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.sw

*   **Config description**: Wikipedia dataset for sw, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.szl

*   **Config description**: Wikipedia dataset for szl, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ta

*   **Config description**: Wikipedia dataset for ta, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tcy

*   **Config description**: Wikipedia dataset for tcy, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.te

*   **Config description**: Wikipedia dataset for te, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tet

*   **Config description**: Wikipedia dataset for tet, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tg

*   **Config description**: Wikipedia dataset for tg, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.th

*   **Config description**: Wikipedia dataset for th, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ti

*   **Config description**: Wikipedia dataset for ti, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tk

*   **Config description**: Wikipedia dataset for tk, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tl

*   **Config description**: Wikipedia dataset for tl, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tn

*   **Config description**: Wikipedia dataset for tn, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.to

*   **Config description**: Wikipedia dataset for to, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tpi

*   **Config description**: Wikipedia dataset for tpi, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tr

*   **Config description**: Wikipedia dataset for tr, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ts

*   **Config description**: Wikipedia dataset for ts, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tt

*   **Config description**: Wikipedia dataset for tt, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tum

*   **Config description**: Wikipedia dataset for tum, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tw

*   **Config description**: Wikipedia dataset for tw, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ty

*   **Config description**: Wikipedia dataset for ty, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.tyv

*   **Config description**: Wikipedia dataset for tyv, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.udm

*   **Config description**: Wikipedia dataset for udm, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ug

*   **Config description**: Wikipedia dataset for ug, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.uk

*   **Config description**: Wikipedia dataset for uk, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ur

*   **Config description**: Wikipedia dataset for ur, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.uz

*   **Config description**: Wikipedia dataset for uz, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.ve

*   **Config description**: Wikipedia dataset for ve, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vec

*   **Config description**: Wikipedia dataset for vec, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vep

*   **Config description**: Wikipedia dataset for vep, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vi

*   **Config description**: Wikipedia dataset for vi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vls

*   **Config description**: Wikipedia dataset for vls, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.vo

*   **Config description**: Wikipedia dataset for vo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wa

*   **Config description**: Wikipedia dataset for wa, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.war

*   **Config description**: Wikipedia dataset for war, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wo

*   **Config description**: Wikipedia dataset for wo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.wuu

*   **Config description**: Wikipedia dataset for wuu, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xal

*   **Config description**: Wikipedia dataset for xal, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xh

*   **Config description**: Wikipedia dataset for xh, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.xmf

*   **Config description**: Wikipedia dataset for xmf, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.yi

*   **Config description**: Wikipedia dataset for yi, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.yo

*   **Config description**: Wikipedia dataset for yo, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.za

*   **Config description**: Wikipedia dataset for za, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zea

*   **Config description**: Wikipedia dataset for zea, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh

*   **Config description**: Wikipedia dataset for zh, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-classical

*   **Config description**: Wikipedia dataset for zh-classical, parsed from
    20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-min-nan

*   **Config description**: Wikipedia dataset for zh-min-nan, parsed from
    20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zh-yue

*   **Config description**: Wikipedia dataset for zh-yue, parsed from 20190301
    dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## wikipedia/20190301.zu

*   **Config description**: Wikipedia dataset for zu, parsed from 20190301 dump.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.
