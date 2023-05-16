<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scicite" />
  <meta itemprop="description" content="This is a dataset for classifying citation intents in academic papers.&#10;The main citation intent label for each Json object is specified with the label&#10;key while the citation context is specified in with a context key. Example:&#10;&#10;```json&#10;{&#10; &#x27;string&#x27;: &#x27;In chacma baboons, male-infant relationships can be linked to both&#10;    formation of friendships and paternity success [30,31].&#x27;&#10; &#x27;sectionName&#x27;: &#x27;Introduction&#x27;,&#10; &#x27;label&#x27;: &#x27;background&#x27;,&#10; &#x27;citingPaperId&#x27;: &#x27;7a6b2d4b405439&#x27;,&#10; &#x27;citedPaperId&#x27;: &#x27;9d1abadc55b5e0&#x27;,&#10; ...&#10; }&#10;```&#10;&#10;You may obtain the full information about the paper using the provided paper ids&#10;with the Semantic Scholar API (https://api.semanticscholar.org/).&#10;&#10;The labels are: Method, Background, Result&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;scicite&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scicite" />
  <meta itemprop="sameAs" content="https://github.com/allenai/scicite" />
  <meta itemprop="citation" content="@InProceedings{Cohan2019Structural,&#10;  author={Arman Cohan and Waleed Ammar and Madeleine Van Zuylen and Field Cady},&#10;  title={Structural Scaffolds for Citation Intent Classification in Scientific Publications},&#10;  booktitle=&quot;NAACL&quot;,&#10;  year=&quot;2019&quot;&#10;}" />
</div>

# `scicite`


*   **Description**:

This is a dataset for classifying citation intents in academic papers. The main
citation intent label for each Json object is specified with the label key while
the citation context is specified in with a context key. Example:

```json
{
 'string': 'In chacma baboons, male-infant relationships can be linked to both
    formation of friendships and paternity success [30,31].'
 'sectionName': 'Introduction',
 'label': 'background',
 'citingPaperId': '7a6b2d4b405439',
 'citedPaperId': '9d1abadc55b5e0',
 ...
 }
```

You may obtain the full information about the paper using the provided paper ids
with the Semantic Scholar API (https://api.semanticscholar.org/).

The labels are: Method, Background, Result

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/scicite">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/allenai/scicite](https://github.com/allenai/scicite)

*   **Source code**:
    [`tfds.datasets.scicite.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/scicite/scicite_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `22.12 MiB`

*   **Dataset size**: `7.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,859
`'train'`      | 8,194
`'validation'` | 916

*   **Feature structure**:

```python
FeaturesDict({
    'citeEnd': int64,
    'citeStart': int64,
    'citedPaperId': Text(shape=(), dtype=string),
    'citingPaperId': Text(shape=(), dtype=string),
    'excerpt_index': int32,
    'id': Text(shape=(), dtype=string),
    'isKeyCitation': bool,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'label2': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'label2_confidence': float32,
    'label_confidence': float32,
    'sectionName': Text(shape=(), dtype=string),
    'source': ClassLabel(shape=(), dtype=int64, num_classes=7),
    'string': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
citeEnd           | Tensor       |       | int64   |
citeStart         | Tensor       |       | int64   |
citedPaperId      | Text         |       | string  |
citingPaperId     | Text         |       | string  |
excerpt_index     | Tensor       |       | int32   |
id                | Text         |       | string  |
isKeyCitation     | Tensor       |       | bool    |
label             | ClassLabel   |       | int64   |
label2            | ClassLabel   |       | int64   |
label2_confidence | Tensor       |       | float32 |
label_confidence  | Tensor       |       | float32 |
sectionName       | Text         |       | string  |
source            | ClassLabel   |       | int64   |
string            | Text         |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('string', 'label')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scicite-1.0.0.html";
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
@InProceedings{Cohan2019Structural,
  author={Arman Cohan and Waleed Ammar and Madeleine Van Zuylen and Field Cady},
  title={Structural Scaffolds for Citation Intent Classification in Scientific Publications},
  booktitle="NAACL",
  year="2019"
}
```

