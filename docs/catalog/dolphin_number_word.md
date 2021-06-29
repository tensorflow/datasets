<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dolphin_number_word" />
  <meta itemprop="description" content="Dolphin Math Word Problem dataset (2015), as presented in https://www.microsoft.com/en-us/research/uploads/prod/2016/02//dolphin-sigmadolphin.datasets.pdf&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dolphin_number_word&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dolphin_number_word" />
  <meta itemprop="sameAs" content="https://www.microsoft.com/en-us/research/project/sigmadolphin-2/" />
  <meta itemprop="citation" content="@inproceedings{inproceedings,&#10;author = {Shi, Shuming and Wang, Yuehui and Lin, Chin-Yew and Liu, Xiaojiang and Rui, Yong},&#10;year = {2015},&#10;month = {09},&#10;pages = {},&#10;title = {Automatically Solving Number Word Problems by Semantic Parsing and Reasoning},&#10;doi = {10.18653/v1/D15-1135}&#10;}" />
</div>

# `dolphin_number_word`


*   **Description**:

Dolphin Math Word Problem dataset (2015), as presented in
https://www.microsoft.com/en-us/research/uploads/prod/2016/02//dolphin-sigmadolphin.datasets.pdf

*   **Homepage**:
    [https://www.microsoft.com/en-us/research/project/sigmadolphin-2/](https://www.microsoft.com/en-us/research/project/sigmadolphin-2/)

*   **Source code**:
    [`tfds.text.dolphin_number_word.DolphinNumberWord`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/dolphin_number_word/dolphin_number_word.py)

*   **Versions**:

    *   `0.0.1`: Initial release.
    *   **`0.0.2`** (default): RaggedTensor fix. Equations and Sources
        represented as a singlestring with components delimited by spaces
    *   `0.0.3`: Reintroduced logic to handle edge-case involving examples
        without sources.

*   **Download size**: `280.42 KiB`

*   **Dataset size**: `1.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 3,507
`'train'` | 864

*   **Features**:

```python
FeaturesDict({
    'ans': Text(shape=(), dtype=tf.string),
    'equations': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'index': tf.int32,
    'sources': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'ans')`

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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dolphin_number_word-0.0.2.html";
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
@inproceedings{inproceedings,
author = {Shi, Shuming and Wang, Yuehui and Lin, Chin-Yew and Liu, Xiaojiang and Rui, Yong},
year = {2015},
month = {09},
pages = {},
title = {Automatically Solving Number Word Problems by Semantic Parsing and Reasoning},
doi = {10.18653/v1/D15-1135}
}
```
