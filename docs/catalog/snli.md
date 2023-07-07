<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="snli" />
  <meta itemprop="description" content="The SNLI corpus (version 1.0) is a collection of 570k human-written English&#10;sentence pairs manually labeled for balanced classification with the labels&#10;entailment, contradiction, and neutral, supporting the task of natural language&#10;inference (NLI), also known as recognizing textual entailment (RTE).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;snli&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/snli" />
  <meta itemprop="sameAs" content="https://nlp.stanford.edu/projects/snli/" />
  <meta itemprop="citation" content="@inproceedings{snli:emnlp2015,&#10;    Author = {Bowman, Samuel R. and Angeli, Gabor and Potts, Christopher, and Manning, Christopher D.},&#10;    Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},&#10;  Publisher = {Association for Computational Linguistics},&#10;   Title = {A large annotated corpus for learning natural language inference},&#10;    Year = {2015}&#10;}" />
</div>

# `snli`


*   **Description**:

The SNLI corpus (version 1.0) is a collection of 570k human-written English
sentence pairs manually labeled for balanced classification with the labels
entailment, contradiction, and neutral, supporting the task of natural language
inference (NLI), also known as recognizing textual entailment (RTE).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/snli">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://nlp.stanford.edu/projects/snli/](https://nlp.stanford.edu/projects/snli/)

*   **Source code**:
    [`tfds.datasets.snli.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/snli/snli_dataset_builder.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Download size**: `90.17 MiB`

*   **Dataset size**: `87.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 550,152
`'validation'` | 10,000

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'premise': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype  | Description
:--------- | :----------- | :---- | :----- | :----------
           | FeaturesDict |       |        |
hypothesis | Text         |       | string |
label      | ClassLabel   |       | int64  |
premise    | Text         |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/snli-1.1.0.html";
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
@inproceedings{snli:emnlp2015,
    Author = {Bowman, Samuel R. and Angeli, Gabor and Potts, Christopher, and Manning, Christopher D.},
    Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    Publisher = {Association for Computational Linguistics},
    Title = {A large annotated corpus for learning natural language inference},
    Year = {2015}
}
```

