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

"""A question-answering dataset with a focus on sentence composition."""

import json
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = "http://data.allenai.org/downloads/qasc/qasc_dataset.tar.gz"
_HOMEPAGE_URL = "https://allenai.org/data/qasc"


class Builder(tfds.core.GeneratorBasedBuilder):
  """QaSC Dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "question": tfds.features.Text(),
            "choices": tfds.features.Sequence(
                {"text": tfds.features.Text(), "label": tfds.features.Text()}
            ),
            "answerKey": tfds.features.Text(),
            "fact1": tfds.features.Text(),
            "fact2": tfds.features.Text(),
            "combinedfact": tfds.features.Text(),
            "formatted_question": tfds.features.Text(),
        }),
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_HOMEPAGE_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract({"QASC_Dataset": _DOWNLOAD_URL})
    data_dir = os.path.join(dl_dir["QASC_Dataset"], "QASC_Dataset")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepath": os.path.join(data_dir, "train.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"filepath": os.path.join(data_dir, "test.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": os.path.join(data_dir, "dev.jsonl")},
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""

    with tf.io.gfile.GFile(filepath, "r") as f:
      for row in f:
        data = json.loads(row)
        answerkey = data.get("answerKey", "")
        id_ = data["id"]
        question = data["question"]["stem"]
        choices = data["question"]["choices"]
        text_choices = [choice["text"] for choice in choices]
        label_choices = [choice["label"] for choice in choices]
        fact1 = data.get("fact1", "")
        fact2 = data.get("fact2", "")
        combined_fact = data.get("combinedfact", "")
        formatted_question = data.get("formatted_question", "")
        yield id_, {
            "id": id_,
            "answerKey": answerkey,
            "question": question,
            "choices": {"text": text_choices, "label": label_choices},
            "fact1": fact1,
            "fact2": fact2,
            "combinedfact": combined_fact,
            "formatted_question": formatted_question,
        }
