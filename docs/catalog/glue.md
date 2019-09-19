<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="glue" />
  <meta itemprop="description" content="The Corpus of Linguistic Acceptability consists of English&#10;            acceptability judgments drawn from books and journal articles on&#10;            linguistic theory. Each example is a sequence of words annotated&#10;            with whether it is a grammatical English sentence." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/glue" />
  <meta itemprop="sameAs" content="https://nyu-mll.github.io/CoLA/" />
</div>

# `glue`

*   URL: [https://nyu-mll.github.io/CoLA/](https://nyu-mll.github.io/CoLA/)
*   `DatasetBuilder`:
    [`tfds.text.glue.Glue`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/glue.py)

`glue` is configured with `tfds.text.glue.GlueConfig` and has the following
configurations predefined (defaults to the first one):

*   `cola` (`v0.0.2`) (`Size: 368.14 KiB`): The Corpus of Linguistic
    Acceptability consists of English acceptability judgments drawn from books
    and journal articles on linguistic theory. Each example is a sequence of
    words annotated with whether it is a grammatical English sentence.

*   `sst2` (`v0.0.2`) (`Size: 7.09 MiB`): The Stanford Sentiment Treebank
    consists of sentences from movie reviews and human annotations of their
    sentiment. The task is to predict the sentiment of a given sentence. We use
    the two-way (positive/negative) class split, and use only sentence-level
    labels.

*   `mrpc` (`v0.0.2`) (`Size: 1.43 MiB`): The Microsoft Research Paraphrase
    Corpus (Dolan & Brockett, 2005) is a corpus of sentence pairs automatically
    extracted from online news sources, with human annotations for whether the
    sentences in the pair are semantically equivalent.

*   `qqp` (`v0.0.2`) (`Size: 57.73 MiB`): The Quora Question Pairs2 dataset is a
    collection of question pairs from the community question-answering website
    Quora. The task is to determine whether a pair of questions are semantically
    equivalent.

*   `stsb` (`v0.0.2`) (`Size: 784.05 KiB`): The Semantic Textual Similarity
    Benchmark (Cer et al., 2017) is a collection of sentence pairs drawn from
    news headlines, video and image captions, and natural language inference
    data. Each pair is human-annotated with a similarity score from 1 to 5.

*   `mnli` (`v0.0.2`) (`Size: 298.29 MiB`): The Multi-Genre Natural Language
    Inference Corpusn is a crowdsourced collection of sentence pairs with
    textual entailment annotations. Given a premise sentence and a hypothesis
    sentence, the task is to predict whether the premise entails the hypothesis
    (entailment), contradicts the hypothesis (contradiction), or neither
    (neutral). The premise sentences are gathered from ten different sources,
    including transcribed speech, fiction, and government reports. We use the
    standard test set, for which we obtained private labels from the authors,
    and evaluate on both the matched (in-domain) and mismatched (cross-domain)
    section. We also use and recommend the SNLI corpus as 550k examples of
    auxiliary training data.

*   `mnli_mismatched` (`v0.0.2`) (`Size: 298.29 MiB`): The mismatched validation
    and test splits from MNLI. See the "mnli" BuilderConfig for additional
    information.

*   `mnli_matched` (`v0.0.2`) (`Size: 298.29 MiB`): The matched validation and
    test splits from MNLI. See the "mnli" BuilderConfig for additional
    information.

*   `qnli` (`v0.0.2`) (`Size: 10.14 MiB`): The Stanford Question Answering
    Dataset is a question-answering dataset consisting of question-paragraph
    pairs, where one of the sentences in the paragraph (drawn from Wikipedia)
    contains the answer to the corresponding question (written by an annotator).
    We convert the task into sentence pair classification by forming a pair
    between each question and each sentence in the corresponding context, and
    filtering out pairs with low lexical overlap between the question and the
    context sentence. The task is to determine whether the context sentence
    contains the answer to the question. This modified version of the original
    task removes the requirement that the model select the exact answer, but
    also removes the simplifying assumptions that the answer is always present
    in the input and that lexical overlap is a reliable cue.

*   `rte` (`v0.0.2`) (`Size: 680.81 KiB`): The Recognizing Textual Entailment
    (RTE) datasets come from a series of annual textual entailment challenges.
    We combine the data from RTE1 (Dagan et al., 2006), RTE2 (Bar Haim et al.,
    2006), RTE3 (Giampiccolo et al., 2007), and RTE5 (Bentivogli et al., 2009).4
    Examples are constructed based on news and Wikipedia text. We convert all
    datasets to a two-class split, where for three-class datasets we collapse
    neutral and contradiction into not entailment, for consistency.

*   `wnli` (`v0.0.2`) (`Size: 28.32 KiB`): The Winograd Schema Challenge
    (Levesque et al., 2011) is a reading comprehension task in which a system
    must read a sentence with a pronoun and select the referent of that pronoun
    from a list of choices. The examples are manually constructed to foil simple
    statistical methods: Each one is contingent on contextual information
    provided by a single word or phrase in the sentence. To convert the problem
    into sentence pair classification, we construct sentence pairs by replacing
    the ambiguous pronoun with each possible referent. The task is to predict if
    the sentence with the pronoun substituted is entailed by the original
    sentence. We use a small evaluation set consisting of new examples derived
    from fiction books that was shared privately by the authors of the original
    corpus. While the included training set is balanced between two classes, the
    test set is imbalanced between them (65% not entailment). Also, due to a
    data quirk, the development set is adversarial: hypotheses are sometimes
    shared between training and development examples, so if a model memorizes
    the training examples, they will predict the wrong label on corresponding
    development set example. As with QNLI, each example is evaluated separately,
    so there is not a systematic correspondence between a model's score on this
    task and its score on the unconverted original task. We call converted
    dataset WNLI (Winograd NLI).

## `glue/cola`

The Corpus of Linguistic Acceptability consists of English acceptability
judgments drawn from books and journal articles on linguistic theory. Each
example is a sequence of words annotated with whether it is a grammatical
English sentence.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 10,657
TRAIN      | 8,551
TEST       | 1,063
VALIDATION | 1,043

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://nyu-mll.github.io/CoLA/](https://nyu-mll.github.io/CoLA/)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/sst2`

The Stanford Sentiment Treebank consists of sentences from movie reviews and
human annotations of their sentiment. The task is to predict the sentiment of a
given sentence. We use the two-way (positive/negative) class split, and use only
sentence-level labels.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 70,042
TRAIN      | 67,349
TEST       | 1,821
VALIDATION | 872

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://nlp.stanford.edu/sentiment/index.html](https://nlp.stanford.edu/sentiment/index.html)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/mrpc`

The Microsoft Research Paraphrase Corpus (Dolan & Brockett, 2005) is a corpus of
sentence pairs automatically extracted from online news sources, with human
annotations for whether the sentences in the pair are semantically equivalent.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,801
TRAIN      | 3,668
TEST       | 1,725
VALIDATION | 408

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://www.microsoft.com/en-us/download/details.aspx?id=52398](https://www.microsoft.com/en-us/download/details.aspx?id=52398)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/qqp`

The Quora Question Pairs2 dataset is a collection of question pairs from the
community question-answering website Quora. The task is to determine whether a
pair of questions are semantically equivalent.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 795,244
TEST       | 390,965
TRAIN      | 363,849
VALIDATION | 40,430

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'question1': Text(shape=(), dtype=tf.string),
    'question2': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/stsb`

The Semantic Textual Similarity Benchmark (Cer et al., 2017) is a collection of
sentence pairs drawn from news headlines, video and image captions, and natural
language inference data. Each pair is human-annotated with a similarity score
from 1 to 5.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 8,628
TRAIN      | 5,749
VALIDATION | 1,500
TEST       | 1,379

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': Tensor(shape=(), dtype=tf.float32),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/mnli`

The Multi-Genre Natural Language Inference Corpusn is a crowdsourced collection
of sentence pairs with textual entailment annotations. Given a premise sentence
and a hypothesis sentence, the task is to predict whether the premise entails
the hypothesis (entailment), contradicts the hypothesis (contradiction), or
neither (neutral). The premise sentences are gathered from ten different
sources, including transcribed speech, fiction, and government reports. We use
the standard test set, for which we obtained private labels from the authors,
and evaluate on both the matched (in-domain) and mismatched (cross-domain)
section. We also use and recommend the SNLI corpus as 550k examples of auxiliary
training data.

### Statistics

Split                 | Examples
:-------------------- | -------:
ALL                   | 431,992
TRAIN                 | 392,702
TEST_MISMATCHED       | 9,847
VALIDATION_MISMATCHED | 9,832
VALIDATION_MATCHED    | 9,815
TEST_MATCHED          | 9,796

### Features

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.nyu.edu/projects/bowman/multinli/](http://www.nyu.edu/projects/bowman/multinli/)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/mnli_mismatched`

The mismatched validation and test splits from MNLI. See the "mnli"
BuilderConfig for additional information.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 19,679
TEST       | 9,847
VALIDATION | 9,832

### Features

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.nyu.edu/projects/bowman/multinli/](http://www.nyu.edu/projects/bowman/multinli/)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/mnli_matched`

The matched validation and test splits from MNLI. See the "mnli" BuilderConfig
for additional information.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 19,611
VALIDATION | 9,815
TEST       | 9,796

### Features

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [http://www.nyu.edu/projects/bowman/multinli/](http://www.nyu.edu/projects/bowman/multinli/)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/qnli`

The Stanford Question Answering Dataset is a question-answering dataset
consisting of question-paragraph pairs, where one of the sentences in the
paragraph (drawn from Wikipedia) contains the answer to the corresponding
question (written by an annotator). We convert the task into sentence pair
classification by forming a pair between each question and each sentence in the
corresponding context, and filtering out pairs with low lexical overlap between
the question and the context sentence. The task is to determine whether the
context sentence contains the answer to the question. This modified version of
the original task removes the requirement that the model select the exact
answer, but also removes the simplifying assumptions that the answer is always
present in the input and that lexical overlap is a reliable cue.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 115,669
TRAIN      | 104,743
TEST       | 5,463
VALIDATION | 5,463

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'question': Text(shape=(), dtype=tf.string),
    'sentence': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/rte`

The Recognizing Textual Entailment (RTE) datasets come from a series of annual
textual entailment challenges. We combine the data from RTE1 (Dagan et al.,
2006), RTE2 (Bar Haim et al., 2006), RTE3 (Giampiccolo et al., 2007), and RTE5
(Bentivogli et al., 2009).4 Examples are constructed based on news and Wikipedia
text. We convert all datasets to a two-class split, where for three-class
datasets we collapse neutral and contradiction into not entailment, for
consistency.

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 5,767
TEST       | 3,000
TRAIN      | 2,490
VALIDATION | 277

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://aclweb.org/aclwiki/Recognizing_Textual_Entailment](https://aclweb.org/aclwiki/Recognizing_Textual_Entailment)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## `glue/wnli`

The Winograd Schema Challenge (Levesque et al., 2011) is a reading comprehension
task in which a system must read a sentence with a pronoun and select the
referent of that pronoun from a list of choices. The examples are manually
constructed to foil simple statistical methods: Each one is contingent on
contextual information provided by a single word or phrase in the sentence. To
convert the problem into sentence pair classification, we construct sentence
pairs by replacing the ambiguous pronoun with each possible referent. The task
is to predict if the sentence with the pronoun substituted is entailed by the
original sentence. We use a small evaluation set consisting of new examples
derived from fiction books that was shared privately by the authors of the
original corpus. While the included training set is balanced between two
classes, the test set is imbalanced between them (65% not entailment). Also, due
to a data quirk, the development set is adversarial: hypotheses are sometimes
shared between training and development examples, so if a model memorizes the
training examples, they will predict the wrong label on corresponding
development set example. As with QNLI, each example is evaluated separately, so
there is not a systematic correspondence between a model's score on this task
and its score on the unconverted original task. We call converted dataset WNLI
(Winograd NLI).

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 852
TRAIN      | 635
TEST       | 146
VALIDATION | 71

### Features

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html](https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html)
*   [https://gluebenchmark.com/](https://gluebenchmark.com/)

## Citation
```
@inproceedings{levesque2012winograd,
              title={The winograd schema challenge},
              author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
              booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
              year={2012}
            }
@inproceedings{wang2019glue,
  title={{GLUE}: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding},
  author={Wang, Alex and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R.},
  note={In the Proceedings of ICLR.},
  year={2019}
}

Note that each GLUE dataset has its own citation. Please see the source to see
the correct citation for each contained dataset.
```

--------------------------------------------------------------------------------
