<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="hillstrom" />
  <meta itemprop="description" content="This dataset contains 64,000 customers who last purchased within twelve months. The customers were involved in an e-mail test.&#10;&#10;1. 1/3 were randomly chosen to receive an e-mail campaign featuring Mens merchandise.&#10;2. 1/3 were randomly chosen to receive an e-mail campaign featuring Womens merchandise.&#10;3. 1/3 were randomly chosen to not receive an e-mail campaign.&#10;&#10;During a period of two weeks following the e-mail campaign, results were tracked.&#10;The task is to tell the world if the Mens or Womens e-mail campaign was successful.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;hillstrom&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/hillstrom" />
  <meta itemprop="sameAs" content="https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html" />
  <meta itemprop="citation" content="@article{entryhillstrom,&#10;  title={Hillstrom’s MineThatData Email Analytics Challenge},&#10;  author={ENTRY, WINNING}&#10;}" />
</div>

# `hillstrom`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

This dataset contains 64,000 customers who last purchased within twelve months.
The customers were involved in an e-mail test.

1.  1/3 were randomly chosen to receive an e-mail campaign featuring Mens
    merchandise.
2.  1/3 were randomly chosen to receive an e-mail campaign featuring Womens
    merchandise.
3.  1/3 were randomly chosen to not receive an e-mail campaign.

During a period of two weeks following the e-mail campaign, results were
tracked. The task is to tell the world if the Mens or Womens e-mail campaign was
successful.

*   **Homepage**:
    [https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)

*   **Source code**:
    [`tfds.recommendation.hillstrom.Hillstrom`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/recommendation/hillstrom/hillstrom.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.78 MiB`

*   **Dataset size**: `15.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 64,000

*   **Feature structure**:

```python
FeaturesDict({
    'channel': Text(shape=(), dtype=tf.string),
    'conversion': tf.int64,
    'history': tf.float32,
    'history_segment': Text(shape=(), dtype=tf.string),
    'mens': tf.int64,
    'newbie': tf.int64,
    'recency': tf.int64,
    'segment': Text(shape=(), dtype=tf.string),
    'spend': tf.float32,
    'visit': tf.int64,
    'womens': tf.int64,
    'zip_code': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype      | Description
:-------------- | :----------- | :---- | :--------- | :----------
                | FeaturesDict |       |            |
channel         | Text         |       | tf.string  |
conversion      | Tensor       |       | tf.int64   |
history         | Tensor       |       | tf.float32 |
history_segment | Text         |       | tf.string  |
mens            | Tensor       |       | tf.int64   |
newbie          | Tensor       |       | tf.int64   |
recency         | Tensor       |       | tf.int64   |
segment         | Text         |       | tf.string  |
spend           | Tensor       |       | tf.float32 |
visit           | Tensor       |       | tf.int64   |
womens          | Tensor       |       | tf.int64   |
zip_code        | Text         |       | tf.string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `({'channel': 'channel', 'history': 'history', 'mens': 'mens', 'newbie':
    'newbie', 'recency': 'recency', 'segment': 'segment', 'womens': 'womens',
    'zip_code': 'zip_code'}, 'visit')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/hillstrom-1.0.0.html";
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
@article{entryhillstrom,
  title={Hillstrom’s MineThatData Email Analytics Challenge},
  author={ENTRY, WINNING}
}
```

