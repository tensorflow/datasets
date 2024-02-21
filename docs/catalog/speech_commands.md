<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="speech_commands" />
  <meta itemprop="description" content="An audio dataset of spoken words designed to help train and evaluate keyword&#10;spotting systems. Its primary goal is to provide a way to build and test small&#10;models that detect when a single word is spoken, from a set of ten target words,&#10;with as few false positives as possible from background noise or unrelated&#10;speech. Note that in the train and validation set, the label &quot;unknown&quot; is much&#10;more prevalent than the labels of the target words or background noise. One&#10;difference from the release version is the handling of silent segments. While in&#10;the test set the silence segments are regular 1 second files, in the training&#10;they are provided as long segments under &quot;background_noise&quot; folder. Here we&#10;split these background noise into 1 second clips, and also keep one of the files&#10;for the validation set.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;speech_commands&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/speech_commands" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/1804.03209" />
  <meta itemprop="citation" content="@article{speechcommandsv2,&#10;   author = {{Warden}, P.},&#10;    title = &quot;{Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition}&quot;,&#10;  journal = {ArXiv e-prints},&#10;  archivePrefix = &quot;arXiv&quot;,&#10;  eprint = {1804.03209},&#10;  primaryClass = &quot;cs.CL&quot;,&#10;  keywords = {Computer Science - Computation and Language, Computer Science - Human-Computer Interaction},&#10;    year = 2018,&#10;    month = apr,&#10;    url = {https://arxiv.org/abs/1804.03209},&#10;}" />
</div>

# `speech_commands`


*   **Description**:

An audio dataset of spoken words designed to help train and evaluate keyword
spotting systems. Its primary goal is to provide a way to build and test small
models that detect when a single word is spoken, from a set of ten target words,
with as few false positives as possible from background noise or unrelated
speech. Note that in the train and validation set, the label "unknown" is much
more prevalent than the labels of the target words or background noise. One
difference from the release version is the handling of silent segments. While in
the test set the silence segments are regular 1 second files, in the training
they are provided as long segments under "background_noise" folder. Here we
split these background noise into 1 second clips, and also keep one of the files
for the validation set.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/speech-commands">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://arxiv.org/abs/1804.03209](https://arxiv.org/abs/1804.03209)

*   **Source code**:
    [`tfds.datasets.speech_commands.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/speech_commands/speech_commands_dataset_builder.py)

*   **Versions**:

    *   **`0.0.3`** (default): Fix audio data type with dtype=tf.int16.

*   **Download size**: `2.37 GiB`

*   **Dataset size**: `8.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,890
`'train'`      | 85,511
`'validation'` | 10,102

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=int16),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=12),
})
```

*   **Feature documentation**:

Feature | Class        | Shape   | Dtype | Description
:------ | :----------- | :------ | :---- | :----------
        | FeaturesDict |         |       |
audio   | Audio        | (None,) | int16 |
label   | ClassLabel   |         | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'label')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/speech_commands-0.0.3.html";
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
@article{speechcommandsv2,
   author = {{Warden}, P.},
    title = "{Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition}",
  journal = {ArXiv e-prints},
  archivePrefix = "arXiv",
  eprint = {1804.03209},
  primaryClass = "cs.CL",
  keywords = {Computer Science - Computation and Language, Computer Science - Human-Computer Interaction},
    year = 2018,
    month = apr,
    url = {https://arxiv.org/abs/1804.03209},
}
```

