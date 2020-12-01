<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ag_news_subset" />
  <meta itemprop="description" content="AG is a collection of more than 1 million news articles.&#10;News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity.&#10;ComeToMyHead is an academic news search engine which has been running since July, 2004.&#10;The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc),&#10;information retrieval (ranking, search, etc), xml, data compression, data streaming,&#10;and any other non-commercial activity.&#10;For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .&#10;&#10;The AG&#x27;s news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above.&#10;It is used as a text classification benchmark in the following paper:&#10;Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).&#10;&#10;The AG&#x27;s news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.&#10;Each class contains 30,000 training samples and 1,900 testing samples.&#10;The total number of training samples is 120,000 and testing 7,600.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ag_news_subset&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ag_news_subset" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/1509.01626" />
  <meta itemprop="citation" content="@misc{zhang2015characterlevel,&#10;    title={Character-level Convolutional Networks for Text Classification},&#10;    author={Xiang Zhang and Junbo Zhao and Yann LeCun},&#10;    year={2015},&#10;    eprint={1509.01626},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `ag_news_subset`

*   **Description**:

AG is a collection of more than 1 million news articles. News articles have been
gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of
activity. ComeToMyHead is an academic news search engine which has been running
since July, 2004. The dataset is provided by the academic comunity for research
purposes in data mining (clustering, classification, etc), information retrieval
(ranking, search, etc), xml, data compression, data streaming, and any other
non-commercial activity. For more information, please refer to the link
http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang
(xiang.zhang@nyu.edu) from the dataset above. It is used as a text
classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann
LeCun. Character-level Convolutional Networks for Text Classification. Advances
in Neural Information Processing Systems 28 (NIPS 2015).

The AG's news topic classification dataset is constructed by choosing 4 largest
classes from the original corpus. Each class contains 30,000 training samples
and 1,900 testing samples. The total number of training samples is 120,000 and
testing 7,600.

*   **Homepage**:
    [https://arxiv.org/abs/1509.01626](https://arxiv.org/abs/1509.01626)

*   **Source code**:
    [`tfds.text.AGNewsSubset`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/ag_news_subset.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `11.24 MiB`

*   **Dataset size**: `35.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 7,600
`'train'` | 120,000

*   **Features**:

```python
FeaturesDict({
    'description': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('description', 'label')`

*   **Citation**:

```
@misc{zhang2015characterlevel,
    title={Character-level Convolutional Networks for Text Classification},
    author={Xiang Zhang and Junbo Zhao and Yann LeCun},
    year={2015},
    eprint={1509.01626},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ag_news_subset-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->