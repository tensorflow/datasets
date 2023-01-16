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

"""PASS dataset."""

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URLS = {
    'train_images': [
        tfds.download.Resource(  # pylint:disable=g-complex-comprehension
            url='https://zenodo.org/record/6615455/files/PASS.%s.tar' % i_,
            extract_method=tfds.download.ExtractMethod.TAR,
        )
        for i_ in '0123456789'
    ],
    'meta_data': tfds.download.Resource(
        url='https://zenodo.org/record/6615455/files/pass_metadata.csv'
    ),
}


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for pass dataset."""

  VERSION = tfds.core.Version('3.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '2.0.0': (
          'v2: Removed 472 images from v1 as they contained humans. Also added'
          ' metadata: datetaken and GPS. '
      ),
      '3.0.0': (
          'v3: Removed 131 images from v2 as they contained humans/tattos.'
      ),
  }

  def _info(self):
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 3)),  # The image.
            'image/creator_uname': (
                tfds.features.Text()
            ),  # The photographer/creator.
            'image/hash': (
                tfds.features.Text()
            ),  # The hash, as computed from YFCC-100M.
            'image/gps_lon': tfds.features.Tensor(
                shape=(), dtype=np.float32
            ),  # Longitude of image if existent, otw. NaN.
            'image/gps_lat': tfds.features.Tensor(
                shape=(), dtype=np.float32
            ),  # Latitude of image if existent, otw. NaN.
            'image/date_taken': (
                tfds.features.Text()
            ),  # Datetime of image if not NaN, else empty string.
        }),
        supervised_keys=None,
        homepage='https://www.robots.ox.ac.uk/~vgg/data/pass/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    pd = tfds.core.lazy_imports.pandas
    paths = dl_manager.download(_URLS)
    with tf.io.gfile.GFile(paths['meta_data']) as f:
      meta = pd.read_csv(f)
    meta = meta.set_index('hash')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                parts=paths['train_images'], meta=meta, dl_manager=dl_manager
            ),
        )
    ]

  def _generate_examples(self, dl_manager, parts, meta):
    """Yields examples."""
    i = 0
    for part in parts:
      for fname, fobj in dl_manager.iter_archive(part):
        i += 1
        img_hash = fname.split('/')[-1].split('.')[0]
        img_meta = meta.loc[img_hash]

        record = {
            'image': fobj,
            'image/creator_uname': img_meta['unickname'],
            'image/hash': img_hash,
            'image/gps_lon': (
                img_meta['longitude'] if 'longitude' in img_meta else 0
            ),
            'image/gps_lat': (
                img_meta['latitude'] if 'latitude' in img_meta else 0
            ),
            'image/date_taken': (
                img_meta['datetaken']
                # Filtering out nan values (which are not equal to themselves).
                if img_meta['datetaken'] == img_meta['datetaken']
                else ''
            ),
        }
        yield i, record
