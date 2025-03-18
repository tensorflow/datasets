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

"""Scientific Papers Dataset."""

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_DOCUMENT = "article"
_SUMMARY = "abstract"

_URLS = {
    "arxiv": "https://drive.google.com/uc?id=1b3rmCSIoh6VhD4HKWjI4HOW-cSwcwbeC&export=download",
    "pubmed": "https://drive.google.com/uc?id=1lvsqvsFi3W-pE1SqNZI0s8NR9rC1tsja&export=download",
}


class ScientificPapersConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Scientific Papers."""

  def __init__(self, *, filename=None, **kwargs):
    """BuilderConfig for Wikihow.

    Args:
      filename: filename of different configs for the dataset.
      **kwargs: keyword arguments forwarded to super.
    """
    # 1.1.0 remove sentence breaker <S> and </S> in summary.
    super(ScientificPapersConfig, self).__init__(
        version=tfds.core.Version("1.1.1"),
        supported_versions=[tfds.core.Version("1.1.0")],
        **kwargs,
    )  # pytype: disable=wrong-arg-types  # gen-stub-imports
    self.filename = filename


class Builder(tfds.core.GeneratorBasedBuilder):
  """Scientific Papers."""

  BUILDER_CONFIGS = [
      ScientificPapersConfig(
          name="arxiv", description="Documents from ArXiv repository."
      ),
      ScientificPapersConfig(
          name="pubmed", description="Documents from PubMed repository."
      ),
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text(),
            "section_names": tfds.features.Text(),
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/armancohan/long-summarization",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(_URLS)
    path = os.path.join(
        dl_paths[self.builder_config.name],
        self.builder_config.name + "-dataset",
    )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(path, "train.txt")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": os.path.join(path, "val.txt")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(path, "test.txt")},
        ),
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    with epath.Path(path).open() as f:
      for line in f:
        # Possible keys are:
        # "article_id": str
        # "article_text": list[str] article (list of paragraphs).
        # "abstract_text": list[str], abstract (list of paragraphs).
        # "section_names": list[str], list of section names.
        # "sections": list[list[str]], list of sections (list of paragraphs)
        d = json.loads(line)
        summary = "\n".join(d["abstract_text"])
        # In original paper, <S> and </S> are not used in vocab during training
        # or during decoding.
        # https://github.com/armancohan/long-summarization/blob/master/data.py#L27
        summary = summary.replace("<S>", "").replace("</S>", "")
        yield d["article_id"], {
            _DOCUMENT: "\n".join(d["article_text"]),
            _SUMMARY: summary,
            "section_names": "\n".join(d["section_names"]),
        }
