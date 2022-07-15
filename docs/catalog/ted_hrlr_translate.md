<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ted_hrlr_translate" />
  <meta itemprop="description" content="Data sets derived from TED talk transcripts for comparing similar language pairs&#10;where one is high resource and the other is low resource.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ted_hrlr_translate&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ted_hrlr_translate" />
  <meta itemprop="sameAs" content="https://github.com/neulab/word-embeddings-for-nmt" />
  <meta itemprop="citation" content="@inproceedings{Ye2018WordEmbeddings,&#10;  author  = {Ye, Qi and Devendra, Sachan and Matthieu, Felix and Sarguna, Padmanabhan and Graham, Neubig},&#10;  title   = {When and Why are pre-trained word embeddings useful for Neural Machine Translation},&#10;  booktitle = {HLT-NAACL},&#10;  year    = {2018},&#10;  }" />
</div>

# `ted_hrlr_translate`


*   **Description**:

Data sets derived from TED talk transcripts for comparing similar language pairs
where one is high resource and the other is low resource.

*   **Homepage**:
    [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

*   **Source code**:
    [`tfds.translate.TedHrlrTranslate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/ted_hrlr.py)

*   **Versions**:

    *   **`1.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{Ye2018WordEmbeddings,
  author  = {Ye, Qi and Devendra, Sachan and Matthieu, Felix and Sarguna, Padmanabhan and Graham, Neubig},
  title   = {When and Why are pre-trained word embeddings useful for Neural Machine Translation},
  booktitle = {HLT-NAACL},
  year    = {2018},
  }
```


## ted_hrlr_translate/az_to_en (default config)

*   **Config description**: Translation dataset from az to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'az': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
az      | Text        |       | tf.string |
en      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('az', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-az_to_en-1.0.0.html";
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

## ted_hrlr_translate/aztr_to_en

*   **Config description**: Translation dataset from az_tr to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'az_tr': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
az_tr   | Text        |       | tf.string |
en      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('az_tr', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-aztr_to_en-1.0.0.html";
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

## ted_hrlr_translate/be_to_en

*   **Config description**: Translation dataset from be to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'be': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
be      | Text        |       | tf.string |
en      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('be', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-be_to_en-1.0.0.html";
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

## ted_hrlr_translate/beru_to_en

*   **Config description**: Translation dataset from be_ru to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'be_ru': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
be_ru   | Text        |       | tf.string |
en      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('be_ru', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-beru_to_en-1.0.0.html";
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

## ted_hrlr_translate/es_to_pt

*   **Config description**: Translation dataset from es to pt in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'es': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
es      | Text        |       | tf.string |
pt      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('es', 'pt')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-es_to_pt-1.0.0.html";
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

## ted_hrlr_translate/fr_to_pt

*   **Config description**: Translation dataset from fr to pt in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'fr': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
fr      | Text        |       | tf.string |
pt      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('fr', 'pt')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-fr_to_pt-1.0.0.html";
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

## ted_hrlr_translate/gl_to_en

*   **Config description**: Translation dataset from gl to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
en      | Text        |       | tf.string |
gl      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('gl', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-gl_to_en-1.0.0.html";
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

## ted_hrlr_translate/glpt_to_en

*   **Config description**: Translation dataset from gl_pt to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl_pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
en      | Text        |       | tf.string |
gl_pt   | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('gl_pt', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-glpt_to_en-1.0.0.html";
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

## ted_hrlr_translate/he_to_pt

*   **Config description**: Translation dataset from he to pt in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'he': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
he      | Text        |       | tf.string |
pt      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('he', 'pt')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-he_to_pt-1.0.0.html";
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

## ted_hrlr_translate/it_to_pt

*   **Config description**: Translation dataset from it to pt in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'it': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
it      | Text        |       | tf.string |
pt      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('it', 'pt')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-it_to_pt-1.0.0.html";
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

## ted_hrlr_translate/pt_to_en

*   **Config description**: Translation dataset from pt to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
en      | Text        |       | tf.string |
pt      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('pt', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-pt_to_en-1.0.0.html";
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

## ted_hrlr_translate/ru_to_en

*   **Config description**: Translation dataset from ru to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
en      | Text        |       | tf.string |
ru      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('ru', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-ru_to_en-1.0.0.html";
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

## ted_hrlr_translate/ru_to_pt

*   **Config description**: Translation dataset from ru to pt in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'pt': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
pt      | Text        |       | tf.string |
ru      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('ru', 'pt')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-ru_to_pt-1.0.0.html";
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

## ted_hrlr_translate/tr_to_en

*   **Config description**: Translation dataset from tr to en in plain text.

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype     | Description
:------ | :---------- | :---- | :-------- | :----------
        | Translation |       |           |
en      | Text        |       | tf.string |
tr      | Text        |       | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('tr', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ted_hrlr_translate-tr_to_en-1.0.0.html";
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