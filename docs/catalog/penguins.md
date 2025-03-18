<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="penguins" />
  <meta itemprop="description" content="Measurements for three penguin species observed in the Palmer Archipelago,&#10;Antarctica.&#10;&#10;These data were collected from 2007 - 2009 by Dr. Kristen Gorman with the&#10;[Palmer Station Long Term Ecological Research Program](https://pal.lternet.edu/),&#10;part of the [US Long Term Ecological Research Network](https://lternet.edu/).&#10;The data were originally imported from the&#10;[Environmental Data Initiative](https://environmentaldatainitiative.org/) (EDI)&#10;Data Portal, and are available for use by CC0 license (&quot;No Rights Reserved&quot;) in&#10;accordance with the Palmer Station Data Policy. This copy was imported from&#10;[Allison Horst&#x27;s GitHub repository](https://allisonhorst.github.io/palmerpenguins/articles/intro.html).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;penguins&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/penguins" />
  <meta itemprop="sameAs" content="https://allisonhorst.github.io/palmerpenguins/" />
  <meta itemprop="citation" content="@Manual{,&#10;  title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},&#10;  author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},&#10;  year = {2020},&#10;  note = {R package version 0.1.0},&#10;  doi = {10.5281/zenodo.3960218},&#10;  url = {https://allisonhorst.github.io/palmerpenguins/},&#10;}" />
</div>

# `penguins`


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
    [`tfds.datasets.penguins.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/penguins/penguins_dataset_builder.py)

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

*   **Feature structure**:

```python
FeaturesDict({
    'features': Tensor(shape=(4,), dtype=float32),
    'species': ClassLabel(shape=(), dtype=int64, num_classes=3),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype   | Description
:------- | :----------- | :---- | :------ | :----------
         | FeaturesDict |       |         |
features | Tensor       | (4,)  | float32 |
species  | ClassLabel   |       | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('features', 'species')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-processed-1.0.0.html";
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

*   **Feature structure**:

```python
FeaturesDict({
    'body_mass_g': float32,
    'culmen_depth_mm': float32,
    'culmen_length_mm': float32,
    'flipper_length_mm': float32,
    'island': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'sex': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'species': ClassLabel(shape=(), dtype=int64, num_classes=3),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype   | Description
:---------------- | :----------- | :---- | :------ | :----------
                  | FeaturesDict |       |         |
body_mass_g       | Tensor       |       | float32 |
culmen_depth_mm   | Tensor       |       | float32 |
culmen_length_mm  | Tensor       |       | float32 |
flipper_length_mm | Tensor       |       | float32 |
island            | ClassLabel   |       | int64   |
sex               | ClassLabel   |       | int64   |
species           | ClassLabel   |       | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'body_mass_g': 'body_mass_g', 'culmen_depth_mm': 'culmen_depth_mm',
    'culmen_length_mm': 'culmen_length_mm', 'flipper_length_mm':
    'flipper_length_mm', 'island': 'island', 'sex': 'sex', 'species':
    'species'}, 'species')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-simple-1.0.0.html";
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

*   **Feature structure**:

```python
FeaturesDict({
    'Body Mass (g)': float32,
    'Clutch Completion': Text(shape=(), dtype=string),
    'Comments': Text(shape=(), dtype=string),
    'Culmen Depth (mm)': float32,
    'Culmen Length (mm)': float32,
    'Date Egg': Text(shape=(), dtype=string),
    'Delta 13 C (o/oo)': float32,
    'Delta 15 N (o/oo)': float32,
    'Flipper Length (mm)': float32,
    'Individual ID': Text(shape=(), dtype=string),
    'Island': Text(shape=(), dtype=string),
    'Region': Text(shape=(), dtype=string),
    'Sample Number': int32,
    'Sex': Text(shape=(), dtype=string),
    'Species': Text(shape=(), dtype=string),
    'Stage': Text(shape=(), dtype=string),
    'studyName': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature             | Class        | Shape | Dtype   | Description
:------------------ | :----------- | :---- | :------ | :----------
                    | FeaturesDict |       |         |
Body Mass (g)       | Tensor       |       | float32 |
Clutch Completion   | Text         |       | string  |
Comments            | Text         |       | string  |
Culmen Depth (mm)   | Tensor       |       | float32 |
Culmen Length (mm)  | Tensor       |       | float32 |
Date Egg            | Text         |       | string  |
Delta 13 C (o/oo)   | Tensor       |       | float32 |
Delta 15 N (o/oo)   | Tensor       |       | float32 |
Flipper Length (mm) | Tensor       |       | float32 |
Individual ID       | Text         |       | string  |
Island              | Text         |       | string  |
Region              | Text         |       | string  |
Sample Number       | Tensor       |       | int32   |
Sex                 | Text         |       | string  |
Species             | Text         |       | string  |
Stage               | Text         |       | string  |
studyName           | Text         |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/penguins-raw-1.0.0.html";
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