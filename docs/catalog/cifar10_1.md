<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cifar10_1" />
  <meta itemprop="description" content="The CIFAR-10.1 dataset is a new test set for CIFAR-10. CIFAR-10.1 contains roughly 2,000 new test images &#10;that were sampled after multiple years of research on the original CIFAR-10 dataset. The data collection &#10;for CIFAR-10.1 was designed to minimize distribution shift relative to the original dataset. We describe &#10;the creation of CIFAR-10.1 in the paper &quot;Do CIFAR-10 Classifiers Generalize to CIFAR-10?&quot;. &#10;The images in CIFAR-10.1 are a subset of the TinyImages dataset. &#10;There are currently two versions of the CIFAR-10.1 dataset: v4 and v6.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cifar10_1&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_1-v4-1.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cifar10_1" />
  <meta itemprop="sameAs" content="https://github.com/modestyachts/CIFAR-10.1" />
  <meta itemprop="citation" content="@article{recht2018cifar10.1,&#10;  author = {Benjamin Recht and Rebecca Roelofs and Ludwig Schmidt and Vaishaal Shankar},&#10;  title = {Do CIFAR-10 Classifiers Generalize to CIFAR-10?},&#10;  year = {2018},&#10;  note = {\url{https://arxiv.org/abs/1806.00451}},&#10;}&#10;&#10;@article{torralba2008tinyimages, &#10;  author = {Antonio Torralba and Rob Fergus and William T. Freeman}, &#10;  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, &#10;  title = {80 Million Tiny Images: A Large Data Set for Nonparametric Object and Scene Recognition}, &#10;  year = {2008}, &#10;  volume = {30}, &#10;  number = {11}, &#10;  pages = {1958-1970}&#10;}" />
</div>

# `cifar10_1`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=cifar10_1">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The CIFAR-10.1 dataset is a new test set for CIFAR-10. CIFAR-10.1 contains
roughly 2,000 new test images that were sampled after multiple years of research
on the original CIFAR-10 dataset. The data collection for CIFAR-10.1 was
designed to minimize distribution shift relative to the original dataset. We
describe the creation of CIFAR-10.1 in the paper "Do CIFAR-10 Classifiers
Generalize to CIFAR-10?". The images in CIFAR-10.1 are a subset of the
TinyImages dataset. There are currently two versions of the CIFAR-10.1 dataset:
v4 and v6.

*   **Homepage**:
    [https://github.com/modestyachts/CIFAR-10.1](https://github.com/modestyachts/CIFAR-10.1)

*   **Source code**:
    [`tfds.image_classification.Cifar10_1`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cifar10_1.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@article{recht2018cifar10.1,
  author = {Benjamin Recht and Rebecca Roelofs and Ludwig Schmidt and Vaishaal Shankar},
  title = {Do CIFAR-10 Classifiers Generalize to CIFAR-10?},
  year = {2018},
  note = {\url{https://arxiv.org/abs/1806.00451}},
}

@article{torralba2008tinyimages,
  author = {Antonio Torralba and Rob Fergus and William T. Freeman},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title = {80 Million Tiny Images: A Large Data Set for Nonparametric Object and Scene Recognition},
  year = {2008},
  volume = {30},
  number = {11},
  pages = {1958-1970}
}
```

## cifar10_1/v4 (default config)

*   **Config description**: It is the first version of our dataset on which we
    tested any classifier. As mentioned above, this makes the v4 dataset
    independent of the classifiers we evaluate. The numbers reported in the main
    sections of our paper use this version of the dataset. It was built from the
    top 25 TinyImages keywords for each class, which led to a slight class
    imbalance. The largest difference is that ships make up only 8% of the test
    set instead of 10%. v4 contains 2,021 images.

*   **Download size**: `5.93 MiB`

*   **Dataset size**: `4.46 MiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,021

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_1-v4-1.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cifar10_1-v4-1.1.0.html";
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

## cifar10_1/v6

*   **Config description**: It is derived from a slightly improved keyword
    allocation that is exactly class balanced. This version of the dataset
    corresponds to the results in Appendix D of our paper. v6 contains 2,000
    images.

*   **Download size**: `5.87 MiB`

*   **Dataset size**: `4.40 MiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/cifar10_1-v6-1.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cifar10_1-v6-1.1.0.html";
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