<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wiki_auto" />
  <meta itemprop="description" content="WikiAuto provides a set of aligned sentences from English Wikipedia and&#10;Simple English Wikipedia as a resource to train sentence simplification&#10;systems. The authors first crowd-sourced a set of manual alignments between&#10;sentences in a subset of the Simple English Wikipedia and their corresponding&#10;versions in English Wikipedia (this corresponds to the `manual` config),&#10;then trained a neural CRF system to predict these alignments. The trained&#10;model was then applied to the other articles in Simple English Wikipedia&#10;with an English counterpart to create a larger corpus of aligned sentences&#10;(corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and&#10;`auto_full_with_split` configs here).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wiki_auto&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wiki_auto" />
  <meta itemprop="sameAs" content="https://github.com/chaojiang06/wiki-auto" />
  <meta itemprop="citation" content="@inproceedings{acl/JiangMLZX20,&#10;  author    = {Chao Jiang and&#10;               Mounica Maddela and&#10;               Wuwei Lan and&#10;               Yang Zhong and&#10;               Wei Xu},&#10;  editor    = {Dan Jurafsky and&#10;               Joyce Chai and&#10;               Natalie Schluter and&#10;               Joel R. Tetreault},&#10;  title     = {Neural {CRF} Model for Sentence Alignment in Text Simplification},&#10;  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational&#10;               Linguistics, {ACL} 2020, Online, July 5-10, 2020},&#10;  pages     = {7943--7960},&#10;  publisher = {Association for Computational Linguistics},&#10;  year      = {2020},&#10;  url       = {https://www.aclweb.org/anthology/2020.acl-main.709/}&#10;}" />
</div>

# `wiki_auto`


*   **Description**:

WikiAuto provides a set of aligned sentences from English Wikipedia and Simple
English Wikipedia as a resource to train sentence simplification systems. The
authors first crowd-sourced a set of manual alignments between sentences in a
subset of the Simple English Wikipedia and their corresponding versions in
English Wikipedia (this corresponds to the `manual` config), then trained a
neural CRF system to predict these alignments. The trained model was then
applied to the other articles in Simple English Wikipedia with an English
counterpart to create a larger corpus of aligned sentences (corresponding to the
`auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split` configs
here).

*   **Homepage**:
    [https://github.com/chaojiang06/wiki-auto](https://github.com/chaojiang06/wiki-auto)

*   **Source code**:
    [`tfds.text_simplification.wiki_auto.WikiAuto`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text_simplification/wiki_auto/wiki_auto.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@inproceedings{acl/JiangMLZX20,
  author    = {Chao Jiang and
               Mounica Maddela and
               Wuwei Lan and
               Yang Zhong and
               Wei Xu},
  editor    = {Dan Jurafsky and
               Joyce Chai and
               Natalie Schluter and
               Joel R. Tetreault},
  title     = {Neural {CRF} Model for Sentence Alignment in Text Simplification},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational
               Linguistics, {ACL} 2020, Online, July 5-10, 2020},
  pages     = {7943--7960},
  publisher = {Association for Computational Linguistics},
  year      = {2020},
  url       = {https://www.aclweb.org/anthology/2020.acl-main.709/}
}
```


## wiki_auto/manual (default config)

*   **Config description**: A set of 10K Wikipedia sentence pairs aligned by
    crowd workers.

*   **Download size**: `53.47 MiB`

*   **Dataset size**: `76.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'dev'`  | 73,249
`'test'` | 118,074

*   **Feature structure**:

```python
FeaturesDict({
    'GLEU-score': float64,
    'alignment_label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'normal_sentence': Text(shape=(), dtype=string),
    'normal_sentence_id': Text(shape=(), dtype=string),
    'simple_sentence': Text(shape=(), dtype=string),
    'simple_sentence_id': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape | Dtype   | Description
:----------------- | :----------- | :---- | :------ | :----------
                   | FeaturesDict |       |         |
GLEU-score         | Tensor       |       | float64 |
alignment_label    | ClassLabel   |       | int64   |
normal_sentence    | Text         |       | string  |
normal_sentence_id | Text         |       | string  |
simple_sentence    | Text         |       | string  |
simple_sentence_id | Text         |       | string  |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_auto-manual-1.0.0.html";
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

## wiki_auto/auto_acl

*   **Config description**: Sentence pairs aligned to train the ACL2020 system.

*   **Download size**: `112.60 MiB`

*   **Dataset size**: `138.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (full)

*   **Splits**:

Split    | Examples
:------- | -------:
`'full'` | 488,332

*   **Feature structure**:

```python
FeaturesDict({
    'normal_sentence': Text(shape=(), dtype=string),
    'simple_sentence': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype  | Description
:-------------- | :----------- | :---- | :----- | :----------
                | FeaturesDict |       |        |
normal_sentence | Text         |       | string |
simple_sentence | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_auto-auto_acl-1.0.0.html";
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

## wiki_auto/auto_full_no_split

*   **Config description**: All automatically aligned sentence pairs without
    sentence splitting.

*   **Download size**: `135.02 MiB`

*   **Dataset size**: `166.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (full)

*   **Splits**:

Split    | Examples
:------- | -------:
`'full'` | 591,994

*   **Feature structure**:

```python
FeaturesDict({
    'normal_sentence': Text(shape=(), dtype=string),
    'simple_sentence': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype  | Description
:-------------- | :----------- | :---- | :----- | :----------
                | FeaturesDict |       |        |
normal_sentence | Text         |       | string |
simple_sentence | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_auto-auto_full_no_split-1.0.0.html";
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

## wiki_auto/auto_full_with_split

*   **Config description**: All automatically aligned sentence pairs with
    sentence splitting.

*   **Download size**: `115.09 MiB`

*   **Dataset size**: `141.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (full)

*   **Splits**:

Split    | Examples
:------- | -------:
`'full'` | 483,801

*   **Feature structure**:

```python
FeaturesDict({
    'normal_sentence': Text(shape=(), dtype=string),
    'simple_sentence': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype  | Description
:-------------- | :----------- | :---- | :----- | :----------
                | FeaturesDict |       |        |
normal_sentence | Text         |       | string |
simple_sentence | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_auto-auto_full_with_split-1.0.0.html";
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

## wiki_auto/auto

*   **Config description**: A large set of automatically aligned sentence pairs.

*   **Download size**: `2.01 GiB`

*   **Dataset size**: `1.76 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split      | Examples
:--------- | -------:
`'part_1'` | 125,059
`'part_2'` | 13,036

*   **Feature structure**:

```python
FeaturesDict({
    'example_id': Text(shape=(), dtype=string),
    'normal': FeaturesDict({
        'normal_article_content': Sequence({
            'normal_sentence': Text(shape=(), dtype=string),
            'normal_sentence_id': Text(shape=(), dtype=string),
        }),
        'normal_article_id': int32,
        'normal_article_title': Text(shape=(), dtype=string),
        'normal_article_url': Text(shape=(), dtype=string),
    }),
    'paragraph_alignment': Sequence({
        'normal_paragraph_id': Text(shape=(), dtype=string),
        'simple_paragraph_id': Text(shape=(), dtype=string),
    }),
    'sentence_alignment': Sequence({
        'normal_sentence_id': Text(shape=(), dtype=string),
        'simple_sentence_id': Text(shape=(), dtype=string),
    }),
    'simple': FeaturesDict({
        'simple_article_content': Sequence({
            'simple_sentence': Text(shape=(), dtype=string),
            'simple_sentence_id': Text(shape=(), dtype=string),
        }),
        'simple_article_id': int32,
        'simple_article_title': Text(shape=(), dtype=string),
        'simple_article_url': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature                                          | Class        | Shape | Dtype  | Description
:----------------------------------------------- | :----------- | :---- | :----- | :----------
                                                 | FeaturesDict |       |        |
example_id                                       | Text         |       | string |
normal                                           | FeaturesDict |       |        |
normal/normal_article_content                    | Sequence     |       |        |
normal/normal_article_content/normal_sentence    | Text         |       | string |
normal/normal_article_content/normal_sentence_id | Text         |       | string |
normal/normal_article_id                         | Tensor       |       | int32  |
normal/normal_article_title                      | Text         |       | string |
normal/normal_article_url                        | Text         |       | string |
paragraph_alignment                              | Sequence     |       |        |
paragraph_alignment/normal_paragraph_id          | Text         |       | string |
paragraph_alignment/simple_paragraph_id          | Text         |       | string |
sentence_alignment                               | Sequence     |       |        |
sentence_alignment/normal_sentence_id            | Text         |       | string |
sentence_alignment/simple_sentence_id            | Text         |       | string |
simple                                           | FeaturesDict |       |        |
simple/simple_article_content                    | Sequence     |       |        |
simple/simple_article_content/simple_sentence    | Text         |       | string |
simple/simple_article_content/simple_sentence_id | Text         |       | string |
simple/simple_article_id                         | Tensor       |       | int32  |
simple/simple_article_title                      | Text         |       | string |
simple/simple_article_url                        | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/wiki_auto-auto-1.0.0.html";
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