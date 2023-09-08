<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cifar10_h" />
  <meta itemprop="description" content="A re-labeled version of CIFAR-10&#x27;s test set with soft-labels&#10;coming from real human annotators. For every pair (image, label) in the&#10;original CIFAR-10 test set, it provides several additional labels given by real&#10;human annotators as well as the average soft-label. The training set is&#10;identical to the one of the original dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cifar10_h&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_h-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cifar10_h" />
  <meta itemprop="sameAs" content="https://github.com/jcpeterson/cifar-10h" />
  <meta itemprop="citation" content="@inproceedings{wei2022learning,&#10;  title={Human uncertainty makes classification more robust},&#10;  author={Joshua C. Peterson and Ruairidh M. Battleday and Thomas L. Griffiths&#10;  and Olga Russakovsky},&#10;  booktitle={IEEE International Conference on Computer Vision and Pattern&#10;  Recognition (CVPR)},&#10;  year={2019}&#10;}" />
</div>

# `cifar10_h`


*   **Description**:

A re-labeled version of CIFAR-10's test set with soft-labels coming from real
human annotators. For every pair (image, label) in the original CIFAR-10 test
set, it provides several additional labels given by real human annotators as
well as the average soft-label. The training set is identical to the one of the
original dataset.

*   **Homepage**:
    [https://github.com/jcpeterson/cifar-10h](https://github.com/jcpeterson/cifar-10h)

*   **Source code**:
    [`tfds.image_classification.cifar10_h.Cifar10H`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cifar10_h/cifar10_h.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `172.92 MiB`

*   **Dataset size**: `144.85 MiB`

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
    'annotator_ids': Sequence(Scalar(shape=(), dtype=int32)),
    'human_labels': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=10)),
    'id': Text(shape=(), dtype=string),
    'image': Image(shape=(32, 32, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=10),
    'reaction_times': Sequence(Scalar(shape=(), dtype=float32)),
    'soft_label': Tensor(shape=(10,), dtype=float32),
    'trial_indices': Sequence(Scalar(shape=(), dtype=int32)),
})
```

*   **Feature documentation**:

Feature        | Class                | Shape       | Dtype   | Description
:------------- | :------------------- | :---------- | :------ | :----------
               | FeaturesDict         |             |         |
annotator_ids  | Sequence(Scalar)     | (None,)     | int32   |
human_labels   | Sequence(ClassLabel) | (None,)     | int64   |
id             | Text                 |             | string  |
image          | Image                | (32, 32, 3) | uint8   |
label          | ClassLabel           |             | int64   |
reaction_times | Sequence(Scalar)     | (None,)     | float32 |
soft_label     | Tensor               | (10,)       | float32 |
trial_indices  | Sequence(Scalar)     | (None,)     | int32   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_h-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cifar10_h-1.0.0.html";
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
  title={Human uncertainty makes classification more robust},
  author={Joshua C. Peterson and Ruairidh M. Battleday and Thomas L. Griffiths
  and Olga Russakovsky},
  booktitle={IEEE International Conference on Computer Vision and Pattern
  Recognition (CVPR)},
  year={2019}
}
```

