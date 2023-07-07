<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cs_restaurants" />
  <meta itemprop="description" content="Czech data-to-text dataset in the restaurant domain. The input meaning representations&#10;contain a dialogue act type (inform, confirm etc.), slots (food, area, etc.) and their values.&#10;It originated as a translation of the English San Francisco Restaurants dataset by Wen et al. (2015).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cs_restaurants&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cs_restaurants" />
  <meta itemprop="sameAs" content="https://github.com/UFAL-DSG/cs_restaurant_dataset" />
  <meta itemprop="citation" content="@inproceedings{dusek_neural_2019,&#10;        author = {Dušek, Ondřej and Jurčíček, Filip},&#10;        title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},&#10;        shorttitle = {Neural {Generation} for {Czech}},&#10;        url = {https://www.aclweb.org/anthology/W19-8670/},&#10;        urldate = {2019-10-18},&#10;        booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},&#10;        month = oct,&#10;        address = {Tokyo, Japan},&#10;        year = {2019},&#10;        pages = {563--574},&#10;        abstract = {We present the first dataset targeted at end-to-end NLG in Czech in the restaurant domain, along with several strong baseline models using the sequence-to-sequence approach. While non-English NLG is under-explored in general, Czech, as a morphologically rich language, makes the task even harder: Since Czech requires inflecting named entities, delexicalization or copy mechanisms do not work out-of-the-box and lexicalizing the generated outputs is non-trivial. In our experiments, we present two different approaches to this this problem: (1) using a neural language model to select the correct inflected form while lexicalizing, (2) a two-step generation setup: our sequence-to-sequence model generates an interleaved sequence of lemmas and morphological tags, which are then inflected by a morphological generator.},&#10;}" />
</div>

# `cs_restaurants`


*   **Description**:

Czech data-to-text dataset in the restaurant domain. The input meaning
representations contain a dialogue act type (inform, confirm etc.), slots (food,
area, etc.) and their values. It originated as a translation of the English San
Francisco Restaurants dataset by Wen et al. (2015).

*   **Homepage**:
    [https://github.com/UFAL-DSG/cs_restaurant_dataset](https://github.com/UFAL-DSG/cs_restaurant_dataset)

*   **Source code**:
    [`tfds.structured.cs_restaurants.CSRestaurants`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/cs_restaurants/cs_restaurants.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `2.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 842
`'train'`      | 3,569
`'validation'` | 781

*   **Feature structure**:

```python
FeaturesDict({
    'delex_input_text': FeaturesDict({
        'table': Sequence({
            'column_header': string,
            'content': string,
            'row_number': int16,
        }),
    }),
    'delex_target_text': string,
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

Feature                              | Class        | Shape | Dtype  | Description
:----------------------------------- | :----------- | :---- | :----- | :----------
                                     | FeaturesDict |       |        |
delex_input_text                     | FeaturesDict |       |        |
delex_input_text/table               | Sequence     |       |        |
delex_input_text/table/column_header | Tensor       |       | string |
delex_input_text/table/content       | Tensor       |       | string |
delex_input_text/table/row_number    | Tensor       |       | int16  |
delex_target_text                    | Tensor       |       | string |
input_text                           | FeaturesDict |       |        |
input_text/table                     | Sequence     |       |        |
input_text/table/column_header       | Tensor       |       | string |
input_text/table/content             | Tensor       |       | string |
input_text/table/row_number          | Tensor       |       | int16  |
target_text                          | Tensor       |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cs_restaurants-1.0.0.html";
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
@inproceedings{dusek_neural_2019,
        author = {Dušek, Ondřej and Jurčíček, Filip},
        title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},
        shorttitle = {Neural {Generation} for {Czech}},
        url = {https://www.aclweb.org/anthology/W19-8670/},
        urldate = {2019-10-18},
        booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
        month = oct,
        address = {Tokyo, Japan},
        year = {2019},
        pages = {563--574},
        abstract = {We present the first dataset targeted at end-to-end NLG in Czech in the restaurant domain, along with several strong baseline models using the sequence-to-sequence approach. While non-English NLG is under-explored in general, Czech, as a morphologically rich language, makes the task even harder: Since Czech requires inflecting named entities, delexicalization or copy mechanisms do not work out-of-the-box and lexicalizing the generated outputs is non-trivial. In our experiments, we present two different approaches to this this problem: (1) using a neural language model to select the correct inflected form while lexicalizing, (2) a two-step generation setup: our sequence-to-sequence model generates an interleaved sequence of lemmas and morphological tags, which are then inflected by a morphological generator.},
}
```

