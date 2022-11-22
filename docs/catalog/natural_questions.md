<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="natural_questions" />
  <meta itemprop="description" content="The NQ corpus contains questions from real users, and it requires QA systems to&#10;read and comprehend an entire Wikipedia article that may or may not contain the&#10;answer to the question. The inclusion of real user questions, and the&#10;requirement that solutions should read an entire page to find the answer, cause&#10;NQ to be a more realistic and challenging task than prior QA datasets.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;natural_questions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/natural_questions" />
  <meta itemprop="sameAs" content="https://ai.google.com/research/NaturalQuestions/dataset" />
  <meta itemprop="citation" content="@article{47761,&#10;title = {Natural Questions: a Benchmark for Question Answering Research},&#10;author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},&#10;year = {2019},&#10;journal = {Transactions of the Association of Computational Linguistics}&#10;}" />
</div>

# `natural_questions`


*   **Description**:

The NQ corpus contains questions from real users, and it requires QA systems to
read and comprehend an entire Wikipedia article that may or may not contain the
answer to the question. The inclusion of real user questions, and the
requirement that solutions should read an entire page to find the answer, cause
NQ to be a more realistic and challenging task than prior QA datasets.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/natural-questions">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://ai.google.com/research/NaturalQuestions/dataset](https://ai.google.com/research/NaturalQuestions/dataset)

*   **Source code**:
    [`tfds.question_answering.NaturalQuestions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/natural_questions.py)

*   **Versions**:

    *   `0.0.2`: No release notes.
    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `41.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 307,373
`'validation'` | 7,830

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{47761,
title = {Natural Questions: a Benchmark for Question Answering Research},
author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
year = {2019},
journal = {Transactions of the Association of Computational Linguistics}
}
```


## natural_questions/default (default config)

*   **Config description**: Default natural_questions config

*   **Dataset size**: `90.26 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'annotations': Sequence({
        'id': object,
        'long_answer': FeaturesDict({
            'end_byte': int64,
            'end_token': int64,
            'start_byte': int64,
            'start_token': int64,
        }),
        'short_answers': Sequence({
            'end_byte': int64,
            'end_token': int64,
            'start_byte': int64,
            'start_token': int64,
            'text': Text(shape=(), dtype=object),
        }),
        'yes_no_answer': ClassLabel(shape=(), dtype=int64, num_classes=2),
    }),
    'document': FeaturesDict({
        'html': Text(shape=(), dtype=object),
        'title': Text(shape=(), dtype=object),
        'tokens': Sequence({
            'is_html': bool,
            'token': Text(shape=(), dtype=object),
        }),
        'url': Text(shape=(), dtype=object),
    }),
    'id': object,
    'question': FeaturesDict({
        'text': Text(shape=(), dtype=object),
        'tokens': Sequence(object),
    }),
})
```

*   **Feature documentation**:

Feature                               | Class            | Shape   | Dtype  | Description
:------------------------------------ | :--------------- | :------ | :----- | :----------
                                      | FeaturesDict     |         |        |
annotations                           | Sequence         |         |        |
annotations/id                        | Tensor           |         | object |
annotations/long_answer               | FeaturesDict     |         |        |
annotations/long_answer/end_byte      | Tensor           |         | int64  |
annotations/long_answer/end_token     | Tensor           |         | int64  |
annotations/long_answer/start_byte    | Tensor           |         | int64  |
annotations/long_answer/start_token   | Tensor           |         | int64  |
annotations/short_answers             | Sequence         |         |        |
annotations/short_answers/end_byte    | Tensor           |         | int64  |
annotations/short_answers/end_token   | Tensor           |         | int64  |
annotations/short_answers/start_byte  | Tensor           |         | int64  |
annotations/short_answers/start_token | Tensor           |         | int64  |
annotations/short_answers/text        | Text             |         | object |
annotations/yes_no_answer             | ClassLabel       |         | int64  |
document                              | FeaturesDict     |         |        |
document/html                         | Text             |         | object |
document/title                        | Text             |         | object |
document/tokens                       | Sequence         |         |        |
document/tokens/is_html               | Tensor           |         | bool   |
document/tokens/token                 | Text             |         | object |
document/url                          | Text             |         | object |
id                                    | Tensor           |         | object |
question                              | FeaturesDict     |         |        |
question/text                         | Text             |         | object |
question/tokens                       | Sequence(Tensor) | (None,) | object |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/natural_questions-default-0.1.0.html";
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

## natural_questions/longt5

*   **Config description**: natural_questions preprocessed as in the longT5
    benchmark

*   **Dataset size**: `8.91 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'all_answers': Sequence(Text(shape=(), dtype=object)),
    'answer': Text(shape=(), dtype=object),
    'context': Text(shape=(), dtype=object),
    'id': Text(shape=(), dtype=object),
    'question': Text(shape=(), dtype=object),
    'title': Text(shape=(), dtype=object),
})
```

*   **Feature documentation**:

Feature     | Class          | Shape   | Dtype  | Description
:---------- | :------------- | :------ | :----- | :----------
            | FeaturesDict   |         |        |
all_answers | Sequence(Text) | (None,) | object |
answer      | Text           |         | object |
context     | Text           |         | object |
id          | Text           |         | object |
question    | Text           |         | object |
title       | Text           |         | object |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/natural_questions-longt5-0.1.0.html";
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