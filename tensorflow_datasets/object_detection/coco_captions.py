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

"""COCO 2014 dataset with caption annotations and splits from Karpathy and Li."""

from __future__ import annotations

import collections
import json
import os

from absl import logging
from etils import epath
import numpy as np
from tensorflow_datasets.object_detection import coco
import tensorflow_datasets.public_api as tfds

_EXTRA_CITATION = """\
@inproceedings{DBLP:conf/cvpr/KarpathyL15,
  author    = {Andrej Karpathy and
               Fei{-}Fei Li},
  title     = {Deep visual-semantic alignments for generating image
               descriptions},
  booktitle = {{IEEE} Conference on Computer Vision and Pattern Recognition,
               {CVPR} 2015, Boston, MA, USA, June 7-12, 2015},
  pages     = {3128--3137},
  publisher = {{IEEE} Computer Society},
  year      = {2015},
  url       = {https://doi.org/10.1109/CVPR.2015.7298932},
  doi       = {10.1109/CVPR.2015.7298932},
  timestamp = {Wed, 16 Oct 2019 14:14:50 +0200},
  biburl    = {https://dblp.org/rec/conf/cvpr/KarpathyL15.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """COCO is a large-scale object detection, segmentation, and
captioning dataset. This version contains images, bounding boxes, labels, and
captions from COCO 2014, split into the subsets defined by Karpathy and Li
(2015). This effectively divides the original COCO 2014 validation data into
new 5000-image validation and test sets, plus a "restval" set containing the
remaining ~30k images. All splits have caption annotations.
"""


class CocoCaptions(coco.Coco):
  """Coco captions dataset with the splits defined by Karpathy and Li 2015."""

  # Only coco/2014 has caption annotations.
  BUILDER_CONFIGS = [coco.Coco.BUILDER_CONFIGS[0]]

  def _info(self):
    coco_info = super(CocoCaptions, self)._info()

    features = dict(coco_info.features)
    features['captions'] = tfds.features.Sequence({
        'text': np.str_,
        'id': np.int64,
    })
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage=coco_info.homepage,
        citation=coco_info.citation + _EXTRA_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    # Only keep the coco train and validation sets.
    coco_splits = {
        split.name: split
        for split in super(CocoCaptions, self)._split_generators(dl_manager)
    }
    coco_train_split = coco_splits[tfds.Split.TRAIN]
    coco_val_split = coco_splits[tfds.Split.VALIDATION]

    urls = {}
    urls['karpathy_and_li_splits'] = (
        'https://cs.stanford.edu/people/karpathy/deepimagesent/'
        'caption_datasets.zip'
    )
    extracted_paths = dl_manager.download_and_extract(urls)

    # Load split definitions.
    captions_json_path = os.path.join(
        extracted_paths['karpathy_and_li_splits'], 'dataset_coco.json'
    )
    with epath.Path(captions_json_path).open() as f:
      annotations = json.load(f)['images']

    # split => image filename => annotations
    annotation_maps = collections.defaultdict(dict)
    for annotation in annotations:
      split = annotation['split']
      image_filename = annotation['filename']
      annotation_maps[split][image_filename] = annotation

    return [
        tfds.core.SplitGenerator(
            'train',
            gen_kwargs=dict(
                image_filename_to_annotations=annotation_maps['train'],
                coco_gen_kwargs=coco_train_split.gen_kwargs,
            ),
        ),
        tfds.core.SplitGenerator(
            'val',
            gen_kwargs=dict(
                image_filename_to_annotations=annotation_maps['val'],
                coco_gen_kwargs=coco_val_split.gen_kwargs,
            ),
        ),
        tfds.core.SplitGenerator(
            'test',
            gen_kwargs=dict(
                image_filename_to_annotations=annotation_maps['test'],
                coco_gen_kwargs=coco_val_split.gen_kwargs,
            ),
        ),
        tfds.core.SplitGenerator(
            'restval',
            gen_kwargs=dict(
                image_filename_to_annotations=annotation_maps['restval'],
                coco_gen_kwargs=coco_val_split.gen_kwargs,
            ),
        ),
    ]

  def _generate_examples(self, image_filename_to_annotations, coco_gen_kwargs):
    """Generate examples as dicts.

    Args:
      image_filename_to_annotations: `dict` mapping each image filename to its
        caption annotations.
      coco_gen_kwargs: `dict` of kwargs to forward to Coco._generate_examples().

    Yields:
      example key and data
    """

    num_generated = 0
    for key, example in super(CocoCaptions, self)._generate_examples(
        **coco_gen_kwargs
    ):
      captions = image_filename_to_annotations.get(example['image/filename'])
      if captions is None:
        # Example not in this split.
        continue

      # Add caption annotation.
      example['captions'] = [
          dict(id=caption['sentid'], text=caption['raw'])
          for caption in captions['sentences']
      ]

      num_generated += 1
      yield key, example

    logging.info('Generated %d examples', num_generated)
