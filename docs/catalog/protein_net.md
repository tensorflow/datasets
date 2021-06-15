<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="protein_net" />
  <meta itemprop="description" content="ProteinNet is a standardized data set for machine learning of protein structure.&#10;It provides protein sequences, structures (secondary and tertiary), multiple&#10;sequence alignments (MSAs), position-specific scoring matrices (PSSMs), and&#10;standardized training / validation / test splits. ProteinNet builds on the&#10;biennial CASP assessments, which carry out blind predictions of recently solved&#10;but publicly unavailable protein structures, to provide test sets that push the&#10;frontiers of computational methodology. It is organized as a series of data&#10;sets, spanning CASP 7 through 12 (covering a ten-year period), to provide a&#10;range of data set sizes that enable assessment of new methods in relatively data&#10;poor and data rich regimes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;protein_net&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/protein_net" />
  <meta itemprop="sameAs" content="https://github.com/aqlaboratory/proteinnet" />
  <meta itemprop="citation" content="@article{ProteinNet19,&#10;title = {{ProteinNet}: a standardized data set for machine learning of protein structure},&#10;author = {AlQuraishi, Mohammed},&#10;journal = {BMC bioinformatics},&#10;volume = {20},&#10;number = {1},&#10;pages = {1--10},&#10;year = {2019},&#10;publisher = {BioMed Central}&#10;}" />
</div>

# `protein_net`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

ProteinNet is a standardized data set for machine learning of protein structure.
It provides protein sequences, structures (secondary and tertiary), multiple
sequence alignments (MSAs), position-specific scoring matrices (PSSMs), and
standardized training / validation / test splits. ProteinNet builds on the
biennial CASP assessments, which carry out blind predictions of recently solved
but publicly unavailable protein structures, to provide test sets that push the
frontiers of computational methodology. It is organized as a series of data
sets, spanning CASP 7 through 12 (covering a ten-year period), to provide a
range of data set sizes that enable assessment of new methods in relatively data
poor and data rich regimes.

*   **Homepage**:
    [https://github.com/aqlaboratory/proteinnet](https://github.com/aqlaboratory/proteinnet)

*   **Source code**:
    [`tfds.structured.proteinnet.ProteinNet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/proteinnet/proteinnet.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'evolutionary': Tensor(shape=(None, 21), dtype=tf.float32),
    'id': Text(shape=(), dtype=tf.string),
    'length': tf.int32,
    'mask': Tensor(shape=(None,), dtype=tf.bool),
    'primary': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=20)),
    'tertiary': Tensor(shape=(None, 3), dtype=tf.float32),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('primary', 'tertiary')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{ProteinNet19,
title = {{ProteinNet}: a standardized data set for machine learning of protein structure},
author = {AlQuraishi, Mohammed},
journal = {BMC bioinformatics},
volume = {20},
number = {1},
pages = {1--10},
year = {2019},
publisher = {BioMed Central}
}
```

## protein_net/casp7 (default config)

*   **Download size**: `3.18 GiB`

*   **Dataset size**: `2.53 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 93
`'train_100'`  | 34,557
`'train_30'`   | 10,333
`'train_50'`   | 13,024
`'train_70'`   | 15,207
`'train_90'`   | 17,611
`'train_95'`   | 17,938
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp7-1.0.0.html";
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

## protein_net/casp8

*   **Download size**: `4.96 GiB`

*   **Dataset size**: `3.55 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 120
`'train_100'`  | 48,087
`'train_30'`   | 13,881
`'train_50'`   | 17,970
`'train_70'`   | 21,191
`'train_90'`   | 24,556
`'train_95'`   | 25,035
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp8-1.0.0.html";
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

## protein_net/casp9

*   **Download size**: `6.65 GiB`

*   **Dataset size**: `4.54 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 116
`'train_100'`  | 60,350
`'train_30'`   | 16,973
`'train_50'`   | 22,172
`'train_70'`   | 26,263
`'train_90'`   | 30,513
`'train_95'`   | 31,128
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp9-1.0.0.html";
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

## protein_net/casp10

*   **Download size**: `8.65 GiB`

*   **Dataset size**: `5.57 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 95
`'train_100'`  | 73,116
`'train_30'`   | 19,495
`'train_50'`   | 25,897
`'train_70'`   | 31,001
`'train_90'`   | 36,258
`'train_95'`   | 37,033
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp10-1.0.0.html";
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

## protein_net/casp11

*   **Download size**: `10.81 GiB`

*   **Dataset size**: `6.72 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 81
`'train_100'`  | 87,573
`'train_30'`   | 22,344
`'train_50'`   | 29,936
`'train_70'`   | 36,005
`'train_90'`   | 42,507
`'train_95'`   | 43,544
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp11-1.0.0.html";
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

## protein_net/casp12

*   **Download size**: `13.18 GiB`

*   **Dataset size**: `8.05 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 40
`'train_100'`  | 104,059
`'train_30'`   | 25,299
`'train_50'`   | 34,039
`'train_70'`   | 41,522
`'train_90'`   | 49,600
`'train_95'`   | 50,914
`'validation'` | 224

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/protein_net-casp12-1.0.0.html";
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