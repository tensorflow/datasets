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

"""iNaturalist2021 dataset."""

import json
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The iNaturalist dataset 2021 contains a total of 10,000 species. 
The full training dataset contains nearly 2.7M images. 
To make the dataset more accessible we have also created a "mini" training 
dataset with 50 examples per species for a total of 500K images. The full 
training `train` split overlaps with the `mini` split. The val set contains for
each species 10 validation images (100K in total). There are a total of 500,000 
test images in the `public_test` split (without ground-truth labels).
"""

_CITATION = r"""\
@misc{inaturalist21,
    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2021}},
    Title = {{iNaturalist} 2021 competition dataset.},
    Year = {2021},
    key = {{iNaturalist} 2021 competition dataset},
    }
"""

_URL = 'https://ml-inat-competition-datasets.s3.amazonaws.com/2021'
_HOMEPAGE = 'https://github.com/visipedia/inat_comp/tree/master/2021'
_SPLIT_FILENAMES = {
    'train': 'train',
    'mini': 'train_mini',
    'val': 'val',
    'test': 'public_test',
}


class INaturalist2021(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for iNaturalist 2021 Competition dataset."""

  VERSION = tfds.core.Version('2.0.1')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '2.0.0': 'Update: Class indices follow the order in the JSON train file.',
      '2.0.1': 'Update: Include the example id as provided in the JSON files.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Scalar(dtype=np.int64),
            'file_id': tfds.features.Text(),
            'image': tfds.features.Image(shape=(None, None, 3)),
            'label': tfds.features.ClassLabel(
                names_file=tfds.core.tfds_path(
                    os.path.join(
                        'image_classification',
                        'i_naturalist2021',
                        'i_naturalist2021_labels_ordered_by_json_id.txt',
                    )
                )
            ),
            'supercategory': tfds.features.ClassLabel(
                names_file=tfds.core.tfds_path(
                    os.path.join(
                        'image_classification',
                        'i_naturalist2021',
                        'i_naturalist2021_supercategories.txt',
                    )
                )
            ),
        }),
        supervised_keys=('image', 'label'),
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    split_downloads = {}
    for split, split_file in _SPLIT_FILENAMES.items():
      split_downloads[f'{split}_img'] = tfds.download.Resource(
          url=f'{_URL}/{split_file}.tar.gz',
          extract_method=tfds.download.ExtractMethod.NO_EXTRACT,
      )
      split_downloads[f'{split}_json'] = f'{_URL}/{split_file}.json.tar.gz'

    output_paths = dl_manager.download_and_extract(split_downloads)
    generate_dict = {}
    for split, split_file in _SPLIT_FILENAMES.items():
      generate_dict[split] = self._generate_examples(
          images_archive=dl_manager.iter_archive(output_paths[f'{split}_img']),
          json_file=os.path.join(
              output_paths[f'{split}_json'], f'{split_file}.json'
          ),
      )

    return generate_dict

  def _generate_examples(self, images_archive, json_file):
    """Generate examples."""
    # Training and validation images.
    with epath.Path(json_file).open('r') as f:
      inat_json = json.load(f)

    def _format(label: str):
      return label.lower().replace(' ', '_')

    def _get_annotation(idx, image_id):
      if 'annotations' in inat_json:
        annotation = inat_json['annotations'][idx]
        assert annotation['image_id'] == image_id
        cat = inat_json['categories'][annotation['category_id']]
        category = _format(cat['name'])
        supercategory = _format(cat['supercategory'])
      else:
        category, supercategory = -1, -1
      return category, supercategory

    fileid2data = {}
    for idx, image in enumerate(inat_json['images']):
      category, supercategory = _get_annotation(idx, image['id'])
      fileid = os.path.basename(image['file_name']).split('.')[0]
      fileid2data[fileid] = {
          'id': image['id'],
          'file_id': fileid,
          'label': category,
          'supercategory': supercategory,
      }

    # Read tar.gz file containing images and yield relevant examples.
    for fpath, fobj in images_archive:
      fileid = os.path.basename(fpath).split('.')[0]
      if fileid in fileid2data:
        data = fileid2data[fileid].copy()
        data['image'] = fobj
        yield data['id'], data
