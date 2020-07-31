# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

r"""Tool to generate the dataset catalog documentation.
"""

import argparse
import os
from typing import List, Optional

from absl import app
from absl.flags import argparse_flags
import dataclasses

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import document_datasets
import yaml


def _parse_flags(_) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog='build_catalog',
      description='Tool to generate the dataset catalog documentation',
  )
  parser.add_argument(
      '--datasets',
      help='Comma separated list of datasets to document. None for all '
      'datasets.',
  )
  parser.add_argument(
      '--catalog_dir',
      help='Directory path where to generate the catalog. Default to TFDS dir.',
  )
  return parser.parse_args()


def main(args: argparse.Namespace):
  catalog_dir = args.catalog_dir or os.path.join(
      tfds.core.utils.tfds_dir(),
      'docs',
      'catalog',
  )

  build_catalog(
      datasets=args.datasets.split(',') if args.datasets else None,
      catalog_dir=catalog_dir,
  )


@dataclasses.dataclass
class DatasetItem(object):
  name: str
  path: str
  is_nightly: bool = False


def create_section_toc(section, section_datasets):
  heading = '\n### `%s`\n' % section
  nightly_suffix = ' ' + document_datasets.NightlyDocUtil.icon
  entries = [
      f' * [`{item.name}`]({item.path})' +
      (item.is_nightly and nightly_suffix or '') for item in section_datasets
  ]
  return '\n'.join([heading] + entries)


def build_catalog(
    datasets: Optional[List[str]] = None,
    catalog_dir: Optional[str] = None,
    toc_relative_path: str = '/datasets/catalog/',
) -> None:
  """Document all datasets, including the table of content.

  Args:
    datasets: Lists of dataset to document (all if not set)
    catalog_dir: Destination path for the catalog
    toc_relative_path: Relative path of the catalog directory, used to
      generate the table of content relative links.
  """
  # Build datasets doc
  print('Build datasets overview...')
  overview_doc, datasets_dict = document_datasets.dataset_docs_str(datasets)

  # For _toc.yaml
  toc_dictionary = {'toc': [{
      'title': 'Overview',
      'path': os.path.join(toc_relative_path, 'overview'),
  }]}

  section_tocs = []

  nightly_util = document_datasets.NightlyDocUtil()

  print('Build Sections')
  for section, datasets_in_section in sorted(list(datasets_dict.items())):
    print('Section %s...' % section)
    section_str = section.replace('_', ' ').capitalize()
    sec_dict = {'title': section_str}
    sec_paths = list()
    section_toc = []
    for dataset_name, is_manual, doc in datasets_in_section:
      print('Dataset %s...' % dataset_name)

      sidebar_item = {
          'path': os.path.join(toc_relative_path, dataset_name),
          'title': dataset_name + (' (manual)' if is_manual else '')
      }
      ds_item = DatasetItem(
          name=dataset_name,
          path=dataset_name + '.md',
      )
      if nightly_util.is_builder_nightly(dataset_name):
        sidebar_item['status'] = 'nightly'
        ds_item.is_nightly = True

      sec_paths.append(sidebar_item)
      section_toc.append(ds_item)

      dataset_file = os.path.join(catalog_dir, dataset_name + '.md')
      with tf.io.gfile.GFile(dataset_file, 'w') as f:
        f.write(doc)

    section_tocs.append(create_section_toc(section_str, section_toc))
    sec_dict['section'] = sec_paths
    toc_dictionary['toc'].append(sec_dict)

  with tf.io.gfile.GFile(os.path.join(catalog_dir, 'overview.md'), 'w') as f:
    f.write(overview_doc.format(toc='\n'.join(section_tocs)))

  with tf.io.gfile.GFile(os.path.join(catalog_dir, '_toc.yaml'), 'w') as f:
    yaml.dump(toc_dictionary, f, default_flow_style=False)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
