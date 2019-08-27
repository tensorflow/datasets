# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Helper functions to generate fake Cityscapes-like zip archives for testing."""

from tensorflow_datasets.testing.fake_data_utils import get_random_png

import re
from os import path
from zipfile import ZipFile
from random import randint


CITY_IN_ID_RE = re.compile(r'(.+)_[0-9]+_[0-9]+')


def generate_ids(city, num=2):
  for _ in range(num):
    yield '{}_{:06d}_{:06d}'.format(city, randint(0, 999999), randint(0, 999999))


def create_zipfile(zip_filepath, splits_with_ids, suffixes=['leftImg8bit'],
                   maindir=None):
  """
  Generates a zipfile with a cityscapes-like file structure and random pngs.

  Args:
    zip_filepath (str): filepath to the zip archive that will be created
    splits_with_ids (Dict[str, List[str]]): data-splits like 'train' or 'val' that map to
        a list of image ids
    suffixes (List[str]): suffix per modality that should be created e.g. 'leftImg8bit'
    maindir (str): name of the root directory of the zipfile, defaults to the name of the
        zipfile
  """
  with ZipFile(zip_filepath, 'w') as z:
    for split, ids in splits_with_ids.items():
      if maindir is None:
        maindir = path.basename(zip_filepath).strip('.zip')
      split = path.join(maindir, split)
      for img_id in ids:
        city = CITY_IN_ID_RE.match(img_id).group(1)
        for suffix in suffixes:
          if 'Img' in suffix:
            img = get_random_png(height=1024, width=2048, channels=3)
          else:
            img = get_random_png(height=1024, width=2048, channels=1)
          z.write(img, path.join(split, city, '{}_{}.png'.format(img_id, suffix)))
