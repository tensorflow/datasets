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

"""QuALITY dataset."""
import dataclasses
import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
QuALITY, a multiple-choice, long-reading comprehension dataset.

We provide only the raw version.
"""

_CITATION = """@article{pang2021quality,
  title={{QuALITY}: Question Answering with Long Input Texts, Yes!},
  author={Pang, Richard Yuanzhe and Parrish, Alicia and Joshi, Nitish and Nangia, Nikita and Phang, Jason and Chen, Angelica and Padmakumar, Vishakh and Ma, Johnny and Thompson, Jana and He, He and Bowman, Samuel R.},
  journal={arXiv preprint arXiv:2112.08608},
  year={2021}
}
"""

_DOWNLOAD_URL = 'https://github.com/nyu-mll/quality/raw/main/data/QuALITY.v0.9.zip'

# Fields that are straight text copies from raw example to processed example.
_ONE2ONE_FIELDS = ('article', 'article_id', 'set_unique_id', 'writer_id',
                   'source', 'title', 'topic', 'url', 'writer_id')


@dataclasses.dataclass
class QualityConfig(tfds.core.BuilderConfig):
  stripped: bool = False


class Quality(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for quality dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
      QualityConfig(name='raw', description='Raw with HTML.',
                    stripped=False),  # default
      QualityConfig(
          name='stripped', description='Stripped of HTML.', stripped=True),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # Mirror format of RACE dataset as much as possible.
    features_dict = {
        'article':
            tfds.features.Text(),
        # The sequence lengths of Sequence fields should match.
        'questions':
            tfds.features.Sequence(tfds.features.Text()),
        'question_ids':
            tfds.features.Sequence(tfds.features.Text()),
        # 4 options per question, similar to RACE
        'options':
            tfds.features.Sequence(
                tfds.features.Sequence(tfds.features.Text())),
        'gold_labels':
            tfds.features.Sequence(tf.int32),  # 0, 1, 2, 3
        'writer_labels':
            tfds.features.Sequence(tf.int32),  # 0, 1, 2, 3
        'difficults':
            tfds.features.Sequence(tf.bool)
    }
    features_dict.update({k: tfds.features.Text() for k in _ONE2ONE_FIELDS})
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        # Note: some fields are left out.
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,
        homepage='https://github.com/nyu-mll/quality',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    if self.builder_config.stripped:
      return {
          'train':
              self._generate_examples(path / 'QuALITY.v0.9.htmlstripped.train',
                                      'train'),
          'test':
              self._generate_examples(path / 'QuALITY.v0.9.htmlstripped.test',
                                      'test'),
          'dev':
              self._generate_examples(path / 'QuALITY.v0.9.htmlstripped.dev',
                                      'dev'),
      }
    else:
      return {
          'train':
              self._generate_examples(path / 'QuALITY.v0.9.train', 'train'),
          'test':
              self._generate_examples(path / 'QuALITY.v0.9.test', 'test'),
          'dev':
              self._generate_examples(path / 'QuALITY.v0.9.dev', 'dev'),
      }

  def _generate_examples(self, path, split: str):
    """Yields examples."""
    for line in path.open():
      j = json.loads(line)
      fields = {k: j[k] for k in _ONE2ONE_FIELDS}
      fields.update({
          'questions': [q['question'] for q in j['questions']],
          'question_ids': [q['question_unique_id'] for q in j['questions']],
          'difficults': [q['difficult'] for q in j['questions']],
          'options': [q['options'] for q in j['questions']],
      })
      if split in ('train', 'dev'):
        fields.update({
            'gold_labels': [q['gold_label'] for q in j['questions']],
            'writer_labels': [q['writer_label'] for q in j['questions']],
        })
      else:
        fields.update({
            'gold_labels': [],
            'writer_labels': [],
        })
      yield j['set_unique_id'], fields
