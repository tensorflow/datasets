<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kddcup99" />
  <meta itemprop="description" content="This is the data set used for The Third International Knowledge Discovery and&#10;Data Mining Tools Competition, which was held in conjunction with KDD-99 The&#10;Fifth International Conference on Knowledge Discovery and Data Mining. The&#10;competition task was to build a network intrusion detector, a predictive model&#10;capable of distinguishing between &#x27;bad&#x27; connections, called intrusions or&#10;attacks, and &#x27;good&#x27; normal connections. This database contains a standard set&#10;of data to be audited, which includes a wide variety of intrusions simulated in&#10;a military network environment.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;kddcup99&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kddcup99" />
  <meta itemprop="sameAs" content="https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html" />
  <meta itemprop="citation" content="@misc{Dua:2019 ,&#10;  author = &quot;Dua, Dheeru and Graff, Casey&quot;,&#10;  year = 2017,&#10;  title = &quot;{UCI} Machine Learning Repository&quot;,&#10;  url = &quot;http://archive.ics.uci.edu/ml&quot;,&#10;  institution = &quot;University of California, Irvine, School of Information and&#10;Computer Sciences&quot;&#10;}" />
</div>

# `kddcup99`


*   **Description**:

This is the data set used for The Third International Knowledge Discovery and
Data Mining Tools Competition, which was held in conjunction with KDD-99 The
Fifth International Conference on Knowledge Discovery and Data Mining. The
competition task was to build a network intrusion detector, a predictive model
capable of distinguishing between 'bad' connections, called intrusions or
attacks, and 'good' normal connections. This database contains a standard set of
data to be audited, which includes a wide variety of intrusions simulated in a
military network environment.

*   **Homepage**:
    [https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html](https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

*   **Source code**:
    [`tfds.structured.kddcup99.Kddcup99`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/kddcup99/kddcup99.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `18.62 MiB`

*   **Dataset size**: `5.25 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'test'`  | 311,029
`'train'` | 4,898,431

*   **Features**:

```python
FeaturesDict({
    'count': tf.int32,
    'diff_srv_rate': tf.float32,
    'dst_bytes': tf.int32,
    'dst_host_count': tf.int32,
    'dst_host_diff_srv_rate': tf.float32,
    'dst_host_rerror_rate': tf.float32,
    'dst_host_same_src_port_rate': tf.float32,
    'dst_host_same_srv_rate': tf.float32,
    'dst_host_serror_rate': tf.float32,
    'dst_host_srv_count': tf.int32,
    'dst_host_srv_diff_host_rate': tf.float32,
    'dst_host_srv_rerror_rate': tf.float32,
    'dst_host_srv_serror_rate': tf.float32,
    'duration': tf.int32,
    'flag': ClassLabel(shape=(), dtype=tf.int64, num_classes=11),
    'hot': tf.int32,
    'is_guest_login': tf.bool,
    'is_hot_login': tf.bool,
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=40),
    'land': tf.bool,
    'logged_in': tf.bool,
    'num_access_files': tf.int32,
    'num_compromised': tf.int32,
    'num_failed_logins': tf.int32,
    'num_file_creations': tf.int32,
    'num_outbound_cmds': tf.int32,
    'num_root': tf.int32,
    'num_shells': tf.int32,
    'protocol_type': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'rerror_rate': tf.float32,
    'root_shell': tf.bool,
    'same_srv_rate': tf.float32,
    'serror_rate': tf.float32,
    'service': ClassLabel(shape=(), dtype=tf.int64, num_classes=71),
    'src_bytes': tf.int32,
    'srv_count': tf.int32,
    'srv_diff_host_rate': tf.float32,
    'srv_rerror_rate': tf.float32,
    'srv_serror_rate': tf.float32,
    'su_attempted': tf.int32,
    'urgent': tf.int32,
    'wrong_fragment': tf.int32,
})
```

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
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/kddcup99-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@misc{Dua:2019 ,
  author = "Dua, Dheeru and Graff, Casey",
  year = 2017,
  title = "{UCI} Machine Learning Repository",
  url = "http://archive.ics.uci.edu/ml",
  institution = "University of California, Irvine, School of Information and
Computer Sciences"
}
```
