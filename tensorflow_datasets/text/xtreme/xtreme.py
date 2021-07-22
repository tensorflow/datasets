# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""xtreme dataset."""

import csv
import os
import json
import glob
import textwrap

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_DESCRIPTION = """
The Cross-lingual TRansfer Evaluation of Multilingual Encoders (XTREME)
benchmark is a benchmark for the evaluation of the cross-lingual generalization
ability of pre-trained multilingual models. It covers 40 typologically diverse
languages (spanning 12 language families) and includes nine tasks that
collectively require reasoning about different levels of syntax and semantics.
The languages in XTREME are selected to maximize language diversity, coverage
in existing tasks, and availability of training data. Among these are many
under-studied languages, such as the Dravidian languages Tamil (spoken in
southern India, Sri Lanka, and Singapore), Telugu and Malayalam (spoken
mainly in southern India), and the Niger-Congo languages Swahili and Yoruba,
spoken in Africa.

For a full description of the benchmark,
see the [paper](https://arxiv.org/abs/2003.11080).
"""

_CITATION = """
@article{hu2020xtreme,
    author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham 
                 Neubig and Orhan Firat and Melvin Johnson},
    title     = {XTREME: A Massively Multilingual Multi-task Benchmark for 
                 Evaluating Cross-lingual Generalization},
    journal   = {CoRR},
    volume    = {abs/2003.11080},
    year      = {2020},
    archivePrefix = {arXiv},
    eprint    = {2003.11080}
}
"""

_URL = "https://sites.research.google/xtreme"

_LANGS = {
    "xnli": [
        "en", "zh", "es", "de", "ar", "ur", "ru", "bg", "el", "fr", "hi", "sw",
        "th", "tr", "vi"
    ],
    "pawsx": ["de", "en", "es", "fr", "ja", "ko", "zh"],
    "pos": {
        "af": "Afrikaans",
        "ar": "Arabic",
        "bg": "Bulgarian",
        "de": "German",
        "el": "Greek",
        "en": "English",
        "es": "Spanish",
        "et": "Estonian",
        "eu": "Basque",
        "fa": "Persian",
        "fi": "Finnish",
        "fr": "French",
        "he": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "id": "Indonesian",
        "it": "Italian",
        "ja": "Japanese",
        "kk": "Kazakh",
        "ko": "Korean",
        "mr": "Marathi",
        "nl": "Dutch",
        "pt": "Portuguese",
        "ru": "Russian",
        "ta": "Tagalog",
        "te": "Telugu",
        "th": "Thai",
        "tl": "Tamil",
        "tr": "Turkish",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "yo": "Yoruba",
        "zh": "Chinese"
    },
    "ner": [
        "af", "ar", "bg", "bn", "de", "el", "en", "es", "et", "eu", "fa", "fi",
        "fr", "he", "hi", "hu", "id", "it", "ja", "jv", "ka", "kk", "ko", "ml",
        "mr", "ms", "my", "nl", "pt", "ru", "sw", "ta", "te", "th", "tl", "tr",
        "ur", "vi", "yo", "zh"
    ],
    "xquad": ["ar", "de", "el", "en", "es", "hi", "ru", "th", "tr", "vi", "zh"],
    "mlqa": ["ar", "de", "en", "es", "hi", "vi", "zh"],
    "tydiqa": {
        "ar": "arabic",
        "bn": "bengali",
        "en": "english",
        "fi": "finnish",
        "id": "indonesian",
        "ko": "korean",
        "ru": "russian",
        "sw": "swahili",
        "te": "telugu",
    },
    "bucc": ["de", "fr", "zh", "ru"],
    "tatoeba": {
        "af": "afr",
        "ar": "ara",
        "bg": "bul",
        "bn": "ben",
        "de": "deu",
        "el": "ell",
        "es": "spa",
        "et": "est",
        "eu": "eus",
        "fa": "pes",
        "fi": "fin",
        "fr": "fra",
        "he": "heb",
        "hi": "hin",
        "hu": "hun",
        "id": "ind",
        "it": "ita",
        "ja": "jpn",
        "jv": "jav",
        "ka": "kat",
        "kk": "kaz",
        "ko": "kor",
        "ml": "mal",
        "mr": "mar",
        "nl": "nld",
        "pt": "por",
        "ru": "rus",
        "sw": "swh",
        "ta": "tam",
        "te": "tel",
        "th": "tha",
        "tl": "tgl",
        "tr": "tur",
        "ur": "urd",
        "vi": "vie",
        "zh": "cmn",
    }
}


class XtremeConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Xtreme."""

  def __init__(self, *, features, data_urls, citation, language, **kwargs):
    """Args:

      features: `tfds.features.FeaturesDict`, specific feature dict for the
      dataset.
      data_urls: `dict`, urls to download the files from
      citation: `string`, citation for the data set
      language: `string`
      **kwargs: keyword arguments forwarded to super.
    """
    super(XtremeConfig, self).__init__(**kwargs)
    self.features = features
    self.data_urls = data_urls
    self.citation = citation
    self.language = language


class Xtreme(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for xtreme dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  XNLI_CONFIGS = [
      XtremeConfig(
          name="xnli_" + language,
          language=language,
          description=textwrap.dedent("""\
XNLI is a subset of a few thousand examples from MNLI which has been translated
into a 14 different languages (some low-ish resource). As with MNLI, the goal is
to predict textual entailment (does sentence A imply/contradict/neither sentence
B) and is a classification task (given two sentences, predict one of three
labels).
      """),
          features=tfds.features.FeaturesDict({
              "premise":
                  tfds.features.Text(),
              "hypothesis":
                  tfds.features.Text(),
              "label":
                  tfds.features.ClassLabel(
                      names=["entailment", "neutral", "contradiction"]),
          }),
          data_urls="https://cims.nyu.edu/~sbowman/xnli/XNLI-1.0.zip",
          citation=textwrap.dedent("""\
          @InProceedings{conneau2018xnli,
  author = "Conneau, Alexis
                 and Rinott, Ruty
                 and Lample, Guillaume
                 and Williams, Adina
                 and Bowman, Samuel R.
                 and Schwenk, Holger
                 and Stoyanov, Veselin",
  title = "XNLI: Evaluating Cross-lingual Sentence Representations",
  booktitle = "Proceedings of the 2018 Conference on Empirical Methods
               in Natural Language Processing",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  location = "Brussels, Belgium",
          }""")) for language in _LANGS["xnli"]
  ]

  PAWS_CONFIGS = [
      XtremeConfig(
          name="pawsx_" + language,
          language=language,
          description=textwrap.dedent("""\
This dataset contains 23,659 human translated PAWS evaluation pairs and
296,406 machine translated training pairs in six typologically distinct 
languages:

* French
* Spanish
* German
* Chinese
* Japanese
* Korean

For further details, see the accompanying paper:
PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification
at  https://arxiv.org/abs/1908.11828

Similar to PAWS Dataset, examples are split into Train/Dev/Test sections.
All files are in the tsv format with four columns:

id	A unique id for each pair
sentence1	The first sentence
sentence2	The second sentence
(noisy_)label	(Noisy) label for each pair

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.
        """),
          features=tfds.features.FeaturesDict({
              "sentence1":
                  tfds.features.Text(),
              "sentence2":
                  tfds.features.Text(),
              # Label 0: Pair has different meaning,
              # Label 1: Pair is a paraphrase
              "label":
                  tfds.features.ClassLabel(
                      names=["different_meaning", "paraphrase"]),
          }),
          data_urls="https://storage.googleapis.com/paws/pawsx/x-final.tar.gz",
          citation=textwrap.dedent("""\
            @InProceedings{conneau2018xnli,
    author = "Conneau, Alexis
                   and Rinott, Ruty
                   and Lample, Guillaume
                   and Williams, Adina
                   and Bowman, Samuel R.
                   and Schwenk, Holger
                   and Stoyanov, Veselin",
    title = "XNLI: Evaluating Cross-lingual Sentence Representations",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods
                 in Natural Language Processing",
    year = "2018",
    publisher = "Association for Computational Linguistics",
    location = "Brussels, Belgium",
            }""")) for language in _LANGS["pawsx"]
  ]

  NER_CONFIGS = [
      XtremeConfig(
          name="ner_" + language,
          language=language,
          description=textwrap.dedent("""\
  WikiANN (sometimes called PAN-X) is a multilingual named entity recognition \
  dataset consisting of Wikipedia articles annotated with LOC (location), PER \
  (person), and ORG (organisation) tags in the IOB2 format. This version \
  corresponds to the balanced train, dev, and test splits of Rahimi et al. \
  (2019), which supports 176 of the 282 languages from the original WikiANN \
  corpus.
        """),
          features=tfds.features.FeaturesDict({
              "tokens":
                  tfds.features.Sequence(tfds.features.Text()),
              "tags":
                  tfds.features.Sequence(
                      tfds.features.ClassLabel(names=[
                          "O",
                          "B-PER",
                          "I-PER",
                          "B-ORG",
                          "I-ORG",
                          "B-LOC",
                          "I-LOC",
                      ])),
          }),
          data_urls="https://www.dropbox.com/s/12h3qqog6q4bjve/panx_dataset.tar?dl=1",
          citation=textwrap.dedent("""\
            @inproceedings{rahimi-etal-2019-massively,
      title = "Massively Multilingual Transfer for {NER}",
      author = "Rahimi, Afshin  and
        Li, Yuan  and
        Cohn, Trevor",
      booktitle = "Proceedings of the 57th Annual Meeting of the Association \
      for Computational Linguistics",
      month = jul,
      year = "2019",
      address = "Florence, Italy",
      publisher = "Association for Computational Linguistics",
      url = "https://www.aclweb.org/anthology/P19-1015",
      pages = "151--164",
  }""")) for language in _LANGS["ner"]
  ]

  POS_CONFIGS = [
      XtremeConfig(
          name="pos_" + language,
          language=language,
          description=textwrap.dedent("""\
    Universal Dependencies (UD) is a framework for consistent annotation of 
    grammar (parts of speech, morphological
    features, and syntactic dependencies) across different human languages. 
    UD is an open community effort with over 200
    contributors producing more than 100 treebanks in over 70 languages. 
    If you’re new to UD, you should start by reading
    the first part of the Short Introduction and then browsing the 
    annotation guidelines.
    """),
          features=tfds.features.FeaturesDict({
              "tokens":
                  tfds.features.Sequence(tfds.features.Text()),
              "tags":
                  tfds.features.Sequence(
                      tfds.features.ClassLabel(names=[
                          "ADJ",
                          "ADP",
                          "ADV",
                          "AUX",
                          "CCONJ",
                          "DET",
                          "INTJ",
                          "NOUN",
                          "NUM",
                          "PART",
                          "PRON",
                          "PROPN",
                          "PUNCT",
                          "SCONJ",
                          "SYM",
                          "VERB",
                          "X",
                      ])),
          }),
          data_urls="https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3105/ud-treebanks-v2.5.tgz",
          citation=textwrap.dedent("""\
          @article{nivre2018universal,
          title={Universal Dependencies 2.2},
          author={Nivre, Joakim and Abrams, Mitchell and Agi{\'c}, {\v{Z}}eljko 
          and Ahrenberg, Lars and Antonsen, Lene and Aranzabe, Maria Jesus and 
          Arutie, Gashaw and Asahara, Masayuki and Ateyah, Luma and Attia, 
          Mohammed and others},
          year={2018}}""")) for language in _LANGS["pos"]
  ]

  TYDIQA_CONFIGS = [
      XtremeConfig(
          name="tydiqa_" + language,
          language=language,
          description=textwrap.dedent("""\
TyDi QA is a question answering dataset covering 11 typologically diverse \
languages with 204K question-answer pairs. The languages of TyDi QA are \
diverse with regard to their typology -- the set of linguistic features that \
each language expresses -- such that we expect models performing well on this \
set to generalize across a large number of the languages in the world. It \
contains language phenomena that would not be found in English-only corpora. \
To provide a realistic information-seeking task and avoid priming effects, \
questions are written by people who want to know the answer, but don't know \
the answer yet, (unlike SQuAD and its descendents) and the data is collected \
directly in each language without the use of translation (unlike MLQA and \
XQuAD).
      """),
          features=qa_utils.SQUADLIKE_FEATURES,
          data_urls={
              "train":
                  "https://storage.googleapis.com/tydiqa/v1.1/tydiqa-goldp-v1.1-train.json",
              "validation":
                  "https://storage.googleapis.com/tydiqa/v1.1/tydiqa-goldp-v1.1-dev.json"
          },
          citation=textwrap.dedent("""\
          @article{tydiqa,
   title = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
  author = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
    year = {2020},
 journal = {Transactions of the Association for Computational Linguistics}
}""")) for language in _LANGS["tydiqa"]
  ]

  MLQA_CONFIGS = [
      XtremeConfig(
          name="mlqa_" + language,
          language=language,
          description=textwrap.dedent("""\
MLQA (Multilingual Question Answering Dataset) is a benchmark dataset for \
evaluating multilingual question answering performance. The dataset consists \
of 7 languages: Arabic, German, Spanish, English, Hindi, Vietnamese, Chinese.
      """),
          features=qa_utils.SQUADLIKE_FEATURES,
          data_urls="https://dl.fbaipublicfiles.com/MLQA/MLQA_V1.zip",
          citation=textwrap.dedent("""\
@article{lewis2019mlqa,
  title={MLQA: Evaluating Cross-lingual Extractive Question Answering},
  author={Lewis, Patrick and Ouguz, Barlas and Rinott, Ruty and Riedel, \
  Sebastian and Schwenk, Holger},
  journal={arXiv preprint arXiv:1910.07475},
  year={2019}
}""")) for language in _LANGS["mlqa"]
  ]

  XQUAD_CONFIGS = [
      XtremeConfig(
          name="xquad_" + language,
          language=language,
          description=textwrap.dedent("""\
XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for \
evaluating cross-lingual question answering performance. The dataset consists \
of a subset of 240 paragraphs and 1190 question-answer pairs from the \
development set of SQuAD v1.1 (Rajpurkar et al., 2016) together with their \
professional translations into ten languages: Spanish, German, Greek, Russian, \
Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Consequently, the \
dataset is entirely parallel across 11 languages. \
\
To run XQuAD in the default zero-shot setting, use the SQuAD v1.1 training and \
validation data here: https://www.tensorflow.org/datasets/catalog/squad
      """),
          features=qa_utils.SQUADLIKE_FEATURES,
          data_urls="https://github.com/deepmind/xquad/raw/master/xquad.{lang}.json",
          citation=textwrap.dedent("""\
@article{lewis2019mlqa,
  title={MLQA: Evaluating Cross-lingual Extractive Question Answering},
  author={Lewis, Patrick and Ouguz, Barlas and Rinott, Ruty and Riedel, \
  Sebastian and Schwenk, Holger},
  journal={arXiv preprint arXiv:1910.07475},
  year={2019}
}""")) for language in _LANGS["xquad"]
  ]

  BUCC_CONFIGS = [
      XtremeConfig(
          name="bucc_" + language,
          language=language,
          description=textwrap.dedent("""\
    Identifying parallel sentences in comparable corpora. Given two 
    sentence-split monolingual corpora, participant systems are expected 
    to identify pairs of sentences that are translations of each other.
    """),
          features=tfds.features.FeaturesDict({
              "source_sentence": tfds.features.Text(),
              "target_sentence": tfds.features.Text(),
              "source_id": tfds.features.Text(),
              "target_id": tfds.features.Text(),
          }),
          data_urls="https://comparable.limsi.fr/bucc2018/",
          citation=textwrap.dedent("""\
  @inproceedings{zweigenbaum2018overview,
  title={Overview of the third BUCC shared task: Spotting parallel sentences 
  in comparable corpora},
  author={Zweigenbaum, Pierre and Sharoff, Serge and Rapp, Reinhard},
  booktitle={Proceedings of 11th Workshop on Building and Using Comparable 
  Corpora},
  pages={39--42},
  year={2018}
}""")) for language in _LANGS["bucc"]
  ]

  TATOEBA_CONFIGS = [
      XtremeConfig(
          name="tatoeba_" + language,
          language=language,
          description=textwrap.dedent("""\
          This data is extracted from the Tatoeba corpus, dated Saturday 
          2018/11/17.
          For each languages, we have selected 1000 English sentences and their 
          translations, if available. Please check
          this paper for a description of the languages, their families and 
          scripts as well as baseline results.
          Please note that the English sentences are not identical for all 
          language pairs. This means that the results are
          not directly comparable across languages. 
    """),
          features=tfds.features.FeaturesDict({
              "source_sentence": tfds.features.Text(),
              "target_sentence": tfds.features.Text(),
              "source_language": tfds.features.Text(),
              "target_language": tfds.features.Text(),
          }),
          data_urls="https://github.com/facebookresearch/LASER/raw/master/data/tatoeba/v1",
          citation=textwrap.dedent("""\
  @article{tatoeba,
            title={Massively Multilingual Sentence Embeddings for Zero-Shot 
                   Cross-Lingual Transfer and Beyond},
            author={Mikel, Artetxe and Holger, Schwenk,},
            journal={arXiv:1812.10464v2},
            year={2018}""")) for language in _LANGS["tatoeba"]
  ]

  BUILDER_CONFIGS = []
  BUILDER_CONFIGS.extend(XNLI_CONFIGS)
  BUILDER_CONFIGS.extend(PAWS_CONFIGS)
  BUILDER_CONFIGS.extend(NER_CONFIGS)
  BUILDER_CONFIGS.extend(POS_CONFIGS)
  BUILDER_CONFIGS.extend(TYDIQA_CONFIGS)
  BUILDER_CONFIGS.extend(MLQA_CONFIGS)
  BUILDER_CONFIGS.extend(XQUAD_CONFIGS)
  BUILDER_CONFIGS.extend(BUCC_CONFIGS)
  BUILDER_CONFIGS.extend(TATOEBA_CONFIGS)

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(self.builder_config.features),
        homepage=_URL,
        citation=self.builder_config.citation + "\n" + _CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    if self.builder_config.name.startswith("xnli"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      data_dir = os.path.join(dl_dir, "XNLI-1.0")
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": os.path.join(data_dir, "xnli.test.tsv"),
                  "language": self.builder_config.language
              }),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": os.path.join(data_dir, "xnli.dev.tsv"),
                  "language": self.builder_config.language
              }),
      ]
    if self.builder_config.name.startswith("pawsx"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      base_path = os.path.join(dl_dir, "x-final")
      # Name of file for training for 'en' is different from other languages
      if self.builder_config.language == "en":
        training_path = os.path.join(base_path, self.builder_config.language,
                                     "train.tsv")
      else:
        training_path = os.path.join(base_path, self.builder_config.language,
                                     "translated_train.tsv")

      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={"filepath": training_path},
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath":
                      os.path.join(base_path, self.builder_config.language,
                                   "test_2k.tsv")
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(base_path, self.builder_config.language,
                                   "dev_2k.tsv")
              },
          ),
      ]
    if self.builder_config.name.startswith("ner"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      subpath = dl_manager.extract(
          os.path.join(dl_dir, self.builder_config.language + ".tar.gz"))

      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={"filepath": os.path.join(subpath, "dev")},
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={"filepath": os.path.join(subpath, "test")},
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={"filepath": os.path.join(subpath, "train")},
          ),
      ]

    if self.builder_config.name.startswith("pos"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      subpath = os.path.join(dl_dir, "ud-treebanks-v2.5")
      lang = _LANGS["pos"][self.builder_config.language]
      data_dir = os.path.join(subpath, "*_" + lang + "*")
      folders = sorted(glob.glob(data_dir))

      if lang == "Kazakh":
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "test" in file and file.endswith(".conllu")
                    ]
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "train" in file and file.endswith(".conllu")
                    ]
                },
            ),
        ]
      elif lang == "Tagalog" or lang == "Thai" or lang == "Yoruba":
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "test" in file and file.endswith(".conllu")
                    ]
                },
            ),
        ]
      else:
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "NYUAD" not in folder and "test" in file and
                        file.endswith(".conllu")
                    ]
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "NYUAD" not in folder and "dev" in file and
                        file.endswith(".conllu")
                    ]
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "filepath": [
                        os.path.join(folder, file)
                        for folder in folders
                        for file in sorted(os.listdir(folder))
                        if "NYUAD" not in folder and "train" in file and
                        file.endswith(".conllu")
                    ]
                },
            ),
        ]

    if self.builder_config.name.startswith("tydiqa"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": dl_dir["train"],
                  "language": self.builder_config.language
              }),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": dl_dir["validation"],
                  "language": self.builder_config.language
              }),
      ]
    if self.builder_config.name.startswith("mlqa"):
      dl_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(
                          dl_dir, "MLQA_V1", "dev",
                          "dev-context-{0}-question-{0}.json".format(
                              self.builder_config.language))
              }),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath":
                      os.path.join(
                          dl_dir, "MLQA_V1", "test",
                          "test-context-{0}-question-{0}.json".format(
                              self.builder_config.language))
              }),
      ]

    if self.builder_config.name.startswith("xquad"):
      dl_dir = dl_manager.download_and_extract(
          self.builder_config.data_urls.format(
              lang=self.builder_config.language))
      return [
          tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
              name=tfds.Split.TEST,
              gen_kwargs={"filepath": dl_dir})
      ]

    if self.builder_config.name.startswith("bucc"):
      bucc_test_dir = dl_manager.download_and_extract(
          os.path.join(
              self.builder_config.data_urls,
              "bucc2018-{}-en.training-gold.tar.bz2".format(
                  self.builder_config.language),
          ))
      bucc_dev_dir = dl_manager.download_and_extract(
          os.path.join(
              self.builder_config.data_urls,
              "bucc2018-{}-en.sample-gold.tar.bz2".format(
                  self.builder_config.language),
          ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(bucc_dev_dir, "bucc2018",
                                   self.builder_config.language + "-en")
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath":
                      os.path.join(bucc_test_dir, "bucc2018",
                                   self.builder_config.language + "-en")
              },
          ),
      ]

    if self.builder_config.name.startswith("tatoeba"):
      lang = _LANGS["tatoeba"][self.builder_config.language]
      tatoeba_source_data = dl_manager.download_and_extract(
          os.path.join(self.builder_config.data_urls,
                       "tatoeba.{}-eng.{}".format(lang, lang)))
      tatoeba_eng_data = dl_manager.download_and_extract(
          os.path.join(self.builder_config.data_urls,
                       "tatoeba.{}-eng.eng".format(lang)))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={"filepath": (tatoeba_source_data, tatoeba_eng_data)},
          ),
      ]

  def _generate_examples(self, filepath, language="en"):
    """Yields examples."""
    if self.builder_config.name.startswith("xnli"):
      with tf.io.gfile.GFile(filepath) as f:
        reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
      for row in reader:
        if row["language"] == language:
          yield row["pairID"], {
              "premise": row["sentence1"],
              "hypothesis": row["sentence2"],
              "label": row["gold_label"],
          }
    if self.builder_config.name.startswith("pawsx"):
      with tf.io.gfile.GFile(filepath) as f:
        reader = csv.DictReader(f, delimiter="\t")
      for row in reader:
        # Some rows in the files have been wrongly populated
        if row["label"] in ("0", "1"):
          key = row["id"]
          example = {
              "sentence1": row["sentence1"],
              "sentence2": row["sentence2"],
              "label": int(row["label"]),
          }
          yield key, example

    if self.builder_config.name.startswith("ner"):
      key = 1
      with tf.io.gfile.GFile(filepath, "r") as f:
        tokens = []
        tags = []
        for line in f:
          line = line.rstrip()
          if line.startswith("-DOCSTART-") or line == "":
            if tokens:
              yield key, {
                  "tokens": tokens,
                  "tags": tags,
              }
              key += 1
              tokens = []
              tags = []
          else:
            # wikiann data is tab separated
            fields = line.split("\t")
            # strip out language prefix
            tokens.append(":".join(fields[0].split(":")[1:]))
            if len(fields) > 1:
              tags.append(fields[-1])
            else:
              # examples have no label in test set
              tags.append("O")
        if tokens:
          yield key, {
              "tokens": tokens,
              "tags": tags,
          }

    if self.builder_config.name.startswith("pos"):
      for id_file, file in enumerate(filepath):
        with open(file, encoding="utf-8") as f:
          data = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
          tokens = []
          pos_tags = []
          for id_row, row in enumerate(data):
            if len(row) >= 10 and row[1] != "_" and row[3] != "_":
              tokens.append(row[1])
              pos_tags.append(row[3])
            if len(row) == 0 and len(tokens) > 0:
              yield str(id_file) + "_" + str(id_row), {
                  "tokens": tokens,
                  "tags": pos_tags,
              }
              tokens = []
              pos_tags = []

    # This is similar to squad example generator with language filter.
    if self.builder_config.name.startswith("tydiqa"):
      qas = {}
      with tf.io.gfile.GFile(filepath) as f:
        squad = json.load(f)
        for article in squad["data"]:
          title = article.get("title", "")
          for paragraph in article["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
              qa["title"] = title
              qa["context"] = context
              id_ = qa["id"]
              if id_ in qas:
                qas[id_]["answers"].extend(qa["answers"])
              else:
                qas[id_] = qa

        for id_, qa in qas.items():
          if _LANGS["tydiqa"][language] == id_.split("--")[0]:
            answer_starts = [answer["answer_start"] for answer in qa["answers"]]
            answers = [answer["text"] for answer in qa["answers"]]
            yield id_, {
                "title": qa["title"],
                "context": qa["context"],
                "question": qa["question"],
                "id": id_,
                "answers": {
                    "answer_start": answer_starts,
                    "text": answers,
                },
            }

    if self.builder_config.name.startswith(
        "mlqa") or self.builder_config.name.startswith("xquad"):
      qas = {}
      with tf.io.gfile.GFile(filepath) as f:
        squad = json.load(f)
        for article in squad["data"]:
          title = article.get("title", "")
          for paragraph in article["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
              qa["title"] = title
              qa["context"] = context
              id_ = qa["id"]
              if id_ in qas:
                qas[id_]["answers"].extend(qa["answers"])
              else:
                qas[id_] = qa

        for id_, qa in qas.items():
          answer_starts = [answer["answer_start"] for answer in qa["answers"]]
          answers = [answer["text"] for answer in qa["answers"]]
          yield id_, {
              "title": qa["title"],
              "context": qa["context"],
              "question": qa["question"],
              "id": id_,
              "answers": {
                  "answer_start": answer_starts,
                  "text": answers,
              },
          }

    if self.builder_config.name.startswith("bucc"):
      files = sorted(os.listdir(filepath))
      target_file = "/"
      source_file = "/"
      source_target_file = "/"
      for file in files:
        if file.endswith("en"):
          target_file = os.path.join(filepath, file)
        elif file.endswith("gold"):
          source_target_file = os.path.join(filepath, file)
        else:
          source_file = os.path.join(filepath, file)
      with open(target_file, encoding="utf-8") as f:
        data = csv.reader(f, delimiter="\t")
        target_sentences = [row for row in data]
      with open(source_file, encoding="utf-8") as f:
        data = csv.reader(f, delimiter="\t")
        source_sentences = [row for row in data]
      with open(source_target_file, encoding="utf-8") as f:
        data = csv.reader(f, delimiter="\t")
        source_target_ids = [row for row in data]
      for id_, pair in enumerate(source_target_ids):
        source_id = pair[0]
        target_id = pair[1]
        source_sent = ""
        target_sent = ""
        for i in range(len(source_sentences)):
          if source_sentences[i][0] == source_id:
            source_sent = source_sentences[i][1]
            source_id = source_sentences[i][0]
            break
        for j in range(len(target_sentences)):
          if target_sentences[j][0] == target_id:
            target_sent = target_sentences[j][1]
            target_id = target_sentences[j][0]
            break
        yield id_, {
            "source_sentence": source_sent,
            "target_sentence": target_sent,
            "source_id": source_id,
            "target_id": target_id,
        }

    if self.builder_config.name.startswith("tatoeba"):
      source_file = filepath[0]
      target_file = filepath[1]
      source_sentences = []
      target_sentences = []
      with open(source_file, encoding="utf-8") as f1:
        for row in f1:
          source_sentences.append(row)
      with open(target_file, encoding="utf-8") as f2:
        for row in f2:
          target_sentences.append(row)
      for i in range(len(source_sentences)):
        yield i, {
            "source_sentence": source_sentences[i],
            "target_sentence": target_sentences[i],
            "source_language": self.builder_config.language,
            "target_language": "en",
        }
