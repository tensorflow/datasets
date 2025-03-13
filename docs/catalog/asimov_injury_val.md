<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asimov_injury_val" />
  <meta itemprop="description" content="Situations generated from real hospital injury reports (validation set).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asimov_injury_val&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asimov_injury_val" />
  <meta itemprop="sameAs" content="https://asimov-benchmark.github.io/" />
  <meta itemprop="citation" content="@article{sermanet2025asimov,&#10;  author    = {Pierre Sermanet and Anirudha Majumdar and Alex Irpan and Dmitry Kalashnikov and Vikas Sindhwani},&#10;  title     = {Generating Robot Constitutions &amp; Benchmarks for Semantic Safety},&#10;  journal   = {arXiv preprint arXiv:2503.08663},&#10;  url       = {https://arxiv.org/abs/2503.08663},&#10;  year      = {2025},&#10;}" />
</div>

# `asimov_injury_val`


*   **Description**:

Situations generated from real hospital injury reports (validation set).

*   **Homepage**:
    [https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)

*   **Source code**:
    [`tfds.robotics.asimov.AsimovInjuryVal`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/asimov/asimov.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `5.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split   | Examples
:------ | -------:
`'val'` | 304

*   **Feature structure**:

```python
FeaturesDict({
    'context': Text(shape=(), dtype=string),
    'context_input_data': FeaturesDict({
        'Age': int32,
        'Alcohol': float32,
        'Body_Part': float32,
        'Body_Part_2': float32,
        'CPSC_Case_Number': Text(shape=(), dtype=string),
        'Diagnosis': float32,
        'Diagnosis_2': float32,
        'Disposition': float32,
        'Drug': float32,
        'Fire_Involvement': float32,
        'Gender': float32,
        'Hispanic': float32,
        'Location': float32,
        'Narrative_1': Text(shape=(), dtype=string),
        'Other_Diagnosis': Text(shape=(), dtype=string),
        'Other_Diagnosis_2': Text(shape=(), dtype=string),
        'Other_Race': Text(shape=(), dtype=string),
        'PSU': float32,
        'Product_1': float32,
        'Product_2': float32,
        'Product_3': float32,
        'Race': float32,
        'Stratum': Text(shape=(), dtype=string),
        'Treatment_Date': Text(shape=(), dtype=string),
        'Weight': float32,
    }),
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
})
```

*   **Feature documentation**:

Feature                                                                 | Class          | Shape   | Dtype   | Description
:---------------------------------------------------------------------- | :------------- | :------ | :------ | :----------
                                                                        | FeaturesDict   |         |         |
context                                                                 | Text           |         | string  |
context_input_data                                                      | FeaturesDict   |         |         |
context_input_data/Age                                                  | Tensor         |         | int32   |
context_input_data/Alcohol                                              | Tensor         |         | float32 |
context_input_data/Body_Part                                            | Tensor         |         | float32 |
context_input_data/Body_Part_2                                          | Tensor         |         | float32 |
context_input_data/CPSC_Case_Number                                     | Text           |         | string  |
context_input_data/Diagnosis                                            | Tensor         |         | float32 |
context_input_data/Diagnosis_2                                          | Tensor         |         | float32 |
context_input_data/Disposition                                          | Tensor         |         | float32 |
context_input_data/Drug                                                 | Tensor         |         | float32 |
context_input_data/Fire_Involvement                                     | Tensor         |         | float32 |
context_input_data/Gender                                               | Tensor         |         | float32 |
context_input_data/Hispanic                                             | Tensor         |         | float32 |
context_input_data/Location                                             | Tensor         |         | float32 |
context_input_data/Narrative_1                                          | Text           |         | string  |
context_input_data/Other_Diagnosis                                      | Text           |         | string  |
context_input_data/Other_Diagnosis_2                                    | Text           |         | string  |
context_input_data/Other_Race                                           | Text           |         | string  |
context_input_data/PSU                                                  | Tensor         |         | float32 |
context_input_data/Product_1                                            | Tensor         |         | float32 |
context_input_data/Product_2                                            | Tensor         |         | float32 |
context_input_data/Product_3                                            | Tensor         |         | float32 |
context_input_data/Race                                                 | Tensor         |         | float32 |
context_input_data/Stratum                                              | Text           |         | string  |
context_input_data/Treatment_Date                                       | Text           |         | string  |
context_input_data/Weight                                               | Tensor         |         | float32 |
instruction                                                             | Text           |         | string  |
prompt_with_constitution                                                | Text           |         | string  |
prompt_with_constitution_chain_of_thought                               | Text           |         | string  |
prompt_with_constitution_chain_of_thought_antijailbreak                 | Text           |         | string  |
prompt_with_constitution_chain_of_thought_antijailbreak_adversary       | Text           |         | string  |
prompt_with_constitution_chain_of_thought_antijailbreak_adversary_parts | Sequence(Text) | (None,) | string  |
prompt_with_constitution_chain_of_thought_antijailbreak_parts           | Sequence(Text) | (None,) | string  |
prompt_with_constitution_chain_of_thought_parts                         | Sequence(Text) | (None,) | string  |
prompt_with_constitution_parts                                          | Sequence(Text) | (None,) | string  |
prompt_without_constitution                                             | Text           |         | string  |
prompt_without_constitution_parts                                       | Sequence(Text) | (None,) | string  |
undesirable_groundtruth_answer                                          | Tensor         |         | bool    |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asimov_injury_val-0.1.0.html";
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

