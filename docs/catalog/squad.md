<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="squad" />
  <meta itemprop="description" content="Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset,&#10;consisting of questions posed by crowdworkers on a set of Wikipedia articles,&#10;where the answer to every question is a segment of text, or span, from the&#10;corresponding reading passage, or the question might be unanswerable.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;squad&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/squad" />
  <meta itemprop="sameAs" content="https://rajpurkar.github.io/SQuAD-explorer/" />
  <meta itemprop="citation" content="@article{2016arXiv160605250R,&#10;       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},&#10;                 Konstantin and {Liang}, Percy},&#10;        title = &quot;{SQuAD: 100,000+ Questions for Machine Comprehension of Text}&quot;,&#10;      journal = {arXiv e-prints},&#10;         year = 2016,&#10;          eid = {arXiv:1606.05250},&#10;        pages = {arXiv:1606.05250},&#10;archivePrefix = {arXiv},&#10;       eprint = {1606.05250},&#10;}" />
</div>

# `squad`


*   **Description**:

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset,
consisting of questions posed by crowdworkers on a set of Wikipedia articles,
where the answer to every question is a segment of text, or span, from the
corresponding reading passage, or the question might be unanswerable.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/squad">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)

*   **Source code**:
    [`tfds.datasets.squad.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/squad/squad_dataset_builder.py)

*   **Versions**:

    *   **`3.0.0`** (default): Fixes issue with small number of examples (19)
        where answer spans are misaligned due to context white-space removal.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
```


## squad/v1.1 (default config)

*   **Config description**: Version 1.1.0 of SQUAD

*   **Download size**: `33.51 MiB`

*   **Dataset size**: `94.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 87,599
`'validation'` | 10,570

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': int32,
        'text': Text(shape=(), dtype=string),
    }),
    'context': Text(shape=(), dtype=string),
    'id': string,
    'question': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature              | Class        | Shape | Dtype  | Description
:------------------- | :----------- | :---- | :----- | :----------
                     | FeaturesDict |       |        |
answers              | Sequence     |       |        |
answers/answer_start | Tensor       |       | int32  |
answers/text         | Text         |       | string |
context              | Text         |       | string |
id                   | Tensor       |       | string |
question             | Text         |       | string |
title                | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/squad-v1.1-3.0.0.html";
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

## squad/v2.0

*   **Config description**: Version 2.0.0 of SQUAD

*   **Download size**: `44.34 MiB`

*   **Dataset size**: `148.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 130,319
`'validation'` | 11,873

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': int32,
        'text': Text(shape=(), dtype=string),
    }),
    'context': Text(shape=(), dtype=string),
    'id': string,
    'is_impossible': bool,
    'plausible_answers': Sequence({
        'answer_start': int32,
        'text': Text(shape=(), dtype=string),
    }),
    'question': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype  | Description
:----------------------------- | :----------- | :---- | :----- | :----------
                               | FeaturesDict |       |        |
answers                        | Sequence     |       |        |
answers/answer_start           | Tensor       |       | int32  |
answers/text                   | Text         |       | string |
context                        | Text         |       | string |
id                             | Tensor       |       | string |
is_impossible                  | Tensor       |       | bool   |
plausible_answers              | Sequence     |       |        |
plausible_answers/answer_start | Tensor       |       | int32  |
plausible_answers/text         | Text         |       | string |
question                       | Text         |       | string |
title                          | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/squad-v2.0-3.0.0.html";
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