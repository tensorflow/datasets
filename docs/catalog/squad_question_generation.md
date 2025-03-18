<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="squad_question_generation" />
  <meta itemprop="description" content="Question generation using squad dataset using data splits described in &#x27;Neural&#10;Question Generation from Text: A Preliminary Study&#x27; (Zhou et al, 2017) and&#10;&#x27;Learning to Ask: Neural Question Generation for Reading Comprehension&#x27; (Du et&#10;al, 2017).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;squad_question_generation&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/squad_question_generation" />
  <meta itemprop="sameAs" content="https://github.com/xinyadu/nqg&#10;@inproceedings{du-etal-2017-learning,&#10;    title = &quot;Learning to Ask: Neural Question Generation for Reading Comprehension&quot;,&#10;    author = &quot;Du, Xinya  and Shao, Junru  and Cardie, Claire&quot;,&#10;    booktitle = &quot;Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)&quot;,&#10;    month = jul,&#10;    year = &quot;2017&quot;,&#10;    address = &quot;Vancouver, Canada&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/P17-1123&quot;,&#10;    doi = &quot;10.18653/v1/P17-1123&quot;,&#10;    pages = &quot;1342--1352&quot;,&#10;}&#10;" />
  <meta itemprop="citation" content="@inproceedings{du-etal-2017-learning,&#10;    title = &quot;Learning to Ask: Neural Question Generation for Reading Comprehension&quot;,&#10;    author = &quot;Du, Xinya  and Shao, Junru  and Cardie, Claire&quot;,&#10;    booktitle = &quot;Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)&quot;,&#10;    month = jul,&#10;    year = &quot;2017&quot;,&#10;    address = &quot;Vancouver, Canada&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/P17-1123&quot;,&#10;    doi = &quot;10.18653/v1/P17-1123&quot;,&#10;    pages = &quot;1342--1352&quot;,&#10;}&#10;&#10;@inproceedings{rajpurkar-etal-2016-squad,&#10;    title = &quot;{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text&quot;,&#10;    author = &quot;Rajpurkar, Pranav  and Zhang, Jian  and Lopyrev, Konstantin  and Liang, Percy&quot;,&#10;    booktitle = &quot;Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = nov,&#10;    year = &quot;2016&quot;,&#10;    address = &quot;Austin, Texas&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/D16-1264&quot;,&#10;    doi = &quot;10.18653/v1/D16-1264&quot;,&#10;    pages = &quot;2383--2392&quot;,&#10;}" />
</div>

# `squad_question_generation`


*   **Description**:

Question generation using squad dataset using data splits described in 'Neural
Question Generation from Text: A Preliminary Study' (Zhou et al, 2017) and
'Learning to Ask: Neural Question Generation for Reading Comprehension' (Du et
al, 2017).

*   **Homepage**: [https://github.com/xinyadu/nqg
    @inproceedings{du-etal-2017-learning, title = "Learning to Ask: Neural
    Question Generation for Reading Comprehension", author = "Du, Xinya and
    Shao, Junru and Cardie, Claire", booktitle = "Proceedings of the 55th Annual
    Meeting of the Association for Computational Linguistics (Volume 1: Long
    Papers)", month = jul, year = "2017", address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics", url =
    "https://aclanthology.org/P17-1123", doi = "10.18653/v1/P17-1123", pages =
    "1342--1352",
    }](https://github.com/xinyadu/nqg @inproceedings{du-etal-2017-learning, title = "Learning to Ask: Neural Question Generation for Reading Comprehension", author = "Du, Xinya and Shao, Junru and Cardie, Claire", booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics \(Volume 1: Long Papers)",
    month = jul, year = "2017", address = "Vancouver, Canada", publisher =
    "Association for Computational Linguistics", url =
    "https://aclanthology.org/P17-1123", doi = "10.18653/v1/P17-1123", pages =
    "1342--1352", } )

*   **Source code**:
    [`tfds.text.squad_question_generation.SquadQuestionGeneration`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/squad_question_generation/squad_question_generation.py)

*   **Versions**:

    *   `1.0.0`: Initial build with unique SQuAD QAS ids in each split, using
        passage-level context (Zhou et al, 2017).

    *   `2.0.0`: Matches the original split of (Zhou et al, 2017), allows both
        sentence- and passage-level contexts, and uses answers from (Zhou et al,
        2017).

    *   **`3.0.0`** (default): Added the split of (Du et al, 2017) also.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('context_passage', 'question')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{du-etal-2017-learning,
    title = "Learning to Ask: Neural Question Generation for Reading Comprehension",
    author = "Du, Xinya  and Shao, Junru  and Cardie, Claire",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1123",
    doi = "10.18653/v1/P17-1123",
    pages = "1342--1352",
}

@inproceedings{rajpurkar-etal-2016-squad,
    title = "{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text",
    author = "Rajpurkar, Pranav  and Zhang, Jian  and Lopyrev, Konstantin  and Liang, Percy",
    booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2016",
    address = "Austin, Texas",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D16-1264",
    doi = "10.18653/v1/D16-1264",
    pages = "2383--2392",
}
```


## squad_question_generation/split_du (default config)

*   **Config description**: Answer independent question generation from
    passage-level contexts (Du et al, 2017).

*   **Download size**: `62.83 MiB`

*   **Dataset size**: `84.67 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 11,877
`'train'`      | 75,722
`'validation'` | 10,570

*   **Feature structure**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=string),
    'context_passage': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype  | Description
:-------------- | :----------- | :---- | :----- | :----------
                | FeaturesDict |       |        |
answer          | Text         |       | string |
context_passage | Text         |       | string |
question        | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/squad_question_generation-split_du-3.0.0.html";
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

## squad_question_generation/split_zhou

*   **Config description**: Answer-span dependent question generation from
    sentence- and passage-level contexts (Zhou et al, 2017).

*   **Download size**: `62.52 MiB`

*   **Dataset size**: `111.02 MiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 8,964
`'train'`      | 86,635
`'validation'` | 8,965

*   **Feature structure**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=string),
    'context_passage': Text(shape=(), dtype=string),
    'context_sentence': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature          | Class        | Shape | Dtype  | Description
:--------------- | :----------- | :---- | :----- | :----------
                 | FeaturesDict |       |        |
answer           | Text         |       | string |
context_passage  | Text         |       | string |
context_sentence | Text         |       | string |
question         | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/squad_question_generation-split_zhou-3.0.0.html";
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