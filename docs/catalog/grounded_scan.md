<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="grounded_scan" />
  <meta itemprop="description" content="Grounded SCAN (gSCAN) is a synthetic dataset for evaluating compositional&#10;generalization in situated language understanding. gSCAN pairs natural language&#10;instructions with action sequences, and requires the agent to interpret&#10;instructions within the context of a grid-based visual navigation environment.&#10;&#10;More information can be found at:&#10;&#10;* For the `compositional_splits` and the `target_length_split`:&#10;https://github.com/LauraRuis/groundedSCAN&#10;&#10;* For the `spatial_relation_splits`:&#10;https://github.com/google-research/language/tree/master/language/gscan/data&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;grounded_scan&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/grounded_scan" />
  <meta itemprop="sameAs" content="https://github.com/LauraRuis/groundedSCAN" />
  <meta itemprop="citation" content="@inproceedings{NEURIPS2020_e5a90182,&#10; author = {Ruis, Laura and Andreas, Jacob and Baroni, Marco and Bouchacourt, Diane and Lake, Brenden M},&#10; booktitle = {Advances in Neural Information Processing Systems},&#10; editor = {H. Larochelle and M. Ranzato and R. Hadsell and M. F. Balcan and H. Lin},&#10; pages = {19861--19872},&#10; publisher = {Curran Associates, Inc.},&#10; title = {A Benchmark for Systematic Generalization in Grounded Language Understanding},&#10; url = {https://proceedings.neurips.cc/paper/2020/file/e5a90182cc81e12ab5e72d66e0b46fe3-Paper.pdf},&#10; volume = {33},&#10; year = {2020}&#10;}&#10;&#10;@inproceedings{qiu-etal-2021-systematic,&#10;    title = &quot;Systematic Generalization on g{SCAN}: {W}hat is Nearly Solved and What is Next?&quot;,&#10;    author = &quot;Qiu, Linlu  and&#10;      Hu, Hexiang  and&#10;      Zhang, Bowen  and&#10;      Shaw, Peter  and&#10;      Sha, Fei&quot;,&#10;    booktitle = &quot;Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = nov,&#10;    year = &quot;2021&quot;,&#10;    address = &quot;Online and Punta Cana, Dominican Republic&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/2021.emnlp-main.166&quot;,&#10;    doi = &quot;10.18653/v1/2021.emnlp-main.166&quot;,&#10;    pages = &quot;2180--2188&quot;,&#10;}" />
</div>

# `grounded_scan`


*   **Description**:

Grounded SCAN (gSCAN) is a synthetic dataset for evaluating compositional
generalization in situated language understanding. gSCAN pairs natural language
instructions with action sequences, and requires the agent to interpret
instructions within the context of a grid-based visual navigation environment.

More information can be found at:

*   For the `compositional_splits` and the `target_length_split`:
    https://github.com/LauraRuis/groundedSCAN

*   For the `spatial_relation_splits`:
    https://github.com/google-research/language/tree/master/language/gscan/data

*   **Homepage**:
    [https://github.com/LauraRuis/groundedSCAN](https://github.com/LauraRuis/groundedSCAN)

*   **Source code**:
    [`tfds.vision_language.grounded_scan.GroundedScan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/grounded_scan/grounded_scan.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.1.0`: Changed `vector` feature to Text().
    *   **`2.0.0`** (default): Adds the new spatial_relation_splits config.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'command': Sequence(Text(shape=(), dtype=string)),
    'manner': Text(shape=(), dtype=string),
    'meaning': Sequence(Text(shape=(), dtype=string)),
    'referred_target': Text(shape=(), dtype=string),
    'situation': FeaturesDict({
        'agent_direction': int32,
        'agent_position': FeaturesDict({
            'column': int32,
            'row': int32,
        }),
        'direction_to_target': Text(shape=(), dtype=string),
        'distance_to_target': int32,
        'grid_size': int32,
        'placed_objects': Sequence({
            'object': FeaturesDict({
                'color': Text(shape=(), dtype=string),
                'shape': Text(shape=(), dtype=string),
                'size': int32,
            }),
            'position': FeaturesDict({
                'column': int32,
                'row': int32,
            }),
            'vector': Text(shape=(), dtype=string),
        }),
        'target_object': FeaturesDict({
            'object': FeaturesDict({
                'color': Text(shape=(), dtype=string),
                'shape': Text(shape=(), dtype=string),
                'size': int32,
            }),
            'position': FeaturesDict({
                'column': int32,
                'row': int32,
            }),
            'vector': Text(shape=(), dtype=string),
        }),
    }),
    'target_commands': Sequence(Text(shape=(), dtype=string)),
    'verb_in_command': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                                  | Class          | Shape   | Dtype  | Description
:--------------------------------------- | :------------- | :------ | :----- | :----------
                                         | FeaturesDict   |         |        |
command                                  | Sequence(Text) | (None,) | string |
manner                                   | Text           |         | string |
meaning                                  | Sequence(Text) | (None,) | string |
referred_target                          | Text           |         | string |
situation                                | FeaturesDict   |         |        |
situation/agent_direction                | Tensor         |         | int32  |
situation/agent_position                 | FeaturesDict   |         |        |
situation/agent_position/column          | Tensor         |         | int32  |
situation/agent_position/row             | Tensor         |         | int32  |
situation/direction_to_target            | Text           |         | string |
situation/distance_to_target             | Tensor         |         | int32  |
situation/grid_size                      | Tensor         |         | int32  |
situation/placed_objects                 | Sequence       |         |        |
situation/placed_objects/object          | FeaturesDict   |         |        |
situation/placed_objects/object/color    | Text           |         | string |
situation/placed_objects/object/shape    | Text           |         | string |
situation/placed_objects/object/size     | Tensor         |         | int32  |
situation/placed_objects/position        | FeaturesDict   |         |        |
situation/placed_objects/position/column | Tensor         |         | int32  |
situation/placed_objects/position/row    | Tensor         |         | int32  |
situation/placed_objects/vector          | Text           |         | string |
situation/target_object                  | FeaturesDict   |         |        |
situation/target_object/object           | FeaturesDict   |         |        |
situation/target_object/object/color     | Text           |         | string |
situation/target_object/object/shape     | Text           |         | string |
situation/target_object/object/size      | Tensor         |         | int32  |
situation/target_object/position         | FeaturesDict   |         |        |
situation/target_object/position/column  | Tensor         |         | int32  |
situation/target_object/position/row     | Tensor         |         | int32  |
situation/target_object/vector           | Text           |         | string |
target_commands                          | Sequence(Text) | (None,) | string |
verb_in_command                          | Text           |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{NEURIPS2020_e5a90182,
 author = {Ruis, Laura and Andreas, Jacob and Baroni, Marco and Bouchacourt, Diane and Lake, Brenden M},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {H. Larochelle and M. Ranzato and R. Hadsell and M. F. Balcan and H. Lin},
 pages = {19861--19872},
 publisher = {Curran Associates, Inc.},
 title = {A Benchmark for Systematic Generalization in Grounded Language Understanding},
 url = {https://proceedings.neurips.cc/paper/2020/file/e5a90182cc81e12ab5e72d66e0b46fe3-Paper.pdf},
 volume = {33},
 year = {2020}
}

@inproceedings{qiu-etal-2021-systematic,
    title = "Systematic Generalization on g{SCAN}: {W}hat is Nearly Solved and What is Next?",
    author = "Qiu, Linlu  and
      Hu, Hexiang  and
      Zhang, Bowen  and
      Shaw, Peter  and
      Sha, Fei",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.166",
    doi = "10.18653/v1/2021.emnlp-main.166",
    pages = "2180--2188",
}
```


## grounded_scan/compositional_splits (default config)

*   **Config description**: Examples for compositional generalization.

*   **Download size**: `82.10 MiB`

*   **Dataset size**: `998.11 MiB`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/grounded_scan-compositional_splits-2.0.0.html";
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

*   **Dataset size**: `546.73 MiB`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/grounded_scan-target_length_split-2.0.0.html";
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

## grounded_scan/spatial_relation_splits

*   **Config description**: Examples for spatial relation reasoning.

*   **Download size**: `89.59 MiB`

*   **Dataset size**: `675.09 MiB`

*   **Splits**:

Split                   | Examples
:---------------------- | -------:
`'dev'`                 | 2,617
`'referent'`            | 30,492
`'relation'`            | 6,285
`'relative_position_1'` | 41,576
`'relative_position_2'` | 41,529
`'test'`                | 28,526
`'train'`               | 259,088
`'visual'`              | 62,250

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/grounded_scan-spatial_relation_splits-2.0.0.html";
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