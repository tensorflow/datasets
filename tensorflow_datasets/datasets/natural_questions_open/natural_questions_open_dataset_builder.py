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

"""Natural Questions Open: A Benchmark for Open Domain Question Answering."""

from __future__ import annotations

import json

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL_FMT = 'https://raw.githubusercontent.com/google-research-datasets/natural-questions/a7a113c9fdc2d9986d624bd43b8a18d6d5779eaa/nq_open/NQ-open.{split}.jsonl'

_URL = 'https://github.com/google-research-datasets/natural-questions/tree/master/nq_open'


class Builder(tfds.core.GeneratorBasedBuilder):
  """Natural Questions Open: A Benchmark for Open Domain Question Answering."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {'question': np.str_, 'answer': tfds.features.Sequence(np.str_)}
        ),
        supervised_keys=None,
        homepage=_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    file_paths = dl_manager.download({
        'train': _DOWNLOAD_URL_FMT.format(split='train'),
        'validation': _DOWNLOAD_URL_FMT.format(split='dev'),
    })
    return [
        tfds.core.SplitGenerator(
            name=split, gen_kwargs={'file_path': file_path}
        )
        for split, file_path in file_paths.items()
    ]

  def _generate_examples(self, file_path):
    """Parses split file and yields examples."""

    with epath.Path(file_path).open() as f:
      for i, line in enumerate(f):
        yield i, json.loads(line)
