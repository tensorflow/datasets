<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mrqa" />
  <meta itemprop="description" content="The MRQA 2019 Shared Task focuses on generalization in question answering. An&#10;effective question answering system should do more than merely interpolate from&#10;the training set to answer test examples drawn from the same distribution: it&#10;should also be able to extrapolate to out-of-distribution examples — a&#10;significantly harder challenge.&#10;&#10;MRQA adapts and unifies multiple distinct question answering datasets (carefully&#10;selected subsets of existing datasets) into the same format (SQuAD format).&#10;Among them, six datasets were made available for training, and six datasets were&#10;made available for testing. Small portions of the training datasets&#10;were held-out as in-domain data that may be used for development. The testing&#10;datasets only contain out-of-domain data. This benchmark is released as part of&#10;the MRQA 2019 Shared Task.&#10;&#10;More information can be found at: `https://mrqa.github.io/2019/shared.html`.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mrqa&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mrqa" />
  <meta itemprop="sameAs" content="https://mrqa.github.io/2019/shared.html" />
  <meta itemprop="citation" content="@inproceedings{rajpurkar-etal-2016-squad,&#10;    title = &quot;{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text&quot;,&#10;    author = &quot;Rajpurkar, Pranav  and&#10;      Zhang, Jian  and&#10;      Lopyrev, Konstantin  and&#10;      Liang, Percy&quot;,&#10;    booktitle = &quot;Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = nov,&#10;    year = &quot;2016&quot;,&#10;    address = &quot;Austin, Texas&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/D16-1264&quot;,&#10;    doi = &quot;10.18653/v1/D16-1264&quot;,&#10;    pages = &quot;2383--2392&quot;,&#10;}&#10;&#10;@inproceedings{fisch-etal-2019-mrqa,&#10;    title = &quot;{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension&quot;,&#10;    author = &quot;Fisch, Adam  and&#10;      Talmor, Alon  and&#10;      Jia, Robin  and&#10;      Seo, Minjoon  and&#10;      Choi, Eunsol  and&#10;      Chen, Danqi&quot;,&#10;    booktitle = &quot;Proceedings of the 2nd Workshop on Machine Reading for Question Answering&quot;,&#10;    month = nov,&#10;    year = &quot;2019&quot;,&#10;    address = &quot;Hong Kong, China&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/D19-5801&quot;,&#10;    doi = &quot;10.18653/v1/D19-5801&quot;,&#10;    pages = &quot;1--13&quot;,&#10;}&#10;&#10;Note that each MRQA dataset has its own citation. Please see the source to see&#10;the correct citation for each contained dataset.&quot;" />
</div>

# `mrqa`


*   **Description**:

The MRQA 2019 Shared Task focuses on generalization in question answering. An
effective question answering system should do more than merely interpolate from
the training set to answer test examples drawn from the same distribution: it
should also be able to extrapolate to out-of-distribution examples — a
significantly harder challenge.

MRQA adapts and unifies multiple distinct question answering datasets (carefully
selected subsets of existing datasets) into the same format (SQuAD format).
Among them, six datasets were made available for training, and six datasets were
made available for testing. Small portions of the training datasets were
held-out as in-domain data that may be used for development. The testing
datasets only contain out-of-domain data. This benchmark is released as part of
the MRQA 2019 Shared Task.

More information can be found at: `https://mrqa.github.io/2019/shared.html`.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/mrqa-2019">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://mrqa.github.io/2019/shared.html](https://mrqa.github.io/2019/shared.html)

*   **Source code**:
    [`tfds.text.mrqa.MRQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/mrqa/mrqa.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Feature structure**:

```python
FeaturesDict({
    'answers': Sequence(string),
    'context': string,
    'context_tokens': Sequence({
        'offsets': int32,
        'tokens': string,
    }),
    'detected_answers': Sequence({
        'char_spans': Sequence({
            'end': int32,
            'start': int32,
        }),
        'text': string,
        'token_spans': Sequence({
            'end': int32,
            'start': int32,
        }),
    }),
    'qid': string,
    'question': string,
    'question_tokens': Sequence({
        'offsets': int32,
        'tokens': string,
    }),
    'subset': string,
})
```

*   **Feature documentation**:

Feature                            | Class            | Shape   | Dtype  | Description
:--------------------------------- | :--------------- | :------ | :----- | :----------
                                   | FeaturesDict     |         |        |
answers                            | Sequence(Tensor) | (None,) | string |
context                            | Tensor           |         | string |
context_tokens                     | Sequence         |         |        |
context_tokens/offsets             | Tensor           |         | int32  |
context_tokens/tokens              | Tensor           |         | string |
detected_answers                   | Sequence         |         |        |
detected_answers/char_spans        | Sequence         |         |        |
detected_answers/char_spans/end    | Tensor           |         | int32  |
detected_answers/char_spans/start  | Tensor           |         | int32  |
detected_answers/text              | Tensor           |         | string |
detected_answers/token_spans       | Sequence         |         |        |
detected_answers/token_spans/end   | Tensor           |         | int32  |
detected_answers/token_spans/start | Tensor           |         | int32  |
qid                                | Tensor           |         | string |
question                           | Tensor           |         | string |
question_tokens                    | Sequence         |         |        |
question_tokens/offsets            | Tensor           |         | int32  |
question_tokens/tokens             | Tensor           |         | string |
subset                             | Tensor           |         | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.


## mrqa/squad (default config)

*   **Config description**: The SQuAD (Stanford Question Answering Dataset)
    dataset is used as the basis for the shared task format. Crowdworkers are
    shown paragraphs from Wikipedia and are asked to write questions with
    extractive answers.

*   **Download size**: `29.66 MiB`

*   **Dataset size**: `271.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 86,588
`'validation'` | 10,507

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-squad-1.0.0.html";
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

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/news_qa

*   **Config description**: Two sets of crowdworkers ask and answer questions
    based on CNN news articles. The “questioners” see only the article’s
    headline and summary while the “answerers” see the full article. Questions
    that have no answer or are flagged in the dataset to be without annotator
    agreement are discarded.

*   **Download size**: `56.83 MiB`

*   **Dataset size**: `654.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 74,160
`'validation'` | 4,212

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-news_qa-1.0.0.html";
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
#
@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/trivia_qa

*   **Config description**: Question and answer pairs are sourced from trivia
    and quiz-league websites. The web version of TriviaQA, where the contexts
    are retrieved from the results of a Bing search query, is used.

*   **Download size**: `383.14 MiB`

*   **Dataset size**: `772.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 61,688
`'validation'` | 7,785

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-trivia_qa-1.0.0.html";
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
@inproceedings{joshi-etal-2017-triviaqa,
    title = "{T}rivia{QA}: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension",
    author = "Joshi, Mandar  and
      Choi, Eunsol  and
      Weld, Daniel  and
      Zettlemoyer, Luke",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1147",
    doi = "10.18653/v1/P17-1147",
    pages = "1601--1611",
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/search_qa

*   **Config description**: Question and answer pairs are sourced from the
    Jeopardy! TV show. The contexts are composed of retrieved snippets from a
    Google search query.

*   **Download size**: `699.86 MiB`

*   **Dataset size**: `1.38 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 117,384
`'validation'` | 16,980

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-search_qa-1.0.0.html";
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
@article{dunn2017searchqa,
    title={Searchqa: A new q\&a dataset augmented with context from a search engine},
    author={Dunn, Matthew and Sagun, Levent and Higgins, Mike and Guney, V Ugur and Cirik, Volkan and Cho, Kyunghyun},
    journal={arXiv preprint arXiv:1704.05179},
    year={2017}
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/hotpot_qa

*   **Config description**: Crowdworkers are shown two entity-linked paragraphs
    from Wikipedia and are asked to write and answer questions that require
    multi-hop reasoning to solve. In the original setting, these paragraphs are
    mixed with additional distractor paragraphs to make inference harder. Here,
    the distractor paragraphs are not included.

*   **Download size**: `111.98 MiB`

*   **Dataset size**: `272.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 72,928
`'validation'` | 5,901

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-hotpot_qa-1.0.0.html";
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
@inproceedings{yang-etal-2018-hotpotqa,
    title = "{H}otpot{QA}: A Dataset for Diverse, Explainable Multi-hop Question Answering",
    author = "Yang, Zhilin  and
      Qi, Peng  and
      Zhang, Saizheng  and
      Bengio, Yoshua  and
      Cohen, William  and
      Salakhutdinov, Ruslan  and
      Manning, Christopher D.",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1259",
    doi = "10.18653/v1/D18-1259",
    pages = "2369--2380",
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/natural_questions

*   **Config description**: Questions are collected from information-seeking
    queries to the Google search engine by real users under natural conditions.
    Answers to the questions are annotated in a retrieved Wikipedia page by
    crowdworkers. Two types of annotations are collected: 1) the HTML bounding
    box containing enough information to completely infer the answer to the
    question (Long Answer), and 2) the subspan or sub-spans within the bounding
    box that comprise the actual answer (Short Answer). Only the examples that
    have short answers are used, and the long answer is used as the context.

*   **Download size**: `121.15 MiB`

*   **Dataset size**: `339.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 104,071
`'validation'` | 12,836

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-natural_questions-1.0.0.html";
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

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/bio_asq

*   **Config description**: BioASQ, a challenge on large-scale biomedical
    semantic indexing and question answering, contains question and answer pairs
    that are created by domain experts. They are then manually linked to
    multiple related science (PubMed) articles. The full abstract of each of the
    linked articles is downloaded and used as individual contexts (e.g., a
    single question can be linked to multiple, independent articles to create
    multiple QA-context pairs). Abstracts that do not exactly contain the answer
    are discarded.

*   **Download size**: `2.54 MiB`

*   **Dataset size**: `6.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,504

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-bio_asq-1.0.0.html";
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
@article{tsatsaronis2015overview,
    title={An overview of the BIOASQ large-scale biomedical semantic indexing and question answering competition},
    author={Tsatsaronis, George and Balikas, Georgios and Malakasiotis, Prodromos and Partalas, Ioannis and Zschunke, Matthias and Alvers, Michael R and Weissenborn, Dirk and Krithara, Anastasia and Petridis, Sergios and Polychronopoulos, Dimitris and others},
    journal={BMC bioinformatics},
    volume={16},
    number={1},
    pages={1--28},
    year={2015},
    publisher={Springer}
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/drop

*   **Config description**: DROP (Discrete Reasoning Over the content of
    Paragraphs) examples were collected similarly to SQuAD, where crowdworkers
    are asked to create question-answer pairs from Wikipedia paragraphs. The
    questions focus on quantitative reasoning, and the original dataset contains
    non-extractive numeric answers as well as extractive text answers. The set
    of questions that are extractive is used.

*   **Download size**: `578.25 KiB`

*   **Dataset size**: `5.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-drop-1.0.0.html";
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

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/duo_rc

*   **Config description**: The ParaphraseRC split of the DuoRC dataset is used.
    In this setting, two different plot summaries of the same movie are
    collected—one from Wikipedia and the other from IMDb. Two different sets of
    crowdworkers ask and answer questions about the movie plot, where the
    “questioners” are shown only the Wikipedia page, and the “answerers” are
    shown only the IMDb page. Questions that are marked as unanswerable are
    discarded.

*   **Download size**: `1.14 MiB`

*   **Dataset size**: `15.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,501

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-duo_rc-1.0.0.html";
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
@inproceedings{saha-etal-2018-duorc,
    title = "{D}uo{RC}: Towards Complex Language Understanding with Paraphrased Reading Comprehension",
    author = "Saha, Amrita  and
      Aralikatte, Rahul  and
      Khapra, Mitesh M.  and
      Sankaranarayanan, Karthik",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-1156",
    doi = "10.18653/v1/P18-1156",
    pages = "1683--1693",
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/race

*   **Config description**: ReAding Comprehension Dataset From Examinations
    (RACE) is collected from English reading comprehension exams for middle and
    high school Chinese students. The high school split (which is more
    challenging) is used and also the implicit “fill in the blank” style
    questions (which are unnatural for this task) are filtered out.

*   **Download size**: `1.49 MiB`

*   **Dataset size**: `3.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-race-1.0.0.html";
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

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/relation_extraction

*   **Config description**: Given a slot-filling dataset, relations among
    entities are systematically transformed into questionanswer pairs using
    templates. For example, the educated_at(x, y) relationship between two
    entities x and y appearing in a sentence can be expressed as “Where was x
    educated at?” with answer y. Multiple templates for each type of relation
    are collected. The dataset’s zeroshot benchmark split (generalization to
    unseen relations) is used, and only the positive examples are kept.

*   **Download size**: `830.88 KiB`

*   **Dataset size**: `3.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,948

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-relation_extraction-1.0.0.html";
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
@inproceedings{levy-etal-2017-zero,
    title = "Zero-Shot Relation Extraction via Reading Comprehension",
    author = "Levy, Omer  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Zettlemoyer, Luke",
    booktitle = "Proceedings of the 21st Conference on Computational Natural Language Learning ({C}o{NLL} 2017)",
    month = aug,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/K17-1034",
    doi = "10.18653/v1/K17-1034",
    pages = "333--342",
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## mrqa/textbook_qa

*   **Config description**: TextbookQA is collected from lessons from middle
    school Life Science, Earth Science, and Physical Science textbooks.
    Questions that are accompanied with a diagram, or that are “True or False”
    questions are not included.

*   **Download size**: `1.79 MiB`

*   **Dataset size**: `14.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,503

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mrqa-textbook_qa-1.0.0.html";
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
@inproceedings{kembhavi2017you,
    title={Are you smarter than a sixth grader? textbook question answering for multimodal machine comprehension},
    author={Kembhavi, Aniruddha and Seo, Minjoon and Schwenk, Dustin and Choi, Jonghyun and Farhadi, Ali and Hajishirzi, Hannaneh},
    booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern recognition},
    pages={4999--5007},
    year={2017}
}

@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```
