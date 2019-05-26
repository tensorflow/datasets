# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The SuperGLUE benchmark."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

import six
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_SUPER_GLUE_CITATION = """\
@article{wang2019superglue,
  title={SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1905.00537},
  year={2019}
}

Note that each SuperGLUE dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.
"""

_CB_DESCRIPTION = """\
The CommitmentBank (De Marneffe et al., 2019) is a corpus of short texts in which at least
one sentence contains an embedded clause. Each of these embedded clauses is annotated with the
degree to which we expect that the person who wrote the text is committed to the truth of the clause.
The resulting task framed as three-class textual entailment on examples that are drawn from the Wall
Street Journal, fiction from the British National Corpus, and Switchboard. Each example consists
of a premise containing an embedded clause and the corresponding hypothesis is the extraction of
that clause. We use a subset of the data that had inter-annotator agreement above 0.85. The data is
imbalanced (relatively fewer neutral examples), so we evaluate using accuracy and F1, where for
multi-class F1 we compute the unweighted average of the F1 per class."""

_COPA_DESCRIPTION = """\
The Choice Of Plausible Alternatives (COPA, Roemmele et al., 2011) dataset is a causal
reasoning task in which a system is given a premise sentence and two possible alternatives. The
system must choose the alternative which has the more plausible causal relationship with the premise.
The method used for the construction of the alternatives ensures that the task requires causal reasoning
to solve. Examples either deal with alternative possible causes or alternative possible effects of the
premise sentence, accompanied by a simple question disambiguating between the two instance
types for the model. All examples are handcrafted and focus on topics from online blogs and a
photography-related encyclopedia. Following the recommendation of the authors, we evaluate using
accuracy."""

_RTE_DESCRIPTION = """\
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
gap to be difficult to close."""

_MULTIRC_DESCRIPTION = """\
The Multi-Sentence Reading Comprehension dataset (MultiRC, Khashabi et al., 2018)
is a true/false question-answering task. Each example consists of a context paragraph, a question
about that paragraph, and a list of possible answers to that question which must be labeled as true or
false. Question-answering (QA) is a popular problem with many datasets. We use MultiRC because
of a number of desirable properties: (i) each question can have multiple possible correct answers,
so each question-answer pair must be evaluated independent of other pairs, (ii) the questions are
designed such that answering each question requires drawing facts from multiple context sentences,
and (iii) the question-answer pair format more closely matches the API of other SuperGLUE tasks
than span-based extractive QA does. The paragraphs are drawn from seven domains including news,
fiction, and historical text."""

_WIC_DESCRIPTION = """\
The Word-in-Context (WiC, Pilehvar and Camacho-Collados, 2019) dataset supports a word
sense disambiguation task cast as binary classification over sentence pairs. Given two sentences and a
polysemous (sense-ambiguous) word that appears in both sentences, the task is to determine whether
the word is used with the same sense in both sentences. Sentences are drawn from WordNet (Miller,
1995), VerbNet (Schuler, 2005), and Wiktionary. We follow the original work and evaluate using
accuracy."""

_WSC_DESCRIPTION = """\
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
high number of noun phrases (and thus more choices for the model), but low to no ambiguity."""

_CB_CITATION = """\
@article{de marneff_simons_tonhauser_2019,
  title={The CommitmentBank: Investigating projection in naturally occurring discourse},
  journal={proceedings of Sinn und Bedeutung 23},
  author={De Marneff, Marie-Catherine and Simons, Mandy and Tonhauser, Judith},
  year={2019}
}"""

_COPA_CITATION = """\
@inproceedings{roemmele2011choice,
  title={Choice of plausible alternatives: An evaluation of commonsense causal reasoning},
  author={Roemmele, Melissa and Bejan, Cosmin Adrian and Gordon, Andrew S},
  booktitle={2011 AAAI Spring Symposium Series},
  year={2011}
}"""

_RTE_CITATION = """\
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
}"""

_MULTIRC_CITATION = """\
@inproceedings{MultiRC2018,
    author = {Daniel Khashabi and Snigdha Chaturvedi and Michael Roth and Shyam Upadhyay and Dan Roth},
    title = {Looking Beyond the Surface:A Challenge Set for Reading Comprehension over Multiple Sentences},
    booktitle = {Proceedings of North American Chapter of the Association for Computational Linguistics (NAACL)},
    year = {2018}
}"""

_WIC_CITATION = """\
@article{DBLP:journals/corr/abs-1808-09121,
  author={Mohammad Taher Pilehvar and os{\'{e}} Camacho{-}Collados},
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
}"""

_WSC_CITATION = """\
@inproceedings{levesque2012winograd,
  title={The winograd schema challenge},
  author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
  booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
  year={2012}
}"""


class SuperGlueConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SuperGLUE."""

  @api_utils.disallow_positional_args
  def __init__(self,
               features,
               data_url,
               citation,
               url,
               label_classes=("False", "True"),
               **kwargs):
    """BuilderConfig for SuperGLUE.

    Args:
      features: `list[string]`, list of the features that will appear in the
        feature dict. Should not include "label".
      data_url: `string`, url to download the zip file from.
      citation: `string`, citation for the data set.
      url: `string`, url for information about the data set.
      label_classes: `list[string]`, the list of classes for the label if the
        label is present as a string. Non-string labels will be cast to either
        'False' or 'True'.
      **kwargs: keyword arguments forwarded to super.
    """
    super(SuperGlueConfig, self).__init__(**kwargs)
    self.features = features
    self.label_classes = label_classes
    self.data_url = data_url
    self.citation = citation
    self.url = url


class SuperGlue(tfds.core.GeneratorBasedBuilder):
  """The SuperGLUE benchmark."""
  BUILDER_CONFIGS = [
      SuperGlueConfig(
          name="cb",
          version="0.0.2",
          description=_CB_DESCRIPTION,
          features=["premise", "hypothesis"],
          label_classes=["entailment", "contradiction", "neutral"],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/CB.zip",
          citation=_CB_CITATION,
          url="https://github.com/mcdm/CommitmentBank"),
      SuperGlueConfig(
          name="copa",
          version="0.0.2",
          description=_COPA_DESCRIPTION,
          label_classes=["choice1", "choice2"],
          # Note that question will only be the X in the statement "What's
          # the X for this?".
          features=["premise", "choice1", "choice2", "question"],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/COPA.zip",
          citation=_COPA_CITATION,
          url="http://people.ict.usc.edu/~gordon/copa.html"),
      SuperGlueConfig(
          name="multirc",
          version="0.0.2",
          description=_MULTIRC_DESCRIPTION,
          features=["paragraph", "question", "answer"],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/MultiRC.zip",
          citation=_MULTIRC_CITATION,
          url="https://cogcomp.org/multirc/"),
      SuperGlueConfig(
          name="rte",
          version="0.0.2",
          description=_RTE_DESCRIPTION,
          features=["premise", "hypothesis"],
          label_classes=["entailment", "not_entailment"],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/RTE.zip",
          citation=_RTE_CITATION,
          url="https://aclweb.org/aclwiki/Recognizing_Textual_Entailment"),
      SuperGlueConfig(
          name="wic",
          version="0.0.2",
          description=_WIC_DESCRIPTION,
          # pos refers to part of speech (e.g., "N", "V", ...).
          features=["word", "pos", "sentence1", "sentence2"],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/WiC.zip",
          citation=_WIC_CITATION,
          url="https://pilehvar.github.io/wic/"),
      SuperGlueConfig(
          name="wsc",
          version="0.0.2",
          description=_WSC_DESCRIPTION,
          # Note that span1_index and span2_index will be integers stored as
          # tf.int32.
          features=[
              "text", "span1_index", "span2_index", "span1_text", "span2_text"
          ],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/WSC.zip",
          citation=_WSC_CITATION,
          url="https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html"
      ),
      SuperGlueConfig(
          name="wsc.fixed",
          version="0.0.2",
          description=(
              _WSC_DESCRIPTION +
              "\n\nThis version fixes issues where the spans are not actually "
              "substrings of the text."),
          # Note that span1_index and span2_index will be integers stored as
          # tf.int32.
          features=[
              "text", "span1_index", "span2_index", "span1_text", "span2_text"
          ],
          data_url="https://dl.fbaipublicfiles.com/glue/superglue/data/WSC.zip",
          citation=_WSC_CITATION,
          url="https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html"
      ),
  ]

  def _info(self):
    features = {
        feature: tfds.features.Text()
        for feature in self.builder_config.features
    }
    if self.builder_config.name.startswith("wsc"):
      features["span1_index"] = tf.int32
      features["span2_index"] = tf.int32
    if self.builder_config.name == "multirc":
      features["idx"] = tfds.features.FeaturesDict({
          "paragraph": tf.int32,
          "question": tf.int32,
          "answer": tf.int32,
      })
    else:
      features["idx"] = tf.int32
    features["label"] = tfds.features.ClassLabel(
        names=self.builder_config.label_classes)
    return tfds.core.DatasetInfo(
        builder=self,
        description=self.builder_config.description,
        features=tfds.features.FeaturesDict(features),
        urls=[
            self.builder_config.url,
            "https://super.gluebenchmark.com/",
        ],
        citation=self.builder_config.citation + "\n" + _SUPER_GLUE_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_dir = dl_manager.download_and_extract(self.builder_config.data_url)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
                "data_file": os.path.join(dl_dir or "", "train.jsonl"),
                "split": tfds.Split.TRAIN,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                "data_file": os.path.join(dl_dir or "", "val.jsonl"),
                "split": tfds.Split.VALIDATION,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={
                "data_file": os.path.join(dl_dir or "", "test.jsonl"),
                "split": tfds.Split.TEST,
            }),
    ]

  def _generate_examples(self, data_file, split):
    with tf.io.gfile.GFile(data_file) as f:
      for line in f:
        row = json.loads(line)

        if self.builder_config.name == "multirc":
          paragraph = row["paragraph"]
          for question in paragraph["questions"]:
            for answer in question["answers"]:
              is_answer = answer.get("isAnswer")
              yield {
                  "paragraph": paragraph["text"],
                  "question": question["question"],
                  "answer": answer["text"],
                  "label": -1 if is_answer is None else _cast_label(is_answer),
                  "idx": {
                      "paragraph": row["idx"],
                      "question": question["idx"],
                      "answer": answer["idx"]
                  }
              }
        else:
          if self.builder_config.name.startswith("wsc"):
            row.update(row["target"])
          example = {
              feature: row[feature] for feature in self.builder_config.features
          }
          if self.builder_config.name == "wsc.fixed":
            example = _fix_wst(example)
          example["idx"] = row["idx"]

          if "label" in row:
            if self.builder_config.name == "copa":
              example["label"] = "choice2" if row["label"] else "choice1"
            else:
              example["label"] = _cast_label(row["label"])
          else:
            assert split == tfds.Split.TEST, row
            example["label"] = -1
          yield example


def _fix_wst(ex):
  """Fixes most cases where spans are not actually substrings of text."""
  def _fix_span_text(k):
    """Fixes a single span."""
    text = ex[k + "_text"]
    index = ex[k + "_index"]

    if text in ex["text"]:
      return

    if text in ("Kamenev and Zinoviev", "Kamenev, Zinoviev, and Stalin"):
      # There is no way to correct these examples since the subjects have
      # intervening text.
      return

    if "theyscold" in text:
      ex["text"].replace("theyscold", "they scold")
      ex["span2_index"] = 10
    # Make sure case of the first words match.
    first_word = ex["text"].split()[index]
    if first_word[0].islower():
      text = text[0].lower() + text[1:]
    else:
      text = text[0].upper() + text[1:]
    # Remove punctuation in span.
    text = text.rstrip(".")
    # Replace incorrect whitespace character in span.
    text = text.replace("\n", " ")
    ex[k + "_text"] = text
    assert ex[k + "_text"] in ex["text"], ex
  _fix_span_text("span1")
  _fix_span_text("span2")
  return ex


def _cast_label(label):
  """Converts the label into the appropriate string version."""
  if isinstance(label, six.string_types):
    return label
  elif isinstance(label, bool):
    return "True" if label else "False"
  elif isinstance(label, six.integer_types):
    assert label in (0, 1)
    return str(label)
  else:
    raise ValueError("Invalid label format.")
