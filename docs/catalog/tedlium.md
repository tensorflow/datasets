<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tedlium" />
  <meta itemprop="description" content="The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled&#10;at 16kHz. It contains about 118 hours of speech.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tedlium&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tedlium" />
  <meta itemprop="sameAs" content="https://www.openslr.org/7/" />
  <meta itemprop="citation" content="@inproceedings{rousseau2012tedlium,&#10;  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus},&#10;  author={Rousseau, Anthony and Del{\&#x27;e}glise, Paul and Est{\`e}ve, Yannick},&#10;  booktitle={Conference on Language Resources and Evaluation (LREC)},&#10;  pages={125--129},&#10;  year={2012}&#10;}" />
</div>

# `tedlium`


*   **Description**:

The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled
at 16kHz. It contains about 118 hours of speech.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/ted-lium-3">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Source code**:
    [`tfds.datasets.tedlium.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/tedlium/tedlium_dataset_builder.py)

*   **Versions**:

    *   **`1.0.1`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'gender': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'id': string,
    'speaker_id': string,
    'speech': Audio(shape=(None,), dtype=int64),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape   | Dtype  | Description
:--------- | :----------- | :------ | :----- | :----------
           | FeaturesDict |         |        |
gender     | ClassLabel   |         | int64  |
id         | Tensor       |         | string |
speaker_id | Tensor       |         | string |
speech     | Audio        | (None,) | int64  |
text       | Text         |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('speech', 'text')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{rousseau2012tedlium,
  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus},
  author={Rousseau, Anthony and Del{\'e}glise, Paul and Est{\`e}ve, Yannick},
  booktitle={Conference on Language Resources and Evaluation (LREC)},
  pages={125--129},
  year={2012}
}
```


## tedlium/release1 (default config)

*   **Config description**: The TED-LIUM corpus is English-language TED talks,
    with transcriptions, sampled at 16kHz. It contains about 118 hours of
    speech.

    ```
    This is the TED-LIUM corpus release 1,
    licensed under Creative Commons BY-NC-ND 3.0
    (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).
    ```

*   **Homepage**: [https://www.openslr.org/7/](https://www.openslr.org/7/)

*   **Download size**: `19.82 GiB`

*   **Dataset size**: `39.23 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,469
`'train'`      | 56,803
`'validation'` | 591

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tedlium-release1-1.0.1.html";
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

## tedlium/release2

*   **Config description**: This is the TED-LIUM corpus release 2, licensed
    under Creative Commons BY-NC-ND 3.0
    (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

    ```
    All talks and text are property of TED Conferences LLC.

    The TED-LIUM corpus was made from audio talks and their transcriptions
    available on the TED website. We have prepared and filtered these data
    in order to train acoustic models to participate to the International
    Workshop on Spoken Language Translation 2011 (the LIUM English/French
    SLT system reached the first rank in the SLT task).

    Contains 1495 talks and transcripts.
    ```

*   **Homepage**: [https://www.openslr.org/19/](https://www.openslr.org/19/)

*   **Download size**: `34.26 GiB`

*   **Dataset size**: `67.04 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,469
`'train'`      | 92,973
`'validation'` | 591

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tedlium-release2-1.0.1.html";
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

## tedlium/release3

*   **Config description**: This is the TED-LIUM corpus release 3, licensed
    under Creative Commons BY-NC-ND 3.0.

    ```
    All talks and text are property of TED Conferences LLC.

    This new TED-LIUM release was made through a collaboration between the
    Ubiqus company and the LIUM (University of Le Mans, France)

    Contents:

    - 2351 audio talks in NIST sphere format (SPH), including talks from
      TED-LIUM 2: be careful, same talks but not same audio files (only
      these audio file must be used with the TED-LIUM 3 STM files)
    - 452 hours of audio
    - 2351 aligned automatic transcripts in STM format
    - TEDLIUM 2 dev and test data: 19 TED talks in SPH format with
      corresponding manual transcriptions (cf. 'legacy' distribution below).
    - Dictionary with pronunciations (159848 entries), same file as the one
      included in TED-LIUM 2
    - Selected monolingual data for language modeling from WMT12 publicly
      available corpora: these files come from the TED-LIUM 2 release, but
      have been modified to get a tokenization more relevant for English
      language

    Two corpus distributions:
    - the legacy one, on which the dev and test datasets are the same as in
      TED-LIUM 2 (and TED-LIUM 1).
    - the 'speaker adaptation' one, especially designed for experiments on
      speaker adaptation.
    ```

*   **Homepage**: [https://www.openslr.org/51/](https://www.openslr.org/51/)

*   **Download size**: `50.59 GiB`

*   **Dataset size**: `145.67 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,469
`'train'`      | 268,263
`'validation'` | 591

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/tedlium-release3-1.0.1.html";
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