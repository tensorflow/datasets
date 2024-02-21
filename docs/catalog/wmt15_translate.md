<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wmt15_translate" />
  <meta itemprop="description" content="Translate dataset based on the data from statmt.org.&#10;&#10;Versions exists for the different years using a combination of multiple data&#10;sources. The base `wmt_translate` allows you to create your own config to choose&#10;your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.&#10;&#10;```&#10;config = tfds.translate.wmt.WmtConfig(&#10;    version=&quot;0.0.1&quot;,&#10;    language_pair=(&quot;fr&quot;, &quot;de&quot;),&#10;    subsets={&#10;        tfds.Split.TRAIN: [&quot;commoncrawl_frde&quot;],&#10;        tfds.Split.VALIDATION: [&quot;euelections_dev2019&quot;],&#10;    },&#10;)&#10;builder = tfds.builder(&quot;wmt_translate&quot;, config=config)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wmt15_translate&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wmt15_translate" />
  <meta itemprop="sameAs" content="http://www.statmt.org/wmt15/translation-task.html" />
  <meta itemprop="citation" content="@InProceedings{bojar-EtAl:2015:WMT,&#10;  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Haddow, Barry  and  Huck, Matthias  and  Hokamp, Chris  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco},&#10;  title     = {Findings of the 2015 Workshop on Statistical Machine Translation},&#10;  booktitle = {Proceedings of the Tenth Workshop on Statistical Machine Translation},&#10;  month     = {September},&#10;  year      = {2015},&#10;  address   = {Lisbon, Portugal},&#10;  publisher = {Association for Computational Linguistics},&#10;  pages     = {1--46},&#10;  url       = {http://aclweb.org/anthology/W15-3001}&#10;}" />
</div>

# `wmt15_translate`


Warning: Manual download required. See instructions below.

*   **Description**:

Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `tfds.translate.wmt.WmtConfig`.

```
config = tfds.translate.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        tfds.Split.TRAIN: ["commoncrawl_frde"],
        tfds.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = tfds.builder("wmt_translate", config=config)
```

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/wmt-2015">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.statmt.org/wmt15/translation-task.html](http://www.statmt.org/wmt15/translation-task.html)

*   **Source code**:
    [`tfds.translate.Wmt15Translate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/wmt15.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Some of the wmt configs here, require a manual download.
    Please look into wmt.py to see the exact path (and file name) that has to
    be downloaded.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@InProceedings{bojar-EtAl:2015:WMT,
  author    = {Bojar, Ond{r}ej  and  Chatterjee, Rajen  and  Federmann, Christian  and  Haddow, Barry  and  Huck, Matthias  and  Hokamp, Chris  and  Koehn, Philipp  and  Logacheva, Varvara  and  Monz, Christof  and  Negri, Matteo  and  Post, Matt  and  Scarton, Carolina  and  Specia, Lucia  and  Turchi, Marco},
  title     = {Findings of the 2015 Workshop on Statistical Machine Translation},
  booktitle = {Proceedings of the Tenth Workshop on Statistical Machine Translation},
  month     = {September},
  year      = {2015},
  address   = {Lisbon, Portugal},
  publisher = {Association for Computational Linguistics},
  pages     = {1--46},
  url       = {http://aclweb.org/anthology/W15-3001}
}
```


## wmt15_translate/cs-en (default config)

*   **Config description**: WMT 2015 cs-en translation task dataset.

*   **Download size**: `1.62 GiB`

*   **Dataset size**: `2.89 GiB`

*   **Splits**:

Split          | Examples
:------------- | ---------:
`'test'`       | 2,656
`'train'`      | 15,793,126
`'validation'` | 3,003

*   **Feature structure**:

```python
Translation({
    'cs': Text(shape=(), dtype=string),
    'en': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype  | Description
:------ | :---------- | :---- | :----- | :----------
        | Translation |       |        |
cs      | Text        |       | string |
en      | Text        |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('cs', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt15_translate-cs-en-1.0.0.html";
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

## wmt15_translate/de-en

*   **Config description**: WMT 2015 de-en translation task dataset.

*   **Download size**: `1.62 GiB`

*   **Dataset size**: `1.37 GiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 2,169
`'train'`      | 4,522,998
`'validation'` | 3,003

*   **Feature structure**:

```python
Translation({
    'de': Text(shape=(), dtype=string),
    'en': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype  | Description
:------ | :---------- | :---- | :----- | :----------
        | Translation |       |        |
de      | Text        |       | string |
en      | Text        |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('de', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt15_translate-de-en-1.0.0.html";
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

## wmt15_translate/fi-en

*   **Config description**: WMT 2015 fi-en translation task dataset.

*   **Download size**: `260.51 MiB`

*   **Dataset size**: `623.22 MiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 1,370
`'train'`      | 2,073,394
`'validation'` | 1,500

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=string),
    'fi': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype  | Description
:------ | :---------- | :---- | :----- | :----------
        | Translation |       |        |
en      | Text        |       | string |
fi      | Text        |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('fi', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt15_translate-fi-en-1.0.0.html";
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

## wmt15_translate/fr-en

*   **Config description**: WMT 2015 fr-en translation task dataset.

*   **Download size**: `6.24 GiB`

*   **Dataset size**: `14.65 GiB`

*   **Splits**:

Split          | Examples
:------------- | ---------:
`'test'`       | 1,500
`'train'`      | 40,853,298
`'validation'` | 4,503

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=string),
    'fr': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype  | Description
:------ | :---------- | :---- | :----- | :----------
        | Translation |       |        |
en      | Text        |       | string |
fr      | Text        |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('fr', 'en')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt15_translate-fr-en-1.0.0.html";
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

## wmt15_translate/ru-en

*   **Config description**: WMT 2015 ru-en translation task dataset.

*   **Download size**: `1.02 GiB`

*   **Dataset size**: `843.90 MiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 2,818
`'train'`      | 2,495,081
`'validation'` | 3,003

*   **Feature structure**:

```python
Translation({
    'en': Text(shape=(), dtype=string),
    'ru': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class       | Shape | Dtype  | Description
:------ | :---------- | :---- | :----- | :----------
        | Translation |       |        |
en      | Text        |       | string |
ru      | Text        |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wmt15_translate-ru-en-1.0.0.html";
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