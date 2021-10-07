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

"""Script that prints number of configs for a dataset."""

from absl import app
from absl import flags

import tensorflow_datasets as tfds

FLAGS = flags.FLAGS

flags.DEFINE_string("dataset", None, "DatasetBuilder to print num configs for")


def main(_):
  print(len(tfds.builder(FLAGS.dataset).BUILDER_CONFIGS))


if __name__ == "__main__":
  app.run(main)
