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

"""RefCoco datasets."""

from __future__ import annotations

import collections
import json
import operator

import numpy as np
import tensorflow_datasets.public_api as tfds


def _build_bbox(image_info, x, y, width, height):
  """Calculates the coordinates of a bbox."""
  return tfds.features.BBox(
      ymin=y / image_info['height'],
      xmin=x / image_info['width'],
      ymax=(y + height) / image_info['height'],
      xmax=(x + width) / image_info['width'],
  )


def _extract_annotation(ann, image_info):
  """Extracts the bounding box annotation information."""
  return {
      'id': ann['id'],
      'area': ann['area'],
      'bbox': _build_bbox(image_info, *ann['bbox']),
      'label': ann['category_id'],
  }


def _generate_examples(refcoco_json, dataset, dataset_partition, split):
  """Generates examples of images and its refexps & ground truth bboxes.

  Args:
    refcoco_json: contents of the annotation file.
    dataset: str specifying the dataset (refcoco, refcoco+, refcocog)
    dataset_partition: str specifying the partition for the dataset
    split: str specifying the split of the dataset_partition

  Yields:
    image_id and example tuple
  """
  refcoco_anns = refcoco_json['ref']
  coco_anns = refcoco_json['coco_anns']

  # Collect all referring expressions for a given image.
  imageid2annref = collections.defaultdict(list)
  for r in refcoco_anns:
    if (
        r['dataset'] == dataset
        and r['dataset_partition'] == dataset_partition
        and r['split'] == split
    ):
      imageid2annref[r['image_id']].append(r)

  # Process all the referring expressions and ground truth annotations for
  # a given COCO image.
  for image_id in sorted(imageid2annref.keys()):
    coco_image = coco_anns[str(image_id)]
    image_info = coco_image['info']
    example = {
        'image_filename': image_info['file_name'],
        'image/id': image_id,
        'coco_annotations': [],
        'objects': [],
    }

    # Collect ground truth bboxes.
    for ann in sorted(coco_image['anns'], key=operator.itemgetter('id')):
      example['coco_annotations'].append(_extract_annotation(ann, image_info))

    # Collect referring expressions.
    for r in sorted(
        imageid2annref[image_id], key=operator.itemgetter('ref_id')
    ):
      obj = _extract_annotation(r['ann'], image_info)

      refexp = []
      for s in sorted(r['sentences'], key=operator.itemgetter('sent_id')):
        refexp.append({
            'raw': s['raw'],
            'refexp_id': s['sent_id'],
        })

      # Match the referring expression to its corresponding bbox in the ground
      # truth list.
      gt_box_index = [
          i
          for i, v in enumerate(example['coco_annotations'])
          if v['id'] == r['ann']['id']
      ]
      if len(gt_box_index) != 1:
        raise ValueError(f'gt_box_index does not have length 1: {gt_box_index}')
      gt_box_index = gt_box_index[0]

      obj.update({
          'refexp': refexp,
          'gt_box_index': gt_box_index,
      })
      example['objects'].append(obj)

    yield image_id, example


class RefCocoConfig(tfds.core.BuilderConfig):
  """Config to specify each RefCoco variant."""

  def __init__(self, dataset, dataset_partition, **kwargs):
    name = f'{dataset}_{dataset_partition}'
    super(RefCocoConfig, self).__init__(name=name, **kwargs)
    self.dataset = dataset
    self.dataset_partition = dataset_partition


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for RefCoco datasets."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  1. Follow the instructions in https://github.com/lichengunc/refer and
  download the annotations and the images, matching the data/ directory
  specified in the repo.

  2. Follow the instructions of PythonAPI in
  https://github.com/cocodataset/cocoapi to get pycocotools and the
  instances_train2014 annotations file from https://cocodataset.org/#download

  3. Add both refer.py from (1) and pycocotools from (2) to your PYTHONPATH.

  4. Run manual_download_process.py to generate refcoco.json, replacing
  `ref_data_root`, `coco_annotations_file`, and `out_file` with the values
  corresponding to where you have downloaded / want to save these files.
  Note that manual_download_process.py can be found in the TFDS repository.

  5. Download the COCO training set from https://cocodataset.org/#download
  and stick it into a folder called `coco_train2014/`. Move `refcoco.json`
  to the same level as `coco_train2014`.

  6. Follow the standard manual download instructions.
  """

  BUILDER_CONFIGS = [
      RefCocoConfig(dataset='refcoco', dataset_partition='unc'),
      RefCocoConfig(dataset='refcoco', dataset_partition='google'),
      RefCocoConfig(dataset='refcocoplus', dataset_partition='unc'),
      RefCocoConfig(dataset='refcocog', dataset_partition='google'),
      RefCocoConfig(dataset='refcocog', dataset_partition='umd'),
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        homepage='https://github.com/lichengunc/refer',
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'image/id': np.int64,
            'objects': tfds.features.Sequence({
                'id': np.int64,
                'area': np.int64,
                'bbox': tfds.features.BBoxFeature(),
                'label': np.int64,
                'gt_box_index': np.int64,
                'refexp': tfds.features.Sequence({
                    'refexp_id': np.int64,
                    'raw': tfds.features.Text(),
                }),
            }),
            'coco_annotations': tfds.features.Sequence({
                'id': np.int64,
                'area': np.int64,
                'bbox': tfds.features.BBoxFeature(),
                'label': np.int64,
            }),
        }),
        supervised_keys=None,
    )

  def _split_generators(self, dl_manager):
    allowed_splits = {
        ('refcoco', 'google'): [
            tfds.Split.TRAIN,
            tfds.Split.VALIDATION,
            tfds.Split.TEST,
        ],
        ('refcoco', 'unc'): [
            tfds.Split.TRAIN,
            tfds.Split.VALIDATION,
            'testA',
            'testB',
        ],
        ('refcocoplus', 'unc'): [
            tfds.Split.TRAIN,
            tfds.Split.VALIDATION,
            'testA',
            'testB',
        ],
        ('refcocog', 'google'): [tfds.Split.TRAIN, tfds.Split.VALIDATION],
        ('refcocog', 'umd'): [
            tfds.Split.TRAIN,
            tfds.Split.VALIDATION,
            tfds.Split.TEST,
        ],
    }
    bc = self.builder_config
    splits = allowed_splits[(bc.dataset, bc.dataset_partition)]

    return {
        split: self._generate_examples(
            bc.dataset, bc.dataset_partition, split, dl_manager
        )
        for split in splits
    }

  def _generate_examples(self, dataset, dataset_partition, split, dl_manager):
    refcoco_json = json.loads(
        (dl_manager.manual_dir / 'refcoco.json').read_text()
    )
    coco_dir = dl_manager.manual_dir / 'coco_train2014'

    if dataset == 'refcocoplus':
      dataset = 'refcoco+'
    if split == tfds.Split.VALIDATION:
      split = 'val'

    for image_id, example in _generate_examples(
        refcoco_json, dataset, dataset_partition, split
    ):
      example['image'] = coco_dir / example['image_filename']
      del example['image_filename']
      yield image_id, example
