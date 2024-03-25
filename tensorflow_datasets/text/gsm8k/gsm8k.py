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

"""gsm8k dataset."""

import json

from etils import epath
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
A dataset of 8.5K high quality linguistically diverse grade school math word problems.
"""

_CITATION = """
@misc{cobbe2021training,
      title={Training Verifiers to Solve Math Word Problems},
      author={Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
      year={2021},
      eprint={2110.14168},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
"""

_URL_PREFIX = 'https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/'
_URLS = {
    k: f'{_URL_PREFIX}{k}.jsonl'
    for k in ['train', 'test', 'train_socratic', 'test_socratic']
}

_FEATURES = ['question', 'answer', 'annotation', 'short_answer']


class Gsm8k(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for gsm8k dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {k: tfds.features.Text() for k in _FEATURES}
        ),
        supervised_keys=None,
        homepage='https://github.com/openai/grade-school-math',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted = dl_manager.download_and_extract(_URLS)
    return {k: self._generate_examples(v) for k, v in extracted.items()}

  def _generate_examples(self, path: epath.PathLike):
    """Yields examples."""
    with epath.Path(path).open() as f:
      for i, line in enumerate(f):
        ex = json.loads(line)
        ex['annotation'], ex['short_answer'] = ex['answer'].split('#### ')
        yield i, ex
