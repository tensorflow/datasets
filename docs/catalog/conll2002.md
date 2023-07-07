<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="conll2002" />
  <meta itemprop="description" content="The shared task of CoNLL-2002 concerns language-independent named entity&#10;recognition. The types of named entities include: persons, locations,&#10;organizations and names of miscellaneous entities that do not belong to the&#10;previous three groups. The participants of the shared task were offered training&#10;and test data for at least two languages. Information sources other than the&#10;training data might have been used in this shared task.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;conll2002&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/conll2002" />
  <meta itemprop="sameAs" content="https://aclanthology.org/W02-2024/" />
  <meta itemprop="citation" content="@inproceedings{tjong-kim-sang-2002-introduction,&#10;    title = &quot;Introduction to the {C}o{NLL}-2002 Shared Task: Language-Independent Named Entity Recognition&quot;,&#10;    author = &quot;Tjong Kim Sang, Erik F.&quot;,&#10;    booktitle = &quot;{COLING}-02: The 6th Conference on Natural Language Learning 2002 ({C}o{NLL}-2002)&quot;,&#10;    year = &quot;2002&quot;,&#10;    url = &quot;https://aclanthology.org/W02-2024&quot;,&#10;}" />
</div>

# `conll2002`


*   **Description**:

The shared task of CoNLL-2002 concerns language-independent named entity
recognition. The types of named entities include: persons, locations,
organizations and names of miscellaneous entities that do not belong to the
previous three groups. The participants of the shared task were offered training
and test data for at least two languages. Information sources other than the
training data might have been used in this shared task.

*   **Homepage**:
    [https://aclanthology.org/W02-2024/](https://aclanthology.org/W02-2024/)

*   **Source code**:
    [`tfds.text.conll2002.Conll2002`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/conll2002/conll2002.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{tjong-kim-sang-2002-introduction,
    title = "Introduction to the {C}o{NLL}-2002 Shared Task: Language-Independent Named Entity Recognition",
    author = "Tjong Kim Sang, Erik F.",
    booktitle = "{COLING}-02: The 6th Conference on Natural Language Learning 2002 ({C}o{NLL}-2002)",
    year = "2002",
    url = "https://aclanthology.org/W02-2024",
}
```


## conll2002/es (default config)

*   **Download size**: `3.95 MiB`

*   **Dataset size**: `3.52 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,916
`'test'`  | 1,518
`'train'` | 8,324

*   **Feature structure**:

```python
FeaturesDict({
    'ner': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=9)),
    'pos': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=60)),
    'tokens': Sequence(Text(shape=(), dtype=string)),
})
```

*   **Feature documentation**:

Feature | Class                | Shape   | Dtype  | Description
:------ | :------------------- | :------ | :----- | :----------
        | FeaturesDict         |         |        |
ner     | Sequence(ClassLabel) | (None,) | int64  |
pos     | Sequence(ClassLabel) | (None,) | int64  |
tokens  | Sequence(Text)       | (None,) | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/conll2002-es-1.0.0.html";
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

## conll2002/nl

*   **Download size**: `3.47 MiB`

*   **Dataset size**: `3.55 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,896
`'test'`  | 5,196
`'train'` | 15,807

*   **Feature structure**:

```python
FeaturesDict({
    'ner': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=9)),
    'pos': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=12)),
    'tokens': Sequence(Text(shape=(), dtype=string)),
})
```

*   **Feature documentation**:

Feature | Class                | Shape   | Dtype  | Description
:------ | :------------------- | :------ | :----- | :----------
        | FeaturesDict         |         |        |
ner     | Sequence(ClassLabel) | (None,) | int64  |
pos     | Sequence(ClassLabel) | (None,) | int64  |
tokens  | Sequence(Text)       | (None,) | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/conll2002-nl-1.0.0.html";
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