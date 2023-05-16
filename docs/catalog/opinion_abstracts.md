<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="opinion_abstracts" />
  <meta itemprop="description" content="There are two sub datasets:&#10;&#10;(1) RottenTomatoes: The movie critics and consensus crawled from&#10;http://rottentomatoes.com/. It has fields of &quot;_movie_name&quot;, &quot;_movie_id&quot;,&#10;&quot;_critics&quot;, and &quot;_critic_consensus&quot;.&#10;&#10;(2) IDebate: The arguments crawled from http://idebate.org/. It has fields of&#10;&quot;_debate_name&quot;, &quot;_debate_id&quot;, &quot;_claim&quot;, &quot;_claim_id&quot;, &quot;_argument_sentences&quot;.&#10;&#10;See also https://web.eecs.umich.edu/~wangluxy/datasets/opinion_README.txt.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;opinion_abstracts&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/opinion_abstracts" />
  <meta itemprop="sameAs" content="https://web.eecs.umich.edu/~wangluxy/data.html" />
  <meta itemprop="citation" content="@inproceedings{wang-ling-2016-neural,&#10;    title = &quot;Neural Network-Based Abstract Generation for Opinions and Arguments&quot;,&#10;    author = &quot;Wang, Lu  and&#10;      Ling, Wang&quot;,&#10;    booktitle = &quot;Proceedings of the 2016 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies&quot;,&#10;    month = jun,&#10;    year = &quot;2016&quot;,&#10;    address = &quot;San Diego, California&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/N16-1007&quot;,&#10;    doi = &quot;10.18653/v1/N16-1007&quot;,&#10;    pages = &quot;47--57&quot;,&#10;}" />
</div>

# `opinion_abstracts`


*   **Description**:

There are two sub datasets:

(1) RottenTomatoes: The movie critics and consensus crawled from
http://rottentomatoes.com/. It has fields of "_movie_name", "_movie_id",
"_critics", and "_critic_consensus".

(2) IDebate: The arguments crawled from http://idebate.org/. It has fields of
"_debate_name", "_debate_id", "_claim", "_claim_id", "_argument_sentences".

See also https://web.eecs.umich.edu/~wangluxy/datasets/opinion_README.txt.

*   **Homepage**:
    [https://web.eecs.umich.edu/~wangluxy/data.html](https://web.eecs.umich.edu/~wangluxy/data.html)

*   **Source code**:
    [`tfds.datasets.opinion_abstracts.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/opinion_abstracts/opinion_abstracts_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `20.08 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{wang-ling-2016-neural,
    title = "Neural Network-Based Abstract Generation for Opinions and Arguments",
    author = "Wang, Lu  and
      Ling, Wang",
    booktitle = "Proceedings of the 2016 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2016",
    address = "San Diego, California",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N16-1007",
    doi = "10.18653/v1/N16-1007",
    pages = "47--57",
}
```


## opinion_abstracts/rotten_tomatoes (default config)

*   **Config description**: Professional critics and consensus of 3,731 movies.

*   **Dataset size**: `50.10 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,731

*   **Feature structure**:

```python
FeaturesDict({
    '_critic_consensus': string,
    '_critics': Sequence({
        'key': string,
        'value': string,
    }),
    '_movie_id': string,
    '_movie_name': string,
})
```

*   **Feature documentation**:

Feature           | Class        | Shape | Dtype  | Description
:---------------- | :----------- | :---- | :----- | :----------
                  | FeaturesDict |       |        |
_critic_consensus | Tensor       |       | string |
_critics          | Sequence     |       |        |
_critics/key      | Tensor       |       | string |
_critics/value    | Tensor       |       | string |
_movie_id         | Tensor       |       | string |
_movie_name       | Tensor       |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('_critics', '_critic_consensus')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/opinion_abstracts-rotten_tomatoes-1.0.0.html";
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

## opinion_abstracts/idebate

*   **Config description**: 2,259 claims for 676 debates.

*   **Dataset size**: `3.15 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 2,259

*   **Feature structure**:

```python
FeaturesDict({
    '_argument_sentences': Sequence({
        'key': string,
        'value': string,
    }),
    '_claim': string,
    '_claim_id': string,
    '_debate_name': string,
})
```

*   **Feature documentation**:

Feature                   | Class        | Shape | Dtype  | Description
:------------------------ | :----------- | :---- | :----- | :----------
                          | FeaturesDict |       |        |
_argument_sentences       | Sequence     |       |        |
_argument_sentences/key   | Tensor       |       | string |
_argument_sentences/value | Tensor       |       | string |
_claim                    | Tensor       |       | string |
_claim_id                 | Tensor       |       | string |
_debate_name              | Tensor       |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('_argument_sentences', '_claim')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/opinion_abstracts-idebate-1.0.0.html";
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