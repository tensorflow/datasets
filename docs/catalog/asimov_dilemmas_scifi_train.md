<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asimov_dilemmas_scifi_train" />
  <meta itemprop="description" content="Multiple-choice ethical questions (with desirable and undesirable answers) based on situations inspired from Science Fiction literature (training set).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asimov_dilemmas_scifi_train&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asimov_dilemmas_scifi_train" />
  <meta itemprop="sameAs" content="https://asimov-benchmark.github.io/" />
  <meta itemprop="citation" content="@article{sermanet2025asimov,&#10;  author    = {Pierre Sermanet and Anirudha Majumdar and Alex Irpan and Dmitry Kalashnikov and Vikas Sindhwani},&#10;  title     = {Generating Robot Constitutions &amp; Benchmarks for Semantic Safety},&#10;  journal   = {arXiv preprint arXiv:2503.08663},&#10;  url       = {https://arxiv.org/abs/2503.08663},&#10;  year      = {2025},&#10;}" />
</div>

# `asimov_dilemmas_scifi_train`


*   **Description**:

Multiple-choice ethical questions (with desirable and undesirable answers) based
on situations inspired from Science Fiction literature (training set).

*   **Homepage**:
    [https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)

*   **Source code**:
    [`tfds.robotics.asimov.AsimovDilemmasScifiTrain`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/asimov/asimov.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `425.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
`'val'` | 9,004

*   **Feature structure**:

```python
FeaturesDict({
    'acting_character': Text(shape=(), dtype=string),
    'characters': Text(shape=(), dtype=string),
    'possible_actions': Sequence({
        'action': Text(shape=(), dtype=string),
        'is_original_scifi_decision': bool,
        'key': Text(shape=(), dtype=string),
    }),
    'prompt_with_constitution': Text(shape=(), dtype=string),
    'prompt_with_constitution_antijailbreak': Text(shape=(), dtype=string),
    'prompt_with_constitution_antijailbreak_adversary': Text(shape=(), dtype=string),
    'prompt_with_constitution_antijailbreak_adversary_parts': Sequence(Text(shape=(), dtype=string)),
    'prompt_with_constitution_antijailbreak_parts': Sequence(Text(shape=(), dtype=string)),
    'prompt_with_constitution_parts': Sequence(Text(shape=(), dtype=string)),
    'prompt_without_constitution': Text(shape=(), dtype=string),
    'prompt_without_constitution_parts': Sequence(Text(shape=(), dtype=string)),
    'reference_domain': Text(shape=(), dtype=string),
    'reference_moment': Text(shape=(), dtype=string),
    'reference_scifi': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                                                | Class          | Shape   | Dtype  | Description
:----------------------------------------------------- | :------------- | :------ | :----- | :----------
                                                       | FeaturesDict   |         |        |
acting_character                                       | Text           |         | string |
characters                                             | Text           |         | string |
possible_actions                                       | Sequence       |         |        |
possible_actions/action                                | Text           |         | string |
possible_actions/is_original_scifi_decision            | Tensor         |         | bool   |
possible_actions/key                                   | Text           |         | string |
prompt_with_constitution                               | Text           |         | string |
prompt_with_constitution_antijailbreak                 | Text           |         | string |
prompt_with_constitution_antijailbreak_adversary       | Text           |         | string |
prompt_with_constitution_antijailbreak_adversary_parts | Sequence(Text) | (None,) | string |
prompt_with_constitution_antijailbreak_parts           | Sequence(Text) | (None,) | string |
prompt_with_constitution_parts                         | Sequence(Text) | (None,) | string |
prompt_without_constitution                            | Text           |         | string |
prompt_without_constitution_parts                      | Sequence(Text) | (None,) | string |
reference_domain                                       | Text           |         | string |
reference_moment                                       | Text           |         | string |
reference_scifi                                        | Text           |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asimov_dilemmas_scifi_train-0.1.0.html";
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

*   **Citation**:

```
@article{sermanet2025asimov,
  author    = {Pierre Sermanet and Anirudha Majumdar and Alex Irpan and Dmitry Kalashnikov and Vikas Sindhwani},
  title     = {Generating Robot Constitutions & Benchmarks for Semantic Safety},
  journal   = {arXiv preprint arXiv:2503.08663},
  url       = {https://arxiv.org/abs/2503.08663},
  year      = {2025},
}
```

