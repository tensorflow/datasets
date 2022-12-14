<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="oxford_flowers102" />
  <meta itemprop="description" content="The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly&#10;occurring in the United Kingdom. Each class consists of between 40 and 258&#10;images. The images have large scale, pose and light variations. In addition,&#10;there are categories that have large variations within the category and several&#10;very similar categories.&#10;&#10;The dataset is divided into a training set, a validation set and a test set. The&#10;training set and validation set each consist of 10 images per class (totalling&#10;1020 images each). The test set consists of the remaining 6149 images (minimum&#10;20 per class).&#10;&#10;Note: The dataset by default comes with a test size larger than the train size.&#10;For more info see this&#10;[issue](https://github.com/tensorflow/datasets/issues/3022).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;oxford_flowers102&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/oxford_flowers102-2.1.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/oxford_flowers102" />
  <meta itemprop="sameAs" content="https://www.robots.ox.ac.uk/~vgg/data/flowers/102/" />
  <meta itemprop="citation" content="@InProceedings{Nilsback08,&#10;   author = &quot;Nilsback, M-E. and Zisserman, A.&quot;,&#10;   title = &quot;Automated Flower Classification over a Large Number of Classes&quot;,&#10;   booktitle = &quot;Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing&quot;,&#10;   year = &quot;2008&quot;,&#10;   month = &quot;Dec&quot;&#10;}" />
</div>

# `oxford_flowers102`


*   **Description**:

The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly
occurring in the United Kingdom. Each class consists of between 40 and 258
images. The images have large scale, pose and light variations. In addition,
there are categories that have large variations within the category and several
very similar categories.

The dataset is divided into a training set, a validation set and a test set. The
training set and validation set each consist of 10 images per class (totalling
1020 images each). The test set consists of the remaining 6149 images (minimum
20 per class).

Note: The dataset by default comes with a test size larger than the train size.
For more info see this
[issue](https://github.com/tensorflow/datasets/issues/3022).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/oxford-102-flower">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://www.robots.ox.ac.uk/~vgg/data/flowers/102/](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)

*   **Source code**:
    [`tfds.datasets.oxford_flowers102.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/oxford_flowers102/oxford_flowers102_dataset_builder.py)

*   **Versions**:

    *   **`2.1.1`** (default): No release notes.

*   **Download size**: `328.90 MiB`

*   **Dataset size**: `331.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,149
`'train'`      | 1,020
`'validation'` | 1,020

*   **Feature structure**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=102),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape           | Dtype  | Description
:-------- | :----------- | :-------------- | :----- | :----------
          | FeaturesDict |                 |        |
file_name | Text         |                 | string |
image     | Image        | (None, None, 3) | uint8  |
label     | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/oxford_flowers102-2.1.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/oxford_flowers102-2.1.1.html";
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
@InProceedings{Nilsback08,
   author = "Nilsback, M-E. and Zisserman, A.",
   title = "Automated Flower Classification over a Large Number of Classes",
   booktitle = "Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing",
   year = "2008",
   month = "Dec"
}
```

