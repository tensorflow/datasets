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

"""ARC dataset."""

import json
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "https://github.com/fchollet/ARC/"


class ARCConfig(tfds.core.BuilderConfig):
  """BuilderConfig for ARC."""

  def __init__(self, *, version, commit, **kwargs):
    """BuilderConfig for ARC.

    Args:
      version (string): version as string.
      commit: github.com/fchollet/ARC commit to use (defaults to "master").
      **kwargs: keyword arguments forwarded to super.
    """
    super(ARCConfig, self).__init__(
        version=tfds.core.Version(version), **kwargs)
    self.commit = commit
    self.download_url = "{}zipball/{}".format(_BASE_URL, self.commit)


class Builder(tfds.core.GeneratorBasedBuilder):
  """The Abstraction and Reasoning Corpus (ARC)."""

  BUILDER_CONFIGS = [
      ARCConfig(
          name="2019-12-06",
          version="1.0.0",
          description="ARC commit bd9e2c9 from 2019-12-06",
          commit="bd9e2c934c83d00251b7b4781ffc38cd167c885f"),
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            # Grids are of varying size
            "task_id":
                tfds.features.Text(),
            "train":
                tfds.features.Sequence({
                    "input":
                        tfds.features.Sequence(
                            tfds.features.Sequence(tf.int32)),
                    "output":
                        tfds.features.Sequence(
                            tfds.features.Sequence(tf.int32)),
                }),
            "test":
                tfds.features.Sequence({
                    "input":
                        tfds.features.Sequence(
                            tfds.features.Sequence(tf.int32)),
                    "output":
                        tfds.features.Sequence(
                            tfds.features.Sequence(tf.int32)),
                })
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_BASE_URL,
    )

  def _split_generators(self, dl_manager):
    """Downloads the data, defines the splits and returns SplitGenerators."""

    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    extracted_dir = dl_manager.download_and_extract(
        self.builder_config.download_url)
    extract_subdir = [
        path for path in tf.io.gfile.listdir(extracted_dir)
        if path.startswith("fchollet-ARC-")
    ]
    if len(extract_subdir) != 1:
      raise ValueError("Unexpected ARC archive format")
    data_dir = os.path.join(extracted_dir, extract_subdir[0], "data")
    train_dir = os.path.join(data_dir, "training")
    test_dir = os.path.join(data_dir, "evaluation")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={
                "directory": train_dir,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, gen_kwargs={
                "directory": test_dir,
            }),
    ]

  def _generate_examples(self, directory):
    """Yields (key, example) tuples from the dataset."""
    json_filepaths = tf.io.gfile.glob(os.path.join(directory, "*.json"))
    for json_path in sorted(json_filepaths):
      with epath.Path(json_path).open() as f:
        task = json.load(f)
      task_id = os.path.basename(json_path)[:-len(".json")]
      yield task_id, {
          "task_id": task_id,
          "train": task["train"],
          "test": task["test"],
      }
