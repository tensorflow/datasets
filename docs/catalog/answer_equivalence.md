<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="answer_equivalence" />
  <meta itemprop="description" content="The Answer Equivalence Dataset contains human ratings on model predictions from&#10;several models on the SQuAD dataset. The ratings establish whether the predicted&#10;answer is &#x27;equivalent&#x27; to the gold answer (taking into account both question and&#10;context).&#10;&#10;More specifically, by &#x27;equivalent&#x27; we mean that the predicted answer contains at&#10;least the same information as the gold answer and does not add superfluous&#10;information. The dataset contains annotations for: * predictions from BiDAF on&#10;SQuAD dev * predictions from XLNet on SQuAD dev * predictions from Luke on SQuAD&#10;dev * predictions from Albert on SQuAD training, dev and test examples&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;answer_equivalence&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/answer_equivalence" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/answer-equivalence-dataset" />
  <meta itemprop="citation" content="@article{bulian-etal-2022-tomayto,&#10;      title={Tomayto, Tomahto. Beyond Token-level Answer Equivalence for Question Answering Evaluation},&#10;      author={Jannis Bulian and Christian Buck and Wojciech Gajewski and Benjamin Boerschinger and Tal Schuster},&#10;      year={2022},&#10;      eprint={2202.07654},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}" />
</div>

# `answer_equivalence`


*   **Description**:

The Answer Equivalence Dataset contains human ratings on model predictions from
several models on the SQuAD dataset. The ratings establish whether the predicted
answer is 'equivalent' to the gold answer (taking into account both question and
context).

More specifically, by 'equivalent' we mean that the predicted answer contains at
least the same information as the gold answer and does not add superfluous
information. The dataset contains annotations for: * predictions from BiDAF on
SQuAD dev * predictions from XLNet on SQuAD dev * predictions from Luke on SQuAD
dev * predictions from Albert on SQuAD training, dev and test examples

*   **Homepage**:
    [https://github.com/google-research-datasets/answer-equivalence-dataset](https://github.com/google-research-datasets/answer-equivalence-dataset)

*   **Source code**:
    [`tfds.datasets.answer_equivalence.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/answer_equivalence/answer_equivalence_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `45.86 MiB`

*   **Dataset size**: `47.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split         | Examples
:------------ | -------:
`'ae_dev'`    | 4,446
`'ae_test'`   | 9,724
`'dev_bidaf'` | 7,522
`'dev_luke'`  | 4,590
`'dev_xlnet'` | 7,932
`'train'`     | 9,090

*   **Feature structure**:

```python
FeaturesDict({
    'candidate': Text(shape=(), dtype=string),
    'context': Text(shape=(), dtype=string),
    'gold_index': int32,
    'qid': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
    'question_1': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'question_2': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'question_3': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'question_4': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'reference': Text(shape=(), dtype=string),
    'score': float32,
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype   | Description
:--------- | :----------- | :---- | :------ | :----------
           | FeaturesDict |       |         |
candidate  | Text         |       | string  |
context    | Text         |       | string  |
gold_index | Tensor       |       | int32   |
qid        | Text         |       | string  |
question   | Text         |       | string  |
question_1 | ClassLabel   |       | int64   |
question_2 | ClassLabel   |       | int64   |
question_3 | ClassLabel   |       | int64   |
question_4 | ClassLabel   |       | int64   |
reference  | Text         |       | string  |
score      | Tensor       |       | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/answer_equivalence-1.0.0.html";
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
@article{bulian-etal-2022-tomayto,
      title={Tomayto, Tomahto. Beyond Token-level Answer Equivalence for Question Answering Evaluation},
      author={Jannis Bulian and Christian Buck and Wojciech Gajewski and Benjamin Boerschinger and Tal Schuster},
      year={2022},
      eprint={2202.07654},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

