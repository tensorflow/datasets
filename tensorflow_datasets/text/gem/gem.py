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

"""gem dataset."""

import csv
import json
import os
import textwrap

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
**GEM** is a benchmark environment for Natural Language Generation with a focus
on its Evaluation, both through human annotations and automated Metrics.

GEM aims to: (1) measure NLG progress across 13 datasets spanning many NLG
tasks and languages. (2) provide an in-depth analysis of data and models
presented via data statements and challenge sets. (3) develop standards for
evaluation of generated text using both automated and human metrics.

More information can be found at
[https://gem-benchmark.com](https://gem-benchmark.com).
"""

_URL = "https://gem-benchmark.com"

_CITATION = r"""@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
"""

# Used to convert IDs into dialog act names in schema-guided dialog.
_SGD_ACTS = [
    "AFFIRM",
    "AFFIRM_INTENT",
    "CONFIRM",
    "GOODBYE",
    "INFORM",
    "INFORM_COUNT",
    "INFORM_INTENT",
    "NEGATE",
    "NEGATE_INTENT",
    "NOTIFY_FAILURE",
    "NOTIFY_SUCCESS",
    "OFFER",
    "OFFER_INTENT",
    "REQUEST",
    "REQUEST_ALTS",
    "REQ_MORE",
    "SELECT",
    "THANK_YOU",
]

# Used in Xsum to clean data.
_XSUM_REMOVE_LINES = set([
    "Share this with\n",
    "Email\n",
    "Facebook\n",
    "Messenger\n",
    "Twitter\n",
    "Pinterest\n",
    "WhatsApp\n",
    "Linkedin\n",
    "LinkedIn\n",
    "Copy this link\n",
    "These are external links and will open in a new window\n",
])

_WIKI_LINGUA_LANGS = {
    "wiki_lingua_arabic_ar":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/arabic.zip",
    "wiki_lingua_chinese_zh":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/chinese.zip",
    "wiki_lingua_czech_cs":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/czech.zip",
    "wiki_lingua_dutch_nl":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/dutch.zip",
    "wiki_lingua_english_en":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/english.zip",
    "wiki_lingua_french_fr":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/french.zip",
    "wiki_lingua_german_de":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/german.zip",
    "wiki_lingua_hindi_hi":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/hindi.zip",
    "wiki_lingua_indonesian_id":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/indonesian.zip",
    "wiki_lingua_italian_it":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/italian.zip",
    "wiki_lingua_japanese_ja":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/japanese.zip",
    "wiki_lingua_korean_ko":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/korean.zip",
    "wiki_lingua_portuguese_pt":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/portuguese.zip",
    "wiki_lingua_russian_ru":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/russian.zip",
    "wiki_lingua_spanish_es":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/spanish.zip",
    "wiki_lingua_thai_th":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/thai.zip",
    "wiki_lingua_turkish_tr":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/turkish.zip",
    "wiki_lingua_vietnamese_vi":
        "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_wikilingua_full/vietnamese.zip",
}


class GemConfig(tfds.core.BuilderConfig):
  """BuilderConfig for GEM."""

  def __init__(self, *, features, data_urls, citation, **kwargs):
    """BuilderConfig for GEM.

    Args:
      features: `tfds.features.FeaturesDict`, specific feature dict for the
        dataset.
      data_urls: `dict`, urls to download the files from
      citation: `string`, citation for the data set
      **kwargs: keyword arguments forwarded to super.
    """
    super(GemConfig, self).__init__(**kwargs)
    self.features = features
    self.data_urls = data_urls
    self.citation = citation


class Gem(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for GEM benchmark."""
  VERSION = tfds.core.Version("1.1.0")
  RELEASE_NOTES = {
      "1.1.0": "Release of the Challenge Sets",
      "1.0.1": "Update bad links filter for MLSum",
      "1.0.0": "Initial version"
  }
  BUILDER_CONFIGS = [
      GemConfig(
          name="common_gen",
          description=textwrap.dedent("""\
      CommonGen is a constrained text generation task, associated with a
      benchmark dataset, to explicitly test machines for the ability of
      generative commonsense reasoning. Given a set of common concepts;
      the task is to generate a coherent sentence describing an everyday
      scenario using these concepts.
      """),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "concept_set_id": tf.int32,
              "concepts": tfds.features.Sequence(tf.string),
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "data":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/common_gen/commongen_data.zip",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/common_gen.zip"
          },
          citation=textwrap.dedent("""\
          @inproceedings{lin2020commongen,
            title = "CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning",
            author = "Lin, Bill Yuchen  and
              Zhou, Wangchunshu  and
              Shen, Ming  and
              Zhou, Pei  and
              Bhagavatula, Chandra  and
              Choi, Yejin  and
              Ren, Xiang",
            booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
            month = nov,
            year = "2020",
            address = "Online",
            publisher = "Association for Computational Linguistics",
            url = "https://www.aclweb.org/anthology/2020.findings-emnlp.165",
            pages = "1823--1840",
          }""")),
      GemConfig(
          name="cs_restaurants",
          description=textwrap.dedent("""\
          The task is generating responses in the context of a (hypothetical)
          dialogue system that provides information about restaurants.
          The input is a basic intent/dialogue act type and a list of slots
          (attributes) and their values. The output is a natural language
          sentence."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "dialog_act": tf.string,
              "dialog_act_delexicalized": tf.string,
              "target_delexicalized": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://raw.githubusercontent.com/UFAL-DSG/cs_restaurant_dataset/master/train.json",
              "validation":
                  "https://raw.githubusercontent.com/UFAL-DSG/cs_restaurant_dataset/master/devel.json",
              "test":
                  "https://raw.githubusercontent.com/UFAL-DSG/cs_restaurant_dataset/master/test.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/cs_restaurants.zip",
          },
          citation=textwrap.dedent("""\
          @inproceedings{cs_restaurants,
            address = {Tokyo, Japan},
            title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},
            shorttitle = {Neural {Generation} for {Czech}},
            url = {https://www.aclweb.org/anthology/W19-8670/},
            urldate = {2019-10-18},
            booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
            author = {Dušek, Ondřej and Jurčíček, Filip},
            month = oct,
            year = {2019},
            pages = {563--574}
          }""")),
      GemConfig(
          name="dart",
          description=textwrap.dedent("""\
            DART is a large and open-domain structured DAta Record to Text
            generation corpus with high-quality sentence annotations with each
            input being a set of entity-relation triples following a
            tree-structured ontology."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "dart_id": tf.int32,
              "tripleset": tfds.features.Sequence(tf.string),
              "subtree_was_extended": tf.bool,
              "target_sources": tfds.features.Sequence(tf.string),
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://raw.githubusercontent.com/Yale-LILY/dart/master/data/v1.1.1/dart-v1.1.1-full-train.json",
              "validation":
                  "https://raw.githubusercontent.com/Yale-LILY/dart/master/data/v1.1.1/dart-v1.1.1-full-dev.json",
              "test":
                  "https://raw.githubusercontent.com/Yale-LILY/dart/master/data/v1.1.1/dart-v1.1.1-full-test.json",
          },
          citation=textwrap.dedent("""\
            @article{radev2020dart,
              title=Dart: Open-domain structured data record to text generation,
              author={Radev, Dragomir and Zhang, Rui and Rau, Amrit and Sivaprasad, Abhinand and Hsieh, Chiachun and Rajani, Nazneen Fatema and Tang, Xiangru and Vyas, Aadit and Verma, Neha and Krishna, Pranav and others},
              journal={arXiv preprint arXiv:2007.02871},
              year={2020}
            }
            }""")),
      GemConfig(
          name="e2e_nlg",
          description=textwrap.dedent("""\
            The E2E dataset is designed for a limited-domain data-to-text task
            -- generation of restaurant descriptions/recommendations based on up
            to 8 different attributes (name, area, price range etc.)"""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "meaning_representation": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/train-fixed.no-ol.csv",
              "validation":
                  "https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/devel-fixed.no-ol.csv",
              "test":
                  "https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/test-fixed.csv",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/e2e_nlg.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{e2e_cleaned,
              address = {Tokyo, Japan},
              title = {Semantic {Noise} {Matters} for {Neural} {Natural} {Language} {Generation}},
              url = {https://www.aclweb.org/anthology/W19-8652/},
              booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
              author = {Dušek, Ondřej and Howcroft, David M and Rieser, Verena},
              year = {2019},
              pages = {421--426},
            }""")),
      GemConfig(
          name="mlsum_de",
          description=textwrap.dedent("""\
            MLSum is a large-scale multiLingual summarization dataset. It is
            buillt from online news outlets, this split focusing on German."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "text": tf.string,
              "topic": tf.string,
              "url": tf.string,
              "title": tf.string,
              "date": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_train.zip",
              "validation":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_val.zip",
              "test":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/de_test.zip",
              "bad_ids":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_mlsum_bad_ids_fixed.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/mlsum_de.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{scialom-etal-2020-mlsum,
                title = "{MLSUM}: The Multilingual Summarization Corpus",
                author = {Scialom, Thomas  and Dray, Paul-Alexis  and Lamprier, Sylvain  and Piwowarski, Benjamin  and Staiano, Jacopo},
                booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
                year = {2020}
            }""")),
      GemConfig(
          name="mlsum_es",
          description=textwrap.dedent("""\
            MLSum is a large-scale multiLingual summarization dataset. It is
            buillt from online news outlets, this split focusing on
            Spanish."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "text": tf.string,
              "topic": tf.string,
              "url": tf.string,
              "title": tf.string,
              "date": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/es_train.zip",
              "validation":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/es_val.zip",
              "test":
                  "https://gitlab.lip6.fr/scialom/mlsum_data/-/raw/master/MLSUM/es_test.zip",
              "bad_ids":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_mlsum_bad_ids_fixed.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/mlsum_es.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{scialom-etal-2020-mlsum,
                title = "{MLSUM}: The Multilingual Summarization Corpus",
                author = {Scialom, Thomas  and Dray, Paul-Alexis  and Lamprier, Sylvain  and Piwowarski, Benjamin  and Staiano, Jacopo},
                booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
                year = {2020}
            }""")),
      GemConfig(
          name="schema_guided_dialog",
          description=textwrap.dedent("""\
            The Schema-Guided Dialogue (SGD) dataset contains 18K multi-domain
            task-oriented dialogues between a human and a virtual assistant,
            which covers 17 domains ranging from banks and events to media,
            calendar, travel, and weather."""),
          features=tfds.features.FeaturesDict({
              "gem_id":
                  tf.string,
              "gem_parent_id":
                  tf.string,
              "dialog_id":
                  tf.string,
              "turn_id":
                  tf.int32,
              "service":
                  tf.string,
              "prompt":
                  tf.string,
              "context":
                  tfds.features.Sequence(
                      tf.string),  # multiple references for validation.
              "dialog_acts":
                  tfds.features.Sequence({
                      "act": tfds.features.ClassLabel(names=_SGD_ACTS),
                      "slot": tf.string,
                      "values": tfds.features.Sequence(tf.string),
                  }),
              "target":
                  tf.string,  # single target for train.
              "references":
                  tfds.features.Sequence(
                      tf.string),  # multiple references for validation.
          }),
          data_urls={
              "data":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_sgd_context.zip",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/schema_guided_dialog.zip",
          },
          citation=textwrap.dedent("""\
            @article{rastogi2019towards,
              title={Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset},
              author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
              journal={arXiv preprint arXiv:1909.05855},
              year={2019}
            }""")),
      GemConfig(
          name="totto",
          description=textwrap.dedent("""\
            ToTTo is a Table-to-Text NLG task. The task is as follows:
            Given a Wikipedia table with row names, column names and table
            cells, with a subset of cells highlighted, generate a natural
            language description for the highlighted part of the table."""),
          features=tfds.features.FeaturesDict({
              "gem_id":
                  tf.string,
              "gem_parent_id":
                  tf.string,
              "totto_id":
                  tf.int32,
              "table_page_title":
                  tf.string,
              "table_webpage_url":
                  tf.string,
              "table_section_title":
                  tf.string,
              "table_section_text":
                  tf.string,
              "table":
                  tfds.features.Sequence(
                      tfds.features.Sequence({
                          "column_span": tf.int32,
                          "is_header": tf.bool,
                          "row_span": tf.int32,
                          "value": tf.string,
                      })),
              "highlighted_cells":
                  tfds.features.Sequence(tfds.features.Sequence(tf.int32)),
              "example_id":
                  tf.string,
              "overlap_subset":
                  tf.string,
              "sentence_annotations":
                  tfds.features.Sequence({
                      "original_sentence": tf.string,
                      "sentence_after_deletion": tf.string,
                      "sentence_after_ambiguity": tf.string,
                      "final_sentence": tf.string,
                  }),
              "target":
                  tf.string,  # single target for train.
              "references":
                  tfds.features.Sequence(
                      tf.string),  # multiple references for validation.
          }),
          data_urls={
              "data":
                  "https://storage.googleapis.com/totto/totto_data.zip",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/totto.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{parikh2020totto,
              title=ToTTo: A Controlled Table-To-Text Generation Dataset,
              author={Parikh, Ankur and Wang, Xuezhi and Gehrmann, Sebastian and Faruqui, Manaal and Dhingra, Bhuwan and Yang, Diyi and Das, Dipanjan},
              booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
              pages={1173--1186},
              year={2020}
            }""")),
      GemConfig(
          name="web_nlg_en",
          description=textwrap.dedent("""\
            WebNLG is a bi-lingual dataset (English, Russian) of parallel
            DBpedia triple sets and short texts that cover about 450 different
            DBpedia properties. The WebNLG data was originally created to
            promote the development of RDF verbalisers able to generate short
            text and to handle micro-planning."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "input": tfds.features.Sequence(tf.string),
              "category": tf.string,
              "webnlg_id": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_en_train.json",
              "validation":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_en_val.json",
              "test":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_en_test.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/web_nlg_en.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{gardent2017creating,
              author = 	"Gardent, Claire
                and Shimorina, Anastasia
                and Narayan, Shashi
                and Perez-Beltrachini, Laura",
              title = 	"Creating Training Corpora for NLG Micro-Planners",
              booktitle = 	"Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
              year = 	"2017",
              publisher = 	"Association for Computational Linguistics",
              pages = 	"179--188",
              location = 	"Vancouver, Canada",
              doi = 	"10.18653/v1/P17-1017",
              url = 	"http://www.aclweb.org/anthology/P17-1017"
            }""")),
      GemConfig(
          name="web_nlg_ru",
          description=textwrap.dedent("""\
            WebNLG is a bi-lingual dataset (English, Russian) of parallel
            DBpedia triple sets and short texts that cover about 450 different
            DBpedia properties. The WebNLG data was originally created to
            promote the development of RDF verbalisers able to generate short
            text and to handle micro-planning."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "input": tfds.features.Sequence(tf.string),
              "category": tf.string,
              "webnlg_id": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_ru_train.json",
              "validation":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_ru_val.json",
              "test":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_web_nlg/webnlg_ru_test.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/web_nlg_ru.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{gardent2017creating,
              author = 	"Gardent, Claire
                and Shimorina, Anastasia
                and Narayan, Shashi
                and Perez-Beltrachini, Laura",
              title = 	"Creating Training Corpora for NLG Micro-Planners",
              booktitle = 	"Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
              year = 	"2017",
              publisher = 	"Association for Computational Linguistics",
              pages = 	"179--188",
              location = 	"Vancouver, Canada",
              doi = 	"10.18653/v1/P17-1017",
              url = 	"http://www.aclweb.org/anthology/P17-1017"
            }""")),
      GemConfig(
          name="wiki_auto_asset_turk",
          description=textwrap.dedent("""\
            WikiAuto provides a set of aligned sentences from English Wikipedia
            and Simple English Wikipedia as a resource to train sentence
            simplification systems. ASSET and TURK are high-quality
            simplification datasets used for testing."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "source": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "train":
                  "https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_with_split/train.tsv",
              "validation":
                  "https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_with_split/valid.tsv",
              "test_turk":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_turk_detokenized.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/wiki_auto_asset_turk_train_valid.zip",
              "test_asset_0":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.0",
              "test_asset_1":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.1",
              "test_asset_2":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.2",
              "test_asset_3":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.3",
              "test_asset_4":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.4",
              "test_asset_5":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.5",
              "test_asset_6":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.6",
              "test_asset_7":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.7",
              "test_asset_8":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.8",
              "test_asset_9":
                  "https://github.com/facebookresearch/asset/raw/master/dataset/asset.test.simp.9",
          },
          citation=textwrap.dedent("""\
            @inproceedings{jiang-etal-2020-neural,
              title = "Neural {CRF} Model for Sentence Alignment in Text Simplification",
              author = "Jiang, Chao  and
                Maddela, Mounica  and
                Lan, Wuwei  and
                Zhong, Yang  and
                Xu, Wei",
              booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
              month = jul,
              year = "2020",
              address = "Online",
              publisher = "Association for Computational Linguistics",
              url = "https://www.aclweb.org/anthology/2020.acl-main.709",
              doi = "10.18653/v1/2020.acl-main.709",
              pages = "7943--7960",
          }""")),
      GemConfig(
          name="xsum",
          description=textwrap.dedent("""\
            The dataset is for the task of abstractive summarization in its
            extreme form, its about summarizing a document in a single
            sentence."""),
          features=tfds.features.FeaturesDict({
              "gem_id": tf.string,
              "gem_parent_id": tf.string,
              "xsum_id": tf.string,
              "document": tf.string,
              "target": tf.string,  # single target for train.
              "references": tfds.features.Sequence(
                  tf.string),  # multiple references for validation.
          }),
          data_urls={
              "data":
                  "http://bollin.inf.ed.ac.uk/public/direct/XSUM-EMNLP18-Summary-Data-Original.tar.gz",
              "splits":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_xsum_confidence_0.8.json",
              "challenge_set":
                  "https://storage.googleapis.com/huggingface-nlp/datasets/gem/gem_challenge_sets/xsum.zip",
          },
          citation=textwrap.dedent("""\
            @inproceedings{Narayan2018dont,
              author = "Shashi Narayan and Shay B. Cohen and Mirella Lapata",
              title = "Don't Give Me the Details, Just the Summary! {T}opic-Aware Convolutional Neural Networks for Extreme Summarization",
              booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing ",
              year = "2018",
              address = "Brussels, Belgium",
            }"""))
  ]
  # Add all the WikiLingua versions.
  for version_name, data_url in _WIKI_LINGUA_LANGS.items():
    ln = version_name.split("_")[-1]
    BUILDER_CONFIGS.append(
        GemConfig(
            name=version_name,
            description=textwrap.dedent("""\
                Wikilingua is a large-scale, multilingual dataset for the evaluation
                of cross-lingual abstractive summarization systems.."""),
            features=tfds.features.FeaturesDict({
                "gem_id":
                    tf.string,
                "gem_parent_id":
                    tf.string,
                "source":
                    tf.string,
                "target":
                    tf.string,  # single target for train.
                "source_aligned":
                    tfds.features.Translation(languages=[ln, "en"]
                                             ),  # parallel in English.
                "target_aligned":
                    tfds.features.Translation(languages=[ln, "en"]),
                "references":
                    tfds.features.Sequence(
                        tf.string),  # multiple references for validation.
            }),
            data_urls={"data": data_url},
            citation=textwrap.dedent("""\
                @inproceedings{ladhak-wiki-2020,
                title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
                author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
                booktitle={Findings of EMNLP, 2020},
                year={2020}
                }""")))

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(self.builder_config.features),
        homepage=_URL,
        citation=self.builder_config.citation + "\n" + _CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    files = dl_manager.download_and_extract(self.builder_config.data_urls)
    if self.builder_config.name == "common_gen":
      challenge_sets = [
          ("challenge_train_sample", "train_common_gen_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_common_gen_RandomSample500.json"),
          ("challenge_test_scramble",
           "test_common_gen_ScrambleInputStructure500.json"),
      ]

      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))

      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["data"], "commongen.train.jsonl"),
                  "set_name":
                      "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["data"], "commongen.dev.jsonl"),
                  "set_name":
                      "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["data"], "commongen.test_noref.jsonl"),
                  "set_name":
                      "test",
              },
          ),
      ] + challenge_splits

    elif self.builder_config.name == "cs_restaurants":
      challenge_sets = [
          ("challenge_train_sample",
           "train_cs_restaurants_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_cs_restaurants_RandomSample500.json"),
          ("challenge_test_scramble",
           "test_cs_restaurants_ScrambleInputStructure500.json"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))

      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["train"],
                  "set_name": "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["validation"],
                  "set_name": "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": files["test"],
                  "set_name": "test",
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name == "dart":
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["train"],
                  "set_name": "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["validation"],
                  "set_name": "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": files["test"],
                  "set_name": "test",
              },
          ),
      ]
    elif self.builder_config.name == "e2e_nlg":
      challenge_sets = [
          ("challenge_train_sample", "train_e2e_nlg_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_e2e_nlg_RandomSample500.json"),
          ("challenge_test_scramble",
           "test_e2e_nlg_ScrambleInputStructure500.json"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["train"],
                  "set_name": "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["validation"],
                  "set_name": "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": files["test"],
                  "set_name": "test",
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name.startswith("mlsum"):
      # Can be either _de or _es.
      lang = self.builder_config.name.split("_")[1]
      challenge_sets = [
          ("challenge_train_sample",
           f"train_mlsum_{lang}_RandomSample500.json"),
          ("challenge_validation_sample",
           f"validation_mlsum_{lang}_RandomSample500.json"),
          ("challenge_test_covid", f"{lang}_test_covid19_cleaned.jsonl"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["train"], lang + "_train.jsonl"),
                  "set_name":
                      "train",
                  "lang":
                      lang,
                  "filepaths":
                      files["bad_ids"]
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["validation"], lang + "_val.jsonl"),
                  "set_name":
                      "validation",
                  "lang":
                      lang,
                  "filepaths":
                      files["bad_ids"]
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": os.path.join(files["test"], lang + "_test.jsonl"),
                  "set_name": "test",
                  "lang": lang,
                  "filepaths": files["bad_ids"]
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name == "schema_guided_dialog":
      challenge_sets = [
          ("challenge_train_sample",
           "train_schema_guided_dialog_RandomSample500_reformatted.json"),
          ("challenge_validation_sample",
           "validation_schema_guided_dialog_RandomSample500_reformatted.json"),
          ("challenge_test_backtranslation",
           "test_schema_guided_dialog_BackTranslation500_reformatted.json"),
          (
              "challenge_test_bfp02",
              "test_schema_guided_dialog_ButterFingersPerturbation_p=0.02_500_reformatted.json",
          ),
          (
              "challenge_test_bfp05",
              "test_schema_guided_dialog_ButterFingersPerturbation_p=0.05_500_reformatted.json",
          ),
          ("challenge_test_nopunc",
           "test_schema_guided_dialog_WithoutPunctuation500_reformatted.json"),
          ("challenge_test_scramble",
           "test_schema_guided_dialog_ScrambleInputStructure500_reformatted.json"
          ),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))

      generators = []
      for tfds_spl, spl in zip(
          [tfds.Split.TRAIN, tfds.Split.VALIDATION, tfds.Split.TEST],
          ["train", "validation", "test"]):
        generators.append(
            tfds.core.SplitGenerator(
                name=tfds_spl,
                gen_kwargs={
                    "filepath": os.path.join(files["data"], "gem_sgd.json"),
                    "set_name": spl
                }))
      return generators + challenge_splits
    elif self.builder_config.name == "totto":
      challenge_sets = [
          ("challenge_train_sample", "train_totto_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_totto_RandomSample500.json"),
          ("challenge_test_scramble",
           "test_totto_ScrambleInputStructure500.json"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))

      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["data"],
                                   "totto_data/totto_train_data.jsonl"),
                  "set_name":
                      "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath":
                      os.path.join(files["data"],
                                   "totto_data/totto_dev_data.jsonl"),
                  "set_name":
                      "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath":
                      os.path.join(
                          files["data"],
                          "totto_data/unlabeled_totto_test_data.jsonl"),
                  "set_name":
                      "test",
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name.startswith("web_nlg"):
      # Can be either _en or _ru.
      ln = self.builder_config.name.split("_")[2]
      challenge_sets = [
          ("challenge_train_sample",
           f"train_web_nlg_{ln}_RandomSample500.json"),
          ("challenge_validation_sample",
           f"validation_web_nlg_{ln}_RandomSample500.json"),
          ("challenge_test_scramble",
           f"test_web_nlg_{ln}_ScrambleInputStructure500.json"),
      ]
      if ln == "en":
        challenge_sets += [("challenge_test_numbers",
                            f"test_web_nlg_{ln}_replace_numbers_500.json")]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["train"],
                  "set_name": "train"
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["validation"],
                  "set_name": "validation"
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": files["test"],
                  "set_name": "test"
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name == "wiki_auto_asset_turk":
      challenge_sets = [
          ("challenge_train_sample",
           "train_wiki_auto_asset_turk_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_wiki_auto_asset_turk_RandomSample500.json"),
          ("challenge_test_asset_backtranslation",
           "test_asset_wiki_auto_asset_turk_BackTranslation.json"),
          (
              "challenge_test_asset_bfp02",
              "test_asset_wiki_auto_asset_turk_ButterFingersPerturbation_p=0.02.json",
          ),
          (
              "challenge_test_asset_bfp05",
              "test_asset_wiki_auto_asset_turk_ButterFingersPerturbation_p=0.05.json",
          ),
          ("challenge_test_asset_nopunc",
           "test_asset_wiki_auto_asset_turk_WithoutPunctuation.json"),
          ("challenge_test_turk_backtranslation",
           "detok_test_turk_wiki_auto_asset_turk_BackTranslation.json"),
          (
              "challenge_test_turk_bfp02",
              "detok_test_turk_wiki_auto_asset_turk_ButterFingersPerturbation_p=0.02.json",
          ),
          (
              "challenge_test_turk_bfp05",
              "detok_test_turk_wiki_auto_asset_turk_ButterFingersPerturbation_p=0.05.json",
          ),
          ("challenge_test_turk_nopunc",
           "detok_test_turk_wiki_auto_asset_turk_WithoutPunctuation.json"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["train"],
                  "set_name": "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["validation"],
                  "set_name": "validation",
              },
          ),
          tfds.core.SplitGenerator(
              name="test_asset",
              gen_kwargs={
                  "filepath":
                      "",
                  "set_name":
                      "test_asset",
                  "filepaths":
                      [files["test_asset_" + str(i)] for i in range(10)],
              },
          ),
          tfds.core.SplitGenerator(
              name="test_turk",
              gen_kwargs={
                  "filepath": files["test_turk"],
                  "set_name": "test_turk",
              },
          ),
      ] + challenge_splits
    elif self.builder_config.name.startswith("wiki_lingua"):
      lang_name = self.builder_config.name.split("_")[-2]
      lang = self.builder_config.name.split("_")[-1]
      base_dir = os.path.join(files["data"], lang_name)
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": base_dir,
                  "set_name": "train",
                  "lang": lang,
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": base_dir,
                  "set_name": "val",
                  "lang": lang,
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": base_dir,
                  "set_name": "test",
                  "lang": lang,
              },
          ),
      ]
    elif self.builder_config.name == "xsum":
      challenge_sets = [
          ("challenge_train_sample", "train_xsum_RandomSample500.json"),
          ("challenge_validation_sample",
           "validation_xsum_RandomSample500.json"),
          ("challenge_test_backtranslation",
           "test_xsum_BackTranslation500.json"),
          ("challenge_test_bfp_02",
           "test_xsum_ButterFingersPerturbation_p=0.02_500.json"),
          ("challenge_test_bfp_05",
           "test_xsum_ButterFingersPerturbation_p=0.05_500.json"),
          ("challenge_test_nopunc", "test_xsum_WithoutPunctuation500.json"),
          ("challenge_test_covid", "en_test_covid19.jsonl"),
      ]
      challenge_splits = []
      for challenge_split, filename in challenge_sets:
        challenge_splits.append(
            tfds.core.SplitGenerator(
                name=challenge_split,
                gen_kwargs={
                    "filepath":
                        os.path.join(files["challenge_set"],
                                     self.builder_config.name, filename),
                    "set_name":
                        challenge_split,
                },
            ))
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "filepath": files["splits"],
                  "set_name": "train",
                  "filepaths": os.path.join(files["data"], "bbc-summary-data"),
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "filepath": files["splits"],
                  "set_name": "validation",
                  "filepaths": os.path.join(files["data"], "bbc-summary-data"),
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "filepath": files["splits"],
                  "set_name": "test",
                  "filepaths": os.path.join(files["data"], "bbc-summary-data"),
              },
          ),
      ] + challenge_splits

  def _generate_examples(self, filepath, set_name, filepaths=None, lang=None):
    """Yields examples."""
    if self.builder_config.name == "common_gen":
      with tf.io.gfile.GFile(filepath) as f:
        if set_name.startswith("challenge"):
          exples = json.load(f)
          if isinstance(exples, dict):
            assert len(exples) == 1, "multiple entries found"
            exples = list(exples.values())[0]
          for id_, exple in enumerate(exples):
            if not exple:
              continue
            exple["gem_parent_id"] = exple["gem_id"]
            exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            yield id_, exple
        else:
          id_ = -1
          i = -1
          for row in f:
            row = row.replace(", }", "}")  # Fix possible JSON format error.
            data = json.loads(row)
            concepts = [word for word in data["concept_set"].split("#")]
            if set_name == "train":
              i += 1
              for scene in data["scene"]:
                id_ += 1
                yield id_, {
                    "gem_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "gem_parent_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "concept_set_id":
                        i,
                    "concepts":
                        concepts,
                    "target":
                        scene,
                    "references": [],
                }
            else:
              id_ += 1
              yield id_, {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "concept_set_id":
                      id_,
                  "concepts":
                      concepts,
                  "target":
                      "" if set_name == "test" else data["scene"][0],
                  "references": [] if set_name == "test" else data["scene"],
              }
    elif self.builder_config.name == "cs_restaurants":
      with tf.io.gfile.GFile(filepath) as f:
        if set_name.startswith("challenge"):
          exples = json.load(f)
          if isinstance(exples, dict):
            assert len(exples) == 1, "multiple entries found"
            exples = list(exples.values())[0]
          for id_, exple in enumerate(exples):
            if not exple:
              continue
            exple["gem_parent_id"] = exple["gem_id"]
            exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            yield id_, exple
        else:
          data = json.load(f)
          for id_, instance in enumerate(data):
            yield id_, {
                "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "dialog_act": instance["da"],
                "dialog_act_delexicalized": instance["delex_da"],
                "target": instance["text"],
                "target_delexicalized": instance["delex_text"],
                "references": [] if set_name == "train" else [instance["text"]],
            }
    elif self.builder_config.name == "dart":
      with tf.io.gfile.GFile(filepath) as f:
        data = json.loads(f.read())
        id_ = -1
        i = -1
        for example in data:
          flat_tripleset = [" ".join(ex) for ex in example["tripleset"]]
          if set_name == "train":
            i += 1
            for annotation in example["annotations"]:
              id_ += 1
              yield id_, {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "dart_id":
                      i,
                  "tripleset":
                      flat_tripleset,
                  "subtree_was_extended":
                      example.get("subtree_was_extended",
                                  None),  # some are missing.
                  "target_sources": [
                      annotation["source"]
                      for annotation in example["annotations"]
                  ],
                  "target":
                      annotation["text"],
                  "references": [],
              }
          else:
            id_ += 1
            yield id_, {
                "gem_id":
                    f"{self.builder_config.name}-{set_name}-{id_}",
                "gem_parent_id":
                    f"{self.builder_config.name}-{set_name}-{id_}",
                "dart_id":
                    id_,
                "tripleset":
                    flat_tripleset,
                "subtree_was_extended":
                    example.get("subtree_was_extended",
                                None),  # some are missing.
                "target_sources": [
                    annotation["source"]
                    for annotation in example["annotations"]
                ],
                "target":
                    example["annotations"][0]["text"]
                    if example["annotations"] else "",
                "references": [
                    annotation["text"] for annotation in example["annotations"]
                ],
            }
    elif self.builder_config.name == "e2e_nlg":
      with tf.io.gfile.GFile(filepath) as f:
        if set_name.startswith("challenge"):
          exples = json.load(f)
          if isinstance(exples, dict):
            assert len(exples) == 1, "multiple entries found"
            exples = list(exples.values())[0]
          for id_, exple in enumerate(exples):
            if not exple:
              continue
            exple["gem_parent_id"] = exple["gem_id"]
            exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            yield id_, exple
        else:
          reader = csv.DictReader(f)
          for id_, example in enumerate(reader):
            yield id_, {
                "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "meaning_representation": example["mr"],
                "target": example["ref"],
                "references": [] if set_name == "train" else [example["ref"]],
            }
    elif self.builder_config.name.startswith("mlsum"):
      if set_name in ["train", "validation", "test", "challenge_test_covid"]:
        if set_name == "challenge_test_covid":
          bad_ids = {}
        else:
          bad_ids_dct = json.load(tf.io.gfile.GFile(filepaths))
          bad_ids = dict((bad_url, True)
                         for _, bad_url in bad_ids_dct[f"{lang}-{set_name}"])
        with tf.io.gfile.GFile(filepath) as f:
          id_ = -1
          for line in f:
            data = json.loads(line)
            if data["url"] in bad_ids:
              continue
            else:
              id_ += 1
              yield id_, {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "text":
                      data["text"],
                  "target":
                      data["summary"],
                  "references": []
                                if set_name == "train" else [data["summary"]],
                  "topic":
                      data["topic"],
                  "url":
                      data["url"],
                  "title":
                      data["title"],
                  "date":
                      data["date"],
              }
      else:
        exples = json.load(tf.io.gfile.GFile(filepath))
        if isinstance(exples, dict):
          assert len(exples) == 1, "multiple entries found"
          exples = list(exples.values())[0]
        for id_, exple in enumerate(exples):
          if not exple:
            continue
          exple["gem_parent_id"] = exple["gem_id"]
          exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
          yield id_, exple
    elif self.builder_config.name == "schema_guided_dialog":
      if "challenge" in set_name:
        exples = json.load(tf.io.gfile.GFile(filepath))
        if isinstance(exples, dict):
          assert len(exples) == 1, "multiple entries found"
          exples = list(exples.values())[0]
        for id_, exple in enumerate(exples):
          if not exple:
            continue
          exple["gem_parent_id"] = exple["gem_id"]
          exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
          yield id_, exple
      else:
        examples = json.load(tf.io.gfile.GFile(filepath))[set_name]
        for id_, example in enumerate(examples):
          dialog_acts = []
          for act_id, slot, values in example["da"]:
            dialog_acts.append({
                "act": act_id,
                "slot": slot,
                "values": values,
            })
          yield id_, {
              "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
              "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
              "dialog_acts": dialog_acts,
              "context": example["context"],
              "dialog_id": example["dialog_id"],
              "service": example["service"],
              "turn_id": example["turn_ix"],
              "prompt": example["prompt"],
              "target": example["target"],
              "references": [] if set_name == "train" else [example["target"]],
          }
    elif self.builder_config.name == "totto":
      if "challenge" in set_name:
        exples = json.load(tf.io.gfile.GFile(filepath))
        if isinstance(exples, dict):
          assert len(exples) == 1, "multiple entries found"
          exples = list(exples.values())[0]
        for id_, exple in enumerate(exples):
          if not exple:
            continue
          exple["gem_parent_id"] = exple["gem_id"]
          exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
          yield id_, exple
      else:
        with tf.io.gfile.GFile(filepath) as json_file:
          json_list = list(json_file)
        id_ = -1
        i = -1
        for json_str in json_list:
          result = json.loads(json_str)
          if set_name == "train":
            i += 1
            for sentence in result["sentence_annotations"]:
              id_ += 1
              response = {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "totto_id":
                      i,
                  "table_page_title":
                      result["table_page_title"],
                  "table_webpage_url":
                      result["table_webpage_url"],
                  "table_section_title":
                      result["table_section_title"],
                  "table_section_text":
                      result["table_section_text"],
                  "table":
                      result["table"],
                  "highlighted_cells":
                      result["highlighted_cells"],
                  "example_id":
                      str(result["example_id"]),
                  "overlap_subset":
                      "none",
                  "sentence_annotations": [sentence],
                  "references": [],
                  "target":
                      sentence["final_sentence"],
              }
              yield id_, response
          else:
            id_ += 1
            response = {
                "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "totto_id": id_,
                "table_page_title": result["table_page_title"],
                "table_webpage_url": result["table_webpage_url"],
                "table_section_title": result["table_section_title"],
                "table_section_text": result["table_section_text"],
                "table": result["table"],
                "highlighted_cells": result["highlighted_cells"],
                "example_id": str(result["example_id"]),
                "overlap_subset": str(result["overlap_subset"]),
            }
            response[
                "sentence_annotations"] = [] if set_name == "test" else result[
                    "sentence_annotations"]
            response["references"] = [
                sentence["final_sentence"]
                for sentence in response["sentence_annotations"]
            ]
            if response["references"]:
              response["target"] = response["references"][0]
            else:
              response["target"] = ""
            yield id_, response
    elif self.builder_config.name.startswith("web_nlg"):
      if "challenge" in set_name:
        exples = json.load(tf.io.gfile.GFile(filepath))
        if isinstance(exples, dict):
          assert len(exples) == 1, "multiple entries found"
          exples = list(exples.values())[0]
        for id_, exple in enumerate(exples):
          if not exple:
            continue
          exple["gem_parent_id"] = exple["gem_id"]
          exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
          yield id_, exple
      else:
        with tf.io.gfile.GFile(filepath) as f:
          examples = json.load(f)
          id_ = -1
          for example in examples["values"]:
            if set_name == "train":
              for target in example["target"]:
                id_ += 1
                yield id_, {
                    "gem_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "gem_parent_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "input":
                        example["input"],
                    "target":
                        target,
                    "references": []
                                  if set_name == "train" else example["target"],
                    "category":
                        example["category"],
                    "webnlg_id":
                        example["webnlg-id"],
                }
            else:
              id_ += 1
              yield id_, {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "input":
                      example["input"],
                  "target":
                      example["target"][0] if example["target"] else "",
                  "references":
                      example["target"],
                  "category":
                      example["category"],
                  "webnlg_id":
                      example["webnlg-id"],
              }
    elif self.builder_config.name == "wiki_auto_asset_turk":
      if set_name in ["train", "validation"]:
        keys = [
            "source",
            "target",
        ]
        with tf.io.gfile.GFile(filepath) as f:
          for id_, line in enumerate(f):
            values = line.strip().split("\t")
            assert len(
                values) == 2, f"Not enough fields in ---- {line} --- {values}"
            example = dict([(k, val) for k, val in zip(keys, values)])
            example["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            example[
                "gem_parent_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            example["references"] = [] if set_name == "train" else [
                example["target"]
            ]
            yield id_, example
      elif set_name == "test_turk":
        examples = json.load(tf.io.gfile.GFile(filepath))
        for id_, example in enumerate(examples):
          example["gem_parent_id"] = example["gem_id"]
          for k in ["source_id", "target_id"]:
            if k in example:
              del example[k]
          yield id_, example
      elif set_name == "test_asset":
        files = [tf.io.gfile.GFile(f_name) for f_name in filepaths]
        for id_, lines in enumerate(zip(*files)):
          yield id_, {
              "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
              "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
              "target": lines[1].strip(),
              "source": lines[0].strip(),
              "references": [line.strip() for line in lines[1:]],
          }
      else:
        exples = json.load(tf.io.gfile.GFile(filepath))
        if isinstance(exples, dict):
          assert len(exples) == 1, "multiple entries found"
          exples = list(exples.values())[0]
        for id_, exple in enumerate(exples):
          exple["gem_parent_id"] = exple["gem_id"]
          exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
          for k in ["source_id", "target_id"]:
            if k in exple:
              del exple[k]
          yield id_, exple
    elif self.builder_config.name.startswith("wiki_lingua"):
      with tf.io.gfile.GFile(os.path.join(filepath,
                                          f"{set_name}.src.{lang}")) as f_in_ln:
        with tf.io.gfile.GFile(os.path.join(filepath,
                                            f"{set_name}.src.en")) as f_in_en:
          with tf.io.gfile.GFile(
              os.path.join(filepath, f"{set_name}.tgt.{lang}")) as f_out_ln:
            with tf.io.gfile.GFile(
                os.path.join(filepath, f"{set_name}.tgt.en")) as f_out_en:
              for id_, (src_ln, src_en, tgt_ln, tgt_en) in enumerate(
                  zip(f_in_ln, f_in_en, f_out_ln, f_out_en)):
                yield id_, {
                    "gem_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "gem_parent_id":
                        f"{self.builder_config.name}-{set_name}-{id_}",
                    "source_aligned": {
                        lang: src_ln.strip(),
                        "en": src_en.strip()
                    },
                    "target_aligned": {
                        lang: tgt_ln.strip(),
                        "en": tgt_en.strip()
                    },
                    "source":
                        src_ln.strip(),
                    "target":
                        tgt_en.strip(),
                    "references": []
                                  if set_name == "train" else [tgt_en.strip()],
                }
    elif self.builder_config.name == "xsum":
      if "challenge" in set_name:
        if "covid" in set_name:
          with tf.io.gfile.GFile(filepath) as f:
            id_ = -1
            for line in f:
              data = json.loads(line)
              id_ += 1
              yield id_, {
                  "gem_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "gem_parent_id":
                      f"{self.builder_config.name}-{set_name}-{id_}",
                  "xsum_id":
                      data["url"],
                  "document":
                      data["text"],
                  "target":
                      data["summary"],
                  "references": []
                                if set_name == "train" else [data["summary"]],
              }
        else:
          exples = json.load(tf.io.gfile.GFile(filepath))
          if isinstance(exples, dict):
            assert len(exples) == 1, "multiple entries found"
            exples = list(exples.values())[0]
          for id_, exple in enumerate(exples):
            exple["gem_parent_id"] = exple["gem_id"]
            exple["gem_id"] = f"{self.builder_config.name}-{set_name}-{id_}"
            yield id_, exple
      else:
        with tf.io.gfile.GFile(filepath) as f:
          split_ids = json.load(f)
        for id_, i in enumerate(split_ids[set_name]):
          with tf.io.gfile.GFile(os.path.join(filepaths, i + ".summary")) as f:
            text = "".join([
                line for line in f.readlines()
                if line not in _XSUM_REMOVE_LINES and line.strip()
            ])
            segs = text.split("[SN]")
            yield id_, {
                "gem_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "gem_parent_id": f"{self.builder_config.name}-{set_name}-{id_}",
                "xsum_id": i,
                "document": segs[8].strip(),
                "target": segs[6].strip(),
                "references": [] if set_name == "train" else [segs[6].strip()],
            }
