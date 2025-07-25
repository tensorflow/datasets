<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="omniglot" />
  <meta itemprop="description" content="Omniglot data set for one-shot learning. This dataset contains 1623 different&#10;handwritten characters from 50 different alphabets.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;omniglot&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/omniglot-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/omniglot" />
  <meta itemprop="sameAs" content="https://github.com/brendenlake/omniglot/" />
  <meta itemprop="citation" content="@article{lake2015human,&#10;  title={Human-level concept learning through probabilistic program induction},&#10;  author={Lake, Brenden M and Salakhutdinov, Ruslan and Tenenbaum, Joshua B},&#10;  journal={Science},&#10;  volume={350},&#10;  number={6266},&#10;  pages={1332--1338},&#10;  year={2015},&#10;  publisher={American Association for the Advancement of Science}&#10;}" />
</div>

# `omniglot`


*   **Description**:

Omniglot data set for one-shot learning. This dataset contains 1623 different
handwritten characters from 50 different alphabets.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/onmiglot">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/brendenlake/omniglot/](https://github.com/brendenlake/omniglot/)

*   **Source code**:
    [`tfds.image_classification.Omniglot`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/omniglot.py)

*   **Versions**:

    *   **`3.0.0`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `17.95 MiB`

*   **Dataset size**: `12.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split      | Examples
:--------- | -------:
`'small1'` | 2,720
`'small2'` | 3,120
`'test'`   | 13,180
`'train'`  | 19,280

*   **Feature structure**:

```python
FeaturesDict({
    'alphabet': ClassLabel(shape=(), dtype=int64, num_classes=50),
    'alphabet_char_id': int64,
    'image': Image(shape=(105, 105, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=1623),
})
```

*   **Feature documentation**:

Feature          | Class        | Shape         | Dtype | Description
:--------------- | :----------- | :------------ | :---- | :----------
                 | FeaturesDict |               |       |
alphabet         | ClassLabel   |               | int64 |
alphabet_char_id | Tensor       |               | int64 |
image            | Image        | (105, 105, 3) | uint8 |
label            | ClassLabel   |               | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/omniglot-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/omniglot-3.0.0.html";
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
@article{lake2015human,
  title={Human-level concept learning through probabilistic program induction},
  author={Lake, Brenden M and Salakhutdinov, Ruslan and Tenenbaum, Joshua B},
  journal={Science},
  volume={350},
  number={6266},
  pages={1332--1338},
  year={2015},
  publisher={American Association for the Advancement of Science}
}
```

