<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="star_cfq" />
  <meta itemprop="description" content="The *-CFQ datasets (and their splits) for measuring the scalability of&#10;compositional generalization.&#10;&#10;See https://arxiv.org/abs/2012.08266 for background.&#10;&#10;Example usage:&#10;&#10;```&#10;data = tfds.load(&#x27;star_cfq/single_pool_10x_b_cfq&#x27;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;star_cfq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/star_cfq" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/star-cfq" />
  <meta itemprop="citation" content="@inproceedings{Tsarkov2021,&#10;  title={*-CFQ: Analyzing the Scalability of Machine Learning on a Compositional Task},&#10;  author={Dmitry Tsarkov and Tibor Tihon and Nathan Scales and Nikola Momchev and Danila Sinopalnikov and Nathanael Sch&quot;{a}rli},&#10;  booktitle={AAAI},&#10;  year={2021},&#10;  url={https://arxiv.org/abs/2012.08266},&#10;}" />
</div>

# `star_cfq`


*   **Description**:

The *-CFQ datasets (and their splits) for measuring the scalability of
compositional generalization.

See https://arxiv.org/abs/2012.08266 for background.

Example usage:

```
data = tfds.load('star_cfq/single_pool_10x_b_cfq')
```

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/star-cfq](https://github.com/google-research/google-research/tree/master/star-cfq)

*   **Source code**:
    [`tfds.text.star_cfq.StarCFQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/star_cfq/star_cfq.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Features**:

```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('question', 'query')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{Tsarkov2021,
  title={*-CFQ: Analyzing the Scalability of Machine Learning on a Compositional Task},
  author={Dmitry Tsarkov and Tibor Tihon and Nathan Scales and Nikola Momchev and Danila Sinopalnikov and Nathanael Sch"{a}rli},
  booktitle={AAAI},
  year={2021},
  url={https://arxiv.org/abs/2012.08266},
}
```

## star_cfq/single_pool_0.1x_cfq (default config)

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `46.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.1x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.2x_cfq

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `50.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.2x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.3x_cfq

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `54.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.3x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_cfq

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `63.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_cfq

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `84.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_cfq-1.1.0.html";
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

## star_cfq/single_pool_2x_cfq

*   **Download size**: `10.56 MiB`

*   **Dataset size**: `105.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,615

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_2x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.1x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `54.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.1x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.2x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `59.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.2x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.3x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `64.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.3x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `75.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `100.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_2x_o_cfq

*   **Download size**: `10.64 MiB`

*   **Dataset size**: `119.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 133,159

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_2x_o_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.1x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `69.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.1x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.2x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `76.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.2x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.3x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `82.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.3x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `95.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `127.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_2x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `190.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_2x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `254.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_6x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `444.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_6x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `698.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `1.92 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_u_cfq

*   **Download size**: `443.54 MiB`

*   **Dataset size**: `6.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,574,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_u_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.1x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `69.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.1x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.2x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `76.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.2x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `79.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.3x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `82.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.3x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.4x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `89.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.4x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `95.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.6x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `101.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.6x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.7x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `108.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 67,019

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.7x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `111.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.8x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `114.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.8x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `127.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_1.5x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `158.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1.5x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_2x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `190.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_2x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `254.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_4x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `317.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_4x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_5x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `381.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_5x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_6x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `444.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_6x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_8x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `572.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_8x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `699.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_11x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `763.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_11x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_12x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `827.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_12x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_13x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `890.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_13x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_15x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `1018.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_15x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `1.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_35x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `2.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_35x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `5.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_85x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `5.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,138,070

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_85x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_b_cfq

*   **Download size**: `376.30 MiB`

*   **Dataset size**: `5.62 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,567,610

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_b_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `78.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `94.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `109.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `125.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `250.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `690.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `1.90 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `4.96 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_l_cfq

*   **Download size**: `504.26 MiB`

*   **Dataset size**: `6.18 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,574,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `79.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `95.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `111.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `127.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `255.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `702.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `1.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `5.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_half_l_cfq

*   **Download size**: `455.16 MiB`

*   **Dataset size**: `6.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,201,303

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_half_l_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `84.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `100.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `117.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `134.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `269.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `740.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `2.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `5.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_n_cfq

*   **Download size**: `402.73 MiB`

*   **Dataset size**: `5.99 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,620,983

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `83.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `99.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `116.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `132.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `265.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `729.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `2.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `5.25 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_half_n_cfq

*   **Download size**: `395.14 MiB`

*   **Dataset size**: `5.88 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,604,020

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_half_n_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `84.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `101.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `118.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `135.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `269.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_3x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_10x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `742.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_10x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_30x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `2.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_30x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_80x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `5.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_80x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_100x_x_cfq

*   **Download size**: `534.78 MiB`

*   **Dataset size**: `6.65 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,574,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_100x_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.25x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `82.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 23,935

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.25x_half_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.5x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `99.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.5x_half_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_0.75x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `115.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 71,806

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_0.75x_half_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_1x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `132.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/star_cfq-single_pool_1x_half_x_cfq-1.1.0.html";
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

## star_cfq/single_pool_3x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `264.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/single_pool_10x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `726.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/single_pool_30x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `2.00 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/single_pool_80x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `5.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/single_pool_100x_half_x_cfq

*   **Download size**: `467.63 MiB`

*   **Dataset size**: `6.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,199,216

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `69.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `82.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `126.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `189.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `252.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `692.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.91 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_80x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `4.98 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,485,866

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `76.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `88.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `132.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `195.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `258.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `699.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.91 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_80x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `4.98 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,668,934

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,495,418

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `82.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `95.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `139.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `202.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `264.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `705.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.92 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.16 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,504,958

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `89.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `101.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `145.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `208.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `271.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `711.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.92 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,514,495

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `101.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `114.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `158.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `221.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `284.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `724.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.18 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,533,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `133.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `146.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `190.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `253.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `315.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `756.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_80x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `5.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,755,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,581,277

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `197.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `209.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `253.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `316.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `379.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `819.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `2.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,676,716

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `260.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `273.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `317.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `380.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `442.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `883.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `2.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,772,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `387.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `400.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `444.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `507.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `569.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1010.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `2.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `6.46 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,962,925

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `70.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `82.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `128.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `192.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `257.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `709.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.95 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_80x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.52 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,283,855

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `76.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `89.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `134.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `199.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `263.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `715.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.96 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_80x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,668,934

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.52 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,293,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `82.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `95.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `140.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `205.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `270.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `721.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.53 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,302,961

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `89.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `102.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `147.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `212.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `276.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `728.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.54 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,312,521

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `101.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `114.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `160.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `224.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `289.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `741.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.98 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.55 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,331,627

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `133.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `146.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `191.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `256.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `321.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `772.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `2.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_80x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,755,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.58 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,379,410

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `197.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `210.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `255.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `320.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `384.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `836.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `2.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.64 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,474,981

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `260.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `273.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `318.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `383.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `448.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `900.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `2.14 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.70 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,570,525

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `387.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `400.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `445.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `510.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `575.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.00 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `2.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `5.83 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,761,618

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `70.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `84.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `132.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `200.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `269.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `749.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.75 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,705,695

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `76.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `90.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `138.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `207.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `275.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `755.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,715,160

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `83.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `96.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `144.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `213.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `281.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `761.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,724,612

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `89.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `103.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `151.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `219.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `288.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `768.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,734,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `102.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `116.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `164.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `232.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `301.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `780.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.78 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,752,988

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `134.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `147.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `195.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `264.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `332.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `812.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.81 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,800,286

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `197.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `211.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `259.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `327.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `396.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `876.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.19 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.87 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,894,872

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `261.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `274.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `322.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `391.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `460.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `940.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `4.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 6,989,437

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `388.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `401.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `449.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `518.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `587.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `1.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `2.38 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `5.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,178,687

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `70.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `84.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `132.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `202.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `271.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `756.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.44 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,366,855

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `76.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `90.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `139.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `208.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `278.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `762.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.45 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,376,429

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `83.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `97.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `145.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `215.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `284.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `769.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.45 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,386,003

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `89.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `103.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `151.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `221.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `290.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `775.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.46 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,395,577

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `102.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `116.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `164.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `234.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `303.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `788.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.12 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.47 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,414,726

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `134.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `147.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `196.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `265.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `335.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `820.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.50 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,462,597

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `197.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `211.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `260.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `329.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `398.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `883.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.57 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,558,339

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `261.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `275.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `323.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `392.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `462.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `947.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.28 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.63 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,654,081

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `388.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `402.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `450.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `519.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `589.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `1.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.40 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `2.75 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,845,565

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `70.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `83.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `131.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `199.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `266.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `739.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_80x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `5.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.66 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,568,229

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `76.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `90.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `137.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `205.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `272.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `746.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_80x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `5.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,668,934

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.67 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,577,771

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `83.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `96.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `144.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `211.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `279.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `752.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.67 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,587,309

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `89.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `103.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `150.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `218.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `285.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `758.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.68 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,596,853

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `102.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `115.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `163.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `230.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `298.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `771.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.69 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,615,914

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `133.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `147.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `194.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `262.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `330.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `803.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_80x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `5.41 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,755,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.72 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,663,600

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `197.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `211.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `258.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `326.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `393.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `867.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.79 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,759,017

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `261.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `274.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `322.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `389.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `457.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `930.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.23 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.85 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,854,427

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `388.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `401.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `448.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `516.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `584.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `1.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `2.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `6.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 10,045,243

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `70.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `83.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `130.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `196.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `263.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `728.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_80x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,659,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.74 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,373,636

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `76.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `89.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `136.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `203.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `269.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `735.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 966,994

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,881,834

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_80x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,668,934

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.75 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,383,193

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `83.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `96.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,870

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `142.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 114,890

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `209.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 210,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `275.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 306,374

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `741.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 976,568

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,891,408

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,392,755

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `89.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 38,296

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `102.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `149.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `215.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `282.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `747.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 986,142

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,900,982

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,402,320

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `102.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,445

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `115.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 76,593

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `162.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 143,613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `228.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 239,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `295.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 335,097

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `760.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,005,291

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,920,131

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,421,434

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `133.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 105,316

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `147.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 124,464

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `193.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `260.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `326.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `792.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,053,162

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,968,002

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_80x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 7,755,102

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_1x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.81 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,469,220

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `197.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 201,058

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `210.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 220,206

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `257.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `323.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `390.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `856.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,148,904

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.14 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,063,744

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_2x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.87 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,564,791

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `260.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 296,800

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `274.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 315,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `320.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 382,968

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `387.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 478,710

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `453.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `919.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,244,646

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.20 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,159,486

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_3x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `5.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,660,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `387.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 488,284

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `401.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 507,432

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `447.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_2x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `514.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 670,194

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `580.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 765,936

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `1.02 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,436,130

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `2.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 3,350,970

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/equal_weighting_5x_b_cfq_100x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `6.05 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 8,851,510

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `76.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `101.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `190.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `442.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.30 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `3.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `9.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `76.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `102.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `191.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `448.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.31 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `3.82 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `10.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `76.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `103.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `195.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `459.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `1.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `3.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `76.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `103.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `196.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `462.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `1.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `3.95 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `76.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `103.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `194.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `457.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `1.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `3.90 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `10.31 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `76.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `102.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `193.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `453.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `1.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `3.87 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `10.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `76.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `101.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `190.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `442.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `1.30 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `3.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_l_cfq

*   **Download size**: `859.54 MiB`

*   **Dataset size**: `9.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `76.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `102.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `191.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `448.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `1.31 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `3.82 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_half_l_cfq

*   **Download size**: `781.70 MiB`

*   **Dataset size**: `10.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `76.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `103.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `195.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `460.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `1.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_n_cfq

*   **Download size**: `712.20 MiB`

*   **Dataset size**: `3.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `76.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `103.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `462.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `1.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_n_cfq

*   **Download size**: `544.71 MiB`

*   **Dataset size**: `3.95 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `76.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `103.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `194.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `457.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `1.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `3.91 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_x_cfq

*   **Download size**: `892.84 MiB`

*   **Dataset size**: `10.31 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `76.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `102.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 57,444

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `193.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `453.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 574,452

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `1.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 1,914,840

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `3.87 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 5,744,520

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_half_x_cfq

*   **Download size**: `797.12 MiB`

*   **Dataset size**: `10.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 95,742
`'train'` | 15,318,720

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_0.1x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `56.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 9,574

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_0.2x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `62.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 19,148

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_0.3x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `69.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 28,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_0.5x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `81.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 47,871

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_1x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `113.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 95,742

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_2x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `177.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 191,484

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_3x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `241.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 287,226

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_10x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `687.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 95,742
`'train'` | 957,420

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_30x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `1.92 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 2,872,260

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/ungrounded_on_grounded_100x

*   **Download size**: `452.00 MiB`

*   **Dataset size**: `6.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 95,742
`'train'` | 9,574,200

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `530.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `560.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `522.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,230
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `538.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `538.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,367
`'train'`      | 1,031,215
`'validation'` | 10,367

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `554.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `543.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,243
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,236
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `537.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,225
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `534.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `537.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `542.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `537.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `536.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `561.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `526.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `538.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `531.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,365
`'train'`      | 1,031,218
`'validation'` | 10,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `540.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,223
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,366
`'train'`      | 1,031,216
`'validation'` | 10,367

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,226
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `534.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,331
`'train'`      | 1,031,286
`'validation'` | 10,332

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `545.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,247
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `532.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,254
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `522.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `534.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,365
`'train'`      | 1,031,218
`'validation'` | 10,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `540.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `524.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,222
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `533.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,223
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `536.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,252
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `547.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,335
`'train'`      | 1,031,278
`'validation'` | 10,336

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `537.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `541.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `534.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `628.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,248
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `597.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,225
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `582.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,252
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `600.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `581.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `584.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `579.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,223
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `582.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `585.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,340
`'train'`      | 1,031,269
`'validation'` | 10,340

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `614.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,253
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `589.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,247
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `584.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `557.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,254
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `573.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `582.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `587.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `595.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `585.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `583.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `614.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `583.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `564.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,246
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `581.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,245
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `568.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `611.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `595.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `618.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,230
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `590.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,368
`'train'`      | 1,031,212
`'validation'` | 10,369

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `626.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,246
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `599.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `588.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `593.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `574.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,255
`'validation'` | 10,347

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `599.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `567.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `582.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,243
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,244
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `553.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,335
`'train'`      | 1,031,279
`'validation'` | 10,335

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `539.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `528.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `547.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `557.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,338
`'train'`      | 1,031,272
`'validation'` | 10,339

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `555.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,230
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `550.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `547.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `555.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `557.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `535.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `595.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,367
`'train'`      | 1,031,215
`'validation'` | 10,367

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `531.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `542.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,247
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `556.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `554.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,331
`'train'`      | 1,031,286
`'validation'` | 10,332

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `566.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `536.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,247
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `542.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `541.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,369
`'train'`      | 1,031,211
`'validation'` | 10,369

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `548.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,340
`'train'`      | 1,031,269
`'validation'` | 10,340

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `534.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `532.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `547.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `572.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,370
`'train'`      | 1,031,209
`'validation'` | 10,370

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `552.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,236
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `565.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,221
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `561.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `555.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `549.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `576.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,254
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `584.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `552.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `546.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `547.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,366
`'train'`      | 1,031,217
`'validation'` | 10,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `559.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `551.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,368
`'train'`      | 1,031,213
`'validation'` | 10,368

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `545.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,222
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `552.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,323
`'train'`      | 1,031,302
`'validation'` | 10,324

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `543.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `567.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `553.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `587.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `550.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,366
`'train'`      | 1,031,217
`'validation'` | 10,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `560.61 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `537.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `574.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,221
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `564.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `578.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `550.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,236
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `559.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `556.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,244
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `565.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,244
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `566.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `553.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `564.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `542.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,244
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `567.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `549.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,221
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `568.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,248
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `561.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,342
`'train'`      | 1,031,264
`'validation'` | 10,343

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `551.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `546.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,252
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `561.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,255
`'validation'` | 10,347

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `659.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `671.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,344
`'train'`      | 1,031,261
`'validation'` | 10,344

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `605.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,330
`'train'`      | 1,031,289
`'validation'` | 10,330

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `652.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `660.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `554.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `679.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `633.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `656.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `656.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `599.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `551.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `582.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `597.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,246
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `666.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `663.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `557.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `590.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `562.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,223
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `588.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,246
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `600.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `589.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,347
`'train'`      | 1,031,254
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `648.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `570.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `610.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `645.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `630.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,351
`'train'`      | 1,031,247
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `600.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,248
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `577.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `638.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `688.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,226
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `653.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,349
`'train'`      | 1,031,251
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `592.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `648.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `656.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,349
`'train'`      | 1,031,250
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `662.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `671.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `634.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,248
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `631.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,349
`'train'`      | 1,031,250
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `624.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `691.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,225
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `658.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,253
`'validation'` | 10,348

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `651.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,229
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `650.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,243
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `662.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,225
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `614.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `575.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `650.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,336
`'train'`      | 1,031,276
`'validation'` | 10,337

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `586.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,343
`'train'`      | 1,031,263
`'validation'` | 10,343

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `658.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `657.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,239
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `678.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `657.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `673.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `625.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `673.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `662.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,226
`'validation'` | 10,362

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `656.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `548.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,355
`'train'`      | 1,031,238
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `657.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,220
`'validation'` | 10,365

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `610.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `643.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,220
`'validation'` | 10,365

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `664.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,220
`'validation'` | 10,365

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `611.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `620.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `650.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,330
`'train'`      | 1,031,289
`'validation'` | 10,330

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `572.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,252
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `607.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `608.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `639.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,232
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `654.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `694.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,230
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r0

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `621.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r1

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `619.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r2

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `643.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r3

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `621.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,342
`'train'`      | 1,031,265
`'validation'` | 10,342

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r4

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `675.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,221
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r5

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `590.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,231
`'validation'` | 10,359

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r6

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `595.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r7

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `671.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,334
`'train'`      | 1,031,280
`'validation'` | 10,335

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r8

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `683.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r9

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `648.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r10

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `591.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,363
`'train'`      | 1,031,223
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r11

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `668.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,235
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r12

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `644.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,366
`'train'`      | 1,031,217
`'validation'` | 10,366

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r13

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `645.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,245
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r14

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `627.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r15

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `638.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r16

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `633.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,362
`'train'`      | 1,031,224
`'validation'` | 10,363

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r17

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `659.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,240
`'validation'` | 10,355

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r18

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `641.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,237
`'validation'` | 10,356

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r19

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `627.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,358
`'train'`      | 1,031,233
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r20

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `586.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,356
`'train'`      | 1,031,236
`'validation'` | 10,357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r21

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `608.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,333
`'train'`      | 1,031,282
`'validation'` | 10,334

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r22

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `571.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,359
`'train'`      | 1,031,230
`'validation'` | 10,360

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r23

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `610.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,249
`'validation'` | 10,350

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r24

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `558.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,245
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r25

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `634.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,243
`'validation'` | 10,353

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r26

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `652.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,353
`'train'`      | 1,031,242
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r27

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `629.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,364
`'train'`      | 1,031,221
`'validation'` | 10,364

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r28

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `648.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,357
`'train'`      | 1,031,234
`'validation'` | 10,358

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r29

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `672.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,369
`'train'`      | 1,031,210
`'validation'` | 10,370

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r30

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `658.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,361
`'train'`      | 1,031,227
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r31

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `631.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,350
`'train'`      | 1,031,248
`'validation'` | 10,351

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r32

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `664.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,348
`'train'`      | 1,031,252
`'validation'` | 10,349

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r33

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `563.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,354
`'train'`      | 1,031,241
`'validation'` | 10,354

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r34

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `575.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,360
`'train'`      | 1,031,228
`'validation'` | 10,361

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r35

*   **Download size**: `1.47 GiB`

*   **Dataset size**: `601.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 10,352
`'train'`      | 1,031,245
`'validation'` | 10,352

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.
