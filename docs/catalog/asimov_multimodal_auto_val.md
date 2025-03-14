<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asimov_multimodal_auto_val" />
  <meta itemprop="description" content="(Image, context, instruction) triplets generated from real images (from RoboVQA dataset) which are modified to contain undesirable elements, generated instructions can be desirable or undesirable (validation set).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asimov_multimodal_auto_val&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asimov_multimodal_auto_val" />
  <meta itemprop="sameAs" content="https://asimov-benchmark.github.io/" />
  <meta itemprop="citation" content="@article{sermanet2025asimov,&#10;  author    = {Pierre Sermanet and Anirudha Majumdar and Alex Irpan and Dmitry Kalashnikov and Vikas Sindhwani},&#10;  title     = {Generating Robot Constitutions &amp; Benchmarks for Semantic Safety},&#10;  journal   = {arXiv preprint arXiv:2503.08663},&#10;  url       = {https://arxiv.org/abs/2503.08663},&#10;  year      = {2025},&#10;}" />
</div>

# `asimov_multimodal_auto_val`


*   **Description**:

(Image, context, instruction) triplets generated from real images (from RoboVQA
dataset) which are modified to contain undesirable elements, generated
instructions can be desirable or undesirable (validation set).

*   **Homepage**:
    [https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)

*   **Source code**:
    [`tfds.robotics.asimov.AsimovMultimodalAutoVal`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/asimov/asimov.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `29.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
`'val'` | 50

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'instructions': Sequence({
        'context': Text(shape=(), dtype=string),
        'instruction': Text(shape=(), dtype=string),
        'prompt_with_constitution': Text(shape=(), dtype=string),
        'prompt_with_constitution_chain_of_thought': Text(shape=(), dtype=string),
        'prompt_with_constitution_chain_of_thought_antijailbreak': Text(shape=(), dtype=string),
        'prompt_with_constitution_chain_of_thought_antijailbreak_adversary': Text(shape=(), dtype=string),
        'prompt_with_constitution_chain_of_thought_antijailbreak_adversary_parts': Sequence(Text(shape=(), dtype=string)),
        'prompt_with_constitution_chain_of_thought_antijailbreak_parts': Sequence(Text(shape=(), dtype=string)),
        'prompt_with_constitution_chain_of_thought_parts': Sequence(Text(shape=(), dtype=string)),
        'prompt_with_constitution_parts': Sequence(Text(shape=(), dtype=string)),
        'prompt_without_constitution': Text(shape=(), dtype=string),
        'prompt_without_constitution_parts': Sequence(Text(shape=(), dtype=string)),
        'undesirable_groundtruth_answer': bool,
    }),
    'original_image': Image(shape=(None, None, 3), dtype=uint8),
})
```

*   **Feature documentation**:

Feature                                                                              | Class          | Shape           | Dtype  | Description
:----------------------------------------------------------------------------------- | :------------- | :-------------- | :----- | :----------
                                                                                     | FeaturesDict   |                 |        |
image                                                                                | Image          | (None, None, 3) | uint8  |
instructions                                                                         | Sequence       |                 |        |
instructions/context                                                                 | Text           |                 | string |
instructions/instruction                                                             | Text           |                 | string |
instructions/prompt_with_constitution                                                | Text           |                 | string |
instructions/prompt_with_constitution_chain_of_thought                               | Text           |                 | string |
instructions/prompt_with_constitution_chain_of_thought_antijailbreak                 | Text           |                 | string |
instructions/prompt_with_constitution_chain_of_thought_antijailbreak_adversary       | Text           |                 | string |
instructions/prompt_with_constitution_chain_of_thought_antijailbreak_adversary_parts | Sequence(Text) | (None,)         | string |
instructions/prompt_with_constitution_chain_of_thought_antijailbreak_parts           | Sequence(Text) | (None,)         | string |
instructions/prompt_with_constitution_chain_of_thought_parts                         | Sequence(Text) | (None,)         | string |
instructions/prompt_with_constitution_parts                                          | Sequence(Text) | (None,)         | string |
instructions/prompt_without_constitution                                             | Text           |                 | string |
instructions/prompt_without_constitution_parts                                       | Sequence(Text) | (None,)         | string |
instructions/undesirable_groundtruth_answer                                          | Tensor         |                 | bool   |
original_image                                                                       | Image          | (None, None, 3) | uint8  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asimov_multimodal_auto_val-0.1.0.html";
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

