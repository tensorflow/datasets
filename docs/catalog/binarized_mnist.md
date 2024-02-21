<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="binarized_mnist" />
  <meta itemprop="description" content="A specific binarization of the MNIST images originally used in (Salakhutdinov &amp;&#10;Murray, 2008). This dataset is frequently used to evaluate generative models of&#10;images, so labels are not provided.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;binarized_mnist&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/binarized_mnist-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/binarized_mnist" />
  <meta itemprop="sameAs" content="http://www.dmi.usherb.ca/~larocheh/mlpython/_modules/datasets/binarized_mnist.html" />
  <meta itemprop="citation" content="@inproceedings{salakhutdinov2008quantitative,&#10;title={On the quantitative analysis of deep belief networks},&#10;author={Salakhutdinov, Ruslan and Murray, Iain},&#10;booktitle={Proceedings of the 25th international conference on Machine learning},&#10;pages={872--879},&#10;year={2008},&#10;organization={ACM}&#10;}" />
</div>

# `binarized_mnist`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=binarized_mnist">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

A specific binarization of the MNIST images originally used in (Salakhutdinov &
Murray, 2008). This dataset is frequently used to evaluate generative models of
images, so labels are not provided.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/binarized-mnist">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.dmi.usherb.ca/~larocheh/mlpython/_modules/datasets/binarized_mnist.html](http://www.dmi.usherb.ca/~larocheh/mlpython/_modules/datasets/binarized_mnist.html)

*   **Source code**:
    [`tfds.datasets.binarized_mnist.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/binarized_mnist/binarized_mnist_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial Release

*   **Download size**: `104.68 MiB`

*   **Dataset size**: `11.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 50,000
`'validation'` | 10,000

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=uint8),
})
```

*   **Feature documentation**:

Feature | Class        | Shape       | Dtype | Description
:------ | :----------- | :---------- | :---- | :----------
        | FeaturesDict |             |       |
image   | Image        | (28, 28, 1) | uint8 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/binarized_mnist-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/binarized_mnist-1.0.0.html";
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
@inproceedings{salakhutdinov2008quantitative,
title={On the quantitative analysis of deep belief networks},
author={Salakhutdinov, Ruslan and Murray, Iain},
booktitle={Proceedings of the 25th international conference on Machine learning},
pages={872--879},
year={2008},
organization={ACM}
}
```

