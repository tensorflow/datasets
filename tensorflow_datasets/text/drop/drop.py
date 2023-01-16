# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""drop dataset."""

import json
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
With system performance on existing reading comprehension benchmarks nearing or
surpassing human performance, we need a new, hard dataset that improves systems'
capabilities to actually read paragraphs of text. DROP is a crowdsourced,
adversarially-created, 96k-question benchmark, in which a system must resolve
references in a question, perhaps to multiple input positions, and perform
discrete operations over them (such as addition, counting, or sorting). These
operations require a much more comprehensive understanding of the content of
paragraphs than what was necessary for prior datasets.
"""

_CITATION = """
@inproceedings{Dua2019DROP,
  author={Dheeru Dua and Yizhong Wang and Pradeep Dasigi and Gabriel Stanovsky and Sameer Singh and Matt Gardner},
  title={  {DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs},
  booktitle={Proc. of NAACL},
  year={2019}
}
"""

_DATA_LINK = (
    "https://s3-us-west-2.amazonaws.com/allennlp/datasets/drop/drop_dataset.zip"
)


def _get_answer(answer_dict):
  if answer_dict.get("number", ""):
    return answer_dict["number"]
  elif answer_dict.get("date", {}).get("day", ""):
    return (
        f'{answer_dict["date"]["year"]}-'
        f'{answer_dict["date"]["month"]}-{answer_dict["date"]["day"]}'
    )
  elif answer_dict.get("spans", []):
    return answer_dict["spans"][0]
  else:
    return ""


class Drop(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for drop dataset."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "Add all options for the answers.",
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "passage": tfds.features.Text(),
            "question": tfds.features.Text(),
            "answer": tfds.features.Text(),
            "validated_answers": tfds.features.Sequence(tfds.features.Text()),
            "query_id": tfds.features.Text(),
        }),
        homepage="https://allennlp.org/drop",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DATA_LINK)

    path = path / "drop_dataset"

    return {
        "train": self._generate_examples(path / "drop_dataset_train.json"),
        "dev": self._generate_examples(path / "drop_dataset_dev.json"),
    }

  def _generate_examples(self, filepath):
    """Yields examples."""
    original_data = json.loads(filepath.read_text())
    for _, example in original_data.items():
      passage = example["passage"]
      for idx, qa in enumerate(example["qa_pairs"]):
        question = qa["question"]
        answer = _get_answer(qa["answer"])
        validated_answers = [
            _get_answer(v_answer)
            for v_answer in qa.get("validated_answers", [])
        ]
        yield qa["query_id"] + str(idx), {
            "passage": passage,
            "question": question,
            "answer": answer,
            "validated_answers": validated_answers,
            "query_id": qa["query_id"] + str(idx),
        }
