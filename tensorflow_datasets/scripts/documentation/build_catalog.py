# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
import collections
import os
from typing import Dict, List, Optional

from absl import app
from absl.flags import argparse_flags

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import doc_utils
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
  # Note: The automated generation call `build_catalog.build_catalog()`
  # directly, so no code should go in `main()`.

  catalog_dir = args.catalog_dir or os.path.join(
      tfds.core.utils.tfds_write_path(),
      'docs',
      'catalog',
  )

  build_catalog(
      datasets=args.datasets.split(',') if args.datasets else None,
      catalog_dir=catalog_dir,
  )


def _create_section_toc(
    section: str,
    builder_docs: List[document_datasets.BuilderDocumentation],
) -> str:
  """Creates the section of the `overview.md` table of content."""
  heading = '\n### `%s`\n' % section
  nightly_suffix = ' ' + doc_utils.NightlyDocUtil.icon
  entries = [
      f' * [`{doc.name}`]({doc.filestem}.md)' +
      (doc.is_nightly and nightly_suffix or '') for doc in builder_docs
  ]
  return '\n'.join([heading] + entries)


def build_catalog(
    datasets: Optional[List[str]] = None,
    *,
    catalog_dir: Optional[tfds.core.utils.PathLike] = None,
    doc_util_paths: Optional[doc_utils.DocUtilPaths] = None,
    toc_relative_path: str = '/datasets/catalog/',
    index_template: Optional[tfds.core.utils.PathLike] = None,
    index_filename: str = 'overview.md',
    dataset_types: Optional[List[tfds.core.visibility.DatasetType]] = None,
) -> None:
  """Document all datasets, including the table of content.

  Args:
    datasets: Lists of dataset to document (all if not set)
    catalog_dir: Destination path for the catalog
    doc_util_paths: Additional path for visualization, nightly info,...
    toc_relative_path: Relative path of the catalog directory, used to generate
      the table of content relative links.
    index_template: Default template for the index page.
    index_filename: Name of the catalog index file.
    dataset_types: Restrict the generation to the given dataset types. Default
      to all open source non-community datasets
  """
  dataset_types = dataset_types or [
      tfds.core.visibility.DatasetType.TFDS_PUBLIC,
      tfds.core.visibility.DatasetType
  ]
  tfds.core.visibility.set_availables(dataset_types)

  catalog_dir = tfds.core.as_path(catalog_dir)
  index_template = index_template or tfds.core.tfds_path(
      'scripts/documentation/templates/catalog_overview.md')
  index_template = tfds.core.as_path(index_template)

  # Iterate over the builder documentations
  section_to_builder_docs = collections.defaultdict(list)
  for builder_doc in document_datasets.iter_documentation_builders(
      datasets, doc_util_paths=doc_util_paths or doc_utils.DocUtilPaths()):
    # Write the builder documentation
    dataset_file = catalog_dir / f'{builder_doc.filestem}.md'
    dataset_file.write_text(builder_doc.content)
    # Save the category
    section_to_builder_docs[builder_doc.section].append(builder_doc)

  _save_table_of_content(
      catalog_dir=catalog_dir,
      section_to_builder_docs=section_to_builder_docs,
      toc_relative_path=toc_relative_path,
      index_template=index_template,
      index_filename=index_filename,
  )


def _save_table_of_content(
    catalog_dir: tfds.core.ReadWritePath,
    section_to_builder_docs: Dict[str,
                                  List[document_datasets.BuilderDocumentation]],
    toc_relative_path: str,
    index_template: tfds.core.ReadOnlyPath,
    index_filename: str,
) -> None:
  """Builds and saves the table of contents (`_toc.yaml` and `overview.md`)."""
  # For _toc.yaml
  toc_yaml = {
      'toc': [{
          'title': 'Overview',
          'path': os.path.join(toc_relative_path, 'overview'),
      }]
  }
  # For overview.md
  toc_overview = []

  # All builder documented, save the table of content
  for section, builder_docs in sorted(section_to_builder_docs.items()):
    builder_docs = sorted(builder_docs, key=lambda doc: doc.name)
    # `object_detection` -> `Object detection`
    section_str = section.replace('_', ' ').capitalize()

    # Add `_toc.yaml` section
    sec_dict = {'title': section_str, 'section': []}
    for doc in builder_docs:
      sidebar_item = {
          'path': os.path.join(toc_relative_path, doc.filestem),
          'title': doc.name + (' (manual)' if doc.is_manual else '')
      }
      if doc.is_nightly:
        sidebar_item['status'] = 'nightly'
      sec_dict['section'].append(sidebar_item)
    toc_yaml['toc'].append(sec_dict)

    # Add `overview.md` section
    toc_overview.append(_create_section_toc(section_str, builder_docs))

  # Write the `overview.md` page
  index_str = index_template.read_text().format(toc='\n'.join(toc_overview))
  catalog_dir.joinpath(index_filename).write_text(index_str)

  # Write the `_toc.yaml` TF documentation navigation bar
  with catalog_dir.joinpath('_toc.yaml').open('w') as f:
    yaml.dump(toc_yaml, f, default_flow_style=False)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
