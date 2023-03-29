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

"""Imagenet validation with multi-label annotations (http://proceedings.mlr.press/v119/shankar20c.html).
"""

import json
import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

_MULTI_LABELS_URL = 'https://storage.googleapis.com/brain-car-datasets/imagenet-mistakes/human_accuracy_v3.0.0.json'


def _get_multi_labels_and_problematic_images(
    dl_manager: tfds.download.DownloadManager,
):
  """Returns multi-labels and problematic images from download json.

  Args:
    dl_manager: tfds.download.DownloadManager for downloading the json file

  Returns:
    val_annotated_images: Dictionary mapping image name to an inner dictionary
      containing the multi_label annotations for that image. The inner multi-
      label annotation dictionary has keys 'correct', 'wrong', or 'unclear'
      (keys will be missing if the image does not have a set of labels of the
      given type) and values that are lists of wnids.
    problematic_images: List of image names for problematic images.
    imagenet_m_2022:  List of image names comprising ImageNet-M 2022 evaluation
      slice.
  """
  with tf.io.gfile.GFile(dl_manager.download(_MULTI_LABELS_URL), 'r') as f:
    human_accuracy_data = json.load(f)
  val_annotated_images = {}
  prefix = 'ILSVRC2012_val_'
  len_prefix = len(prefix)
  for image_name in human_accuracy_data['initial_annots'].keys():
    if image_name[:len_prefix] == prefix:
      val_annotated_images[image_name] = human_accuracy_data['initial_annots'][
          image_name
      ]

  problematic_images = list(human_accuracy_data['problematic_images'].keys())
  imagenet_m_2022 = human_accuracy_data['imagenet_m']
  return val_annotated_images, problematic_images, imagenet_m_2022


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for imagenet2012_multilabel dataset."""

  VERSION = tfds.core.Version('3.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '2.0.0': 'Fixed ILSVRC2012_img_val.tar file.',
      '3.0.0': 'Corrected labels and ImageNet-M split.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain `ILSVRC2012_img_val.tar` file.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'original_label': tfds.features.ClassLabel(names_file=names_file),
            'correct_multi_labels': tfds.features.Sequence(
                tfds.features.ClassLabel(names_file=names_file)
            ),
            'wrong_multi_labels': tfds.features.Sequence(
                tfds.features.ClassLabel(names_file=names_file)
            ),
            'unclear_multi_labels': tfds.features.Sequence(
                tfds.features.ClassLabel(names_file=names_file)
            ),
            'is_problematic': tfds.features.Tensor(shape=(), dtype=np.bool_),
            'file_name': tfds.features.Text(),
        }),
        supervised_keys=('image', 'correct_multi_labels'),
        homepage='https://github.com/modestyachts/evaluating_machine_accuracy_on_imagenet',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    if not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}'.format(val_path)
      )

    original_labels = imagenet_common.get_validation_labels(val_path)

    (multi_labels, problematic_images, imagenet_m_2022_errors) = (
        _get_multi_labels_and_problematic_images(dl_manager)
    )

    imagenet_m_2022 = dict(
        [(k, multi_labels[k]) for k in imagenet_m_2022_errors]
    )

    return {
        'validation': self._generate_examples(
            archive=dl_manager.iter_archive(val_path),
            original_labels=original_labels,
            multi_labels=multi_labels,
            problematic_images=problematic_images,
        ),
        'imagenet_m': self._generate_examples(
            archive=dl_manager.iter_archive(val_path),
            original_labels=original_labels,
            multi_labels=imagenet_m_2022,
            problematic_images=problematic_images,
        ),
    }

  def _generate_examples(
      self, archive, original_labels, multi_labels, problematic_images
  ):
    """Yields (key, example) tuples from the dataset."""
    for fname, fobj in archive:
      if fname not in multi_labels:
        # Image is not in the annotated set of 20,000 images
        continue
      else:
        is_problematic = fname in problematic_images
        correct_multi_labels = []
        wrong_multi_labels = []
        unclear_multi_labels = []
        if 'correct' in multi_labels[fname]:
          correct_multi_labels = multi_labels[fname]['correct']
        if 'wrong' in multi_labels[fname]:
          wrong_multi_labels = multi_labels[fname]['wrong']
        if 'unclear' in multi_labels[fname]:
          unclear_multi_labels = multi_labels[fname]['unclear']

      record = {
          'file_name': fname,
          'image': fobj,
          'original_label': original_labels[fname],
          'correct_multi_labels': correct_multi_labels,
          'wrong_multi_labels': wrong_multi_labels,
          'unclear_multi_labels': unclear_multi_labels,
          'is_problematic': is_problematic,
      }
      yield fname, record
