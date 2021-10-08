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

PASS contains 1.440.191 images without any labels sourced from YFCC-100M.

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
            url=f'https://zenodo.org/record/5528345/files/PASS.{i}.tar',
            extract_method=tfds.download.ExtractMethod.TAR) for i in range(10)
    ],
    'meta_data':
        tfds.download.Resource(
            url='https://zenodo.org/record/5528345/files/pass_metadata.csv')
}


class PASS(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for pass dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self):
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 3)),
            'image/creator_uname': tf.string,
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
    meta = {m[1]['hash']: m[1]['unickname'] for m in meta.iterrows()}
    return {
        'train':
            self._generate_examples(dl_manager, paths['train_images'], meta)
    }

  def _generate_examples(self, dl_manager, parts, meta):
    """Yields examples."""
    i = 0
    for part in parts:
      for fname, fobj in dl_manager.iter_archive(part):
        i += 1
        record = {
            'image': fobj,
            'image/creator_uname': meta[fname.split('/')[-1].split('.')[0]]
        }
        yield i, record
