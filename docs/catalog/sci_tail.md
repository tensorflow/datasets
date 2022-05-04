<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="sci_tail" />
  <meta itemprop="description" content="The SciTail dataset is an entailment dataset created from multiple-choice&#10;science exams and web sentences. Each question and the correct answer choice&#10;are converted into an assertive statement to form the hypothesis. Information&#10;retrieval is used to obtain relevant text from a large text corpus of web&#10;sentences, and these sentences are used as a premise P. The annotation of such&#10;premise-hypothesis pair is crowdsourced as supports (entails) or not (neutral),&#10;in order to create the SciTail dataset. The dataset contains 27,026 examples&#10;with 10,101 examples with entails label and 16,925 examples with neutral label.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;sci_tail&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/sci_tail" />
  <meta itemprop="sameAs" content="https://allenai.org/data/scitail" />
  <meta itemprop="citation" content="@inproceedings{khot2018scitail,&#10;    title={Scitail: A textual entailment dataset from science question answering},&#10;    author={Khot, Tushar and Sabharwal, Ashish and Clark, Peter},&#10;    booktitle={Proceedings of the 32th AAAI Conference on Artificial Intelligence (AAAI 2018)},&#10;    url = &quot;http://ai2-website.s3.amazonaws.com/publications/scitail-aaai-2018_cameraready.pdf&quot;,&#10;    year={2018}&#10;}" />
</div>

# `sci_tail`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The SciTail dataset is an entailment dataset created from multiple-choice
science exams and web sentences. Each question and the correct answer choice are
converted into an assertive statement to form the hypothesis. Information
retrieval is used to obtain relevant text from a large text corpus of web
sentences, and these sentences are used as a premise P. The annotation of such
premise-hypothesis pair is crowdsourced as supports (entails) or not (neutral),
in order to create the SciTail dataset. The dataset contains 27,026 examples
with 10,101 examples with entails label and 16,925 examples with neutral label.

*   **Homepage**:
    [https://allenai.org/data/scitail](https://allenai.org/data/scitail)

*   **Source code**:
    [`tfds.text.scitail.SciTail`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/scitail/scitail.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `13.52 MiB`

*   **Dataset size**: `6.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,126
`'train'`      | 23,097
`'validation'` | 1,304

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'premise': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype     | Description
:--------- | :----------- | :---- | :-------- | :----------
           | FeaturesDict |       |           |
hypothesis | Text         |       | tf.string |
label      | ClassLabel   |       | tf.int64  |
premise    | Text         |       | tf.string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/sci_tail-1.0.0.html";
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
@inproceedings{khot2018scitail,
    title={Scitail: A textual entailment dataset from science question answering},
    author={Khot, Tushar and Sabharwal, Ashish and Clark, Peter},
    booktitle={Proceedings of the 32th AAAI Conference on Artificial Intelligence (AAAI 2018)},
    url = "http://ai2-website.s3.amazonaws.com/publications/scitail-aaai-2018_cameraready.pdf",
    year={2018}
}
```

