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

"""media_sum dataset."""

import json
from typing import List

from etils import epath
import tensorflow_datasets.public_api as tfds

_BEAM_NAMESPACE = 'TFDS_MEDIA_SUM'

_DESCRIPTION = """
This large-scale media interview dataset contains 463.6K transcripts with
abstractive summaries, collected from interview transcripts and overview /
topic descriptions from NPR and CNN.

**Please restrict your usage of this dataset to research purpose only.**

And please cite our paper:
**[MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization](https://arxiv.org/abs/2103.06410)**

## Ethics

We have used only the publicly available transcripts data from the media
sources and adhere to their only-for-research-purpose guideline.

As media and guests may have biased views, the transcripts and summaries will
likely contain them. The content of the transcripts and summaries only reflect
the views of the media and guests, and should be viewed with discretion.
"""

_CITATION = """
@article{zhu2021mediasum,
  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},
  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},
  journal={arXiv preprint arXiv:2103.06410},
  year={2021}
}
"""


class MediaSum(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for media_sum dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  manual_dir should contain the files:

    * news_dialogue.json
    * train_val_test_split.json

  The files can be downloaded and extracted from the dataset's GitHub page:
  https://github.com/zcgzcgzcg1/MediaSum/tree/main/data
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'program': tfds.features.Text(),
            'date': tfds.features.Text(),
            'url': tfds.features.Text(),
            'summary': tfds.features.Text(),
            'utt': tfds.features.Sequence(tfds.features.Text()),
            'speaker': tfds.features.Sequence(tfds.features.Text()),
        }),
        supervised_keys=('utt', 'summary'),
        homepage='https://github.com/zcgzcgzcg1/MediaSum',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    archive = {
        'samples': dl_manager.manual_dir / 'news_dialogue.json',
        'splits_ids': dl_manager.manual_dir / 'train_val_test_split.json',
    }

    splits_ids = self._load_json_file(archive['splits_ids'])
    raw_samples = self._load_json_file(archive['samples'])

    return {
        'train':
            self._generate_examples(
                split_ids=splits_ids['train'], raw_samples=raw_samples),
        'val':
            self._generate_examples(
                split_ids=splits_ids['val'], raw_samples=raw_samples),
        'test':
            self._generate_examples(
                split_ids=splits_ids['test'], raw_samples=raw_samples),
    }

  def _load_json_file(self, json_path: epath.Path):
    with epath.Path(json_path).open() as f:
      file_content = json.load(f)
    return file_content

  def _generate_examples(self, split_ids: List[str], raw_samples: List[str]):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_example(sample):
      example = {}
      for k in self.info.features.keys():
        try:
          example[k] = sample[k]
        # Some of the keys are optional.
        except KeyError:
          example[k] = ''
      return example['id'], example

    return (beam.Create(raw_samples)
            | 'Select raw samples with the correct split id' >>
            beam.Filter(lambda x: x['id'] in split_ids)
            | 'Process and yield examples' >> beam.Map(_process_example))
