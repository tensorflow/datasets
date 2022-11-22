<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xnli" />
  <meta itemprop="description" content="XNLI is a subset of a few thousand examples from MNLI which has been translated&#10;into a 14 different languages (some low-ish resource). As with MNLI, the goal is&#10;to predict textual entailment (does sentence A imply/contradict/neither sentence&#10;B) and is a classification task (given two sentences, predict one of three&#10;labels).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xnli&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xnli" />
  <meta itemprop="sameAs" content="https://www.nyu.edu/projects/bowman/xnli/" />
  <meta itemprop="citation" content="@InProceedings{conneau2018xnli,&#10;  author = &quot;Conneau, Alexis&#10;                 and Rinott, Ruty&#10;                 and Lample, Guillaume&#10;                 and Williams, Adina&#10;                 and Bowman, Samuel R.&#10;                 and Schwenk, Holger&#10;                 and Stoyanov, Veselin&quot;,&#10;  title = &quot;XNLI: Evaluating Cross-lingual Sentence Representations&quot;,&#10;  booktitle = &quot;Proceedings of the 2018 Conference on Empirical Methods&#10;               in Natural Language Processing&quot;,&#10;  year = &quot;2018&quot;,&#10;  publisher = &quot;Association for Computational Linguistics&quot;,&#10;  location = &quot;Brussels, Belgium&quot;,&#10;}" />
</div>

# `xnli`


*   **Description**:

XNLI is a subset of a few thousand examples from MNLI which has been translated
into a 14 different languages (some low-ish resource). As with MNLI, the goal is
to predict textual entailment (does sentence A imply/contradict/neither sentence
B) and is a classification task (given two sentences, predict one of three
labels).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/xnli">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.nyu.edu/projects/bowman/xnli/](https://www.nyu.edu/projects/bowman/xnli/)

*   **Source code**:
    [`tfds.text.Xnli`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/xnli.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Download size**: `17.04 MiB`

*   **Dataset size**: `29.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 5,010
`'validation'` | 2,490

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': TranslationVariableLanguages({
        'language': Text(shape=(), dtype=object),
        'translation': Text(shape=(), dtype=object),
    }),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'premise': Translation({
        'ar': Text(shape=(), dtype=object),
        'bg': Text(shape=(), dtype=object),
        'de': Text(shape=(), dtype=object),
        'el': Text(shape=(), dtype=object),
        'en': Text(shape=(), dtype=object),
        'es': Text(shape=(), dtype=object),
        'fr': Text(shape=(), dtype=object),
        'hi': Text(shape=(), dtype=object),
        'ru': Text(shape=(), dtype=object),
        'sw': Text(shape=(), dtype=object),
        'th': Text(shape=(), dtype=object),
        'tr': Text(shape=(), dtype=object),
        'ur': Text(shape=(), dtype=object),
        'vi': Text(shape=(), dtype=object),
        'zh': Text(shape=(), dtype=object),
    }),
})
```

*   **Feature documentation**:

Feature                | Class                        | Shape | Dtype  | Description
:--------------------- | :--------------------------- | :---- | :----- | :----------
                       | FeaturesDict                 |       |        |
hypothesis             | TranslationVariableLanguages |       |        |
hypothesis/language    | Text                         |       | object |
hypothesis/translation | Text                         |       | object |
label                  | ClassLabel                   |       | int64  |
premise                | Translation                  |       |        |
premise/ar             | Text                         |       | object |
premise/bg             | Text                         |       | object |
premise/de             | Text                         |       | object |
premise/el             | Text                         |       | object |
premise/en             | Text                         |       | object |
premise/es             | Text                         |       | object |
premise/fr             | Text                         |       | object |
premise/hi             | Text                         |       | object |
premise/ru             | Text                         |       | object |
premise/sw             | Text                         |       | object |
premise/th             | Text                         |       | object |
premise/tr             | Text                         |       | object |
premise/ur             | Text                         |       | object |
premise/vi             | Text                         |       | object |
premise/zh             | Text                         |       | object |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xnli-1.1.0.html";
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

*   **Citation**:

```
@InProceedings{conneau2018xnli,
  author = "Conneau, Alexis
                 and Rinott, Ruty
                 and Lample, Guillaume
                 and Williams, Adina
                 and Bowman, Samuel R.
                 and Schwenk, Holger
                 and Stoyanov, Veselin",
  title = "XNLI: Evaluating Cross-lingual Sentence Representations",
  booktitle = "Proceedings of the 2018 Conference on Empirical Methods
               in Natural Language Processing",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  location = "Brussels, Belgium",
}
```

