<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia_toxicity_subtypes" />
  <meta itemprop="description" content="The comments in this dataset come from an archive of Wikipedia talk page&#10;comments. These have been annotated by Jigsaw for toxicity, as well as (for the&#10;main config) a variety of toxicity subtypes, including severe toxicity,&#10;obscenity, threatening language, insulting language, and identity attacks. This&#10;dataset is a replica of the data released for the Jigsaw Toxic Comment&#10;Classification Challenge and Jigsaw Multilingual Toxic Comment Classification&#10;competition on Kaggle, with the test dataset merged with the test_labels&#10;released after the end of the competitions. Test data not used for scoring has&#10;been dropped. This dataset is released under CC0, as is the underlying comment&#10;text.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikipedia_toxicity_subtypes&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia_toxicity_subtypes" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data" />
  <meta itemprop="citation" content="@inproceedings{10.1145/3038912.3052591,&#10;  author = {Wulczyn, Ellery and Thain, Nithum and Dixon, Lucas},&#10;  title = {Ex Machina: Personal Attacks Seen at Scale},&#10;  year = {2017},&#10;  isbn = {9781450349130},&#10;  publisher = {International World Wide Web Conferences Steering Committee},&#10;  address = {Republic and Canton of Geneva, CHE},&#10;  url = {https://doi.org/10.1145/3038912.3052591},&#10;  doi = {10.1145/3038912.3052591},&#10;  booktitle = {Proceedings of the 26th International Conference on World Wide Web},&#10;  pages = {1391-1399},&#10;  numpages = {9},&#10;  keywords = {online discussions, wikipedia, online harassment},&#10;  location = {Perth, Australia},&#10;  series = {WWW &#x27;17}&#10;}" />
</div>

# `wikipedia_toxicity_subtypes`


*   **Description**:

The comments in this dataset come from an archive of Wikipedia talk page
comments. These have been annotated by Jigsaw for toxicity, as well as (for the
main config) a variety of toxicity subtypes, including severe toxicity,
obscenity, threatening language, insulting language, and identity attacks. This
dataset is a replica of the data released for the Jigsaw Toxic Comment
Classification Challenge and Jigsaw Multilingual Toxic Comment Classification
competition on Kaggle, with the test dataset merged with the test_labels
released after the end of the competitions. Test data not used for scoring has
been dropped. This dataset is released under CC0, as is the underlying comment
text.

*   **Source code**:
    [`tfds.text.WikipediaToxicitySubtypes`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia_toxicity_subtypes.py)

*   **Versions**:

    *   `0.2.0`: Updated features for consistency with CivilComments dataset.
    *   `0.3.0`: Added WikipediaToxicityMultilingual config.
    *   **`0.3.1`** (default): Added a unique id for each comment. (For the
        Multilingual config, these are only unique within each split.)

*   **Download size**: `50.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{10.1145/3038912.3052591,
  author = {Wulczyn, Ellery and Thain, Nithum and Dixon, Lucas},
  title = {Ex Machina: Personal Attacks Seen at Scale},
  year = {2017},
  isbn = {9781450349130},
  publisher = {International World Wide Web Conferences Steering Committee},
  address = {Republic and Canton of Geneva, CHE},
  url = {https://doi.org/10.1145/3038912.3052591},
  doi = {10.1145/3038912.3052591},
  booktitle = {Proceedings of the 26th International Conference on World Wide Web},
  pages = {1391-1399},
  numpages = {9},
  keywords = {online discussions, wikipedia, online harassment},
  location = {Perth, Australia},
  series = {WWW '17}
}
```


## wikipedia_toxicity_subtypes/EnglishSubtypes (default config)

*   **Config description**: The comments in the WikipediaToxicitySubtypes config
    are from an archive of English Wikipedia talk page comments which have been
    annotated by Jigsaw for toxicity, as well as five toxicity subtype labels
    (severe toxicity, obscene, threat, insult, identity_attack). The toxicity
    and toxicity subtype labels are binary values (0 or 1) indicating whether
    the majority of annotators assigned that attribute to the comment text. This
    config is a replica of the data released for the Jigsaw Toxic Comment
    Classification Challenge on Kaggle, with the test dataset joined with the
    test_labels released after the competition, and test data not used for
    scoring dropped.

See the Kaggle documentation
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data or
https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more
details.

*   **Homepage**:
    [https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data)

*   **Dataset size**: `128.32 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 63,978
`'train'` | 159,571

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'identity_attack': float32,
    'insult': float32,
    'language': Text(shape=(), dtype=string),
    'obscene': float32,
    'severe_toxicity': float32,
    'text': Text(shape=(), dtype=string),
    'threat': float32,
    'toxicity': float32,
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype   | Description
:-------------- | :----------- | :---- | :------ | :----------
                | FeaturesDict |       |         |
id              | Text         |       | string  |
identity_attack | Tensor       |       | float32 |
insult          | Tensor       |       | float32 |
language        | Text         |       | string  |
obscene         | Tensor       |       | float32 |
severe_toxicity | Tensor       |       | float32 |
text            | Text         |       | string  |
threat          | Tensor       |       | float32 |
toxicity        | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia_toxicity_subtypes-EnglishSubtypes-0.3.1.html";
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

## wikipedia_toxicity_subtypes/Multilingual

*   **Config description**: The comments in the WikipediaToxicityMultilingual
    config here are from an archive of non-English Wikipedia talk page comments
    annotated by Jigsaw for toxicity, with a binary value (0 or 1) indicating
    whether the majority of annotators rated the comment text as toxic. The
    comments in this config are in multiple different languages (Turkish,
    Italian, Spanish, Portuguese, Russian, and French). This config is a replica
    of the data released for the Jigsaw Multilingual Toxic Comment
    Classification on Kaggle, with the test dataset joined with the test_labels
    released after the competition.

See the Kaggle documentation
https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data
for more details.

*   **Homepage**:
    [https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data)

*   **Dataset size**: `35.13 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 63,812
`'validation'` | 8,000

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'language': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
    'toxicity': float32,
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype   | Description
:------- | :----------- | :---- | :------ | :----------
         | FeaturesDict |       |         |
id       | Text         |       | string  |
language | Text         |       | string  |
text     | Text         |       | string  |
toxicity | Tensor       |       | float32 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia_toxicity_subtypes-Multilingual-0.3.1.html";
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