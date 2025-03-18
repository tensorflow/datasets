<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lfw" />
  <meta itemprop="description" content="Labeled Faces in the Wild: A Database for Studying Face Recognition in&#10;Unconstrained Environments&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lfw&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/lfw-0.1.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lfw" />
  <meta itemprop="sameAs" content="http://vis-www.cs.umass.edu/lfw" />
  <meta itemprop="citation" content="@TechReport{LFWTech,&#10;    author = {Gary B. Huang and Manu Ramesh and Tamara Berg and Erik Learned-Miller},&#10;    title = {Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments},&#10;    institution = {University of Massachusetts, Amherst},&#10;    year = 2007,&#10;    number = {07-49},&#10;    month = {October}&#10;}" />
</div>

# `lfw`


*   **Description**:

Labeled Faces in the Wild: A Database for Studying Face Recognition in
Unconstrained Environments

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/lfw">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://vis-www.cs.umass.edu/lfw](http://vis-www.cs.umass.edu/lfw)

*   **Source code**:
    [`tfds.datasets.lfw.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/lfw/lfw_dataset_builder.py)

*   **Versions**:

    *   **`0.1.1`** (default): No release notes.

*   **Download size**: `172.20 MiB`

*   **Dataset size**: `180.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 13,233

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(250, 250, 3), dtype=uint8),
    'label': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape         | Dtype  | Description
:------ | :----------- | :------------ | :----- | :----------
        | FeaturesDict |               |        |
image   | Image        | (250, 250, 3) | uint8  |
label   | Text         |               | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('label', 'image')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/lfw-0.1.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/lfw-0.1.1.html";
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
@TechReport{LFWTech,
    author = {Gary B. Huang and Manu Ramesh and Tamara Berg and Erik Learned-Miller},
    title = {Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments},
    institution = {University of Massachusetts, Amherst},
    year = 2007,
    number = {07-49},
    month = {October}
}
```

