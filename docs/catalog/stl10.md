<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stl10" />
  <meta itemprop="description" content="The STL-10 dataset is an image recognition dataset for developing unsupervised&#10;feature learning, deep learning, self-taught learning algorithms. It is inspired&#10;by the CIFAR-10 dataset but with some modifications. In particular, each class&#10;has fewer labeled training examples than in CIFAR-10, but a very large set of&#10;unlabeled examples is provided to learn image models prior to supervised&#10;training. The primary challenge is to make use of the unlabeled data (which&#10;comes from a similar but different distribution from the labeled data) to build&#10;a useful prior. All images were acquired from labeled examples on ImageNet.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stl10&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/stl10-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stl10" />
  <meta itemprop="sameAs" content="http://ai.stanford.edu/~acoates/stl10/" />
  <meta itemprop="citation" content="@inproceedings{coates2011stl10,&#10;  title={{An Analysis of Single Layer Networks in Unsupervised Feature Learning}},&#10;  author={Coates, Adam and Ng, Andrew and Lee, Honglak},&#10;  booktitle={AISTATS},&#10;  year={2011},&#10;  note = {\url{https://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf}},&#10;}" />
</div>

# `stl10`


*   **Description**:

The STL-10 dataset is an image recognition dataset for developing unsupervised
feature learning, deep learning, self-taught learning algorithms. It is inspired
by the CIFAR-10 dataset but with some modifications. In particular, each class
has fewer labeled training examples than in CIFAR-10, but a very large set of
unlabeled examples is provided to learn image models prior to supervised
training. The primary challenge is to make use of the unlabeled data (which
comes from a similar but different distribution from the labeled data) to build
a useful prior. All images were acquired from labeled examples on ImageNet.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/stl-10">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://ai.stanford.edu/~acoates/stl10/](http://ai.stanford.edu/~acoates/stl10/)

*   **Source code**:
    [`tfds.datasets.stl10.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/stl10/stl10_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `2.46 GiB`

*   **Dataset size**: `1.86 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,000
`'train'`      | 5,000
`'unlabelled'` | 100,000

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(96, 96, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=10),
})
```

*   **Feature documentation**:

Feature | Class        | Shape       | Dtype | Description
:------ | :----------- | :---------- | :---- | :----------
        | FeaturesDict |             |       |
image   | Image        | (96, 96, 3) | uint8 |
label   | ClassLabel   |             | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/stl10-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/stl10-1.0.0.html";
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
@inproceedings{coates2011stl10,
  title={{An Analysis of Single Layer Networks in Unsupervised Feature Learning}},
  author={Coates, Adam and Ng, Andrew and Lee, Honglak},
  booktitle={AISTATS},
  year={2011},
  note = {\url{https://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf}},
}
```

