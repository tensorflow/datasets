<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="corr2cause" />
  <meta itemprop="description" content="# Corr2cause&#10;&#10;Causal inference is one of the hallmarks of human intelligence.&#10;&#10;Corr2cause is a large-scale dataset of more than 400K samples, on which&#10;seventeen existing LLMs are evaluated in the related paper.&#10;&#10;Overall, Corr2cause contains 415,944 samples, with 18.57% in valid samples.&#10;The average length of the premise is 424.11 tokens, and hypothesis 10.83 tokens.&#10;The data is split into 411,452 training samples, 2,246 development and test&#10;samples, respectively. Since the main purpose of the dataset is to benchmark the&#10;performance of LLMs, the test and development sets have been prioritized to have&#10;a comprehensive coverage over all sizes of graphs.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;corr2cause&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/corr2cause" />
  <meta itemprop="sameAs" content="https://github.com/causalNLP/corr2cause/tree/main" />
  <meta itemprop="citation" content="@misc{jin2023large,&#10;      title={Can Large Language Models Infer Causation from Correlation?}, &#10;      author={Zhijing Jin and Jiarui Liu and Zhiheng Lyu and Spencer Poff and Mrinmaya Sachan and Rada Mihalcea and Mona Diab and Bernhard Schölkopf},&#10;      year={2023},&#10;      eprint={2306.05836},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}" />
</div>

# `corr2cause`


*   **Description**:

# Corr2cause

Causal inference is one of the hallmarks of human intelligence.

Corr2cause is a large-scale dataset of more than 400K samples, on which
seventeen existing LLMs are evaluated in the related paper.

Overall, Corr2cause contains 415,944 samples, with 18.57% in valid samples. The
average length of the premise is 424.11 tokens, and hypothesis 10.83 tokens. The
data is split into 411,452 training samples, 2,246 development and test samples,
respectively. Since the main purpose of the dataset is to benchmark the
performance of LLMs, the test and development sets have been prioritized to have
a comprehensive coverage over all sizes of graphs.

*   **Homepage**:
    [https://github.com/causalNLP/corr2cause/tree/main](https://github.com/causalNLP/corr2cause/tree/main)

*   **Source code**:
    [`tfds.datasets.corr2cause.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/corr2cause/corr2cause_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `727.22 MiB`

*   **Dataset size**: `739.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,246
`'test'`  | 2,246
`'train'` | 411,452

*   **Feature structure**:

```python
FeaturesDict({
    'input': Text(shape=(), dtype=string),
    'label': int64,
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype  | Description
:------ | :----------- | :---- | :----- | :----------
        | FeaturesDict |       |        |
input   | Text         |       | string |
label   | Tensor       |       | int64  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/corr2cause-1.0.0.html";
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
@misc{jin2023large,
      title={Can Large Language Models Infer Causation from Correlation?},
      author={Zhijing Jin and Jiarui Liu and Zhiheng Lyu and Spencer Poff and Mrinmaya Sachan and Rada Mihalcea and Mona Diab and Bernhard Schölkopf},
      year={2023},
      eprint={2306.05836},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

