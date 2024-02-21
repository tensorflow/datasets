<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="e2e_cleaned" />
  <meta itemprop="description" content="An update release of E2E NLG Challenge data with cleaned MRs. The E2E data&#10;contains dialogue act-based meaning representation (MR) in the restaurant domain&#10;and up to 5 references in natural language, which is what one needs to predict.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;e2e_cleaned&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/e2e_cleaned" />
  <meta itemprop="sameAs" content="https://github.com/tuetschek/e2e-cleaning" />
  <meta itemprop="citation" content="@inproceedings{dusek-etal-2019-semantic,&#10;    title = &quot;Semantic Noise Matters for Neural Natural Language Generation&quot;,&#10;    author = &quot;Du{\v{s}}ek, Ond{\v{r}}ej  and&#10;      Howcroft, David M.  and&#10;      Rieser, Verena&quot;,&#10;    booktitle = &quot;Proceedings of the 12th International Conference on Natural Language Generation&quot;,&#10;    month = oct # &quot;{--}&quot; # nov,&#10;    year = &quot;2019&quot;,&#10;    address = &quot;Tokyo, Japan&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/W19-8652&quot;,&#10;    doi = &quot;10.18653/v1/W19-8652&quot;,&#10;    pages = &quot;421--426&quot;,&#10;    abstract = &quot;Neural natural language generation (NNLG) systems are known for their pathological outputs, i.e. generating text which is unrelated to the input specification. In this paper, we show the impact of semantic noise on state-of-the-art NNLG models which implement different semantic control mechanisms. We find that cleaned data can improve semantic correctness by up to 97{\%}, while maintaining fluency. We also find that the most common error is omitting information, rather than hallucination.&quot;,&#10;}" />
</div>

# `e2e_cleaned`


*   **Description**:

An update release of E2E NLG Challenge data with cleaned MRs. The E2E data
contains dialogue act-based meaning representation (MR) in the restaurant domain
and up to 5 references in natural language, which is what one needs to predict.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/e2e">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/tuetschek/e2e-cleaning](https://github.com/tuetschek/e2e-cleaning)

*   **Source code**:
    [`tfds.datasets.e2e_cleaned.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/e2e_cleaned/e2e_cleaned_dataset_builder.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `13.92 MiB`

*   **Dataset size**: `14.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,693
`'train'`      | 33,525
`'validation'` | 4,299

*   **Feature structure**:

```python
FeaturesDict({
    'input_text': FeaturesDict({
        'table': Sequence({
            'column_header': string,
            'content': string,
            'row_number': int16,
        }),
    }),
    'target_text': string,
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype  | Description
:----------------------------- | :----------- | :---- | :----- | :----------
                               | FeaturesDict |       |        |
input_text                     | FeaturesDict |       |        |
input_text/table               | Sequence     |       |        |
input_text/table/column_header | Tensor       |       | string |
input_text/table/content       | Tensor       |       | string |
input_text/table/row_number    | Tensor       |       | int16  |
target_text                    | Tensor       |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('input_text', 'target_text')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/e2e_cleaned-0.1.0.html";
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
@inproceedings{dusek-etal-2019-semantic,
    title = "Semantic Noise Matters for Neural Natural Language Generation",
    author = "Du{\v{s}}ek, Ond{\v{r}}ej  and
      Howcroft, David M.  and
      Rieser, Verena",
    booktitle = "Proceedings of the 12th International Conference on Natural Language Generation",
    month = oct # "{--}" # nov,
    year = "2019",
    address = "Tokyo, Japan",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-8652",
    doi = "10.18653/v1/W19-8652",
    pages = "421--426",
    abstract = "Neural natural language generation (NNLG) systems are known for their pathological outputs, i.e. generating text which is unrelated to the input specification. In this paper, we show the impact of semantic noise on state-of-the-art NNLG models which implement different semantic control mechanisms. We find that cleaned data can improve semantic correctness by up to 97{\%}, while maintaining fluency. We also find that the most common error is omitting information, rather than hallucination.",
}
```

