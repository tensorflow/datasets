<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asqa" />
  <meta itemprop="description" content="ASQA is the first long-form question answering dataset that focuses on ambiguous&#10;factoid questions. Different from previous long-form answers datasets, each&#10;question is annotated with both long-form answers and extractive question-answer&#10;pairs, which should be answerable by the generated passage. A generated&#10;long-form answer will be evaluated using both ROUGE and QA accuracy. We showed&#10;that these evaluation metrics correlated with human judgment well. In this&#10;repostory we release the ASQA dataset, together with the evaluation code:&#10;`https://github.com/google-research/language/tree/master/language/asqa`&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asqa" />
  <meta itemprop="sameAs" content="https://github.com/google-research/language/tree/master/language/asqa" />
  <meta itemprop="citation" content="@misc{https://doi.org/10.48550/arxiv.2204.06092,&#10;doi = {10.48550/ARXIV.2204.06092},&#10;url = {https://arxiv.org/abs/2204.06092},&#10;author = {Stelmakh, Ivan and Luan, Yi and Dhingra, Bhuwan and Chang, Ming-Wei},&#10;keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},&#10;title = {ASQA: Factoid Questions Meet Long-Form Answers},&#10;publisher = {arXiv},&#10;year = {2022},&#10;copyright = {arXiv.org perpetual, non-exclusive license}&#10;}" />
</div>

# `asqa`


*   **Description**:

ASQA is the first long-form question answering dataset that focuses on ambiguous
factoid questions. Different from previous long-form answers datasets, each
question is annotated with both long-form answers and extractive question-answer
pairs, which should be answerable by the generated passage. A generated
long-form answer will be evaluated using both ROUGE and QA accuracy. We showed
that these evaluation metrics correlated with human judgment well. In this
repostory we release the ASQA dataset, together with the evaluation code:
`https://github.com/google-research/language/tree/master/language/asqa`

*   **Homepage**:
    [https://github.com/google-research/language/tree/master/language/asqa](https://github.com/google-research/language/tree/master/language/asqa)

*   **Source code**:
    [`tfds.datasets.asqa.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/asqa/asqa_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`2.0.0`** (default): Sample ID goes from int32 (overflowing) to int64.

*   **Download size**: `17.86 MiB`

*   **Dataset size**: `14.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 948
`'train'` | 4,353

*   **Feature structure**:

```python
FeaturesDict({
    'ambiguous_question': Text(shape=(), dtype=string),
    'annotations': Sequence({
        'knowledge': Sequence({
            'content': Text(shape=(), dtype=string),
            'wikipage': Text(shape=(), dtype=string),
        }),
        'long_answer': Text(shape=(), dtype=string),
    }),
    'qa_pairs': Sequence({
        'context': Text(shape=(), dtype=string),
        'question': Text(shape=(), dtype=string),
        'short_answers': Sequence(Text(shape=(), dtype=string)),
        'wikipage': Text(shape=(), dtype=string),
    }),
    'sample_id': int64,
    'wikipages': Sequence({
        'title': Text(shape=(), dtype=string),
        'url': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                        | Class          | Shape   | Dtype  | Description
:----------------------------- | :------------- | :------ | :----- | :----------
                               | FeaturesDict   |         |        |
ambiguous_question             | Text           |         | string | Disambiguated question from AmbigQA.
annotations                    | Sequence       |         |        | Long-form answers to the ambiguous question constructed by ASQA annotators.
annotations/knowledge          | Sequence       |         |        | List of additional knowledge pieces.
annotations/knowledge/content  | Text           |         | string | A passage from Wikipedia.
annotations/knowledge/wikipage | Text           |         | string | Title of the Wikipedia page the passage was taken from.
annotations/long_answer        | Text           |         | string | Annotation.
qa_pairs                       | Sequence       |         |        | Q&A pairs from AmbigQA which are used for disambiguation.
qa_pairs/context               | Text           |         | string | Additional context provided.
qa_pairs/question              | Text           |         | string |
qa_pairs/short_answers         | Sequence(Text) | (None,) | string | List of short answers from AmbigQA.
qa_pairs/wikipage              | Text           |         | string | Title of the Wikipedia page the additional context was taken from.
sample_id                      | Tensor         |         | int64  |
wikipages                      | Sequence       |         |        | List of Wikipedia pages visited by AmbigQA annotators.
wikipages/title                | Text           |         | string | Title of the Wikipedia page.
wikipages/url                  | Text           |         | string | Link to the Wikipedia page.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asqa-2.0.0.html";
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
@misc{https://doi.org/10.48550/arxiv.2204.06092,
doi = {10.48550/ARXIV.2204.06092},
url = {https://arxiv.org/abs/2204.06092},
author = {Stelmakh, Ivan and Luan, Yi and Dhingra, Bhuwan and Chang, Ming-Wei},
keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
title = {ASQA: Factoid Questions Meet Long-Form Answers},
publisher = {arXiv},
year = {2022},
copyright = {arXiv.org perpetual, non-exclusive license}
}
```

