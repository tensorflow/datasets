<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="yes_no" />
  <meta itemprop="description" content="Sixty recordings of one individual saying yes or no in Hebrew; each recording is eight words long.&#10;&#10;The main point of the dataset is to provide an easy and fast way to test out the Kaldi scripts for free.&#10;&#10;The archive &quot;waves_yesno.tar.gz&quot; contains 60 .wav files, sampled at 8 kHz.&#10;All were recorded by the same male speaker, in Hebrew.&#10;In each file, the individual says 8 words; each word is either the Hebrew for &quot;yes&quot; or &quot;no&quot;,&#10;so each file is a random sequence of 8 yes-es or noes.&#10;There is no separate transcription provided; the sequence is encoded in the filename, with 1 for yes and 0 for no.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;yes_no&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/yes_no" />
  <meta itemprop="sameAs" content="https://www.openslr.org/1/" />
  <meta itemprop="citation" content="@ONLINE {YesNo,&#10;    author = &quot;Created for the Kaldi Project&quot;,&#10;    title  = &quot;YesNo&quot;,&#10;    url    = &quot;http://www.openslr.org/1/&quot;&#10;}" />
</div>

# `yes_no`


*   **Description**:

Sixty recordings of one individual saying yes or no in Hebrew; each recording is
eight words long.

The main point of the dataset is to provide an easy and fast way to test out the
Kaldi scripts for free.

The archive "waves_yesno.tar.gz" contains 60 .wav files, sampled at 8 kHz. All
were recorded by the same male speaker, in Hebrew. In each file, the individual
says 8 words; each word is either the Hebrew for "yes" or "no", so each file is
a random sequence of 8 yes-es or noes. There is no separate transcription
provided; the sequence is encoded in the filename, with 1 for yes and 0 for no.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/yesno">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://www.openslr.org/1/](https://www.openslr.org/1/)

*   **Source code**:
    [`tfds.audio.yesno.YesNo`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/yesno/yesno.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `4.49 MiB`

*   **Dataset size**: `16.27 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 60

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=int64),
    'audio/filename': Text(shape=(), dtype=string),
    'label': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=2)),
})
```

*   **Feature documentation**:

Feature        | Class                | Shape   | Dtype  | Description
:------------- | :------------------- | :------ | :----- | :----------
               | FeaturesDict         |         |        |
audio          | Audio                | (None,) | int64  |
audio/filename | Text                 |         | string |
label          | Sequence(ClassLabel) | (None,) | int64  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/yes_no-1.0.0.html";
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
@ONLINE {YesNo,
    author = "Created for the Kaldi Project",
    title  = "YesNo",
    url    = "http://www.openslr.org/1/"
}
```

