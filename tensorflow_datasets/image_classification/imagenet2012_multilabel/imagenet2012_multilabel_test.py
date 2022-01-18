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

"""imagenet2012_multilabel dataset."""

from tensorflow_datasets.image_classification.imagenet2012_multilabel import imagenet2012_multilabel
import tensorflow_datasets.public_api as tfds


class Imagenet2012MultilabelTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for imagenet2012_multilabel dataset."""
  DATASET_CLASS = imagenet2012_multilabel.Imagenet2012Multilabel
  SPLITS = {'validation': 3}  # Number of fake validation examples
  DL_DOWNLOAD_RESULT = 'human_accuracy_fixed.json'

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == '__main__':
  tfds.testing.test_main()
