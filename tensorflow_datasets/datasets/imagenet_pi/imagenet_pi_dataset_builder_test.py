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

from tensorflow_datasets.datasets.imagenet_pi import imagenet_pi_dataset_builder
import tensorflow_datasets.public_api as tfds


class ImagenetPiTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for imagenet_pi dataset."""

  DATASET_CLASS = imagenet_pi_dataset_builder.Builder
  SPLITS = {
      'train': 100,  # Number of fake train example.
      'validation': 10,  # Number of fake validation example.
  }

  DL_EXTRACT_RESULT = {
      'labels_train': 'labels/train.csv',
      'labels_validation': 'labels/validation.csv',
      'confidences_train': 'confidences/train.csv',
      'confidences_validation': 'confidences/validation.csv',
      'train_path': 'ILSVRC2012_img_train.tar',
      'val_path': 'ILSVRC2012_img_val.tar',
  }

  SKIP_CHECKSUMS = True


if __name__ == '__main__':
  tfds.testing.test_main()
