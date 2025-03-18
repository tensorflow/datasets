<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="summscreen" />
  <meta itemprop="description" content="SummScreen Summarization dataset, non-anonymized, non-tokenized version.&#10;&#10;Train/val/test splits and filtering are based on the final tokenized dataset,&#10;but transcripts and recaps provided are based on the untokenized text.&#10;&#10;There are two features:&#10;&#10;-   transcript: Full episode transcripts, each line of dialogue separated by&#10;    newlines&#10;-   recap: Recaps or summaries of episodes&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;summscreen&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/summscreen" />
  <meta itemprop="sameAs" content="https://github.com/mingdachen/SummScreen" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-2104-07091,&#10;  author    = {Mingda Chen and&#10;               Zewei Chu and&#10;               Sam Wiseman and&#10;               Kevin Gimpel},&#10;  title     = {SummScreen: {A} Dataset for Abstractive Screenplay Summarization},&#10;  journal   = {CoRR},&#10;  volume    = {abs/2104.07091},&#10;  year      = {2021},&#10;  url       = {https://arxiv.org/abs/2104.07091},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {2104.07091},&#10;  timestamp = {Mon, 19 Apr 2021 16:45:47 +0200},&#10;  biburl    = {https://dblp.org/rec/journals/corr/abs-2104-07091.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `summscreen`


*   **Description**:

SummScreen Summarization dataset, non-anonymized, non-tokenized version.

Train/val/test splits and filtering are based on the final tokenized dataset,
but transcripts and recaps provided are based on the untokenized text.

There are two features:

-   transcript: Full episode transcripts, each line of dialogue separated by
    newlines
-   recap: Recaps or summaries of episodes

*   **Homepage**:
    [https://github.com/mingdachen/SummScreen](https://github.com/mingdachen/SummScreen)

*   **Source code**:
    [`tfds.datasets.summscreen.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/summscreen/summscreen_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `841.27 MiB`

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('transcript', 'recap')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{DBLP:journals/corr/abs-2104-07091,
  author    = {Mingda Chen and
               Zewei Chu and
               Sam Wiseman and
               Kevin Gimpel},
  title     = {SummScreen: {A} Dataset for Abstractive Screenplay Summarization},
  journal   = {CoRR},
  volume    = {abs/2104.07091},
  year      = {2021},
  url       = {https://arxiv.org/abs/2104.07091},
  archivePrefix = {arXiv},
  eprint    = {2104.07091},
  timestamp = {Mon, 19 Apr 2021 16:45:47 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2104-07091.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


## summscreen/fd (default config)

*   **Config description**: ForeverDreaming

*   **Dataset size**: `132.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 337
`'train'`      | 3,673
`'validation'` | 338

*   **Feature structure**:

```python
FeaturesDict({
    'episode_number': Text(shape=(), dtype=string),
    'episode_title': Text(shape=(), dtype=string),
    'recap': Text(shape=(), dtype=string),
    'show_title': Text(shape=(), dtype=string),
    'transcript': Text(shape=(), dtype=string),
    'transcript_author': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype  | Description
:---------------- | :----------- | :---- | :----- | :----------
                  | FeaturesDict |       |        |
episode_number    | Text         |       | string |
episode_title     | Text         |       | string |
recap             | Text         |       | string |
show_title        | Text         |       | string |
transcript        | Text         |       | string |
transcript_author | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/summscreen-fd-1.0.0.html";
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

## summscreen/tms

*   **Config description**: TVMegaSite

*   **Dataset size**: `592.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,793
`'train'`      | 18,915
`'validation'` | 1,795

*   **Feature structure**:

```python
FeaturesDict({
    'episode_summary': Text(shape=(), dtype=string),
    'recap': Text(shape=(), dtype=string),
    'recap_author': Text(shape=(), dtype=string),
    'show_title': Text(shape=(), dtype=string),
    'transcript': Text(shape=(), dtype=string),
    'transcript_author': Tensor(shape=(None,), dtype=string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape   | Dtype  | Description
:---------------- | :----------- | :------ | :----- | :----------
                  | FeaturesDict |         |        |
episode_summary   | Text         |         | string |
recap             | Text         |         | string |
recap_author      | Text         |         | string |
show_title        | Text         |         | string |
transcript        | Text         |         | string |
transcript_author | Tensor       | (None,) | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/summscreen-tms-1.0.0.html";
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