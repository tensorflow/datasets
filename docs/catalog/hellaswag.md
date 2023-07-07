<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="hellaswag" />
  <meta itemprop="description" content="The HellaSwag dataset is a benchmark for Commonsense NLI. It includes a context&#10;and some endings which complete the context.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;hellaswag&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/hellaswag" />
  <meta itemprop="sameAs" content="https://rowanzellers.com/hellaswag/" />
  <meta itemprop="citation" content="@inproceedings{zellers2019hellaswag,&#10;    title={HellaSwag: Can a Machine Really Finish Your Sentence?},&#10;    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},&#10;    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},&#10;    year={2019}&#10;}" />
</div>

# `hellaswag`


*   **Description**:

The HellaSwag dataset is a benchmark for Commonsense NLI. It includes a context
and some endings which complete the context.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/hellaswag">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://rowanzellers.com/hellaswag/](https://rowanzellers.com/hellaswag/)

*   **Source code**:
    [`tfds.text.Hellaswag`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/hellaswag.py)

*   **Versions**:

    *   `0.0.1`: No release notes.
    *   `1.0.0`: Adding separate splits for in-domain and out-of-domain
        validation/test sets.
    *   **`1.1.0`** (default): Another split dimension for source (wikihow vs
        activitynet)

*   **Download size**: `68.18 MiB`

*   **Dataset size**: `107.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                          | Examples
:----------------------------- | -------:
`'test'`                       | 10,003
`'test_ind_activitynet'`       | 1,870
`'test_ind_wikihow'`           | 3,132
`'test_ood_activitynet'`       | 1,651
`'test_ood_wikihow'`           | 3,350
`'train'`                      | 39,905
`'train_activitynet'`          | 14,740
`'train_wikihow'`              | 25,165
`'validation'`                 | 10,042
`'validation_ind_activitynet'` | 1,809
`'validation_ind_wikihow'`     | 3,192
`'validation_ood_activitynet'` | 1,434
`'validation_ood_wikihow'`     | 3,607

*   **Feature structure**:

```python
FeaturesDict({
    'activity_label': Text(shape=(), dtype=string),
    'context': Text(shape=(), dtype=string),
    'endings': Sequence(Text(shape=(), dtype=string)),
    'label': int32,
    'source_id': Text(shape=(), dtype=string),
    'split_type': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature        | Class          | Shape   | Dtype  | Description
:------------- | :------------- | :------ | :----- | :----------
               | FeaturesDict   |         |        |
activity_label | Text           |         | string |
context        | Text           |         | string |
endings        | Sequence(Text) | (None,) | string |
label          | Tensor         |         | int32  |
source_id      | Text           |         | string |
split_type     | Text           |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/hellaswag-1.1.0.html";
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
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
```

