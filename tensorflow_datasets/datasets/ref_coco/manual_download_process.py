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

"""Script to manually process RefCoco datasets.

Follow the instructions in the TFDS description.
"""

import json

from pycocotools.coco import COCO
from refer import REFER


def main():
  ref_data_root = '<path/to/refer/data/folder>'
  all_refs = []
  for dataset, split_bys in [
      ('refcoco', ['google', 'unc']),
      ('refcoco+', ['unc']),
      ('refcocog', ['google', 'umd']),
  ]:
    for split_by in split_bys:
      refer = REFER(ref_data_root, dataset, split_by)
      for ref_id in refer.getRefIds():
        ref = refer.Refs[ref_id]
        ann = refer.refToAnn[ref_id]
        ref['ann'] = ann
        ref['dataset'] = dataset
        ref['dataset_partition'] = split_by
        all_refs.append(ref)

  coco_annotations_file = '<path/to/instances_train2014.json>'
  coco = COCO(coco_annotations_file)
  ref_image_ids = set(x['image_id'] for x in all_refs)
  coco_anns = {
      image_id: {'info': coco.imgs[image_id], 'anns': coco.imgToAnns[image_id]}
      for image_id in ref_image_ids
  }

  out_file = '<path/to/refcoco.json>'
  with open(out_file, 'w') as f:
    json.dump({'ref': all_refs, 'coco_anns': coco_anns}, f)


if __name__ == '__main__':
  main()
