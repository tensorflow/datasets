<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rock_paper_scissors" />
  <meta itemprop="description" content="Images of hands playing rock, paper, scissor game.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rock_paper_scissors&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/rock_paper_scissors-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rock_paper_scissors" />
  <meta itemprop="sameAs" content="http://laurencemoroney.com/rock-paper-scissors-dataset" />
  <meta itemprop="citation" content="@ONLINE {rps,&#10;author = &quot;Laurence Moroney&quot;,&#10;title = &quot;Rock, Paper, Scissors Dataset&quot;,&#10;month = &quot;feb&quot;,&#10;year = &quot;2019&quot;,&#10;url = &quot;http://laurencemoroney.com/rock-paper-scissors-dataset&quot;&#10;}" />
</div>

# `rock_paper_scissors`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=rock_paper_scissors">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

Images of hands playing rock, paper, scissor game.

*   **Homepage**:
    [http://laurencemoroney.com/rock-paper-scissors-dataset](http://laurencemoroney.com/rock-paper-scissors-dataset)

*   **Source code**:
    [`tfds.datasets.rock_paper_scissors.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/rock_paper_scissors/rock_paper_scissors_dataset_builder.py)

*   **Versions**:

    *   **`3.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `219.53 MiB`

*   **Dataset size**: `219.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 372
`'train'` | 2,520

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(300, 300, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
})
```

*   **Feature documentation**:

Feature | Class        | Shape         | Dtype | Description
:------ | :----------- | :------------ | :---- | :----------
        | FeaturesDict |               |       |
image   | Image        | (300, 300, 3) | uint8 |
label   | ClassLabel   |               | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/rock_paper_scissors-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/rock_paper_scissors-3.0.0.html";
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
@ONLINE {rps,
author = "Laurence Moroney",
title = "Rock, Paper, Scissors Dataset",
month = "feb",
year = "2019",
url = "http://laurencemoroney.com/rock-paper-scissors-dataset"
}
```

