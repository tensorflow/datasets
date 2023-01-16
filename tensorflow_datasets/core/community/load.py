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

"""Utils to load community datasets."""

import importlib
import sys
from typing import Type

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.community import huggingface_wrapper


def builder_cls_from_module(
    module_name: str,
) -> Type[dataset_builder.DatasetBuilder]:
  """Imports the module and extract the `tfds.core.DatasetBuilder`.

  Args:
    module_name: Dataset module to import containing the dataset definition
      (e.g. `tensorflow_datasets.image.mnist.mnist`)

  Returns:
    The extracted tfds.core.DatasetBuilder builder class.
  """
  if module_name not in sys.modules:  # Module already imported
    # Module can be created during execution, so call invalidate_caches() to
    # make sure the new module is noticed by the import system.
    importlib.invalidate_caches()

    # Executing the module will register the datasets in _MODULE_TO_DATASETS.
    with registered.skip_registration(), huggingface_wrapper.mock_huggingface_import():
      importlib.import_module(module_name)
      # TODO(tfds): For community-installed modules, we should raise cleaner
      # error if there is additional missing dependency. E.g. Parsing all
      # import statements. Or wrap this `importlib.import_module` within a
      # `with lazy_imports():` context manager ?

  builder_classes = registered._MODULE_TO_DATASETS.get(module_name, [])  # pylint: disable=protected-access

  if len(builder_classes) != 1:
    raise ValueError(
        f'Could not load DatasetBuilder from: {module_name}. '
        'Make sure the module only contains a single `DatasetBuilder`.\n'
        'If no dataset is detected, make sure that all abstractmethods are '
        'implemented.\n'
        f'Detected builders: {builder_classes}'
    )
  return builder_classes[0]
