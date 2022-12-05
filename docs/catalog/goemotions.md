<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="goemotions" />
  <meta itemprop="description" content="The GoEmotions dataset contains 58k carefully curated Reddit comments labeled&#10;for 27 emotion categories or Neutral. The emotion categories are admiration,&#10;amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,&#10;disappointment, disapproval, disgust, embarrassment, excitement, fear,&#10;gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief,&#10;remorse, sadness, surprise.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;goemotions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/goemotions" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/goemotions" />
  <meta itemprop="citation" content="@inproceedings{demszky-2020-goemotions,&#10;    title = &quot;{G}o{E}motions: A Dataset of Fine-Grained Emotions&quot;,&#10;    author = &quot;Demszky, Dorottya  and&#10;      Movshovitz-Attias, Dana  and&#10;      Ko, Jeongwoo  and&#10;      Cowen, Alan  and&#10;      Nemade, Gaurav  and&#10;      Ravi, Sujith&quot;,&#10;    booktitle = &quot;Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics&quot;,&#10;    month = jul,&#10;    year = &quot;2020&quot;,&#10;    address = &quot;Online&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/2020.acl-main.372&quot;,&#10;    pages = &quot;4040--4054&quot;,&#10;}" />
</div>

# `goemotions`


*   **Description**:

The GoEmotions dataset contains 58k carefully curated Reddit comments labeled
for 27 emotion categories or Neutral. The emotion categories are admiration,
amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear,
gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief,
remorse, sadness, surprise.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/goemotions">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/goemotions](https://github.com/google-research/google-research/tree/master/goemotions)

*   **Source code**:
    [`tfds.text.Goemotions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/goemotions.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `4.19 MiB`

*   **Dataset size**: `32.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 5,427
`'train'`      | 43,410
`'validation'` | 5,426

*   **Feature structure**:

```python
FeaturesDict({
    'admiration': bool,
    'amusement': bool,
    'anger': bool,
    'annoyance': bool,
    'approval': bool,
    'caring': bool,
    'comment_text': Text(shape=(), dtype=string),
    'confusion': bool,
    'curiosity': bool,
    'desire': bool,
    'disappointment': bool,
    'disapproval': bool,
    'disgust': bool,
    'embarrassment': bool,
    'excitement': bool,
    'fear': bool,
    'gratitude': bool,
    'grief': bool,
    'joy': bool,
    'love': bool,
    'nervousness': bool,
    'neutral': bool,
    'optimism': bool,
    'pride': bool,
    'realization': bool,
    'relief': bool,
    'remorse': bool,
    'sadness': bool,
    'surprise': bool,
})
```

*   **Feature documentation**:

Feature        | Class        | Shape | Dtype  | Description
:------------- | :----------- | :---- | :----- | :----------
               | FeaturesDict |       |        |
admiration     | Tensor       |       | bool   |
amusement      | Tensor       |       | bool   |
anger          | Tensor       |       | bool   |
annoyance      | Tensor       |       | bool   |
approval       | Tensor       |       | bool   |
caring         | Tensor       |       | bool   |
comment_text   | Text         |       | string |
confusion      | Tensor       |       | bool   |
curiosity      | Tensor       |       | bool   |
desire         | Tensor       |       | bool   |
disappointment | Tensor       |       | bool   |
disapproval    | Tensor       |       | bool   |
disgust        | Tensor       |       | bool   |
embarrassment  | Tensor       |       | bool   |
excitement     | Tensor       |       | bool   |
fear           | Tensor       |       | bool   |
gratitude      | Tensor       |       | bool   |
grief          | Tensor       |       | bool   |
joy            | Tensor       |       | bool   |
love           | Tensor       |       | bool   |
nervousness    | Tensor       |       | bool   |
neutral        | Tensor       |       | bool   |
optimism       | Tensor       |       | bool   |
pride          | Tensor       |       | bool   |
realization    | Tensor       |       | bool   |
relief         | Tensor       |       | bool   |
remorse        | Tensor       |       | bool   |
sadness        | Tensor       |       | bool   |
surprise       | Tensor       |       | bool   |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/goemotions-0.1.0.html";
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
@inproceedings{demszky-2020-goemotions,
    title = "{G}o{E}motions: A Dataset of Fine-Grained Emotions",
    author = "Demszky, Dorottya  and
      Movshovitz-Attias, Dana  and
      Ko, Jeongwoo  and
      Cowen, Alan  and
      Nemade, Gaurav  and
      Ravi, Sujith",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.372",
    pages = "4040--4054",
}
```

