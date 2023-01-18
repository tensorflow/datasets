<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="unnatural_instructions" />
  <meta itemprop="description" content="Dataset described in the paper: Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor (2022).&#10;Contains sets of natural-language instructions, with optional constraints / LLM-generated reformulations.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;unnatural_instructions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/unnatural_instructions" />
  <meta itemprop="sameAs" content="https://github.com/orhonovich/unnatural-instructions" />
  <meta itemprop="citation" content="@misc{honovich2022unnatural,&#10;      title = {Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor},&#10;      author = {Honovich, Or and Scialom, Thomas and Levy, Omer and Schick, Timo},&#10;      url = {https://arxiv.org/abs/2212.09689},&#10;      publisher = {arXiv},&#10;      year={2022}&#10;}" />
</div>

# `unnatural_instructions`


*   **Description**:

Dataset described in the paper: Unnatural Instructions: Tuning Language Models
with (Almost) No Human Labor (2022). Contains sets of natural-language
instructions, with optional constraints / LLM-generated reformulations.

*   **Homepage**:
    [https://github.com/orhonovich/unnatural-instructions](https://github.com/orhonovich/unnatural-instructions)

*   **Source code**:
    [`tfds.text.unnatural_instructions.UnnaturalInstructions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/unnatural_instructions/unnatural_instructions.py)

*   **Versions**:

    *   **`0.0.1`** (default): Initial release. Omit instructions / inputs, as
        they require additional processing to be used. Instruction_with_inputs
        and reformulations contain instructions and contexts.

*   **Download size**: `17.48 MiB`

*   **Dataset size**: `154.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 66,010

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'instances': Sequence({
        'constraints': Text(shape=(), dtype=string),
        'input': Text(shape=(), dtype=string),
        'instruction_with_input': Text(shape=(), dtype=string),
        'output': Text(shape=(), dtype=string),
    }),
    'instruction': Text(shape=(), dtype=string),
    'reformulations': Sequence({
        'input': Text(shape=(), dtype=string),
        'instruction': Text(shape=(), dtype=string),
        'instruction_with_input': Text(shape=(), dtype=string),
        'output': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                               | Class        | Shape | Dtype  | Description
:------------------------------------ | :----------- | :---- | :----- | :----------
                                      | FeaturesDict |       |        |
id                                    | Text         |       | string | Unique identifier for example.
instances                             | Sequence     |       |        |
instances/constraints                 | Text         |       | string | Task-specific constraints.
instances/input                       | Text         |       | string | Input to be fed into placeholders for given instruction.
instances/instruction_with_input      | Text         |       | string | Instructions with inputs supplied to placeholders.
instances/output                      | Text         |       | string | Target output for given task.
instruction                           | Text         |       | string | Instruction with placeholder for inputs.
reformulations                        | Sequence     |       |        |
reformulations/input                  | Text         |       | string | Input to be fed into placeholders for given instruction.
reformulations/instruction            | Text         |       | string | Instruction with placeholder for inputs.
reformulations/instruction_with_input | Text         |       | string | Instructions with inputs supplied to placeholders.
reformulations/output                 | Text         |       | string | Target output for given task.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unnatural_instructions-0.0.1.html";
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
@misc{honovich2022unnatural,
      title = {Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor},
      author = {Honovich, Or and Scialom, Thomas and Levy, Omer and Schick, Timo},
      url = {https://arxiv.org/abs/2212.09689},
      publisher = {arXiv},
      year={2022}
}
```

