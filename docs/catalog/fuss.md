<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="fuss" />
  <meta itemprop="description" content="The Free Universal Sound Separation (FUSS) Dataset is a database of arbitrary&#10;sound mixtures and source-level references, for use in experiments on arbitrary&#10;sound separation.&#10;&#10;This is the official sound separation data for the DCASE2020 Challenge Task 4:&#10;Sound Event Detection and Separation in Domestic Environments.&#10;&#10;Overview: FUSS audio data is sourced from a pre-release of Freesound dataset&#10;known as (FSD50k), a sound event dataset composed of Freesound content annotated&#10;with labels from the AudioSet Ontology. Using the FSD50K labels, these source&#10;files have been screened such that they likely only contain a single type of&#10;sound. Labels are not provided for these source files, and are not considered&#10;part of the challenge. For the purpose of the DCASE Task4 Sound Separation and&#10;Event Detection challenge,  systems should not use FSD50K labels, even though&#10;they may become available upon FSD50K release.&#10;&#10;To create mixtures, 10 second clips of sources are convolved with simulated room&#10;impulse responses and added together. Each 10 second mixture contains between&#10;1 and 4 sources. Source files longer than 10 seconds are considered &quot;background&quot;&#10;sources. Every mixture contains one background source, which is active for the&#10;entire duration. We provide: a software recipe to create the dataset, the room&#10;impulse responses, and the original source audio.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;fuss&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/fuss" />
  <meta itemprop="sameAs" content="https://github.com/google-research/sound-separation/blob/master/datasets/fuss/FUSS_license_doc/README.md" />
  <meta itemprop="citation" content="\&#10;@inproceedings{wisdom2020fuss,&#10;  title = {What&#x27;s All the {FUSS} About Free Universal Sound Separation Data?},&#10;  author = {Scott Wisdom and Hakan Erdogan and Daniel P. W. Ellis and Romain Serizel and Nicolas Turpault and Eduardo Fonseca and Justin Salamon and Prem Seetharaman and John R. Hershey},&#10;  year = {2020},&#10;  url = {https://arxiv.org/abs/2011.00803},&#10;}&#10;&#10;@inproceedings{fonseca2020fsd50k,&#10;  author = {Eduardo Fonseca and Xavier Favory and Jordi Pons and Frederic Font Corbera and Xavier Serra},&#10;  title = {{FSD}50k: an open dataset of human-labeled sound events},&#10;  year = {2020},&#10;  url = {https://arxiv.org/abs/2010.00475},&#10;}" />
</div>

# `fuss`


*   **Description**:

The Free Universal Sound Separation (FUSS) Dataset is a database of arbitrary
sound mixtures and source-level references, for use in experiments on arbitrary
sound separation.

This is the official sound separation data for the DCASE2020 Challenge Task 4:
Sound Event Detection and Separation in Domestic Environments.

Overview: FUSS audio data is sourced from a pre-release of Freesound dataset
known as (FSD50k), a sound event dataset composed of Freesound content annotated
with labels from the AudioSet Ontology. Using the FSD50K labels, these source
files have been screened such that they likely only contain a single type of
sound. Labels are not provided for these source files, and are not considered
part of the challenge. For the purpose of the DCASE Task4 Sound Separation and
Event Detection challenge, systems should not use FSD50K labels, even though
they may become available upon FSD50K release.

To create mixtures, 10 second clips of sources are convolved with simulated room
impulse responses and added together. Each 10 second mixture contains between 1
and 4 sources. Source files longer than 10 seconds are considered "background"
sources. Every mixture contains one background source, which is active for the
entire duration. We provide: a software recipe to create the dataset, the room
impulse responses, and the original source audio.

*   **Homepage**:
    [https://github.com/google-research/sound-separation/blob/master/datasets/fuss/FUSS_license_doc/README.md](https://github.com/google-research/sound-separation/blob/master/datasets/fuss/FUSS_license_doc/README.md)

*   **Source code**:
    [`tfds.audio.Fuss`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/fuss.py)

*   **Versions**:

    *   **`1.2.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 20,000
`'validation'` | 1,000

*   **Features**:

```python
FeaturesDict({
    'id': tf.string,
    'jams': tf.string,
    'mixture_audio': Audio(shape=(160000,), dtype=tf.int16),
    'segments': Sequence({
        'end_time_seconds': tf.float32,
        'label': tf.string,
        'start_time_seconds': tf.float32,
    }),
    'sources': Sequence({
        'audio': Audio(shape=(160000,), dtype=tf.int16),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=4),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('mixture_audio', 'sources')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
\
@inproceedings{wisdom2020fuss,
  title = {What's All the {FUSS} About Free Universal Sound Separation Data?},
  author = {Scott Wisdom and Hakan Erdogan and Daniel P. W. Ellis and Romain Serizel and Nicolas Turpault and Eduardo Fonseca and Justin Salamon and Prem Seetharaman and John R. Hershey},
  year = {2020},
  url = {https://arxiv.org/abs/2011.00803},
}

@inproceedings{fonseca2020fsd50k,
  author = {Eduardo Fonseca and Xavier Favory and Jordi Pons and Frederic Font Corbera and Xavier Serra},
  title = {{FSD}50k: an open dataset of human-labeled sound events},
  year = {2020},
  url = {https://arxiv.org/abs/2010.00475},
}
```

## fuss/reverberant (default config)

*   **Config description**: Default reverberated audio.

*   **Download size**: `7.35 GiB`

*   **Dataset size**: `43.20 GiB`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/fuss-reverberant-1.2.0.html";
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

## fuss/unprocessed

*   **Config description**: Unprocessed audio without additional reverberation.

*   **Download size**: `8.28 GiB`

*   **Dataset size**: `45.58 GiB`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/fuss-unprocessed-1.2.0.html";
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