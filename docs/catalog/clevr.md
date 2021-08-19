<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="clevr" />
  <meta itemprop="description" content="CLEVR is a diagnostic dataset that tests a range of visual reasoning abilities.&#10;It contains minimal biases and has detailed annotations describing the kind of&#10;reasoning each question requires.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;clevr&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/clevr-3.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/clevr" />
  <meta itemprop="sameAs" content="https://cs.stanford.edu/people/jcjohns/clevr/" />
  <meta itemprop="citation" content="@inproceedings{johnson2017clevr,&#10;  title={{CLEVR}: A diagnostic dataset for compositional language and elementary visual reasoning},&#10;  author={Johnson, Justin and Hariharan, Bharath and van der Maaten, Laurens and Fei-Fei, Li and Lawrence Zitnick, C and Girshick, Ross},&#10;  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},&#10;  year={2017}&#10;}" />
</div>

# `clevr`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=clevr">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

CLEVR is a diagnostic dataset that tests a range of visual reasoning abilities.
It contains minimal biases and has detailed annotations describing the kind of
reasoning each question requires.

*   **Homepage**:
    [https://cs.stanford.edu/people/jcjohns/clevr/](https://cs.stanford.edu/people/jcjohns/clevr/)

*   **Source code**:
    [`tfds.image.CLEVR`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/clevr.py)

*   **Versions**:

    *   `3.0.0`: No release notes.
    *   **`3.1.0`** (default): Add question/answer text.

*   **Download size**: `17.72 GiB`

*   **Dataset size**: `17.75 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 15,000
`'train'`      | 70,000
`'validation'` | 15,000

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'objects': Sequence({
        '3d_coords': Tensor(shape=(3,), dtype=tf.float32),
        'color': ClassLabel(shape=(), dtype=tf.int64, num_classes=8),
        'material': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'pixel_coords': Tensor(shape=(3,), dtype=tf.float32),
        'rotation': tf.float32,
        'shape': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
        'size': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
    'question_answer': Sequence({
        'answer': Text(shape=(), dtype=tf.string),
        'question': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/clevr-3.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/clevr-3.1.0.html";
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
@inproceedings{johnson2017clevr,
  title={{CLEVR}: A diagnostic dataset for compositional language and elementary visual reasoning},
  author={Johnson, Justin and Hariharan, Bharath and van der Maaten, Laurens and Fei-Fei, Li and Lawrence Zitnick, C and Girshick, Ross},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2017}
}
```
