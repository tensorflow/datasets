<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="real_toxicity_prompts" />
  <meta itemprop="description" content="# RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models&#10;&#10;The RealToxicityPrompts is a corpus of English prompts (specifically sentence&#10;beginnings) of varying toxicity. These prompts are meant to be given as&#10;contexts to an autoregressive language model (ie. GPT-2) and used for&#10;generating completions.&#10;&#10;More details are presented in the original&#10;[paper](https://api.semanticscholar.org/CorpusID:221878771).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;real_toxicity_prompts&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/real_toxicity_prompts" />
  <meta itemprop="sameAs" content="https://github.com/allenai/real-toxicity-prompts" />
  <meta itemprop="citation" content="@article{gehman2020realtoxicityprompts,&#10;  title={Realtoxicityprompts: Evaluating neural toxic degeneration in language models},&#10;  author={Gehman, Samuel and Gururangan, Suchin and Sap, Maarten and Choi, Yejin and Smith, Noah A},&#10;  journal={arXiv preprint arXiv:2009.11462},&#10;  year={2020}&#10;}" />
</div>

# `real_toxicity_prompts`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

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
    Missing.

*   **Citation**:

```
@article{gehman2020realtoxicityprompts,
  title={Realtoxicityprompts: Evaluating neural toxic degeneration in language models},
  author={Gehman, Samuel and Gururangan, Suchin and Sap, Maarten and Choi, Yejin and Smith, Noah A},
  journal={arXiv preprint arXiv:2009.11462},
  year={2020}
}
```

