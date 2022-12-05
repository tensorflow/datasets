<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="unified_qa" />
  <meta itemprop="description" content="The UnifiedQA benchmark consists of 20 main question answering (QA) datasets&#10;(each may have multiple versions) that target different formats as well as&#10;various complex linguistic phenomena. These datasets are grouped into several&#10;formats/categories, including: extractive QA, abstractive QA, multiple-choice&#10;QA, and yes/no QA. Additionally, contrast sets are used for several datasets&#10;(denoted with &quot;contrast_sets_&quot;). These evaluation sets are expert-generated&#10;perturbations that deviate from the patterns common in the original dataset. For&#10;several datasets that do not come with evidence paragraphs, two variants are&#10;included: one where the datasets are used as-is and another that uses paragraphs&#10;fetched via an information retrieval system as additional evidence, indicated&#10;with &quot;_ir&quot; tags.&#10;&#10;More information can be found at: https://github.com/allenai/unifiedqa.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;unified_qa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/unified_qa" />
  <meta itemprop="sameAs" content="https://github.com/allenai/unifiedqa" />
  <meta itemprop="citation" content="http://data.allenai.org/ai2-science-questions&#10;&#10;@inproceedings{khashabi-etal-2020-unifiedqa,&#10;    title = &quot;{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System&quot;,&#10;    author = &quot;Khashabi, Daniel  and&#10;      Min, Sewon  and&#10;      Khot, Tushar  and&#10;      Sabharwal, Ashish  and&#10;      Tafjord, Oyvind  and&#10;      Clark, Peter  and&#10;      Hajishirzi, Hannaneh&quot;,&#10;    booktitle = &quot;Findings of the Association for Computational Linguistics: EMNLP 2020&quot;,&#10;    month = nov,&#10;    year = &quot;2020&quot;,&#10;    address = &quot;Online&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/2020.findings-emnlp.171&quot;,&#10;    doi = &quot;10.18653/v1/2020.findings-emnlp.171&quot;,&#10;    pages = &quot;1896--1907&quot;,&#10;}&#10;&#10;Note that each UnifiedQA dataset has its own citation. Please see the source to&#10;see the correct citation for each contained dataset.&quot;" />
</div>

# `unified_qa`


*   **Description**:

The UnifiedQA benchmark consists of 20 main question answering (QA) datasets
(each may have multiple versions) that target different formats as well as
various complex linguistic phenomena. These datasets are grouped into several
formats/categories, including: extractive QA, abstractive QA, multiple-choice
QA, and yes/no QA. Additionally, contrast sets are used for several datasets
(denoted with "contrast_sets_"). These evaluation sets are expert-generated
perturbations that deviate from the patterns common in the original dataset. For
several datasets that do not come with evidence paragraphs, two variants are
included: one where the datasets are used as-is and another that uses paragraphs
fetched via an information retrieval system as additional evidence, indicated
with "_ir" tags.

More information can be found at: https://github.com/allenai/unifiedqa.

*   **Homepage**:
    [https://github.com/allenai/unifiedqa](https://github.com/allenai/unifiedqa)

*   **Source code**:
    [`tfds.text.unifiedqa.UnifiedQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/unifiedqa/unifiedqa.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Feature structure**:

```python
FeaturesDict({
    'input': string,
    'output': string,
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype  | Description
:------ | :----------- | :---- | :----- | :----------
        | FeaturesDict |       |        |
input   | Tensor       |       | string |
output  | Tensor       |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.


## unified_qa/ai2_science_elementary (default config)

*   **Config description**: The AI2 Science Questions dataset consists of
    questions used in student assessments in the United States across elementary
    and middle school grade levels. Each question is 4-way multiple choice
    format and may or may not include a diagram element. This set consists of
    questions used for elementary school grade levels.

*   **Download size**: `345.59 KiB`

*   **Dataset size**: `390.02 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 542
`'train'`      | 623
`'validation'` | 123

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-ai2_science_elementary-1.0.0.html";
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
http://data.allenai.org/ai2-science-questions

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/ai2_science_middle

*   **Config description**: The AI2 Science Questions dataset consists of
    questions used in student assessments in the United States across elementary
    and middle school grade levels. Each question is 4-way multiple choice
    format and may or may not include a diagram element. This set consists of
    questions used for middle school grade levels.

*   **Download size**: `428.41 KiB`

*   **Dataset size**: `477.40 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 679
`'train'`      | 605
`'validation'` | 125

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-ai2_science_middle-1.0.0.html";
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
http://data.allenai.org/ai2-science-questions

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/ambigqa

*   **Config description**: AmbigQA is an open-domain question answering task
    which involves finding every plausible answer, and then rewriting the
    question for each one to resolve the ambiguity.

*   **Download size**: `2.27 MiB`

*   **Dataset size**: `3.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 19,806
`'validation'` | 5,674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-ambigqa-1.0.0.html";
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
@inproceedings{min-etal-2020-ambigqa,
    title = "{A}mbig{QA}: Answering Ambiguous Open-domain Questions",
    author = "Min, Sewon  and
      Michael, Julian  and
      Hajishirzi, Hannaneh  and
      Zettlemoyer, Luke",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.466",
    doi = "10.18653/v1/2020.emnlp-main.466",
    pages = "5783--5797",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_easy

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "easy" questions.

*   **Download size**: `1.24 MiB`

*   **Dataset size**: `1.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,376
`'train'`      | 2,251
`'validation'` | 570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_easy-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_easy_dev

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "easy" questions.

*   **Download size**: `1.24 MiB`

*   **Dataset size**: `1.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,376
`'train'`      | 2,251
`'validation'` | 570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_easy_dev-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_easy_with_ir

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "easy" questions. This version includes
    paragraphs fetched via an information retrieval system as additional
    evidence.

*   **Download size**: `7.00 MiB`

*   **Dataset size**: `7.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,376
`'train'`      | 2,251
`'validation'` | 570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_easy_with_ir-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_easy_with_ir_dev

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "easy" questions. This version includes
    paragraphs fetched via an information retrieval system as additional
    evidence.

*   **Download size**: `7.00 MiB`

*   **Dataset size**: `7.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,376
`'train'`      | 2,251
`'validation'` | 570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_easy_with_ir_dev-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_hard

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "hard" questions.

*   **Download size**: `758.03 KiB`

*   **Dataset size**: `848.28 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,172
`'train'`      | 1,119
`'validation'` | 299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_hard-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_hard_dev

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "hard" questions.

*   **Download size**: `758.03 KiB`

*   **Dataset size**: `848.28 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,172
`'train'`      | 1,119
`'validation'` | 299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_hard_dev-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_hard_with_ir

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "hard" questions. This version includes
    paragraphs fetched via an information retrieval system as additional
    evidence.

*   **Download size**: `3.53 MiB`

*   **Dataset size**: `3.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,172
`'train'`      | 1,119
`'validation'` | 299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_hard_with_ir-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/arc_hard_with_ir_dev

*   **Config description**: This dataset consists of genuine grade-school level,
    multiple-choice science questions, assembled to encourage research in
    advanced question-answering. The dataset is partitioned into a Challenge Set
    and an Easy Set, where the former contains only questions answered
    incorrectly by both a retrieval-based algorithm and a word co-occurrence
    algorithm. This set consists of "hard" questions. This version includes
    paragraphs fetched via an information retrieval system as additional
    evidence.

*   **Download size**: `3.53 MiB`

*   **Dataset size**: `3.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,172
`'train'`      | 1,119
`'validation'` | 299

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-arc_hard_with_ir_dev-1.0.0.html";
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
@article{clark2018think,
    title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
    author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
    journal={arXiv preprint arXiv:1803.05457},
    year={2018}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/boolq

*   **Config description**: BoolQ is a question answering dataset for yes/no
    questions. These questions are naturally occurring ---they are generated in
    unprompted and unconstrained settings. Each example is a triplet of
    (question, passage, answer), with the title of the page as optional
    additional context. The text-pair classification setup is similar to
    existing natural language inference tasks.

*   **Download size**: `7.77 MiB`

*   **Dataset size**: `8.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 9,427
`'validation'` | 3,270

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-boolq-1.0.0.html";
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
@inproceedings{clark-etal-2019-boolq,
    title = "{B}ool{Q}: Exploring the Surprising Difficulty of Natural Yes/No Questions",
    author = "Clark, Christopher  and
      Lee, Kenton  and
      Chang, Ming-Wei  and
      Kwiatkowski, Tom  and
      Collins, Michael  and
      Toutanova, Kristina",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1300",
    doi = "10.18653/v1/N19-1300",
    pages = "2924--2936",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/boolq_np

*   **Config description**: BoolQ is a question answering dataset for yes/no
    questions. These questions are naturally occurring ---they are generated in
    unprompted and unconstrained settings. Each example is a triplet of
    (question, passage, answer), with the title of the page as optional
    additional context. The text-pair classification setup is similar to
    existing natural language inference tasks. This version adds natural
    perturbations to the original version.

*   **Download size**: `10.80 MiB`

*   **Dataset size**: `11.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 9,727
`'validation'` | 7,596

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-boolq_np-1.0.0.html";
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
@inproceedings{khashabi-etal-2020-bang,
    title = "More Bang for Your Buck: Natural Perturbation for Robust Question Answering",
    author = "Khashabi, Daniel  and
      Khot, Tushar  and
      Sabharwal, Ashish",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.12",
    doi = "10.18653/v1/2020.emnlp-main.12",
    pages = "163--170",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/commonsenseqa

*   **Config description**: CommonsenseQA is a new multiple-choice question
    answering dataset that requires different types of commonsense knowledge to
    predict the correct answers . It contains questions with one correct answer
    and four distractor answers.

*   **Download size**: `1.79 MiB`

*   **Dataset size**: `2.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,140
`'train'`      | 9,741
`'validation'` | 1,221

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-commonsenseqa-1.0.0.html";
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
@inproceedings{talmor-etal-2019-commonsenseqa,
    title = "{C}ommonsense{QA}: A Question Answering Challenge Targeting Commonsense Knowledge",
    author = "Talmor, Alon  and
      Herzig, Jonathan  and
      Lourie, Nicholas  and
      Berant, Jonathan",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1421",
    doi = "10.18653/v1/N19-1421",
    pages = "4149--4158",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/commonsenseqa_test

*   **Config description**: CommonsenseQA is a new multiple-choice question
    answering dataset that requires different types of commonsense knowledge to
    predict the correct answers . It contains questions with one correct answer
    and four distractor answers.

*   **Download size**: `1.79 MiB`

*   **Dataset size**: `2.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,140
`'train'`      | 9,741
`'validation'` | 1,221

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-commonsenseqa_test-1.0.0.html";
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
@inproceedings{talmor-etal-2019-commonsenseqa,
    title = "{C}ommonsense{QA}: A Question Answering Challenge Targeting Commonsense Knowledge",
    author = "Talmor, Alon  and
      Herzig, Jonathan  and
      Lourie, Nicholas  and
      Berant, Jonathan",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1421",
    doi = "10.18653/v1/N19-1421",
    pages = "4149--4158",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/contrast_sets_boolq

*   **Config description**: BoolQ is a question answering dataset for yes/no
    questions. These questions are naturally occurring ---they are generated in
    unprompted and unconstrained settings. Each example is a triplet of
    (question, passage, answer), with the title of the page as optional
    additional context. The text-pair classification setup is similar to
    existing natural language inference tasks. This version uses contrast sets.
    These evaluation sets are expert-generated perturbations that deviate from
    the patterns common in the original dataset.

*   **Download size**: `438.51 KiB`

*   **Dataset size**: `462.35 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 340
`'validation'` | 340

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-contrast_sets_boolq-1.0.0.html";
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
@inproceedings{clark-etal-2019-boolq,
    title = "{B}ool{Q}: Exploring the Surprising Difficulty of Natural Yes/No Questions",
    author = "Clark, Christopher  and
      Lee, Kenton  and
      Chang, Ming-Wei  and
      Kwiatkowski, Tom  and
      Collins, Michael  and
      Toutanova, Kristina",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1300",
    doi = "10.18653/v1/N19-1300",
    pages = "2924--2936",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/contrast_sets_drop

*   **Config description**: DROP is a crowdsourced, adversarially-created QA
    benchmark, in which a system must resolve references in a question, perhaps
    to multiple input positions, and perform discrete operations over them (such
    as addition, counting, or sorting). These operations require a much more
    comprehensive understanding of the content of paragraphs than what was
    necessary for prior datasets. This version uses contrast sets. These
    evaluation sets are expert-generated perturbations that deviate from the
    patterns common in the original dataset.

*   **Download size**: `2.20 MiB`

*   **Dataset size**: `2.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 947
`'validation'` | 947

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-contrast_sets_drop-1.0.0.html";
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
@inproceedings{dua-etal-2019-drop,
    title = "{DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs",
    author = "Dua, Dheeru  and
      Wang, Yizhong  and
      Dasigi, Pradeep  and
      Stanovsky, Gabriel  and
      Singh, Sameer  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1246",
    doi = "10.18653/v1/N19-1246",
    pages = "2368--2378",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/contrast_sets_quoref

*   **Config description**: This dataset tests the coreferential reasoning
    capability of reading comprehension systems. In this span-selection
    benchmark containing questions over paragraphs from Wikipedia, a system must
    resolve hard coreferences before selecting the appropriate span(s) in the
    paragraphs for answering questions. This version uses contrast sets. These
    evaluation sets are expert-generated perturbations that deviate from the
    patterns common in the original dataset.

*   **Download size**: `2.60 MiB`

*   **Dataset size**: `2.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 700
`'validation'` | 700

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-contrast_sets_quoref-1.0.0.html";
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
@inproceedings{dasigi-etal-2019-quoref,
    title = "{Q}uoref: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning",
    author = "Dasigi, Pradeep  and
      Liu, Nelson F.  and
      Marasovi{'c}, Ana  and
      Smith, Noah A.  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1606",
    doi = "10.18653/v1/D19-1606",
    pages = "5925--5932",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/contrast_sets_ropes

*   **Config description**: This dataset tests a system's ability to apply
    knowledge from a passage of text to a new situation. A system is presented a
    background passage containing a causal or qualitative relation(s) (e.g.,
    "animal pollinators increase efficiency of fertilization in flowers"), a
    novel situation that uses this background, and questions that require
    reasoning about effects of the relationships in the background passage in
    the context of the situation. This version uses contrast sets. These
    evaluation sets are expert-generated perturbations that deviate from the
    patterns common in the original dataset.

*   **Download size**: `1.97 MiB`

*   **Dataset size**: `2.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 974
`'validation'` | 974

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-contrast_sets_ropes-1.0.0.html";
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
@inproceedings{lin-etal-2019-reasoning,
    title = "Reasoning Over Paragraph Effects in Situations",
    author = "Lin, Kevin  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5808",
    doi = "10.18653/v1/D19-5808",
    pages = "58--62",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/drop

*   **Config description**: DROP is a crowdsourced, adversarially-created QA
    benchmark, in which a system must resolve references in a question, perhaps
    to multiple input positions, and perform discrete operations over them (such
    as addition, counting, or sorting). These operations require a much more
    comprehensive understanding of the content of paragraphs than what was
    necessary for prior datasets.

*   **Download size**: `105.18 MiB`

*   **Dataset size**: `108.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 77,399
`'validation'` | 9,536

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-drop-1.0.0.html";
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
@inproceedings{dua-etal-2019-drop,
    title = "{DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs",
    author = "Dua, Dheeru  and
      Wang, Yizhong  and
      Dasigi, Pradeep  and
      Stanovsky, Gabriel  and
      Singh, Sameer  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1246",
    doi = "10.18653/v1/N19-1246",
    pages = "2368--2378",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/mctest

*   **Config description**: MCTest requires machines to answer multiple-choice
    reading comprehension questions about fictional stories, directly tackling
    the high-level goal of open-domain machine comprehension. Reading
    comprehension can test advanced abilities such as causal reasoning and
    understanding the world, yet, by being multiple-choice, still provide a
    clear metric. By being fictional, the answer typically can be found only in
    the story itself. The stories and questions are also carefully limited to
    those a young child would understand, reducing the world knowledge that is
    required for the task.

*   **Download size**: `2.14 MiB`

*   **Dataset size**: `2.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 1,480
`'validation'` | 320

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-mctest-1.0.0.html";
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
@inproceedings{richardson-etal-2013-mctest,
    title = "{MCT}est: A Challenge Dataset for the Open-Domain Machine Comprehension of Text",
    author = "Richardson, Matthew  and
      Burges, Christopher J.C.  and
      Renshaw, Erin",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D13-1020",
    pages = "193--203",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/mctest_corrected_the_separator

*   **Config description**: MCTest requires machines to answer multiple-choice
    reading comprehension questions about fictional stories, directly tackling
    the high-level goal of open-domain machine comprehension. Reading
    comprehension can test advanced abilities such as causal reasoning and
    understanding the world, yet, by being multiple-choice, still provide a
    clear metric. By being fictional, the answer typically can be found only in
    the story itself. The stories and questions are also carefully limited to
    those a young child would understand, reducing the world knowledge that is
    required for the task.

*   **Download size**: `2.15 MiB`

*   **Dataset size**: `2.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 1,480
`'validation'` | 320

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-mctest_corrected_the_separator-1.0.0.html";
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
@inproceedings{richardson-etal-2013-mctest,
    title = "{MCT}est: A Challenge Dataset for the Open-Domain Machine Comprehension of Text",
    author = "Richardson, Matthew  and
      Burges, Christopher J.C.  and
      Renshaw, Erin",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D13-1020",
    pages = "193--203",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/multirc

*   **Config description**: MultiRC is a reading comprehension challenge in
    which questions can only be answered by taking into account information from
    multiple sentences. Questions and answers for this challenge were solicited
    and verified through a 4-step crowdsourcing experiment. The dataset contains
    questions for paragraphs across 7 different domains ( elementary school
    science, news, travel guides, fiction stories, etc) bringing in linguistic
    diversity to the texts and to the questions wordings.

*   **Download size**: `897.09 KiB`

*   **Dataset size**: `918.42 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 312
`'validation'` | 312

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-multirc-1.0.0.html";
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
@inproceedings{khashabi-etal-2018-looking,
    title = "Looking Beyond the Surface: A Challenge Set for Reading Comprehension over Multiple Sentences",
    author = "Khashabi, Daniel  and
      Chaturvedi, Snigdha  and
      Roth, Michael  and
      Upadhyay, Shyam  and
      Roth, Dan",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1023",
    doi = "10.18653/v1/N18-1023",
    pages = "252--262",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/narrativeqa

*   **Config description**: NarrativeQA is an English-lanaguage dataset of
    stories and corresponding questions designed to test reading comprehension,
    especially on long documents.

*   **Download size**: `308.28 MiB`

*   **Dataset size**: `311.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 21,114
`'train'`      | 65,494
`'validation'` | 6,922

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-narrativeqa-1.0.0.html";
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
@article{kocisky-etal-2018-narrativeqa,
    title = "The {N}arrative{QA} Reading Comprehension Challenge",
    author = "Ko{{c}}isk{'y}, Tom{'a}{{s}}  and
      Schwarz, Jonathan  and
      Blunsom, Phil  and
      Dyer, Chris  and
      Hermann, Karl Moritz  and
      Melis, G{'a}bor  and
      Grefenstette, Edward",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "6",
    year = "2018",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q18-1023",
    doi = "10.1162/tacl_a_00023",
    pages = "317--328",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/narrativeqa_dev

*   **Config description**: NarrativeQA is an English-lanaguage dataset of
    stories and corresponding questions designed to test reading comprehension,
    especially on long documents.

*   **Download size**: `308.28 MiB`

*   **Dataset size**: `311.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 21,114
`'train'`      | 65,494
`'validation'` | 6,922

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-narrativeqa_dev-1.0.0.html";
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
@article{kocisky-etal-2018-narrativeqa,
    title = "The {N}arrative{QA} Reading Comprehension Challenge",
    author = "Ko{{c}}isk{'y}, Tom{'a}{{s}}  and
      Schwarz, Jonathan  and
      Blunsom, Phil  and
      Dyer, Chris  and
      Hermann, Karl Moritz  and
      Melis, G{'a}bor  and
      Grefenstette, Edward",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "6",
    year = "2018",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q18-1023",
    doi = "10.1162/tacl_a_00023",
    pages = "317--328",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/natural_questions

*   **Config description**: The NQ corpus contains questions from real users,
    and it requires QA systems to read and comprehend an entire Wikipedia
    article that may or may not contain the answer to the question. The
    inclusion of real user questions, and the requirement that solutions should
    read an entire page to find the answer, cause NQ to be a more realistic and
    challenging task than prior QA datasets.

*   **Download size**: `6.95 MiB`

*   **Dataset size**: `9.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 96,075
`'validation'` | 2,295

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-natural_questions-1.0.0.html";
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
@article{kwiatkowski-etal-2019-natural,
    title = "Natural Questions: A Benchmark for Question Answering Research",
    author = "Kwiatkowski, Tom  and
      Palomaki, Jennimaria  and
      Redfield, Olivia  and
      Collins, Michael  and
      Parikh, Ankur  and
      Alberti, Chris  and
      Epstein, Danielle  and
      Polosukhin, Illia  and
      Devlin, Jacob  and
      Lee, Kenton  and
      Toutanova, Kristina  and
      Jones, Llion  and
      Kelcey, Matthew  and
      Chang, Ming-Wei  and
      Dai, Andrew M.  and
      Uszkoreit, Jakob  and
      Le, Quoc  and
      Petrov, Slav",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "7",
    year = "2019",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q19-1026",
    doi = "10.1162/tacl_a_00276",
    pages = "452--466",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/natural_questions_direct_ans

*   **Config description**: The NQ corpus contains questions from real users,
    and it requires QA systems to read and comprehend an entire Wikipedia
    article that may or may not contain the answer to the question. The
    inclusion of real user questions, and the requirement that solutions should
    read an entire page to find the answer, cause NQ to be a more realistic and
    challenging task than prior QA datasets. This version consists of
    direct-answer questions.

*   **Download size**: `6.82 MiB`

*   **Dataset size**: `10.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,468
`'train'`      | 96,676
`'validation'` | 10,693

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-natural_questions_direct_ans-1.0.0.html";
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
@article{kwiatkowski-etal-2019-natural,
    title = "Natural Questions: A Benchmark for Question Answering Research",
    author = "Kwiatkowski, Tom  and
      Palomaki, Jennimaria  and
      Redfield, Olivia  and
      Collins, Michael  and
      Parikh, Ankur  and
      Alberti, Chris  and
      Epstein, Danielle  and
      Polosukhin, Illia  and
      Devlin, Jacob  and
      Lee, Kenton  and
      Toutanova, Kristina  and
      Jones, Llion  and
      Kelcey, Matthew  and
      Chang, Ming-Wei  and
      Dai, Andrew M.  and
      Uszkoreit, Jakob  and
      Le, Quoc  and
      Petrov, Slav",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "7",
    year = "2019",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q19-1026",
    doi = "10.1162/tacl_a_00276",
    pages = "452--466",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/natural_questions_direct_ans_test

*   **Config description**: The NQ corpus contains questions from real users,
    and it requires QA systems to read and comprehend an entire Wikipedia
    article that may or may not contain the answer to the question. The
    inclusion of real user questions, and the requirement that solutions should
    read an entire page to find the answer, cause NQ to be a more realistic and
    challenging task than prior QA datasets. This version consists of
    direct-answer questions.

*   **Download size**: `6.82 MiB`

*   **Dataset size**: `10.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,468
`'train'`      | 96,676
`'validation'` | 10,693

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-natural_questions_direct_ans_test-1.0.0.html";
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
@article{kwiatkowski-etal-2019-natural,
    title = "Natural Questions: A Benchmark for Question Answering Research",
    author = "Kwiatkowski, Tom  and
      Palomaki, Jennimaria  and
      Redfield, Olivia  and
      Collins, Michael  and
      Parikh, Ankur  and
      Alberti, Chris  and
      Epstein, Danielle  and
      Polosukhin, Illia  and
      Devlin, Jacob  and
      Lee, Kenton  and
      Toutanova, Kristina  and
      Jones, Llion  and
      Kelcey, Matthew  and
      Chang, Ming-Wei  and
      Dai, Andrew M.  and
      Uszkoreit, Jakob  and
      Le, Quoc  and
      Petrov, Slav",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "7",
    year = "2019",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q19-1026",
    doi = "10.1162/tacl_a_00276",
    pages = "452--466",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/natural_questions_with_dpr_para

*   **Config description**: The NQ corpus contains questions from real users,
    and it requires QA systems to read and comprehend an entire Wikipedia
    article that may or may not contain the answer to the question. The
    inclusion of real user questions, and the requirement that solutions should
    read an entire page to find the answer, cause NQ to be a more realistic and
    challenging task than prior QA datasets. This version includes additional
    paragraphs (obtained using the DPR retrieval engine) to augment each
    question.

*   **Download size**: `319.22 MiB`

*   **Dataset size**: `322.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 96,676
`'validation'` | 10,693

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-natural_questions_with_dpr_para-1.0.0.html";
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
@article{kwiatkowski-etal-2019-natural,
    title = "Natural Questions: A Benchmark for Question Answering Research",
    author = "Kwiatkowski, Tom  and
      Palomaki, Jennimaria  and
      Redfield, Olivia  and
      Collins, Michael  and
      Parikh, Ankur  and
      Alberti, Chris  and
      Epstein, Danielle  and
      Polosukhin, Illia  and
      Devlin, Jacob  and
      Lee, Kenton  and
      Toutanova, Kristina  and
      Jones, Llion  and
      Kelcey, Matthew  and
      Chang, Ming-Wei  and
      Dai, Andrew M.  and
      Uszkoreit, Jakob  and
      Le, Quoc  and
      Petrov, Slav",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "7",
    year = "2019",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q19-1026",
    doi = "10.1162/tacl_a_00276",
    pages = "452--466",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/natural_questions_with_dpr_para_test

*   **Config description**: The NQ corpus contains questions from real users,
    and it requires QA systems to read and comprehend an entire Wikipedia
    article that may or may not contain the answer to the question. The
    inclusion of real user questions, and the requirement that solutions should
    read an entire page to find the answer, cause NQ to be a more realistic and
    challenging task than prior QA datasets. This version includes additional
    paragraphs (obtained using the DPR retrieval engine) to augment each
    question.

*   **Download size**: `306.94 MiB`

*   **Dataset size**: `310.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,468
`'train'` | 96,676

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-natural_questions_with_dpr_para_test-1.0.0.html";
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
@article{kwiatkowski-etal-2019-natural,
    title = "Natural Questions: A Benchmark for Question Answering Research",
    author = "Kwiatkowski, Tom  and
      Palomaki, Jennimaria  and
      Redfield, Olivia  and
      Collins, Michael  and
      Parikh, Ankur  and
      Alberti, Chris  and
      Epstein, Danielle  and
      Polosukhin, Illia  and
      Devlin, Jacob  and
      Lee, Kenton  and
      Toutanova, Kristina  and
      Jones, Llion  and
      Kelcey, Matthew  and
      Chang, Ming-Wei  and
      Dai, Andrew M.  and
      Uszkoreit, Jakob  and
      Le, Quoc  and
      Petrov, Slav",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "7",
    year = "2019",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/Q19-1026",
    doi = "10.1162/tacl_a_00276",
    pages = "452--466",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/newsqa

*   **Config description**: NewsQA is a challenging machine comprehension
    dataset of human-generated question-answer pairs. Crowdworkers supply
    questions and answers based on a set of news articles from CNN, with answers
    consisting of spans of text from the corresponding articles.

*   **Download size**: `283.33 MiB`

*   **Dataset size**: `285.94 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 75,882
`'validation'` | 4,309

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-newsqa-1.0.0.html";
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
@inproceedings{trischler-etal-2017-newsqa,
    title = "{N}ews{QA}: A Machine Comprehension Dataset",
    author = "Trischler, Adam  and
      Wang, Tong  and
      Yuan, Xingdi  and
      Harris, Justin  and
      Sordoni, Alessandro  and
      Bachman, Philip  and
      Suleman, Kaheer",
    booktitle = "Proceedings of the 2nd Workshop on Representation Learning for {NLP}",
    month = aug,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-2623",
    doi = "10.18653/v1/W17-2623",
    pages = "191--200",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/openbookqa

*   **Config description**: OpenBookQA aims to promote research in advanced
    question-answering, probing a deeper understanding of both the topic (with
    salient facts summarized as an open book, also provided with the dataset)
    and the language it is expressed in. In particular, it contains questions
    that require multi-step reasoning, use of additional common and commonsense
    knowledge, and rich text comprehension. OpenBookQA is a new kind of
    question-answering dataset modeled after open book exams for assessing human
    understanding of a subject.

*   **Download size**: `942.34 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 4,957
`'validation'` | 500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-openbookqa-1.0.0.html";
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
@inproceedings{mihaylov-etal-2018-suit,
    title = "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering",
    author = "Mihaylov, Todor  and
      Clark, Peter  and
      Khot, Tushar  and
      Sabharwal, Ashish",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1260",
    doi = "10.18653/v1/D18-1260",
    pages = "2381--2391",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/openbookqa_dev

*   **Config description**: OpenBookQA aims to promote research in advanced
    question-answering, probing a deeper understanding of both the topic (with
    salient facts summarized as an open book, also provided with the dataset)
    and the language it is expressed in. In particular, it contains questions
    that require multi-step reasoning, use of additional common and commonsense
    knowledge, and rich text comprehension. OpenBookQA is a new kind of
    question-answering dataset modeled after open book exams for assessing human
    understanding of a subject.

*   **Download size**: `942.34 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 4,957
`'validation'` | 500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-openbookqa_dev-1.0.0.html";
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
@inproceedings{mihaylov-etal-2018-suit,
    title = "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering",
    author = "Mihaylov, Todor  and
      Clark, Peter  and
      Khot, Tushar  and
      Sabharwal, Ashish",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1260",
    doi = "10.18653/v1/D18-1260",
    pages = "2381--2391",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/openbookqa_with_ir

*   **Config description**: OpenBookQA aims to promote research in advanced
    question-answering, probing a deeper understanding of both the topic (with
    salient facts summarized as an open book, also provided with the dataset)
    and the language it is expressed in. In particular, it contains questions
    that require multi-step reasoning, use of additional common and commonsense
    knowledge, and rich text comprehension. OpenBookQA is a new kind of
    question-answering dataset modeled after open book exams for assessing human
    understanding of a subject. This version includes paragraphs fetched via an
    information retrieval system as additional evidence.

*   **Download size**: `6.08 MiB`

*   **Dataset size**: `6.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 4,957
`'validation'` | 500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-openbookqa_with_ir-1.0.0.html";
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
@inproceedings{mihaylov-etal-2018-suit,
    title = "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering",
    author = "Mihaylov, Todor  and
      Clark, Peter  and
      Khot, Tushar  and
      Sabharwal, Ashish",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1260",
    doi = "10.18653/v1/D18-1260",
    pages = "2381--2391",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/openbookqa_with_ir_dev

*   **Config description**: OpenBookQA aims to promote research in advanced
    question-answering, probing a deeper understanding of both the topic (with
    salient facts summarized as an open book, also provided with the dataset)
    and the language it is expressed in. In particular, it contains questions
    that require multi-step reasoning, use of additional common and commonsense
    knowledge, and rich text comprehension. OpenBookQA is a new kind of
    question-answering dataset modeled after open book exams for assessing human
    understanding of a subject. This version includes paragraphs fetched via an
    information retrieval system as additional evidence.

*   **Download size**: `6.08 MiB`

*   **Dataset size**: `6.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 4,957
`'validation'` | 500

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-openbookqa_with_ir_dev-1.0.0.html";
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
@inproceedings{mihaylov-etal-2018-suit,
    title = "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering",
    author = "Mihaylov, Todor  and
      Clark, Peter  and
      Khot, Tushar  and
      Sabharwal, Ashish",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1260",
    doi = "10.18653/v1/D18-1260",
    pages = "2381--2391",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/physical_iqa

*   **Config description**: This is a dataset for benchmarking progress in
    physical commonsense understanding. The underlying task is multiple choice
    question answering: given a question q and two possible solutions s1, s2, a
    model or a human must choose the most appropriate solution, of which exactly
    one is correct. The dataset focuses on everyday situations with a preference
    for atypical solutions. The dataset is inspired by instructables.com, which
    provides users with instructions on how to build, craft, bake, or manipulate
    objects using everyday materials. Annotators are asked to provide semantic
    perturbations or alternative approaches which are otherwise syntactically
    and topically similar to ensure physical knowledge is targeted. The dataset
    is further cleaned of basic artifacts using the AFLite algorithm.

*   **Download size**: `6.01 MiB`

*   **Dataset size**: `6.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 16,113
`'validation'` | 1,838

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-physical_iqa-1.0.0.html";
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
@inproceedings{bisk2020piqa,
    title={Piqa: Reasoning about physical commonsense in natural language},
    author={Bisk, Yonatan and Zellers, Rowan and Gao, Jianfeng and Choi, Yejin and others},
    booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
    volume={34},
    number={05},
    pages={7432--7439},
    year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/qasc

*   **Config description**: QASC is a question-answering dataset with a focus on
    sentence composition. It consists of 8-way multiple-choice questions about
    grade school science, and comes with a corpus of 17M sentences.

*   **Download size**: `1.75 MiB`

*   **Dataset size**: `2.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-qasc-1.0.0.html";
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
@inproceedings{khot2020qasc,
    title={Qasc: A dataset for question answering via sentence composition},
    author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
    booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
    volume={34},
    number={05},
    pages={8082--8090},
    year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/qasc_test

*   **Config description**: QASC is a question-answering dataset with a focus on
    sentence composition. It consists of 8-way multiple-choice questions about
    grade school science, and comes with a corpus of 17M sentences.

*   **Download size**: `1.75 MiB`

*   **Dataset size**: `2.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-qasc_test-1.0.0.html";
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
@inproceedings{khot2020qasc,
    title={Qasc: A dataset for question answering via sentence composition},
    author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
    booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
    volume={34},
    number={05},
    pages={8082--8090},
    year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/qasc_with_ir

*   **Config description**: QASC is a question-answering dataset with a focus on
    sentence composition. It consists of 8-way multiple-choice questions about
    grade school science, and comes with a corpus of 17M sentences. This version
    includes paragraphs fetched via an information retrieval system as
    additional evidence.

*   **Download size**: `16.95 MiB`

*   **Dataset size**: `17.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-qasc_with_ir-1.0.0.html";
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
@inproceedings{khot2020qasc,
    title={Qasc: A dataset for question answering via sentence composition},
    author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
    booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
    volume={34},
    number={05},
    pages={8082--8090},
    year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/qasc_with_ir_test

*   **Config description**: QASC is a question-answering dataset with a focus on
    sentence composition. It consists of 8-way multiple-choice questions about
    grade school science, and comes with a corpus of 17M sentences. This version
    includes paragraphs fetched via an information retrieval system as
    additional evidence.

*   **Download size**: `16.95 MiB`

*   **Dataset size**: `17.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 920
`'train'`      | 8,134
`'validation'` | 926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-qasc_with_ir_test-1.0.0.html";
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
@inproceedings{khot2020qasc,
    title={Qasc: A dataset for question answering via sentence composition},
    author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
    booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
    volume={34},
    number={05},
    pages={8082--8090},
    year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/quoref

*   **Config description**: This dataset tests the coreferential reasoning
    capability of reading comprehension systems. In this span-selection
    benchmark containing questions over paragraphs from Wikipedia, a system must
    resolve hard coreferences before selecting the appropriate span(s) in the
    paragraphs for answering questions.

*   **Download size**: `51.43 MiB`

*   **Dataset size**: `52.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 22,265
`'validation'` | 2,768

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-quoref-1.0.0.html";
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
@inproceedings{dasigi-etal-2019-quoref,
    title = "{Q}uoref: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning",
    author = "Dasigi, Pradeep  and
      Liu, Nelson F.  and
      Marasovi{'c}, Ana  and
      Smith, Noah A.  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1606",
    doi = "10.18653/v1/D19-1606",
    pages = "5925--5932",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/race_string

*   **Config description**: Race is a large-scale reading comprehension dataset.
    The dataset is collected from English examinations in China, which are
    designed for middle school and high school students. The dataset can be
    served as the training and test sets for machine comprehension.

*   **Download size**: `167.97 MiB`

*   **Dataset size**: `171.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,934
`'train'`      | 87,863
`'validation'` | 4,887

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-race_string-1.0.0.html";
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
@inproceedings{lai-etal-2017-race,
    title = "{RACE}: Large-scale {R}e{A}ding Comprehension Dataset From Examinations",
    author = "Lai, Guokun  and
      Xie, Qizhe  and
      Liu, Hanxiao  and
      Yang, Yiming  and
      Hovy, Eduard",
    booktitle = "Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D17-1082",
    doi = "10.18653/v1/D17-1082",
    pages = "785--794",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/race_string_dev

*   **Config description**: Race is a large-scale reading comprehension dataset.
    The dataset is collected from English examinations in China, which are
    designed for middle school and high school students. The dataset can be
    served as the training and test sets for machine comprehension.

*   **Download size**: `167.97 MiB`

*   **Dataset size**: `171.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,934
`'train'`      | 87,863
`'validation'` | 4,887

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-race_string_dev-1.0.0.html";
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
@inproceedings{lai-etal-2017-race,
    title = "{RACE}: Large-scale {R}e{A}ding Comprehension Dataset From Examinations",
    author = "Lai, Guokun  and
      Xie, Qizhe  and
      Liu, Hanxiao  and
      Yang, Yiming  and
      Hovy, Eduard",
    booktitle = "Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D17-1082",
    doi = "10.18653/v1/D17-1082",
    pages = "785--794",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/ropes

*   **Config description**: This dataset tests a system's ability to apply
    knowledge from a passage of text to a new situation. A system is presented a
    background passage containing a causal or qualitative relation(s) (e.g.,
    "animal pollinators increase efficiency of fertilization in flowers"), a
    novel situation that uses this background, and questions that require
    reasoning about effects of the relationships in the background passage in
    the context of the situation.

*   **Download size**: `12.91 MiB`

*   **Dataset size**: `13.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 10,924
`'validation'` | 1,688

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-ropes-1.0.0.html";
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
@inproceedings{lin-etal-2019-reasoning,
    title = "Reasoning Over Paragraph Effects in Situations",
    author = "Lin, Kevin  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5808",
    doi = "10.18653/v1/D19-5808",
    pages = "58--62",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/social_iqa

*   **Config description**: This is a large-scale benchmark for commonsense
    reasoning about social situations. Social IQa contains multiple choice
    questions for probing emotional and social intelligence in a variety of
    everyday situations. Through crowdsourcing, commonsense questions along with
    correct and incorrect answers about social interactions are collected, using
    a new framework that mitigates stylistic artifacts in incorrect answers by
    asking workers to provide the right answer to a different but related
    question.

*   **Download size**: `7.08 MiB`

*   **Dataset size**: `8.22 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 33,410
`'validation'` | 1,954

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-social_iqa-1.0.0.html";
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
@inproceedings{sap-etal-2019-social,
    title = "Social {IQ}a: Commonsense Reasoning about Social Interactions",
    author = "Sap, Maarten  and
      Rashkin, Hannah  and
      Chen, Derek  and
      Le Bras, Ronan  and
      Choi, Yejin",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1454",
    doi = "10.18653/v1/D19-1454",
    pages = "4463--4473",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/squad1_1

*   **Config description**: This is a reading comprehension dataset consisting
    of questions posed by crowdworkers on a set of Wikipedia articles, where the
    answer to each question is a segment of text from the corresponding reading
    passage.

*   **Download size**: `80.62 MiB`

*   **Dataset size**: `83.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 87,514
`'validation'` | 10,570

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-squad1_1-1.0.0.html";
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
@inproceedings{rajpurkar-etal-2016-squad,
    title = "{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text",
    author = "Rajpurkar, Pranav  and
      Zhang, Jian  and
      Lopyrev, Konstantin  and
      Liang, Percy",
    booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2016",
    address = "Austin, Texas",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D16-1264",
    doi = "10.18653/v1/D16-1264",
    pages = "2383--2392",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/squad2

*   **Config description**: This dataset combines the original Stanford Question
    Answering Dataset (SQuAD) dataset with unanswerable questions written
    adversarially by crowdworkers to look similar to answerable ones.

*   **Download size**: `116.56 MiB`

*   **Dataset size**: `121.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 130,149
`'validation'` | 11,873

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-squad2-1.0.0.html";
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
@inproceedings{rajpurkar-etal-2018-know,
    title = "Know What You Don{'}t Know: Unanswerable Questions for {SQ}u{AD}",
    author = "Rajpurkar, Pranav  and
      Jia, Robin  and
      Liang, Percy",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-2124",
    doi = "10.18653/v1/P18-2124",
    pages = "784--789",
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/winogrande_l

*   **Config description**: This dataset is inspired by the original Winograd
    Schema Challenge design, but adjusted to improve both the scale and the
    hardness of the dataset. The key steps of the dataset construction consist
    of (1) a carefully designed crowdsourcing procedure, followed by (2)
    systematic bias reduction using a novel AfLite algorithm that generalizes
    human-detectable word associations to machine-detectable embedding
    associations. Training sets with differnt sizes are provided. This set
    corresponds to size `l`.

*   **Download size**: `1.49 MiB`

*   **Dataset size**: `1.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 10,234
`'validation'` | 1,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-winogrande_l-1.0.0.html";
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
@inproceedings{sakaguchi2020winogrande,
  title={Winogrande: An adversarial winograd schema challenge at scale},
  author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={34},
  number={05},
  pages={8732--8740},
  year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/winogrande_m

*   **Config description**: This dataset is inspired by the original Winograd
    Schema Challenge design, but adjusted to improve both the scale and the
    hardness of the dataset. The key steps of the dataset construction consist
    of (1) a carefully designed crowdsourcing procedure, followed by (2)
    systematic bias reduction using a novel AfLite algorithm that generalizes
    human-detectable word associations to machine-detectable embedding
    associations. Training sets with differnt sizes are provided. This set
    corresponds to size `m`.

*   **Download size**: `507.46 KiB`

*   **Dataset size**: `623.15 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 2,558
`'validation'` | 1,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-winogrande_m-1.0.0.html";
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
@inproceedings{sakaguchi2020winogrande,
  title={Winogrande: An adversarial winograd schema challenge at scale},
  author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={34},
  number={05},
  pages={8732--8740},
  year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```

## unified_qa/winogrande_s

*   **Config description**: This dataset is inspired by the original Winograd
    Schema Challenge design, but adjusted to improve both the scale and the
    hardness of the dataset. The key steps of the dataset construction consist
    of (1) a carefully designed crowdsourcing procedure, followed by (2)
    systematic bias reduction using a novel AfLite algorithm that generalizes
    human-detectable word associations to machine-detectable embedding
    associations. Training sets with differnt sizes are provided. This set
    corresponds to size `s`.

*   **Download size**: `479.24 KiB`

*   **Dataset size**: `590.47 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,767
`'train'`      | 640
`'validation'` | 1,267

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/unified_qa-winogrande_s-1.0.0.html";
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
@inproceedings{sakaguchi2020winogrande,
  title={Winogrande: An adversarial winograd schema challenge at scale},
  author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={34},
  number={05},
  pages={8732--8740},
  year={2020}
}

@inproceedings{khashabi-etal-2020-unifiedqa,
    title = "{UNIFIEDQA}: Crossing Format Boundaries with a Single {QA} System",
    author = "Khashabi, Daniel  and
      Min, Sewon  and
      Khot, Tushar  and
      Sabharwal, Ashish  and
      Tafjord, Oyvind  and
      Clark, Peter  and
      Hajishirzi, Hannaneh",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.171",
    doi = "10.18653/v1/2020.findings-emnlp.171",
    pages = "1896--1907",
}

Note that each UnifiedQA dataset has its own citation. Please see the source to
see the correct citation for each contained dataset."
```
