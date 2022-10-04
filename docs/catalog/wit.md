<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wit" />
  <meta itemprop="description" content="Wikipedia-based Image Text (WIT) Dataset is a large multimodal multilingual&#10;dataset. WIT is composed of a curated set of 37.6 million entity rich image-text&#10;examples with 11.5 million unique images across 108 Wikipedia languages. Its&#10;size enables WIT to be used as a pretraining dataset for multimodal machine&#10;learning models.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wit&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wit" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/wit/" />
  <meta itemprop="citation" content="@article{srinivasan2021wit,&#10;  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},&#10;  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},&#10;  journal={arXiv preprint arXiv:2103.01913},&#10;  year={2021}&#10;}" />
</div>

# `wit`


*   **Description**:

Wikipedia-based Image Text (WIT) Dataset is a large multimodal multilingual
dataset. WIT is composed of a curated set of 37.6 million entity rich image-text
examples with 11.5 million unique images across 108 Wikipedia languages. Its
size enables WIT to be used as a pretraining dataset for multimodal machine
learning models.

*   **Homepage**:
    [https://github.com/google-research-datasets/wit/](https://github.com/google-research-datasets/wit/)

*   **Source code**:
    [`tfds.vision_language.wit.Wit`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/wit/wit.py)

*   **Versions**:

    *   `1.0.0`: Initial release. It loads the WIT dataset from
        https://storage.googleapis.com/gresearch/wit/
    *   **`1.1.0`** (default): Added `val` and `test` splits.

*   **Download size**: `25.20 GiB`

*   **Dataset size**: `81.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'test'`  | 210,166
`'train'` | 37,046,386
`'val'`   | 261,024

*   **Feature structure**:

```python
FeaturesDict({
    'attribution_passes_lang_id': tf.bool,
    'caption_alt_text_description': Text(shape=(), dtype=tf.string),
    'caption_attribution_description': Text(shape=(), dtype=tf.string),
    'caption_reference_description': Text(shape=(), dtype=tf.string),
    'context_page_description': Text(shape=(), dtype=tf.string),
    'context_section_description': Text(shape=(), dtype=tf.string),
    'hierarchical_section_title': Text(shape=(), dtype=tf.string),
    'image_url': Text(shape=(), dtype=tf.string),
    'is_main_image': tf.bool,
    'language': Text(shape=(), dtype=tf.string),
    'mime_type': Text(shape=(), dtype=tf.string),
    'original_height': tf.int32,
    'original_width': tf.int32,
    'page_changed_recently': tf.bool,
    'page_title': Text(shape=(), dtype=tf.string),
    'page_url': Text(shape=(), dtype=tf.string),
    'section_title': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature                         | Class        | Shape | Dtype     | Description
:------------------------------ | :----------- | :---- | :-------- | :----------
                                | FeaturesDict |       |           |
attribution_passes_lang_id      | Tensor       |       | tf.bool   |
caption_alt_text_description    | Text         |       | tf.string |
caption_attribution_description | Text         |       | tf.string |
caption_reference_description   | Text         |       | tf.string |
context_page_description        | Text         |       | tf.string |
context_section_description     | Text         |       | tf.string |
hierarchical_section_title      | Text         |       | tf.string |
image_url                       | Text         |       | tf.string |
is_main_image                   | Tensor       |       | tf.bool   |
language                        | Text         |       | tf.string |
mime_type                       | Text         |       | tf.string |
original_height                 | Tensor       |       | tf.int32  |
original_width                  | Tensor       |       | tf.int32  |
page_changed_recently           | Tensor       |       | tf.bool   |
page_title                      | Text         |       | tf.string |
page_url                        | Text         |       | tf.string |
section_title                   | Text         |       | tf.string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wit-1.1.0.html";
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
@article{srinivasan2021wit,
  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},
  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},
  journal={arXiv preprint arXiv:2103.01913},
  year={2021}
}
```

