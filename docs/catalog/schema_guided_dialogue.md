<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="schema_guided_dialogue" />
  <meta itemprop="description" content="The Schema-Guided Dialogue (SGD) dataset consists of over 20k annotated&#10;multi-domain, task-oriented conversations between a human and a virtual&#10;assistant. These conversations involve interactions with services and APIs&#10;spanning 20 domains, ranging from banks and events to media, calendar, travel,&#10;and weather. For most of these domains, the dataset contains multiple different&#10;APIs, many of which have overlapping functionalities but different interfaces,&#10;which reflects common real-world scenarios. The wide range of available&#10;annotations can be used for intent prediction, slot filling, dialogue state&#10;tracking, policy imitation learning, language generation, user simulation&#10;learning, among other tasks in large-scale virtual assistants. Besides these,&#10;the dataset has unseen domains and services in the evaluation set to quantify&#10;the performance in zero-shot or few shot settings.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;schema_guided_dialogue&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/schema_guided_dialogue" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/dstc8-schema-guided-dialogue" />
  <meta itemprop="citation" content="@article{rastogi2019towards,&#10;  title={Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset},&#10;  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},&#10;  journal={arXiv preprint arXiv:1909.05855},&#10;  year={2019}&#10;}" />
</div>

# `schema_guided_dialogue`


*   **Description**:

The Schema-Guided Dialogue (SGD) dataset consists of over 20k annotated
multi-domain, task-oriented conversations between a human and a virtual
assistant. These conversations involve interactions with services and APIs
spanning 20 domains, ranging from banks and events to media, calendar, travel,
and weather. For most of these domains, the dataset contains multiple different
APIs, many of which have overlapping functionalities but different interfaces,
which reflects common real-world scenarios. The wide range of available
annotations can be used for intent prediction, slot filling, dialogue state
tracking, policy imitation learning, language generation, user simulation
learning, among other tasks in large-scale virtual assistants. Besides these,
the dataset has unseen domains and services in the evaluation set to quantify
the performance in zero-shot or few shot settings.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/sgd">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/google-research-datasets/dstc8-schema-guided-dialogue](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)

*   **Source code**:
    [`tfds.datasets.schema_guided_dialogue.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/schema_guided_dialogue/schema_guided_dialogue_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `35.12 MiB`

*   **Dataset size**: `25.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,482
`'test'`  | 4,201
`'train'` | 16,142

*   **Feature structure**:

```python
FeaturesDict({
    'first_speaker': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'metadata': FeaturesDict({
        'services': Sequence({
            'name': string,
        }),
    }),
    'utterances': Sequence(Text(shape=(), dtype=string)),
})
```

*   **Feature documentation**:

Feature                | Class          | Shape   | Dtype  | Description
:--------------------- | :------------- | :------ | :----- | :----------
                       | FeaturesDict   |         |        |
first_speaker          | ClassLabel     |         | int64  |
metadata               | FeaturesDict   |         |        |
metadata/services      | Sequence       |         |        |
metadata/services/name | Tensor         |         | string |
utterances             | Sequence(Text) | (None,) | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/schema_guided_dialogue-1.0.0.html";
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
@article{rastogi2019towards,
  title={Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset},
  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
  journal={arXiv preprint arXiv:1909.05855},
  year={2019}
}
```

