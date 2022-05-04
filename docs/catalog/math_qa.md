<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="math_qa" />
  <meta itemprop="description" content="A large-scale dataset of math word problems and an interpretable neural math problem solver that learns to map problems to operation programs.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;math_qa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/math_qa" />
  <meta itemprop="sameAs" content="https://math-qa.github.io/" />
  <meta itemprop="citation" content="@misc{amini2019mathqa,&#10;      title={MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms},&#10;      author={Aida Amini and Saadia Gabriel and Peter Lin and Rik Koncel-Kedziorski and Yejin Choi and Hannaneh Hajishirzi},&#10;      year={2019},&#10;      eprint={1905.13319},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}" />
</div>

# `math_qa`


*   **Description**:

A large-scale dataset of math word problems and an interpretable neural math
problem solver that learns to map problems to operation programs.

*   **Homepage**: [https://math-qa.github.io/](https://math-qa.github.io/)

*   **Source code**:
    [`tfds.text.math_qa.MathQa`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/math_qa/math_qa.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `6.96 MiB`

*   **Dataset size**: `27.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,985
`'train'`      | 29,837
`'validation'` | 4,475

*   **Feature structure**:

```python
FeaturesDict({
    'Problem': Text(shape=(), dtype=tf.string),
    'Rationale': Text(shape=(), dtype=tf.string),
    'annotated_formula': Text(shape=(), dtype=tf.string),
    'category': Text(shape=(), dtype=tf.string),
    'correct': Text(shape=(), dtype=tf.string),
    'correct_option': Text(shape=(), dtype=tf.string),
    'linear_formula': Text(shape=(), dtype=tf.string),
    'options': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype     | Description
:---------------- | :----------- | :---- | :-------- | :----------
                  | FeaturesDict |       |           |
Problem           | Text         |       | tf.string |
Rationale         | Text         |       | tf.string |
annotated_formula | Text         |       | tf.string |
category          | Text         |       | tf.string |
correct           | Text         |       | tf.string |
correct_option    | Text         |       | tf.string |
linear_formula    | Text         |       | tf.string |
options           | Text         |       | tf.string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/math_qa-1.0.0.html";
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
@misc{amini2019mathqa,
      title={MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms},
      author={Aida Amini and Saadia Gabriel and Peter Lin and Rik Koncel-Kedziorski and Yejin Choi and Hannaneh Hajishirzi},
      year={2019},
      eprint={1905.13319},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

