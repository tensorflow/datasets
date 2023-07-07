<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gsm8k" />
  <meta itemprop="description" content="A dataset of 8.5K high quality linguistically diverse grade school math word problems.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gsm8k&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gsm8k" />
  <meta itemprop="sameAs" content="https://github.com/openai/grade-school-math" />
  <meta itemprop="citation" content="@misc{cobbe2021training,&#10;      title={Training Verifiers to Solve Math Word Problems},&#10;      author={Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},&#10;      year={2021},&#10;      eprint={2110.14168},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.LG}&#10;}" />
</div>

# `gsm8k`


*   **Description**:

A dataset of 8.5K high quality linguistically diverse grade school math word
problems.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/gsm8k">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/openai/grade-school-math](https://github.com/openai/grade-school-math)

*   **Source code**:
    [`tfds.text.gsm8k.Gsm8k`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/gsm8k/gsm8k.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `10.77 MiB`

*   **Dataset size**: `17.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split              | Examples
:----------------- | -------:
`'test'`           | 1,319
`'test_socratic'`  | 1,319
`'train'`          | 7,473
`'train_socratic'` | 7,473

*   **Feature structure**:

```python
FeaturesDict({
    'annotation': Text(shape=(), dtype=string),
    'answer': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
    'short_answer': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature      | Class        | Shape | Dtype  | Description
:----------- | :----------- | :---- | :----- | :----------
             | FeaturesDict |       |        |
annotation   | Text         |       | string |
answer       | Text         |       | string |
question     | Text         |       | string |
short_answer | Text         |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gsm8k-1.0.0.html";
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
@misc{cobbe2021training,
      title={Training Verifiers to Solve Math Word Problems},
      author={Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
      year={2021},
      eprint={2110.14168},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

