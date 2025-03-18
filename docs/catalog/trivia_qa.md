<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="trivia_qa" />
  <meta itemprop="description" content="TriviaqQA is a reading comprehension dataset containing over 650K&#10;question-answer-evidence triples. TriviaqQA includes 95K question-answer pairs&#10;authored by trivia enthusiasts and independently gathered evidence documents,&#10;six per question on average, that provide high quality distant supervision for&#10;answering the questions.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;trivia_qa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/trivia_qa" />
  <meta itemprop="sameAs" content="http://nlp.cs.washington.edu/triviaqa/" />
  <meta itemprop="citation" content="@article{2017arXivtriviaqa,&#10;       author = {{Joshi}, Mandar and {Choi}, Eunsol and {Weld},&#10;                 Daniel and {Zettlemoyer}, Luke},&#10;        title = &quot;{triviaqa: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension}&quot;,&#10;      journal = {arXiv e-prints},&#10;         year = 2017,&#10;          eid = {arXiv:1705.03551},&#10;        pages = {arXiv:1705.03551},&#10;archivePrefix = {arXiv},&#10;       eprint = {1705.03551},&#10;}" />
</div>

# `trivia_qa`


*   **Description**:

TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer pairs
authored by trivia enthusiasts and independently gathered evidence documents,
six per question on average, that provide high quality distant supervision for
answering the questions.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/triviaqa">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://nlp.cs.washington.edu/triviaqa/](http://nlp.cs.washington.edu/triviaqa/)

*   **Source code**:
    [`tfds.datasets.trivia_qa.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/trivia_qa/trivia_qa_dataset_builder.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Feature structure**:

```python
FeaturesDict({
    'answer': FeaturesDict({
        'aliases': Sequence(Text(shape=(), dtype=string)),
        'matched_wiki_entity_name': Text(shape=(), dtype=string),
        'normalized_aliases': Sequence(Text(shape=(), dtype=string)),
        'normalized_matched_wiki_entity_name': Text(shape=(), dtype=string),
        'normalized_value': Text(shape=(), dtype=string),
        'type': Text(shape=(), dtype=string),
        'value': Text(shape=(), dtype=string),
    }),
    'entity_pages': Sequence({
        'doc_source': Text(shape=(), dtype=string),
        'filename': Text(shape=(), dtype=string),
        'title': Text(shape=(), dtype=string),
        'wiki_context': Text(shape=(), dtype=string),
    }),
    'question': Text(shape=(), dtype=string),
    'question_id': Text(shape=(), dtype=string),
    'question_source': Text(shape=(), dtype=string),
    'search_results': Sequence({
        'description': Text(shape=(), dtype=string),
        'filename': Text(shape=(), dtype=string),
        'rank': int32,
        'search_context': Text(shape=(), dtype=string),
        'title': Text(shape=(), dtype=string),
        'url': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class          | Shape   | Dtype  | Description
:----------------------------------------- | :------------- | :------ | :----- | :----------
                                           | FeaturesDict   |         |        |
answer                                     | FeaturesDict   |         |        |
answer/aliases                             | Sequence(Text) | (None,) | string |
answer/matched_wiki_entity_name            | Text           |         | string |
answer/normalized_aliases                  | Sequence(Text) | (None,) | string |
answer/normalized_matched_wiki_entity_name | Text           |         | string |
answer/normalized_value                    | Text           |         | string |
answer/type                                | Text           |         | string |
answer/value                               | Text           |         | string |
entity_pages                               | Sequence       |         |        |
entity_pages/doc_source                    | Text           |         | string |
entity_pages/filename                      | Text           |         | string |
entity_pages/title                         | Text           |         | string |
entity_pages/wiki_context                  | Text           |         | string |
question                                   | Text           |         | string |
question_id                                | Text           |         | string |
question_source                            | Text           |         | string |
search_results                             | Sequence       |         |        |
search_results/description                 | Text           |         | string |
search_results/filename                    | Text           |         | string |
search_results/rank                        | Tensor         |         | int32  |
search_results/search_context              | Text           |         | string |
search_results/title                       | Text           |         | string |
search_results/url                         | Text           |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{2017arXivtriviaqa,
       author = {{Joshi}, Mandar and {Choi}, Eunsol and {Weld},
                 Daniel and {Zettlemoyer}, Luke},
        title = "{triviaqa: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension}",
      journal = {arXiv e-prints},
         year = 2017,
          eid = {arXiv:1705.03551},
        pages = {arXiv:1705.03551},
archivePrefix = {arXiv},
       eprint = {1705.03551},
}
```


## trivia_qa/rc (default config)

*   **Config description**: Question-answer pairs where all documents for a
    given question contain the answer string(s). Includes context from Wikipedia
    and search results.

*   **Download size**: `2.48 GiB`

*   **Dataset size**: `14.99 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 17,210
`'train'`      | 138,384
`'validation'` | 18,669

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/trivia_qa-rc-1.1.0.html";
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

## trivia_qa/rc.nocontext

*   **Config description**: Question-answer pairs where all documents for a
    given question contain the answer string(s).

*   **Download size**: `2.48 GiB`

*   **Dataset size**: `196.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 17,210
`'train'`      | 138,384
`'validation'` | 18,669

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/trivia_qa-rc.nocontext-1.1.0.html";
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

## trivia_qa/unfiltered

*   **Config description**: 110k question-answer pairs for open domain QA where
    not all documents for a given question contain the answer string(s). This
    makes the unfiltered dataset more appropriate for IR-style QA. Includes
    context from Wikipedia and search results.

*   **Download size**: `3.07 GiB`

*   **Dataset size**: `27.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,832
`'train'`      | 87,622
`'validation'` | 11,313

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/trivia_qa-unfiltered-1.1.0.html";
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

## trivia_qa/unfiltered.nocontext

*   **Config description**: 110k question-answer pairs for open domain QA where
    not all documents for a given question contain the answer string(s). This
    makes the unfiltered dataset more appropriate for IR-style QA.

*   **Download size**: `603.25 MiB`

*   **Dataset size**: `119.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,832
`'train'`      | 87,622
`'validation'` | 11,313

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/trivia_qa-unfiltered.nocontext-1.1.0.html";
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