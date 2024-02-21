<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="web_questions" />
  <meta itemprop="description" content="This dataset consists of 6,642 question/answer pairs.&#10;The questions are supposed to be answerable by Freebase, a large knowledge graph.&#10;The questions are mostly centered around a single named entity.&#10;The questions are popular ones asked on the web (at least in 2013).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;web_questions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/web_questions" />
  <meta itemprop="sameAs" content="https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a" />
  <meta itemprop="citation" content="@inproceedings{berant-etal-2013-semantic,&#10;    title = &quot;Semantic Parsing on {F}reebase from Question-Answer Pairs&quot;,&#10;    author = &quot;Berant, Jonathan  and&#10;      Chou, Andrew  and&#10;      Frostig, Roy  and&#10;      Liang, Percy&quot;,&#10;    booktitle = &quot;Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = oct,&#10;    year = &quot;2013&quot;,&#10;    address = &quot;Seattle, Washington, USA&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/D13-1160&quot;,&#10;    pages = &quot;1533--1544&quot;,&#10;}" />
</div>

# `web_questions`


*   **Description**:

This dataset consists of 6,642 question/answer pairs. The questions are supposed
to be answerable by Freebase, a large knowledge graph. The questions are mostly
centered around a single named entity. The questions are popular ones asked on
the web (at least in 2013).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/webquestions">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a](https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a)

*   **Source code**:
    [`tfds.question_answering.WebQuestions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/web_questions.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.21 MiB`

*   **Dataset size**: `983.88 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,032
`'train'` | 3,778

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence(Text(shape=(), dtype=string)),
    'question': Text(shape=(), dtype=string),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature  | Class          | Shape   | Dtype  | Description
:------- | :------------- | :------ | :----- | :----------
         | FeaturesDict   |         |        |
answers  | Sequence(Text) | (None,) | string |
question | Text           |         | string |
url      | Text           |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/web_questions-1.0.0.html";
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
@inproceedings{berant-etal-2013-semantic,
    title = "Semantic Parsing on {F}reebase from Question-Answer Pairs",
    author = "Berant, Jonathan  and
      Chou, Andrew  and
      Frostig, Roy  and
      Liang, Percy",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1160",
    pages = "1533--1544",
}
```

