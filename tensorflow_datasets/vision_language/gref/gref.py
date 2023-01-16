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

r"""GRef dataset.
"""
from __future__ import annotations

import collections
import json

import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The Google RefExp dataset is a collection of text descriptions of objects in
images which builds on the publicly available MS-COCO dataset. Whereas the
image captions in MS-COCO apply to the entire image, this dataset focuses on
text descriptions that allow one to uniquely identify a single object or region
within an image. See more details in this paper: Generation and Comprehension
of Unambiguous Object Descriptions.
"""

_CITATION = """
@inproceedings{mao2016generation,
  title={Generation and Comprehension of Unambiguous Object Descriptions},
  author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},
  booktitle={CVPR},
  year={2016}
}
"""


def _build_bbox(image_info, x, y, width, height):
  return tfds.features.BBox(
      ymin=y / image_info['height'],
      xmin=x / image_info['width'],
      ymax=(y + height) / image_info['height'],
      xmax=(x + width) / image_info['width'],
  )


def _combine_gref_anns(gref_anns):
  """Reorganize G-Ref by matching annotations to image_id.

  Also map referring expressions to annotation id.
  Args:
    gref_anns: a dict of gref_anns annotations.

  Returns:
    combine_anns: a list of dict based on gref_anns['images'].
      Each dict has a key 'instances' corresponding to a list of annotations
      of that image.
  """
  img_id2annotations = collections.defaultdict(list)
  for _, v in gref_anns['annotations'].items():
    # Add ref expression to annotation.
    # this adds the referent, the raw string, tokens, and the referring
    # expression id to the annotation.
    ref_list = []
    for rexp_id in sorted(v['refexp_ids']):
      r = gref_anns['refexps'][str(rexp_id)]
      if 'word' in r['parse']['referent']:
        r['referent'] = r['parse']['referent']['word']
      else:
        r['referent'] = ''
      r.pop('parse')
      ref_list.append(r)

    v['refexps'] = ref_list
    img_id2annotations[int(v['image_id'])].append(v)

  img_id2annotations = {
      k: list(sorted(v, key=lambda a: a['annotation_id']))
      for k, v in img_id2annotations.items()
  }
  combined_anns = []
  for _, v in gref_anns['images'].items():
    v['instances'] = img_id2annotations[v['image_id']]
    combined_anns.append((v['image_id'], v))

  combined_anns = sorted(combined_anns, key=lambda a: a[0])
  return combined_anns


class Gref(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for gref dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """
    Follow instructions at https://github.com/mjhucla/Google_Refexp_toolbox
    to download and pre-process the data into aligned format with COCO.
    The directory contains 2 files and one folder:
    * google_refexp_train_201511_coco_aligned_catg.json
    * google_refexp_val_201511_coco_aligned_catg.json
    * coco_train2014/

    The coco_train2014 folder contains all of COCO 2014 training images.
    """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        # Description and homepage used for documentation
        description=_DESCRIPTION,
        homepage='https://github.com/mjhucla/Google_Refexp_toolbox',
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'image/id': np.int64,
            'objects': tfds.features.Sequence({
                'id': np.int64,
                'area': np.int64,
                'bbox': tfds.features.BBoxFeature(),
                'label': np.int64,
                'label_name': tfds.features.ClassLabel(num_classes=80),
                'refexp': tfds.features.Sequence({
                    'refexp_id': np.int64,
                    'tokens': tfds.features.Sequence(tfds.features.Text()),
                    'referent': tfds.features.Text(),
                    'raw': tfds.features.Text(),
                }),
            }),
        }),
        # If there's a common `(input, target)` tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=None,
        # Bibtex citation for the dataset
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    coco_image_dir = dl_manager.manual_dir / 'coco_train2014'
    gref_aligned_json_train = (
        dl_manager.manual_dir
        / 'google_refexp_train_201511_coco_aligned_catg.json'
    )
    gref_aligned_json_val = (
        dl_manager.manual_dir
        / 'google_refexp_val_201511_coco_aligned_catg.json'
    )
    # Specify the splits
    return {
        tfds.Split.TRAIN: self._generate_examples(
            coco_image_dir,
            gref_aligned_json_train,
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            coco_image_dir,
            gref_aligned_json_val,
        ),
    }

  def _generate_examples(self, image_dir, gref_aligned_json):
    """Yields examples."""
    gref_anns = json.loads(gref_aligned_json.read_text())

    categories_id2name = {c['id']: c['name'] for c in gref_anns['categories']}
    self.info.features['objects']['label_name'].names = [
        c['name'] for c in gref_anns['categories']
    ]
    gref_anns = _combine_gref_anns(gref_anns)
    for image_id, image_ann in gref_anns:
      image_path = image_dir / image_ann['file_name']
      example = {
          'image': image_path,
          'image/id': image_id,
          'objects': [],
      }
      for inst in image_ann['instances']:
        # build instance dictionary
        example['objects'].append({
            'id': inst['annotation_id'],
            'area': inst['area'],
            'bbox': _build_bbox(image_ann, *inst['bbox']),
            'label': inst['category_id'],  # 1-index.
            'label_name': categories_id2name[inst['category_id']],
            'refexp': inst['refexps'],
        })
      yield image_id, example
