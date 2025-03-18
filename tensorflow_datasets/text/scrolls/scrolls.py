# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""scrolls dataset."""
import dataclasses
import json

from etils import epath
import tensorflow_datasets.public_api as tfds

# Corresponding HF dataset:
# https://huggingface.co/datasets/tau/scrolls/blob/main/scrolls.py

_SCROLLS_CITATION = """
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
"""

_SCROLLS_DESCRIPTION = """
SCROLLS: Standardized CompaRison Over Long Language Sequences.
A suite of natural language tfds.core.that require reasoning over long texts.
https://scrolls-benchmark.com/
"""

_SUMM_SCREEN_CITATION = r"""
@misc{chen2021summscreen,
      title={SummScreen: A Dataset for Abstractive Screenplay Summarization},
      author={Mingda Chen and Zewei Chu and Sam Wiseman and Kevin Gimpel},
      year={2021},
      eprint={2104.07091},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}"""

_QASPER_CITATION = r"""
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
}"""

_QMSUM_CITATION = r"""@inproceedings{zhong-etal-2021-qmsum,
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
}"""

_NARRATIVE_QA_CITATION = r"""
@article{kovcisky2018narrativeqa,
  title={The narrativeqa reading comprehension challenge},
  author={Ko{\v{c}}isk{\'y}, Tom{\'a}{\v{s}} and Schwarz, Jonathan and Blunsom, Phil and Dyer, Chris and Hermann, Karl Moritz and Melis, G{\'a}bor and Grefenstette, Edward},
  journal={Transactions of the Association for Computational Linguistics},
  volume={6},
  pages={317--328},
  year={2018},
  publisher={MIT Press}
}"""

_GOV_REPORT_CITATION = r"""
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
}"""

_CONTRACT_NLI_CITATION = """\
@inproceedings{koreeda-manning-2021-contractnli,
    title = "ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts",
    author = "Koreeda, Yuta  and
      Manning, Christopher D.",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    year = "2021",
    publisher = "Association for Computational Linguistics"
}
"""
_QUALITY_CITATION = """\
@article{pang2021quality,
  title={{QuALITY}: Question Answering with Long Input Texts, Yes!},
  author={Pang, Richard Yuanzhe and Parrish, Alicia and Joshi, Nitish and Nangia, Nikita and Phang, Jason and Chen, Angelica and Padmakumar, Vishakh and Ma, Johnny and Thompson, Jana and He, He and Bowman, Samuel R.},
  journal={arXiv preprint arXiv:2112.08608},
  year={2021}
}
"""


@dataclasses.dataclass
class ScrollsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SCROLLS."""

  data_url: str = ""
  citation: str = ""
  url: str = ""


_INPUT_KEY = "input"
_OUTPUT_KEY = "output"
_FEATURES = ("id", "pid", _INPUT_KEY, _OUTPUT_KEY)


class Scrolls(tfds.core.GeneratorBasedBuilder):
  """The SCROLLS benchmark."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  BUILDER_CONFIGS = [
      ScrollsConfig(
          name="summ_screen_fd",
          description="summ_screen_fd subset",
          data_url="https://scrolls-tau.s3.us-east-2.amazonaws.com/summ_screen_fd.zip",
          citation=_SUMM_SCREEN_CITATION,
          url="https://github.com/mingdachen/SummScreen",
      ),
      ScrollsConfig(
          name="qasper",
          description="qasper subset",
          data_url="https://scrolls-tau.s3.us-east-2.amazonaws.com/qasper.zip",
          citation=_QASPER_CITATION,
          url="https://allenai.org/project/qasper",
      ),
      ScrollsConfig(
          name="qmsum",
          description="qmsum subset",
          data_url="https://scrolls-tau.s3.us-east-2.amazonaws.com/qmsum.zip",
          citation=_QMSUM_CITATION,
          url="https://github.com/Yale-LILY/QMSum",
      ),
      ScrollsConfig(
          name="narrative_qa",
          description="narrative_qa subset",
          data_url=(
              "https://scrolls-tau.s3.us-east-2.amazonaws.com/narrative_qa.zip"
          ),
          citation=_NARRATIVE_QA_CITATION,
          url="https://deepmind.com/research/publications/narrativeqa-reading-comprehension-challenge",
      ),
      ScrollsConfig(
          name="gov_report",
          description="gov_report subset",
          data_url=(
              "https://scrolls-tau.s3.us-east-2.amazonaws.com/gov_report.zip"
          ),
          citation=_GOV_REPORT_CITATION,
          url="https://gov-report-data.github.io/",
      ),
      ScrollsConfig(
          name="contract_nli",
          description="contract_nli subset",
          data_url=(
              "https://scrolls-tau.s3.us-east-2.amazonaws.com/contract_nli.zip"
          ),
          citation=_CONTRACT_NLI_CITATION,
          url="https://stanfordnlp.github.io/contract-nli/",
      ),
      ScrollsConfig(
          name="quality",
          description="quality subset",
          data_url="https://scrolls-tau.s3.us-east-2.amazonaws.com/quality.zip",
          citation=_QUALITY_CITATION,
          url="https://github.com/nyu-mll/quality",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_SCROLLS_DESCRIPTION + self.builder_config.description,
        features=tfds.features.FeaturesDict(
            {feature: tfds.features.Text() for feature in _FEATURES}
        ),
        supervised_keys=(_INPUT_KEY, _OUTPUT_KEY),
        homepage=self.builder_config.url,
        citation=self.builder_config.citation + "\n" + _SCROLLS_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_dir = dl_manager.download_and_extract(self.builder_config.data_url)
    task_name = task_name = _get_task_name_from_data_url(
        self.builder_config.data_url
    )

    return {
        "train": self._generate_examples(dl_dir / task_name / "train.jsonl"),
        "validation": self._generate_examples(
            dl_dir / task_name / "validation.jsonl"
        ),
        "test": self._generate_examples(dl_dir / task_name / "test.jsonl"),
    }

  def _generate_examples(self, path):
    with epath.Path(path).open() as f:
      for line in f:
        row = json.loads(line)

        # Test set has 'null' for 'output'
        yield row["pid"], {
            k: row[k] if row[k] is not None else "" for k in _FEATURES
        }


def _get_task_name_from_data_url(data_url):
  return data_url.split("/")[-1].split(".")[0]
