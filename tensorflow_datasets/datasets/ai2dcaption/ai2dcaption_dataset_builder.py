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

"""AI2DCaption dataset."""

import json
import os.path

import tensorflow_datasets.public_api as tfds

LAYOUT_NAMES = [
    'abstract',
    'circular',
    'columns',
    'linear',
    'rows',
    'tree',
    'unspecified',
]

TOPIC_NAMES = ['astronomy', 'biology', 'engineering', 'unspecified']

TYPE_NAMES = [
    'arrow',
    'image',
    'object',
    'relationship',
    'text',
]

CATEGORIES = [
    'imageCaption',
    'imageTitle',
    'interObjectLinkage',
    'intraObjectLabel',
    'intraObjectLinkage',
    'intraObjectRegionLabel',
    'intraObjectTextLinkage',
    'misc',
    'sectionTitle',
    'unspecified',
]

SPLITS = [
    'auditor_llm_training_examples',
    'gpt4v',
    'llava_15',
    'planner_llm_training_examples',
    'test',
]

JSON_URL_TMPL = 'https://huggingface.co/datasets/abhayzala/AI2D-Caption/resolve/main/ai2d_caption_{split}.json?download=true'

IMAGES_URL = 'http://ai2-website.s3.amazonaws.com/data/ai2d-all.zip'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for AI2DCaption dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(
                shape=(None, None, 3),
                doc=tfds.features.Documentation(
                    desc='The image of the diagram.',
                ),
            ),
            'image_filename': tfds.features.Text(
                doc=tfds.features.Documentation(
                    desc='Image filename. e.g. "1337.png"',
                ),
            ),
            'topic': tfds.features.ClassLabel(names=TOPIC_NAMES),
            'layout': tfds.features.ClassLabel(names=LAYOUT_NAMES),
            'caption': tfds.features.Text(),
            'relationships': tfds.features.Sequence(tfds.features.Text()),
            'entities': tfds.features.Sequence(
                tfds.features.FeaturesDict({
                    'id': tfds.features.Text(),
                    'type': tfds.features.ClassLabel(names=TYPE_NAMES),
                    'label': tfds.features.Text(),
                    'bounds': tfds.features.BBoxFeature(),
                    # Not always specified:
                    'cat': tfds.features.ClassLabel(names=CATEGORIES),
                    'from': tfds.features.Text(),
                    'to': tfds.features.Text(),
                })
            ),
        }),
        supervised_keys=None,
        homepage='https://huggingface.co/datasets/abhayzala/AI2D-Caption',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = {split: JSON_URL_TMPL.format(split=split) for split in SPLITS}
    paths['images'] = IMAGES_URL
    dl_paths = dl_manager.download(paths)

    return {
        split: self._generate_examples(
            split, dl_paths[split], dl_paths['images']
        )
        for split in SPLITS
    }

  def _generate_examples(self, split, json_path, images_path):
    """Yields examples."""
    # Build an images index from JSON:
    json_data = json.loads(json_path.read_text(encoding='utf-8'))
    metadata_by_filename = {}  # Maps from image id/filename to image metadata.
    for image_metadata in json_data:
      metadata_by_filename[image_metadata['image']] = image_metadata
    # Iterate over the images,ß yield the ones present in metadata_by_filename:
    for image_path, file in tfds.download.iter_archive(
        images_path, tfds.download.ExtractMethod.ZIP
    ):
      if not image_path.startswith('ai2d/images/'):
        continue
      image_id = os.path.basename(image_path)
      if (metadata := metadata_by_filename.get(image_id)) is None:
        continue
      # Convert bounding box format from REL_XYXY to TFDS format.
      entities = list(metadata['entities'].values())
      for entity in entities:
        # auditor_llm_training_examples split has non-sense bounds (max<min).
        if (
            bounds := entity.get('bounds')
        ) and split != 'auditor_llm_training_examples':
          xmin, ymin, xmax, ymax = [c / 100.0 for c in bounds]
        else:
          xmin, ymin, xmax, ymax = 0.0, 0.0, 0.0, 0.0
        entity['bounds'] = tfds.features.BBox(ymin, xmin, ymax, xmax)
        entity.setdefault('label', '')
        entity.setdefault('cat', 'unspecified')
        entity.setdefault('from', '')
        entity.setdefault('to', '')
      relationships = metadata.get('relationships', [])
      # ai2d_caption_test.json has a few relationships expressed as a dict.
      if isinstance(relationships, dict):
        relationships = list(relationships.values())
      yield image_id, {
          'image_filename': image_id,
          'image': file,
          'topic': metadata.get('topic', 'unspecified'),
          # layout may be an empty string, hence the following construct.
          'layout': metadata.get('layout', None) or 'unspecified',
          'caption': metadata.get('caption', ''),
          'relationships': relationships,
          'entities': entities,
      }
