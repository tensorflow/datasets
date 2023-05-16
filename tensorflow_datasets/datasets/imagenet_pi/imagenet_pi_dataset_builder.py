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

"""imagenet_pi dataset."""

import io
import os
from etils import epath
import numpy as np

from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

NUM_MODEL_ANNOTATORS = 16


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for imagenet_pi dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain two files: ILSVRC2012_img_train.tar and
  ILSVRC2012_img_val.tar.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'clean_label': tfds.features.ClassLabel(names_file=names_file),
            'annotator_labels': tfds.features.Tensor(
                shape=(NUM_MODEL_ANNOTATORS,), dtype=np.int64
            ),
            'annotator_confidences': tfds.features.Tensor(
                shape=(NUM_MODEL_ANNOTATORS,), dtype=np.float32
            ),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'.
        }),
        supervised_keys=('image', 'annotator_labels'),
        homepage='https://github.com/google-research-datasets/imagenet_pi/',
    )

  def _get_values_from_csv(self, input_csv, to_type=int):
    """Gets the annotator labels from the csv lines list."""
    # The input_csv contains lines such as
    # n02097047_2079.JPEG,165,196,196,196,196,196,196,196.
    values_dict = {}
    for cur_line in input_csv:
      elems = cur_line.split(',')
      filename = elems[0]
      values = [to_type(elem) for elem in elems[1:]]
      assert len(values) == NUM_MODEL_ANNOTATORS
      values_dict[filename] = values
    return values_dict

  def _assertion_error_msg(self, missing_item: str, path: str) -> str:
    return (
        f'ImageNet-PI requires manual download of the {missing_item}. '
        f'Please download them and place them into: {path}'
    )

  def _get_train_annotator_labels(self, dl_manager):
    labels_path = dl_manager.manual_dir / 'labels' / 'train.csv'
    labels_path = epath.Path(labels_path)
    if not labels_path.exists():
      raise AssertionError(
          self._assertion_error_msg(
              'train annotator labels', os.fspath(labels_path)
          )
      )
    return self._get_values_from_csv(labels_path.read_text().splitlines())

  def _get_validation_annotator_labels(self, dl_manager):
    labels_path = dl_manager.manual_dir / 'labels' / 'validation.csv'
    labels_path = epath.Path(labels_path)
    if not labels_path.exists():
      raise AssertionError(
          self._assertion_error_msg(
              'validation annotator labels', os.fspath(labels_path)
          )
      )
    return self._get_values_from_csv(labels_path.read_text().splitlines())

  def _get_train_annotator_confidences(self, dl_manager):
    confidences_path = dl_manager.manual_dir / 'confidences' / 'train.csv'
    confidences_path = epath.Path(confidences_path)
    if not confidences_path.exists():
      raise AssertionError(
          self._assertion_error_msg(
              'train annotator confidences', os.fspath(confidences_path)
          )
      )
    return self._get_values_from_csv(
        confidences_path.read_text().splitlines(), to_type=float
    )

  def _get_validation_annotator_confidences(self, dl_manager):
    confidences_path = dl_manager.manual_dir / 'confidences' / 'validation.csv'
    confidences_path = epath.Path(confidences_path)
    if not confidences_path.exists():
      raise AssertionError(
          self._assertion_error_msg(
              'validation annotator confidences', os.fspath(confidences_path)
          )
      )
    return self._get_values_from_csv(
        confidences_path.read_text().splitlines(), to_type=float
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    train_path = dl_manager.manual_dir / 'ILSVRC2012_img_train.tar'
    val_path = dl_manager.manual_dir / 'ILSVRC2012_img_val.tar'

    if not train_path.exists() or not val_path.exists():
      raise AssertionError(
          'ImageNet-PI requires manual download of the ImageNet2012 data. '
          'Please download the train and val set and place them into:'
          '{}, {}'.format(train_path, val_path)
      )

    return {
        'train': self._generate_examples(
            archive=dl_manager.iter_archive(train_path),
            annotator_labels=self._get_train_annotator_labels(dl_manager),
            annotator_confidences=self._get_train_annotator_confidences(
                dl_manager
            ),
            validation_labels=None,
        ),
        'validation': self._generate_examples(
            archive=dl_manager.iter_archive(val_path),
            annotator_labels=self._get_validation_annotator_labels(dl_manager),
            annotator_confidences=self._get_validation_annotator_confidences(
                dl_manager
            ),
            validation_labels=imagenet_common.get_validation_labels(val_path),
        ),
    }

  def _generate_examples(
      self,
      archive,
      annotator_labels,
      annotator_confidences,
      validation_labels=None,
  ):
    # Validation split.
    if validation_labels:
      for fname, fobj in archive:
        assert fname in validation_labels
        assert fname in annotator_labels
        assert fname in annotator_confidences
        record = {
            'file_name': fname,
            'image': fobj,
            'clean_label': validation_labels[fname],
            'annotator_labels': annotator_labels[fname],
            'annotator_confidences': annotator_confidences[fname],
        }
        yield fname, record

    # Training split. Main archive contains archives names after a synset noun.
    # Each sub-archive contains pictures associated to that synset.
    for fname, fobj in archive:
      assert fname.endswith('.tar')
      label = fname[:-4]  # fname is something like 'n01632458.tar'
      fobj_mem = io.BytesIO(fobj.read())
      for image_fname, image in tfds.download.iter_archive(
          fobj_mem, tfds.download.ExtractMethod.TAR_STREAM
      ):
        record = {
            'file_name': image_fname,
            'image': image,
            'clean_label': label,
            'annotator_labels': annotator_labels[image_fname],
            'annotator_confidences': annotator_confidences[image_fname],
        }
        yield image_fname, record
