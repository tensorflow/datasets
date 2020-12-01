<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="eraser_multi_rc" />
  <meta itemprop="description" content="Eraser Multi RC is a dataset for queries over multi-line passages, along with&#10;answers and a rationalte. Each example in this dataset has the following 5 parts&#10;1. A Mutli-line Passage&#10;2. A Query about the passage&#10;3. An Answer to the query&#10;4. A Classification as to whether the answer is right or wrong&#10;5. An Explanation justifying the classification&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;eraser_multi_rc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/eraser_multi_rc" />
  <meta itemprop="sameAs" content="https://cogcomp.seas.upenn.edu/multirc/" />
  <meta itemprop="citation" content="@unpublished{eraser2019,&#10;    title = {ERASER: A Benchmark to Evaluate Rationalized NLP Models},&#10;    author = {Jay DeYoung and Sarthak Jain and Nazneen Fatema Rajani and Eric Lehman and Caiming Xiong and Richard Socher and Byron C. Wallace}&#10;}&#10;@inproceedings{MultiRC2018,&#10;    author = {Daniel Khashabi and Snigdha Chaturvedi and Michael Roth and Shyam Upadhyay and Dan Roth},&#10;    title = {Looking Beyond the Surface:A Challenge Set for Reading Comprehension over Multiple Sentences},&#10;    booktitle = {NAACL},&#10;    year = {2018}&#10;}" />
</div>

# `eraser_multi_rc`

*   **Description**:

Eraser Multi RC is a dataset for queries over multi-line passages, along with
answers and a rationalte. Each example in this dataset has the following 5 parts
1. A Mutli-line Passage 2. A Query about the passage 3. An Answer to the query
4. A Classification as to whether the answer is right or wrong 5. An Explanation
justifying the classification

*   **Homepage**:
    [https://cogcomp.seas.upenn.edu/multirc/](https://cogcomp.seas.upenn.edu/multirc/)

*   **Source code**:
    [`tfds.text.EraserMultiRc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/eraser_multi_rc.py)

*   **Versions**:

    *   **`0.1.1`** (default): No release notes.

*   **Download size**: `1.59 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,848
`'train'`      | 24,029
`'validation'` | 3,214

*   **Features**:

```python
FeaturesDict({
    'evidences': Sequence(Text(shape=(), dtype=tf.string)),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'passage': Text(shape=(), dtype=tf.string),
    'query_and_answer': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@unpublished{eraser2019,
    title = {ERASER: A Benchmark to Evaluate Rationalized NLP Models},
    author = {Jay DeYoung and Sarthak Jain and Nazneen Fatema Rajani and Eric Lehman and Caiming Xiong and Richard Socher and Byron C. Wallace}
}
@inproceedings{MultiRC2018,
    author = {Daniel Khashabi and Snigdha Chaturvedi and Michael Roth and Shyam Upadhyay and Dan Roth},
    title = {Looking Beyond the Surface:A Challenge Set for Reading Comprehension over Multiple Sentences},
    booktitle = {NAACL},
    year = {2018}
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/eraser_multi_rc-0.1.1.html";
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