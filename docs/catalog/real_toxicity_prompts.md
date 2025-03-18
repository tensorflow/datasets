<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="real_toxicity_prompts" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/real_toxicity_prompts" />
  <meta itemprop="sameAs" content="https://github.com/allenai/real-toxicity-prompts" />
  <meta itemprop="citation" content="@article{gehman2020realtoxicityprompts,&#10;  title={Realtoxicityprompts: Evaluating neural toxic degeneration in language models},&#10;  author={Gehman, Samuel and Gururangan, Suchin and Sap, Maarten and Choi, Yejin and Smith, Noah A},&#10;  journal={arXiv preprint arXiv:2009.11462},&#10;  year={2020}&#10;}" />
</div>

# `real_toxicity_prompts`


*   **Description**:

# RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models

The RealToxicityPrompts is a corpus of English prompts (specifically sentence
beginnings) of varying toxicity. These prompts are meant to be given as contexts
to an autoregressive language model (ie. GPT-2) and used for generating
completions.

More details are presented in the original
[paper](https://api.semanticscholar.org/CorpusID:221878771).


*   **Homepage**:
    [https://github.com/allenai/real-toxicity-prompts](https://github.com/allenai/real-toxicity-prompts)

*   **Source code**:
    [`tfds.datasets.real_toxicity_prompts.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/real_toxicity_prompts/real_toxicity_prompts_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.46 GiB`

*   **Dataset size**: `81.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 99,442

*   **Feature structure**:

```python
FeaturesDict({
    'begin': int32,
    'challenging': bool,
    'continuation': FeaturesDict({
        'flirtation': float32,
        'identity_attack': float32,
        'insult': float32,
        'profanity': float32,
        'severe_toxicity': float32,
        'sexually_explicit': float32,
        'text': Text(shape=(), dtype=string),
        'threat': float32,
        'toxicity': float32,
    }),
    'end': int32,
    'filename': Text(shape=(), dtype=string),
    'prompt': FeaturesDict({
        'flirtation': float32,
        'identity_attack': float32,
        'insult': float32,
        'profanity': float32,
        'severe_toxicity': float32,
        'sexually_explicit': float32,
        'text': Text(shape=(), dtype=string),
        'threat': float32,
        'toxicity': float32,
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape | Dtype   | Description
:----------------------------- | :----------- | :---- | :------ | :----------
                               | FeaturesDict |       |         |
begin                          | Tensor       |       | int32   |
challenging                    | Tensor       |       | bool    |
continuation                   | FeaturesDict |       |         |
continuation/flirtation        | Tensor       |       | float32 |
continuation/identity_attack   | Tensor       |       | float32 |
continuation/insult            | Tensor       |       | float32 |
continuation/profanity         | Tensor       |       | float32 |
continuation/severe_toxicity   | Tensor       |       | float32 |
continuation/sexually_explicit | Tensor       |       | float32 |
continuation/text              | Text         |       | string  |
continuation/threat            | Tensor       |       | float32 |
continuation/toxicity          | Tensor       |       | float32 |
end                            | Tensor       |       | int32   |
filename                       | Text         |       | string  |
prompt                         | FeaturesDict |       |         |
prompt/flirtation              | Tensor       |       | float32 |
prompt/identity_attack         | Tensor       |       | float32 |
prompt/insult                  | Tensor       |       | float32 |
prompt/profanity               | Tensor       |       | float32 |
prompt/severe_toxicity         | Tensor       |       | float32 |
prompt/sexually_explicit       | Tensor       |       | float32 |
prompt/text                    | Text         |       | string  |
prompt/threat                  | Tensor       |       | float32 |
prompt/toxicity                | Tensor       |       | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/real_toxicity_prompts-1.0.0.html";
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
@article{gehman2020realtoxicityprompts,
  title={Realtoxicityprompts: Evaluating neural toxic degeneration in language models},
  author={Gehman, Samuel and Gururangan, Suchin and Sap, Maarten and Choi, Yejin and Smith, Noah A},
  journal={arXiv preprint arXiv:2009.11462},
  year={2020}
}
```

