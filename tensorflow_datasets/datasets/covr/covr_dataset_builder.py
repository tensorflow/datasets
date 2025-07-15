# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""covr dataset."""

import json

from etils import epath
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for covr dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'utterance': tfds.features.Text(),
            'scenes': tfds.features.Sequence(
                feature=tfds.features.Text(),
            ),
            'properties': tfds.features.Sequence(
                feature=tfds.features.Text(),
            ),
            'pattern_name': tfds.features.Text(),
            'program': tfds.features.Text(),
            'label': tfds.features.Text(),
            'images': tfds.features.Sequence(
                feature=tfds.features.Image(),
            ),
        }),
        supervised_keys=None,
        homepage='https://covr-dataset.github.io/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted_dirs = dl_manager.download_and_extract({
        'covr_dir': (
            'https://drive.google.com/uc?export=download&'
            'id=10xlQ6isRdGX94BypoqN6klniGeqdLBJA'
        ),
        'imsitu_dir': (
            'https://s3.amazonaws.com/my89-frame-annotation'
            '/public/of500_images.tar'
        ),
        'vg1_dir': 'https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip',
        'vg2_dir': (
            'https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip'
        ),
    })

    # Each name is the image file name without the ".jpg" extension, which is
    # also used as the scene id in COVR.
    image_path_by_scene_id: dict[str, epath.Path] = {}
    image_globs = [
        extracted_dirs['vg1_dir'].glob('*/*.jpg'),
        extracted_dirs['vg2_dir'].glob('*/*.jpg'),
        extracted_dirs['imsitu_dir'].glob('of500_images/*/*.jpg'),
    ]
    for image_glob in image_globs:
      for image_path in image_glob:
        name = image_path.stem
        image_path_by_scene_id[name] = image_path
    path = extracted_dirs['covr_dir']
    return {
        'train': self._generate_examples(
            path / 'train.jsonl', image_path_by_scene_id
        ),
        'test': self._generate_examples(
            path / 'test.jsonl', image_path_by_scene_id
        ),
        'validation': self._generate_examples(
            path / 'val.jsonl', image_path_by_scene_id
        ),
    }

  def _generate_examples(
      self, path: epath.Path, image_path_by_scene_id: dict[str, epath.Path]
  ):
    """Yields examples."""
    with path.open() as f:
      for line in f:
        item = json.loads(line)
        images = [
            image_path_by_scene_id[scene_id] for scene_id in item['scenes']
        ]
        yield item['qid'], {
            'utterance': item['utterance'],
            'scenes': item['scenes'],
            'properties': item['properties'],
            'pattern_name': item['pattern_name'],
            'program': str(item['program']),
            'label': str(item.get('answer')),
            'images': images,
        }
