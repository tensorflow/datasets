<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="race" />
  <meta itemprop="description" content="Race is a large-scale reading comprehension dataset with more than 28,000&#10;passages and nearly 100,000 questions. The dataset is collected from English&#10;examinations in China, which are designed for middle school and high school&#10;students. The dataset can be served as the training and test sets for machine&#10;comprehension.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;race&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/race" />
  <meta itemprop="sameAs" content="https://www.cs.cmu.edu/~glai1/data/race/" />
  <meta itemprop="citation" content="@article{lai2017large,&#10;    title={RACE: Large-scale ReAding Comprehension Dataset From Examinations},&#10;    author={Lai, Guokun and Xie, Qizhe and Liu, Hanxiao and Yang, Yiming and Hovy, Eduard},&#10;    journal={arXiv preprint arXiv:1704.04683},&#10;    year={2017}&#10;}" />
</div>

# `race`


*   **Description**:

Race is a large-scale reading comprehension dataset with more than 28,000
passages and nearly 100,000 questions. The dataset is collected from English
examinations in China, which are designed for middle school and high school
students. The dataset can be served as the training and test sets for machine
comprehension.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/race">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Config description**: Builder config for RACE dataset.

*   **Homepage**:
    [https://www.cs.cmu.edu/~glai1/data/race/](https://www.cs.cmu.edu/~glai1/data/race/)

*   **Source code**:
    [`tfds.datasets.race.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/race/race_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`2.0.0`** (default): Add the example id.

*   **Download size**: `24.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence(Text(shape=(), dtype=string)),
    'article': Text(shape=(), dtype=string),
    'example_id': Text(shape=(), dtype=string),
    'options': Sequence(Sequence(Text(shape=(), dtype=string))),
    'questions': Sequence(Text(shape=(), dtype=string)),
})
```

*   **Feature documentation**:

Feature    | Class                    | Shape        | Dtype  | Description
:--------- | :----------------------- | :----------- | :----- | :----------
           | FeaturesDict             |              |        |
answers    | Sequence(Text)           | (None,)      | string |
article    | Text                     |              | string |
example_id | Text                     |              | string |
options    | Sequence(Sequence(Text)) | (None, None) | string |
questions  | Sequence(Text)           | (None,)      | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{lai2017large,
    title={RACE: Large-scale ReAding Comprehension Dataset From Examinations},
    author={Lai, Guokun and Xie, Qizhe and Liu, Hanxiao and Yang, Yiming and Hovy, Eduard},
    journal={arXiv preprint arXiv:1704.04683},
    year={2017}
}
```


## race/high (default config)

*   **Dataset size**: `52.39 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,021
`'test'`  | 1,045
`'train'` | 18,728

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/race-high-2.0.0.html";
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

## race/middle

*   **Dataset size**: `12.51 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 368
`'test'`  | 362
`'train'` | 6,409

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/race-middle-2.0.0.html";
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