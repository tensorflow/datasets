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

"""The scicite dataset."""

import json
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_SOURCE_NAMES = [
    "properNoun",
    "andPhrase",
    "acronym",
    "etAlPhrase",
    "explicit",
    "acronymParen",
    "nan",
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for classifying citation intents in academic papers."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "string": tfds.features.Text(),
            "sectionName": tfds.features.Text(),
            "label": tfds.features.ClassLabel(
                names=["method", "background", "result"]
            ),
            "citingPaperId": tfds.features.Text(),
            "citedPaperId": tfds.features.Text(),
            "excerpt_index": np.int32,
            "isKeyCitation": np.bool_,
            "label2": tfds.features.ClassLabel(
                names=["supportive", "not_supportive", "cant_determine", "none"]
            ),
            "citeEnd": np.int64,
            "citeStart": np.int64,
            "source": tfds.features.ClassLabel(names=_SOURCE_NAMES),
            "label_confidence": np.float32,
            "label2_confidence": np.float32,
            "id": tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("string", "label"),
        # Homepage of the dataset for documentation
        homepage="https://github.com/allenai/scicite",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(
        {
            "scicite": "https://s3-us-west-2.amazonaws.com/ai2-s2-research/scicite/scicite.tar.gz",
        }
    )
    path = os.path.join(dl_paths["scicite"], "scicite")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(path, "train.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": os.path.join(path, "dev.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(path, "test.jsonl")},
        ),
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    with epath.Path(path).open() as f:
      unique_ids = {}
      for line in f:
        d = json.loads(line)
        unique_id = str(d["unique_id"])
        if unique_id in unique_ids:
          continue
        unique_ids[unique_id] = True
        yield unique_id, {
            "string": d["string"],
            "label": str(d["label"]),
            "sectionName": str(d["sectionName"]),
            "citingPaperId": str(d["citingPaperId"]),
            "citedPaperId": str(d["citedPaperId"]),
            "excerpt_index": int(d["excerpt_index"]),
            "isKeyCitation": bool(d["isKeyCitation"]),
            "label2": str(d.get("label2", "none")),
            "citeEnd": _safe_int(d["citeEnd"]),
            "citeStart": _safe_int(d["citeStart"]),
            "source": str(d["source"]),
            "label_confidence": float(d.get("label_confidence", 0.0)),
            "label2_confidence": float(d.get("label2_confidence", 0.0)),
            "id": str(d["id"]),
        }


def _safe_int(a):
  try:
    # skip NaNs
    return int(a)
  except ValueError:
    return -1
