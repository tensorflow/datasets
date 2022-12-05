<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cos_e" />
  <meta itemprop="description" content="Common Sense Explanations (CoS-E) allows for training language models to&#10;automatically generate explanations that can be used during training and&#10;inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cos_e&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cos_e" />
  <meta itemprop="sameAs" content="https://github.com/salesforce/cos-e" />
  <meta itemprop="citation" content="@inproceedings{rajani2019explain,&#10;     title = &quot;Explain Yourself! Leveraging Language models for Commonsense Reasoning&quot;,&#10;    author = &quot;Rajani, Nazneen Fatema  and&#10;      McCann, Bryan  and&#10;      Xiong, Caiming  and&#10;      Socher, Richard&quot;,&#10;      year=&quot;2019&quot;,&#10;    booktitle = &quot;Proceedings of the 2019 Conference of the Association for Computational Linguistics (ACL2019)&quot;,&#10;    url =&quot;https://arxiv.org/abs/1906.02361&quot;&#10;}" />
</div>

# `cos_e`


*   **Description**:

Common Sense Explanations (CoS-E) allows for training language models to
automatically generate explanations that can be used during training and
inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/cos-e">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/salesforce/cos-e](https://github.com/salesforce/cos-e)

*   **Source code**:
    [`tfds.text.CosE`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/cos_e.py)

*   **Versions**:

    *   **`0.0.1`** (default): No release notes.

*   **Download size**: `6.23 MiB`

*   **Dataset size**: `3.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 9,741
`'validation'` | 1,221

*   **Feature structure**:

```python
FeaturesDict({
    'abstractive_explanation': Text(shape=(), dtype=string),
    'answer': Text(shape=(), dtype=string),
    'choices': Sequence(Text(shape=(), dtype=string)),
    'extractive_explanation': Text(shape=(), dtype=string),
    'id': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                 | Class          | Shape   | Dtype  | Description
:---------------------- | :------------- | :------ | :----- | :----------
                        | FeaturesDict   |         |        |
abstractive_explanation | Text           |         | string |
answer                  | Text           |         | string |
choices                 | Sequence(Text) | (None,) | string |
extractive_explanation  | Text           |         | string |
id                      | Text           |         | string |
question                | Text           |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cos_e-0.0.1.html";
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
@inproceedings{rajani2019explain,
     title = "Explain Yourself! Leveraging Language models for Commonsense Reasoning",
    author = "Rajani, Nazneen Fatema  and
      McCann, Bryan  and
      Xiong, Caiming  and
      Socher, Richard",
      year="2019",
    booktitle = "Proceedings of the 2019 Conference of the Association for Computational Linguistics (ACL2019)",
    url ="https://arxiv.org/abs/1906.02361"
}
```

