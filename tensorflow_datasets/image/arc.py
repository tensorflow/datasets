# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""ARC dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{chollet_françois_2019,
  title     = {The Measure of Intelligence},
  url       = {https://arxiv.org/abs/1911.01547},
  journal   = {arXiv.org},
  author    = {François Chollet},
  year      = {2019},
  month     = {Nov}
}
"""

_DESCRIPTION = """
ARC can be seen as a general artificial intelligence benchmark, as a program
synthesis benchmark, or as a psychometric intelligence test. It is targeted at
both humans and artificially intelligent systems that aim at emulating a
human-like form of general fluid intelligence.
"""


_BASE_URL = "https://github.com/fchollet/ARC/"
_COMMIT = "34bc532"
_DL_URL = _BASE_URL + f"zipball/{_COMMIT}/"
_DL_RESOURCE = tfds.download.Resource(
    url=_DL_URL,
    extract_method=tfds.download.ExtractMethod.ZIP)
_EXTRACT_SUBDIR = f"fchollet-ARC-{_COMMIT}"

class ARC(tfds.core.GeneratorBasedBuilder):
  """The Abstraction and Reasoning Corpus (ARC)."""

  VERSION = tfds.core.Version(
      "1.0.0", experiments={tfds.core.Experiment.S3: False})
  SUPPORTED_VERSIONS = [
      tfds.core.Version(
          "3.0.0", "New split API (https://tensorflow.org/datasets/splits)"),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # Images are of varying size
            "task_id": tfds.features.Text(),
            "train": tfds.features.Sequence({
                "input": tfds.features.Tensor(shape=(30, 30), dtype=tf.int8),
                "input_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
                "output": tfds.features.Tensor(shape=(30, 30), dtype=tf.int8),
                "output_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
            }),
            "test": tfds.features.Sequence({
                "input": tfds.features.Tensor(shape=(30, 30), dtype=tf.int8),
                "input_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
                "output": tfds.features.Tensor(shape=(30, 30), dtype=tf.int8),
                "output_size": tfds.features.Tensor(shape=(2,), dtype=tf.uint8),
            })
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_BASE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Downloads the data, defines the splits and returns SplitGenerators."""

    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    extracted_dir = dl_manager.download_and_extract(_DL_RESOURCE)
    data_dir = os.path.join(extracted_dir, _EXTRACT_SUBDIR, "data")
    train_dir = os.path.join(data_dir, "training")
    test_dir = os.path.join(data_dir, "evaluation")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "directory": train_dir,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs={
                "directory": test_dir,
            }),
    ]

  def _to_image(self, data):
      img = np.full(shape=[30, 30], fill_value=-1, dtype=np.int8)
      height = len(data)
      width = len(data[0])
      for index, row in enumerate(data):
          width = max(width, len(row))
          img[index, :len(row)] = [value if value is not None else -1
                                   for value in row]
      return img, np.array([height, width], dtype=np.uint8)

  def _prepare_pairs(self, pairs):
      prepared_pairs = []
      for pair in pairs:
          input_image, input_size = self._to_image(pair["input"])
          output_image, output_size = self._to_image(pair["output"])
          prepared_pairs.append({
                  "input": input_image,
                  "input_size": input_size,
                  "output": output_image,
                  "output_size": output_size
              })
      return prepared_pairs

  def _generate_examples(self, directory):
    """Yields (key, example) tuples from the dataset"""
    json_filepaths = tf.io.gfile.glob(os.path.join(directory, "*.json"))
    for json_path in sorted(json_filepaths):
        with tf.io.gfile.GFile(json_path) as f:
            task = json.load(f)
        task_id = os.path.basename(json_path)[:-len(".json")]
        yield task_id, {
            "task_id": task_id,
            "train": self._prepare_pairs(task["train"]),
            "test": self._prepare_pairs(task["test"]),
        }
