<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="deep1b" />
  <meta itemprop="description" content="Pre-trained embeddings for approximate nearest neighbor search using the&#10;cosine distance. This dataset consists of two splits:&#10;&#10;  1. &#x27;database&#x27;: consists of 9,990,000 data points, each has features:&#10;    &#x27;embedding&#x27; (96 floats), &#x27;index&#x27; (int64), &#x27;neighbors&#x27; (empty list).&#10;  2. &#x27;test&#x27;: consists of 10,000 data points, each has features: &#x27;embedding&#x27; (96&#10;    floats), &#x27;index&#x27; (int64), &#x27;neighbors&#x27; (list of &#x27;index&#x27; and &#x27;distance&#x27;&#10;    of the nearest neighbors in the database.)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;deep1b&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/deep1b" />
  <meta itemprop="sameAs" content="http://sites.skoltech.ru/compvision/noimi/" />
  <meta itemprop="citation" content="@inproceedings{babenko2016efficient,&#10;  title={Efficient indexing of billion-scale datasets of deep descriptors},&#10;  author={Babenko, Artem and Lempitsky, Victor},&#10;  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},&#10;  pages={2055--2063},&#10;  year={2016}&#10;}" />
</div>

# `deep1b`


*   **Description**:

Pre-trained embeddings for approximate nearest neighbor search using the cosine
distance. This dataset consists of two splits:

1.  'database': consists of 9,990,000 data points, each has features:
    'embedding' (96 floats), 'index' (int64), 'neighbors' (empty list).
2.  'test': consists of 10,000 data points, each has features: 'embedding' (96
    floats), 'index' (int64), 'neighbors' (list of 'index' and 'distance' of the
    nearest neighbors in the database.)

*   **Homepage**:
    [http://sites.skoltech.ru/compvision/noimi/](http://sites.skoltech.ru/compvision/noimi/)

*   **Source code**:
    [`tfds.nearest_neighbors.deep1b.Deep1b`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/nearest_neighbors/deep1b/deep1b.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.58 GiB`

*   **Dataset size**: `4.46 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split        | Examples
:----------- | --------:
`'database'` | 9,990,000
`'test'`     | 10,000

*   **Feature structure**:

```python
FeaturesDict({
    'embedding': Tensor(shape=(96,), dtype=float32),
    'index': Scalar(shape=(), dtype=int64, description=Index within the split.),
    'neighbors': Sequence({
        'distance': Scalar(shape=(), dtype=float32, description=Neighbor distance.),
        'index': Scalar(shape=(), dtype=int64, description=Neighbor index.),
    }),
})
```

*   **Feature documentation**:

| Feature            | Class        | Shape | Dtype   | Description            |
| :----------------- | :----------- | :---- | :------ | :--------------------- |
|                    | FeaturesDict |       |         |                        |
| embedding          | Tensor       | (96,) | float32 |                        |
| index              | Scalar       |       | int64   | Index within the       |
:                    :              :       :         : split.                 :
| neighbors          | Sequence     |       |         | The computed           |
:                    :              :       :         : neighbors, which is    :
:                    :              :       :         : only available for the :
:                    :              :       :         : test split.            :
| neighbors/distance | Scalar       |       | float32 | Neighbor distance.     |
| neighbors/index    | Scalar       |       | int64   | Neighbor index.        |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/deep1b-1.0.0.html";
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
@inproceedings{babenko2016efficient,
  title={Efficient indexing of billion-scale datasets of deep descriptors},
  author={Babenko, Artem and Lempitsky, Victor},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={2055--2063},
  year={2016}
}
```

