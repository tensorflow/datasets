# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""multi_news dataset."""

from etils import epath
import tensorflow_datasets.public_api as tfds

_URL_PATH = (
    "https://huggingface.co/datasets/alexfabbri/multi_news/resolve/main/data/"
)
_LICENSE = "For non-commercial research and educational purposes only"


_DOCUMENT = "document"
_SUMMARY = "summary"


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for multi_news dataset."""

  VERSION = tfds.core.Version("2.1.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
      "2.0.0": "[Do not use] Update the dataset with valid URLs.",
      "2.1.0": (
          "Update the dataset with the correct URLs. The URLs in this version"
          " come from HuggingFace's dataset repo, which is curated by the same"
          " author: https://huggingface.co/datasets/alexfabbri/multi_news."
      ),
  }
  BLOCKED_VERSIONS = tfds.core.utils.BlockedVersions(
      versions={"2.0.0": "The URLs of this version are invalid."}
  )

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {_DOCUMENT: tfds.features.Text(), _SUMMARY: tfds.features.Text()}
        ),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/Alex-Fabbri/Multi-News",
        license=_LICENSE,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    data_dict = {
        "train_src": _URL_PATH + "train.src.cleaned",
        "train_tgt": _URL_PATH + "train.tgt",
        "val_src": _URL_PATH + "val.src.cleaned",
        "val_tgt": _URL_PATH + "val.tgt",
        "test_src": _URL_PATH + "test.src.cleaned",
        "test_tgt": _URL_PATH + "test.tgt",
    }
    files = dl_manager.download_and_extract(data_dict)
    return {
        "train": self._generate_examples(
            files["train_src"], files["train_tgt"]
        ),
        "validation": self._generate_examples(
            files["val_src"], files["val_tgt"]
        ),
        "test": self._generate_examples(files["test_src"], files["test_tgt"]),
    }

  def _generate_examples(self, src_file, tgt_file):
    """Yields examples."""
    with epath.Path(src_file).open() as src_f, epath.Path(
        tgt_file
    ).open() as tgt_f:
      for i, (src_line, tgt_line) in enumerate(zip(src_f, tgt_f)):
        yield i, {
            # In the original file, each line has one example and natural
            # newline tokens "\n" are being replaced with "NEWLINE_CHAR"
            # Here, we restore the natural newline token to avoid the special
            # vocab token "NEWLINE_CHAR".
            _DOCUMENT: src_line.strip().replace("NEWLINE_CHAR", "\n"),
            _SUMMARY: tgt_line.strip().lstrip(),
        }
