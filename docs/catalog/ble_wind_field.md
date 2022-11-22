<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ble_wind_field" />
  <meta itemprop="description" content="Historical wind field dataset for the Balloon Learning Environment.&#10;&#10;4D wind fields, where the dimensions are latitude, longitude, altitude, and&#10;time. Each entry contains two float values (_u_ and _v_) which indicate the wind&#10;direction and magnitude at the specified location, altitude, and time.&#10;&#10;Acknowledgements:&#10;&#10;Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,&#10;Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,&#10;Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,&#10;Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,&#10;Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,&#10;Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,&#10;Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,&#10;Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF&#10;atmospheric reanalyses of the global climate. Copernicus Climate Change Service&#10;(C3S) Data Store (CDS). (Accessed on 01-04-2021)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ble_wind_field&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ble_wind_field" />
  <meta itemprop="sameAs" content="https://github.com/google/balloon-learning-environment" />
  <meta itemprop="citation" content="@software{ble2021,&#10;author = {Greaves, Joshua and Candido, Salvatore and Dumoulin, Vincent and Goroshin, Ross and Ponda, Sameera S. and Bellemare, Marc G. and Castro, Pablo Samuel},&#10;month = {12},&#10;title = {{Balloon Learning Environment}},&#10;url = {https://github.com/google/balloon-learning-environment},&#10;version = {1.0.0},&#10;year = {2021}&#10;}&#10;&#10;Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,&#10;Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,&#10;Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,&#10;Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,&#10;Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,&#10;Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,&#10;Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,&#10;Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF&#10;atmospheric reanalyses of the global climate. Copernicus Climate Change Service&#10;(C3S) Data Store (CDS). (Accessed on 01-04-2021)" />
</div>

# `ble_wind_field`


*   **Description**:

Historical wind field dataset for the Balloon Learning Environment.

4D wind fields, where the dimensions are latitude, longitude, altitude, and
time. Each entry contains two float values (*u* and *v*) which indicate the wind
direction and magnitude at the specified location, altitude, and time.

Acknowledgements:

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,
Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,
Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,
Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,
Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,
Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,
Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF
atmospheric reanalyses of the global climate. Copernicus Climate Change Service
(C3S) Data Store (CDS). (Accessed on 01-04-2021)

*   **Homepage**:
    [https://github.com/google/balloon-learning-environment](https://github.com/google/balloon-learning-environment)

*   **Source code**:
    [`tfds.datasets.ble_wind_field.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/ble_wind_field/ble_wind_field_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Feature structure**:

```python
FeaturesDict({
    'field': Tensor(shape=(21, 21, 10, 9, 2), dtype=float32),
})
```

*   **Feature documentation**:

Feature | Class        | Shape              | Dtype   | Description
:------ | :----------- | :----------------- | :------ | :----------
        | FeaturesDict |                    |         |
field   | Tensor       | (21, 21, 10, 9, 2) | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@software{ble2021,
author = {Greaves, Joshua and Candido, Salvatore and Dumoulin, Vincent and Goroshin, Ross and Ponda, Sameera S. and Bellemare, Marc G. and Castro, Pablo Samuel},
month = {12},
title = {{Balloon Learning Environment}},
url = {https://github.com/google/balloon-learning-environment},
version = {1.0.0},
year = {2021}
}

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,
Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,
Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,
Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,
Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,
Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,
Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF
atmospheric reanalyses of the global climate. Copernicus Climate Change Service
(C3S) Data Store (CDS). (Accessed on 01-04-2021)
```


## ble_wind_field/full (default config)

*   **Config description**: The entire historical wind field dataset.

*   **Dataset size**: `79.53 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 290,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ble_wind_field-full-1.0.0.html";
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

## ble_wind_field/small

*   **Config description**: Small sample of 256 fields from the dataset.

*   **Dataset size**: `71.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 256

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ble_wind_field-small-1.0.0.html";
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