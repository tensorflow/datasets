<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dolma" />
  <meta itemprop="description" content="Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining&#10;Research&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dolma&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dolma" />
  <meta itemprop="sameAs" content="https://github.com/allenai/dolma" />
  <meta itemprop="citation" content="@article{dolma,&#10;  title = {{Dolma: An Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},&#10;  author = {&#10;    Luca Soldaini and Rodney Kinney and Akshita Bhagia and Dustin Schwenk and David Atkinson and&#10;    Russell Authur and Ben Bogin and Khyathi Chandu and Jennifer Dumas and Yanai Elazar and&#10;    Valentin Hofmann and Ananya Harsh Jha and Sachin Kumar and Li Lucy and Xinxi Lyu and Ian Magnusson and&#10;    Jacob Morrison and Niklas Muennighoff and Aakanksha Naik and Crystal Nam and Matthew E. Peters and&#10;    Abhilasha Ravichander and Kyle Richardson and Zejiang Shen and Emma Strubell and Nishant Subramani and&#10;    Oyvind Tafjord and Evan Pete Walsh and Hannaneh Hajishirzi and Noah A. Smith and Luke Zettlemoyer and&#10;    Iz Beltagy and Dirk Groeneveld and Jesse Dodge and Kyle Lo&#10;},&#10;  year = {2024},&#10;  journal={arXiv preprint},&#10;}" />
</div>

# `dolma`


*   **Description**:

Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining
Research

*   **Homepage**:
    [https://github.com/allenai/dolma](https://github.com/allenai/dolma)

*   **Source code**:
    [`tfds.datasets.dolma.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/dolma/dolma_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `9.61 TiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ------------:
`'train'` | 3,403,336,408

*   **Feature structure**:

```python
FeaturesDict({
    'added': Text(shape=(), dtype=string),
    'created': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'source': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype  | Description
:------ | :----------- | :---- | :----- | :----------
        | FeaturesDict |       |        |
added   | Text         |       | string |
created | Text         |       | string |
id      | Text         |       | string |
source  | Text         |       | string |
text    | Text         |       | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dolma-1.0.0.html";
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
@article{dolma,
  title = {{Dolma: An Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
  author = {
    Luca Soldaini and Rodney Kinney and Akshita Bhagia and Dustin Schwenk and David Atkinson and
    Russell Authur and Ben Bogin and Khyathi Chandu and Jennifer Dumas and Yanai Elazar and
    Valentin Hofmann and Ananya Harsh Jha and Sachin Kumar and Li Lucy and Xinxi Lyu and Ian Magnusson and
    Jacob Morrison and Niklas Muennighoff and Aakanksha Naik and Crystal Nam and Matthew E. Peters and
    Abhilasha Ravichander and Kyle Richardson and Zejiang Shen and Emma Strubell and Nishant Subramani and
    Oyvind Tafjord and Evan Pete Walsh and Hannaneh Hajishirzi and Noah A. Smith and Luke Zettlemoyer and
    Iz Beltagy and Dirk Groeneveld and Jesse Dodge and Kyle Lo
},
  year = {2024},
  journal={arXiv preprint},
}
```

