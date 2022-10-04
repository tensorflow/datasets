<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="yahoo_ltrc" />
  <meta itemprop="description" content="The Yahoo Learning to Rank Challenge dataset (also called &quot;C14&quot;) is a&#10;Learning-to-Rank dataset released by Yahoo. The dataset consists of&#10;query-document pairs represented as feature vectors and corresponding relevance&#10;judgment labels.&#10;&#10;The dataset contains two versions:&#10;&#10; * `set1`: Containing 709,877 query-document pairs.&#10; * `set2`: Containing 172,870 query-document pairs.&#10;&#10;You can specify whether to use the `set1` or `set2` version of the dataset as&#10;follows:&#10;&#10;```python&#10;ds = tfds.load(&quot;yahoo_ltrc/set1&quot;)&#10;ds = tfds.load(&quot;yahoo_ltrc/set2&quot;)&#10;```&#10;&#10;If only `yahoo_ltrc` is specified, the `yahoo_ltrc/set1` option is selected by&#10;default:&#10;&#10;```python&#10;# This is the same as `tfds.load(&quot;yahoo_ltrc/set1&quot;)`&#10;ds = tfds.load(&quot;yahoo_ltrc&quot;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;yahoo_ltrc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/yahoo_ltrc" />
  <meta itemprop="sameAs" content="https://research.yahoo.com/datasets" />
  <meta itemprop="citation" content="@inproceedings{chapelle2011yahoo,&#10;  title={Yahoo! learning to rank challenge overview},&#10;  author={Chapelle, Olivier and Chang, Yi},&#10;  booktitle={Proceedings of the learning to rank challenge},&#10;  pages={1--24},&#10;  year={2011},&#10;  organization={PMLR}&#10;}" />
</div>

# `yahoo_ltrc`


Warning: Manual download required. See instructions below.

*   **Description**:

The Yahoo Learning to Rank Challenge dataset (also called "C14") is a
Learning-to-Rank dataset released by Yahoo. The dataset consists of
query-document pairs represented as feature vectors and corresponding relevance
judgment labels.

The dataset contains two versions:

*   `set1`: Containing 709,877 query-document pairs.
*   `set2`: Containing 172,870 query-document pairs.

You can specify whether to use the `set1` or `set2` version of the dataset as
follows:

```python
ds = tfds.load("yahoo_ltrc/set1")
ds = tfds.load("yahoo_ltrc/set2")
```

If only `yahoo_ltrc` is specified, the `yahoo_ltrc/set1` option is selected by
default:

```python
# This is the same as `tfds.load("yahoo_ltrc/set1")`
ds = tfds.load("yahoo_ltrc")
```

*   **Homepage**:
    [https://research.yahoo.com/datasets](https://research.yahoo.com/datasets)

*   **Source code**:
    [`tfds.ranking.yahoo_ltrc.YahooLTRC`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/ranking/yahoo_ltrc/yahoo_ltrc.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Request access for the C14 Yahoo Learning To Rank Challenge dataset on
    https://research.yahoo.com/datasets. Extract the downloaded `dataset.tgz` file
    and place the `ltrc_yahoo.tar.bz2` file in `manual_dir/`.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{chapelle2011yahoo,
  title={Yahoo! learning to rank challenge overview},
  author={Chapelle, Olivier and Chang, Yi},
  booktitle={Proceedings of the learning to rank challenge},
  pages={1--24},
  year={2011},
  organization={PMLR}
}
```


## yahoo_ltrc/set1 (default config)

*   **Dataset size**: `792.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,983
`'train'` | 19,944
`'vali'`  | 2,994

*   **Feature structure**:

```python
FeaturesDict({
    'float_features': Tensor(shape=(None, 699), dtype=tf.float64),
    'label': Tensor(shape=(None,), dtype=tf.float64),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype      | Description
:------------- | :----------- | :---------- | :--------- | :----------
               | FeaturesDict |             |            |
float_features | Tensor       | (None, 699) | tf.float64 |
label          | Tensor       | (None,)     | tf.float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/yahoo_ltrc-set1-1.0.0.html";
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

## yahoo_ltrc/set2

*   **Dataset size**: `194.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 3,798
`'train'` | 1,266
`'vali'`  | 1,266

*   **Feature structure**:

```python
FeaturesDict({
    'float_features': Tensor(shape=(None, 700), dtype=tf.float64),
    'label': Tensor(shape=(None,), dtype=tf.float64),
})
```

*   **Feature documentation**:

Feature        | Class        | Shape       | Dtype      | Description
:------------- | :----------- | :---------- | :--------- | :----------
               | FeaturesDict |             |            |
float_features | Tensor       | (None, 700) | tf.float64 |
label          | Tensor       | (None,)     | tf.float64 |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/yahoo_ltrc-set2-1.0.0.html";
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