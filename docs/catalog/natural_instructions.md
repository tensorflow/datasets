<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="natural_instructions" />
  <meta itemprop="description" content="# Description&#10;&#10;A compilation of 1600+ tasks phrased as natural instructions.&#10;The original task collection can be found at:&#10;https://github.com/allenai/natural-instructions.&#10;No preprocessing or changes were made to this original version.&#10;&#10;&#10;Note that users of this task collection should consult the underlying&#10;licenses of the contained datasets, and cite them accordingly.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;natural_instructions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/natural_instructions" />
  <meta itemprop="sameAs" content="https://github.com/allenai/natural-instructions" />
  <meta itemprop="citation" content="@article{wang2022benchmarking,&#10;  title={Benchmarking generalization via in-context instructions on 1,600+ language tasks},&#10;  author={Wang, Yizhong and Mishra, Swaroop and Alipoormolabashi, Pegah and Kordi, Yeganeh and Mirzaei, Amirreza and Arunkumar, Anjana and Ashok, Arjun and Dhanasekaran, Arut Selvan and Naik, Atharva and Stap, David and others},&#10;  journal={arXiv preprint arXiv:2204.07705},&#10;  year={2022}&#10;}" />
</div>

# `natural_instructions`


*   **Description**:

# Description

A compilation of 1600+ tasks phrased as natural instructions. The original task
collection can be found at: https://github.com/allenai/natural-instructions. No
preprocessing or changes were made to this original version.

Note that users of this task collection should consult the underlying licenses
of the contained datasets, and cite them accordingly.

*   **Homepage**:
    [https://github.com/allenai/natural-instructions](https://github.com/allenai/natural-instructions)

*   **Source code**:
    [`tfds.datasets.natural_instructions.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/natural_instructions/natural_instructions_dataset_builder.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Added task name field, and fixed ID used for
        shuffling to use stable IDs.

*   **Download size**: `3.08 GiB`

*   **Dataset size**: `4.73 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,040,134

*   **Feature structure**:

```python
FeaturesDict({
    'definition': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'input': Text(shape=(), dtype=string),
    'output': Text(shape=(), dtype=string),
    'source': Text(shape=(), dtype=string),
    'task_name': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype  | Description
:--------- | :----------- | :---- | :----- | :----------
           | FeaturesDict |       |        |
definition | Text         |       | string |
id         | Text         |       | string |
input      | Text         |       | string |
output     | Text         |       | string |
source     | Text         |       | string |
task_name  | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/natural_instructions-1.0.1.html";
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
@article{wang2022benchmarking,
  title={Benchmarking generalization via in-context instructions on 1,600+ language tasks},
  author={Wang, Yizhong and Mishra, Swaroop and Alipoormolabashi, Pegah and Kordi, Yeganeh and Mirzaei, Amirreza and Arunkumar, Anjana and Ashok, Arjun and Dhanasekaran, Arut Selvan and Naik, Atharva and Stap, David and others},
  journal={arXiv preprint arXiv:2204.07705},
  year={2022}
}
```

