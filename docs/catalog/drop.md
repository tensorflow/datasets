<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="drop" />
  <meta itemprop="description" content="With system performance on existing reading comprehension benchmarks nearing or&#10;surpassing human performance, we need a new, hard dataset that improves systems&#x27;&#10;capabilities to actually read paragraphs of text. DROP is a crowdsourced,&#10;adversarially-created, 96k-question benchmark, in which a system must resolve&#10;references in a question, perhaps to multiple input positions, and perform&#10;discrete operations over them (such as addition, counting, or sorting). These&#10;operations require a much more comprehensive understanding of the content of&#10;paragraphs than what was necessary for prior datasets.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;drop&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/drop" />
  <meta itemprop="sameAs" content="https://allennlp.org/drop" />
  <meta itemprop="citation" content="@inproceedings{Dua2019DROP,&#10;  author={Dheeru Dua and Yizhong Wang and Pradeep Dasigi and Gabriel Stanovsky and Sameer Singh and Matt Gardner},&#10;  title={  {DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs},&#10;  booktitle={Proc. of NAACL},&#10;  year={2019}&#10;}" />
</div>

# `drop`

*   **Description**:

With system performance on existing reading comprehension benchmarks nearing or
surpassing human performance, we need a new, hard dataset that improves systems'
capabilities to actually read paragraphs of text. DROP is a crowdsourced,
adversarially-created, 96k-question benchmark, in which a system must resolve
references in a question, perhaps to multiple input positions, and perform
discrete operations over them (such as addition, counting, or sorting). These
operations require a much more comprehensive understanding of the content of
paragraphs than what was necessary for prior datasets.

*   **Homepage**: [https://allennlp.org/drop](https://allennlp.org/drop)

*   **Source code**:
    [`tfds.text.drop.Drop`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/drop/drop.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`2.0.0`** (default): Add all options for the answers.

*   **Download size**: `7.92 MiB`

*   **Dataset size**: `116.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 9,536
`'train'` | 77,409

*   **Features**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'passage': Text(shape=(), dtype=tf.string),
    'query_id': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
    'validated_answers': Sequence(Text(shape=(), dtype=tf.string)),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/drop-2.0.0.html";
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
@inproceedings{Dua2019DROP,
  author={Dheeru Dua and Yizhong Wang and Pradeep Dasigi and Gabriel Stanovsky and Sameer Singh and Matt Gardner},
  title={  {DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs},
  booktitle={Proc. of NAACL},
  year={2019}
}
```
