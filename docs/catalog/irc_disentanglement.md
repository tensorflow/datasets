<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="irc_disentanglement" />
  <meta itemprop="description" content="IRC Disentanglement dataset contains over 77,563 messages from Ubuntu IRC&#10;channel.&#10;&#10;Features include message id, message text and timestamp. Target is list of&#10;messages that current message replies to. Each record contains a list of&#10;messages from one day of IRC chat.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;irc_disentanglement&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/irc_disentanglement" />
  <meta itemprop="sameAs" content="https://jkk.name/irc-disentanglement" />
  <meta itemprop="citation" content="@InProceedings{acl19disentangle,&#10;  author    = {Jonathan K. Kummerfeld and Sai R. Gouravajhala and Joseph Peper and Vignesh Athreya and Chulaka Gunasekara and Jatin Ganhotra and Siva Sankalp Patel and Lazaros Polymenakos and Walter S. Lasecki},&#10;  title     = {A Large-Scale Corpus for Conversation Disentanglement},&#10;  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},&#10;  location  = {Florence, Italy},&#10;  month     = {July},&#10;  year      = {2019},&#10;  doi       = {10.18653/v1/P19-1374},&#10;  pages     = {3846--3856},&#10;  url       = {https://aclweb.org/anthology/papers/P/P19/P19-1374/},&#10;  arxiv     = {https://arxiv.org/abs/1810.11118},&#10;  software  = {https://jkk.name/irc-disentanglement},&#10;  data      = {https://jkk.name/irc-disentanglement},&#10;}" />
</div>

# `irc_disentanglement`


*   **Description**:

IRC Disentanglement dataset contains over 77,563 messages from Ubuntu IRC
channel.

Features include message id, message text and timestamp. Target is list of
messages that current message replies to. Each record contains a list of
messages from one day of IRC chat.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/irc-disentanglement">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://jkk.name/irc-disentanglement](https://jkk.name/irc-disentanglement)

*   **Source code**:
    [`tfds.datasets.irc_disentanglement.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/irc_disentanglement/irc_disentanglement_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): No release notes.

*   **Download size**: `113.53 MiB`

*   **Dataset size**: `26.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10
`'train'`      | 153
`'validation'` | 10

*   **Feature structure**:

```python
FeaturesDict({
    'day': Sequence({
        'id': Text(shape=(), dtype=string),
        'parents': Sequence(Text(shape=(), dtype=string)),
        'text': Text(shape=(), dtype=string),
        'timestamp': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature       | Class          | Shape   | Dtype  | Description
:------------ | :------------- | :------ | :----- | :----------
              | FeaturesDict   |         |        |
day           | Sequence       |         |        |
day/id        | Text           |         | string |
day/parents   | Sequence(Text) | (None,) | string |
day/text      | Text           |         | string |
day/timestamp | Text           |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/irc_disentanglement-2.0.0.html";
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
@InProceedings{acl19disentangle,
  author    = {Jonathan K. Kummerfeld and Sai R. Gouravajhala and Joseph Peper and Vignesh Athreya and Chulaka Gunasekara and Jatin Ganhotra and Siva Sankalp Patel and Lazaros Polymenakos and Walter S. Lasecki},
  title     = {A Large-Scale Corpus for Conversation Disentanglement},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  location  = {Florence, Italy},
  month     = {July},
  year      = {2019},
  doi       = {10.18653/v1/P19-1374},
  pages     = {3846--3856},
  url       = {https://aclweb.org/anthology/papers/P/P19/P19-1374/},
  arxiv     = {https://arxiv.org/abs/1810.11118},
  software  = {https://jkk.name/irc-disentanglement},
  data      = {https://jkk.name/irc-disentanglement},
}
```

