<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kddcup99" />
  <meta itemprop="description" content="This is the data set used for The Third International Knowledge Discovery and&#10;Data Mining Tools Competition, which was held in conjunction with KDD-99 The&#10;Fifth International Conference on Knowledge Discovery and Data Mining. The&#10;competition task was to build a network intrusion detector, a predictive model&#10;capable of distinguishing between &#x27;bad&#x27; connections, called intrusions or&#10;attacks, and &#x27;good&#x27; normal connections. This database contains a standard set of&#10;data to be audited, which includes a wide variety of intrusions simulated in a&#10;military network environment.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;kddcup99&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
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

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/kdd-cup-1999-data-data-set">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html](https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

*   **Source code**:
    [`tfds.datasets.kddcup99.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/kddcup99/kddcup99_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Fixes parsing of boolean fields `land`,
        `logged_in`, `root_shell`, `is_hot_login` and `is_guest_login`.

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

*   **Feature structure**:

```python
FeaturesDict({
    'count': int32,
    'diff_srv_rate': float32,
    'dst_bytes': int32,
    'dst_host_count': int32,
    'dst_host_diff_srv_rate': float32,
    'dst_host_rerror_rate': float32,
    'dst_host_same_src_port_rate': float32,
    'dst_host_same_srv_rate': float32,
    'dst_host_serror_rate': float32,
    'dst_host_srv_count': int32,
    'dst_host_srv_diff_host_rate': float32,
    'dst_host_srv_rerror_rate': float32,
    'dst_host_srv_serror_rate': float32,
    'duration': int32,
    'flag': ClassLabel(shape=(), dtype=int64, num_classes=11),
    'hot': int32,
    'is_guest_login': bool,
    'is_hot_login': bool,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=40),
    'land': bool,
    'logged_in': bool,
    'num_access_files': int32,
    'num_compromised': int32,
    'num_failed_logins': int32,
    'num_file_creations': int32,
    'num_outbound_cmds': int32,
    'num_root': int32,
    'num_shells': int32,
    'protocol_type': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rerror_rate': float32,
    'root_shell': bool,
    'same_srv_rate': float32,
    'serror_rate': float32,
    'service': ClassLabel(shape=(), dtype=int64, num_classes=71),
    'src_bytes': int32,
    'srv_count': int32,
    'srv_diff_host_rate': float32,
    'srv_rerror_rate': float32,
    'srv_serror_rate': float32,
    'su_attempted': int32,
    'urgent': int32,
    'wrong_fragment': int32,
})
```

*   **Feature documentation**:

Feature                     | Class        | Shape | Dtype   | Description
:-------------------------- | :----------- | :---- | :------ | :----------
                            | FeaturesDict |       |         |
count                       | Tensor       |       | int32   |
diff_srv_rate               | Tensor       |       | float32 |
dst_bytes                   | Tensor       |       | int32   |
dst_host_count              | Tensor       |       | int32   |
dst_host_diff_srv_rate      | Tensor       |       | float32 |
dst_host_rerror_rate        | Tensor       |       | float32 |
dst_host_same_src_port_rate | Tensor       |       | float32 |
dst_host_same_srv_rate      | Tensor       |       | float32 |
dst_host_serror_rate        | Tensor       |       | float32 |
dst_host_srv_count          | Tensor       |       | int32   |
dst_host_srv_diff_host_rate | Tensor       |       | float32 |
dst_host_srv_rerror_rate    | Tensor       |       | float32 |
dst_host_srv_serror_rate    | Tensor       |       | float32 |
duration                    | Tensor       |       | int32   |
flag                        | ClassLabel   |       | int64   |
hot                         | Tensor       |       | int32   |
is_guest_login              | Tensor       |       | bool    |
is_hot_login                | Tensor       |       | bool    |
label                       | ClassLabel   |       | int64   |
land                        | Tensor       |       | bool    |
logged_in                   | Tensor       |       | bool    |
num_access_files            | Tensor       |       | int32   |
num_compromised             | Tensor       |       | int32   |
num_failed_logins           | Tensor       |       | int32   |
num_file_creations          | Tensor       |       | int32   |
num_outbound_cmds           | Tensor       |       | int32   |
num_root                    | Tensor       |       | int32   |
num_shells                  | Tensor       |       | int32   |
protocol_type               | ClassLabel   |       | int64   |
rerror_rate                 | Tensor       |       | float32 |
root_shell                  | Tensor       |       | bool    |
same_srv_rate               | Tensor       |       | float32 |
serror_rate                 | Tensor       |       | float32 |
service                     | ClassLabel   |       | int64   |
src_bytes                   | Tensor       |       | int32   |
srv_count                   | Tensor       |       | int32   |
srv_diff_host_rate          | Tensor       |       | float32 |
srv_rerror_rate             | Tensor       |       | float32 |
srv_serror_rate             | Tensor       |       | float32 |
su_attempted                | Tensor       |       | int32   |
urgent                      | Tensor       |       | int32   |
wrong_fragment              | Tensor       |       | int32   |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/kddcup99-1.0.1.html";
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
@misc{Dua:2019 ,
  author = "Dua, Dheeru and Graff, Casey",
  year = 2017,
  title = "{UCI} Machine Learning Repository",
  url = "http://archive.ics.uci.edu/ml",
  institution = "University of California, Irvine, School of Information and
Computer Sciences"
}
```

