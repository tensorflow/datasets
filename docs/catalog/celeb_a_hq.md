<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="celeb_a_hq" />
  <meta itemprop="description" content="High-quality version of the CELEBA dataset, consisting of 30000 images in 1024 x&#10;1024 resolution.&#10;&#10;Note: CelebAHQ dataset may contain potential bias. The fairness indicators&#10;[example](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)&#10;goes into detail about several considerations to keep in mind while using the&#10;CelebAHQ dataset.&#10;&#10;WARNING: This dataset currently requires you to prepare images on your own.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;celeb_a_hq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-1024-2.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/celeb_a_hq" />
  <meta itemprop="sameAs" content="https://github.com/tkarras/progressive_growing_of_gans" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1710-10196,&#10;  author    = {Tero Karras and&#10;               Timo Aila and&#10;               Samuli Laine and&#10;               Jaakko Lehtinen},&#10;  title     = {Progressive Growing of GANs for Improved Quality, Stability, and Variation},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1710.10196},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1710.10196},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1710.10196},&#10;  timestamp = {Mon, 13 Aug 2018 16:46:42 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10196},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `celeb_a_hq`


Warning: Manual download required. See instructions below.

*   **Description**:

High-quality version of the CELEBA dataset, consisting of 30000 images in 1024 x
1024 resolution.

Note: CelebAHQ dataset may contain potential bias. The fairness indicators
[example](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)
goes into detail about several considerations to keep in mind while using the
CelebAHQ dataset.

WARNING: This dataset currently requires you to prepare images on your own.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/celeba-hq">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/tkarras/progressive_growing_of_gans](https://github.com/tkarras/progressive_growing_of_gans)

*   **Source code**:
    [`tfds.datasets.celeb_a_hq.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/celeb_a_hq/celeb_a_hq_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain multiple tar files with images (data2x2.tar,
    data4x4.tar .. data1024x1024.tar).
    Detailed instructions are here:
    https://github.com/tkarras/progressive_growing_of_gans#preparing-datasets-for-training

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 30,000

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@article{DBLP:journals/corr/abs-1710-10196,
  author    = {Tero Karras and
               Timo Aila and
               Samuli Laine and
               Jaakko Lehtinen},
  title     = {Progressive Growing of GANs for Improved Quality, Stability, and Variation},
  journal   = {CoRR},
  volume    = {abs/1710.10196},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.10196},
  archivePrefix = {arXiv},
  eprint    = {1710.10196},
  timestamp = {Mon, 13 Aug 2018 16:46:42 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-10196},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


## celeb_a_hq/1024 (default config)

*   **Config description**: CelebaHQ images in 1024 x 1024 resolution

*   **Dataset size**: `54.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(1024, 1024, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape           | Dtype  | Description
:------------- | :----------- | :-------------- | :----- | :----------
               | FeaturesDict |                 |        |
image          | Image        | (1024, 1024, 3) | uint8  |
image/filename | Text         |                 | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-1024-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-1024-2.0.0.html";
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

## celeb_a_hq/512

*   **Config description**: CelebaHQ images in 512 x 512 resolution

*   **Dataset size**: `15.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(512, 512, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape         | Dtype  | Description
:------------- | :----------- | :------------ | :----- | :----------
               | FeaturesDict |               |        |
image          | Image        | (512, 512, 3) | uint8  |
image/filename | Text         |               | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-512-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-512-2.0.0.html";
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

## celeb_a_hq/256

*   **Config description**: CelebaHQ images in 256 x 256 resolution

*   **Dataset size**: `4.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape         | Dtype  | Description
:------------- | :----------- | :------------ | :----- | :----------
               | FeaturesDict |               |        |
image          | Image        | (256, 256, 3) | uint8  |
image/filename | Text         |               | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-256-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-256-2.0.0.html";
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

## celeb_a_hq/128

*   **Config description**: CelebaHQ images in 128 x 128 resolution

*   **Dataset size**: `1.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(128, 128, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape         | Dtype  | Description
:------------- | :----------- | :------------ | :----- | :----------
               | FeaturesDict |               |        |
image          | Image        | (128, 128, 3) | uint8  |
image/filename | Text         |               | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-128-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-128-2.0.0.html";
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

## celeb_a_hq/64

*   **Config description**: CelebaHQ images in 64 x 64 resolution

*   **Dataset size**: `310.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(64, 64, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype  | Description
:------------- | :----------- | :---------- | :----- | :----------
               | FeaturesDict |             |        |
image          | Image        | (64, 64, 3) | uint8  |
image/filename | Text         |             | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-64-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-64-2.0.0.html";
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

## celeb_a_hq/32

*   **Config description**: CelebaHQ images in 32 x 32 resolution

*   **Dataset size**: `85.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype  | Description
:------------- | :----------- | :---------- | :----- | :----------
               | FeaturesDict |             |        |
image          | Image        | (32, 32, 3) | uint8  |
image/filename | Text         |             | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-32-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-32-2.0.0.html";
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

## celeb_a_hq/16

*   **Config description**: CelebaHQ images in 16 x 16 resolution

*   **Dataset size**: `25.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(16, 16, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype  | Description
:------------- | :----------- | :---------- | :----- | :----------
               | FeaturesDict |             |        |
image          | Image        | (16, 16, 3) | uint8  |
image/filename | Text         |             | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-16-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-16-2.0.0.html";
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

## celeb_a_hq/8

*   **Config description**: CelebaHQ images in 8 x 8 resolution

*   **Dataset size**: `9.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(8, 8, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape     | Dtype  | Description
:------------- | :----------- | :-------- | :----- | :----------
               | FeaturesDict |           |        |
image          | Image        | (8, 8, 3) | uint8  |
image/filename | Text         |           | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-8-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-8-2.0.0.html";
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

## celeb_a_hq/4

*   **Config description**: CelebaHQ images in 4 x 4 resolution

*   **Dataset size**: `5.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(4, 4, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape     | Dtype  | Description
:------------- | :----------- | :-------- | :----- | :----------
               | FeaturesDict |           |        |
image          | Image        | (4, 4, 3) | uint8  |
image/filename | Text         |           | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-4-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-4-2.0.0.html";
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

## celeb_a_hq/2

*   **Config description**: CelebaHQ images in 2 x 2 resolution

*   **Dataset size**: `3.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(2, 2, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape     | Dtype  | Description
:------------- | :----------- | :-------- | :----- | :----------
               | FeaturesDict |           |        |
image          | Image        | (2, 2, 3) | uint8  |
image/filename | Text         |           | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-2-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-2-2.0.0.html";
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

## celeb_a_hq/1

*   **Config description**: CelebaHQ images in 1 x 1 resolution

*   **Dataset size**: `3.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(1, 1, 3), dtype=uint8),
    'image/filename': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape     | Dtype  | Description
:------------- | :----------- | :-------- | :----- | :----------
               | FeaturesDict |           |        |
image          | Image        | (1, 1, 3) | uint8  |
image/filename | Text         |           | string |

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a_hq-1-2.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a_hq-1-2.0.0.html";
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