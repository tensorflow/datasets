<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="openbookqa" />
  <meta itemprop="description" content="The dataset contains 5,957 4-way multiple choice questions. Additionally, they&#10;provide 5,167 crowd-sourced common knowledge facts, and an expanded version of&#10;the train/dev/test questions where each question is associated with its&#10;originating core fact, a human accuracy score, a clarity score, and an&#10;anonymized crowd-worker ID.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;openbookqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/openbookqa" />
  <meta itemprop="sameAs" content="https://leaderboard.allenai.org/open_book_qa/submissions/get-started" />
  <meta itemprop="citation" content="@article{mihaylov2018can,&#10;  title={Can a suit of armor conduct electricity? a new dataset for open book question answering},&#10;  author={Mihaylov, Todor and Clark, Peter and Khot, Tushar and Sabharwal, Ashish},&#10;  journal={arXiv preprint arXiv:1809.02789},&#10;  year={2018}&#10;}" />
</div>

# `openbookqa`


*   **Description**:

The dataset contains 5,957 4-way multiple choice questions. Additionally, they
provide 5,167 crowd-sourced common knowledge facts, and an expanded version of
the train/dev/test questions where each question is associated with its
originating core fact, a human accuracy score, a clarity score, and an
anonymized crowd-worker ID.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/openbookqa">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://leaderboard.allenai.org/open_book_qa/submissions/get-started](https://leaderboard.allenai.org/open_book_qa/submissions/get-started)

*   **Source code**:
    [`tfds.datasets.openbookqa.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/openbookqa/openbookqa_dataset_builder.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `1.38 MiB`

*   **Dataset size**: `2.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 4,957
`'validation'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'answerKey': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'clarity': float32,
    'fact1': Text(shape=(), dtype=string),
    'humanScore': float32,
    'question': FeaturesDict({
        'choice_A': Text(shape=(), dtype=string),
        'choice_B': Text(shape=(), dtype=string),
        'choice_C': Text(shape=(), dtype=string),
        'choice_D': Text(shape=(), dtype=string),
        'stem': Text(shape=(), dtype=string),
    }),
    'turkIdAnonymized': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
answerKey         | ClassLabel   |       | int64   |
clarity           | Tensor       |       | float32 |
fact1             | Text         |       | string  |
humanScore        | Tensor       |       | float32 |
question          | FeaturesDict |       |         |
question/choice_A | Text         |       | string  |
question/choice_B | Text         |       | string  |
question/choice_C | Text         |       | string  |
question/choice_D | Text         |       | string  |
question/stem     | Text         |       | string  |
turkIdAnonymized  | Text         |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('question', 'answerKey')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/openbookqa-0.1.0.html";
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
@article{mihaylov2018can,
  title={Can a suit of armor conduct electricity? a new dataset for open book question answering},
  author={Mihaylov, Todor and Clark, Peter and Khot, Tushar and Sabharwal, Ashish},
  journal={arXiv preprint arXiv:1809.02789},
  year={2018}
}
```

