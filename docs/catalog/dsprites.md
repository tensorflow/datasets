<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dsprites" />
  <meta itemprop="description" content="dSprites is a dataset of 2D shapes procedurally generated from 6 ground truth&#10;independent latent factors. These factors are *color*, *shape*, *scale*,&#10;*rotation*, *x* and *y* positions of a sprite.&#10;&#10;All possible combinations of these latents are present exactly once, generating&#10;N = 737280 total images.&#10;&#10;### Latent factor values&#10;&#10;*   Color: white&#10;*   Shape: square, ellipse, heart&#10;*   Scale: 6 values linearly spaced in [0.5, 1]&#10;*   Orientation: 40 values in [0, 2 pi]&#10;*   Position X: 32 values in [0, 1]&#10;*   Position Y: 32 values in [0, 1]&#10;&#10;We varied one latent at a time (starting from Position Y, then Position X, etc),&#10;and sequentially stored the images in fixed order. Hence the order along the&#10;first dimension is fixed and allows you to map back to the value of the latents&#10;corresponding to that image.&#10;&#10;We chose the latents values deliberately to have the smallest step changes while&#10;ensuring that all pixel outputs were different. No noise was added.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dsprites&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/dsprites-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dsprites" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/dsprites-dataset" />
  <meta itemprop="citation" content="@misc{dsprites17,&#10;author = {Loic Matthey and Irina Higgins and Demis Hassabis and Alexander Lerchner},&#10;title = {dSprites: Disentanglement testing Sprites dataset},&#10;howpublished= {https://github.com/deepmind/dsprites-dataset/},&#10;year = &quot;2017&quot;,&#10;}" />
</div>

# `dsprites`


*   **Description**:

dSprites is a dataset of 2D shapes procedurally generated from 6 ground truth
independent latent factors. These factors are *color*, *shape*, *scale*,
*rotation*, *x* and *y* positions of a sprite.

All possible combinations of these latents are present exactly once, generating
N = 737280 total images.

### Latent factor values

*   Color: white
*   Shape: square, ellipse, heart
*   Scale: 6 values linearly spaced in [0.5, 1]
*   Orientation: 40 values in [0, 2 pi]
*   Position X: 32 values in [0, 1]
*   Position Y: 32 values in [0, 1]

We varied one latent at a time (starting from Position Y, then Position X, etc),
and sequentially stored the images in fixed order. Hence the order along the
first dimension is fixed and allows you to map back to the value of the latents
corresponding to that image.

We chose the latents values deliberately to have the smallest step changes while
ensuring that all pixel outputs were different. No noise was added.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/dsprites">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/deepmind/dsprites-dataset](https://github.com/deepmind/dsprites-dataset)

*   **Source code**:
    [`tfds.datasets.dsprites.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/dsprites/dsprites_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)
    *   `2.1.0`: No release notes.

*   **Download size**: `26.73 MiB`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 737,280

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(64, 64, 1), dtype=uint8),
    'label_orientation': ClassLabel(shape=(), dtype=int64, num_classes=40),
    'label_scale': ClassLabel(shape=(), dtype=int64, num_classes=6),
    'label_shape': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'label_x_position': ClassLabel(shape=(), dtype=int64, num_classes=32),
    'label_y_position': ClassLabel(shape=(), dtype=int64, num_classes=32),
    'value_orientation': float32,
    'value_scale': float32,
    'value_shape': float32,
    'value_x_position': float32,
    'value_y_position': float32,
})
```

*   **Feature documentation**:

Feature           | Class        | Shape       | Dtype   | Description
:---------------- | :----------- | :---------- | :------ | :----------
                  | FeaturesDict |             |         |
image             | Image        | (64, 64, 1) | uint8   |
label_orientation | ClassLabel   |             | int64   |
label_scale       | ClassLabel   |             | int64   |
label_shape       | ClassLabel   |             | int64   |
label_x_position  | ClassLabel   |             | int64   |
label_y_position  | ClassLabel   |             | int64   |
value_orientation | Tensor       |             | float32 |
value_scale       | Tensor       |             | float32 |
value_shape       | Tensor       |             | float32 |
value_x_position  | Tensor       |             | float32 |
value_y_position  | Tensor       |             | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/dsprites-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dsprites-2.0.0.html";
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
@misc{dsprites17,
author = {Loic Matthey and Irina Higgins and Demis Hassabis and Alexander Lerchner},
title = {dSprites: Disentanglement testing Sprites dataset},
howpublished= {https://github.com/deepmind/dsprites-dataset/},
year = "2017",
}
```

