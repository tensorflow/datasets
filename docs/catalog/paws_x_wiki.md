<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="paws_x_wiki" />
  <meta itemprop="description" content="This dataset contains 23,659 human translated PAWS evaluation pairs and&#10;296,406 machine translated training pairs in six typologically distinct languages:&#10;&#10;* French&#10;* Spanish&#10;* German&#10;* Chinese&#10;* Japanese&#10;* Korean&#10;&#10;For further details, see the accompanying paper:&#10;PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification&#10;at  https://arxiv.org/abs/1908.11828&#10;&#10;Similar to PAWS Dataset, examples are split into Train/Dev/Test sections.&#10;All files are in the tsv format with four columns:&#10;&#10;id    A unique id for each pair&#10;sentence1 The first sentence&#10;sentence2    The second sentence&#10;(noisy_)label   (Noisy) label for each pair&#10;&#10;Each label has two possible values: 0 indicates the pair has different meaning,&#10;while 1 indicates the pair is a paraphrase.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;paws_x_wiki&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/paws_x_wiki" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/paws/tree/master/pawsx" />
  <meta itemprop="citation" content="@InProceedings{pawsx2019emnlp,&#10;  title = {{PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification}},&#10;  author = {Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},&#10;  booktitle = {Proc. of EMNLP},&#10;  year = {2019}&#10;}" />
</div>

# `paws_x_wiki`

*   **Description**:

This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406
machine translated training pairs in six typologically distinct languages:

*   French
*   Spanish
*   German
*   Chinese
*   Japanese
*   Korean

For further details, see the accompanying paper: PAWS-X: A Cross-lingual
Adversarial Dataset for Paraphrase Identification at
https://arxiv.org/abs/1908.11828

Similar to PAWS Dataset, examples are split into Train/Dev/Test sections. All
files are in the tsv format with four columns:

id A unique id for each pair sentence1 The first sentence sentence2 The second
sentence (noisy_)label (Noisy) label for each pair

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.

*   **Homepage**:
    [https://github.com/google-research-datasets/paws/tree/master/pawsx](https://github.com/google-research-datasets/paws/tree/master/pawsx)

*   **Source code**:
    [`tfds.text.paws_x_wiki.PawsXWiki`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/paws_x_wiki/paws_x_wiki.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `28.88 MiB`

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

*   **Citation**:

```
@InProceedings{pawsx2019emnlp,
  title = {{PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification}},
  author = {Yang, Yinfei and Zhang, Yuan and Tar, Chris and Baldridge, Jason},
  booktitle = {Proc. of EMNLP},
  year = {2019}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## paws_x_wiki/de (default config)

*   **Config description**: Translated to de

*   **Dataset size**: `15.27 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,380
`'validation'` | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-de-1.0.0.html";
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

## paws_x_wiki/en

*   **Config description**: Translated to en

*   **Dataset size**: `14.59 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,175
`'validation'` | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-en-1.0.0.html";
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

## paws_x_wiki/es

*   **Config description**: Translated to es

*   **Dataset size**: `15.27 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,401
`'validation'` | 1,961

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-es-1.0.0.html";
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

## paws_x_wiki/fr

*   **Config description**: Translated to fr

*   **Dataset size**: `15.79 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,399
`'validation'` | 1,988

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-fr-1.0.0.html";
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

## paws_x_wiki/ja

*   **Config description**: Translated to ja

*   **Dataset size**: `17.77 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,401
`'validation'` | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-ja-1.0.0.html";
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

## paws_x_wiki/ko

*   **Config description**: Translated to ko

*   **Dataset size**: `16.42 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,999
`'train'`      | 49,164
`'validation'` | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-ko-1.0.0.html";
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

## paws_x_wiki/zh

*   **Config description**: Translated to zh

*   **Dataset size**: `13.20 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 49,401
`'validation'` | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_x_wiki-zh-1.0.0.html";
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