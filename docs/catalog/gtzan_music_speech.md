<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gtzan_music_speech" />
  <meta itemprop="description" content="The dataset was collected for the purposes of music/speech discrimination.&#10;The dataset consists of 120 tracks, each 30 seconds long.&#10;Each class (music/speech) has 60 examples.&#10;The tracks are all 22050Hz Mono 16-bit audio files in .wav format.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gtzan_music_speech&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gtzan_music_speech" />
  <meta itemprop="sameAs" content="http://marsyas.info/index.html" />
  <meta itemprop="citation" content="@ONLINE {Music Speech,&#10;    author = &quot;Tzanetakis, George&quot;,&#10;    title  = &quot;GTZAN Music/Speech Collection&quot;,&#10;    year   = &quot;1999&quot;,&#10;    url    = &quot;http://marsyas.info/index.html&quot;&#10;}" />
</div>

# `gtzan_music_speech`


*   **Description**:

The dataset was collected for the purposes of music/speech discrimination. The
dataset consists of 120 tracks, each 30 seconds long. Each class (music/speech)
has 60 examples. The tracks are all 22050Hz Mono 16-bit audio files in .wav
format.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/gtzan-music-speech">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://marsyas.info/index.html](http://marsyas.info/index.html)

*   **Source code**:
    [`tfds.audio.gtzan_music_speech.GTZANMusicSpeech`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/gtzan_music_speech/gtzan_music_speech.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `283.29 MiB`

*   **Dataset size**: `424.64 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 128

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=int64),
    'audio/filename': Text(shape=(), dtype=string),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gtzan_music_speech-1.0.0.html";
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
@ONLINE {Music Speech,
    author = "Tzanetakis, George",
    title  = "GTZAN Music/Speech Collection",
    year   = "1999",
    url    = "http://marsyas.info/index.html"
}
```

