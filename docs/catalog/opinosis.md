<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="opinosis" />
  <meta itemprop="description" content="The Opinosis Opinion Dataset consists of sentences extracted from reviews for 51&#10;topics. Topics and opinions are obtained from Tripadvisor, Edmunds.com and&#10;Amazon.com.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;opinosis&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/opinosis" />
  <meta itemprop="sameAs" content="http://kavita-ganesan.com/opinosis/" />
  <meta itemprop="citation" content="@inproceedings{ganesan2010opinosis,&#10;  title={Opinosis: a graph-based approach to abstractive summarization of highly redundant opinions},&#10;  author={Ganesan, Kavita and Zhai, ChengXiang and Han, Jiawei},&#10;  booktitle={Proceedings of the 23rd International Conference on Computational Linguistics},&#10;  pages={340--348},&#10;  year={2010},&#10;  organization={Association for Computational Linguistics}&#10;}" />
</div>

# `opinosis`


*   **Description**:

The Opinosis Opinion Dataset consists of sentences extracted from reviews for 51
topics. Topics and opinions are obtained from Tripadvisor, Edmunds.com and
Amazon.com.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/opinosis">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://kavita-ganesan.com/opinosis/](http://kavita-ganesan.com/opinosis/)

*   **Source code**:
    [`tfds.datasets.opinosis.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/opinosis/opinosis_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `739.65 KiB`

*   **Dataset size**: `725.45 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 51

*   **Feature structure**:

```python
FeaturesDict({
    'review_sents': Text(shape=(), dtype=string),
    'summaries': Sequence(Text(shape=(), dtype=string)),
})
```

*   **Feature documentation**:

Feature      | Class          | Shape   | Dtype  | Description
:----------- | :------------- | :------ | :----- | :----------
             | FeaturesDict   |         |        |
review_sents | Text           |         | string |
summaries    | Sequence(Text) | (None,) | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('review_sents', 'summaries')`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/opinosis-1.0.0.html";
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
@inproceedings{ganesan2010opinosis,
  title={Opinosis: a graph-based approach to abstractive summarization of highly redundant opinions},
  author={Ganesan, Kavita and Zhai, ChengXiang and Han, Jiawei},
  booktitle={Proceedings of the 23rd International Conference on Computational Linguistics},
  pages={340--348},
  year={2010},
  organization={Association for Computational Linguistics}
}
```

