<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="so2sat" />
  <meta itemprop="description" content="So2Sat LCZ42 is a dataset consisting of co-registered synthetic aperture radar&#10;and multispectral optical image patches acquired by the Sentinel-1 and&#10;Sentinel-2 remote sensing satellites, and the corresponding local climate zones&#10;(LCZ) label. The dataset is distributed over 42 cities across different&#10;continents and cultural regions of the world.&#10;&#10;The full dataset (`all`) consists of 8 Sentinel-1 and 10 Sentinel-2 channels.&#10;Alternatively, one can select the `rgb` subset, which contains only the optical&#10;frequency bands of Sentinel-2, rescaled and encoded as JPEG.&#10;&#10;Dataset URL: http://doi.org/10.14459/2018MP1454690 \&#10;License: http://creativecommons.org/licenses/by/4.0&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;so2sat&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/so2sat" />
  <meta itemprop="sameAs" content="http://doi.org/10.14459/2018MP1454690" />
  <meta itemprop="citation" content="@misc{mediatum1483140,&#10;    author = {Zhu, Xiaoxiang  and  Hu, Jingliang  and  Qiu, Chunping  and  Shi, Yilei  and  Bagheri, Hossein  and  Kang, Jian  and  Li, Hao  and  Mou, Lichao  and  Zhang, Guicheng  and  Häberle, Matthias  and  Han, Shiyao  and  Hua, Yuansheng  and  Huang, Rong  and  Hughes, Lloyd  and  Sun, Yao  and  Schmitt, Michael and  Wang, Yuanyuan },&#10;  title = {NEW: So2Sat LCZ42},&#10;   publisher = {Technical University of Munich},&#10;  url = {https://mediatum.ub.tum.de/1483140},&#10;    type = {Dataset},&#10;  year = {2019},&#10; doi = {10.14459/2018mp1483140},&#10;    keywords = {local climate zones ; big data ; classification ; remote sensing ; deep learning ; data fusion ; synthetic aperture radar imagery ; optical imagery},&#10;  abstract = {So2Sat LCZ42 is a dataset consisting of corresponding synthetic aperture radar and multispectral optical image data acquired by the Sentinel-1 and Sentinel-2 remote sensing satellites, and a corresponding local climate zones (LCZ) label. The dataset is distributed over 42 cities across different continents and cultural regions of the world, and comes with a split into fully independent, non-overlapping training, validation, and test sets.},&#10;   language = {en},&#10;&#10;}" />
</div>

# `so2sat`


*   **Description**:

So2Sat LCZ42 is a dataset consisting of co-registered synthetic aperture radar
and multispectral optical image patches acquired by the Sentinel-1 and
Sentinel-2 remote sensing satellites, and the corresponding local climate zones
(LCZ) label. The dataset is distributed over 42 cities across different
continents and cultural regions of the world.

The full dataset (`all`) consists of 8 Sentinel-1 and 10 Sentinel-2 channels.
Alternatively, one can select the `rgb` subset, which contains only the optical
frequency bands of Sentinel-2, rescaled and encoded as JPEG.

Dataset URL: http://doi.org/10.14459/2018MP1454690 \
License: http://creativecommons.org/licenses/by/4.0

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/so2sat-lcz42">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://doi.org/10.14459/2018MP1454690](http://doi.org/10.14459/2018MP1454690)

*   **Source code**:
    [`tfds.datasets.so2sat.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/so2sat/so2sat_dataset_builder.py)

*   **Versions**:

    *   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   **`2.1.0`** (default): Using updated optical channels calibration
        factor.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@misc{mediatum1483140,
    author = {Zhu, Xiaoxiang  and  Hu, Jingliang  and  Qiu, Chunping  and  Shi, Yilei  and  Bagheri, Hossein  and  Kang, Jian  and  Li, Hao  and  Mou, Lichao  and  Zhang, Guicheng  and  Häberle, Matthias  and  Han, Shiyao  and  Hua, Yuansheng  and  Huang, Rong  and  Hughes, Lloyd  and  Sun, Yao  and  Schmitt, Michael and  Wang, Yuanyuan },
    title = {NEW: So2Sat LCZ42},
    publisher = {Technical University of Munich},
    url = {https://mediatum.ub.tum.de/1483140},
    type = {Dataset},
    year = {2019},
    doi = {10.14459/2018mp1483140},
    keywords = {local climate zones ; big data ; classification ; remote sensing ; deep learning ; data fusion ; synthetic aperture radar imagery ; optical imagery},
    abstract = {So2Sat LCZ42 is a dataset consisting of corresponding synthetic aperture radar and multispectral optical image data acquired by the Sentinel-1 and Sentinel-2 remote sensing satellites, and a corresponding local climate zones (LCZ) label. The dataset is distributed over 42 cities across different continents and cultural regions of the world, and comes with a split into fully independent, non-overlapping training, validation, and test sets.},
    language = {en},

}
```


## so2sat/rgb (default config)

*   **Config description**: Sentinel-2 RGB channels

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=17),
    'sample_id': int64,
})
```

*   **Feature documentation**:

Feature   | Class        | Shape       | Dtype | Description
:-------- | :----------- | :---------- | :---- | :----------
          | FeaturesDict |             |       |
image     | Image        | (32, 32, 3) | uint8 |
label     | ClassLabel   |             | int64 |
sample_id | Tensor       |             | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

## so2sat/all

*   **Config description**: 8 Sentinel-1 and 10 Sentinel-2 channels

*   **Feature structure**:

```python
FeaturesDict({
    'label': ClassLabel(shape=(), dtype=int64, num_classes=17),
    'sample_id': int64,
    'sentinel1': Tensor(shape=(32, 32, 8), dtype=float32),
    'sentinel2': Tensor(shape=(32, 32, 10), dtype=float32),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape        | Dtype   | Description
:-------- | :----------- | :----------- | :------ | :----------
          | FeaturesDict |              |         |
label     | ClassLabel   |              | int64   |
sample_id | Tensor       |              | int64   |
sentinel1 | Tensor       | (32, 32, 8)  | float32 |
sentinel2 | Tensor       | (32, 32, 10) | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
