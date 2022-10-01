<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wit_kaggle" />
  <meta itemprop="description" content="Wikipedia - Image/Caption Matching Kaggle Competition.&#10;&#10;This competition is organized by the&#10;[Research team](https://research.wikimedia.org/) at the&#10;[Wikimedia Foundation](https://wikimediafoundation.org/) in collaboration with&#10;Google Research and a few external collaborators.&#10;This competition is based on the&#10;[WIT dataset](https://github.com/google-research-datasets/wit) published by&#10;Google Research as detailed in this[SIGIR paper](https://dl.acm.org/doi/abs/10.1145/3404835.3463257).&#10;&#10;In this competition, you’ll build a model that automatically retrieves the text&#10;closest to an image. Specifically, you&#x27;ll train your model to associate given&#10;images with article titles or complex captions, in multiple languages.&#10;The best models will account for the semantic granularity of Wikipedia images.&#10;If successful, you&#x27;ll be contributing to the accessibility of the largest&#10;online encyclopedia. The millions of Wikipedia readers and edietors will be able&#10;to more easily understand, search, and describe media at scale. As a result,&#10;you’ll contribute to an open model to improve learning for all.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wit_kaggle&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/wit_kaggle-train_with_extended_features-1.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wit_kaggle" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/wikipedia-image-caption/code" />
  <meta itemprop="citation" content="@article{srinivasan2021wit,&#10;  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},&#10;  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},&#10;  journal={arXiv preprint arXiv:2103.01913},&#10;  year={2021}&#10;}" />
</div>

# `wit_kaggle`


Warning: Manual download required. See instructions below.

*   **Description**:

Wikipedia - Image/Caption Matching Kaggle Competition.

This competition is organized by the
[Research team](https://research.wikimedia.org/) at the
[Wikimedia Foundation](https://wikimediafoundation.org/) in collaboration with
Google Research and a few external collaborators. This competition is based on
the [WIT dataset](https://github.com/google-research-datasets/wit) published by
Google Research as detailed in
this[SIGIR paper](https://dl.acm.org/doi/abs/10.1145/3404835.3463257).

In this competition, you’ll build a model that automatically retrieves the text
closest to an image. Specifically, you'll train your model to associate given
images with article titles or complex captions, in multiple languages. The best
models will account for the semantic granularity of Wikipedia images. If
successful, you'll be contributing to the accessibility of the largest online
encyclopedia. The millions of Wikipedia readers and edietors will be able to
more easily understand, search, and describe media at scale. As a result, you’ll
contribute to an open model to improve learning for all.

*   **Homepage**:
    [https://www.kaggle.com/c/wikipedia-image-caption/code](https://www.kaggle.com/c/wikipedia-image-caption/code)

*   **Source code**:
    [`tfds.vision_language.wit_kaggle.WitKaggle`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/wit_kaggle/wit_kaggle.py)

*   **Versions**:

    *   `1.0.0`: Initial release. It provides the train and test datasets from
        the Wikipedia - Image/Caption Matching Kaggle competition
        (https://www.kaggle.com/c/wikipedia-image-caption/data).

        The goal of the competition is to build a model that automatically
        retrieves the text closest to an image. Specifically, the model shuld be
        trained to associate given images with article titles or complex
        captions, in multiple languages. The best models will account for the
        semantic granularity of Wikipedia images.

        Note that this release doesn't provide the ground truth for the test
        set, as it hasn't been provided by the Kaggle competition yet.

        Note that not all of the training observations have corresponding image
        data. The released images exclude all images containing humans. For
        samples which are not associated with image data, the following image
        features are used: `image` is a byte-64 encoded blank image, `embedding`
        is a vector of 2048 zeros.

        The samples released for the competition can be loaded as:
        `tfds.load("wit_kaggle/train_with_extended_features")
        tfds.load("wit_kaggle/test_without_gold")`

    *   **`1.0.1`** (default): Optimize Beam pipeline to avoid strugglers,
        ignoring rows without an image URL. Also added more Beam counters.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Depending on the config called, manual_dir should contain some of the
    following subdirectories:

    *   train
    -   train-{0000x}-of-00005.tsv.zip
    -   image_data_train/
        *   image_pixels/
        -   train_image_pixels_part-00{000-199}.csv.gz
        *   resnet_embeddings/
        -   train_resnet_embeddings_part-00{000-214}.csv.gz
    *   test
    -   test.tsv.zip
    -   image_data_test/
        *   image_pixels/
        -   test_image_pixels_part-0000{0-4}.csv
        *   resnet_embeddings/
        -   test_resnet_embeddings_part-0000{0-9}.csv

Registration at https://www.kaggle.com/c/wikipedia-image-caption/data is needed
to get the links to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image_url', 'caption_title_and_reference_description')`

*   **Citation**:

```
@article{srinivasan2021wit,
  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},
  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},
  journal={arXiv preprint arXiv:2103.01913},
  year={2021}
}
```


## wit_kaggle/train_with_extended_features (default config)

*   **Config description**: Training samples for the Wikipedia-Image/Caption
    Matching competition.

*   **Dataset size**: `1.16 TiB`

*   **Splits**:

Split                            | Examples
:------------------------------- | ---------:
`'train_with_extended_features'` | 37,046,386

*   **Feature structure**:

```python
FeaturesDict({
    'attribution_passes_lang_id': tf.bool,
    'caption_alt_text_description': Text(shape=(), dtype=tf.string),
    'caption_attribution_description': Text(shape=(), dtype=tf.string),
    'caption_reference_description': Text(shape=(), dtype=tf.string),
    'caption_title_and_reference_description': Text(shape=(), dtype=tf.string),
    'context_page_description': Text(shape=(), dtype=tf.string),
    'context_section_description': Text(shape=(), dtype=tf.string),
    'embedding': Tensor(shape=(2048,), dtype=tf.float32),
    'hierarchical_section_title': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image_url': Text(shape=(), dtype=tf.string),
    'is_main_image': tf.bool,
    'language': Text(shape=(), dtype=tf.string),
    'metadata_url': Text(shape=(), dtype=tf.string),
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

Feature                                 | Class        | Shape           | Dtype      | Description
:-------------------------------------- | :----------- | :-------------- | :--------- | :----------
                                        | FeaturesDict |                 |            |
attribution_passes_lang_id              | Tensor       |                 | tf.bool    |
caption_alt_text_description            | Text         |                 | tf.string  |
caption_attribution_description         | Text         |                 | tf.string  |
caption_reference_description           | Text         |                 | tf.string  |
caption_title_and_reference_description | Text         |                 | tf.string  |
context_page_description                | Text         |                 | tf.string  |
context_section_description             | Text         |                 | tf.string  |
embedding                               | Tensor       | (2048,)         | tf.float32 |
hierarchical_section_title              | Text         |                 | tf.string  |
image                                   | Image        | (None, None, 3) | tf.uint8   |
image_url                               | Text         |                 | tf.string  |
is_main_image                           | Tensor       |                 | tf.bool    |
language                                | Text         |                 | tf.string  |
metadata_url                            | Text         |                 | tf.string  |
mime_type                               | Text         |                 | tf.string  |
original_height                         | Tensor       |                 | tf.int32   |
original_width                          | Tensor       |                 | tf.int32   |
page_changed_recently                   | Tensor       |                 | tf.bool    |
page_title                              | Text         |                 | tf.string  |
page_url                                | Text         |                 | tf.string  |
section_title                           | Text         |                 | tf.string  |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/wit_kaggle-train_with_extended_features-1.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wit_kaggle-train_with_extended_features-1.0.1.html";
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

## wit_kaggle/test_without_gold

*   **Config description**: Test samples (without gold answers) for the
    Wikipedia-Image/Caption Matching competition.

*   **Dataset size**: `3.37 GiB`

*   **Splits**:

Split                 | Examples
:-------------------- | -------:
`'test_without_gold'` | 92,366

*   **Feature structure**:

```python
FeaturesDict({
    'caption_title_and_reference_description': Text(shape=(), dtype=tf.string),
    'embedding': Tensor(shape=(2048,), dtype=tf.float32),
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image_url': Text(shape=(), dtype=tf.string),
    'metadata_url': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature                                 | Class        | Shape           | Dtype      | Description
:-------------------------------------- | :----------- | :-------------- | :--------- | :----------
                                        | FeaturesDict |                 |            |
caption_title_and_reference_description | Text         |                 | tf.string  |
embedding                               | Tensor       | (2048,)         | tf.float32 |
id                                      | Text         |                 | tf.string  |
image                                   | Image        | (None, None, 3) | tf.uint8   |
image_url                               | Text         |                 | tf.string  |
metadata_url                            | Text         |                 | tf.string  |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/wit_kaggle-test_without_gold-1.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wit_kaggle-test_without_gold-1.0.1.html";
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