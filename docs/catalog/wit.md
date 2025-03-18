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

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/wit">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

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
    'attribution_passes_lang_id': bool,
    'caption_alt_text_description': Text(shape=(), dtype=string),
    'caption_attribution_description': Text(shape=(), dtype=string),
    'caption_reference_description': Text(shape=(), dtype=string),
    'context_page_description': Text(shape=(), dtype=string),
    'context_section_description': Text(shape=(), dtype=string),
    'hierarchical_section_title': Text(shape=(), dtype=string),
    'image_url': Text(shape=(), dtype=string),
    'is_main_image': bool,
    'language': Text(shape=(), dtype=string),
    'mime_type': Text(shape=(), dtype=string),
    'original_height': int32,
    'original_width': int32,
    'page_changed_recently': bool,
    'page_title': Text(shape=(), dtype=string),
    'page_url': Text(shape=(), dtype=string),
    'section_title': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                         | Class        | Shape | Dtype  | Description
:------------------------------ | :----------- | :---- | :----- | :----------
                                | FeaturesDict |       |        |
attribution_passes_lang_id      | Tensor       |       | bool   |
caption_alt_text_description    | Text         |       | string |
caption_attribution_description | Text         |       | string |
caption_reference_description   | Text         |       | string |
context_page_description        | Text         |       | string |
context_section_description     | Text         |       | string |
hierarchical_section_title      | Text         |       | string |
image_url                       | Text         |       | string |
is_main_image                   | Tensor       |       | bool   |
language                        | Text         |       | string |
mime_type                       | Text         |       | string |
original_height                 | Tensor       |       | int32  |
original_width                  | Tensor       |       | int32  |
page_changed_recently           | Tensor       |       | bool   |
page_title                      | Text         |       | string |
page_url                        | Text         |       | string |
section_title                   | Text         |       | string |

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

