# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
PASS is a large-scale image dataset that does not include any humans,
human parts, or other personally identifiable information.
It that can be used for high-quality self-supervised pretraining while significantly reducing privacy concerns.

PASS contains 1,439,719 images without any labels sourced from YFCC-100M.

All images in this dataset are licenced under the CC-BY licence, as is the dataset itself.
For YFCC-100M see  http://www.multimediacommons.org/.
"""

_CITATION = """
@Article{asano21pass,
author = "Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi",
title = "PASS: An ImageNet replacement for self-supervised pretraining without humans",
journal = "NeurIPS Track on Datasets and Benchmarks",
year = "2021"
}
"""

_URLS = {
    'train_images': [
        tfds.download.Resource(  # pylint:disable=g-complex-comprehension
            url='https://zenodo.org/record/5570664/files/PASS.%s.tar' % i_,
            extract_method=tfds.download.ExtractMethod.TAR)
        for i_ in '0123456789'
    ],
    'meta_data':
        tfds.download.Resource(
            url='https://zenodo.org/record/5570664/files/pass_metadata.csv')
}


class PASS(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for pass dataset."""

  VERSION = tfds.core.Version('2.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '2.0.0':
          'v2: Removed 472 images from v1 as they contained humans. Also added'
          ' metadata: datetaken and GPS. ',
  }

  def _info(self):
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 3)),  # The image.
            'image/creator_uname':
                tfds.features.Text(),  # The photographer/creator.
            'image/hash':
                tfds.features.Text(),  # The hash, as computed from YFCC-100M.
            'image/gps_lon': tfds.features.Tensor(
                shape=(),
                dtype=tf.float32),  # Longitude of image if existent, otw. NaN.
            'image/gps_lat': tfds.features.Tensor(
                shape=(),
                dtype=tf.float32),  # Latitude of image if existent, otw. NaN.
            'image/date_taken': tfds.features.Text(
            ),  # Datetime of image if not NaN, else empty string.
        }),
        supervised_keys=None,
        homepage='https://www.robots.ox.ac.uk/~vgg/research/pass/',
        citation=_CITATION,
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
                parts=paths['train_images'], meta=meta, dl_manager=dl_manager),
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
            'image':
                fobj,
            'image/creator_uname':
                img_meta['unickname'],
            'image/hash':
                img_hash,
            'image/gps_lon':
                img_meta['longitude'] if 'longitude' in img_meta else 0,
            'image/gps_lat':
                img_meta['latitude'] if 'latitude' in img_meta else 0,
            'image/date_taken':
                img_meta['datetaken']
                if img_meta['datetaken'] == img_meta['datetaken'] else ''
        }
        yield i, record
