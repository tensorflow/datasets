<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="super_glue" />
  <meta itemprop="description" content="The Winograd Schema Challenge (WSC, Levesque et al., 2012) is a reading comprehension&#10;task in which a system must read a sentence with a pronoun and select the referent of that pronoun&#10;from a list of choices. Given the difficulty of this task and the headroom still left, we have included&#10;WSC in SuperGLUE and recast the dataset into its coreference form. The task is cast as a binary&#10;classification problem, as opposed to N-multiple choice, in order to isolate the model's ability to&#10;understand the coreference links within a sentence as opposed to various other strategies that may&#10;come into play in multiple choice conditions. With that in mind, we create a split with 65% negative&#10;majority class in the validation set, reflecting the distribution of the hidden test set, and 52% negative&#10;class in the training set. The training and validation examples are drawn from the original Winograd&#10;Schema dataset (Levesque et al., 2012), as well as those distributed by the affiliated organization&#10;Commonsense Reasoning. The test examples are derived from fiction books and have been shared&#10;with us by the authors of the original dataset. Previously, a version of WSC recast as NLI as included&#10;in GLUE, known as WNLI. No substantial progress was made on WNLI, with many submissions&#10;opting to submit only majority class predictions. WNLI was made especially difficult due to an&#10;adversarial train/dev split: Premise sentences that appeared in the training set sometimes appeared&#10;in the development set with a different hypothesis and a flipped label. If a system memorized the&#10;training set without meaningfully generalizing, which was easy due to the small size of the training&#10;set, it could perform far below chance on the development set. We remove this adversarial design&#10;in the SuperGLUE version of WSC by ensuring that no sentences are shared between the training,&#10;validation, and test sets.&#10;&#10;However, the validation and test sets come from different domains, with the validation set consisting&#10;of ambiguous examples such that changing one non-noun phrase word will change the coreference&#10;dependencies in the sentence. The test set consists only of more straightforward examples, with a&#10;high number of noun phrases (and thus more choices for the model), but low to no ambiguity.&#10;&#10;This version fixes issues where the spans are not actually substrings of the text." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/super_glue" />
  <meta itemprop="sameAs" content="https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html" />
</div>

# `super_glue`

The Winograd Schema Challenge (WSC, Levesque et al., 2012) is a reading
comprehension task in which a system must read a sentence with a pronoun and
select the referent of that pronoun from a list of choices. Given the difficulty
of this task and the headroom still left, we have included WSC in SuperGLUE and
recast the dataset into its coreference form. The task is cast as a binary
classification problem, as opposed to N-multiple choice, in order to isolate the
model's ability to understand the coreference links within a sentence as opposed
to various other strategies that may come into play in multiple choice
conditions. With that in mind, we create a split with 65% negative majority
class in the validation set, reflecting the distribution of the hidden test set,
and 52% negative class in the training set. The training and validation examples
are drawn from the original Winograd Schema dataset (Levesque et al., 2012), as
well as those distributed by the affiliated organization Commonsense Reasoning.
The test examples are derived from fiction books and have been shared with us by
the authors of the original dataset. Previously, a version of WSC recast as NLI
as included in GLUE, known as WNLI. No substantial progress was made on WNLI,
with many submissions opting to submit only majority class predictions. WNLI was
made especially difficult due to an adversarial train/dev split: Premise
sentences that appeared in the training set sometimes appeared in the
development set with a different hypothesis and a flipped label. If a system
memorized the training set without meaningfully generalizing, which was easy due
to the small size of the training set, it could perform far below chance on the
development set. We remove this adversarial design in the SuperGLUE version of
WSC by ensuring that no sentences are shared between the training, validation,
and test sets.

However, the validation and test sets come from different domains, with the
validation set consisting of ambiguous examples such that changing one non-noun
phrase word will change the coreference dependencies in the sentence. The test
set consists only of more straightforward examples, with a high number of noun
phrases (and thus more choices for the model), but low to no ambiguity.

This version fixes issues where the spans are not actually substrings of the
text.

*   URL:
    [https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html](https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html)
*   `DatasetBuilder`:
    [`tfds.text.super_glue.SuperGlue`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/super_glue.py)

`super_glue` is configured with `tfds.text.super_glue.SuperGlueConfig` and has
the following configurations predefined (defaults to the first one):

*   `cb` (`v0.0.2`) (`Size: 73.56 KiB`): The CommitmentBank (De Marneffe et al.,
    2019) is a corpus of short texts in which at least one sentence contains an
    embedded clause. Each of these embedded clauses is annotated with the degree
    to which we expect that the person who wrote the text is committed to the
    truth of the clause. The resulting task framed as three-class textual
    entailment on examples that are drawn from the Wall Street Journal, fiction
    from the British National Corpus, and Switchboard. Each example consists of
    a premise containing an embedded clause and the corresponding hypothesis is
    the extraction of that clause. We use a subset of the data that had
    inter-annotator agreement above 0.85. The data is imbalanced (relatively
    fewer neutral examples), so we evaluate using accuracy and F1, where for
    multi-class F1 we compute the unweighted average of the F1 per class.

*   `copa` (`v0.0.2`) (`Size: 42.79 KiB`): The Choice Of Plausible Alternatives
    (COPA, Roemmele et al., 2011) dataset is a causal reasoning task in which a
    system is given a premise sentence and two possible alternatives. The system
    must choose the alternative which has the more plausible causal relationship
    with the premise. The method used for the construction of the alternatives
    ensures that the task requires causal reasoning to solve. Examples either
    deal with alternative possible causes or alternative possible effects of the
    premise sentence, accompanied by a simple question disambiguating between
    the two instance types for the model. All examples are handcrafted and focus
    on topics from online blogs and a photography-related encyclopedia.
    Following the recommendation of the authors, we evaluate using accuracy.

*   `multirc` (`v0.0.2`) (`Size: 1.16 MiB`): The Multi-Sentence Reading
    Comprehension dataset (MultiRC, Khashabi et al., 2018) is a true/false
    question-answering task. Each example consists of a context paragraph, a
    question about that paragraph, and a list of possible answers to that
    question which must be labeled as true or false. Question-answering (QA) is
    a popular problem with many datasets. We use MultiRC because of a number of
    desirable properties: (i) each question can have multiple possible correct
    answers, so each question-answer pair must be evaluated independent of other
    pairs, (ii) the questions are designed such that answering each question
    requires drawing facts from multiple context sentences, and (iii) the
    question-answer pair format more closely matches the API of other SuperGLUE
    tasks than span-based extractive QA does. The paragraphs are drawn from
    seven domains including news, fiction, and historical text.

*   `rte` (`v0.0.2`) (`Size: 733.16 KiB`): The Recognizing Textual Entailment
    (RTE) datasets come from a series of annual competitions on textual
    entailment, the problem of predicting whether a given premise sentence
    entails a given hypothesis sentence (also known as natural language
    inference, NLI). RTE was previously included in GLUE, and we use the same
    data and format as before: We merge data from RTE1 (Dagan et al., 2006),
    RTE2 (Bar Haim et al., 2006), RTE3 (Giampiccolo et al., 2007), and RTE5
    (Bentivogli et al., 2009). All datasets are combined and converted to
    two-class classification: entailment and not_entailment. Of all the GLUE
    tasks, RTE was among those that benefited from transfer learning the most,
    jumping from near random-chance performance (~56%) at the time of GLUE's
    launch to 85% accuracy (Liu et al., 2019c) at the time of writing. Given the
    eight point gap with respect to human performance, however, the task is not
    yet solved by machines, and we expect the remaining gap to be difficult to
    close.

*   `wic` (`v0.0.2`) (`Size: 347.15 KiB`): The Word-in-Context (WiC, Pilehvar
    and Camacho-Collados, 2019) dataset supports a word sense disambiguation
    task cast as binary classification over sentence pairs. Given two sentences
    and a polysemous (sense-ambiguous) word that appears in both sentences, the
    task is to determine whether the word is used with the same sense in both
    sentences. Sentences are drawn from WordNet (Miller, 1995), VerbNet
    (Schuler, 2005), and Wiktionary. We follow the original work and evaluate
    using accuracy.

*   `wsc` (`v0.0.2`) (`Size: 31.84 KiB`): The Winograd Schema Challenge (WSC,
    Levesque et al., 2012) is a reading comprehension task in which a system
    must read a sentence with a pronoun and select the referent of that pronoun
    from a list of choices. Given the difficulty of this task and the headroom
    still left, we have included WSC in SuperGLUE and recast the dataset into
    its coreference form. The task is cast as a binary classification problem,
    as opposed to N-multiple choice, in order to isolate the model's ability to
    understand the coreference links within a sentence as opposed to various
    other strategies that may come into play in multiple choice conditions. With
    that in mind, we create a split with 65% negative majority class in the
    validation set, reflecting the distribution of the hidden test set, and 52%
    negative class in the training set. The training and validation examples are
    drawn from the original Winograd Schema dataset (Levesque et al., 2012), as
    well as those distributed by the affiliated organization Commonsense
    Reasoning. The test examples are derived from fiction books and have been
    shared with us by the authors of the original dataset. Previously, a version
    of WSC recast as NLI as included in GLUE, known as WNLI. No substantial
    progress was made on WNLI, with many submissions opting to submit only
    majority class predictions. WNLI was made especially difficult due to an
    adversarial train/dev split: Premise sentences that appeared in the training
    set sometimes appeared in the development set with a different hypothesis
    and a flipped label. If a system memorized the training set without
    meaningfully generalizing, which was easy due to the small size of the
    training set, it could perform far below chance on the development set. We
    remove this adversarial design in the SuperGLUE version of WSC by ensuring
    that no sentences are shared between the training, validation, and test
    sets.

However, the validation and test sets come from different domains, with the
validation set consisting of ambiguous examples such that changing one non-noun
phrase word will change the coreference dependencies in the sentence. The test
set consists only of more straightforward examples, with a high number of noun
phrases (and thus more choices for the model), but low to no ambiguity.

*   `wsc.fixed` (`v0.0.2`) (`Size: 31.84 KiB`): The Winograd Schema Challenge
    (WSC, Levesque et al., 2012) is a reading comprehension task in which a
    system must read a sentence with a pronoun and select the referent of that
    pronoun from a list of choices. Given the difficulty of this task and the
    headroom still left, we have included WSC in SuperGLUE and recast the
    dataset into its coreference form. The task is cast as a binary
    classification problem, as opposed to N-multiple choice, in order to isolate
    the model's ability to understand the coreference links within a sentence as
    opposed to various other strategies that may come into play in multiple
    choice conditions. With that in mind, we create a split with 65% negative
    majority class in the validation set, reflecting the distribution of the
    hidden test set, and 52% negative class in the training set. The training
    and validation examples are drawn from the original Winograd Schema dataset
    (Levesque et al., 2012), as well as those distributed by the affiliated
    organization Commonsense Reasoning. The test examples are derived from
    fiction books and have been shared with us by the authors of the original
    dataset. Previously, a version of WSC recast as NLI as included in GLUE,
    known as WNLI. No substantial progress was made on WNLI, with many
    submissions opting to submit only majority class predictions. WNLI was made
    especially difficult due to an adversarial train/dev split: Premise
    sentences that appeared in the training set sometimes appeared in the
    development set with a different hypothesis and a flipped label. If a system
    memorized the training set without meaningfully generalizing, which was easy
    due to the small size of the training set, it could perform far below chance
    on the development set. We remove this adversarial design in the SuperGLUE
    version of WSC by ensuring that no sentences are shared between the
    training, validation, and test sets.

However, the validation and test sets come from different domains, with the
validation set consisting of ambiguous examples such that changing one non-noun
phrase word will change the coreference dependencies in the sentence. The test
set consists only of more straightforward examples, with a high number of noun
phrases (and thus more choices for the model), but low to no ambiguity.

This version fixes issues where the spans are not actually substrings of the
text.

## `super_glue/cb`

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'premise': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/copa`

```python
FeaturesDict({
    'choice1': Text(shape=(), dtype=tf.string),
    'choice2': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'premise': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/multirc`

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'idx': FeaturesDict({
        'answer': Tensor(shape=(), dtype=tf.int32),
        'paragraph': Tensor(shape=(), dtype=tf.int32),
        'question': Tensor(shape=(), dtype=tf.int32),
    }),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'paragraph': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/rte`

```python
FeaturesDict({
    'hypothesis': Text(shape=(), dtype=tf.string),
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'premise': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/wic`

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'pos': Text(shape=(), dtype=tf.string),
    'sentence1': Text(shape=(), dtype=tf.string),
    'sentence2': Text(shape=(), dtype=tf.string),
    'word': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/wsc`

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'span1_index': Tensor(shape=(), dtype=tf.int32),
    'span1_text': Text(shape=(), dtype=tf.string),
    'span2_index': Tensor(shape=(), dtype=tf.int32),
    'span2_text': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
})
```

## `super_glue/wsc.fixed`

```python
FeaturesDict({
    'idx': Tensor(shape=(), dtype=tf.int32),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'span1_index': Tensor(shape=(), dtype=tf.int32),
    'span1_text': Text(shape=(), dtype=tf.string),
    'span2_index': Tensor(shape=(), dtype=tf.int32),
    'span2_text': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 804
TRAIN      | 554
TEST       | 146
VALIDATION | 104

## Urls

*   [https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html](https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html)
*   [https://super.gluebenchmark.com/](https://super.gluebenchmark.com/)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
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

--------------------------------------------------------------------------------
