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

"""segment_anything dataset."""

import csv
import json
from typing import Dict, List

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_HOMEPAGE_URL = 'https://ai.facebook.com/datasets/segment-anything-downloads'
_LOCAL_LINKS_FILE_NAME = 'segment_anything_links.txt'


def _parse_json(path: epath.Path):
  with path.open() as file:
    return json.load(file)


def _normalize_bbox(
    original_coords: List[int], img_height: int, img_width: int
):
  """Converts from COCO to TFDS format."""
  if len(original_coords) != 4:
    raise ValueError(f'Malformed BBox: {original_coords}')
  # COCO format: [x_min, y_min, width, height] in absolute values.
  x_min, y_min, bbox_width, bbox_height = original_coords
  # TFDS format: [y_min, x_min, y_max, x_max] in normalized values.
  x_max = x_min + bbox_width
  y_max = y_min + bbox_height
  return np.array([
      y_min / img_height,
      x_min / img_width,
      y_max / img_height,
      x_max / img_width,
  ])


def _parse_annotations(original_annotations, img_height: int, img_width: int):
  """Parses annotations to the TFDS format."""
  annotations = []
  for annotation in original_annotations:
    annotation['bbox'] = _normalize_bbox(
        annotation['bbox'], img_height, img_width
    )
    annotation['crop_box'] = _normalize_bbox(
        annotation['crop_box'], img_height, img_width
    )
    annotations.append(annotation)
  return annotations


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for segment_anything dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = (
      f'Download the links file from {_HOMEPAGE_URL}. `manual_dir` should'
      f' contain the links file saved as {_LOCAL_LINKS_FILE_NAME}.'
  )
  # The dataset is ~1000 * 10.5GB = ~10.5TB big, so we try to increase
  # parallelism to download. The default is 50.
  MAX_SIMULTANEOUS_DOWNLOADS = 100

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    annotation_feature = tfds.features.FeaturesDict({
        'area': tfds.features.Scalar(
            dtype=np.uint64, doc='The area in pixels of the mask.'
        ),
        'bbox': tfds.features.BBoxFeature(
            doc='The box around the mask, in TFDS format.'
        ),
        'crop_box': tfds.features.BBoxFeature(
            doc=(
                'The crop of the image used to generate the mask,'
                ' in TFDS format.'
            )
        ),
        'id': tfds.features.Scalar(
            dtype=np.uint64, doc='Identifier for the annotation.'
        ),
        'point_coords': tfds.features.Tensor(
            shape=(1, 2),
            dtype=np.float64,
            doc=(
                'The point coordinates input to the model to generate the mask.'
            ),
        ),
        'predicted_iou': tfds.features.Scalar(
            dtype=np.float64,
            doc="The model's own prediction of the mask's quality.",
        ),
        'segmentation': tfds.features.FeaturesDict(
            {
                'counts': np.str_,
                'size': tfds.features.Tensor(shape=(2,), dtype=np.uint64),
            },
            doc=(
                'Encoded segmentation mask in COCO RLE format (dict'
                ' with keys `size` and `counts`).'
            ),
        ),
        'stability_score': tfds.features.Scalar(
            dtype=np.float64, doc="A measure of the mask's quality."
        ),
    })
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.FeaturesDict({
                'content': tfds.features.Image(doc='Content of the image.'),
                'file_name': np.str_,
                'height': np.uint64,
                'image_id': np.uint64,
                'width': np.uint64,
            }),
            'annotations': tfds.features.Sequence(annotation_feature),
        }),
        homepage=_HOMEPAGE_URL,
        license=f'Custom (see: {_HOMEPAGE_URL})',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path_to_links = dl_manager.manual_dir / _LOCAL_LINKS_FILE_NAME
    dict_of_urls = {}
    with path_to_links.open() as file:
      reader = csv.reader(file, delimiter='\t')
      for i, (name, url) in enumerate(reader):
        # Skip the headers.
        if i == 0:
          continue
        dict_of_urls[name] = url
    paths = dl_manager.download_and_extract(dict_of_urls)
    return {
        'train': self._generate_examples(paths),
    }

  def _generate_examples(self, paths: Dict[str, epath.Path]):
    """Yields examples."""

    def _extract_examples(path: epath.Path) -> List[epath.Path]:
      return list(path.glob('*.jpg'))

    def _process_example(image_path: epath.Path):
      json_content = _parse_json(image_path.parent / f'{image_path.stem}.json')
      image = json_content['image']
      image['content'] = image_path
      height, width = image['height'], image['width']
      assert height != 0 and width != 0, f'The image {image_path} is malformed.'
      annotations = _parse_annotations(
          json_content['annotations'], height, width
      )
      return image['image_id'], {
          'image': image,
          'annotations': annotations,
      }

    beam = tfds.core.lazy_imports.apache_beam
    return (
        beam.Create(paths.values())
        | beam.FlatMap(_extract_examples)
        | beam.Map(_process_example)
    )
