<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="super_glue" />
  <meta itemprop="description" content="SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after&#10;GLUE with a new set of more difficult language understanding tasks, improved&#10;resources, and a new public leaderboard.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;super_glue&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/super_glue" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/boolean-questions" />
  <meta itemprop="citation" content="@inproceedings{clark2019boolq,&#10;  title={BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},&#10;  author={Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},&#10;  booktitle={NAACL},&#10;  year={2019}&#10;}&#10;@article{wang2019superglue,&#10;  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},&#10;  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},&#10;  journal={arXiv preprint arXiv:1905.00537},&#10;  year={2019}&#10;}&#10;&#10;Note that each SuperGLUE dataset has its own citation. Please see the source to&#10;get the correct citation for each contained dataset." />
</div>

# `super_glue`


*   **Description**:

SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/superglue">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Source code**:
    [`tfds.text.SuperGlue`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/super_glue.py)

*   **Versions**:

    *   **`1.0.2`** (default): No release notes.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.


## super_glue/boolq (default config)

*   **Config description**: BoolQ (Boolean Questions, Clark et al., 2019a) is a
    QA task where each example consists of a short passage and a yes/no question
    about the passage. The questions are provided anonymously and unsolicited by
    users of the Google search engine, and afterwards paired with a paragraph
    from a Wikipedia article containing the answer. Following the original work,
    we evaluate with accuracy.

*   **Homepage**:
    [https://github.com/google-research-datasets/boolean-questions](https://github.com/google-research-datasets/boolean-questions)

*   **Download size**: `3.93 MiB`

*   **Dataset size**: `10.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 3,245
`'train'`      | 9,427
`'validation'` | 3,270

*   **Feature structure**:

```python
FeaturesDict({
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'passage': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype  | Description
:------- | :----------- | :---- | :----- | :----------
         | FeaturesDict |       |        |
idx      | Tensor       |       | int32  |
label    | ClassLabel   |       | int64  |
passage  | Text         |       | string |
question | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-boolq-1.0.2.html";
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
@inproceedings{clark2019boolq,
  title={BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},
  author={Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},
  booktitle={NAACL},
  year={2019}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/cb

*   **Config description**: The CommitmentBank (De Marneffe et al., 2019) is a
    corpus of short texts in which at least one sentence contains an embedded
    clause. Each of these embedded clauses is annotated with the degree to which
    we expect that the person who wrote the text is committed to the truth of
    the clause. The resulting task framed as three-class textual entailment on
    examples that are drawn from the Wall Street Journal, fiction from the
    British National Corpus, and Switchboard. Each example consists of a premise
    containing an embedded clause and the corresponding hypothesis is the
    extraction of that clause. We use a subset of the data that had
    inter-annotator agreement above 0.85. The data is imbalanced (relatively
    fewer neutral examples), so we evaluate using accuracy and F1, where for
    multi-class F1 we compute the unweighted average of the F1 per class.

*   **Homepage**:
    [https://github.com/mcdm/CommitmentBank](https://github.com/mcdm/CommitmentBank)

*   **Download size**: `73.71 KiB`

*   **Dataset size**: `229.28 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 250
`'train'`      | 250
`'validation'` | 56

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=string),
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'premise': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype  | Description
:--------- | :----------- | :---- | :----- | :----------
           | FeaturesDict |       |        |
hypothesis | Text         |       | string |
idx        | Tensor       |       | int32  |
label      | ClassLabel   |       | int64  |
premise    | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-cb-1.0.2.html";
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
@article{de marneff_simons_tonhauser_2019,
  title={The CommitmentBank: Investigating projection in naturally occurring discourse},
  journal={proceedings of Sinn und Bedeutung 23},
  author={De Marneff, Marie-Catherine and Simons, Mandy and Tonhauser, Judith},
  year={2019}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/copa

*   **Config description**: The Choice Of Plausible Alternatives (COPA, Roemmele
    et al., 2011) dataset is a causal reasoning task in which a system is given
    a premise sentence and two possible alternatives. The system must choose the
    alternative which has the more plausible causal relationship with the
    premise. The method used for the construction of the alternatives ensures
    that the task requires causal reasoning to solve. Examples either deal with
    alternative possible causes or alternative possible effects of the premise
    sentence, accompanied by a simple question disambiguating between the two
    instance types for the model. All examples are handcrafted and focus on
    topics from online blogs and a photography-related encyclopedia. Following
    the recommendation of the authors, we evaluate using accuracy.

*   **Homepage**:
    [http://people.ict.usc.edu/~gordon/copa.html](http://people.ict.usc.edu/~gordon/copa.html)

*   **Download size**: `42.96 KiB`

*   **Dataset size**: `196.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 500
`'train'`      | 400
`'validation'` | 100

*   **Feature structure**:

```python
FeaturesDict({
    'choice1': Text(shape=(), dtype=string),
    'choice2': Text(shape=(), dtype=string),
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'premise': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape | Dtype  | Description
:------- | :----------- | :---- | :----- | :----------
         | FeaturesDict |       |        |
choice1  | Text         |       | string |
choice2  | Text         |       | string |
idx      | Tensor       |       | int32  |
label    | ClassLabel   |       | int64  |
premise  | Text         |       | string |
question | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-copa-1.0.2.html";
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
@inproceedings{roemmele2011choice,
  title={Choice of plausible alternatives: An evaluation of commonsense causal reasoning},
  author={Roemmele, Melissa and Bejan, Cosmin Adrian and Gordon, Andrew S},
  booktitle={2011 AAAI Spring Symposium Series},
  year={2011}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/multirc

*   **Config description**: The Multi-Sentence Reading Comprehension dataset
    (MultiRC, Khashabi et al., 2018) is a true/false question-answering task.
    Each example consists of a context paragraph, a question about that
    paragraph, and a list of possible answers to that question which must be
    labeled as true or false. Question-answering (QA) is a popular problem with
    many datasets. We use MultiRC because of a number of desirable properties:
    (i) each question can have multiple possible correct answers, so each
    question-answer pair must be evaluated independent of other pairs, (ii) the
    questions are designed such that answering each question requires drawing
    facts from multiple context sentences, and (iii) the question-answer pair
    format more closely matches the API of other SuperGLUE tasks than span-based
    extractive QA does. The paragraphs are drawn from seven domains including
    news, fiction, and historical text.

*   **Homepage**: [https://cogcomp.org/multirc/](https://cogcomp.org/multirc/)

*   **Download size**: `1.06 MiB`

*   **Dataset size**: `70.39 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,693
`'train'`      | 27,243
`'validation'` | 4,848

*   **Feature structure**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=string),
    'idx': FeaturesDict({
        'answer': int32,
        'paragraph': int32,
        'question': int32,
    }),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'paragraph': Text(shape=(), dtype=string),
    'question': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape | Dtype  | Description
:------------ | :----------- | :---- | :----- | :----------
              | FeaturesDict |       |        |
answer        | Text         |       | string |
idx           | FeaturesDict |       |        |
idx/answer    | Tensor       |       | int32  |
idx/paragraph | Tensor       |       | int32  |
idx/question  | Tensor       |       | int32  |
label         | ClassLabel   |       | int64  |
paragraph     | Text         |       | string |
question      | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-multirc-1.0.2.html";
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
@inproceedings{MultiRC2018,
    author = {Daniel Khashabi and Snigdha Chaturvedi and Michael Roth and Shyam Upadhyay and Dan Roth},
    title = {Looking Beyond the Surface:A Challenge Set for Reading Comprehension over Multiple Sentences},
    booktitle = {Proceedings of North American Chapter of the Association for Computational Linguistics (NAACL)},
    year = {2018}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/record

*   **Config description**: (Reading Comprehension with Commonsense Reasoning
    Dataset, Zhang et al., 2018) is a multiple-choice QA task. Each example
    consists of a news article and a Cloze-style question about the article in
    which one entity is masked out. The system must predict the masked out
    entity from a given list of possible entities in the provided passage, where
    the same entity may be expressed using multiple different surface forms, all
    of which are considered correct. Articles are drawn from CNN and Daily Mail.
    Following the original work, we evaluate with max (over all mentions)
    token-level F1 and exact match (EM).

*   **Homepage**:
    [https://sheng-z.github.io/ReCoRD-explorer/](https://sheng-z.github.io/ReCoRD-explorer/)

*   **Download size**: `49.36 MiB`

*   **Dataset size**: `166.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,000
`'train'`      | 100,730
`'validation'` | 10,000

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence(Text(shape=(), dtype=string)),
    'entities': Sequence(Text(shape=(), dtype=string)),
    'idx': FeaturesDict({
        'passage': int32,
        'query': int32,
    }),
    'passage': Text(shape=(), dtype=string),
    'query': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature     | Class          | Shape   | Dtype  | Description
:---------- | :------------- | :------ | :----- | :----------
            | FeaturesDict   |         |        |
answers     | Sequence(Text) | (None,) | string |
entities    | Sequence(Text) | (None,) | string |
idx         | FeaturesDict   |         |        |
idx/passage | Tensor         |         | int32  |
idx/query   | Tensor         |         | int32  |
passage     | Text           |         | string |
query       | Text           |         | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-record-1.0.2.html";
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
@article{zhang2018record,
  title={Record: Bridging the gap between human and machine commonsense reading comprehension},
  author={Zhang, Sheng and Liu, Xiaodong and Liu, Jingjing and Gao, Jianfeng and Duh, Kevin and Van Durme, Benjamin},
  journal={arXiv preprint arXiv:1810.12885},
  year={2018}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/rte

*   **Config description**: The Recognizing Textual Entailment (RTE) datasets
    come from a series of annual competitions on textual entailment, the problem
    of predicting whether a given premise sentence entails a given hypothesis
    sentence (also known as natural language inference, NLI). RTE was previously
    included in GLUE, and we use the same data and format as before: We merge
    data from RTE1 (Dagan et al., 2006), RTE2 (Bar Haim et al., 2006), RTE3
    (Giampiccolo et al., 2007), and RTE5 (Bentivogli et al., 2009). All datasets
    are combined and converted to two-class classification: entailment and
    not_entailment. Of all the GLUE tasks, RTE was among those that benefited
    from transfer learning the most, jumping from near random-chance performance
    (~56%) at the time of GLUE's launch to 85% accuracy (Liu et al., 2019c) at
    the time of writing. Given the eight point gap with respect to human
    performance, however, the task is not yet solved by machines, and we expect
    the remaining gap to be difficult to close.

*   **Homepage**:
    [https://aclweb.org/aclwiki/Recognizing_Textual_Entailment](https://aclweb.org/aclwiki/Recognizing_Textual_Entailment)

*   **Download size**: `733.32 KiB`

*   **Dataset size**: `2.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 3,000
`'train'`      | 2,490
`'validation'` | 277

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=string),
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'premise': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype  | Description
:--------- | :----------- | :---- | :----- | :----------
           | FeaturesDict |       |        |
hypothesis | Text         |       | string |
idx        | Tensor       |       | int32  |
label      | ClassLabel   |       | int64  |
premise    | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-rte-1.0.2.html";
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
@inproceedings{dagan2005pascal,
  title={The PASCAL recognising textual entailment challenge},
  author={Dagan, Ido and Glickman, Oren and Magnini, Bernardo},
  booktitle={Machine Learning Challenges Workshop},
  pages={177--190},
  year={2005},
  organization={Springer}
}
@inproceedings{bar2006second,
  title={The second pascal recognising textual entailment challenge},
  author={Bar-Haim, Roy and Dagan, Ido and Dolan, Bill and Ferro, Lisa and Giampiccolo, Danilo and Magnini, Bernardo and Szpektor, Idan},
  booktitle={Proceedings of the second PASCAL challenges workshop on recognising textual entailment},
  volume={6},
  number={1},
  pages={6--4},
  year={2006},
  organization={Venice}
}
@inproceedings{giampiccolo2007third,
  title={The third pascal recognizing textual entailment challenge},
  author={Giampiccolo, Danilo and Magnini, Bernardo and Dagan, Ido and Dolan, Bill},
  booktitle={Proceedings of the ACL-PASCAL workshop on textual entailment and paraphrasing},
  pages={1--9},
  year={2007},
  organization={Association for Computational Linguistics}
}
@inproceedings{bentivogli2009fifth,
  title={The Fifth PASCAL Recognizing Textual Entailment Challenge.},
  author={Bentivogli, Luisa and Clark, Peter and Dagan, Ido and Giampiccolo, Danilo},
  booktitle={TAC},
  year={2009}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/wic

*   **Config description**: The Word-in-Context (WiC, Pilehvar and
    Camacho-Collados, 2019) dataset supports a word sense disambiguation task
    cast as binary classification over sentence pairs. Given two sentences and a
    polysemous (sense-ambiguous) word that appears in both sentences, the task
    is to determine whether the word is used with the same sense in both
    sentences. Sentences are drawn from WordNet (Miller, 1995), VerbNet
    (Schuler, 2005), and Wiktionary. We follow the original work and evaluate
    using accuracy.

*   **Homepage**:
    [https://pilehvar.github.io/wic/](https://pilehvar.github.io/wic/)

*   **Download size**: `386.93 KiB`

*   **Dataset size**: `1.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,400
`'train'`      | 5,428
`'validation'` | 638

*   **Feature structure**:

```python
FeaturesDict({
    'end1': int32,
    'end2': int32,
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=string),
    'sentence2': Text(shape=(), dtype=string),
    'start1': int32,
    'start2': int32,
    'word': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape | Dtype  | Description
:-------- | :----------- | :---- | :----- | :----------
          | FeaturesDict |       |        |
end1      | Tensor       |       | int32  |
end2      | Tensor       |       | int32  |
idx       | Tensor       |       | int32  |
label     | ClassLabel   |       | int64  |
sentence1 | Text         |       | string |
sentence2 | Text         |       | string |
start1    | Tensor       |       | int32  |
start2    | Tensor       |       | int32  |
word      | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-wic-1.0.2.html";
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
@article{DBLP:journals/corr/abs-1808-09121,
  author={Mohammad Taher Pilehvar and os{'{e}} Camacho{-}Collados},
  title={WiC: 10, 000 Example Pairs for Evaluating Context-Sensitive Representations},
  journal={CoRR},
  volume={abs/1808.09121},
  year={2018},
  url={http://arxiv.org/abs/1808.09121},
  archivePrefix={arXiv},
  eprint={1808.09121},
  timestamp={Mon, 03 Sep 2018 13:36:40 +0200},
  biburl={https://dblp.org/rec/bib/journals/corr/abs-1808-09121},
  bibsource={dblp computer science bibliography, https://dblp.org}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/wsc

*   **Config description**: The Winograd Schema Challenge (WSC, Levesque et al.,
    2012) is a reading comprehension task in which a system must read a sentence
    with a pronoun and select the referent of that pronoun from a list of
    choices. Given the difficulty of this task and the headroom still left, we
    have included WSC in SuperGLUE and recast the dataset into its coreference
    form. The task is cast as a binary classification problem, as opposed to
    N-multiple choice, in order to isolate the model's ability to understand the
    coreference links within a sentence as opposed to various other strategies
    that may come into play in multiple choice conditions. With that in mind, we
    create a split with 65% negative majority class in the validation set,
    reflecting the distribution of the hidden test set, and 52% negative class
    in the training set. The training and validation examples are drawn from the
    original Winograd Schema dataset (Levesque et al., 2012), as well as those
    distributed by the affiliated organization Commonsense Reasoning. The test
    examples are derived from fiction books and have been shared with us by the
    authors of the original dataset. Previously, a version of WSC recast as NLI
    as included in GLUE, known as WNLI. No substantial progress was made on
    WNLI, with many submissions opting to submit only majority class
    predictions. WNLI was made especially difficult due to an adversarial
    train/dev split: Premise sentences that appeared in the training set
    sometimes appeared in the development set with a different hypothesis and a
    flipped label. If a system memorized the training set without meaningfully
    generalizing, which was easy due to the small size of the training set, it
    could perform far below chance on the development set. We remove this
    adversarial design in the SuperGLUE version of WSC by ensuring that no
    sentences are shared between the training, validation, and test sets.

However, the validation and test sets come from different domains, with the
validation set consisting of ambiguous examples such that changing one non-noun
phrase word will change the coreference dependencies in the sentence. The test
set consists only of more straightforward examples, with a high number of noun
phrases (and thus more choices for the model), but low to no ambiguity.

*   **Homepage**:
    [https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html](https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html)

*   **Download size**: `31.98 KiB`

*   **Dataset size**: `219.70 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 146
`'train'`      | 554
`'validation'` | 104

*   **Feature structure**:

```python
FeaturesDict({
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'span1_index': int32,
    'span1_text': Text(shape=(), dtype=string),
    'span2_index': int32,
    'span2_text': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape | Dtype  | Description
:---------- | :----------- | :---- | :----- | :----------
            | FeaturesDict |       |        |
idx         | Tensor       |       | int32  |
label       | ClassLabel   |       | int64  |
span1_index | Tensor       |       | int32  |
span1_text  | Text         |       | string |
span2_index | Tensor       |       | int32  |
span2_text  | Text         |       | string |
text        | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-wsc-1.0.2.html";
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
@inproceedings{levesque2012winograd,
  title={The winograd schema challenge},
  author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
  booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
  year={2012}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/wsc.fixed

*   **Config description**: The Winograd Schema Challenge (WSC, Levesque et al.,
    2012) is a reading comprehension task in which a system must read a sentence
    with a pronoun and select the referent of that pronoun from a list of
    choices. Given the difficulty of this task and the headroom still left, we
    have included WSC in SuperGLUE and recast the dataset into its coreference
    form. The task is cast as a binary classification problem, as opposed to
    N-multiple choice, in order to isolate the model's ability to understand the
    coreference links within a sentence as opposed to various other strategies
    that may come into play in multiple choice conditions. With that in mind, we
    create a split with 65% negative majority class in the validation set,
    reflecting the distribution of the hidden test set, and 52% negative class
    in the training set. The training and validation examples are drawn from the
    original Winograd Schema dataset (Levesque et al., 2012), as well as those
    distributed by the affiliated organization Commonsense Reasoning. The test
    examples are derived from fiction books and have been shared with us by the
    authors of the original dataset. Previously, a version of WSC recast as NLI
    as included in GLUE, known as WNLI. No substantial progress was made on
    WNLI, with many submissions opting to submit only majority class
    predictions. WNLI was made especially difficult due to an adversarial
    train/dev split: Premise sentences that appeared in the training set
    sometimes appeared in the development set with a different hypothesis and a
    flipped label. If a system memorized the training set without meaningfully
    generalizing, which was easy due to the small size of the training set, it
    could perform far below chance on the development set. We remove this
    adversarial design in the SuperGLUE version of WSC by ensuring that no
    sentences are shared between the training, validation, and test sets.

However, the validation and test sets come from different domains, with the
validation set consisting of ambiguous examples such that changing one non-noun
phrase word will change the coreference dependencies in the sentence. The test
set consists only of more straightforward examples, with a high number of noun
phrases (and thus more choices for the model), but low to no ambiguity.

This version fixes issues where the spans are not actually substrings of the
text.

*   **Homepage**:
    [https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html](https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html)

*   **Download size**: `31.98 KiB`

*   **Dataset size**: `219.70 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 146
`'train'`      | 554
`'validation'` | 104

*   **Feature structure**:

```python
FeaturesDict({
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'span1_index': int32,
    'span1_text': Text(shape=(), dtype=string),
    'span2_index': int32,
    'span2_text': Text(shape=(), dtype=string),
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape | Dtype  | Description
:---------- | :----------- | :---- | :----- | :----------
            | FeaturesDict |       |        |
idx         | Tensor       |       | int32  |
label       | ClassLabel   |       | int64  |
span1_index | Tensor       |       | int32  |
span1_text  | Text         |       | string |
span2_index | Tensor       |       | int32  |
span2_text  | Text         |       | string |
text        | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-wsc.fixed-1.0.2.html";
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
@inproceedings{levesque2012winograd,
  title={The winograd schema challenge},
  author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
  booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
  year={2012}
}
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/axb

*   **Config description**: An expert-constructed, diagnostic dataset that
    automatically tests models for a broad range of linguistic, commonsense, and
    world knowledge. Each example in this broad-coverage diagnostic is a
    sentence pair labeled with a three-way entailment relation (entailment,
    neutral, or contradiction) and tagged with labels that indicate the
    phenomena that characterize the relationship between the two sentences.
    Submissions to the GLUE leaderboard are required to include predictions from
    the submission's MultiNLI classifier on the diagnostic dataset, and analyses
    of the results were shown alongside the main leaderboard. Since this
    broad-coverage diagnostic task has proved difficult for top models, we
    retain it in SuperGLUE. However, since MultiNLI is not part of SuperGLUE, we
    collapse contradiction and neutral into a single not_entailment label, and
    request that submissions include predictions on the resulting set from the
    model used for the RTE task.

*   **Homepage**:
    [https://gluebenchmark.com/diagnostics](https://gluebenchmark.com/diagnostics)

*   **Download size**: `33.15 KiB`

*   **Dataset size**: `290.53 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,104

*   **Feature structure**:

```python
FeaturesDict({
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=string),
    'sentence2': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape | Dtype  | Description
:-------- | :----------- | :---- | :----- | :----------
          | FeaturesDict |       |        |
idx       | Tensor       |       | int32  |
label     | ClassLabel   |       | int64  |
sentence1 | Text         |       | string |
sentence2 | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-axb-1.0.2.html";
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
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```

## super_glue/axg

*   **Config description**: Winogender is designed to measure gender bias in
    coreference resolution systems. We use the Diverse Natural Language
    Inference Collection (DNC; Poliak et al., 2018) version that casts
    Winogender as a textual entailment task. Each example consists of a premise
    sentence with a male or female pronoun and a hypothesis giving a possible
    antecedent of the pronoun. Examples occur in minimal pairs, where the only
    difference between an example and its pair is the gender of the pronoun in
    the premise. Performance on Winogender is measured with both accuracy and
    the gender parity score: the percentage of minimal pairs for which the
    predictions are the same. We note that a system can trivially obtain a
    perfect gender parity score by guessing the same class for all examples, so
    a high gender parity score is meaningless unless accompanied by high
    accuracy. As a diagnostic test of gender bias, we view the schemas as having
    high positive predictive value and low negative predictive value; that is,
    they may demonstrate the presence of gender bias in a system, but not prove
    its absence.

*   **Homepage**:
    [https://github.com/rudinger/winogender-schemas](https://github.com/rudinger/winogender-schemas)

*   **Download size**: `10.17 KiB`

*   **Dataset size**: `69.75 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 356

*   **Feature structure**:

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=string),
    'idx': int32,
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'premise': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype  | Description
:--------- | :----------- | :---- | :----- | :----------
           | FeaturesDict |       |        |
hypothesis | Text         |       | string |
idx        | Tensor       |       | int32  |
label      | ClassLabel   |       | int64  |
premise    | Text         |       | string |

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/super_glue-axg-1.0.2.html";
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
@inproceedings{rudinger-EtAl:2018:N18,
  author    = {Rudinger, Rachel  and  Naradowsky, Jason  and  Leonard, Brian  and  {Van Durme}, Benjamin},
  title     = {Gender Bias in Coreference Resolution},
  booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2018},
  address   = {New Orleans, Louisiana},
  publisher = {Association for Computational Linguistics}
}

@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
```
