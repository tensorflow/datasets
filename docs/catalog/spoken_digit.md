<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="spoken_digit" />
  <meta itemprop="description" content="A free audio dataset of spoken digits. Think MNIST for audio.&#10;&#10;A simple audio/speech dataset consisting of recordings of spoken digits in wav&#10;files at 8kHz.&#10;The recordings are trimmed so that they have near minimal silence at the&#10;beginnings and ends.&#10;&#10;5 speakers\&#10;2,500 recordings (50 of each digit per speaker)\&#10;English pronunciations&#10;&#10;Files are named in the following format: {digitLabel}_{speakerName}_{index}.wav&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;spoken_digit&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/spoken_digit" />
  <meta itemprop="sameAs" content="https://github.com/Jakobovski/free-spoken-digit-dataset" />
  <meta itemprop="citation" content="@ONLINE {Free Spoken Digit Dataset,&#10;    author = &quot;Zohar Jackson&quot;,&#10;    title  = &quot;Spoken_Digit&quot;,&#10;    year   = &quot;2016&quot;,&#10;    url    = &quot;https://github.com/Jakobovski/free-spoken-digit-dataset&quot;&#10;}" />
</div>

# `spoken_digit`


*   **Description**:

A free audio dataset of spoken digits. Think MNIST for audio.

A simple audio/speech dataset consisting of recordings of spoken digits in wav
files at 8kHz. The recordings are trimmed so that they have near minimal silence
at the beginnings and ends.

5 speakers \
2,500 recordings (50 of each digit per speaker) \
English pronunciations

Files are named in the following format: {digitLabel}_{speakerName}_{index}.wav

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/fsdd">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/Jakobovski/free-spoken-digit-dataset](https://github.com/Jakobovski/free-spoken-digit-dataset)

*   **Source code**:
    [`tfds.datasets.spoken_digit.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/spoken_digit/spoken_digit_dataset_builder.py)

*   **Versions**:

    *   **`1.0.9`** (default): No release notes.

*   **Download size**: `11.42 MiB`

*   **Dataset size**: `45.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,500

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=int64),
    'audio/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=10),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape   | Dtype  | Description
:------------- | :----------- | :------ | :----- | :----------
               | FeaturesDict |         |        |
audio          | Audio        | (None,) | int64  |
audio/filename | Text         |         | string |
label          | ClassLabel   |         | int64  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/spoken_digit-1.0.9.html";
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
@ONLINE {Free Spoken Digit Dataset,
    author = "Zohar Jackson",
    title  = "Spoken_Digit",
    year   = "2016",
    url    = "https://github.com/Jakobovski/free-spoken-digit-dataset"
}
```

