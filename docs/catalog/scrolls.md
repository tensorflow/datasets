<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scrolls" />
  <meta itemprop="description" content="SCROLLS: Standardized CompaRison Over Long Language Sequences.&#10;A suite of natural language tfds.core.that require reasoning over long texts.&#10;https://scrolls-benchmark.com/&#10;summ_screen_fd subset&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;scrolls&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scrolls" />
  <meta itemprop="sameAs" content="https://github.com/mingdachen/SummScreen" />
  <meta itemprop="citation" content="@misc{chen2021summscreen,&#10;      title={SummScreen: A Dataset for Abstractive Screenplay Summarization},&#10;      author={Mingda Chen and Zewei Chu and Sam Wiseman and Kevin Gimpel},&#10;      year={2021},&#10;      eprint={2104.07091},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}&#10;&#10;@misc{shaham2022scrolls,&#10;      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},&#10;      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},&#10;      year={2022},&#10;      eprint={2201.03533},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.CL}&#10;}&#10;Note that each SCROLLS dataset has its own citation. Please see the source to&#10;get the correct citation for each contained dataset." />
</div>

# `scrolls`


*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/scrolls">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Source code**:
    [`tfds.text.scrolls.Scrolls`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/scrolls/scrolls.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=string),
    'input': Text(shape=(), dtype=string),
    'output': Text(shape=(), dtype=string),
    'pid': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature | Class        | Shape | Dtype  | Description
:------ | :----------- | :---- | :----- | :----------
        | FeaturesDict |       |        |
id      | Text         |       | string |
input   | Text         |       | string |
output  | Text         |       | string |
pid     | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('input', 'output')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.


## scrolls/summ_screen_fd (default config)

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ summ_screen_fd subset

*   **Config description**: summ_screen_fd subset

*   **Homepage**:
    [https://github.com/mingdachen/SummScreen](https://github.com/mingdachen/SummScreen)

*   **Download size**: `48.67 MiB`

*   **Dataset size**: `132.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 337
`'train'`      | 3,673
`'validation'` | 338

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-summ_screen_fd-1.0.0.html";
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
@misc{chen2021summscreen,
      title={SummScreen: A Dataset for Abstractive Screenplay Summarization},
      author={Mingda Chen and Zewei Chu and Sam Wiseman and Kevin Gimpel},
      year={2021},
      eprint={2104.07091},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/qasper

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ qasper subset

*   **Config description**: qasper subset

*   **Homepage**:
    [https://allenai.org/project/qasper](https://allenai.org/project/qasper)

*   **Download size**: `19.20 MiB`

*   **Dataset size**: `131.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,399
`'train'`      | 2,567
`'validation'` | 1,726

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-qasper-1.0.0.html";
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
@inproceedings{dasigi-etal-2021-dataset,
    title = "A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers",
    author = "Dasigi, Pradeep  and
      Lo, Kyle  and
      Beltagy, Iz  and
      Cohan, Arman  and
      Smith, Noah A.  and
      Gardner, Matt",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.365",
    doi = "10.18653/v1/2021.naacl-main.365",
    pages = "4599--4610",
    abstract = "Readers of academic research papers often read with the goal of answering specific questions. Question Answering systems that can answer those questions can make consumption of the content much more efficient. However, building such tools requires data that reflect the difficulty of the task arising from complex reasoning about claims made in multiple parts of a paper. In contrast, existing information-seeking question answering tfds.core.usually contain questions about generic factoid-type information. We therefore present Qasper, a dataset of 5049 questions over 1585 Natural Language Processing papers. Each question is written by an NLP practitioner who read only the title and abstract of the corresponding paper, and the question seeks information present in the full text. The questions are then answered by a separate set of NLP practitioners who also provide supporting evidence to answers. We find that existing models that do well on other QA tasks do not perform well on answering these questions, underperforming humans by at least 27 F1 points when answering them from entire papers, motivating further research in document-grounded, information-seeking QA, which our dataset is designed to facilitate.",
}

@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/qmsum

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ qmsum subset

*   **Config description**: qmsum subset

*   **Homepage**:
    [https://github.com/Yale-LILY/QMSum](https://github.com/Yale-LILY/QMSum)

*   **Download size**: `26.02 MiB`

*   **Dataset size**: `97.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 281
`'train'`      | 1,257
`'validation'` | 272

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-qmsum-1.0.0.html";
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
@inproceedings{zhong-etal-2021-qmsum,
    title = "{QMS}um: A New Benchmark for Query-based Multi-domain Meeting Summarization",
    author = "Zhong, Ming  and
      Yin, Da  and
      Yu, Tao  and
      Zaidi, Ahmad  and
      Mutuma, Mutethia  and
      Jha, Rahul  and
      Awadallah, Ahmed Hassan  and
      Celikyilmaz, Asli  and
      Liu, Yang  and
      Qiu, Xipeng  and
      Radev, Dragomir",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.472",
    doi = "10.18653/v1/2021.naacl-main.472",
    pages = "5905--5921",
    abstract = "Meetings are a key component of human collaboration. As increasing numbers of meetings are recorded and transcribed, meeting summaries have become essential to remind those who may or may not have attended the meetings about the key decisions made and the tasks to be completed. However, it is hard to create a single short summary that covers all the content of a long meeting involving multiple people and topics. In order to satisfy the needs of different types of users, we define a new query-based multi-domain meeting summarization task, where models have to select and summarize relevant spans of meetings in response to a query, and we introduce QMSum, a new benchmark for this task. QMSum consists of 1,808 query-summary pairs over 232 meetings in multiple domains. Besides, we investigate a locate-then-summarize method and evaluate a set of strong summarization baselines on the task. Experimental results and manual analysis reveal that QMSum presents significant challenges in long meeting summarization for future research. Dataset is available at \url{https://github.com/Yale-LILY/QMSum}.",
}

@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/narrative_qa

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ narrative_qa subset

*   **Config description**: narrative_qa subset

*   **Homepage**:
    [https://deepmind.com/research/publications/narrativeqa-reading-comprehension-challenge](https://deepmind.com/research/publications/narrativeqa-reading-comprehension-challenge)

*   **Download size**: `7.50 GiB`

*   **Dataset size**: `21.56 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,306
`'train'`      | 55,003
`'validation'` | 5,878

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-narrative_qa-1.0.0.html";
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
@article{kovcisky2018narrativeqa,
  title={The narrativeqa reading comprehension challenge},
  author={Ko{\v{c}}isk{\'y}, Tom{\'a}{\v{s}} and Schwarz, Jonathan and Blunsom, Phil and Dyer, Chris and Hermann, Karl Moritz and Melis, G{\'a}bor and Grefenstette, Edward},
  journal={Transactions of the Association for Computational Linguistics},
  volume={6},
  pages={317--328},
  year={2018},
  publisher={MIT Press}
}

@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/gov_report

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ gov_report subset

*   **Config description**: gov_report subset

*   **Homepage**:
    [https://gov-report-data.github.io/](https://gov-report-data.github.io/)

*   **Download size**: `301.58 MiB`

*   **Dataset size**: `1.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 973
`'train'`      | 17,457
`'validation'` | 972

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-gov_report-1.0.0.html";
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
@inproceedings{huang-etal-2021-efficient,
    title = "Efficient Attentions for Long Document Summarization",
    author = "Huang, Luyang  and
      Cao, Shuyang  and
      Parulian, Nikolaus  and
      Ji, Heng  and
      Wang, Lu",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.112",
    doi = "10.18653/v1/2021.naacl-main.112",
    pages = "1419--1436",
    abstract = "The quadratic computational and memory complexities of large Transformers have limited their scalability for long document summarization. In this paper, we propose Hepos, a novel efficient encoder-decoder attention with head-wise positional strides to effectively pinpoint salient information from the source. We further conduct a systematic study of existing efficient self-attentions. Combined with Hepos, we are able to process ten times more tokens than existing models that use full attentions. For evaluation, we present a new dataset, GovReport, with significantly longer documents and summaries. Results show that our models produce significantly higher ROUGE scores than competitive comparisons, including new state-of-the-art results on PubMed. Human evaluation also shows that our models generate more informative summaries with fewer unfaithful errors.",
}

@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/contract_nli

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ contract_nli subset

*   **Config description**: contract_nli subset

*   **Homepage**:
    [https://stanfordnlp.github.io/contract-nli/](https://stanfordnlp.github.io/contract-nli/)

*   **Download size**: `4.64 MiB`

*   **Dataset size**: `112.56 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,091
`'train'`      | 7,191
`'validation'` | 1,037

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-contract_nli-1.0.0.html";
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
@inproceedings{koreeda-manning-2021-contractnli,
    title = "ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts",
    author = "Koreeda, Yuta  and
      Manning, Christopher D.",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    year = "2021",
    publisher = "Association for Computational Linguistics"
}


@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## scrolls/quality

*   **Description**:

SCROLLS: Standardized CompaRison Over Long Language Sequences. A suite of
natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/ quality subset

*   **Config description**: quality subset

*   **Homepage**:
    [https://github.com/nyu-mll/quality](https://github.com/nyu-mll/quality)

*   **Download size**: `29.80 MiB`

*   **Dataset size**: `163.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,128
`'train'`      | 2,523
`'validation'` | 2,086

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/scrolls-quality-1.0.0.html";
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
@article{pang2021quality,
  title={{QuALITY}: Question Answering with Long Input Texts, Yes!},
  author={Pang, Richard Yuanzhe and Parrish, Alicia and Joshi, Nitish and Nangia, Nikita and Phang, Jason and Chen, Angelica and Padmakumar, Vishakh and Ma, Johnny and Thompson, Jana and He, He and Bowman, Samuel R.},
  journal={arXiv preprint arXiv:2112.08608},
  year={2021}
}


@misc{shaham2022scrolls,
      title={SCROLLS: Standardized CompaRison Over Long Language Sequences},
      author={Uri Shaham and Elad Segal and Maor Ivgi and Avia Efrat and Ori Yoran and Adi Haviv and Ankit Gupta and Wenhan Xiong and Mor Geva and Jonathan Berant and Omer Levy},
      year={2022},
      eprint={2201.03533},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
Note that each SCROLLS dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```
