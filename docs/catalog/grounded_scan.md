<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="grounded_scan" />
  <meta itemprop="description" content="Grounded SCAN (gSCAN) is a synthetic dataset for evaluating compositional&#10;generalization in situated language understanding. gSCAN pairs natural language&#10;instructions with action sequences, and requires the agent to interpret&#10;instructions within the context of a grid-based visual navigation environment.&#10;&#10;More information can be found at: https://github.com/LauraRuis/groundedSCAN&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;grounded_scan&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/grounded_scan" />
  <meta itemprop="sameAs" content="https://github.com/LauraRuis/groundedSCAN" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-2003-05161,&#10;  author    = {Laura Ruis and&#10;               Jacob Andreas and&#10;               Marco Baroni and&#10;               Diane Bouchacourt and&#10;               Brenden M. Lake},&#10;  title     = {A Benchmark for Systematic Generalization in Grounded Language Understanding},&#10;  journal   = {CoRR},&#10;  volume    = {abs/2003.05161},&#10;  year      = {2020},&#10;  url       = {https://arxiv.org/abs/2003.05161},&#10;  eprinttype = {arXiv},&#10;  eprint    = {2003.05161},&#10;  timestamp = {Tue, 17 Mar 2020 14:18:27 +0100},&#10;  biburl    = {https://dblp.org/rec/journals/corr/abs-2003-05161.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `grounded_scan`


*   **Description**:

Grounded SCAN (gSCAN) is a synthetic dataset for evaluating compositional
generalization in situated language understanding. gSCAN pairs natural language
instructions with action sequences, and requires the agent to interpret
instructions within the context of a grid-based visual navigation environment.

More information can be found at: https://github.com/LauraRuis/groundedSCAN

*   **Homepage**:
    [https://github.com/LauraRuis/groundedSCAN](https://github.com/LauraRuis/groundedSCAN)

*   **Source code**:
    [`tfds.vision_language.grounded_scan.GroundedScan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/grounded_scan/grounded_scan.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.
    *   `1.1.0`: Changed `vector` feature to Text().

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'command': Sequence(Text(shape=(), dtype=tf.string)),
    'manner': Text(shape=(), dtype=tf.string),
    'meaning': Sequence(Text(shape=(), dtype=tf.string)),
    'referred_target': Text(shape=(), dtype=tf.string),
    'situation': FeaturesDict({
        'agent_direction': tf.int32,
        'agent_position': FeaturesDict({
            'column': tf.int32,
            'row': tf.int32,
        }),
        'direction_to_target': Text(shape=(), dtype=tf.string),
        'distance_to_target': tf.int32,
        'grid_size': tf.int32,
        'placed_objects': Sequence({
            'object': FeaturesDict({
                'color': Text(shape=(), dtype=tf.string),
                'shape': Text(shape=(), dtype=tf.string),
                'size': tf.int32,
            }),
            'position': FeaturesDict({
                'column': tf.int32,
                'row': tf.int32,
            }),
            'vector': Text(shape=(), dtype=tf.string),
        }),
        'target_object': FeaturesDict({
            'object': FeaturesDict({
                'color': Text(shape=(), dtype=tf.string),
                'shape': Text(shape=(), dtype=tf.string),
                'size': tf.int32,
            }),
            'position': FeaturesDict({
                'column': tf.int32,
                'row': tf.int32,
            }),
            'vector': Text(shape=(), dtype=tf.string),
        }),
    }),
    'target_commands': Sequence(Text(shape=(), dtype=tf.string)),
    'verb_in_command': Text(shape=(), dtype=tf.string),
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
@article{DBLP:journals/corr/abs-2003-05161,
  author    = {Laura Ruis and
               Jacob Andreas and
               Marco Baroni and
               Diane Bouchacourt and
               Brenden M. Lake},
  title     = {A Benchmark for Systematic Generalization in Grounded Language Understanding},
  journal   = {CoRR},
  volume    = {abs/2003.05161},
  year      = {2020},
  url       = {https://arxiv.org/abs/2003.05161},
  eprinttype = {arXiv},
  eprint    = {2003.05161},
  timestamp = {Tue, 17 Mar 2020 14:18:27 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2003-05161.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


## grounded_scan/compositional_splits (default config)

*   **Config description**: Examples for compositional generalization.

*   **Download size**: `82.10 MiB`

*   **Dataset size**: `1004.27 MiB`

*   **Splits**:

Split             | Examples
:---------------- | -------:
`'adverb_1'`      | 112,880
`'adverb_2'`      | 38,582
`'contextual'`    | 11,460
`'dev'`           | 3,716
`'situational_1'` | 88,642
`'situational_2'` | 16,808
`'test'`          | 19,282
`'train'`         | 367,933
`'visual'`        | 37,436
`'visual_easier'` | 18,718

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/grounded_scan-compositional_splits-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## grounded_scan/target_length_split

*   **Config description**: Examples for generalizing to larger target lengths.

*   **Download size**: `53.41 MiB`

*   **Dataset size**: `550.15 MiB`

*   **Splits**:

Split              | Examples
:----------------- | -------:
`'dev'`            | 1,821
`'target_lengths'` | 198,588
`'test'`           | 37,784
`'train'`          | 180,301

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/grounded_scan-target_length_split-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->