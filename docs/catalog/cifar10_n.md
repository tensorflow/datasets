<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cifar10_n" />
  <meta itemprop="description" content="A re-labeled version of CIFAR-10 with real human annotation errors. For every &#10;pair (image, label) in the original CIFAR-10 train set, it provides several &#10;additional labels given by real human annotators.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cifar10_n&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_n-1.0.4.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cifar10_n" />
  <meta itemprop="sameAs" content="https://ucsc-real.soe.ucsc.edu:1995/Home.html/" />
  <meta itemprop="citation" content="@inproceedings{wei2022learning,&#10;  title={Learning with Noisy Labels Revisited: A Study Using Real-World Human &#10;  Annotations},&#10;  author={Jiaheng Wei and Zhaowei Zhu and Hao Cheng and Tongliang Liu and Gang &#10;  Niu and Yang Liu},&#10;  booktitle={International Conference on Learning Representations},&#10;  year={2022},&#10;  url={https://openreview.net/forum?id=TBWA6PLJZQm}&#10;}" />
</div>

# `cifar10_n`


Warning: Manual download required. See instructions below.

*   **Description**:

A re-labeled version of CIFAR-10 with real human annotation errors. For every
pair (image, label) in the original CIFAR-10 train set, it provides several
additional labels given by real human annotators.

*   **Homepage**:
    [https://ucsc-real.soe.ucsc.edu:1995/Home.html/](https://ucsc-real.soe.ucsc.edu:1995/Home.html/)

*   **Source code**:
    [`tfds.image_classification.cifar10_n.Cifar10N`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cifar10_n/cifar10_n.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   `1.0.1`: Fixed typo in `worse_label` key.
    *   `1.0.2`: Fixed correspondence between annotations and images.
    *   `1.0.3`: Fixed files in `MANUAL_DIR`.
    *   **`1.0.4`** (default): Fixed loading of side information.

*   **Download size**: `162.17 MiB`

*   **Dataset size**: `147.91 MiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Download 'side_info_cifar10N.csv', 'CIFAR-10_human_ordered.npy' and
    'image_order_c10.npy' from https://github.com/UCSC-REAL/cifar-10-100n.

Then convert 'CIFAR-10_human_ordered.npy' into a CSV file
'CIFAR-10_human_annotations.csv'. This can be done with the following code:

```
import numpy as np
import pandas as pd
import tensorflow as tf

human_labels_np_path = '<local_path>/CIFAR-10_human_ordered.npy'
human_labels_csv_path = '<local_path>/CIFAR-10_human_annotations.csv'

with tf.io.gfile.GFile(human_labels_np_path, "rb") as f:
  human_annotations = np.load(f, allow_pickle=True)

df = pd.DataFrame(human_annotations[()])

with tf.io.gfile.GFile(human_labels_csv_path, "w") as f:
  df.to_csv(f, index=False)
```

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 10,000
`'train'` | 50,000

*   **Feature structure**:

```python
FeaturesDict({
    'aggre_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'random_label1': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'random_label2': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'random_label3': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'worker1_id': tf.int64,
    'worker1_time': tf.float32,
    'worker2_id': tf.int64,
    'worker2_time': tf.float32,
    'worker3_id': tf.int64,
    'worker3_time': tf.float32,
    'worse_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape       | Dtype      | Description
:------------ | :----------- | :---------- | :--------- | :----------
              | FeaturesDict |             |            |
aggre_label   | ClassLabel   |             | tf.int64   |
id            | Text         |             | tf.string  |
image         | Image        | (32, 32, 3) | tf.uint8   |
label         | ClassLabel   |             | tf.int64   |
random_label1 | ClassLabel   |             | tf.int64   |
random_label2 | ClassLabel   |             | tf.int64   |
random_label3 | ClassLabel   |             | tf.int64   |
worker1_id    | Tensor       |             | tf.int64   |
worker1_time  | Tensor       |             | tf.float32 |
worker2_id    | Tensor       |             | tf.int64   |
worker2_time  | Tensor       |             | tf.float32 |
worker3_id    | Tensor       |             | tf.int64   |
worker3_time  | Tensor       |             | tf.float32 |
worse_label   | ClassLabel   |             | tf.int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_n-1.0.4.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cifar10_n-1.0.4.html";
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
@inproceedings{wei2022learning,
  title={Learning with Noisy Labels Revisited: A Study Using Real-World Human
  Annotations},
  author={Jiaheng Wei and Zhaowei Zhu and Hao Cheng and Tongliang Liu and Gang
  Niu and Yang Liu},
  booktitle={International Conference on Learning Representations},
  year={2022},
  url={https://openreview.net/forum?id=TBWA6PLJZQm}
}
```

