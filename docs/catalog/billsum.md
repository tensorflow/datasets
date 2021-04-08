<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="billsum" />
  <meta itemprop="description" content="BillSum, summarization of US Congressional and California state bills.&#10;&#10;There are several features:&#10;  - text: bill text.&#10;  - summary: summary of the bills.&#10;  - title: title of the bills.&#10;features for us bills. ca bills does not have.&#10;  - text_len: number of chars in text.&#10;  - sum_len: number of chars in summary.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;billsum&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/billsum" />
  <meta itemprop="sameAs" content="https://github.com/FiscalNote/BillSum" />
  <meta itemprop="citation" content="@misc{kornilova2019billsum,&#10;    title={BillSum: A Corpus for Automatic Summarization of US Legislation},&#10;    author={Anastassia Kornilova and Vlad Eidelman},&#10;    year={2019},&#10;    eprint={1910.00523},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `billsum`

*   **Description**:

BillSum, summarization of US Congressional and California state bills.

There are several features: - text: bill text. - summary: summary of the
bills. - title: title of the bills. features for us bills. ca bills does not
have. - text_len: number of chars in text. - sum_len: number of chars in
summary.

*   **Homepage**:
    [https://github.com/FiscalNote/BillSum](https://github.com/FiscalNote/BillSum)

*   **Source code**:
    [`tfds.summarization.Billsum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/billsum.py)

*   **Versions**:

    *   **`3.0.0`** (default): No release notes.

*   **Download size**: `64.14 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split       | Examples
:---------- | -------:
`'ca_test'` | 1,237
`'test'`    | 3,269
`'train'`   | 18,949

*   **Features**:

```python
FeaturesDict({
    'summary': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'summary')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/billsum-3.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@misc{kornilova2019billsum,
    title={BillSum: A Corpus for Automatic Summarization of US Legislation},
    author={Anastassia Kornilova and Vlad Eidelman},
    year={2019},
    eprint={1910.00523},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
