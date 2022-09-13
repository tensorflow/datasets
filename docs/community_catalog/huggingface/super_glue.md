# super_glue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/super_glue)
*   [Huggingface](https://huggingface.co/datasets/super_glue)


## boolq


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/boolq')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

BoolQ (Boolean Questions, Clark et al., 2019a) is a QA task where each example consists of a short
passage and a yes/no question about the passage. The questions are provided anonymously and
unsolicited by users of the Google search engine, and afterwards paired with a paragraph from a
Wikipedia article containing the answer. Following the original work, we evaluate with accuracy.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3245
`'train'` | 9427
`'validation'` | 3270

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## cb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/cb')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The CommitmentBank (De Marneffe et al., 2019) is a corpus of short texts in which at least
one sentence contains an embedded clause. Each of these embedded clauses is annotated with the
degree to which we expect that the person who wrote the text is committed to the truth of the clause.
The resulting task framed as three-class textual entailment on examples that are drawn from the Wall
Street Journal, fiction from the British National Corpus, and Switchboard. Each example consists
of a premise containing an embedded clause and the corresponding hypothesis is the extraction of
that clause. We use a subset of the data that had inter-annotator agreement above 0.85. The data is
imbalanced (relatively fewer neutral examples), so we evaluate using accuracy and F1, where for
multi-class F1 we compute the unweighted average of the F1 per class.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 250
`'train'` | 250
`'validation'` | 56

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "contradiction",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## copa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/copa')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Choice Of Plausible Alternatives (COPA, Roemmele et al., 2011) dataset is a causal
reasoning task in which a system is given a premise sentence and two possible alternatives. The
system must choose the alternative which has the more plausible causal relationship with the premise.
The method used for the construction of the alternatives ensures that the task requires causal reasoning
to solve. Examples either deal with alternative possible causes or alternative possible effects of the
premise sentence, accompanied by a simple question disambiguating between the two instance
types for the model. All examples are handcrafted and focus on topics from online blogs and a
photography-related encyclopedia. Following the recommendation of the authors, we evaluate using
accuracy.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 400
`'validation'` | 100

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "choice1",
            "choice2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## multirc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/multirc')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Multi-Sentence Reading Comprehension dataset (MultiRC, Khashabi et al., 2018)
is a true/false question-answering task. Each example consists of a context paragraph, a question
about that paragraph, and a list of possible answers to that question which must be labeled as true or
false. Question-answering (QA) is a popular problem with many datasets. We use MultiRC because
of a number of desirable properties: (i) each question can have multiple possible correct answers,
so each question-answer pair must be evaluated independent of other pairs, (ii) the questions are
designed such that answering each question requires drawing facts from multiple context sentences,
and (iii) the question-answer pair format more closely matches the API of other SuperGLUE tasks
than span-based extractive QA does. The paragraphs are drawn from seven domains including news,
fiction, and historical text.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9693
`'train'` | 27243
`'validation'` | 4848

*   **Features**:

```json
{
    "paragraph": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "paragraph": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "question": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "answer": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## record


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/record')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

(Reading Comprehension with Commonsense Reasoning Dataset, Zhang et al., 2018) is a
multiple-choice QA task. Each example consists of a news article and a Cloze-style question about
the article in which one entity is masked out. The system must predict the masked out entity from a
given list of possible entities in the provided passage, where the same entity may be expressed using
multiple different surface forms, all of which are considered correct. Articles are drawn from CNN
and Daily Mail. Following the original work, we evaluate with max (over all mentions) token-level
F1 and exact match (EM).
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 100730
`'validation'` | 10000

*   **Features**:

```json
{
    "passage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entities": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "idx": {
        "passage": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "query": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    }
}
```



## rte


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/rte')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Recognizing Textual Entailment (RTE) datasets come from a series of annual competitions
on textual entailment, the problem of predicting whether a given premise sentence entails a given
hypothesis sentence (also known as natural language inference, NLI). RTE was previously included
in GLUE, and we use the same data and format as before: We merge data from RTE1 (Dagan
et al., 2006), RTE2 (Bar Haim et al., 2006), RTE3 (Giampiccolo et al., 2007), and RTE5 (Bentivogli
et al., 2009). All datasets are combined and converted to two-class classification: entailment and
not_entailment. Of all the GLUE tasks, RTE was among those that benefited from transfer learning
the most, jumping from near random-chance performance (~56%) at the time of GLUE's launch to
85% accuracy (Liu et al., 2019c) at the time of writing. Given the eight point gap with respect to
human performance, however, the task is not yet solved by machines, and we expect the remaining
gap to be difficult to close.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 2490
`'validation'` | 277

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "entailment",
            "not_entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/wic')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Word-in-Context (WiC, Pilehvar and Camacho-Collados, 2019) dataset supports a word
sense disambiguation task cast as binary classification over sentence pairs. Given two sentences and a
polysemous (sense-ambiguous) word that appears in both sentences, the task is to determine whether
the word is used with the same sense in both sentences. Sentences are drawn from WordNet (Miller,
1995), VerbNet (Schuler, 2005), and Wiktionary. We follow the original work and evaluate using
accuracy.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1400
`'train'` | 5428
`'validation'` | 638

*   **Features**:

```json
{
    "word": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "start2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end1": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end2": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wsc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/wsc')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Winograd Schema Challenge (WSC, Levesque et al., 2012) is a reading comprehension
task in which a system must read a sentence with a pronoun and select the referent of that pronoun
from a list of choices. Given the difficulty of this task and the headroom still left, we have included
WSC in SuperGLUE and recast the dataset into its coreference form. The task is cast as a binary
classification problem, as opposed to N-multiple choice, in order to isolate the model's ability to
understand the coreference links within a sentence as opposed to various other strategies that may
come into play in multiple choice conditions. With that in mind, we create a split with 65% negative
majority class in the validation set, reflecting the distribution of the hidden test set, and 52% negative
class in the training set. The training and validation examples are drawn from the original Winograd
Schema dataset (Levesque et al., 2012), as well as those distributed by the affiliated organization
Commonsense Reasoning. The test examples are derived from fiction books and have been shared
with us by the authors of the original dataset. Previously, a version of WSC recast as NLI as included
in GLUE, known as WNLI. No substantial progress was made on WNLI, with many submissions
opting to submit only majority class predictions. WNLI was made especially difficult due to an
adversarial train/dev split: Premise sentences that appeared in the training set sometimes appeared
in the development set with a different hypothesis and a flipped label. If a system memorized the
training set without meaningfully generalizing, which was easy due to the small size of the training
set, it could perform far below chance on the development set. We remove this adversarial design
in the SuperGLUE version of WSC by ensuring that no sentences are shared between the training,
validation, and test sets.

However, the validation and test sets come from different domains, with the validation set consisting
of ambiguous examples such that changing one non-noun phrase word will change the coreference
dependencies in the sentence. The test set consists only of more straightforward examples, with a
high number of noun phrases (and thus more choices for the model), but low to no ambiguity.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 554
`'validation'` | 104

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span1_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span2_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span1_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span2_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wsc.fixed


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/wsc.fixed')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

The Winograd Schema Challenge (WSC, Levesque et al., 2012) is a reading comprehension
task in which a system must read a sentence with a pronoun and select the referent of that pronoun
from a list of choices. Given the difficulty of this task and the headroom still left, we have included
WSC in SuperGLUE and recast the dataset into its coreference form. The task is cast as a binary
classification problem, as opposed to N-multiple choice, in order to isolate the model's ability to
understand the coreference links within a sentence as opposed to various other strategies that may
come into play in multiple choice conditions. With that in mind, we create a split with 65% negative
majority class in the validation set, reflecting the distribution of the hidden test set, and 52% negative
class in the training set. The training and validation examples are drawn from the original Winograd
Schema dataset (Levesque et al., 2012), as well as those distributed by the affiliated organization
Commonsense Reasoning. The test examples are derived from fiction books and have been shared
with us by the authors of the original dataset. Previously, a version of WSC recast as NLI as included
in GLUE, known as WNLI. No substantial progress was made on WNLI, with many submissions
opting to submit only majority class predictions. WNLI was made especially difficult due to an
adversarial train/dev split: Premise sentences that appeared in the training set sometimes appeared
in the development set with a different hypothesis and a flipped label. If a system memorized the
training set without meaningfully generalizing, which was easy due to the small size of the training
set, it could perform far below chance on the development set. We remove this adversarial design
in the SuperGLUE version of WSC by ensuring that no sentences are shared between the training,
validation, and test sets.

However, the validation and test sets come from different domains, with the validation set consisting
of ambiguous examples such that changing one non-noun phrase word will change the coreference
dependencies in the sentence. The test set consists only of more straightforward examples, with a
high number of noun phrases (and thus more choices for the model), but low to no ambiguity.

This version fixes issues where the spans are not actually substrings of the text.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 554
`'validation'` | 104

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span1_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span2_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "span1_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "span2_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "False",
            "True"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## axb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/axb')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

An expert-constructed,
diagnostic dataset that automatically tests models for a broad range of linguistic, commonsense, and
world knowledge. Each example in this broad-coverage diagnostic is a sentence pair labeled with
a three-way entailment relation (entailment, neutral, or contradiction) and tagged with labels that
indicate the phenomena that characterize the relationship between the two sentences. Submissions
to the GLUE leaderboard are required to include predictions from the submission's MultiNLI
classifier on the diagnostic dataset, and analyses of the results were shown alongside the main
leaderboard. Since this broad-coverage diagnostic task has proved difficult for top models, we retain
it in SuperGLUE. However, since MultiNLI is not part of SuperGLUE, we collapse contradiction
and neutral into a single not_entailment label, and request that submissions include predictions
on the resulting set from the model used for the RTE task.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1104

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "entailment",
            "not_entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## axg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:super_glue/axg')
```

*   **Description**:

```
SuperGLUE (https://super.gluebenchmark.com/) is a new benchmark styled after
GLUE with a new set of more difficult language understanding tasks, improved
resources, and a new public leaderboard.

Winogender is designed to measure gender
bias in coreference resolution systems. We use the Diverse Natural Language Inference Collection
(DNC; Poliak et al., 2018) version that casts Winogender as a textual entailment task. Each example
consists of a premise sentence with a male or female pronoun and a hypothesis giving a possible
antecedent of the pronoun. Examples occur in minimal pairs, where the only difference between
an example and its pair is the gender of the pronoun in the premise. Performance on Winogender
is measured with both accuracy and the gender parity score: the percentage of minimal pairs for
which the predictions are the same. We note that a system can trivially obtain a perfect gender parity
score by guessing the same class for all examples, so a high gender parity score is meaningless unless
accompanied by high accuracy. As a diagnostic test of gender bias, we view the schemas as having high
positive predictive value and low negative predictive value; that is, they may demonstrate the presence
of gender bias in a system, but not prove its absence.
```

*   **License**: No known license
*   **Version**: 1.0.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 356

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "entailment",
            "not_entailment"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


