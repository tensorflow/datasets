<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wake_vision" />
  <meta itemprop="description" content="Wake Vision is a large, high-quality dataset featuring over 6 million images,&#10;significantly exceeding the scale and diversity of current tinyML datasets&#10;(100x). This dataset includes images with annotations of whether each image&#10;contains a person. Additionally, it incorporates a comprehensive fine-grained&#10;benchmark to assess fairness and robustness, covering perceived gender,&#10;perceived age, subject distance, lighting conditions, and depictions. The Wake&#10;Vision labels are derived from Open Image&#x27;s annotations which are licensed by&#10;Google LLC under CC BY 4.0 license. The images are listed as having a CC BY 2.0&#10;license. Note from Open Images: &quot;while we tried to identify images that are&#10;licensed under a Creative Commons Attribution license, we make no&#10;representations or warranties regarding the license status of each image and you&#10;should verify the license for each image yourself.&quot;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wake_vision&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/wake_vision-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wake_vision" />
  <meta itemprop="sameAs" content="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F1HOPXC" />
  <meta itemprop="citation" content="@article{banbury2024wake,&#10;  title={Wake Vision: A Large-scale, Diverse Dataset and Benchmark Suite for TinyML Person Detection},&#10;  author={Banbury, Colby and Njor, Emil and Stewart, Matthew and Warden, Pete and Kudlur, Manjunath and Jeffries, Nat and Fafoutis, Xenofon and Reddi, Vijay Janapa},&#10;  journal={arXiv preprint arXiv:2405.00892},&#10;  year={2024}&#10;}" />
</div>

# `wake_vision`


*   **Description**:

Wake Vision is a large, high-quality dataset featuring over 6 million images,
significantly exceeding the scale and diversity of current tinyML datasets
(100x). This dataset includes images with annotations of whether each image
contains a person. Additionally, it incorporates a comprehensive fine-grained
benchmark to assess fairness and robustness, covering perceived gender,
perceived age, subject distance, lighting conditions, and depictions. The Wake
Vision labels are derived from Open Image's annotations which are licensed by
Google LLC under CC BY 4.0 license. The images are listed as having a CC BY 2.0
license. Note from Open Images: "while we tried to identify images that are
licensed under a Creative Commons Attribution license, we make no
representations or warranties regarding the license status of each image and you
should verify the license for each image yourself."

*   **Homepage**:
    [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F1HOPXC](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F1HOPXC)

*   **Source code**:
    [`tfds.datasets.wake_vision.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/wake_vision/wake_vision_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial TensorFlow Datasets release. Note that
        this is based on the 2.0 version of Wake Vision on Harvard Dataverse.

*   **Download size**: `Unknown size`

*   **Dataset size**: `239.25 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split             | Examples
:---------------- | --------:
`'test'`          | 55,763
`'train_large'`   | 5,760,428
`'train_quality'` | 1,248,230
`'validation'`    | 18,582

*   **Feature structure**:

```python
FeaturesDict({
    'age_unknown': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'body_part': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'bright': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'dark': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'depiction': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'far': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'filename': Text(shape=(), dtype=string),
    'gender_unknown': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'medium_distance': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'middle_age': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'near': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'non-person_depiction': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'non-person_non-depiction': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'normal_lighting': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'older': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'person': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'person_depiction': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'predominantly_female': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'predominantly_male': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'young': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature                  | Class        | Shape           | Dtype  | Description
:----------------------- | :----------- | :-------------- | :----- | :----------
                         | FeaturesDict |                 |        |
age_unknown              | ClassLabel   |                 | int64  |
body_part                | ClassLabel   |                 | int64  |
bright                   | ClassLabel   |                 | int64  |
dark                     | ClassLabel   |                 | int64  |
depiction                | ClassLabel   |                 | int64  |
far                      | ClassLabel   |                 | int64  |
filename                 | Text         |                 | string |
gender_unknown           | ClassLabel   |                 | int64  |
image                    | Image        | (None, None, 3) | uint8  |
medium_distance          | ClassLabel   |                 | int64  |
middle_age               | ClassLabel   |                 | int64  |
near                     | ClassLabel   |                 | int64  |
non-person_depiction     | ClassLabel   |                 | int64  |
non-person_non-depiction | ClassLabel   |                 | int64  |
normal_lighting          | ClassLabel   |                 | int64  |
older                    | ClassLabel   |                 | int64  |
person                   | ClassLabel   |                 | int64  |
person_depiction         | ClassLabel   |                 | int64  |
predominantly_female     | ClassLabel   |                 | int64  |
predominantly_male       | ClassLabel   |                 | int64  |
young                    | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'person')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/wake_vision-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wake_vision-1.0.0.html";
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
@article{banbury2024wake,
  title={Wake Vision: A Large-scale, Diverse Dataset and Benchmark Suite for TinyML Person Detection},
  author={Banbury, Colby and Njor, Emil and Stewart, Matthew and Warden, Pete and Kudlur, Manjunath and Jeffries, Nat and Fafoutis, Xenofon and Reddi, Vijay Janapa},
  journal={arXiv preprint arXiv:2405.00892},
  year={2024}
}
```

