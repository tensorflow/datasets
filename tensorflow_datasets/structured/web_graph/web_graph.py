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

"""web_graph dataset."""

from __future__ import annotations

import dataclasses
import os
import textwrap
from typing import List

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This dataset contains a sparse graph representing web link structure for a
small subset of the Web.

Its a processed version of a single crawl performed by CommonCrawl in 2021
where we strip everything and keep only the link->outlinks structure.
The final dataset is basically int -> List[int] format with each integer id
representing a url.

Also, in order to increase the value of this resource, we created 6 different
version of WebGraph, each varying in the sparsity pattern and locale. We took
the following processing steps, in order:

- We started with WAT files from June 2021 crawl.
- Since the outlinks in HTTP-Response-Metadata are stored as relative paths, we
convert them to absolute paths using urllib after validating each link.
- To study locale-specific graphs, we further filter based on 2 top level
domains: ‘de’ and ‘in’, each producing a graph with an order of magnitude less
number of nodes.
- These graphs can still have arbitrary sparsity patterns and dangling links.
Thus we further filter the nodes in each graph to have minimum of K ∈ [10, 50]
inlinks and outlinks. Note that we only do this processing once, thus this is
still an approximation i.e. the resulting graph might have nodes with less than
K links.
- Using both locale and count filters, we finalize 6 versions of WebGraph
dataset, summarized in the folling table.

| Version      | Top level domain | Min count | Num nodes | Num edges |
| -----------  | ---------------- | --------- | --------- | --------- |
| sparse       |                  | 10        | 365.4M    | 30B       |
| dense        |                  | 50        | 136.5M    | 22B       |
| de-sparse    | de               | 10        | 19.7M     | 1.19B     |
| de-dense     | de               | 50        | 5.7M      | 0.82B     |
| in-sparse    | in               | 10        | 1.5M      | 0.14B     |
| in-dense     | in               | 50        | 0.5M      | 0.12B     |

All versions of the dataset have following features:

- "row_tag": a unique identifier of the row (source link).
- "col_tag": a list of unique identifiers of non-zero columns (dest outlinks).
- "gt_tag": a list of unique identifiers of non-zero columns used as ground
truth (dest outlinks), empty for train/train_t splits.
"""

_CITATION = """
@article{mehta2021alx,
    title={ALX: Large Scale Matrix Factorization on TPUs},
    author={Harsh Mehta and Steffen Rendle and Walid Krichene and Li Zhang},
    year={2021},
    eprint={2112.02194},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""


@dataclasses.dataclass
class WebGraphConfig(tfds.core.BuilderConfig):
  """Palmer Penguins dataset builder config."""
  # Basename of the file hosting the data.
  subfolder: str = ''
  num_shards: int = 1


def filename(subfolder: str, name: str):
  full_name = os.path.join(subfolder, name)
  return os.fspath(tfds.core.Path(full_name))


class WebGraph(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for web_graph dataset."""

  VERSION = tfds.core.Version('1.0.0')
  WEB_GRAPH_HOMEPAGE = 'gs://gresearch/web_graph/'
  SHARDS = None
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      WebGraphConfig(
          name='sparse',
          subfolder='web_graph_min_10',
          num_shards=1000,
          description=textwrap.dedent("""\
              WebGraph-sparse contains around 30B edges and around 365M nodes.
              """),
      ),
      WebGraphConfig(
          name='dense',
          subfolder='web_graph_min_50',
          num_shards=1000,
          description=textwrap.dedent("""\
              WebGraph-dense contains around 22B edges and around 136.5M nodes.
              """),
      ),
      WebGraphConfig(
          name='de-sparse',
          subfolder='web_graph_tld_de_min_10',
          num_shards=100,
          description=textwrap.dedent("""\
              WebGraph-de-sparse contains around 1.19B edges and around 19.7M
              nodes.
              """),
      ),
      WebGraphConfig(
          name='de-dense',
          subfolder='web_graph_tld_de_min_50',
          num_shards=100,
          description=textwrap.dedent("""\
              WebGraph-de-dense contains around 0.82B edges and around 5.7M
              nodes.
              """),
      ),
      WebGraphConfig(
          name='in-sparse',
          subfolder='web_graph_tld_in_min_10',
          num_shards=10,
          description=textwrap.dedent("""\
              WebGraph-de-sparse contains around 0.14B edges and around 1.5M
              nodes.
              """),
      ),
      WebGraphConfig(
          name='in-dense',
          subfolder='web_graph_tld_in_min_50',
          num_shards=10,
          description=textwrap.dedent("""\
              WebGraph-de-dense contains around 0.12B edges and around 0.5M
              nodes.
              """),
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'row_tag': tf.int64,
            'col_tag': tfds.features.Sequence(tf.int64),
            'gt_tag': tfds.features.Sequence(tf.int64),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://arxiv.org/abs/2112.02194',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager,
                        pipeline):
    """Returns SplitGenerators."""
    del dl_manager

    subfolder = os.path.join(self.WEB_GRAPH_HOMEPAGE,
                             self.builder_config.subfolder)
    shards = self.SHARDS or self.builder_config.num_shards

    train_files = [
        filename(subfolder, f'train.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    train_t_files = [
        filename(subfolder, f'train.transpose.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    test_files = [
        filename(subfolder, f'test.tfr-{i:05}-of-{int(shards):05}')
        for i in range(shards)
    ]
    return {
        'train':
            self._generate_examples(pipeline, train_files, split='train'),
        'train_t':
            self._generate_examples(pipeline, train_t_files, split='train_t'),
        'test':
            self._generate_examples(pipeline, test_files, split='test')
    }

  def _generate_examples(self, pipeline, files, split: str):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _get_int_feature(example: tf.train.Example,
                         feature_name: str) -> List[int]:
      return example.features.feature[feature_name].int64_list.value

    def _process_example(example: bytes, is_test=False):
      example = tf.train.Example.FromString(example)
      row_tag = _get_int_feature(example, 'row_tag')[0]
      col_tag = np.array(_get_int_feature(example, 'col_tag'), dtype=np.int64)
      if is_test:
        gt_tag = _get_int_feature(example, 'gt_tag')
      else:
        gt_tag = []
      gt_tag = np.array(gt_tag, dtype=np.int64)
      return_dict = {'row_tag': row_tag, 'col_tag': col_tag, 'gt_tag': gt_tag}
      return row_tag, return_dict

    return (pipeline
            | f'{split}_create' >> beam.Create(files)
            | f'{split}_read' >> beam.io.tfrecordio.ReadAllFromTFRecord()
            | f'{split}_process' >> beam.Map(_process_example, split == 'test'))
