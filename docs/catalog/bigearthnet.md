<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="bigearthnet" />
  <meta itemprop="description" content="The BigEarthNet is a new large-scale Sentinel-2 benchmark archive, consisting of&#10;590,326 Sentinel-2 image patches. The image patch size on the ground is 1.2 x&#10;1.2 km with variable image size depending on the channel resolution. This is a&#10;multi-label dataset with 43 imbalanced labels.&#10;&#10;To construct the BigEarthNet, 125 Sentinel-2 tiles acquired between June 2017&#10;and May 2018 over the 10 countries (Austria, Belgium, Finland, Ireland, Kosovo,&#10;Lithuania, Luxembourg, Portugal, Serbia, Switzerland) of Europe were initially&#10;selected. All the tiles were atmospherically corrected by the Sentinel-2 Level&#10;2A product generation and formatting tool (sen2cor). Then, they were divided&#10;into 590,326 non-overlapping image patches. Each image patch was annotated by&#10;the multiple land-cover classes (i.e., multi-labels) that were provided from the&#10;CORINE Land Cover database of the year 2018 (CLC 2018).&#10;&#10;Bands and pixel resolution in meters:&#10;&#10;*   B01: Coastal aerosol; 60m&#10;*   B02: Blue; 10m&#10;*   B03: Green; 10m&#10;*   B04: Red; 10m&#10;*   B05: Vegetation red edge; 20m&#10;*   B06: Vegetation red edge; 20m&#10;*   B07: Vegetation red edge; 20m&#10;*   B08: NIR; 10m&#10;*   B09: Water vapor; 60m&#10;*   B11: SWIR; 20m&#10;*   B12: SWIR; 20m&#10;*   B8A: Narrow NIR; 20m&#10;&#10;License: Community Data License Agreement - Permissive, Version 1.0.&#10;&#10;URL: http://bigearth.net/&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;bigearthnet&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/bigearthnet-rgb-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/bigearthnet" />
  <meta itemprop="sameAs" content="http://bigearth.net" />
  <meta itemprop="citation" content="@article{Sumbul2019BigEarthNetAL,&#10;  title={BigEarthNet: A Large-Scale Benchmark Archive For Remote Sensing Image Understanding},&#10;  author={Gencer Sumbul and Marcela Charfuelan and Beg{&quot;u}m Demir and Volker Markl},&#10;  journal={CoRR},&#10;  year={2019},&#10;  volume={abs/1902.06148}&#10;}" />
</div>

# `bigearthnet`


*   **Description**:

The BigEarthNet is a new large-scale Sentinel-2 benchmark archive, consisting of
590,326 Sentinel-2 image patches. The image patch size on the ground is 1.2 x
1.2 km with variable image size depending on the channel resolution. This is a
multi-label dataset with 43 imbalanced labels.

To construct the BigEarthNet, 125 Sentinel-2 tiles acquired between June 2017
and May 2018 over the 10 countries (Austria, Belgium, Finland, Ireland, Kosovo,
Lithuania, Luxembourg, Portugal, Serbia, Switzerland) of Europe were initially
selected. All the tiles were atmospherically corrected by the Sentinel-2 Level
2A product generation and formatting tool (sen2cor). Then, they were divided
into 590,326 non-overlapping image patches. Each image patch was annotated by
the multiple land-cover classes (i.e., multi-labels) that were provided from the
CORINE Land Cover database of the year 2018 (CLC 2018).

Bands and pixel resolution in meters:

*   B01: Coastal aerosol; 60m
*   B02: Blue; 10m
*   B03: Green; 10m
*   B04: Red; 10m
*   B05: Vegetation red edge; 20m
*   B06: Vegetation red edge; 20m
*   B07: Vegetation red edge; 20m
*   B08: NIR; 10m
*   B09: Water vapor; 60m
*   B11: SWIR; 20m
*   B12: SWIR; 20m
*   B8A: Narrow NIR; 20m

License: Community Data License Agreement - Permissive, Version 1.0.

URL: http://bigearth.net/

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/bigearthnet">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [http://bigearth.net](http://bigearth.net)

*   **Source code**:
    [`tfds.datasets.bigearthnet.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/bigearthnet/bigearthnet_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `65.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 590,326

*   **Citation**:

```
@article{Sumbul2019BigEarthNetAL,
  title={BigEarthNet: A Large-Scale Benchmark Archive For Remote Sensing Image Understanding},
  author={Gencer Sumbul and Marcela Charfuelan and Beg{"u}m Demir and Volker Markl},
  journal={CoRR},
  year={2019},
  volume={abs/1902.06148}
}
```


## bigearthnet/rgb (default config)

*   **Config description**: Sentinel-2 RGB channels

*   **Dataset size**: `14.07 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=string),
    'image': Image(shape=(120, 120, 3), dtype=uint8),
    'labels': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=43)),
    'metadata': FeaturesDict({
        'acquisition_date': Text(shape=(), dtype=string),
        'coordinates': FeaturesDict({
            'lrx': int64,
            'lry': int64,
            'ulx': int64,
            'uly': int64,
        }),
        'projection': Text(shape=(), dtype=string),
        'tile_source': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                   | Class                | Shape         | Dtype  | Description
:------------------------ | :------------------- | :------------ | :----- | :----------
                          | FeaturesDict         |               |        |
filename                  | Text                 |               | string |
image                     | Image                | (120, 120, 3) | uint8  |
labels                    | Sequence(ClassLabel) | (None,)       | int64  |
metadata                  | FeaturesDict         |               |        |
metadata/acquisition_date | Text                 |               | string |
metadata/coordinates      | FeaturesDict         |               |        |
metadata/coordinates/lrx  | Tensor               |               | int64  |
metadata/coordinates/lry  | Tensor               |               | int64  |
metadata/coordinates/ulx  | Tensor               |               | int64  |
metadata/coordinates/uly  | Tensor               |               | int64  |
metadata/projection       | Text                 |               | string |
metadata/tile_source      | Text                 |               | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'labels')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/bigearthnet-rgb-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bigearthnet-rgb-1.0.0.html";
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

## bigearthnet/all

*   **Config description**: 13 Sentinel-2 channels

*   **Dataset size**: `176.63 GiB`

*   **Feature structure**:

```python
FeaturesDict({
    'B01': Tensor(shape=(20, 20), dtype=float32),
    'B02': Tensor(shape=(120, 120), dtype=float32),
    'B03': Tensor(shape=(120, 120), dtype=float32),
    'B04': Tensor(shape=(120, 120), dtype=float32),
    'B05': Tensor(shape=(60, 60), dtype=float32),
    'B06': Tensor(shape=(60, 60), dtype=float32),
    'B07': Tensor(shape=(60, 60), dtype=float32),
    'B08': Tensor(shape=(120, 120), dtype=float32),
    'B09': Tensor(shape=(20, 20), dtype=float32),
    'B11': Tensor(shape=(60, 60), dtype=float32),
    'B12': Tensor(shape=(60, 60), dtype=float32),
    'B8A': Tensor(shape=(60, 60), dtype=float32),
    'filename': Text(shape=(), dtype=string),
    'labels': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=43)),
    'metadata': FeaturesDict({
        'acquisition_date': Text(shape=(), dtype=string),
        'coordinates': FeaturesDict({
            'lrx': int64,
            'lry': int64,
            'ulx': int64,
            'uly': int64,
        }),
        'projection': Text(shape=(), dtype=string),
        'tile_source': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                   | Class                | Shape      | Dtype   | Description
:------------------------ | :------------------- | :--------- | :------ | :----------
                          | FeaturesDict         |            |         |
B01                       | Tensor               | (20, 20)   | float32 |
B02                       | Tensor               | (120, 120) | float32 |
B03                       | Tensor               | (120, 120) | float32 |
B04                       | Tensor               | (120, 120) | float32 |
B05                       | Tensor               | (60, 60)   | float32 |
B06                       | Tensor               | (60, 60)   | float32 |
B07                       | Tensor               | (60, 60)   | float32 |
B08                       | Tensor               | (120, 120) | float32 |
B09                       | Tensor               | (20, 20)   | float32 |
B11                       | Tensor               | (60, 60)   | float32 |
B12                       | Tensor               | (60, 60)   | float32 |
B8A                       | Tensor               | (60, 60)   | float32 |
filename                  | Text                 |            | string  |
labels                    | Sequence(ClassLabel) | (None,)    | int64   |
metadata                  | FeaturesDict         |            |         |
metadata/acquisition_date | Text                 |            | string  |
metadata/coordinates      | FeaturesDict         |            |         |
metadata/coordinates/lrx  | Tensor               |            | int64   |
metadata/coordinates/lry  | Tensor               |            | int64   |
metadata/coordinates/ulx  | Tensor               |            | int64   |
metadata/coordinates/uly  | Tensor               |            | int64   |
metadata/projection       | Text                 |            | string  |
metadata/tile_source      | Text                 |            | string  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/bigearthnet-all-1.0.0.html";
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