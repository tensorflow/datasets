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

"""mslr_web dataset."""

import dataclasses
import itertools

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.ranking.libsvm_ranking_parser import LibSVMRankingParser

_DESCRIPTION = """
MSLR-WEB are two large-scale Learning-to-Rank datasets released by Microsoft
Research. The first dataset (called "30k") contains 30,000 queries and the
second dataset (called "10k") contains 10,000 queries. Each dataset consists of
query-document pairs represented as feature vectors and corresponding relevance
judgment labels.

You can specify whether to use the "10k" or "30k" version of the dataset, and a
corresponding fold, as follows:

```python
ds = tfds.load("mslr_web/30k_fold1")
```

If only `mslr_web` is specified, the `mslr_web/10k_fold1` option is selected by
default:

```python
# This is the same as `tfds.load("mslr_web/10k_fold1")`
ds = tfds.load("mslr_web")
```
"""

_CITATION = """
@article{DBLP:journals/corr/QinL13,
  author    = {Tao Qin and Tie{-}Yan Liu},
  title     = {Introducing {LETOR} 4.0 Datasets},
  journal   = {CoRR},
  volume    = {abs/1306.2597},
  year      = {2013},
  url       = {http://arxiv.org/abs/1306.2597},
  timestamp = {Mon, 01 Jul 2013 20:31:25 +0200},
  biburl    = {http://dblp.uni-trier.de/rec/bib/journals/corr/QinL13},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
"""

_URLS = {
    "10k":
        "https://api.onedrive.com/v1.0/shares/s!AtsMfWUz5l8nbOIoJ6Ks0bEMp78/root/content",
    "30k":
        "https://api.onedrive.com/v1.0/shares/s!AtsMfWUz5l8nbXGPBlwD1rnFdBY/root/content"
}

_FEATURE_NAMES = {
    1: "covered_query_term_number_body",
    2: "covered_query_term_number_anchor",
    3: "covered_query_term_number_title",
    4: "covered_query_term_number_url",
    5: "covered_query_term_number_whole_document",
    6: "covered_query_term_ratio_body",
    7: "covered_query_term_ratio_anchor",
    8: "covered_query_term_ratio_title",
    9: "covered_query_term_ratio_url",
    10: "covered_query_term_ratio_whole_document",
    11: "stream_length_body",
    12: "stream_length_anchor",
    13: "stream_length_title",
    14: "stream_length_url",
    15: "stream_length_whole_document",
    16: "idf_body",
    17: "idf_anchor",
    18: "idf_title",
    19: "idf_url",
    20: "idf_whole_document",
    21: "sum_of_term_frequency_body",
    22: "sum_of_term_frequency_anchor",
    23: "sum_of_term_frequency_title",
    24: "sum_of_term_frequency_url",
    25: "sum_of_term_frequency_whole_document",
    26: "min_of_term_frequency_body",
    27: "min_of_term_frequency_anchor",
    28: "min_of_term_frequency_title",
    29: "min_of_term_frequency_url",
    30: "min_of_term_frequency_whole_document",
    31: "max_of_term_frequency_body",
    32: "max_of_term_frequency_anchor",
    33: "max_of_term_frequency_title",
    34: "max_of_term_frequency_url",
    35: "max_of_term_frequency_whole_document",
    36: "mean_of_term_frequency_body",
    37: "mean_of_term_frequency_anchor",
    38: "mean_of_term_frequency_title",
    39: "mean_of_term_frequency_url",
    40: "mean_of_term_frequency_whole_document",
    41: "variance_of_term_frequency_body",
    42: "variance_of_term_frequency_anchor",
    43: "variance_of_term_frequency_title",
    44: "variance_of_term_frequency_url",
    45: "variance_of_term_frequency_whole_document",
    46: "sum_of_stream_length_normalized_term_frequency_body",
    47: "sum_of_stream_length_normalized_term_frequency_anchor",
    48: "sum_of_stream_length_normalized_term_frequency_title",
    49: "sum_of_stream_length_normalized_term_frequency_url",
    50: "sum_of_stream_length_normalized_term_frequency_whole_document",
    51: "min_of_stream_length_normalized_term_frequency_body",
    52: "min_of_stream_length_normalized_term_frequency_anchor",
    53: "min_of_stream_length_normalized_term_frequency_title",
    54: "min_of_stream_length_normalized_term_frequency_url",
    55: "min_of_stream_length_normalized_term_frequency_whole_document",
    56: "max_of_stream_length_normalized_term_frequency_body",
    57: "max_of_stream_length_normalized_term_frequency_anchor",
    58: "max_of_stream_length_normalized_term_frequency_title",
    59: "max_of_stream_length_normalized_term_frequency_url",
    60: "max_of_stream_length_normalized_term_frequency_whole_document",
    61: "mean_of_stream_length_normalized_term_frequency_body",
    62: "mean_of_stream_length_normalized_term_frequency_anchor",
    63: "mean_of_stream_length_normalized_term_frequency_title",
    64: "mean_of_stream_length_normalized_term_frequency_url",
    65: "mean_of_stream_length_normalized_term_frequency_whole_document",
    66: "variance_of_stream_length_normalized_term_frequency_body",
    67: "variance_of_stream_length_normalized_term_frequency_anchor",
    68: "variance_of_stream_length_normalized_term_frequency_title",
    69: "variance_of_stream_length_normalized_term_frequency_url",
    70: "variance_of_stream_length_normalized_term_frequency_whole_document",
    71: "sum_of_tf_idf_body",
    72: "sum_of_tf_idf_anchor",
    73: "sum_of_tf_idf_title",
    74: "sum_of_tf_idf_url",
    75: "sum_of_tf_idf_whole_document",
    76: "min_of_tf_idf_body",
    77: "min_of_tf_idf_anchor",
    78: "min_of_tf_idf_title",
    79: "min_of_tf_idf_url",
    80: "min_of_tf_idf_whole_document",
    81: "max_of_tf_idf_body",
    82: "max_of_tf_idf_anchor",
    83: "max_of_tf_idf_title",
    84: "max_of_tf_idf_url",
    85: "max_of_tf_idf_whole_document",
    86: "mean_of_tf_idf_body",
    87: "mean_of_tf_idf_anchor",
    88: "mean_of_tf_idf_title",
    89: "mean_of_tf_idf_url",
    90: "mean_of_tf_idf_whole_document",
    91: "variance_of_tf_idf_body",
    92: "variance_of_tf_idf_anchor",
    93: "variance_of_tf_idf_title",
    94: "variance_of_tf_idf_url",
    95: "variance_of_tf_idf_whole_document",
    96: "boolean_model_body",
    97: "boolean_model_anchor",
    98: "boolean_model_title",
    99: "boolean_model_url",
    100: "boolean_model_whole_document",
    101: "vector_space_model_body",
    102: "vector_space_model_anchor",
    103: "vector_space_model_title",
    104: "vector_space_model_url",
    105: "vector_space_model_whole_document",
    106: "bm25_body",
    107: "bm25_anchor",
    108: "bm25_title",
    109: "bm25_url",
    110: "bm25_whole_document",
    111: "lmir_abs_body",
    112: "lmir_abs_anchor",
    113: "lmir_abs_title",
    114: "lmir_abs_url",
    115: "lmir_abs_whole_document",
    116: "lmir_dir_body",
    117: "lmir_dir_anchor",
    118: "lmir_dir_title",
    119: "lmir_dir_url",
    120: "lmir_dir_whole_document",
    121: "lmir_jm_body",
    122: "lmir_jm_anchor",
    123: "lmir_jm_title",
    124: "lmir_jm_url",
    125: "lmir_jm_whole_document",
    126: "number_of_slash_in_url",
    127: "length_of_url",
    128: "inlink_number",
    129: "outlink_number",
    130: "page_rank",
    131: "site_rank",
    132: "quality_score",
    133: "quality_score_2",
    134: "query_url_click_count",
    135: "url_click_count",
    136: "url_dwell_time",
}

_LABEL_NAME = "label"


@dataclasses.dataclass
class MslrWebConfig(tfds.core.BuilderConfig):
  size: str = "10k"  # one of "10k" or "30k"
  fold: int = 1


class MslrWeb(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for mslr_web dataset."""

  VERSION = tfds.core.Version("1.1.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
      "1.1.0": "Bundle features into a single 'float_features' feature."
  }
  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      MslrWebConfig(name=f"{size}_fold{fold}", size=size, fold=fold)
      for size, fold in itertools.product(["10k", "30k"], [1, 2, 3, 4, 5])
  ]

  # pytype: enable=wrong-keyword-args

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    encoding = tfds.features.Encoding.ZLIB
    features = {
        "float_features":
            tfds.features.Tensor(
                shape=(None, len(_FEATURE_NAMES)),
                dtype=tf.float64,
                encoding=encoding),
        _LABEL_NAME:
            tfds.features.Tensor(
                shape=(None,), dtype=tf.float64, encoding=encoding)
    }
    metadata = tfds.core.MetadataDict({
        "float_features_names": {
            idx: _FEATURE_NAMES[key]
            for idx, key in enumerate(sorted(_FEATURE_NAMES))
        }
    })

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage="https://www.microsoft.com/en-us/research/project/mslr/",
        citation=_CITATION,
        metadata=metadata)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    size = self.builder_config.size
    fold = self.builder_config.fold
    path = dl_manager.download_and_extract(_URLS[size])

    return {
        split: self._generate_examples(path / f"Fold{fold}/{split}.txt")
        for split in ["train", "vali", "test"]
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with tf.io.gfile.GFile(path, "r") as f:
      yield from LibSVMRankingParser(
          f, _FEATURE_NAMES, _LABEL_NAME, combine_features=True)
