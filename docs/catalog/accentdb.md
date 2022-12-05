<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="accentdb" />
  <meta itemprop="description" content="AccentDB is a multi-pairwise parallel corpus of structured and labelled accented&#10;speech. It contains speech samples from speakers of 4 non-native accents of&#10;English (8 speakers, 4 Indian languages); and also has a compilation of 4 native&#10;accents of English (4 countries, 13 speakers) and a metropolitan Indian accent&#10;(2 speakers). The dataset available here corresponds to release titled&#10;accentdb_extended on https://accentdb.github.io/#dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;accentdb&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/accentdb" />
  <meta itemprop="sameAs" content="https://accentdb.github.io/" />
  <meta itemprop="citation" content="@InProceedings{ahamad-anand-bhargava:2020:LREC,&#10;  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},&#10;  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},&#10;  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},&#10;  month          = {May},&#10;  year           = {2020},&#10;  address        = {Marseille, France},&#10;  publisher      = {European Language Resources Association},&#10;  pages     = {5353--5360},&#10;  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}&#10;}" />
</div>

# `accentdb`


*   **Description**:

AccentDB is a multi-pairwise parallel corpus of structured and labelled accented
speech. It contains speech samples from speakers of 4 non-native accents of
English (8 speakers, 4 Indian languages); and also has a compilation of 4 native
accents of English (4 countries, 13 speakers) and a metropolitan Indian accent
(2 speakers). The dataset available here corresponds to release titled
accentdb_extended on https://accentdb.github.io/#dataset.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/accentdb">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://accentdb.github.io/](https://accentdb.github.io/)

*   **Source code**:
    [`tfds.datasets.accentdb.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/accentdb/accentdb_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `3.56 GiB`

*   **Dataset size**: `19.47 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 17,313

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=int64),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=9),
    'speaker_id': string,
})
```

*   **Feature documentation**:

Feature    | Class        | Shape   | Dtype  | Description
:--------- | :----------- | :------ | :----- | :----------
           | FeaturesDict |         |        |
audio      | Audio        | (None,) | int64  |
label      | ClassLabel   |         | int64  |
speaker_id | Tensor       |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/accentdb-1.0.0.html";
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
@InProceedings{ahamad-anand-bhargava:2020:LREC,
  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},
  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},
  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},
  month          = {May},
  year           = {2020},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5353--5360},
  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}
}
```

