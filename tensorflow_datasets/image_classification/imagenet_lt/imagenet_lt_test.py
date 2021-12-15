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

"""imagenet_lt dataset."""

from tensorflow_datasets.image_classification.imagenet_lt import imagenet_lt
import tensorflow_datasets.public_api as tfds


class ImagenetLtTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for imagenet_lt dataset."""
  # TODO(imagenet_lt):
  DATASET_CLASS = imagenet_lt.ImagenetLt
  SPLITS = {
      'train': 3,  # Number of fake train examples
      'validation': 1,  # Number of fake validation examples
      'test': 10,  # Number of fake test examples
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
      'train': 'train.txt',
      'validation': 'validation.txt',
      'train_path': 'ILSVRC2012_img_train.tar',
      'val_path': 'ILSVRC2012_img_val.tar',
  }

  SKIP_CHECKSUMS = True


if __name__ == '__main__':
  tfds.testing.test_main()
