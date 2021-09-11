<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="penguins" />
  <meta itemprop="description" content="Measurements for three penguin species observed in the Palmer Archipelago, Antarctica.&#10;&#10;These data were collected from 2007 - 2009 by Dr. Kristen Gorman with the [Palmer&#10;Station Long Term Ecological Research Program](https://pal.lternet.edu/), part&#10;of the [US Long Term Ecological Research Network](https://lternet.edu/). The&#10;data were originally imported from the [Environmental Data&#10;Initiative](https://environmentaldatainitiative.org/) (EDI) Data Portal, and are&#10;available for use by CC0 license (&quot;No Rights Reserved&quot;) in accordance with the&#10;Palmer Station Data Policy. This copy was imported from [Allison Horst&#x27;s GitHub&#10;repository](https://allisonhorst.github.io/palmerpenguins/articles/intro.html).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;penguins&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/penguins" />
  <meta itemprop="sameAs" content="https://allisonhorst.github.io/palmerpenguins/" />
  <meta itemprop="citation" content="@Manual{,&#10;  title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},&#10;  author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},&#10;  year = {2020},&#10;  note = {R package version 0.1.0},&#10;  doi = {10.5281/zenodo.3960218},&#10;  url = {https://allisonhorst.github.io/palmerpenguins/},&#10;}" />
</div>

# `penguins`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Measurements for three penguin species observed in the Palmer Archipelago,
Antarctica.

These data were collected from 2007 - 2009 by Dr. Kristen Gorman with the
[Palmer Station Long Term Ecological Research Program](https://pal.lternet.edu/),
part of the [US Long Term Ecological Research Network](https://lternet.edu/).
The data were originally imported from the
[Environmental Data Initiative](https://environmentaldatainitiative.org/) (EDI)
Data Portal, and are available for use by CC0 license ("No Rights Reserved") in
accordance with the Palmer Station Data Policy. This copy was imported from
[Allison Horst's GitHub repository](https://allisonhorst.github.io/palmerpenguins/articles/intro.html).

*   **Homepage**:
    [https://allisonhorst.github.io/palmerpenguins/](https://allisonhorst.github.io/palmerpenguins/)

*   **Source code**:
    [`tfds.structured.penguins.Penguins`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/penguins/penguins.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@Manual{,
  title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},
  author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},
  year = {2020},
  note = {R package version 0.1.0},
  doi = {10.5281/zenodo.3960218},
  url = {https://allisonhorst.github.io/palmerpenguins/},
}
```

## penguins/processed (default config)

*   **Config description**: `penguins/processed` is a drop-in replacement for
    the `iris` dataset. It contains 4 normalised numerical features presented as
    a single tensor, no missing values and the class label (species) is
    presented as an integer (n = 334).

*   **Download size**: `25.05 KiB`

*   **Dataset size**: `17.61 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 334

*   **Features**:

```python
FeaturesDict({
    'features': Tensor(shape=(4,), dtype=tf.float32),
    'species': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'species')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-processed-1.0.0.html";
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

## penguins/simple

*   **Config description**: `penguins/simple` has been processed from the raw
    dataset, with simplified class labels derived from text fields, missing
    values marked as NaN/NA and retains only 7 significant features (n = 344).

*   **Download size**: `13.20 KiB`

*   **Dataset size**: `56.10 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 344

*   **Features**:

```python
FeaturesDict({
    'body_mass_g': tf.float32,
    'culmen_depth_mm': tf.float32,
    'culmen_length_mm': tf.float32,
    'flipper_length_mm': tf.float32,
    'island': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sex': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'species': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'flipper_length_mm': 'flipper_length_mm', 'culmen_length_mm':
    'culmen_length_mm', 'island': 'island', 'sex': 'sex', 'culmen_depth_mm':
    'culmen_depth_mm', 'body_mass_g': 'body_mass_g', 'species': 'species'},
    'species')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-simple-1.0.0.html";
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

## penguins/raw

*   **Config description**: `penguins/raw` is the original, unprocessed copy
    from @allisonhorst, containing all 17 features, presented either as numeric
    types or as raw text (n = 344).

*   **Download size**: `49.72 KiB`

*   **Dataset size**: `164.51 KiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 344

*   **Features**:

```python
FeaturesDict({
    'Body Mass (g)': tf.float32,
    'Clutch Completion': Text(shape=(), dtype=tf.string),
    'Comments': Text(shape=(), dtype=tf.string),
    'Culmen Depth (mm)': tf.float32,
    'Culmen Length (mm)': tf.float32,
    'Date Egg': Text(shape=(), dtype=tf.string),
    'Delta 13 C (o/oo)': tf.float32,
    'Delta 15 N (o/oo)': tf.float32,
    'Flipper Length (mm)': tf.float32,
    'Individual ID': Text(shape=(), dtype=tf.string),
    'Island': Text(shape=(), dtype=tf.string),
    'Region': Text(shape=(), dtype=tf.string),
    'Sample Number': tf.int32,
    'Sex': Text(shape=(), dtype=tf.string),
    'Species': Text(shape=(), dtype=tf.string),
    'Stage': Text(shape=(), dtype=tf.string),
    'studyName': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-raw-1.0.0.html";
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