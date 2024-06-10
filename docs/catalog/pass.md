<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="pass" />
  <meta itemprop="description" content="PASS is a large-scale image dataset that does not include any humans,&#10;human parts, or other personally identifiable information.&#10;It can be used for high-quality self-supervised pretraining while&#10;significantly reducing privacy concerns.&#10;&#10;PASS contains 1,439,589 images without any labels sourced from YFCC-100M.&#10;&#10;All images in this dataset are licenced under the CC-BY licence, as is the&#10;dataset itself.&#10;For YFCC-100M see  http://www.multimediacommons.org/.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;pass&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/pass-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/pass" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/pass/" />
  <meta itemprop="citation" content="@Article{asano21pass,&#10;author = &quot;Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi&quot;,&#10;title = &quot;PASS: An ImageNet replacement for self-supervised pretraining without humans&quot;,&#10;journal = &quot;NeurIPS Track on Datasets and Benchmarks&quot;,&#10;year = &quot;2021&quot;&#10;}" />
</div>

# `pass`


*   **Description**:

PASS is a large-scale image dataset that does not include any humans, human
parts, or other personally identifiable information. It can be used for
high-quality self-supervised pretraining while significantly reducing privacy
concerns.

PASS contains 1,439,589 images without any labels sourced from YFCC-100M.

All images in this dataset are licenced under the CC-BY licence, as is the
dataset itself. For YFCC-100M see http://www.multimediacommons.org/.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/pass">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.robots.ox.ac.uk/~vgg/data/pass/](https://www.robots.ox.ac.uk/~vgg/data/pass/)

*   **Source code**:
    [`tfds.datasets.pass.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/pass/pass_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `2.0.0`: v2: Removed 472 images from v1 as they contained humans. Also
        added metadata: datetaken and GPS.
    *   **`3.0.0`** (default): v3: Removed 131 images from v2 as they contained
        humans/tattos.

*   **Download size**: `167.30 GiB`

*   **Dataset size**: `166.43 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,439,588

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/creator_uname': Text(shape=(), dtype=string),
    'image/date_taken': Text(shape=(), dtype=string),
    'image/gps_lat': float32,
    'image/gps_lon': float32,
    'image/hash': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature             | Class        | Shape           | Dtype   | Description
:------------------ | :----------- | :-------------- | :------ | :----------
                    | FeaturesDict |                 |         |
image               | Image        | (None, None, 3) | uint8   |
image/creator_uname | Text         |                 | string  |
image/date_taken    | Text         |                 | string  |
image/gps_lat       | Tensor       |                 | float32 |
image/gps_lon       | Tensor       |                 | float32 |
image/hash          | Text         |                 | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/pass-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/pass-3.0.0.html";
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
@Article{asano21pass,
author = "Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi",
title = "PASS: An ImageNet replacement for self-supervised pretraining without humans",
journal = "NeurIPS Track on Datasets and Benchmarks",
year = "2021"
}
```

