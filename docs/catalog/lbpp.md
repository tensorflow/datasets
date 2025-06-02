<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lbpp" />
  <meta itemprop="description" content="*Less Basic Python Programming* is a collection of 161 programming problems&#10;with accompanying unit tests.&#10;They were created with the aim of being fresh (not leaked at the time of&#10;creation) and more difficult than similar datasets (e.g., HumanEval and MBPP).&#10;It can serve as a drop-in replacement or enrichment of those datasets as they&#10;are structured in an equivalent way.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lbpp&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lbpp" />
  <meta itemprop="sameAs" content="https://aclanthology.org/2024.findings-emnlp.772/" />
  <meta itemprop="citation" content="@inproceedings{matton-etal-2024-leakage,&#10;    title = &quot;On Leakage of Code Generation Evaluation Datasets&quot;,&#10;    author = &quot;Matton, Alexandre  and&#10;      Sherborne, Tom  and&#10;      Aumiller, Dennis  and&#10;      Tommasone, Elena  and&#10;      Alizadeh, Milad  and&#10;      He, Jingyi  and&#10;      Ma, Raymond  and&#10;      Voisin, Maxime  and&#10;      Gilsenan-McMahon, Ellen  and&#10;      Gall{\&#x27;e}, Matthias&quot;,&#10;    editor = &quot;Al-Onaizan, Yaser  and&#10;      Bansal, Mohit  and&#10;      Chen, Yun-Nung&quot;,&#10;    booktitle = &quot;Findings of the Association for Computational Linguistics: EMNLP 2024&quot;,&#10;    month = nov,&#10;    year = &quot;2024&quot;,&#10;    address = &quot;Miami, Florida, USA&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/2024.findings-emnlp.772/&quot;,&#10;    doi = &quot;10.18653/v1/2024.findings-emnlp.772&quot;,&#10;    pages = &quot;13215--13223&quot;,&#10;}" />
</div>

# `lbpp`


*   **Description**:

*Less Basic Python Programming* is a collection of 161 programming problems with
accompanying unit tests. They were created with the aim of being fresh (not
leaked at the time of creation) and more difficult than similar datasets (e.g.,
HumanEval and MBPP). It can serve as a drop-in replacement or enrichment of
those datasets as they are structured in an equivalent way.

*   **Homepage**:
    [https://aclanthology.org/2024.findings-emnlp.772/](https://aclanthology.org/2024.findings-emnlp.772/)

*   **Source code**:
    [`tfds.datasets.lbpp.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/lbpp/lbpp_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'categories': Sequence(Text(shape=(), dtype=string)),
    'completion': Text(shape=(), dtype=string),
    'instruction': Text(shape=(), dtype=string),
    'language': Text(shape=(), dtype=string),
    'signature': Text(shape=(), dtype=string),
    'task_id': Text(shape=(), dtype=string),
    'test_file': Text(shape=(), dtype=string),
    'test_list': Sequence(Text(shape=(), dtype=string)),
    'test_setup': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature     | Class          | Shape   | Dtype  | Description
:---------- | :------------- | :------ | :----- | :----------
            | FeaturesDict   |         |        |
categories  | Sequence(Text) | (None,) | string |
completion  | Text           |         | string |
instruction | Text           |         | string |
language    | Text           |         | string |
signature   | Text           |         | string |
task_id     | Text           |         | string |
test_file   | Text           |         | string |
test_list   | Sequence(Text) | (None,) | string |
test_setup  | Text           |         | string |
title       | Text           |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{matton-etal-2024-leakage,
    title = "On Leakage of Code Generation Evaluation Datasets",
    author = "Matton, Alexandre  and
      Sherborne, Tom  and
      Aumiller, Dennis  and
      Tommasone, Elena  and
      Alizadeh, Milad  and
      He, Jingyi  and
      Ma, Raymond  and
      Voisin, Maxime  and
      Gilsenan-McMahon, Ellen  and
      Gall{\'e}, Matthias",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.772/",
    doi = "10.18653/v1/2024.findings-emnlp.772",
    pages = "13215--13223",
}
```


## lbpp/all (default config)

*   **Config description**: Multilingual LBPP

*   **Download size**: `1.78 MiB`

*   **Dataset size**: `4.30 MiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 944

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-all-2.0.0.html";
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

## lbpp/multilingual

*   **Config description**: Multilingual LBPP

*   **Download size**: `1.78 MiB`

*   **Dataset size**: `4.30 MiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 944

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-multilingual-2.0.0.html";
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

## lbpp/default

*   **Config description**: Python LBPP

*   **Download size**: `279.90 KiB`

*   **Dataset size**: `627.04 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-default-2.0.0.html";
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

## lbpp/python

*   **Config description**: Python LBPP

*   **Download size**: `279.90 KiB`

*   **Dataset size**: `627.04 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-python-2.0.0.html";
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

## lbpp/cpp

*   **Config description**: C++ LBPP

*   **Download size**: `314.45 KiB`

*   **Dataset size**: `761.87 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 161

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-cpp-2.0.0.html";
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

## lbpp/go

*   **Config description**: Go LBPP

*   **Download size**: `317.09 KiB`

*   **Dataset size**: `687.23 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 161

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-go-2.0.0.html";
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

## lbpp/java

*   **Config description**: Java LBPP

*   **Download size**: `337.90 KiB`

*   **Dataset size**: `887.40 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 158

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-java-2.0.0.html";
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

## lbpp/js

*   **Config description**: JavaScript LBPP

*   **Download size**: `303.40 KiB`

*   **Dataset size**: `756.69 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 153

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-js-2.0.0.html";
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

## lbpp/javascript

*   **Config description**: JavaScript LBPP

*   **Download size**: `303.40 KiB`

*   **Dataset size**: `756.69 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 153

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-javascript-2.0.0.html";
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

## lbpp/rust

*   **Config description**: JavaScript LBPP

*   **Download size**: `272.61 KiB`

*   **Dataset size**: `684.31 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 149

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lbpp-rust-2.0.0.html";
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