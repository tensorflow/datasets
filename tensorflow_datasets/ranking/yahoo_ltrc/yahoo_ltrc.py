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

"""yahoo_ltrc dataset."""

import dataclasses

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.ranking.libsvm_ranking_parser import LibSVMRankingParser

_DESCRIPTION = """
The Yahoo Learning to Rank Challenge dataset (also called "C14") is a
Learning-to-Rank dataset released by Yahoo. The dataset consists of
query-document pairs represented as feature vectors and corresponding relevance
judgment labels.

The dataset contains two versions:

 * `set1`: Containing 709,877 query-document pairs.
 * `set2`: Containing 172,870 query-document pairs.

You can specify whether to use the `set1` or `set2` version of the dataset as
follows:

```python
ds = tfds.load("yahoo_ltrc/set1")
ds = tfds.load("yahoo_ltrc/set2")
```

If only `yahoo_ltrc` is specified, the `yahoo_ltrc/set1` option is selected by
default:

```python
# This is the same as `tfds.load("yahoo_ltrc/set1")`
ds = tfds.load("yahoo_ltrc")
```
"""

_CITATION = """
@inproceedings{chapelle2011yahoo,
  title={Yahoo! learning to rank challenge overview},
  author={Chapelle, Olivier and Chang, Yi},
  booktitle={Proceedings of the learning to rank challenge},
  pages={1--24},
  year={2011},
  organization={PMLR}
}
"""

_LABEL_NAME = "label"


@dataclasses.dataclass
class YahooLTRCConfig(tfds.core.BuilderConfig):
  prefix: str = "set1"
  num_features: int = 699


class YahooLTRC(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for yahoo_ltrc dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }
  # pytype: disable=wrong-keyword-args
  # pylint: disable=unexpected-keyword-arg
  BUILDER_CONFIGS = [
      YahooLTRCConfig(name="set1", prefix="set1", num_features=699),
      YahooLTRCConfig(name="set2", prefix="set2", num_features=700),
  ]

  # pylint: enable=unexpected-keyword-arg
  # pytype: enable=wrong-keyword-args

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Request access for the C14 Yahoo Learning To Rank Challenge dataset on
  https://research.yahoo.com/datasets. Extract the downloaded `dataset.tgz` file
  and place the `ltrc_yahoo.tar.bz2` file in `manual_dir/`.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    encoding = tfds.features.Encoding.ZLIB
    features = {
        "float_features":
            tfds.features.Tensor(
                shape=(None, self.builder_config.num_features),
                dtype=tf.float64,
                encoding=encoding),
        _LABEL_NAME:
            tfds.features.Tensor(
                shape=(None,), dtype=tf.float64, encoding=encoding)
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage="https://research.yahoo.com/datasets",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Extract the manually downloaded `ltrc_yahoo.tar.bz2`
    archive_path = dl_manager.manual_dir / "ltrc_yahoo.tar.bz2"
    path = dl_manager.extract(archive_path)

    prefix = self.builder_config.prefix
    feature_names = {
        n: f"feature_{n}"
        for n in range(1, self.builder_config.num_features + 1)
    }

    splits = {
        "train":
            self._generate_examples(path / f"{prefix}.train.txt",
                                    feature_names),
        "vali":
            self._generate_examples(path / f"{prefix}.valid.txt",
                                    feature_names),
        "test":
            self._generate_examples(path / f"{prefix}.test.txt", feature_names)
    }

    return splits

  def _generate_examples(self, path, feature_names):
    """Yields examples."""
    with tf.io.gfile.GFile(path, "r") as f:
      yield from LibSVMRankingParser(
          f, feature_names, _LABEL_NAME, combine_features=True)
