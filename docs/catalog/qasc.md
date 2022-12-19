<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="qasc" />
  <meta itemprop="description" content="QASC is a question-answering dataset with a focus on sentence composition. It&#10;consists of 9,980 8-way multiple-choice questions about grade school science&#10;(8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;qasc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/qasc" />
  <meta itemprop="sameAs" content="https://allenai.org/data/qasc" />
  <meta itemprop="citation" content="@article{allenai:qasc,&#10;      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},&#10;      title     = {QASC: A Dataset for Question Answering via Sentence Composition},&#10;      journal   = {arXiv:1910.11473v2},&#10;      year      = {2020},&#10;}" />
</div>

# `qasc`


*   **Description**:

QASC is a question-answering dataset with a focus on sentence composition. It
consists of 9,980 8-way multiple-choice questions about grade school science
(8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/qasc">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://allenai.org/data/qasc](https://allenai.org/data/qasc)

*   **Source code**:
    [`tfds.datasets.qasc.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/qasc/qasc_dataset_builder.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `1.54 MiB`

*   **Dataset size**: `6.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Feature structure**:

```python
FeaturesDict({
    'answerKey': Text(shape=(), dtype=string),
    'choices': Sequence({
        'label': Text(shape=(), dtype=string),
        'text': Text(shape=(), dtype=string),
    }),
    'combinedfact': Text(shape=(), dtype=string),
    'fact1': Text(shape=(), dtype=string),
    'fact2': Text(shape=(), dtype=string),
    'formatted_question': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape | Dtype  | Description
:----------------- | :----------- | :---- | :----- | :----------
                   | FeaturesDict |       |        |
answerKey          | Text         |       | string |
choices            | Sequence     |       |        |
choices/label      | Text         |       | string |
choices/text       | Text         |       | string |
combinedfact       | Text         |       | string |
fact1              | Text         |       | string |
fact2              | Text         |       | string |
formatted_question | Text         |       | string |
id                 | Text         |       | string |
question           | Text         |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/qasc-0.1.0.html";
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
@article{allenai:qasc,
      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},
      title     = {QASC: A Dataset for Question Answering via Sentence Composition},
      journal   = {arXiv:1910.11473v2},
      year      = {2020},
}
```

