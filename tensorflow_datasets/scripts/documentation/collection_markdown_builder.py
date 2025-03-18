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

"""Dataset collection catalog documentation template."""

import abc
import textwrap
from typing import List

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import dataset_markdown_builder as dmb
from tensorflow_datasets.scripts.documentation import doc_utils

# Token used to indicate the section shouldn't be displayed
_SKIP_SECTION = object()


class CollectionSection(abc.ABC):
  """Abstract class for a documentation Section (description, homepage, ...)."""

  NAME: str
  EXTRA_DOC: str = ''

  @abc.abstractmethod
  def get_key(self, loader: tfds.core.DatasetCollectionLoader) -> dmb.Key:
    """Get the key of the section.

    The key is used to merge similar sections across builder configs. For
    instance, https://www.tensorflow.org/datasets/catalog/wiki40b only display
    once the `FeatureDict`, homepage,... as those sections are the same for
    all configs.

    Args:
      loader: The loader of the DatasetCollection to document.

    Returns:
      key: The section key.
    """
    pass

  @abc.abstractmethod
  def content(self, loader: tfds.core.DatasetCollectionLoader) -> str:
    """Returns the section content."""
    pass

  def display(self, loader: tfds.core.DatasetCollectionLoader) -> str:
    """Returns the section content."""
    content = self.content(loader)
    if content is _SKIP_SECTION:
      return ''
    header = f'*   **{self.NAME}**{self.EXTRA_DOC}'
    is_block = isinstance(content, dmb.Block)
    if not isinstance(content, dmb.IntentedBlock):
      content = content.strip()  # Note: `strip()` cast `Block` -> `str`
    if is_block:
      content = f'{header}:\n\n{content}\n\n'
    else:
      content = f'{header}: {content}\n\n'
    return content


# ------------------------------ Sections -------------------------------------

# pylint:disable = missing-class-docstring


class CollectionHomepageSection(CollectionSection):
  NAME = 'Homepage'

  def get_key(self, loader: tfds.core.DatasetCollectionLoader):
    return loader.collection.info.homepage

  def content(self, loader: tfds.core.DatasetCollectionLoader):
    homepage = self.get_key(loader)
    if homepage:
      homepage = doc_utils.format_homepage_url(homepage)
    else:
      homepage = ''
    return dmb.Block(homepage)


class CollectionDescriptionSection(CollectionSection):
  NAME = 'Description'

  def get_key(self, loader: tfds.core.DatasetCollectionLoader):
    return loader.collection.info.description

  def content(self, loader: tfds.core.DatasetCollectionLoader):
    return dmb.Block(loader.collection.info.description)


class CollectionVersionSection(CollectionSection):
  """Lists versions in the dataset collection, along with their datasets."""

  NAME = 'Versions'

  def _list_versions(self, loader: tfds.core.DatasetCollectionLoader):
    """List versions."""
    # Default version is the latest.
    default_version = loader.collection.get_latest_version()
    all_versions = [
        *loader.collection.info.release_notes,
        *loader.collection.datasets,
    ]

    all_versions_and_notes = loader.collection.info.release_notes

    all_versions = set(tfds.core.Version(v) for v in all_versions)

    for v in sorted(all_versions):  # List all available versions.
      if v == default_version:  # Highlight the default version.
        version_name = '**`{}`** (default)'.format(str(v))
      else:
        version_name = '`{}`'.format(str(v))
      description = all_versions_and_notes.get(str(v), 'No release notes.')
      yield f'    * {version_name}: {description}'

  def get_key(self, loader: tfds.core.DatasetCollectionLoader):
    release_key = tuple(
        (k, v) for k, v in loader.collection.info.release_notes.items()
    )
    return (tuple(loader.collection.all_versions), release_key)

  def content(self, loader: tfds.core.DatasetCollectionLoader):
    return dmb.IntentedBlock('\n'.join(self._list_versions(loader)))


class CollectionDatasetsSection(CollectionSection):
  NAME = 'Datasets in the default version'

  def get_key(self, loader: tfds.core.DatasetCollectionLoader):
    return loader.collection.get_latest_version()

  def _get_dataset_catalog_link(self, reference):
    """Returns the link to a dataset documentation in TFDS catalog."""
    prefix = 'https://www.tensorflow.org/datasets/catalog/'
    # Links to TFDS catalog's entries don't include versions.
    ds_link = prefix + reference.dataset_name
    # For configs, return precise link to config documentation.
    if reference.config:
      ds_link += f'#{reference.config}'
    return ds_link

  def _list_datasets(
      self, collection_loader: tfds.core.DatasetCollectionLoader
  ):
    """List datasets for the latest version."""
    # get_collection retrieves the datasets in the default (= latest) version.
    datasets = collection_loader.collection.get_collection()
    for name, reference in datasets.items():
      ds_link = self._get_dataset_catalog_link(reference)
      yield f'    * `{name}`: [`{reference.tfds_name()}`]({ds_link})'

  def content(self, loader: tfds.core.DatasetCollectionLoader):
    return dmb.IntentedBlock('\n'.join(self._list_datasets(loader)))


class CollectionCitationSection(CollectionSection):
  NAME = 'Citation'

  def get_key(self, loader: tfds.core.DatasetCollectionLoader):
    return loader.collection.info.citation

  def content(self, loader: tfds.core.DatasetCollectionLoader):
    if not loader.collection.info.citation:
      return ''
    return dmb.Block(textwrap.dedent(f"""
            ```
            {tfds.core.utils.indent(loader.collection.info.citation, '            ')}
            ```
            """))


# --------------------------- Main page ---------------------------


def _display_collection_heading(
    collection: tfds.core.DatasetCollectionLoader,
) -> str:
  return f"""
      # `{collection.collection_name}`

      """


def _display_collection_sections(
    loader: tfds.core.DatasetCollectionLoader,
    all_sections: List[CollectionSection],
) -> str:
  return ''.join([section.display(loader) for section in all_sections])


def get_collection_markdown_string(
    *,
    collection: tfds.core.DatasetCollectionLoader,
) -> str:
  """Build the collection markdown."""
  all_sections = [
      CollectionDescriptionSection(),
      CollectionHomepageSection(),
      CollectionVersionSection(),
      CollectionDatasetsSection(),
      CollectionCitationSection(),
  ]

  doc_str = [
      _display_collection_heading(collection),
      _display_collection_sections(
          loader=collection, all_sections=all_sections
      ),
  ]
  return '\n\n'.join([tfds.core.utils.dedent(s) for s in doc_str if s])
