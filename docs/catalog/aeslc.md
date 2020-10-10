<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="aeslc" />
  <meta itemprop="description" content="A collection of email messages of employees in the Enron Corporation.&#10;&#10;There are two features:&#10;  - email_body: email body text.&#10;  - subject_line: email subject text.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;aeslc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/aeslc" />
  <meta itemprop="sameAs" content="https://github.com/ryanzhumich/AESLC" />
  <meta itemprop="citation" content="@misc{zhang2019email,&#10;    title={This Email Could Save Your Life: Introducing the Task of Email Subject Line Generation},&#10;    author={Rui Zhang and Joel Tetreault},&#10;    year={2019},&#10;    eprint={1906.03497},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>
# `aeslc`

*   **Description**:

A collection of email messages of employees in the Enron Corporation.

There are two features:
  - email_body: email body text.
  - subject_line: email subject text.

*   **Homepage**: [https://github.com/ryanzhumich/AESLC](https://github.com/ryanzhumich/AESLC)

*   **Source code**: [`tfds.summarization.Aeslc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/aeslc.py)

*   **Versions**:

    * **`1.0.0`** (default): No release notes.

*   **Download size**: `11.10 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached** ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)): Unknown

*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1,906
`'train'` | 14,436
`'validation'` | 1,960

*   **Features**:

```python
FeaturesDict({
    'email_body': Text(shape=(), dtype=tf.string),
    'subject_line': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)): `('email_body', 'subject_line')`

*   **Citation**:

```
@misc{zhang2019email,
    title={This Email Could Save Your Life: Introducing the Task of Email Subject Line Generation},
    author={Rui Zhang and Joel Tetreault},
    year={2019},
    eprint={1906.03497},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

*   **Figure** ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)): Not supported.

*   **Examples** ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>

<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>

<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/aeslc-1.0.0.html";
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
