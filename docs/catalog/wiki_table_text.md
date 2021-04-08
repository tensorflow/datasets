<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wiki_table_text" />
  <meta itemprop="description" content="Wikipedia tables with at least 3 rows and 2 columns, 3 random rows for each&#10;table were selected for further annotation. Each row was annotated by a&#10;different person, so the dataset is composed by (one row table, text&#10;description) pairs. Annotations include at least 2 cells of the row, but do not&#10;require to include them all.&#10;The dataset follows a standarized table format.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wiki_table_text&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wiki_table_text" />
  <meta itemprop="sameAs" content="https://github.com/msra-nlc/Table2Text" />
  <meta itemprop="citation" content="@inproceedings{bao2018table,&#10;  title={Table-to-Text: Describing Table Region with Natural Language},&#10;  author={Junwei Bao and Duyu Tang and Nan Duan and Zhao Yan and Yuanhua Lv and Ming Zhou and Tiejun Zhao},&#10;  booktitle={AAAI},&#10;  url={https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/download/16138/16782},&#10;  year={2018}&#10;}" />
</div>

# `wiki_table_text`

*   **Description**:

Wikipedia tables with at least 3 rows and 2 columns, 3 random rows for each
table were selected for further annotation. Each row was annotated by a
different person, so the dataset is composed by (one row table, text
description) pairs. Annotations include at least 2 cells of the row, but do not
require to include them all. The dataset follows a standarized table format.

*   **Homepage**:
    [https://github.com/msra-nlc/Table2Text](https://github.com/msra-nlc/Table2Text)

*   **Source code**:
    [`tfds.structured.wiki_table_text.WikiTableText`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/wiki_table_text/wiki_table_text.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.70 MiB`

*   **Dataset size**: `4.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 10,000
`'validation'` | 1,318

*   **Features**:

```python
FeaturesDict({
    'input_text': FeaturesDict({
        'table': Sequence({
            'column_header': tf.string,
            'content': tf.string,
            'row_number': tf.int16,
        }),
    }),
    'target_text': tf.string,
})
```

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
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_table_text-1.0.0.html";
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
@inproceedings{bao2018table,
  title={Table-to-Text: Describing Table Region with Natural Language},
  author={Junwei Bao and Duyu Tang and Nan Duan and Zhao Yan and Yuanhua Lv and Ming Zhou and Tiejun Zhao},
  booktitle={AAAI},
  url={https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/download/16138/16782},
  year={2018}
}
```
