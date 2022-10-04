<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="placesfull" />
  <meta itemprop="description" content="The Places dataset is designed following principles of human visual cognition.&#10;Our goal is to build a core of visual knowledge that can be used to train&#10;artificial systems for high-level visual understanding tasks, such as scene&#10;context, object recognition, action and event prediction, and theory-of-mind&#10;inference.&#10;&#10;The semantic categories of Places are defined by their function: the labels&#10;represent the entry-level of an environment. To illustrate, the dataset has&#10;different categories of bedrooms, or streets, etc, as one does not act the same&#10;way, and does not make the same predictions of what can happen next, in a home&#10;bedroom, an hotel bedroom or a nursery. In total, Places contains more than 10&#10;million images comprising 400+ unique scene categories. The dataset features&#10;5000 to 30,000 training images per class, consistent with real-world frequencies&#10;of occurrence. Using convolutional neural networks (CNN), Places dataset allows&#10;learning of deep scene features for various scene recognition tasks, with the&#10;goal to establish new state-of-the-art performances on scene-centric benchmarks.&#10;&#10;Here we provide the Places Database and the trained CNNs for academic research&#10;and education purposes.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;placesfull&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/placesfull-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/placesfull" />
  <meta itemprop="sameAs" content="http://places2.csail.mit.edu/" />
  <meta itemprop="citation" content="@article{zhou2017places,&#10;  title={Places: A 10 million Image Database for Scene Recognition},&#10;  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},&#10;  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},&#10;  year={2017},&#10;  publisher={IEEE}&#10;}" />
</div>

# `placesfull`


*   **Description**:

The Places dataset is designed following principles of human visual cognition.
Our goal is to build a core of visual knowledge that can be used to train
artificial systems for high-level visual understanding tasks, such as scene
context, object recognition, action and event prediction, and theory-of-mind
inference.

The semantic categories of Places are defined by their function: the labels
represent the entry-level of an environment. To illustrate, the dataset has
different categories of bedrooms, or streets, etc, as one does not act the same
way, and does not make the same predictions of what can happen next, in a home
bedroom, an hotel bedroom or a nursery. In total, Places contains more than 10
million images comprising 400+ unique scene categories. The dataset features
5000 to 30,000 training images per class, consistent with real-world frequencies
of occurrence. Using convolutional neural networks (CNN), Places dataset allows
learning of deep scene features for various scene recognition tasks, with the
goal to establish new state-of-the-art performances on scene-centric benchmarks.

Here we provide the Places Database and the trained CNNs for academic research
and education purposes.

*   **Homepage**: [http://places2.csail.mit.edu/](http://places2.csail.mit.edu/)

*   **Source code**:
    [`tfds.image_classification.placesfull.Placesfull`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/placesfull/placesfull.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `143.56 GiB`

*   **Dataset size**: `136.56 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 10,653,087

*   **Feature structure**:

```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=435),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape         | Dtype     | Description
:------- | :----------- | :------------ | :-------- | :----------
         | FeaturesDict |               |           |
filename | Text         |               | tf.string |
image    | Image        | (256, 256, 3) | tf.uint8  |
label    | ClassLabel   |               | tf.int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label', 'filename')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/placesfull-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/placesfull-1.0.0.html";
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
@article{zhou2017places,
  title={Places: A 10 million Image Database for Scene Recognition},
  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2017},
  publisher={IEEE}
}
```

