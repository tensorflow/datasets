<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="duke_ultrasound" />
  <meta itemprop="description" content="DukeUltrasound is an ultrasound dataset collected at Duke University with a&#10;Verasonics c52v probe. It contains delay-and-sum (DAS) beamformed data as well&#10;as data post-processed with Siemens Dynamic TCE for speckle reduction, contrast&#10;enhancement and improvement in conspicuity of anatomical structures. These data&#10;were collected with support from the National Institute of Biomedical Imaging&#10;and Bioengineering under Grant R01-EB026574 and National Institutes of Health&#10;under Grant 5T32GM007171-44. A usage example is available&#10;[here](https://colab.research.google.com/drive/1R_ARqpWoiHcUQWg1Fxwyx-ZkLi0IZ5qs).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;duke_ultrasound&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/duke_ultrasound" />
  <meta itemprop="sameAs" content="https://github.com/ouwen/mimicknet" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1908-05782,&#10;  author    = {Ouwen Huang and&#10;               Will Long and&#10;               Nick Bottenus and&#10;               Gregg E. Trahey and&#10;               Sina Farsiu and&#10;               Mark L. Palmeri},&#10;  title     = {MimickNet, Matching Clinical Post-Processing Under Realistic Black-Box&#10;               Constraints},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1908.05782},&#10;  year      = {2019},&#10;  url       = {http://arxiv.org/abs/1908.05782},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1908.05782},&#10;  timestamp = {Mon, 19 Aug 2019 13:21:03 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1908-05782},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `duke_ultrasound`


*   **Description**:

DukeUltrasound is an ultrasound dataset collected at Duke University with a
Verasonics c52v probe. It contains delay-and-sum (DAS) beamformed data as well
as data post-processed with Siemens Dynamic TCE for speckle reduction, contrast
enhancement and improvement in conspicuity of anatomical structures. These data
were collected with support from the National Institute of Biomedical Imaging
and Bioengineering under Grant R01-EB026574 and National Institutes of Health
under Grant 5T32GM007171-44. A usage example is available
[here](https://colab.research.google.com/drive/1R_ARqpWoiHcUQWg1Fxwyx-ZkLi0IZ5qs).

*   **Homepage**:
    [https://github.com/ouwen/mimicknet](https://github.com/ouwen/mimicknet)

*   **Source code**:
    [`tfds.datasets.duke_ultrasound.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/duke_ultrasound/duke_ultrasound_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.0.1`: Fixes parsing of boolean field `harmonic`.
    *   **`2.0.0`** (default): Fix timestamp_id from %Y%m%d%H%M%S to posix
        timestamp.

*   **Download size**: `12.78 GiB`

*   **Dataset size**: `13.79 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'A'`          | 1,362
`'B'`          | 1,194
`'MARK'`       | 420
`'test'`       | 438
`'train'`      | 2,556
`'validation'` | 278

*   **Feature structure**:

```python
FeaturesDict({
    'das': FeaturesDict({
        'dB': Tensor(shape=(None,), dtype=float32),
        'imag': Tensor(shape=(None,), dtype=float32),
        'real': Tensor(shape=(None,), dtype=float32),
    }),
    'dtce': Tensor(shape=(None,), dtype=float32),
    'f0_hz': float32,
    'final_angle': float32,
    'final_radius': float32,
    'focus_cm': float32,
    'harmonic': bool,
    'height': uint32,
    'initial_angle': float32,
    'initial_radius': float32,
    'probe': string,
    'scanner': string,
    'target': string,
    'timestamp_id': uint32,
    'voltage': float32,
    'width': uint32,
})
```

*   **Feature documentation**:

Feature        | Class        | Shape   | Dtype   | Description
:------------- | :----------- | :------ | :------ | :----------
               | FeaturesDict |         |         |
das            | FeaturesDict |         |         |
das/dB         | Tensor       | (None,) | float32 |
das/imag       | Tensor       | (None,) | float32 |
das/real       | Tensor       | (None,) | float32 |
dtce           | Tensor       | (None,) | float32 |
f0_hz          | Tensor       |         | float32 |
final_angle    | Tensor       |         | float32 |
final_radius   | Tensor       |         | float32 |
focus_cm       | Tensor       |         | float32 |
harmonic       | Tensor       |         | bool    |
height         | Tensor       |         | uint32  |
initial_angle  | Tensor       |         | float32 |
initial_radius | Tensor       |         | float32 |
probe          | Tensor       |         | string  |
scanner        | Tensor       |         | string  |
target         | Tensor       |         | string  |
timestamp_id   | Tensor       |         | uint32  |
voltage        | Tensor       |         | float32 |
width          | Tensor       |         | uint32  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('das/dB', 'dtce')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/duke_ultrasound-2.0.0.html";
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
@article{DBLP:journals/corr/abs-1908-05782,
  author    = {Ouwen Huang and
               Will Long and
               Nick Bottenus and
               Gregg E. Trahey and
               Sina Farsiu and
               Mark L. Palmeri},
  title     = {MimickNet, Matching Clinical Post-Processing Under Realistic Black-Box
               Constraints},
  journal   = {CoRR},
  volume    = {abs/1908.05782},
  year      = {2019},
  url       = {http://arxiv.org/abs/1908.05782},
  archivePrefix = {arXiv},
  eprint    = {1908.05782},
  timestamp = {Mon, 19 Aug 2019 13:21:03 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1908-05782},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

