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

"""RedPajamaV2 dataset."""

import collections
from collections.abc import Iterator
import contextlib
import gzip
import json
import os
from typing import Any, TypedDict

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq
import tensorflow_datasets.public_api as tfds


class _Example(TypedDict):
  raw_content: str
  meta: dict[str, Any]
  quality_signals: dict[str, Any]


_NUM_SHARDS = 5000
_PARTITIONS = ['head', 'middle', 'tail']
_LANGUAGES = ['en', 'de', 'fr', 'es', 'it']

_COMPONENTS_URL = 'https://data.together.xyz/redpajama-data-v2/v1.0.0'
_DOCS_COMPONENT = 'documents'
_SIGNALS_COMPONENT = 'signals'
_DUPLICATES_COMPONENT = 'duplicates'
_URL_TEMPLATE_BY_COMPONENT = {
    _DOCS_COMPONENT: os.path.join(
        _COMPONENTS_URL, 'documents/{base_tag}.json.gz'
    ),
    _SIGNALS_COMPONENT: os.path.join(
        _COMPONENTS_URL, 'quality_signals/{base_tag}.signals.json.gz'
    ),
    _DUPLICATES_COMPONENT: os.path.join(
        _COMPONENTS_URL, 'duplicates/{base_tag}.duplicates.parquet'
    ),
}

_URL = 'https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2/resolve/main'
_MISSING_URLS_TEMPLATE = os.path.join(_URL, 'urls/missing-{component}.txt')
_SNAPSHOTS_URL = os.path.join(_URL, '_CC_SNAPSHOT_IDS')


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for RedPajamaV2 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'raw_content': tfds.features.Text(),
            'doc_id': tfds.features.Text(),
            'meta': tfds.features.Text(),
            'quality_signals': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://www.together.ai/blog/redpajama-data-v2',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    snapshots_filepath = dl_manager.download_and_extract(_SNAPSHOTS_URL)
    snapshots = epath.Path(snapshots_filepath).read_text().splitlines()

    base_tags = []
    for lang in _LANGUAGES:
      for snapshot in snapshots:
        for partition in _PARTITIONS:
          for shard_idx in range(_NUM_SHARDS):
            base_tags.append(f'{snapshot}/{shard_idx:04d}/{lang}_{partition}')

    resource_by_component_by_base_tag = collections.defaultdict(dict)
    for component, url_template in _URL_TEMPLATE_BY_COMPONENT.items():
      missing_urls_filepath = dl_manager.download_and_extract(
          _MISSING_URLS_TEMPLATE.format(component=component)
      )
      missing_urls = set(
          epath.Path(missing_urls_filepath).read_text().splitlines()
      )

      for base_tag in base_tags:
        if (url := url_template.format(base_tag=base_tag)) not in missing_urls:
          snapshot = base_tag.split('/', maxsplit=1)[0]
          resource_by_component_by_base_tag[base_tag][component] = (
              tfds.download.Resource(url=url, relative_download_dir=snapshot)
          )

    filepath_by_component_by_base_tag = dl_manager.download(
        resource_by_component_by_base_tag
    )
    return {
        'train': self._generate_examples(filepath_by_component_by_base_tag),
    }

  def _generate_examples(self, filepath_by_component_by_base_tag):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_base_tag(base_tag, filepath_by_component):
      if not filepath_by_component[_DOCS_COMPONENT]:
        return

      if (
          base_tag.endswith('_tail')
          or not filepath_by_component[_SIGNALS_COMPONENT]
      ):
        generate_examples = _generate_tail
        partition = 'tail'
        duplicates = None
      else:
        generate_examples = _generate_head_middle
        partition = 'head_middle'

        try:
          with open_gzip(
              filepath_by_component[_DUPLICATES_COMPONENT]
          ) as duplicates_file:
            duplicates = set(
                pq.read_table(
                    duplicates_file,
                    columns=['doc_id'],
                    use_pandas_metadata=False,
                )['doc_id'].to_pylist()
            )
        except:  # pylint: disable=bare-except
          duplicates = set()

      for example_idx, example in generate_examples(filepath_by_component):
        doc_id = f'{base_tag}.json.gz/{example_idx}'

        example['meta']['partition'] = partition
        example['quality_signals']['is_duplicate'] = (
            doc_id in duplicates if duplicates else None
        )

        yield f'{base_tag}_{example_idx}', {
            'raw_content': example['raw_content'],
            'doc_id': doc_id,
            'meta': json.dumps(example['meta']),
            'quality_signals': json.dumps(example['quality_signals']),
        }

    return beam.Create(
        filepath_by_component_by_base_tag.items()
    ) | beam.FlatMapTuple(_process_base_tag)


@contextlib.contextmanager
def open_gzip(filepath):
  with epath.Path(filepath).open('rb') as f:
    yield gzip.open(f)


def _generate_tail(filepath_by_component) -> Iterator[tuple[int, _Example]]:
  """Yields examples for tail partitions."""
  try:
    with open_gzip(filepath_by_component[_DOCS_COMPONENT]) as docs_file:
      for idx, doc in enumerate(docs_file):
        if example := _get_example(doc, None):
          yield idx, example
  except gzip.BadGzipFile:
    # skip broken gzip files
    return


def _generate_head_middle(
    filepath_by_component,
) -> Iterator[tuple[int, _Example]]:
  """Yields examples for head and middle partitions."""
  try:
    with open_gzip(
        filepath_by_component[_DOCS_COMPONENT]
    ) as docs_file, open_gzip(
        filepath_by_component[_SIGNALS_COMPONENT]
    ) as signals_file:
      for idx, (doc, signals) in enumerate(zip(docs_file, signals_file)):
        if example := _get_example(doc, signals):
          yield idx, example
  except gzip.BadGzipFile:
    # skip broken gzip files
    return


def _get_example(doc: str, signals: str | None) -> _Example | None:
  """Returns an example."""
  try:
    doc = json.loads(doc)
    signals = json.loads(signals) if signals else {}

    meta = {
        key: doc[key]
        for key in [
            'url',
            'language',
            'source_domain',
            'date_download',
            'digest',
        ]
    }

    return {
        'raw_content': doc['raw_content'],
        'meta': meta,
        'quality_signals': signals.get('quality_signals', {}),
    }
  except:  # pylint: disable=bare-except
    return None
