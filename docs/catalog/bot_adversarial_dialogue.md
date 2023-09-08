<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bot_adversarial_dialogue" />
  <meta itemprop="description" content="# Bot Adversarial Dialogue Dataset.&#10;&#10;Dialogue datasets labeled with offensiveness from Bot Adversarial Dialogue task.&#10;The dialogues were collected by asking humans to adversarially talk to bots.&#10;&#10;&#10;More details in the [paper](https://arxiv.org/abs/2010.07079).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bot_adversarial_dialogue&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bot_adversarial_dialogue" />
  <meta itemprop="sameAs" content="https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/bot_adversarial_dialogue" />
  <meta itemprop="citation" content="@misc{xu2021recipes,&#10;      title={Recipes for Safety in Open-domain Chatbots}, &#10;      author={Jing Xu and Da Ju and Margaret Li and Y-Lan Boureau and Jason Weston and Emily Dinan},&#10;      year={2021},&#10;      eprint={2010.07079},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}" />
</div>

# `bot_adversarial_dialogue`


*   **Description**:

# Bot Adversarial Dialogue Dataset.

Dialogue datasets labeled with offensiveness from Bot Adversarial Dialogue task.
The dialogues were collected by asking humans to adversarially talk to bots.

More details in the [paper](https://arxiv.org/abs/2010.07079).

*   **Homepage**:
    [https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/bot_adversarial_dialogue](https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/bot_adversarial_dialogue)

*   **Source code**:
    [`tfds.datasets.bot_adversarial_dialogue.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/bot_adversarial_dialogue/bot_adversarial_dialogue_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{xu2021recipes,
      title={Recipes for Safety in Open-domain Chatbots},
      author={Jing Xu and Da Ju and Margaret Li and Y-Lan Boureau and Jason Weston and Emily Dinan},
      year={2021},
      eprint={2010.07079},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


## bot_adversarial_dialogue/dialogue_datasets (default config)

*   **Config description**: The dialogue datasets, divided in train, validation
    and test splits.

*   **Download size**: `3.06 MiB`

*   **Dataset size**: `23.38 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,598
`'train'` | 69,274
`'valid'` | 7,002

*   **Feature structure**:

```python
FeaturesDict({
    'bot_persona': Sequence(Text(shape=(), dtype=string)),
    'dialogue_id': float32,
    'episode_done': bool,
    'id': Text(shape=(), dtype=string),
    'labels': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'round_id': float32,
    'speaker_to_eval': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

| Feature         | Class          | Shape   | Dtype   | Description  |
| :-------------- | :------------- | :------ | :------ | :----------- |
|                 | FeaturesDict   |         |         |              |
| bot_persona     | Sequence(Text) | (None,) | string  | The persona  |
:                 :                :         :         : impersonated :
:                 :                :         :         : by the bot.  :
| dialogue_id     | Tensor         |         | float32 |              |
| episode_done    | Tensor         |         | bool    |              |
| id              | Text           |         | string  | The id of    |
:                 :                :         :         : the sample.  :
| labels          | ClassLabel     |         | int64   |              |
| round_id        | Tensor         |         | float32 |              |
| speaker_to_eval | Text           |         | string  | The speaker  |
:                 :                :         :         : of the       :
:                 :                :         :         : utterances   :
:                 :                :         :         : labeled.     :
| text            | Text           |         | string  | The          |
:                 :                :         :         : utterance to :
:                 :                :         :         : classify.    :

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bot_adversarial_dialogue-dialogue_datasets-1.0.0.html";
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

## bot_adversarial_dialogue/human_nonadv_safety_eval

*   **Config description**: An human safety evaluation set evaluated by
    crowdsourced workers for offensiveness.

*   **Download size**: `10.57 KiB`

*   **Dataset size**: `34.55 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 180

*   **Feature structure**:

```python
FeaturesDict({
    'episode_done': bool,
    'id': Text(shape=(), dtype=string),
    'labels': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature      | Class        | Shape | Dtype  | Description
:----------- | :----------- | :---- | :----- | :-------------------------
             | FeaturesDict |       |        |
episode_done | Tensor       |       | bool   |
id           | Text         |       | string | The id of the sample.
labels       | ClassLabel   |       | int64  |
text         | Text         |       | string | The utterance to classify.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bot_adversarial_dialogue-human_nonadv_safety_eval-1.0.0.html";
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