<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xtreme_pawsx" />
  <meta itemprop="description" content="This dataset contains machine translations of the English PAWS training&#10;data. The translations are provided by the XTREME benchmark and cover the following&#10;languages:&#10;&#10;* French&#10;* Spanish&#10;* German&#10;* Chinese&#10;* Japanese&#10;* Korean&#10;&#10;For further details on PAWS, see the  papers:&#10;PAWS: Paraphrase Adversaries from Word Scrambling&#10;at https://arxiv.org/abs/1904.01130&#10;and&#10;PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification&#10;at  https://arxiv.org/abs/1908.11828&#10;&#10;For details related to XTREME, please refer to:&#10;XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization&#10;at https://arxiv.org/abs/2003.11080&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xtreme_pawsx&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xtreme_pawsx" />
  <meta itemprop="sameAs" content="https://github.com/google-research/xtreme" />
  <meta itemprop="citation" content="@article{hu2020xtreme,&#10;      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},&#10;      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},&#10;      journal   = {CoRR},&#10;      volume    = {abs/2003.11080},&#10;      year      = {2020},&#10;      archivePrefix = {arXiv},&#10;      eprint    = {2003.11080}&#10;}" />
</div>

# `xtreme_pawsx`

*   **Description**:

This dataset contains machine translations of the English PAWS training data.
The translations are provided by the XTREME benchmark and cover the following
languages:

*   French
*   Spanish
*   German
*   Chinese
*   Japanese
*   Korean

For further details on PAWS, see the papers: PAWS: Paraphrase Adversaries from
Word Scrambling at https://arxiv.org/abs/1904.01130 and PAWS-X: A Cross-lingual
Adversarial Dataset for Paraphrase Identification at
https://arxiv.org/abs/1908.11828

For details related to XTREME, please refer to: XTREME: A Massively Multilingual
Multi-task Benchmark for Evaluating Cross-lingual Generalization at
https://arxiv.org/abs/2003.11080

*   **Homepage**:
    [https://github.com/google-research/xtreme](https://github.com/google-research/xtreme)

*   **Source code**:
    [`tfds.text.xtreme_pawsx.XtremePawsx`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/xtreme_pawsx/xtreme_pawsx.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{hu2020xtreme,
      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},
      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},
      journal   = {CoRR},
      volume    = {abs/2003.11080},
      year      = {2020},
      archivePrefix = {arXiv},
      eprint    = {2003.11080}
}
```

## xtreme_pawsx/de (default config)

*   **Config description**: Translated to de

*   **Download size**: `22.34 MiB`

*   **Dataset size**: `14.19 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,340

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-de-1.0.0.html";
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

## xtreme_pawsx/es

*   **Config description**: Translated to es

*   **Download size**: `22.27 MiB`

*   **Dataset size**: `14.09 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,244

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-es-1.0.0.html";
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

## xtreme_pawsx/fr

*   **Config description**: Translated to fr

*   **Download size**: `22.70 MiB`

*   **Dataset size**: `14.53 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,208

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-fr-1.0.0.html";
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

## xtreme_pawsx/ja

*   **Config description**: Translated to ja

*   **Download size**: `25.12 MiB`

*   **Dataset size**: `16.98 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,086

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-ja-1.0.0.html";
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

## xtreme_pawsx/ko

*   **Config description**: Translated to ko

*   **Download size**: `22.99 MiB`

*   **Dataset size**: `14.86 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,298

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-ko-1.0.0.html";
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

## xtreme_pawsx/zh

*   **Config description**: Translated to zh

*   **Download size**: `21.45 MiB`

*   **Dataset size**: `13.21 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 49,149

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/xtreme_pawsx-zh-1.0.0.html";
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