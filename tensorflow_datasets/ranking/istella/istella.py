# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""istella dataset."""

import dataclasses
from typing import Optional

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.ranking.libsvm_ranking_parser import LibSVMRankingParser

_DESCRIPTION = """
The Istella datasets are three large-scale Learning-to-Rank datasets released by
Istella. Each dataset consists of query-document pairs represented as feature
vectors and corresponding relevance judgment labels.

The dataset contains three versions:

 * `main` ("Istella LETOR"): Containing 10,454,629 query-document pairs.
 * `s` ("Istella-S LETOR"): Containing 3,408,630 query-document pairs.
 * `x` ("Istella-X LETOR"): Containing 26,791,447 query-document pairs.

You can specify whether to use the `main`, `s` or `x` version of the dataset as
follows:

```python
ds = tfds.load("istella/main")
ds = tfds.load("istella/s")
ds = tfds.load("istella/x")
```

If only `istella` is specified, the `istella/main` option is selected by
default:

```python
# This is the same as `tfds.load("istella/main")`
ds = tfds.load("istella")
```
"""

_CITATION = """
@article{10.1145/2987380,
  author = {Dato, Domenico and Lucchese, Claudio and Nardini, Franco Maria and Orlando, Salvatore and Perego, Raffaele and Tonellotto, Nicola and Venturini, Rossano},
  title = {Fast Ranking with Additive Ensembles of Oblivious and Non-Oblivious Regression Trees},
  year = {2016},
  publisher = {ACM},
  address = {New York, NY, USA},
  volume = {35},
  number = {2},
  issn = {1046-8188},
  url = {https://doi.org/10.1145/2987380},
  doi = {10.1145/2987380},
  journal = {ACM Transactions on Information Systems},
  articleno = {15},
  numpages = {31},
}
"""

_URLS = {
    "main": "http://library.istella.it/dataset/istella-letor.tar.gz",
    "s": "http://library.istella.it/dataset/istella-s-letor.tar.gz",
    "x": (
        "http://quickrank.isti.cnr.it/istella-datasets-mirror/istella-X.tar.gz"
    ),
}

_FEATURE_NAMES = {n: f"feature_{n}" for n in range(1, 221)}

_LABEL_NAME = "label"


@dataclasses.dataclass
class IstellaConfig(tfds.core.BuilderConfig):
  has_vali: bool = False
  subdirectory: Optional[str] = None


class Istella(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for istella dataset."""

  VERSION = tfds.core.Version("1.2.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
      "1.0.1": "Fix serialization to support float64.",
      "1.1.0": "Bundle features into a single 'float_features' feature.",
      "1.2.0": "Add query and document identifiers.",
  }
  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      IstellaConfig(name="main", has_vali=False, subdirectory="full"),
      IstellaConfig(name="s", has_vali=True, subdirectory="sample"),
      IstellaConfig(name="x", has_vali=True, subdirectory=None),
  ]

  # pytype: enable=wrong-keyword-args

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    encoding = tfds.features.Encoding.ZLIB
    features = {
        "float_features": tfds.features.Tensor(
            shape=(None, len(_FEATURE_NAMES)),
            dtype=np.float64,
            encoding=encoding,
        ),
        _LABEL_NAME: tfds.features.Tensor(
            shape=(None,), dtype=np.float64, encoding=encoding
        ),
        "query_id": tfds.features.Text(),
        "doc_id": tfds.features.Tensor(
            shape=(None,), dtype=np.int64, encoding=encoding
        ),
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage="http://quickrank.isti.cnr.it/istella-dataset/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URLS[self.builder_config.name])

    # For some dataset configs, the data is in a subdirectory.
    if self.builder_config.subdirectory is not None:
      path = path / self.builder_config.subdirectory

    splits = {
        "train": self._generate_examples(path / "train.txt"),
        "test": self._generate_examples(path / "test.txt"),
    }

    # For some dataset configs, there is an additional validation split.
    if self.builder_config.has_vali:
      splits["vali"] = self._generate_examples(path / "vali.txt")

    return splits

  def _generate_examples(self, path):
    """Yields examples."""
    # Istella datasets seems to be encoded as latin1 and not utf-8, so we have
    # to read the file contents as bytes and manually decode it as latin1.
    with tf.io.gfile.GFile(path, "rb") as f:
      lines = map(lambda bytes_line: bytes_line.decode("latin1"), f)
      yield from LibSVMRankingParser(
          lines, _FEATURE_NAMES, _LABEL_NAME, combine_features=True
      )
