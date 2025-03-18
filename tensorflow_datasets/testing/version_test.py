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

import dataclasses
import inspect

import tensorflow_datasets as tfds

_DO_NOT_CKECK_DATASETS = ['imagenet_v2']


@dataclasses.dataclass(frozen=True, kw_only=True)
class _BuilderWithVersionMismatch:
  name: str
  file: str
  version: str
  max_version_in_release_notes: str


def test_internal_datasets_have_versions_on_line_with_the_release_notes():
  builders = tfds.list_builders(with_community_datasets=False)
  assert builders
  builders_with_version_mismatch: list[_BuilderWithVersionMismatch] = []
  for builder in builders:
    builder_cls = tfds.core.registered.imported_builder_cls(builder)
    if builder_cls.name in _DO_NOT_CKECK_DATASETS:
      continue
    if not (
        hasattr(builder_cls, 'VERSION')
        and hasattr(builder_cls, 'RELEASE_NOTES')
    ):
      # This can be the case for test datasets
      continue
    if builder_cls.VERSION and builder_cls.RELEASE_NOTES:
      max_version_in_release_notes = max(
          [tfds.core.Version(version) for version in builder_cls.RELEASE_NOTES]
      )
      version = tfds.core.Version(builder_cls.VERSION)
      if version < max_version_in_release_notes:
        # This means the builder is as follow:
        # ```
        # RELEASE_NOTES = {
        #   '1.0.1': 'Bug fix.',
        #   '1.0.0': 'Initial release.',
        # }
        # VERSION = '1.0.0'  # <- Someone forgot to increment this version.
        # ```
        file = inspect.getfile(builder_cls).split('tensorflow_datasets/')[-1]
        builders_with_version_mismatch.append(
            _BuilderWithVersionMismatch(
                name=builder_cls.name,
                file=file,
                version=version,
                max_version_in_release_notes=max_version_in_release_notes,
            )
        )
  if builders_with_version_mismatch:
    error = 'The following datasets have a version mismatch:'
    for builder_cls in builders_with_version_mismatch:
      error += (
          f'\n  - Dataset {builder_cls.name} ({builder_cls.file}) has VERSION='
          f'"{builder_cls.version}" but RELEASE_NOTES contains version'
          f' "{builder_cls.max_version_in_release_notes}".'
      )
    raise ValueError(error)
