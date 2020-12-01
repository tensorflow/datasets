<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="big_patent" />
  <meta itemprop="description" content="BIGPATENT, consisting of 1.3 million records of U.S. patent documents&#10;along with human written abstractive summaries.&#10;Each US patent application is filed under a Cooperative Patent Classification&#10;(CPC) code. There are nine such classification categories:&#10;A (Human Necessities), B (Performing Operations; Transporting),&#10;C (Chemistry; Metallurgy), D (Textiles; Paper), E (Fixed Constructions),&#10;F (Mechanical Engineering; Lightning; Heating; Weapons; Blasting),&#10;G (Physics), H (Electricity), and&#10;Y (General tagging of new or cross-sectional technology)&#10;&#10;There are two features:&#10;  - description: detailed description of patent.&#10;  - summary: Patent abastract.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;big_patent&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/big_patent" />
  <meta itemprop="sameAs" content="https://evasharma.github.io/bigpatent/" />
  <meta itemprop="citation" content="@misc{sharma2019bigpatent,&#10;    title={BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization},&#10;    author={Eva Sharma and Chen Li and Lu Wang},&#10;    year={2019},&#10;    eprint={1906.03741},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `big_patent`

*   **Description**:

BIGPATENT, consisting of 1.3 million records of U.S. patent documents along with
human written abstractive summaries. Each US patent application is filed under a
Cooperative Patent Classification (CPC) code. There are nine such classification
categories: A (Human Necessities), B (Performing Operations; Transporting), C
(Chemistry; Metallurgy), D (Textiles; Paper), E (Fixed Constructions), F
(Mechanical Engineering; Lightning; Heating; Weapons; Blasting), G (Physics), H
(Electricity), and Y (General tagging of new or cross-sectional technology)

There are two features: - description: detailed description of patent. -
summary: Patent abastract.

*   **Homepage**:
    [https://evasharma.github.io/bigpatent/](https://evasharma.github.io/bigpatent/)

*   **Source code**:
    [`tfds.summarization.BigPatent`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/big_patent.py)

*   **Versions**:

    *   `1.0.0`: lower cased tokenized words
    *   `2.0.0`: Update to use cased raw strings
    *   **`2.1.2`** (default): Fix update to cased raw strings.

*   **Download size**: `9.45 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'abstract': Text(shape=(), dtype=tf.string),
    'description': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('description', 'abstract')`

*   **Citation**:

```
@misc{sharma2019bigpatent,
    title={BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization},
    author={Eva Sharma and Chen Li and Lu Wang},
    year={2019},
    eprint={1906.03741},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## big_patent/all (default config)

*   **Config description**: Patents under all categories.

*   **Dataset size**: `35.17 GiB`

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 67,072
`'train'`      | 1,207,222
`'validation'` | 67,068

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-all-2.1.2.html";
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

## big_patent/a

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)a: Human Necessities

*   **Dataset size**: `5.16 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,675
`'train'`      | 174,134
`'validation'` | 9,674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-a-2.1.2.html";
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

## big_patent/b

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)b: Performing Operations; Transporting

*   **Dataset size**: `4.06 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,974
`'train'`      | 161,520
`'validation'` | 8,973

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-b-2.1.2.html";
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

## big_patent/c

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)c: Chemistry; Metallurgy

*   **Dataset size**: `3.63 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 5,614
`'train'`      | 101,042
`'validation'` | 5,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-c-2.1.2.html";
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

## big_patent/d

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)d: Textiles; Paper

*   **Dataset size**: `255.56 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 565
`'train'`      | 10,164
`'validation'` | 565

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-d-2.1.2.html";
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

## big_patent/e

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)e: Fixed Constructions

*   **Dataset size**: `871.40 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,914
`'train'`      | 34,443
`'validation'` | 1,914

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-e-2.1.2.html";
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

## big_patent/f

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)f: Mechanical Engineering; Lightning; Heating; Weapons; Blasting

*   **Dataset size**: `2.06 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,754
`'train'`      | 85,568
`'validation'` | 4,754

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-f-2.1.2.html";
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

## big_patent/g

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)g: Physics

*   **Dataset size**: `8.19 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 14,386
`'train'`      | 258,935
`'validation'` | 14,385

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-g-2.1.2.html";
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

## big_patent/h

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)h: Electricity

*   **Dataset size**: `7.50 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 14,279
`'train'`      | 257,019
`'validation'` | 14,279

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-h-2.1.2.html";
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

## big_patent/y

*   **Config description**: Patents under Cooperative Patent Classification
    (CPC)y: General tagging of new or cross-sectional technology

*   **Dataset size**: `3.46 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,911
`'train'`      | 124,397
`'validation'` | 6,911

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/big_patent-y-2.1.2.html";
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