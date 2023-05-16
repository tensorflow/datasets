<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="quac" />
  <meta itemprop="description" content="Question Answering in Context is a dataset for modeling, understanding, and&#10;participating in information seeking dialog. Data instances consist of an&#10;interactive dialog between two crowd workers: (1) a student who poses a sequence&#10;of freeform questions to learn as much as possible about a hidden Wikipedia&#10;text, and (2) a teacher who answers the questions by providing short excerpts&#10;(spans) from the text. QuAC introduces challenges not found in existing machine&#10;comprehension datasets: its questions are often more open-ended, unanswerable,&#10;or only meaningful within the dialog context.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;quac&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/quac" />
  <meta itemprop="sameAs" content="https://quac.ai/" />
  <meta itemprop="citation" content="@article{choi2018quac,&#10;  title={Quac: Question answering in context},&#10;  author={Choi, Eunsol and He, He and Iyyer, Mohit and Yatskar, Mark and Yih, Wen-tau and Choi, Yejin and Liang, Percy and Zettlemoyer, Luke},&#10;  journal={arXiv preprint arXiv:1808.07036},&#10;  year={2018}&#10;}" />
</div>

# `quac`


*   **Description**:

Question Answering in Context is a dataset for modeling, understanding, and
participating in information seeking dialog. Data instances consist of an
interactive dialog between two crowd workers: (1) a student who poses a sequence
of freeform questions to learn as much as possible about a hidden Wikipedia
text, and (2) a teacher who answers the questions by providing short excerpts
(spans) from the text. QuAC introduces challenges not found in existing machine
comprehension datasets: its questions are often more open-ended, unanswerable,
or only meaningful within the dialog context.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/quac">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://quac.ai/](https://quac.ai/)

*   **Source code**:
    [`tfds.datasets.quac.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/quac/quac_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `73.47 MiB`

*   **Dataset size**: `298.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 83,568
`'validation'` | 7,354

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': int32,
        'text': Text(shape=(), dtype=string),
    }),
    'background': Text(shape=(), dtype=string),
    'context': Text(shape=(), dtype=string),
    'followup': Text(shape=(), dtype=string),
    'orig_answer': FeaturesDict({
        'answer_start': int32,
        'text': Text(shape=(), dtype=string),
    }),
    'question': Text(shape=(), dtype=string),
    'section_title': Text(shape=(), dtype=string),
    'title': Text(shape=(), dtype=string),
    'yesno': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                  | Class        | Shape | Dtype  | Description
:----------------------- | :----------- | :---- | :----- | :----------
                         | FeaturesDict |       |        |
answers                  | Sequence     |       |        |
answers/answer_start     | Tensor       |       | int32  |
answers/text             | Text         |       | string |
background               | Text         |       | string |
context                  | Text         |       | string |
followup                 | Text         |       | string |
orig_answer              | FeaturesDict |       |        |
orig_answer/answer_start | Tensor       |       | int32  |
orig_answer/text         | Text         |       | string |
question                 | Text         |       | string |
section_title            | Text         |       | string |
title                    | Text         |       | string |
yesno                    | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('context', 'answers')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/quac-1.0.0.html";
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
@article{choi2018quac,
  title={Quac: Question answering in context},
  author={Choi, Eunsol and He, He and Iyyer, Mohit and Yatskar, Mark and Yih, Wen-tau and Choi, Yejin and Liang, Percy and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:1808.07036},
  year={2018}
}
```

