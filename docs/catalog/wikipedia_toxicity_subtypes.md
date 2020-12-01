<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia_toxicity_subtypes" />
  <meta itemprop="description" content="This version of the Wikipedia Toxicity Subtypes dataset provides access to the&#10;primary toxicity label, as well the five toxicity subtype labels annotated by&#10;crowd workers. The toxicity and toxicity subtype labels are binary values&#10;(0 or 1) indicating whether the majority of annotators assigned that&#10;attributes to the comment text.&#10;&#10;The comments in this dataset come from an archive of Wikipedia talk pages&#10;comments. These have been annotated by Jigsaw for toxicity, as well as a variety&#10;of toxicity subtypes, including severe toxicity, obscenity, threatening&#10;language, insulting language, and identity attacks. This dataset is a replica of&#10;the data released for the Jigsaw Toxic Comment Classification Challenge on&#10;Kaggle, with the training set unchanged, and the test dataset merged with the&#10;test_labels released after the end of the competition. Test data not used for&#10;scoring has been dropped. This dataset is released under CC0, as is the&#10;underlying comment text.&#10;&#10;See the Kaggle documentation or&#10;https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more&#10;details.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikipedia_toxicity_subtypes&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia_toxicity_subtypes" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data" />
  <meta itemprop="citation" content="@inproceedings{10.1145/3038912.3052591,&#10;  author = {Wulczyn, Ellery and Thain, Nithum and Dixon, Lucas},&#10;  title = {Ex Machina: Personal Attacks Seen at Scale},&#10;  year = {2017},&#10;  isbn = {9781450349130},&#10;  publisher = {International World Wide Web Conferences Steering Committee},&#10;  address = {Republic and Canton of Geneva, CHE},&#10;  url = {https://doi.org/10.1145/3038912.3052591},&#10;  doi = {10.1145/3038912.3052591},&#10;  booktitle = {Proceedings of the 26th International Conference on World Wide Web},&#10;  pages = {1391-1399},&#10;  numpages = {9},&#10;  keywords = {online discussions, wikipedia, online harassment},&#10;  location = {Perth, Australia},&#10;  series = {WWW &#x27;17}&#10;}" />
</div>

# `wikipedia_toxicity_subtypes`

*   **Description**:

This version of the Wikipedia Toxicity Subtypes dataset provides access to the
primary toxicity label, as well the five toxicity subtype labels annotated by
crowd workers. The toxicity and toxicity subtype labels are binary values (0 or
1) indicating whether the majority of annotators assigned that attributes to the
comment text.

The comments in this dataset come from an archive of Wikipedia talk pages
comments. These have been annotated by Jigsaw for toxicity, as well as a variety
of toxicity subtypes, including severe toxicity, obscenity, threatening
language, insulting language, and identity attacks. This dataset is a replica of
the data released for the Jigsaw Toxic Comment Classification Challenge on
Kaggle, with the training set unchanged, and the test dataset merged with the
test_labels released after the end of the competition. Test data not used for
scoring has been dropped. This dataset is released under CC0, as is the
underlying comment text.

See the Kaggle documentation or
https://figshare.com/articles/Wikipedia_Talk_Labels_Toxicity/4563973 for more
details.

*   **Homepage**:
    [https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data)

*   **Source code**:
    [`tfds.text.WikipediaToxicitySubtypes`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia_toxicity_subtypes.py)

*   **Versions**:

    *   **`0.2.0`** (default): Updated features for consistency with
        CivilComments dataset.

*   **Download size**: `36.85 MiB`

*   **Dataset size**: `118.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 63,978
`'train'` | 159,571

*   **Features**:

```python
FeaturesDict({
    'identity_attack': tf.float32,
    'insult': tf.float32,
    'obscene': tf.float32,
    'severe_toxicity': tf.float32,
    'text': Text(shape=(), dtype=tf.string),
    'threat': tf.float32,
    'toxicity': tf.float32,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Citation**:

```
@inproceedings{10.1145/3038912.3052591,
  author = {Wulczyn, Ellery and Thain, Nithum and Dixon, Lucas},
  title = {Ex Machina: Personal Attacks Seen at Scale},
  year = {2017},
  isbn = {9781450349130},
  publisher = {International World Wide Web Conferences Steering Committee},
  address = {Republic and Canton of Geneva, CHE},
  url = {https://doi.org/10.1145/3038912.3052591},
  doi = {10.1145/3038912.3052591},
  booktitle = {Proceedings of the 26th International Conference on World Wide Web},
  pages = {1391-1399},
  numpages = {9},
  keywords = {online discussions, wikipedia, online harassment},
  location = {Perth, Australia},
  series = {WWW '17}
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wikipedia_toxicity_subtypes-0.2.0.html";
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