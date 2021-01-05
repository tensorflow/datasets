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

"""s3o4d dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.image.s3o4d import s3o4d


class S3o4dTest(testing.DatasetBuilderTestCase):
  """Tests for s3o4d dataset."""
  DATASET_CLASS = s3o4d.S3o4d
  SPLITS = {
      'bunny_train': 3,  # Number of fake train example
      'bunny_test': 1,  # Number of fake test example
      'dragon_train': 3,
      'dragon_test': 1,
  }

  DL_EXTRACT_RESULT = {
      'bunny_train_img': 'bunny/train_images.zip',
      'bunny_test_img': 'bunny/test_images.zip',
      'dragon_train_img': 'dragon/train_images.zip',
      'dragon_test_img': 'dragon/test_images.zip',
      'bunny_train_latent': 'bunny/train_latents.npz',
      'bunny_test_latent': 'bunny/test_latents.npz',
      'dragon_train_latent': 'dragon/train_latents.npz',
      'dragon_test_latent': 'dragon/test_latents.npz',
  }

if __name__ == '__main__':
  testing.test_main()
