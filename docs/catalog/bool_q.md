<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bool_q" />
  <meta itemprop="description" content="BoolQ is a question answering dataset for yes/no questions containing 15942 examples.&#10;These questions are naturally occurring, they are generated in unprompted and unconstrained settings.&#10;&#10;Each example is a triplet of (question, passage, answer),&#10;with the title of the page as optional additional context.&#10;The text-pair classification setup is similar to existing&#10;natural language inference tasks.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bool_q&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bool_q" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/boolean-questions" />
  <meta itemprop="citation" content="@inproceedings{clark2019boolq,&#10;  title =     {BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},&#10;  author =    {Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},&#10;  booktitle = {NAACL},&#10;  year =      {2019},&#10;}" />
</div>

# `bool_q`

*   **Description**:

BoolQ is a question answering dataset for yes/no questions containing 15942
examples. These questions are naturally occurring, they are generated in
unprompted and unconstrained settings.

Each example is a triplet of (question, passage, answer), with the title of the
page as optional additional context. The text-pair classification setup is
similar to existing natural language inference tasks.

*   **Homepage**:
    [https://github.com/google-research-datasets/boolean-questions](https://github.com/google-research-datasets/boolean-questions)

*   **Source code**:
    [`tfds.text.bool_q.BoolQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/bool_q/bool_q.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `8.36 MiB`

*   **Dataset size**: `8.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 9,427
`'validation'` | 3,270

*   **Features**:

```python
FeaturesDict({
    'answer': tf.bool,
    'passage': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bool_q-1.0.0.html";
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
@inproceedings{clark2019boolq,
  title =     {BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},
  author =    {Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},
  booktitle = {NAACL},
  year =      {2019},
}
```
