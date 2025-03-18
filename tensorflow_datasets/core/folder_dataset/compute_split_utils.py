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

r"""Pipeline which computes the number of examples in a dataset."""

import collections
from collections.abc import Mapping, Sequence, Set
import dataclasses
import functools
import itertools
import os
import pprint
from typing import Optional, Type, Union, cast

from etils import epath
from etils import etree
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as split_lib
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_data_source

from google.protobuf import json_format

_SplitFilesDict = Mapping[str, Sequence[naming.FilenameInfo]]


@dataclasses.dataclass
class _ShardInfo:
  """Metadata computed for each shard."""

  file_info: naming.FilenameInfo
  num_examples: int
  bytes_size: int


def _enrich_filename_template(
    filename_template: naming.ShardedFileTemplate,
    files_per_split: _SplitFilesDict,
) -> naming.ShardedFileTemplate:
  """Overrides the template's dataset name and suffix based on the filenames."""
  found_dataset_names = set()
  found_filetype_suffixes = set()
  for file_infos in files_per_split.values():
    for file_info in file_infos:
      found_dataset_names.add(file_info.dataset_name)
      found_filetype_suffixes.add(file_info.filetype_suffix)

  dataset_name = None
  if len(found_dataset_names) == 1:
    dataset_name = next(iter(found_dataset_names))
  elif len(found_dataset_names) > 1:
    raise ValueError(f'Found multiple dataset names: {found_dataset_names}')

  filetype_suffix = None
  if len(found_filetype_suffixes) == 1:
    filetype_suffix = next(iter(found_filetype_suffixes))
  if len(found_filetype_suffixes) > 1:
    raise ValueError(
        f'Found multiple filetype suffixes: {found_filetype_suffixes}'
    )

  return filename_template.replace(
      dataset_name=dataset_name, filetype_suffix=filetype_suffix
  )


def compute_split_info_from_directory(
    *,
    out_dir: Optional[epath.PathLike] = None,
    data_dir: epath.PathLike,
    filename_template: Union[None, str, naming.ShardedFileTemplate] = None,
) -> Sequence[split_lib.SplitInfo]:
  """Compute the split info for the splits in the given data dir.

  Arguments:
    out_dir: directory where to save the metadata. It should be available from
      the apache beam workers. If not set, apache beam won't be used (only
      available with some file formats).
    data_dir: directory where the data is.
    filename_template: the template to which the data files correspond. If None,
      then the default template is used.

  Returns:
    list of split infos for the splits in the given data dir.
  """
  data_dir = epath.Path(data_dir)
  if filename_template is None:
    filename_template = naming.ShardedFileTemplate(data_dir=data_dir)
  elif isinstance(filename_template, str):
    filename_template = naming.ShardedFileTemplate(
        template=filename_template, data_dir=data_dir
    )
  filename_template = filename_template.replace(data_dir=data_dir)

  if (
      filename_template.dataset_name is None
      or filename_template.filetype_suffix is None
  ):
    # Get the dataset name and filetype suffix from the files in the data dir.
    files_per_split = _extract_split_files(filename_template)
    filename_template = _enrich_filename_template(
        filename_template=filename_template, files_per_split=files_per_split
    )
  return compute_split_info(
      out_dir=out_dir, filename_template=filename_template
  )


def compute_split_info(
    *,
    out_dir: Optional[epath.PathLike] = None,
    filename_template: naming.ShardedFileTemplate,
) -> Sequence[split_lib.SplitInfo]:
  """Compute the split info on the given files.

  Compute the split info (num shards, num examples,...) metadata required
  by `tfds.folder_dataset.write_metadata`.

  See documentation for usage:
  https://www.tensorflow.org/datasets/external_tfrecord

  Args:
    out_dir: Output directory where to save the metadata. It should be available
      from the apache beam workers. If not set, apache beam won't be used (only
      available with some file formats).
    filename_template: filename template of the splits. The template should have
      set the data_dir because this is used to compute the split info.

  Returns:
    split_infos: The list of `tfds.core.SplitInfo`.
  """
  # Auto-detect the splits from the files
  split_files = _extract_split_files(filename_template)
  print('Auto-detected splits:')
  for split_name, file_infos in split_files.items():
    print(f' * {split_name}: {file_infos[0].num_shards} shards')

  if out_dir is not None:
    # Launch the beam pipeline to compute the split infos.
    split_infos = _compute_split_statistics_beam(
        split_files=split_files,
        out_dir=out_dir,
        filename_template=filename_template,
    )
  else:
    # Compute split infos locally.
    split_infos = _compute_split_statistics(
        split_files=split_files,
        filename_template=filename_template,
    )

  print('Computed split infos: ')
  pprint.pprint(split_infos)

  return split_infos


def _extract_split_files(
    filename_template: naming.ShardedFileTemplate,
) -> _SplitFilesDict:
  """Extract the files."""
  files = sorted(filename_template.data_dir.iterdir())
  file_infos = [filename_template.parse_filename_info(f.name) for f in files]
  file_infos = [f for f in file_infos if f is not None]
  if not file_infos:
    raise ValueError(
        f'No example files detected in {filename_template.data_dir}. '
        f'Make sure to follow the pattern: {filename_template.template}'
    )

  files_without_splits = []
  split_files = collections.defaultdict(list)
  for file_info in file_infos:
    if file_info.split is not None:
      split_files[file_info.split].append(file_info)
    else:
      files_without_splits.append(file_info)
  if files_without_splits:
    raise ValueError(
        f'Some matched files did not specify the split: {files_without_splits}'
    )

  return split_files


def _assert_split_is_consistent(
    file_infos: Sequence[naming.FilenameInfo],
) -> None:
  # Use unpack syntax on set to implicitly check that all values are the same
  (_,) = {f.split for f in file_infos}

  # Check that all the file-info from the given split are consistent
  # (no missing file)
  shard_ids = sorted(f.shard_index for f in file_infos)
  (num_shards,) = {f.num_shards for f in file_infos}
  if num_shards:
    assert shard_ids == list(range(num_shards)), 'Missing shard files.'


def _compute_split_statistics(
    *,
    split_files: _SplitFilesDict,
    filename_template: naming.ShardedFileTemplate,
) -> Sequence[split_lib.SplitInfo]:
  """Computes and returns the split statistics."""

  adapter = None
  for _, file_infos in split_files.items():
    _assert_split_is_consistent(file_infos)
    if adapter is None:
      (file_suffix,) = {f.filetype_suffix for f in file_infos}
      file_format = file_adapters.file_format_from_suffix(file_suffix)
      adapter = file_adapters.ADAPTER_FOR_FORMAT[file_format]

  # Compute all shard info in parallel
  split_to_shard_infos = cast(
      Mapping[str, Sequence[_ShardInfo]],
      etree.parallel_map(
          functools.partial(
              _process_shard,
              data_dir=filename_template.data_dir,
              adapter=adapter,
          ),
          split_files,
          progress_bar=True,
      ),
  )
  # Create the SplitInfo for all splits
  return [
      _merge_shard_info(shard_infos=si, filename_template=filename_template)
      for si in split_to_shard_infos.values()
  ]


def _compute_split_statistics_beam(
    *,
    split_files: _SplitFilesDict,
    out_dir: epath.PathLike,
    filename_template: naming.ShardedFileTemplate,
) -> Sequence[split_lib.SplitInfo]:
  """Compute statistics."""
  out_dir = epath.Path(out_dir)

  assert out_dir.exists(), f'{out_dir} does not exist'

  # Launch the beam pipeline computation
  runner = None
  # Create the global pipeline object common for all splits
  # Disable type_hint as it doesn't works with typing.Protocol
  beam_options = beam.options.pipeline_options.PipelineOptions()
  beam_options.view_as(
      beam.options.pipeline_options.TypeOptions
  ).pipeline_type_check = False
  with beam.Pipeline(runner=runner, options=beam_options) as pipeline:
    for split_name, file_infos in split_files.items():
      _ = (
          pipeline
          | split_name
          >> _process_split(  # pylint: disable=no-value-for-parameter
              filename_template=filename_template,
              out_dir=out_dir,
              file_infos=file_infos,  # pytype: disable=missing-parameter
          )
      )

  # After the files have been computed
  return [
      _split_info_from_path(
          filename_template.replace(data_dir=out_dir, split=split)
      )
      for split in split_files
  ]


@lazy_imports_lib.beam_ptransform_fn
def _process_split(
    pipeline,
    *,
    filename_template: naming.ShardedFileTemplate,
    out_dir: epath.Path,
    file_infos: Sequence[naming.FilenameInfo],
):
  """Process a single split."""
  # Use unpack syntax on set to implicitly check that all values are the same
  (split_name,) = {f.split for f in file_infos}

  # Check that all the file-info from the given split are consistent
  # (no missing file)
  shard_ids = sorted(f.shard_index for f in file_infos)
  (num_shards,) = {f.num_shards for f in file_infos}
  assert shard_ids == list(range(num_shards)), 'Missing shard files.'

  # Check that the file extension is correct.
  (file_suffix,) = {f.filetype_suffix for f in file_infos}
  file_format = file_adapters.file_format_from_suffix(file_suffix)
  adapter = file_adapters.ADAPTER_FOR_FORMAT[file_format]
  data_dir = epath.Path(filename_template.data_dir)

  # Build the pipeline to process one split
  return (
      pipeline
      | beam.Create(file_infos)
      | beam.Map(_process_shard, data_dir=data_dir, adapter=adapter)
      # Group everything in a single elem (_ShardInfo -> Sequence[_ShardInfo])
      | beam.GroupBy(lambda x: None)
      | beam.Values()
      | beam.Map(_merge_shard_info, filename_template=filename_template)
      | beam.Map(_split_info_to_json_str)
      | beam.io.WriteToText(
          os.fspath(out_dir / _out_filename(split_name)),
          num_shards=1,
          shard_name_template='',
      )
  )


def _process_shard(
    file_info: naming.FilenameInfo,
    *,
    data_dir: epath.Path,
    adapter: Type[file_adapters.FileAdapter],
) -> _ShardInfo:
  """Process a single shard."""
  # Load the ds
  ds = adapter.make_tf_data(data_dir / str(file_info))
  num_examples = 0
  bytes_size = 0
  for ex in ds:
    num_examples += 1
    bytes_size += len(ex._numpy())  # pylint: disable=protected-access
  return _ShardInfo(
      file_info=file_info,
      num_examples=num_examples,
      bytes_size=bytes_size,
  )


def _merge_shard_info(
    shard_infos: Sequence[_ShardInfo],
    filename_template: naming.ShardedFileTemplate,
) -> split_lib.SplitInfo:
  """Merge all shard info from one splits and returns the SplitInfo.

  Args:
    shard_infos: The shard infos from all shards.
    filename_template: filename template of the splits.

  Returns:
    The json SplitInfo proto
  """
  (split_name,) = {s.file_info.split for s in shard_infos}
  shard_infos = sorted(shard_infos, key=lambda s: s.file_info.shard_index)
  filename_template = filename_template.replace(split=split_name)
  return split_lib.SplitInfo(
      name=split_name,
      shard_lengths=[s.num_examples for s in shard_infos],
      num_bytes=sum(s.bytes_size for s in shard_infos),
      filename_template=filename_template,
  )


def _split_info_to_json_str(split_info: split_lib.SplitInfo) -> str:
  proto = split_info.to_proto()
  return json_format.MessageToJson(proto, sort_keys=True)


def _out_filename(split_name: str) -> str:
  return f'{split_name}-info.json'


def _split_info_from_path(
    filename_template: naming.ShardedFileTemplate,
) -> split_lib.SplitInfo:
  """Load the split info from the path."""
  path = filename_template.data_dir / _out_filename(filename_template.split)
  json_str = path.read_text()
  proto = json_format.Parse(json_str, dataset_info_pb2.SplitInfo())
  return split_lib.SplitInfo.from_proto(
      proto, filename_template=filename_template.replace(split=proto.name)
  )


def split_infos_from_path(
    split_names: Sequence[str],
    filename_template: naming.ShardedFileTemplate,
) -> Sequence[split_lib.SplitInfo]:
  """Restore the split info from a directory."""
  return [
      _split_info_from_path(
          filename_template=filename_template.replace(split=split_name)
      )
      for split_name in split_names
  ]
