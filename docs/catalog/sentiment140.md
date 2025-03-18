<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="sentiment140" />
  <meta itemprop="description" content="Sentiment140 allows you to discover the sentiment of a brand, product, or topic&#10;on Twitter.&#10;&#10;The data is a CSV with emoticons removed. Data file format has 6 fields:&#10;&#10;1.  the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)&#10;2.  the id of the tweet (2087)&#10;3.  the date of the tweet (Sat May 16 23:58:44 UTC 2009)&#10;4.  the query (lyx). If there is no query, then this value is NO_QUERY.&#10;5.  the user that tweeted (robotickilldozr)&#10;6.  the text of the tweet (Lyx is cool)&#10;&#10;For more information, refer to the paper Twitter Sentiment Classification with&#10;Distant Supervision at&#10;https://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;sentiment140&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/sentiment140" />
  <meta itemprop="sameAs" content="http://help.sentiment140.com/home" />
  <meta itemprop="citation" content="@ONLINE {Sentiment140,&#10;    author = &quot;Go, Alec and Bhayani, Richa and Huang, Lei&quot;,&#10;    title  = &quot;Twitter Sentiment Classification using Distant Supervision&quot;,&#10;    year   = &quot;2009&quot;,&#10;    url    = &quot;http://help.sentiment140.com/home&quot;&#10;}" />
</div>

# `sentiment140`


*   **Description**:

Sentiment140 allows you to discover the sentiment of a brand, product, or topic
on Twitter.

The data is a CSV with emoticons removed. Data file format has 6 fields:

1.  the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
2.  the id of the tweet (2087)
3.  the date of the tweet (Sat May 16 23:58:44 UTC 2009)
4.  the query (lyx). If there is no query, then this value is NO_QUERY.
5.  the user that tweeted (robotickilldozr)
6.  the text of the tweet (Lyx is cool)

For more information, refer to the paper Twitter Sentiment Classification with
Distant Supervision at
https://cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/sentiment140">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://help.sentiment140.com/home](http://help.sentiment140.com/home)

*   **Source code**:
    [`tfds.datasets.sentiment140.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/sentiment140/sentiment140_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `77.59 MiB`

*   **Dataset size**: `305.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 498
`'train'` | 1,600,000

*   **Feature structure**:

```python
FeaturesDict({
    'date': Text(shape=(), dtype=string),
    'polarity': int32,
    'query': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
    'user': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype  | Description
:------- | :----------- | :---- | :----- | :----------
         | FeaturesDict |       |        |
date     | Text         |       | string |
polarity | Tensor       |       | int32  |
query    | Text         |       | string |
text     | Text         |       | string |
user     | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'polarity')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/sentiment140-1.0.0.html";
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
@ONLINE {Sentiment140,
    author = "Go, Alec and Bhayani, Richa and Huang, Lei",
    title  = "Twitter Sentiment Classification using Distant Supervision",
    year   = "2009",
    url    = "http://help.sentiment140.com/home"
}
```

