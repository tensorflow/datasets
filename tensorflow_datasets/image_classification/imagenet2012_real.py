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

"""Imagenet val. annotated by ReaL labels (https://arxiv.org/abs/2006.07159)."""

import json
import os
import tarfile

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = '''\
This dataset contains ILSVRC-2012 (ImageNet) validation images augmented with a
new set of "Re-Assessed" (ReaL) labels from the "Are we done with ImageNet"
paper, see https://arxiv.org/abs/2006.07159. These labels are collected using
the enhanced protocol, resulting in multi-label and more accurate annotations.

Important note: about 3500 examples contain no label, these should be [excluded
from the averaging when computing the accuracy](https://github.com/google-research/reassessed-imagenet#numpy).
One possible way of doing this is with the following NumPy code:

```python
is_correct = [pred in real_labels[i] for i, pred in enumerate(predictions) if real_labels[i]]
real_accuracy = np.mean(is_correct)
```
'''

_CITATION = '''\
@article{beyer2020imagenet,
  title={Are we done with ImageNet?},
  author={Lucas Beyer and Olivier J. Henaff and Alexander Kolesnikov and Xiaohua Zhai and Aaron van den Oord},
  journal={arXiv preprint arXiv:2002.05709},
  year={2020}
}
@article{ILSVRC15,
  Author={Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
  Title={{ImageNet Large Scale Visual Recognition Challenge}},
  Year={2015},
  journal={International Journal of Computer Vision (IJCV)},
  doi={10.1007/s11263-015-0816-y},
  volume={115},
  number={3},
  pages={211-252}
}
'''

_VALIDATION_LABELS_FNAME = 'image_classification/imagenet2012_validation_labels.txt'
_LABELS_FNAME = 'image_classification/imagenet2012_labels.txt'

_REAL_LABELS_URL = 'https://raw.githubusercontent.com/google-research/reassessed-imagenet/master/real.json'


class Imagenet2012Real(tfds.core.GeneratorBasedBuilder):
  """ImageNet validation images with ReaL labels."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain `ILSVRC2012_img_val.tar` file.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'original_label': tfds.features.ClassLabel(names_file=names_file),
            'real_label': tfds.features.Sequence(
                tfds.features.ClassLabel(names_file=names_file)),
            'file_name': tfds.features.Text(),
        }),
        supervised_keys=('image', 'real_label'),
        homepage='https://github.com/google-research/reassessed-imagenet',
        citation=_CITATION,
    )

  def _get_real_labels(self, dl_manager):
    with tf.io.gfile.GFile(dl_manager.download(_REAL_LABELS_URL), 'r') as f:
      # ReaL labels are ordered in the lexicographical order.
      return {'ILSVRC2012_val_{:08}.JPEG'.format(i + 1): labels
              for i, labels in enumerate(json.load(f))}

  @staticmethod
  def _get_original_labels(val_path):
    """Returns labels for validation.

    Args:
      val_path: path to TAR file containing validation images. It is used to
      retrieve the name of pictures and associate them to labels.

    Returns:
      dict, mapping from image name (str) to label (str).
    """
    labels_path = os.fspath(tfds.core.tfds_path(_VALIDATION_LABELS_FNAME))
    with tf.io.gfile.GFile(labels_path) as labels_f:
      # `splitlines` to remove trailing `\r` in Windows
      labels = labels_f.read().strip().splitlines()
    with tf.io.gfile.GFile(val_path, 'rb') as tar_f_obj:
      tar = tarfile.open(mode='r:', fileobj=tar_f_obj)
      images = sorted(tar.getnames())
    return dict(zip(images, labels))

  def _split_generators(self, dl_manager):
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    if not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}'.format(val_path))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'archive': dl_manager.iter_archive(val_path),
                'original_labels': self._get_original_labels(val_path),
                'real_labels': self._get_real_labels(dl_manager),
            },
        ),
    ]

  def _generate_examples(self, archive, original_labels, real_labels):
    for fname, fobj in archive:
      record = {
          'file_name': fname,
          'image': fobj,
          'original_label': original_labels[fname],
          'real_label': real_labels[fname],
      }
      yield fname, record
