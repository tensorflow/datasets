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

"""Util to globally control which datasets can be accessed.

Different scripts may access different datasets (community datasets,...).

By default all TFDS scripts only have access to open-source non-community
datasets. This avoid accidentally accessing datasets (e.g. documenting
community datasets in the TFDS documentation).

Scripts which require additional datasets visibility should explicitly opt-in
for the requested category:

```python
tfds.core.visibility.set_availables([
    tfds.core.visibility.DatasetType.TFDS_PUBLIC,
    tfds.core.visibility.DatasetType.COMMUNITY_PUBLIC,
])
```

Updating the visibility affect the following functions:

* `tfds.load`
* `tfds.list_builders`
* `tfds.core.load.list_full_names`

"""

import contextlib
import enum
import pathlib
from typing import Iterable, Iterator, List

from absl import app


class DatasetType(enum.Enum):
  TFDS_PUBLIC = enum.auto()
  COMMUNITY_PUBLIC = enum.auto()

  def is_available(self) -> bool:
    return self in _current_available


# Default datasets availables.
# For TFDS internal scripts, this is overwritten in `_set_default_visibility`
_current_available = {
    DatasetType.TFDS_PUBLIC,
    DatasetType.COMMUNITY_PUBLIC,
}


def set_availables(new_ds_types: Iterable[DatasetType]) -> None:
  """Overwrites the current visibility permissions.

  Calling this function will affect the returned value of
  `tfds.list_builders`,...

  Args:
    new_ds_types: New ds types.
  """
  _current_available.clear()
  _current_available.update(new_ds_types)


def get_availables() -> List[DatasetType]:
  """Returns availables dataset types."""
  return sorted(_current_available, key=lambda ds_type: ds_type.name)


@contextlib.contextmanager
def set_availables_tmp(new_ds_types: Iterable[DatasetType]) -> Iterator[None]:
  """Contextmanager/decorator version of `set_availables`."""
  old_ds_types = set(_current_available)
  try:
    set_availables(new_ds_types)
    yield
  finally:
    set_availables(old_ds_types)  # Restore previous permissions


def _set_default_visibility() -> None:
  """Overwrittes the default visibility for the TFDS scripts.

  If the script executed is a TFDS script, then restrict the visibility
  to only open-source non-community datasets.

  """
  import __main__  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top
  main_file = getattr(__main__, '__file__', None)
  if main_file and 'tensorflow_datasets' in pathlib.Path(main_file).parts:
    # If the script is launched from within a TFDS script, we disable community
    # datasets and restrict scripts to only public datasets.
    # Accessing community datasets should be explicitly requested.
    set_availables([
        DatasetType.TFDS_PUBLIC,
    ])


app.call_after_init(_set_default_visibility)
