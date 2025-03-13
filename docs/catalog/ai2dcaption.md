<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ai2dcaption" />
  <meta itemprop="description" content="This dataset is primarily based off the AI2D Dataset (see [here](&#10;  https://prior.allenai.org/projects/diagram-understanding)).&#10;&#10;See [Section 4.1](https://arxiv.org/pdf/2310.12128) of our paper for&#10; the AI2D-Caption dataset annotation process.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ai2dcaption&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/ai2dcaption-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ai2dcaption" />
  <meta itemprop="sameAs" content="https://huggingface.co/datasets/abhayzala/AI2D-Caption" />
  <meta itemprop="citation" content="@inproceedings{Zala2024DiagrammerGPT,&#10;        author = {Abhay Zala and Han Lin and Jaemin Cho and Mohit Bansal},&#10;        title = {DiagrammerGPT: Generating Open-Domain, Open-Platform Diagrams via LLM Planning},&#10;        year = {2024},&#10;        booktitle = {COLM},&#10;}" />
</div>

# `ai2dcaption`


*   **Description**:

This dataset is primarily based off the AI2D Dataset (see
[here](https://prior.allenai.org/projects/diagram-understanding)).

See [Section 4.1](https://arxiv.org/pdf/2310.12128) of our paper for the
AI2D-Caption dataset annotation process.

*   **Homepage**:
    [https://huggingface.co/datasets/abhayzala/AI2D-Caption](https://huggingface.co/datasets/abhayzala/AI2D-Caption)

*   **Source code**:
    [`tfds.datasets.ai2dcaption.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/ai2dcaption/ai2dcaption_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `2.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split                             | Examples
:-------------------------------- | -------:
`'auditor_llm_training_examples'` | 30
`'gpt4v'`                         | 4,903
`'llava_15'`                      | 4,902
`'planner_llm_training_examples'` | 30
`'test'`                          | 75

*   **Feature structure**:

```python
FeaturesDict({
    'caption': Text(shape=(), dtype=string),
    'entities': Sequence({
        'bounds': BBoxFeature(shape=(4,), dtype=float32),
        'cat': ClassLabel(shape=(), dtype=int64, num_classes=10),
        'from': Text(shape=(), dtype=string),
        'id': Text(shape=(), dtype=string),
        'label': Text(shape=(), dtype=string),
        'to': Text(shape=(), dtype=string),
        'type': ClassLabel(shape=(), dtype=int64, num_classes=5),
    }),
    'image': Image(shape=(None, None, 3), dtype=uint8, description=The image of the diagram.),
    'image_filename': Text(shape=(), dtype=string),
    'layout': ClassLabel(shape=(), dtype=int64, num_classes=7),
    'relationships': Sequence(Text(shape=(), dtype=string)),
    'topic': ClassLabel(shape=(), dtype=int64, num_classes=4),
})
```

*   **Feature documentation**:

| Feature         | Class          | Shape        | Dtype   | Description      |
| :-------------- | :------------- | :----------- | :------ | :--------------- |
|                 | FeaturesDict   |              |         |                  |
| caption         | Text           |              | string  |                  |
| entities        | Sequence       |              |         |                  |
| entities/bounds | BBoxFeature    | (4,)         | float32 |                  |
| entities/cat    | ClassLabel     |              | int64   |                  |
| entities/from   | Text           |              | string  |                  |
| entities/id     | Text           |              | string  |                  |
| entities/label  | Text           |              | string  |                  |
| entities/to     | Text           |              | string  |                  |
| entities/type   | ClassLabel     |              | int64   |                  |
| image           | Image          | (None, None, | uint8   | The image of the |
:                 :                : 3)           :         : diagram.         :
| image_filename  | Text           |              | string  | Image filename.  |
:                 :                :              :         : e.g. "1337.png"  :
| layout          | ClassLabel     |              | int64   |                  |
| relationships   | Sequence(Text) | (None,)      | string  |                  |
| topic           | ClassLabel     |              | int64   |                  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ai2dcaption-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ai2dcaption-1.0.0.html";
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
@inproceedings{Zala2024DiagrammerGPT,
        author = {Abhay Zala and Han Lin and Jaemin Cho and Mohit Bansal},
        title = {DiagrammerGPT: Generating Open-Domain, Open-Platform Diagrams via LLM Planning},
        year = {2024},
        booktitle = {COLM},
}
```

