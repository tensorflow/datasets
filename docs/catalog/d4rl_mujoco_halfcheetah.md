<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_mujoco_halfcheetah" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_mujoco_halfcheetah&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_mujoco_halfcheetah" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl/home" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_mujoco_halfcheetah`


*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

*   **Homepage**:
    [https://sites.google.com/view/d4rl/home](https://sites.google.com/view/d4rl/home)

*   **Source code**:
    [`tfds.d4rl.d4rl_mujoco_halfcheetah.D4rlMujocoHalfcheetah`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_mujoco_halfcheetah/d4rl_mujoco_halfcheetah.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.0.1`: Support for episode and step metadata, and unification of the
        reward shape across all the configs.
    *   **`1.1.0`** (default): Added is_last.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{fu2020d4rl,
    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},
    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
    year={2020},
    eprint={2004.07219},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

## d4rl_mujoco_halfcheetah/v0-expert (default config)

*   **Download size**: `83.44 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v0-medium

*   **Download size**: `82.92 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-medium-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v0-medium-expert

*   **Download size**: `166.36 MiB`

*   **Dataset size**: `196.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,004

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-medium-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v0-mixed

*   **Download size**: `8.60 MiB`

*   **Dataset size**: `9.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 101

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-mixed-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v0-random

*   **Download size**: `84.79 MiB`

*   **Dataset size**: `98.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,002

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v0-random-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-expert

*   **Download size**: `146.94 MiB`

*   **Dataset size**: `451.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 17), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium

*   **Download size**: `146.65 MiB`

*   **Dataset size**: `451.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 17), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium-expert

*   **Download size**: `293.00 MiB`

*   **Dataset size**: `342.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-medium-replay

*   **Download size**: `57.68 MiB`

*   **Dataset size**: `34.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(9,), dtype=tf.float64),
            'qvel': Tensor(shape=(9,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-medium-replay-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-full-replay

*   **Download size**: `285.01 MiB`

*   **Dataset size**: `171.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(9,), dtype=tf.float64),
            'qvel': Tensor(shape=(9,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-full-replay-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v1-random

*   **Download size**: `145.19 MiB`

*   **Dataset size**: `171.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v1-random-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-expert

*   **Download size**: `209.48 MiB`

*   **Dataset size**: `451.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 17), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-full-replay

*   **Download size**: `285.01 MiB`

*   **Dataset size**: `171.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(9,), dtype=tf.float64),
            'qvel': Tensor(shape=(9,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-full-replay-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium

*   **Download size**: `209.48 MiB`

*   **Dataset size**: `451.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 17), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(6,), dtype=tf.float32),
            'weight': Tensor(shape=(6, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium-expert

*   **Download size**: `418.37 MiB`

*   **Dataset size**: `342.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,000

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-expert-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-medium-replay

*   **Download size**: `57.68 MiB`

*   **Dataset size**: `34.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 202

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(9,), dtype=tf.float64),
            'qvel': Tensor(shape=(9,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-medium-replay-1.1.0.html";
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

## d4rl_mujoco_halfcheetah/v2-random

*   **Download size**: `208.68 MiB`

*   **Dataset size**: `171.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(9,), dtype=tf.float32),
            'qvel': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(17,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/d4rl_mujoco_halfcheetah-v2-random-1.1.0.html";
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