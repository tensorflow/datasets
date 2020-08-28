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

"""Splits related API."""

import typing
from typing import List, Union

from tensorflow_datasets.core import proto
from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import shard_utils


@utils.as_proto_cls(proto.SplitInfo)
class SplitInfo(object):
  """Wraps `proto.SplitInfo` with an additional property."""

  @property
  def num_examples(self) -> int:
    if self.shard_lengths:  # pytype: disable=attribute-error
      return sum(int(sl) for sl in self.shard_lengths)  # pytype: disable=attribute-error
    return int(self.statistics.num_examples)  # pytype: disable=attribute-error

  @property
  def num_shards(self) -> int:
    if self.shard_lengths:
      return len(self.shard_lengths)
    return self._ProtoCls__proto.num_shards

  def __repr__(self) -> str:
    num_examples = self.num_examples or "unknown"
    return "<tfds.core.SplitInfo num_examples=%s>" % str(num_examples)

  @property
  def file_instructions(self) -> List[shard_utils.FileInstruction]:
    """Returns the list of dict(filename, take, skip).

    This allows for creating your own `tf.data.Dataset` using the low-level
    TFDS values.

    Example:

    ```
    file_instructions = info.splits['train[75%:]'].file_instructions
    instruction_ds = tf.data.Dataset.from_generator(
        lambda: file_instructions,
        output_types={
            'filename': tf.string,
            'take': tf.int64,
            'skip': tf.int64,
        },
    )
    ds = instruction_ds.interleave(
        lambda f: tf.data.TFRecordDataset(
            f['filename']).skip(f['skip']).take(f['take'])
    )
    ```

    When `skip=0` and `take=-1`, the full shard will be read, so the `ds.skip`
    and `ds.take` could be skipped.

    Returns:
      A `dict(filename, take, skip)`
    """
    # `self._dataset_name` is assigned in `SplitDict.add()`.
    return tfrecords_reader.make_file_instructions(
        name=self._dataset_name,
        split_infos=[self],
        instruction=str(self.name),
    )

  @property
  def filenames(self) -> List[str]:
    """Returns the list of filenames."""
    return sorted(f.filename for f in self.file_instructions)


class SubSplitInfo(object):
  """Wrapper around a sub split info.

  This class expose info on the subsplit:

  ```
  ds, info = tfds.load(..., split='train[75%:]', with_info=True)
  info.splits['train[75%:]'].num_examples
  ```

  """

  def __init__(self, file_instructions: List[shard_utils.FileInstruction]):
    """Constructor.

    Args:
      file_instructions: List[FileInstruction]
    """
    self._file_instructions = file_instructions

  @property
  def num_examples(self) -> int:
    """Returns the number of example in the subsplit."""
    return sum(f.num_examples for f in self._file_instructions)

  @property
  def file_instructions(self) -> List[shard_utils.FileInstruction]:
    """Returns the list of dict(filename, take, skip)."""
    return self._file_instructions

  @property
  def filenames(self) -> List[str]:
    """Returns the list of filenames."""
    return sorted(f.filename for f in self.file_instructions)


# TODO(epot): `: tfds.Split` type should be `Union[str, Split]`
class Split(str):
  # pylint: disable=line-too-long
  """`Enum` for dataset splits.

  Datasets are typically split into different subsets to be used at various
  stages of training and evaluation.

  * `TRAIN`: the training data.
  * `VALIDATION`: the validation data. If present, this is typically used as
    evaluation data while iterating on a model (e.g. changing hyperparameters,
    model architecture, etc.).
  * `TEST`: the testing data. This is the data to report metrics on. Typically
    you do not want to use this during model iteration as you may overfit to it.

  See the
  [guide on splits](https://github.com/tensorflow/datasets/tree/master/docs/splits.md)
  for more information.
  """

  def __repr__(self) -> str:
    return "{}({})".format(type(self).__name__, super(Split, self).__repr__())  # pytype: disable=wrong-arg-types


Split.TRAIN = Split("train")
Split.TEST = Split("test")
Split.VALIDATION = Split("validation")

if typing.TYPE_CHECKING:
  # For type checking, `tfds.Split` is an alias for `str` with additional
  # `.TRAIN`, `.TEST`,... attributes. All strings are valid split type.
  Split = Union[Split, str]


class SplitDict(utils.NonMutableDict):
  """Split info object."""

  def __init__(self, dataset_name):
    super(SplitDict, self).__init__(error_msg="Split {key} already present")
    self._dataset_name = dataset_name

  def __getitem__(self, key):
    # 1st case: The key exists: `info.splits['train']`
    if str(key) in self:
      return super(SplitDict, self).__getitem__(str(key))
    # 2nd case: Uses instructions: `info.splits['train[50%]']`
    else:
      instructions = tfrecords_reader.make_file_instructions(
          name=self._dataset_name,
          split_infos=self.values(),
          instruction=key,
      )
      return SubSplitInfo(instructions)

  def __setitem__(self, key, value):
    raise ValueError("Cannot add elem. Use .add() instead.")

  def add(self, split_info):
    """Add the split info."""
    if split_info.name in self:
      raise ValueError("Split {} already present".format(split_info.name))
    # Forward the dataset name required to build file instructions:
    # info.splits['train'].file_instructions
    # Use `object.__setattr__`, because ProtoCls forbid new fields assignement.
    object.__setattr__(split_info, "_dataset_name", self._dataset_name)
    super(SplitDict, self).__setitem__(split_info.name, split_info)

  @classmethod
  def from_proto(cls, dataset_name, repeated_split_infos):
    """Returns a new SplitDict initialized from the `repeated_split_infos`."""
    split_dict = cls(dataset_name)
    for split_info_proto in repeated_split_infos:
      split_info = SplitInfo()
      split_info.CopyFrom(split_info_proto)
      split_dict.add(split_info)
    return split_dict

  def to_proto(self):
    """Returns a list of SplitInfo protos that we have."""
    # Return the proto.SplitInfo, sorted by name
    return sorted((s.get_proto() for s in self.values()), key=lambda s: s.name)

  @property
  def total_num_examples(self):
    """Return the total number of examples."""
    return sum(s.num_examples for s in self.values())

  def copy(self):
    return SplitDict.from_proto(self._dataset_name, self.to_proto())


def check_splits_equals(splits1, splits2):
  """Check two split dicts have same name, shard_lengths and num_shards."""
  if set(splits1) ^ set(splits2):  # Name intersection should be null
    return False
  for _, (split1, split2) in utils.zip_dict(splits1, splits2):
    if (split1.num_shards != split2.num_shards or
        split1.shard_lengths != split2.shard_lengths):
      return False
  return True


class SplitGenerator(object):
  """Defines the split information for the generator.

  This should be used as returned value of
  `GeneratorBasedBuilder._split_generators`.
  See `GeneratorBasedBuilder._split_generators` for more info and example
  of usage.
  """

  def __init__(self, name, gen_kwargs=None):
    """Constructs a `SplitGenerator`.

    Args:
      name: `str`, name of the Split for which the generator will
        create the examples.
      gen_kwargs: `dict`, kwargs to forward to the _generate_examples() method
        of the builder.
    """
    self.name = name
    self.gen_kwargs = gen_kwargs or {}
    self.split_info = SplitInfo(name=str(name))


def even_splits(
    split: str,
    n: int,
) -> List[str]:
  """Generates a list of sub-splits of same size.

  Example:

  ```python
  assert tfds.even_splits('train', n=3) == [
      'train[0%:33%]', 'train[33%:67%]', 'train[67%:100%]
  ]
  ```

  Args:
    split: Split name (e.g. 'train', 'test',...)
    n: Number of sub-splits to create

  Returns:
    The list of subsplits.
  """
  if n <= 0:
    raise ValueError(f"n should be > 0. Got {n}")
  partitions = [round(i * 100 / n) for i in range(n + 1)]
  return [
      f"{split}[{partitions[i]}%:{partitions[i+1]}%]" for i in range(n)
  ]
