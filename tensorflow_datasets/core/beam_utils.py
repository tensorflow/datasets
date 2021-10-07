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

"""Beam utils."""

from typing import Any

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import shard_utils

__all__ = [
    'ReadFromTFDS',
]


@lazy_imports_lib.beam_ptransform_fn
def ReadFromTFDS(
    pipeline,
    builder: dataset_builder.DatasetBuilder,
    split: str,
    **as_dataset_kwargs: Any,
):
  """Creates a beam pipeline yielding TFDS examples.

  Each dataset shard will be processed in parallel.

  Usage:

  ```python
  builder = tfds.builder('my_dataset')

  _ = (
      pipeline
      | tfds.beam.ReadFromTFDS(builder, split='train')
      | beam.Map(tfds.as_numpy)
      | ...
  )
  ```

  Use `tfds.as_numpy` to convert each examples from `tf.Tensor` to numpy.

  Args:
    pipeline: beam pipeline (automatically set)
    builder: Dataset builder to load
    split: Split name to load (e.g. `train+test`, `train`)
    **as_dataset_kwargs: Arguments forwarded to `builder.as_dataset`.

  Returns:
    The PCollection containing the TFDS examples.
  """
  beam = lazy_imports_lib.lazy_imports.apache_beam

  if '[' in split:
    raise NotImplementedError(
        f'ReadFromTFDS only supports plain splits. Got {split!r}. '
        'Please open a github issue if you need this feature.')
  if not builder.info.splits.total_num_examples:
    raise ValueError(
        f'No examples found in {builder.name!r}. Was the dataset generated ?')

  def load_shard(file_instruction: shard_utils.FileInstruction):  # pylint: disable=invalid-name
    """Loads a single shard."""
    file_info = naming.FilenameInfo.from_str(file_instruction.filename)
    # Could try to support subsplit by adding `ds.skip(file_instruction.skip)`
    # but won't work if `batch_size =! None`. The best way would be to convert
    # file_instruction to absolute instructions (and check that
    # `splits[abs_split].file_instructions == [file_instruction]` ).
    ds = builder.as_dataset(
        split=f'{file_info.split}[{file_info.shard_index}shard]',
        **as_dataset_kwargs,
    )
    return ds

  file_instructions = builder.info.splits[split].file_instructions
  return pipeline | beam.Create(file_instructions) | beam.FlatMap(load_shard)
