<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="q_re_cc" />
  <meta itemprop="description" content="A dataset containing 14K conversations with 81K question-answer pairs. QReCC is built on questions from TREC CAsT, QuAC and Google Natural Questions.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;q_re_cc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/q_re_cc" />
  <meta itemprop="sameAs" content="https://github.com/apple/ml-qrecc" />
  <meta itemprop="citation" content="@article{qrecc,&#10;  title={Open-Domain Question Answering Goes Conversational via Question Rewriting},&#10;  author={Anantha, Raviteja and Vakulenko, Svitlana and Tu, Zhucheng and Longpre, Shayne and Pulman, Stephen and Chappidi, Srinivas},&#10;  journal={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},&#10;  year={2021}&#10;}" />
</div>

# `q_re_cc`


*   **Description**:

A dataset containing 14K conversations with 81K question-answer pairs. QReCC is
built on questions from TREC CAsT, QuAC and Google Natural Questions.

*   **Homepage**:
    [https://github.com/apple/ml-qrecc](https://github.com/apple/ml-qrecc)

*   **Source code**:
    [`tfds.text.qrecc.QReCC`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/qrecc/qrecc.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `7.60 MiB`

*   **Dataset size**: `69.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 16,451
`'train'` | 63,501

*   **Feature structure**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=string),
    'answer_url': Text(shape=(), dtype=string),
    'context': Sequence(Text(shape=(), dtype=string)),
    'conversation_id': Scalar(shape=(), dtype=int32, description=The id of the conversation.),
    'question': Text(shape=(), dtype=string),
    'question_rewrite': Text(shape=(), dtype=string),
    'source': Text(shape=(), dtype=string),
    'turn_id': Scalar(shape=(), dtype=int32, description=The id of the conversation turn, within a conversation.),
})
```

*   **Feature documentation**:

| Feature          | Class          | Shape   | Dtype  | Description   |
| :--------------- | :------------- | :------ | :----- | :------------ |
|                  | FeaturesDict   |         |        |               |
| answer           | Text           |         | string |               |
| answer_url       | Text           |         | string |               |
| context          | Sequence(Text) | (None,) | string |               |
| conversation_id  | Scalar         |         | int32  | The id of the |
:                  :                :         :        : conversation. :
| question         | Text           |         | string |               |
| question_rewrite | Text           |         | string |               |
| source           | Text           |         | string | The original  |
:                  :                :         :        : source of the :
:                  :                :         :        : data --       :
:                  :                :         :        : either QuAC,  :
:                  :                :         :        : CAsT or       :
:                  :                :         :        : Natural       :
:                  :                :         :        : Questions     :
| turn_id          | Scalar         |         | int32  | The id of the |
:                  :                :         :        : conversation  :
:                  :                :         :        : turn, within  :
:                  :                :         :        : a             :
:                  :                :         :        : conversation. :

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/q_re_cc-1.0.0.html";
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
@article{qrecc,
  title={Open-Domain Question Answering Goes Conversational via Question Rewriting},
  author={Anantha, Raviteja and Vakulenko, Svitlana and Tu, Zhucheng and Longpre, Shayne and Pulman, Stephen and Chappidi, Srinivas},
  journal={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  year={2021}
}
```

