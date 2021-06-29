<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="paws_wiki" />
  <meta itemprop="description" content="Existing paraphrase identification datasets lack sentence pairs&#10;that have high lexical overlap without being paraphrases.&#10;Models trained on such data fail to distinguish pairs like flights&#10;from New York to Florida and flights from Florida to New York.&#10;This dataset contains 108,463 human-labeled and 656k noisily labeled pairs&#10;that feature the importance of modeling structure, context, and word order information&#10;for the problem of paraphrase identification.&#10;&#10;For further details, see the accompanying paper: PAWS: Paraphrase Adversaries from Word Scrambling&#10;at https://arxiv.org/abs/1904.01130&#10;&#10;This corpus contains pairs generated from Wikipedia pages,&#10;containing pairs that are generated from both word swapping and back translation methods.&#10;All pairs have human judgements on both paraphrasing and fluency&#10;and they are split into Train/Dev/Test sections.&#10;&#10;All files are in the tsv format with four columns:&#10;&#10;id A unique id for each pair&#10;sentence1 The first sentence&#10;sentence2    The second sentence&#10;(noisy_)label   (Noisy) label for each pair&#10;&#10;Each label has two possible values: 0 indicates the pair has different meaning,&#10;while 1 indicates the pair is a paraphrase.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;paws_wiki&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
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

id A unique id for each pair sentence1 The first sentence sentence2 The second
sentence (noisy_)label (Noisy) label for each pair

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.

*   **Homepage**:
    [https://github.com/google-research-datasets/paws](https://github.com/google-research-datasets/paws)

*   **Source code**:
    [`tfds.text.PawsWiki`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/paws_wiki.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `4.47 MiB`

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

*   **Features**:

```python
FeaturesDict({
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

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
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/paws_wiki-1.0.0.html";
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

*   **Citation**:

```
@InProceedings{paws2019naacl,
  title = {{PAWS: Paraphrase Adversaries from Word Scrambling}},
  author = {Zhang, Yuan and Baldridge, Jason and He, Luheng},
  booktitle = {Proc. of NAACL},
  year = {2019}
}
```
