<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lambada" />
  <meta itemprop="description" content="The LAMBADA dataset evaluates the capabilities of computational&#10;models for text understanding by means of a word prediction task. LAMBADA is a&#10;collection of narrative passages sharing the characteristic that human subjects&#10;are able to guess their last word if they are exposed to the whole passage, but&#10;not if they only see the last sentence preceding the target word&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lambada&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lambada" />
  <meta itemprop="sameAs" content="https://zenodo.org/record/2630551#.X4Xzn5NKjUI" />
  <meta itemprop="citation" content="@inproceedings{paperno-etal-2016-lambada,&#10;    title = &quot;The {LAMBADA} dataset: Word prediction requiring a broad discourse context&quot;,&#10;    author = &quot;Paperno, Denis  and&#10;      Kruszewski, Germ{&#x27;a}n  and&#10;      Lazaridou, Angeliki  and&#10;      Pham, Ngoc Quan  and&#10;      Bernardi, Raffaella  and&#10;      Pezzelle, Sandro  and&#10;      Baroni, Marco  and&#10;      Boleda, Gemma  and&#10;      Fern{&#x27;a}ndez, Raquel&quot;,&#10;    booktitle = &quot;Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)&quot;,&#10;    month = aug,&#10;    year = &quot;2016&quot;,&#10;    address = &quot;Berlin, Germany&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/P16-1144&quot;,&#10;    doi = &quot;10.18653/v1/P16-1144&quot;,&#10;    pages = &quot;1525--1534&quot;,&#10;}" />
</div>

# `lambada`

*   **Description**:

The LAMBADA dataset evaluates the capabilities of computational models for text
understanding by means of a word prediction task. LAMBADA is a collection of
narrative passages sharing the characteristic that human subjects are able to
guess their last word if they are exposed to the whole passage, but not if they
only see the last sentence preceding the target word

*   **Homepage**:
    [https://zenodo.org/record/2630551#.X4Xzn5NKjUI](https://zenodo.org/record/2630551#.X4Xzn5NKjUI)

*   **Source code**:
    [`tfds.text.lambada.Lambada`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/lambada/lambada.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `319.03 MiB`

*   **Dataset size**: `3.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 5,153
`'train'` | 4,869

*   **Features**:

```python
FeaturesDict({
    'passage': Text(shape=(), dtype=tf.string),
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
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lambada-1.0.0.html";
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
@inproceedings{paperno-etal-2016-lambada,
    title = "The {LAMBADA} dataset: Word prediction requiring a broad discourse context",
    author = "Paperno, Denis  and
      Kruszewski, Germ{'a}n  and
      Lazaridou, Angeliki  and
      Pham, Ngoc Quan  and
      Bernardi, Raffaella  and
      Pezzelle, Sandro  and
      Baroni, Marco  and
      Boleda, Gemma  and
      Fern{'a}ndez, Raquel",
    booktitle = "Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2016",
    address = "Berlin, Germany",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P16-1144",
    doi = "10.18653/v1/P16-1144",
    pages = "1525--1534",
}
```
