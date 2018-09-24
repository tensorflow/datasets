# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Access registered datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import naming

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}
REGISTERED_OVERRIDE_ATTR = "REGISTERED"


class RegisteredDataset(type):
  """Subclasses will be registered and given a `name` property."""

  def __new__(mcs, cls_name, bases, class_dict):
    name = naming.camelcase_to_snakecase(cls_name)
    class_dict["name"] = name
    cls = type.__new__(mcs, cls_name, bases, class_dict)

    if name in _DATASET_REGISTRY:
      raise ValueError("Dataset with name %s already registered." % name)
    should_register = class_dict.get(REGISTERED_OVERRIDE_ATTR, True)
    if should_register:
      _DATASET_REGISTRY[name] = cls
    return cls


def registered():
  """Returns names of all registered datasets."""
  return sorted(list(_DATASET_REGISTRY))


def builder(name):
  """Returns the DatasetBuilder class registered with name."""
  if name not in _DATASET_REGISTRY:
    all_datasets_str = "".join(["  * %s\n" % d for d in registered()])
    raise ValueError("Dataset %s not found. Available datasets:\n%s" %
                     (name, all_datasets_str))
  return _DATASET_REGISTRY[name]


@api_utils.disallow_positional_args
def load(name,
         data_dir=api_utils.REQUIRED_ARG,
         download=False,
         **as_dataset_kwargs):
  """Load tf.data.Dataset.

  This is a convenience method that fetches the dataset by string, optionally
  calls DatasetBuilder.download_and_prepare, and then calls
  DatasetBuilder.as_dataset.

  Args:
    name (str): DatasetBuilder name. This is the class name snake-cased.
    data_dir (str): directory to read/write data.
    download (bool): whether to call download_and_prepare before calling
      as_dataset. If False, data is expected to be in data_dir. If True and the
      data is already in data_dir, download_and_prepare is a no-op.
    **as_dataset_kwargs (dict): Keyword arguments to pass to as_dataset.

  Returns:
    tf.data.Dataset
  """
  dbuilder = builder(name)(data_dir=data_dir)
  if download:
    dbuilder.download_and_prepare()
  return dbuilder.as_dataset(**as_dataset_kwargs)
