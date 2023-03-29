# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""UnifiedQA datasets."""

from __future__ import annotations

import csv
import textwrap

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
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
"""

_HOMEPAGE = 'https://github.com/allenai/unifiedqa'

_CITATION = """@inproceedings{khashabi-etal-2020-unifiedqa,
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
"""

_URL_BASE = 'https://storage.googleapis.com/unifiedqa/data'


class UnifiedQAConfig(tfds.core.BuilderConfig):
  """BuilderConfig for UnifiedQA."""

  def __init__(self, *, features, data_urls, citation, header=False, **kwargs):
    """BuilderConfig for UnifiedQA.

    Args:
      features: `tfds.features.FeaturesDict`, specific feature dict for the
        dataset.
      data_urls: `dict`, urls to download the files from
      citation: `string`, citation for the data set
      header: `bool`, whether the data files have a header
      **kwargs: keyword arguments forwarded to super.
    """
    super(UnifiedQAConfig, self).__init__(**kwargs)
    self.features = features
    self.data_urls = data_urls
    self.citation = citation
    self.header = header


class UnifiedQA(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for UnifiedQA datasets."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  DEFAULT_FEATURES = tfds.features.FeaturesDict({
      'input': np.str_,
      'output': np.str_,
  })
  BUILDER_CONFIGS = [
      UnifiedQAConfig(
          name='ai2_science_elementary',
          description=textwrap.dedent(
              """\
          The AI2 Science Questions dataset consists of questions used in
          student assessments in the United States across elementary and middle
          school grade levels. Each question is 4-way multiple choice format and
          may or may not include a diagram element. This set consists of
          questions used for elementary school grade levels.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/ai2_science_elementary/train.tsv',
              'validation': f'{_URL_BASE}/ai2_science_elementary/dev.tsv',
              'test': f'{_URL_BASE}/ai2_science_elementary/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          http://data.allenai.org/ai2-science-questions
          """
          ),
      ),
      UnifiedQAConfig(
          name='ai2_science_middle',
          description=textwrap.dedent(
              """\
          The AI2 Science Questions dataset consists of questions used in
          student assessments in the United States across elementary and middle
          school grade levels. Each question is 4-way multiple choice format and
          may or may not include a diagram element. This set consists of
          questions used for middle school grade levels.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/ai2_science_middle/train.tsv',
              'validation': f'{_URL_BASE}/ai2_science_middle/dev.tsv',
              'test': f'{_URL_BASE}/ai2_science_middle/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          http://data.allenai.org/ai2-science-questions
          """
          ),
      ),
      UnifiedQAConfig(
          name='ambigqa',
          description=textwrap.dedent(
              """\
          AmbigQA is an open-domain question answering task which involves
          finding every plausible answer, and then rewriting the question for
          each one to resolve the ambiguity.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/ambigqa/train.tsv',
              'validation': f'{_URL_BASE}/ambigqa/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_easy',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "easy" questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_easy/train.tsv',
              'validation': f'{_URL_BASE}/arc_easy/dev.tsv',
              'test': f'{_URL_BASE}/arc_easy/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_easy_dev',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "easy" questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_easy_dev/train.tsv',
              'validation': f'{_URL_BASE}/arc_easy_dev/dev.tsv',
              'test': f'{_URL_BASE}/arc_easy_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_easy_with_ir',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "easy" questions. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_easy_with_ir/train.tsv',
              'validation': f'{_URL_BASE}/arc_easy_with_ir/dev.tsv',
              'test': f'{_URL_BASE}/arc_easy_with_ir/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_easy_with_ir_dev',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "easy" questions. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_easy_with_ir_dev/train.tsv',
              'validation': f'{_URL_BASE}/arc_easy_with_ir_dev/dev.tsv',
              'test': f'{_URL_BASE}/arc_easy_with_ir_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_hard',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "hard" questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_hard/train.tsv',
              'validation': f'{_URL_BASE}/arc_hard/dev.tsv',
              'test': f'{_URL_BASE}/arc_hard/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_hard_dev',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "hard" questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_hard_dev/train.tsv',
              'validation': f'{_URL_BASE}/arc_hard_dev/dev.tsv',
              'test': f'{_URL_BASE}/arc_hard_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_hard_with_ir',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "hard" questions. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_hard_with_ir/train.tsv',
              'validation': f'{_URL_BASE}/arc_hard_with_ir/dev.tsv',
              'test': f'{_URL_BASE}/arc_hard_with_ir/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='arc_hard_with_ir_dev',
          description=textwrap.dedent(
              """\
          This dataset consists of genuine grade-school level, multiple-choice
          science questions, assembled to encourage research in advanced
          question-answering. The dataset is partitioned into a Challenge Set
          and an Easy Set, where the former contains only questions answered
          incorrectly by both a retrieval-based algorithm and a word
          co-occurrence algorithm. This set consists of "hard" questions. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/arc_hard_with_ir_dev/train.tsv',
              'validation': f'{_URL_BASE}/arc_hard_with_ir_dev/dev.tsv',
              'test': f'{_URL_BASE}/arc_hard_with_ir_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{clark2018think,
              title={Think you have solved question answering? try arc, the ai2 reasoning challenge},
              author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
              journal={arXiv preprint arXiv:1803.05457},
              year={2018}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='boolq',
          description=textwrap.dedent(
              """\
          BoolQ is a question answering dataset for yes/no questions. These
          questions are naturally occurring ---they are generated in unprompted
          and unconstrained settings. Each example is a triplet of (question,
          passage, answer), with the title of the page as optional additional
          context. The text-pair classification setup is similar to existing
          natural language inference tasks.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/boolq/train.tsv',
              'validation': f'{_URL_BASE}/boolq/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='boolq_np',
          description=textwrap.dedent(
              """\
          BoolQ is a question answering dataset for yes/no questions. These
          questions are naturally occurring ---they are generated in unprompted
          and unconstrained settings. Each example is a triplet of (question,
          passage, answer), with the title of the page as optional additional
          context. The text-pair classification setup is similar to existing
          natural language inference tasks. This version adds natural
          perturbations to the original version.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/boolq_np/train.tsv',
              'validation': f'{_URL_BASE}/boolq_np/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='commonsenseqa',
          description=textwrap.dedent(
              """\
          CommonsenseQA is a new multiple-choice question answering dataset that
          requires different types of commonsense knowledge to predict the
          correct answers . It contains questions with one correct answer and
          four distractor answers.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/commonsenseqa/train.tsv',
              'validation': f'{_URL_BASE}/commonsenseqa/dev.tsv',
              'test': f'{_URL_BASE}/commonsenseqa/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='commonsenseqa_test',
          description=textwrap.dedent(
              """\
          CommonsenseQA is a new multiple-choice question answering dataset that
          requires different types of commonsense knowledge to predict the
          correct answers . It contains questions with one correct answer and
          four distractor answers.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/commonsenseqa_test/train.tsv',
              'validation': f'{_URL_BASE}/commonsenseqa_test/dev.tsv',
              'test': f'{_URL_BASE}/commonsenseqa_test/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='contrast_sets_boolq',
          description=textwrap.dedent(
              """\
          BoolQ is a question answering dataset for yes/no questions. These
          questions are naturally occurring ---they are generated in unprompted
          and unconstrained settings. Each example is a triplet of (question,
          passage, answer), with the title of the page as optional additional
          context. The text-pair classification setup is similar to existing
          natural language inference tasks. This version uses contrast sets.
          These evaluation sets are expert-generated perturbations that deviate
          from the patterns common in the original dataset.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/contrast_sets_boolq/train.tsv',
              'validation': f'{_URL_BASE}/contrast_sets_boolq/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
          header=True,
      ),
      UnifiedQAConfig(
          name='contrast_sets_drop',
          description=textwrap.dedent(
              """\
          DROP is a crowdsourced, adversarially-created QA benchmark, in which a
          system must resolve references in a question, perhaps to multiple
          input positions, and perform discrete operations over them (such as
          addition, counting, or sorting). These operations require a much more
          comprehensive understanding of the content of paragraphs than what was
          necessary for prior datasets. This version uses contrast sets. These
          evaluation sets are expert-generated perturbations that deviate from
          the patterns common in the original dataset.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/contrast_sets_drop/train.tsv',
              'validation': f'{_URL_BASE}/contrast_sets_drop/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='contrast_sets_quoref',
          description=textwrap.dedent(
              """\
          This dataset tests the coreferential reasoning capability of reading
          comprehension systems. In this span-selection benchmark containing
          questions over paragraphs from Wikipedia, a system must resolve hard
          coreferences before selecting the appropriate span(s) in the
          paragraphs for answering questions. This version uses contrast sets.
          These evaluation sets are expert-generated perturbations that deviate
          from the patterns common in the original dataset.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/contrast_sets_quoref/train.tsv',
              'validation': f'{_URL_BASE}/contrast_sets_quoref/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{dasigi-etal-2019-quoref,
              title = "{Q}uoref: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning",
              author = "Dasigi, Pradeep  and
                Liu, Nelson F.  and
                Marasovi{\'c}, Ana  and
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='contrast_sets_ropes',
          description=textwrap.dedent(
              """\
          This dataset tests a system's ability to apply knowledge from a
          passage of text to a new situation. A system is presented a background
          passage containing a causal or qualitative relation(s) (e.g., "animal
          pollinators increase efficiency of fertilization in flowers"), a novel
          situation that uses this background, and questions that require
          reasoning about effects of the relationships in the background passage
          in the context of the situation. This version uses contrast sets.
          These evaluation sets are expert-generated perturbations that deviate
          from the patterns common in the original dataset.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/contrast_sets_ropes/train.tsv',
              'validation': f'{_URL_BASE}/contrast_sets_ropes/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='drop',
          description=textwrap.dedent(
              """\
          DROP is a crowdsourced, adversarially-created QA benchmark, in which a
          system must resolve references in a question, perhaps to multiple
          input positions, and perform discrete operations over them (such as
          addition, counting, or sorting). These operations require a much more
          comprehensive understanding of the content of paragraphs than what was
          necessary for prior datasets.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/drop/train.tsv',
              'validation': f'{_URL_BASE}/drop/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='mctest',
          description=textwrap.dedent(
              """\
          MCTest requires machines to answer multiple-choice reading
          comprehension questions about fictional stories, directly tackling the
          high-level goal of open-domain machine comprehension. Reading
          comprehension can test advanced abilities such as causal reasoning and
          understanding the world, yet, by being multiple-choice, still provide
          a clear metric. By being fictional, the answer typically can be found
          only in the story itself. The stories and questions are also carefully
          limited to those a young child would understand, reducing the world
          knowledge that is required for the task.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/mctest/train.tsv',
              'validation': f'{_URL_BASE}/mctest/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='mctest_corrected_the_separator',
          description=textwrap.dedent(
              """\
          MCTest requires machines to answer multiple-choice reading
          comprehension questions about fictional stories, directly tackling the
          high-level goal of open-domain machine comprehension. Reading
          comprehension can test advanced abilities such as causal reasoning and
          understanding the world, yet, by being multiple-choice, still provide
          a clear metric. By being fictional, the answer typically can be found
          only in the story itself. The stories and questions are also carefully
          limited to those a young child would understand, reducing the world
          knowledge that is required for the task.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/mctest_corrected_the_separator/train.tsv',
              'validation': (
                  f'{_URL_BASE}/mctest_corrected_the_separator/dev.tsv'
              ),
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='multirc',
          description=textwrap.dedent(
              """\
          MultiRC is a reading comprehension challenge in which questions can
          only be answered by taking into account information from multiple
          sentences. Questions and answers for this challenge were solicited and
          verified through a 4-step crowdsourcing experiment. The dataset
          contains questions for paragraphs across 7 different domains (
          elementary school science, news, travel guides, fiction stories, etc)
          bringing in linguistic diversity to the texts and to the questions
          wordings.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/multirc/train.tsv',
              'validation': f'{_URL_BASE}/multirc/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='narrativeqa',
          description=textwrap.dedent(
              """\
          NarrativeQA is an English-lanaguage dataset of stories and
          corresponding questions designed to test reading comprehension,
          especially on long documents.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/narrativeqa/train.tsv',
              'validation': f'{_URL_BASE}/narrativeqa/dev.tsv',
              'test': f'{_URL_BASE}/narrativeqa/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{kocisky-etal-2018-narrativeqa,
              title = "The {N}arrative{QA} Reading Comprehension Challenge",
              author = "Ko{\v{c}}isk{\'y}, Tom{\'a}{\v{s}}  and
                Schwarz, Jonathan  and
                Blunsom, Phil  and
                Dyer, Chris  and
                Hermann, Karl Moritz  and
                Melis, G{\'a}bor  and
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='narrativeqa_dev',
          description=textwrap.dedent(
              """\
          NarrativeQA is an English-lanaguage dataset of stories and
          corresponding questions designed to test reading comprehension,
          especially on long documents.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/narrativeqa_dev/train.tsv',
              'validation': f'{_URL_BASE}/narrativeqa_dev/dev.tsv',
              'test': f'{_URL_BASE}/narrativeqa_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @article{kocisky-etal-2018-narrativeqa,
              title = "The {N}arrative{QA} Reading Comprehension Challenge",
              author = "Ko{\v{c}}isk{\'y}, Tom{\'a}{\v{s}}  and
                Schwarz, Jonathan  and
                Blunsom, Phil  and
                Dyer, Chris  and
                Hermann, Karl Moritz  and
                Melis, G{\'a}bor  and
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='natural_questions',
          description=textwrap.dedent(
              """\
          The NQ corpus contains questions from real users, and it requires QA
          systems to read and comprehend an entire Wikipedia article that may or
          may not contain the answer to the question. The inclusion of real user
          questions, and the requirement that solutions should read an entire
          page to find the answer, cause NQ to be a more realistic and
          challenging task than prior QA datasets.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/natural_questions/train.tsv',
              'validation': f'{_URL_BASE}/natural_questions/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='natural_questions_direct_ans',
          description=textwrap.dedent(
              """\
          The NQ corpus contains questions from real users, and it requires QA
          systems to read and comprehend an entire Wikipedia article that may or
          may not contain the answer to the question. The inclusion of real user
          questions, and the requirement that solutions should read an entire
          page to find the answer, cause NQ to be a more realistic and
          challenging task than prior QA datasets. This version consists of
          direct-answer questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/natural_questions_direct_ans/train.tsv',
              'validation': f'{_URL_BASE}/natural_questions_direct_ans/dev.tsv',
              'test': f'{_URL_BASE}/natural_questions_direct_ans/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='natural_questions_direct_ans_test',
          description=textwrap.dedent(
              """\
          The NQ corpus contains questions from real users, and it requires QA
          systems to read and comprehend an entire Wikipedia article that may or
          may not contain the answer to the question. The inclusion of real user
          questions, and the requirement that solutions should read an entire
          page to find the answer, cause NQ to be a more realistic and
          challenging task than prior QA datasets. This version consists of
          direct-answer questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': (
                  f'{_URL_BASE}/natural_questions_direct_ans_test/train.tsv'
              ),
              'validation': (
                  f'{_URL_BASE}/natural_questions_direct_ans_test/dev.tsv'
              ),
              'test': f'{_URL_BASE}/natural_questions_direct_ans_test/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='natural_questions_with_dpr_para',
          description=textwrap.dedent(
              """\
          The NQ corpus contains questions from real users, and it requires QA
          systems to read and comprehend an entire Wikipedia article that may or
          may not contain the answer to the question. The inclusion of real user
          questions, and the requirement that solutions should read an entire
          page to find the answer, cause NQ to be a more realistic and
          challenging task than prior QA datasets. This version includes
          additional paragraphs (obtained using the DPR retrieval engine) to
          augment each question.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/natural_questions_with_dpr_para/train.tsv',
              'validation': (
                  f'{_URL_BASE}/natural_questions_with_dpr_para/dev.tsv'
              ),
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='natural_questions_with_dpr_para_test',
          description=textwrap.dedent(
              """\
          The NQ corpus contains questions from real users, and it requires QA
          systems to read and comprehend an entire Wikipedia article that may or
          may not contain the answer to the question. The inclusion of real user
          questions, and the requirement that solutions should read an entire
          page to find the answer, cause NQ to be a more realistic and
          challenging task than prior QA datasets. This version includes
          additional paragraphs (obtained using the DPR retrieval engine) to
          augment each question.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': (
                  f'{_URL_BASE}/natural_questions_with_dpr_para_test/train.tsv'
              ),
              'test': (
                  f'{_URL_BASE}/natural_questions_with_dpr_para_test/test.tsv'
              ),
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='newsqa',
          description=textwrap.dedent(
              """\
          NewsQA is a challenging machine comprehension dataset of
          human-generated question-answer pairs. Crowdworkers supply questions
          and answers based on a set of news articles from CNN, with answers
          consisting of spans of text from the corresponding articles.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/newsqa/train.tsv',
              'validation': f'{_URL_BASE}/newsqa/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='openbookqa',
          description=textwrap.dedent(
              """\
          OpenBookQA aims to promote research in advanced question-answering,
          probing a deeper understanding of both the topic (with salient facts
          summarized as an open book, also provided with the dataset) and the
          language it is expressed in. In particular, it contains questions that
          require multi-step reasoning, use of additional common and commonsense
          knowledge, and rich text comprehension. OpenBookQA is a new kind of
          question-answering dataset modeled after open book exams for assessing
          human understanding of a subject.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/openbookqa/train.tsv',
              'validation': f'{_URL_BASE}/openbookqa/dev.tsv',
              'test': f'{_URL_BASE}/openbookqa/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='openbookqa_dev',
          description=textwrap.dedent(
              """\
          OpenBookQA aims to promote research in advanced question-answering,
          probing a deeper understanding of both the topic (with salient facts
          summarized as an open book, also provided with the dataset) and the
          language it is expressed in. In particular, it contains questions that
          require multi-step reasoning, use of additional common and commonsense
          knowledge, and rich text comprehension. OpenBookQA is a new kind of
          question-answering dataset modeled after open book exams for assessing
          human understanding of a subject.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/openbookqa_dev/train.tsv',
              'validation': f'{_URL_BASE}/openbookqa_dev/dev.tsv',
              'test': f'{_URL_BASE}/openbookqa_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='openbookqa_with_ir',
          description=textwrap.dedent(
              """\
          OpenBookQA aims to promote research in advanced question-answering,
          probing a deeper understanding of both the topic (with salient facts
          summarized as an open book, also provided with the dataset) and the
          language it is expressed in. In particular, it contains questions that
          require multi-step reasoning, use of additional common and commonsense
          knowledge, and rich text comprehension. OpenBookQA is a new kind of
          question-answering dataset modeled after open book exams for assessing
          human understanding of a subject. This version includes paragraphs
          fetched via an information retrieval system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/openbookqa_with_ir/train.tsv',
              'validation': f'{_URL_BASE}/openbookqa_with_ir/dev.tsv',
              'test': f'{_URL_BASE}/openbookqa_with_ir/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='openbookqa_with_ir_dev',
          description=textwrap.dedent(
              """\
          OpenBookQA aims to promote research in advanced question-answering,
          probing a deeper understanding of both the topic (with salient facts
          summarized as an open book, also provided with the dataset) and the
          language it is expressed in. In particular, it contains questions that
          require multi-step reasoning, use of additional common and commonsense
          knowledge, and rich text comprehension. OpenBookQA is a new kind of
          question-answering dataset modeled after open book exams for assessing
          human understanding of a subject. This version includes paragraphs
          fetched via an information retrieval system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/openbookqa_with_ir_dev/train.tsv',
              'validation': f'{_URL_BASE}/openbookqa_with_ir_dev/dev.tsv',
              'test': f'{_URL_BASE}/openbookqa_with_ir_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='physical_iqa',
          description=textwrap.dedent(
              """\
          This is a dataset for benchmarking progress in physical commonsense
          understanding. The underlying task is multiple choice question
          answering: given a question q and two possible solutions s1, s2, a
          model or a human must choose the most appropriate solution, of which
          exactly one is correct. The dataset focuses on everyday situations
          with a preference for atypical solutions. The dataset is inspired by
          instructables.com, which provides users with instructions on how to
          build, craft, bake, or manipulate objects using everyday materials.
          Annotators are asked to provide semantic perturbations or alternative
          approaches which are otherwise syntactically and topically similar to
          ensure physical knowledge is targeted. The dataset is further cleaned
          of basic artifacts using the AFLite algorithm.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/physical_iqa/train.tsv',
              'validation': f'{_URL_BASE}/physical_iqa/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{bisk2020piqa,
              title={Piqa: Reasoning about physical commonsense in natural language},
              author={Bisk, Yonatan and Zellers, Rowan and Gao, Jianfeng and Choi, Yejin and others},
              booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
              volume={34},
              number={05},
              pages={7432--7439},
              year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='qasc',
          description=textwrap.dedent(
              """\
          QASC is a question-answering dataset with a focus on sentence
          composition. It consists of 8-way multiple-choice questions about
          grade school science, and comes with a corpus of 17M sentences.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/qasc/train.tsv',
              'validation': f'{_URL_BASE}/qasc/dev.tsv',
              'test': f'{_URL_BASE}/qasc/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{khot2020qasc,
              title={Qasc: A dataset for question answering via sentence composition},
              author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
              booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
              volume={34},
              number={05},
              pages={8082--8090},
              year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='qasc_test',
          description=textwrap.dedent(
              """\
          QASC is a question-answering dataset with a focus on sentence
          composition. It consists of 8-way multiple-choice questions about
          grade school science, and comes with a corpus of 17M sentences.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/qasc_test/train.tsv',
              'validation': f'{_URL_BASE}/qasc_test/dev.tsv',
              'test': f'{_URL_BASE}/qasc_test/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{khot2020qasc,
              title={Qasc: A dataset for question answering via sentence composition},
              author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
              booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
              volume={34},
              number={05},
              pages={8082--8090},
              year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='qasc_with_ir',
          description=textwrap.dedent(
              """\
          QASC is a question-answering dataset with a focus on sentence
          composition. It consists of 8-way multiple-choice questions about
          grade school science, and comes with a corpus of 17M sentences. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/qasc_with_ir/train.tsv',
              'validation': f'{_URL_BASE}/qasc_with_ir/dev.tsv',
              'test': f'{_URL_BASE}/qasc_with_ir/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{khot2020qasc,
              title={Qasc: A dataset for question answering via sentence composition},
              author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
              booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
              volume={34},
              number={05},
              pages={8082--8090},
              year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='qasc_with_ir_test',
          description=textwrap.dedent(
              """\
          QASC is a question-answering dataset with a focus on sentence
          composition. It consists of 8-way multiple-choice questions about
          grade school science, and comes with a corpus of 17M sentences. This
          version includes paragraphs fetched via an information retrieval
          system as additional evidence.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/qasc_with_ir_test/train.tsv',
              'validation': f'{_URL_BASE}/qasc_with_ir_test/dev.tsv',
              'test': f'{_URL_BASE}/qasc_with_ir_test/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{khot2020qasc,
              title={Qasc: A dataset for question answering via sentence composition},
              author={Khot, Tushar and Clark, Peter and Guerquin, Michal and Jansen, Peter and Sabharwal, Ashish},
              booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
              volume={34},
              number={05},
              pages={8082--8090},
              year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='quoref',
          description=textwrap.dedent(
              """\
          This dataset tests the coreferential reasoning capability of reading
          comprehension systems. In this span-selection benchmark containing
          questions over paragraphs from Wikipedia, a system must resolve hard
          coreferences before selecting the appropriate span(s) in the
          paragraphs for answering questions.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/quoref/train.tsv',
              'validation': f'{_URL_BASE}/quoref/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{dasigi-etal-2019-quoref,
              title = "{Q}uoref: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning",
              author = "Dasigi, Pradeep  and
                Liu, Nelson F.  and
                Marasovi{\'c}, Ana  and
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='race_string',
          description=textwrap.dedent(
              """\
          Race is a large-scale reading comprehension dataset. The dataset is
          collected from English examinations in China, which are designed for
          middle school and high school students. The dataset can be served as
          the training and test sets for machine comprehension.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/race_string/train.tsv',
              'validation': f'{_URL_BASE}/race_string/dev.tsv',
              'test': f'{_URL_BASE}/race_string/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='race_string_dev',
          description=textwrap.dedent(
              """\
          Race is a large-scale reading comprehension dataset. The dataset is
          collected from English examinations in China, which are designed for
          middle school and high school students. The dataset can be served as
          the training and test sets for machine comprehension.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/race_string_dev/train.tsv',
              'validation': f'{_URL_BASE}/race_string_dev/dev.tsv',
              'test': f'{_URL_BASE}/race_string_dev/test.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='ropes',
          description=textwrap.dedent(
              """\
          This dataset tests a system's ability to apply knowledge from a
          passage of text to a new situation. A system is presented a background
          passage containing a causal or qualitative relation(s) (e.g., "animal
          pollinators increase efficiency of fertilization in flowers"), a novel
          situation that uses this background, and questions that require
          reasoning about effects of the relationships in the background passage
          in the context of the situation.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/ropes/train.tsv',
              'validation': f'{_URL_BASE}/ropes/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='social_iqa',
          description=textwrap.dedent(
              """\
          This is a large-scale benchmark for commonsense reasoning about social
          situations. Social IQa contains multiple choice questions for probing
          emotional and social intelligence in a variety of everyday situations.
          Through crowdsourcing, commonsense questions along with correct and
          incorrect answers about social interactions are collected, using a new
          framework that mitigates stylistic artifacts in incorrect answers by
          asking workers to provide the right answer to a different but related
          question.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/social_iqa/train.tsv',
              'validation': f'{_URL_BASE}/social_iqa/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='squad1_1',
          description=textwrap.dedent(
              """\
          This is a reading comprehension dataset consisting of questions posed
          by crowdworkers on a set of Wikipedia articles, where the answer to
          each question is a segment of text from the corresponding reading
          passage.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/squad1_1/train.tsv',
              'validation': f'{_URL_BASE}/squad1_1/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='squad2',
          description=textwrap.dedent(
              """\
          This dataset combines the original Stanford Question Answering Dataset
          (SQuAD) dataset with unanswerable questions written adversarially by
          crowdworkers to look similar to answerable ones.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/squad2/train.tsv',
              'validation': f'{_URL_BASE}/squad2/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
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
          """
          ),
      ),
      UnifiedQAConfig(
          name='winogrande_l',
          description=textwrap.dedent(
              """\
          This dataset is inspired by the original Winograd Schema Challenge
          design, but adjusted to improve both the scale and the hardness of the
          dataset. The key steps of the dataset construction consist of (1) a
          carefully designed crowdsourcing procedure, followed by (2) systematic
          bias reduction using a novel AfLite algorithm that generalizes
          human-detectable word associations to machine-detectable embedding
          associations. Training sets with differnt sizes are provided. This set
          corresponds to size `l`.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/winogrande_l/train.tsv',
              'validation': f'{_URL_BASE}/winogrande_l/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{sakaguchi2020winogrande,
            title={Winogrande: An adversarial winograd schema challenge at scale},
            author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
            booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
            volume={34},
            number={05},
            pages={8732--8740},
            year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='winogrande_m',
          description=textwrap.dedent(
              """\
          This dataset is inspired by the original Winograd Schema Challenge
          design, but adjusted to improve both the scale and the hardness of the
          dataset. The key steps of the dataset construction consist of (1) a
          carefully designed crowdsourcing procedure, followed by (2) systematic
          bias reduction using a novel AfLite algorithm that generalizes
          human-detectable word associations to machine-detectable embedding
          associations. Training sets with differnt sizes are provided. This set
          corresponds to size `m`.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/winogrande_m/train.tsv',
              'validation': f'{_URL_BASE}/winogrande_m/dev.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{sakaguchi2020winogrande,
            title={Winogrande: An adversarial winograd schema challenge at scale},
            author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
            booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
            volume={34},
            number={05},
            pages={8732--8740},
            year={2020}
          }
          """
          ),
      ),
      UnifiedQAConfig(
          name='winogrande_s',
          description=textwrap.dedent(
              """\
          This dataset is inspired by the original Winograd Schema Challenge
          design, but adjusted to improve both the scale and the hardness of the
          dataset. The key steps of the dataset construction consist of (1) a
          carefully designed crowdsourcing procedure, followed by (2) systematic
          bias reduction using a novel AfLite algorithm that generalizes
          human-detectable word associations to machine-detectable embedding
          associations. Training sets with differnt sizes are provided. This set
          corresponds to size `s`.
          """
          ),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': f'{_URL_BASE}/winogrande_s/train.tsv',
              'validation': f'{_URL_BASE}/winogrande_s/dev.tsv',
              'test': f'{_URL_BASE}/winogrande_s/test.tsv',
          },
          citation=textwrap.dedent(
              """\
          @inproceedings{sakaguchi2020winogrande,
            title={Winogrande: An adversarial winograd schema challenge at scale},
            author={Sakaguchi, Keisuke and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
            booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
            volume={34},
            number={05},
            pages={8732--8740},
            year={2020}
          }
          """
          ),
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(self.builder_config.features),
        supervised_keys=None,
        homepage=_HOMEPAGE,
        citation=self.builder_config.citation + '\n' + _CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
    split_generators = {}

    if 'train' in self.builder_config.data_urls:
      split_generators.update(
          {
              tfds.Split.TRAIN: self._generate_examples(path=data_dir['train']),
          }
      )

    if 'validation' in self.builder_config.data_urls:
      split_generators.update(
          {
              tfds.Split.VALIDATION: self._generate_examples(
                  path=data_dir['validation']
              ),
          }
      )

    if 'test' in self.builder_config.data_urls:
      split_generators.update(
          {
              tfds.Split.TEST: self._generate_examples(path=data_dir['test']),
          }
      )
    return split_generators

  def _generate_examples(self, path):
    """Yields examples."""
    with epath.Path(path).open() as f:
      data = csv.reader(f, delimiter='\t')
      # Skip the header row
      if self.builder_config.header:
        next(data)
      for id_, row in enumerate(data):
        yield id_, {'input': row[0].strip(), 'output': row[1].strip()}
