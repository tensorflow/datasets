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

"""beir dataset."""

from __future__ import annotations

import functools
import json
import os
from typing import Mapping

import numpy as np
import tensorflow_datasets.public_api as tfds

_BASE_DOWNLOAD_URL = (
    'https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets'
)


class BeirConfig(tfds.core.BuilderConfig):
  """BuilderConfig for BEIR datasets."""

  def __init__(
      self,
      name: str,
      download_url: str,
      qrel_splits: Mapping[str, str],
      subdir=None,
      **kwargs,
  ):
    """BuilderConfig for Beir.

    Args:
      name: Name for the config.
      download_url: Path to zip file of corpus, quries, and qrels.
      qrel_splits: Path to splits of TSV files that contain three columns, i.e.
        the query-id, corpus-id and score in this order.
      subdir: The sub-directory to use.
      **kwargs: keyword arguments forwarded to super.
    """
    super(BeirConfig, self).__init__(name=name, **kwargs)

    self.download_url = download_url
    self.qrel_splits = qrel_splits
    self.subdir = subdir


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for beir dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
      BeirConfig(
          'msmarco',
          download_url=f'{_BASE_DOWNLOAD_URL}/msmarco.zip',
          qrel_splits={
              'train': 'train.tsv',
              'validation': 'dev.tsv',
              'test': 'test.tsv',
          },
      ),
      BeirConfig(
          'trec_covid',
          download_url=f'{_BASE_DOWNLOAD_URL}/trec-covid.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'nfcorpus',
          download_url=f'{_BASE_DOWNLOAD_URL}/nfcorpus.zip',
          qrel_splits={
              'train': 'train.tsv',
              'validation': 'dev.tsv',
              'test': 'test.tsv',
          },
      ),
      BeirConfig(
          'nq',
          download_url=f'{_BASE_DOWNLOAD_URL}/nq.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'hotpotqa',
          download_url=f'{_BASE_DOWNLOAD_URL}/hotpotqa.zip',
          qrel_splits={
              'train': 'train.tsv',
              'validation': 'dev.tsv',
              'test': 'test.tsv',
          },
      ),
      BeirConfig(
          'fiqa',
          download_url=f'{_BASE_DOWNLOAD_URL}/fiqa.zip',
          qrel_splits={
              'train': 'train.tsv',
              'validation': 'dev.tsv',
              'test': 'test.tsv',
          },
      ),
      BeirConfig(
          'arguana',
          download_url=f'{_BASE_DOWNLOAD_URL}/arguana.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'webis_touche2020',
          download_url=f'{_BASE_DOWNLOAD_URL}/webis-touche2020.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'cqadupstack.android',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='android',
      ),
      BeirConfig(
          'cqadupstack.english',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='english',
      ),
      BeirConfig(
          'cqadupstack.gaming',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='gaming',
      ),
      BeirConfig(
          'cqadupstack.gis',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='gis',
      ),
      BeirConfig(
          'cqadupstack.mathematica',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='mathematica',
      ),
      BeirConfig(
          'cqadupstack.physics',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='physics',
      ),
      BeirConfig(
          'cqadupstack.programmers',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='programmers',
      ),
      BeirConfig(
          'cqadupstack.stats',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='stats',
      ),
      BeirConfig(
          'cqadupstack.tex',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='tex',
      ),
      BeirConfig(
          'cqadupstack.unix',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='unix',
      ),
      BeirConfig(
          'cqadupstack.webmasters',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='webmasters',
      ),
      BeirConfig(
          'cqadupstack.wordpress',
          download_url=f'{_BASE_DOWNLOAD_URL}/cqadupstack.zip',
          qrel_splits={'test': 'test.tsv'},
          subdir='wordpress',
      ),
      BeirConfig(
          'quora',
          download_url=f'{_BASE_DOWNLOAD_URL}/quora.zip',
          qrel_splits={'validation': 'dev.tsv', 'test': 'test.tsv'},
      ),
      BeirConfig(
          'dbpedia_entity',
          download_url=f'{_BASE_DOWNLOAD_URL}/dbpedia-entity.zip',
          qrel_splits={'validation': 'dev.tsv', 'test': 'test.tsv'},
      ),
      BeirConfig(
          'scidocs',
          download_url=f'{_BASE_DOWNLOAD_URL}/scidocs.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'fever',
          download_url=f'{_BASE_DOWNLOAD_URL}/fever.zip',
          qrel_splits={
              'train': 'train.tsv',
              'validation': 'dev.tsv',
              'test': 'test.tsv',
          },
      ),
      BeirConfig(
          'climate_fever',
          download_url=f'{_BASE_DOWNLOAD_URL}/climate-fever.zip',
          qrel_splits={'test': 'test.tsv'},
      ),
      BeirConfig(
          'scifact',
          download_url=f'{_BASE_DOWNLOAD_URL}/scifact.zip',
          qrel_splits={'train': 'train.tsv', 'test': 'test.tsv'},
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(beir): Specifies the tfds.core.DatasetInfo object
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'query_id': tfds.features.Text(),
            'query': tfds.features.Text(),
            'query_metadata': tfds.features.Text(),
            'passage_id': tfds.features.Text(),
            'passage': tfds.features.Text(),
            'passage_metadata': tfds.features.Text(),
            'score': np.float32,
        }),
        homepage='https://github.com/beir-cellar/beir',
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager, pipeline
  ):
    """Returns SplitGenerators."""
    beam = tfds.core.lazy_imports.apache_beam
    # Downloads the data and defines the splits.
    builder_config = self.builder_config
    root = dl_manager.download_and_extract(builder_config.download_url)
    basename = os.path.basename(builder_config.download_url)
    unzip_dir_name = os.path.splitext(basename)[0]
    subdir = builder_config.subdir if builder_config.subdir else ''
    data_dir = os.path.join(root, unzip_dir_name, subdir)

    query_pipeline = (
        pipeline
        | 'ReadQueryData'
        >> beam.io.textio.ReadFromText(os.path.join(data_dir, 'queries.jsonl'))
        | 'ParseQueryJson' >> beam.Map(_parse_query_json)
    )

    passage_pipeline = (
        pipeline
        | 'ReadPassageData'
        >> beam.io.textio.ReadFromText(os.path.join(data_dir, 'corpus.jsonl'))
        | 'ParsePassageJson' >> beam.Map(_parse_passage_json)
    )

    splits = {
        'query': (
            query_pipeline
            | 'Query' >> beam.ptransform_fn(self._generate_query_examples)()
        ),
        'passage': (
            passage_pipeline
            | 'Passage' >> beam.ptransform_fn(self._generate_passage_examples)()
        ),
    }

    # Creates splits for (query, document) pairs.
    for qrel_split, tsv_file in builder_config.qrel_splits.items():
      splits[
          qrel_split
      ] = pipeline | qrel_split.capitalize() >> beam.ptransform_fn(
          self._generate_qrel_examples
      )(
          qrel_path=os.path.join(data_dir, 'qrels', tsv_file),
          query_pipeline=query_pipeline,
          passage_pipeline=passage_pipeline,
      )

    return splits

  def _generate_query_examples(self, pipeline):
    """Generates examples for query split."""
    beam = tfds.core.lazy_imports.apache_beam
    return (
        pipeline
        | 'AddEmptyFeatures'
        >> beam.Map(
            functools.partial(
                _append_constant_features,
                mapping={
                    'passage_id': '',
                    'passage': '',
                    'passage_metadata': '{}',
                    'score': -1,
                },
            )
        )
        | 'GetHashKey' >> beam.Map(lambda x: (_get_hash(x), x))
    )

  def _generate_passage_examples(self, pipeline):
    """Generates examples for passage split."""
    beam = tfds.core.lazy_imports.apache_beam
    return (
        pipeline
        | 'AddEmptyFeatures'
        >> beam.Map(
            functools.partial(
                _append_constant_features,
                mapping={
                    'query_id': '',
                    'query': '',
                    'query_metadata': '{}',
                    'score': -1,
                },
            )
        )
        | 'GetHashKey' >> beam.Map(lambda x: (_get_hash(x), x))
    )

  def _generate_qrel_examples(
      self, pipeline, qrel_path, query_pipeline, passage_pipeline
  ):
    """Generates (query, passage) pair examples."""
    beam = tfds.core.lazy_imports.apache_beam
    qid_query = query_pipeline | 'QidAsKey' >> beam.Map(
        lambda x: (x['query_id'], x)  # pylint: disable=g-long-lambda
    )
    docid_passage = passage_pipeline | 'DocidAsKey' >> beam.Map(
        lambda x: (x['passage_id'], x)
    )

    # PCollection[qid, Tuple(docid, score)]
    qid_docid = (
        pipeline
        | beam.io.ReadFromText(qrel_path)
        | 'Split' >> beam.Map(lambda x: x.strip().split('\t')[:3])
        | 'FilterFirstLine' >> beam.Filter(lambda x: x[0] != 'query-id')
        | 'QidAsKeyAndDocid' >> beam.Map(lambda x: (x[0], (x[1], float(x[2]))))
    )

    def to_docid_query_fn(ex):
      rst = []
      for docid, score in ex['docids']:
        rst.append((
            docid,
            {  # pylint: disable=g-complex-comprehension
                **ex['query'][0],
                'score': score,
            },
        ))
      return rst

    # PCollection[docid, Dict].
    # Dict.keys() = ['query_id', 'query', 'query_metadata', 'score']
    docid_query = (
        ({
            'docids': qid_docid,
            'query': qid_query,
        })
        | 'GroupByQid' >> beam.CoGroupByKey()
        | 'DropQid' >> beam.Values()
        | 'FilterEmptyQid' >> beam.Filter(lambda x: x['query'] and x['docids'])
        | 'SetKeyDocid' >> beam.FlatMap(to_docid_query_fn)
    )

    return (
        ({
            'query': docid_query,
            'passage': docid_passage,
        })
        | 'GroupByDocid' >> beam.CoGroupByKey()
        | 'DropDocid' >> beam.Values()
        | 'FilterEmptyDocid'
        >> beam.Filter(lambda x: x['query'] and x['passage'])
        | 'MergeQueryAndPassage'
        >> beam.Map(
            lambda x: {  # pylint: disable=g-long-lambda
                **x['query'][0],
                **x['passage'][0],
            }
        )
        | 'GetHashKey' >> beam.Map(lambda x: (_get_hash(x), x))
    )

  def _generate_examples(self, pipeline):
    """Yields examples."""
    # Not used.
    pass


def _parse_query_json(text):
  """Parses query json object."""
  data = json.loads(text)
  return {
      'query_id': data['_id'],
      'query': data['text'],
      'query_metadata': json.dumps(data['metadata']),
  }


def _parse_passage_json(text):
  """Parses passage json object."""
  data = json.loads(text)
  metadata = data['metadata']
  if 'title' in data:
    metadata['title'] = data['title']
  return {
      'passage_id': data['_id'],
      'passage': data['text'],
      'passage_metadata': json.dumps(metadata),
  }


def _append_constant_features(features, mapping):
  """Appends constant features."""
  output = dict(features)
  output.update(mapping)
  return output


def _get_hash(features):
  """Returns a hash key for features."""
  s = '|'.join([
      str(features['query_id']),
      features['query'] or '',
      str(features['passage_id']),
      features['passage'] or '',
  ])
  return hash(s.encode())
