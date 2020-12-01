<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="hellaswag" />
  <meta itemprop="description" content="The HellaSwag dataset is a benchmark for Commonsense NLI. It includes a context&#10;and some endings which complete the context.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;hellaswag&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/hellaswag" />
  <meta itemprop="sameAs" content="https://rowanzellers.com/hellaswag/" />
  <meta itemprop="citation" content="@inproceedings{zellers2019hellaswag,&#10;    title={HellaSwag: Can a Machine Really Finish Your Sentence?},&#10;    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},&#10;    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},&#10;    year={2019}&#10;}" />
</div>

# `hellaswag`

*   **Description**:

The HellaSwag dataset is a benchmark for Commonsense NLI. It includes a context
and some endings which complete the context.

*   **Homepage**:
    [https://rowanzellers.com/hellaswag/](https://rowanzellers.com/hellaswag/)

*   **Source code**:
    [`tfds.text.Hellaswag`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/hellaswag.py)

*   **Versions**:

    *   **`0.0.1`** (default): No release notes.

*   **Download size**: `68.18 MiB`

*   **Dataset size**: `51.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,003
`'train'`      | 39,905
`'validation'` | 10,042

*   **Features**:

```python
FeaturesDict({
    'activity_label': Text(shape=(), dtype=tf.string),
    'context': Text(shape=(), dtype=tf.string),
    'endings': Sequence(Text(shape=(), dtype=tf.string)),
    'label': tf.int32,
    'split_type': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
```

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/hellaswag-0.0.1.html";
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