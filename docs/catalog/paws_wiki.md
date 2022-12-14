<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="paws_wiki" />
  <meta itemprop="description" content="Existing paraphrase identification datasets lack sentence pairs that have high&#10;lexical overlap without being paraphrases. Models trained on such data fail to&#10;distinguish pairs like flights from New York to Florida and flights from Florida&#10;to New York. This dataset contains 108,463 human-labeled and 656k noisily&#10;labeled pairs that feature the importance of modeling structure, context, and&#10;word order information for the problem of paraphrase identification.&#10;&#10;For further details, see the accompanying paper: PAWS: Paraphrase Adversaries&#10;from Word Scrambling at https://arxiv.org/abs/1904.01130&#10;&#10;This corpus contains pairs generated from Wikipedia pages, containing pairs that&#10;are generated from both word swapping and back translation methods. All pairs&#10;have human judgements on both paraphrasing and fluency and they are split into&#10;Train/Dev/Test sections.&#10;&#10;All files are in the tsv format with four columns:&#10;&#10;1. `id`: A unique id for each pair.&#10;2. `sentence1`: The first sentence.&#10;3. `sentence2`: The second sentence.&#10;4. `(noisy_)label`: (Noisy) label for each pair.&#10;&#10;Each label has two possible values: 0 indicates the pair has different meaning,&#10;while 1 indicates the pair is a paraphrase.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;paws_wiki&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/paws_wiki" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/paws" />
  <meta itemprop="citation" content="@InProceedings{paws2019naacl,&#10;  title = {{PAWS: Paraphrase Adversaries from Word Scrambling}},&#10;  author = {Zhang, Yuan and Baldridge, Jason and He, Luheng},&#10;  booktitle = {Proc. of NAACL},&#10;  year = {2019}&#10;}" />
</div>

# `paws_wiki`


*   **Description**:

Existing paraphrase identification datasets lack sentence pairs that have high
lexical overlap without being paraphrases. Models trained on such data fail to
distinguish pairs like flights from New York to Florida and flights from Florida
to New York. This dataset contains 108,463 human-labeled and 656k noisily
labeled pairs that feature the importance of modeling structure, context, and
word order information for the problem of paraphrase identification.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries
from Word Scrambling at https://arxiv.org/abs/1904.01130

This corpus contains pairs generated from Wikipedia pages, containing pairs that
are generated from both word swapping and back translation methods. All pairs
have human judgements on both paraphrasing and fluency and they are split into
Train/Dev/Test sections.

All files are in the tsv format with four columns:

1.  `id`: A unique id for each pair.
2.  `sentence1`: The first sentence.
3.  `sentence2`: The second sentence.
4.  `(noisy_)label`: (Noisy) label for each pair.

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/paws">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/google-research-datasets/paws](https://github.com/google-research-datasets/paws)

*   **Source code**:
    [`tfds.datasets.paws_wiki.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/paws_wiki/paws_wiki_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial version.
    *   **`1.1.0`** (default): Adds configs to different subset and support raw
        text.

*   **Download size**: `57.47 MiB`

*   **Feature structure**:

```python
FeaturesDict({
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=string),
    'sentence2': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape | Dtype  | Description
:-------- | :----------- | :---- | :----- | :----------
          | FeaturesDict |       |        |
label     | ClassLabel   |       | int64  |
sentence1 | Text         |       | string |
sentence2 | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@InProceedings{paws2019naacl,
  title = {{PAWS: Paraphrase Adversaries from Word Scrambling}},
  author = {Zhang, Yuan and Baldridge, Jason and He, Luheng},
  booktitle = {Proc. of NAACL},
  year = {2019}
}
```


## paws_wiki/labeled_final_tokenized (default config)

*   **Config description**: Subset: labeled_final tokenized: True

*   **Dataset size**: `17.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,000
`'train'`      | 49,401
`'validation'` | 8,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-labeled_final_tokenized-1.1.0.html";
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

## paws_wiki/labeled_final_raw

*   **Config description**: Subset: labeled_final tokenized: False

*   **Dataset size**: `17.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,000
`'train'`      | 49,401
`'validation'` | 8,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-labeled_final_raw-1.1.0.html";
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

## paws_wiki/labeled_swap_tokenized

*   **Config description**: Subset: labeled_swap tokenized: True

*   **Dataset size**: `8.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,397

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-labeled_swap_tokenized-1.1.0.html";
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

## paws_wiki/labeled_swap_raw

*   **Config description**: Subset: labeled_swap tokenized: False

*   **Dataset size**: `8.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,397

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-labeled_swap_raw-1.1.0.html";
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

## paws_wiki/unlabeled_final_tokenized

*   **Config description**: Subset: unlabeled_final tokenized: True

*   **Dataset size**: `177.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 645,652
`'validation'` | 10,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-unlabeled_final_tokenized-1.1.0.html";
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