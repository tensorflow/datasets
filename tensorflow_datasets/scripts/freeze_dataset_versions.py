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

r"""Dump the list of all registered datasets/config/version in a `.txt` file.

Instructions:

```
python tensorflow_datasets/scripts/freeze_dataset_version.py
```


"""

from absl import app

import tensorflow_datasets as tfds


def main(_):
  tfds.core.visibility.set_availables([
      tfds.core.visibility.DatasetType.TFDS_PUBLIC,
      tfds.core.visibility.DatasetType
  ])

  registered_names = tfds.core.load.list_full_names()
  version_path = tfds.core.utils.tfds_write_path() / 'stable_versions.txt'
  version_path.write_text('\n'.join(registered_names))
  print(f'{len(registered_names)} datasets versions written.')


if __name__ == '__main__':
  app.run(main)
