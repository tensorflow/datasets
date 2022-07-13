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

r"""Script to clean up old generated datasets.

The script will display the datasets to delete and will ask users for
confirmation.

Instructions:

python -m tensorflow_datasets.scripts.cleanup.delete_old_versions
    --data_dir=/path/to/data_dir/ --skip_confirmation=False

"""

import collections
import concurrent.futures
import dataclasses
import os
import pathlib
from typing import Dict, Iterable, List, Tuple

from absl import app
from absl import flags
import tensorflow as tf
import tensorflow_datasets as tfds
import termcolor

FLAGS = flags.FLAGS

flags.DEFINE_string('data_dir', tfds.core.constants.DATA_DIR,
                    'Path to the data directory.')
flags.DEFINE_boolean('skip_confirmation', False,
                     'Whether to skip user confirmation or not.')

# Nested dict representing the file structure.
TreeDict = Dict[str, 'TreeDict']  # pytype: disable=not-supported-yet

# Folder in this lists are never deleted
DIRS_TO_KEEP = frozenset({'downloads', 'download', 'manual', 'extracted'})


def _tree_dict() -> TreeDict:
  """Nested dict."""
  return collections.defaultdict(_tree_dict)


def _split_full_names(full_names: List[str]) -> TreeDict:
  """Split the list of full names into a tree of nested dict."""
  root_tree = _tree_dict()
  for full_name in full_names:
    tree = root_tree
    for part in full_name.split('/'):
      tree = tree[part]  # `ds/config/version` -> tree[ds][config][version]
  return root_tree


@dataclasses.dataclass
class TaskResult:
  """Structure containing the tasks result.

  Attributes:
    to_keep: List of directories to keep
    to_delete: List of directories to delete
    sub_tasks: Childs tasks
  """
  to_keep: Iterable[pathlib.Path]
  to_delete: Iterable[pathlib.Path]
  sub_tasks: Iterable[concurrent.futures.Future]


def _extract_dirs_to_delete(
    executor: concurrent.futures.ThreadPoolExecutor,
    curr_dir: pathlib.Path,
    curr_tree: TreeDict,
) -> TaskResult:
  """Tasks which compute the directories to keep and delete.

  This recursively computes `listdir()` on the `curr_dir`, and compares with
  `curr_tree` to check which directory to delete. Recursion is done on the
  remaining sub-directory (cleanup `data_dir/...`, then `data_dir/mnist/...`,
  ...)

  Args:
    executor: Executor to launch subtasks
    curr_dir: Current directory to explore
    curr_tree: Current tree containing the name of folders to keep

  Returns:
    The dataclass containing files to keep, delete and sub-tasks
  """
  # End recursion with tree leafs (`.../1.2.0/`)
  if not curr_tree:
    return TaskResult(
        to_keep=[curr_dir],
        to_delete=[],
        sub_tasks=[],
    )

  # Compute the list of dirs to keep and delete.
  all_files = set(tf.io.gfile.listdir(str(curr_dir)))
  all_dirs_to_keep = set(curr_tree)
  dirs_to_delete = all_files - all_dirs_to_keep - DIRS_TO_KEEP
  dirs_to_maybe_keep = all_files & all_dirs_to_keep

  # Recurse on sub-dirs (e.g. `ds/config/`), add the dirs to the task queue.
  sub_tasks = [
      executor.submit(  # pylint: disable=g-complex-comprehension
          _extract_dirs_to_delete,
          executor=executor,
          curr_dir=curr_dir / dir_name,
          curr_tree=curr_tree[dir_name],
      ) for dir_name in dirs_to_maybe_keep
  ]
  return TaskResult(
      to_keep=[],
      to_delete=[curr_dir / d for d in dirs_to_delete],
      sub_tasks=sub_tasks,
  )


def _extract_dirs_from_future(
    dirs_to_keep: List[pathlib.Path],
    dirs_to_delete: List[pathlib.Path],
    future: concurrent.futures.Future,
) -> None:
  """Merge all results from all subtasks."""
  task_result = future.result()
  dirs_to_keep.extend(task_result.to_keep)
  dirs_to_delete.extend(task_result.to_delete)
  for sub_task in task_result.sub_tasks:
    _extract_dirs_from_future(
        dirs_to_keep=dirs_to_keep,
        dirs_to_delete=dirs_to_delete,
        future=sub_task,
    )


def _get_extra_dirs(
    data_dir: pathlib.Path,
    current_full_names: List[str],
) -> Tuple[List[pathlib.Path], List[pathlib.Path]]:
  """Returns a tuple of installed datasets and extra dirs to delete.

  Args:
      data_dir : The path to the data directory
      current_full_names : Names of the latest datasets supported in TFDS

  Returns:
    dirs_to_keep: List of directory to keep (existing supported versions)
    dirs_to_delete: List of directory to delete
  """
  # Normalize paths for windows
  current_full_names = [os.path.normpath(name) for name in current_full_names]

  full_names_tree = _split_full_names(current_full_names)

  # Parse all existing dirs.
  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future = executor.submit(
        _extract_dirs_to_delete,
        executor=executor,
        curr_dir=data_dir,
        curr_tree=full_names_tree,
    )

    dirs_to_keep = []
    dirs_to_delete = []
    _extract_dirs_from_future(
        dirs_to_keep=dirs_to_keep, dirs_to_delete=dirs_to_delete, future=future)
  return sorted(dirs_to_keep), sorted(dirs_to_delete)


def _display_dirs(
    data_dir: pathlib.Path,
    dirs_to_keep: List[pathlib.Path],
    dirs_to_delete: List[pathlib.Path],
) -> None:
  """Display dirs to keep and delete."""
  dirs_to_keep = set(dirs_to_keep)
  dirs_to_delete = set(dirs_to_delete)

  # Format dirs to strip prefix and keep in bold.
  def _format(d, keep: bool):
    d = str(d.relative_to(data_dir))
    if keep:
      d = termcolor.colored(f'{d} (*)', attrs=['bold'])
    return d

  all_dirs = [
      _format(d, keep=d in dirs_to_keep)
      for d in sorted(dirs_to_keep | dirs_to_delete)
  ]
  # Preview the dirs to delete
  print(f'The script will delete the following modifications to `{data_dir}`:')
  print('Path indicated in bold (*) will be kept, the other will be deleted.\n')
  print('\n'.join(all_dirs))
  print()
  print(f'{len(dirs_to_delete)} datasets to delete, {len(dirs_to_keep)} to '
        'keep.\n')


def delete_old_versions(
    data_dir: pathlib.Path,
    skip_confirmation: bool = False,
) -> None:
  """Detects and deletes all datasets which are not in supported version."""
  # Extract the list of directory to keep and delete.
  dirs_to_keep, dirs_to_delete = _get_extra_dirs(
      data_dir=data_dir,
      # Explicitly set predicate_fn to None to load all datasets
      current_full_names=tfds.core.load.list_full_names(),
  )

  _display_dirs(
      data_dir=data_dir,
      dirs_to_keep=dirs_to_keep,
      dirs_to_delete=dirs_to_delete,
  )

  if skip_confirmation:
    delete = True
  else:
    delete = str(input('Do you want to continue (Y/n): ')) in ('Y', 'y')
  if not delete:
    print('Exiting the program without change!')
    return

  for path in dirs_to_delete:
    print(f'Delete: {path}')
    tf.io.gfile.rmtree(str(path))
  print('Add directories have been deleted!')


def main(_):
  tfds.core.visibility.set_availables([
      tfds.core.visibility.DatasetType.TFDS_PUBLIC,
  ])
  delete_old_versions(
      data_dir=pathlib.Path(FLAGS.data_dir),
      skip_confirmation=FLAGS.skip_confirmation,
  )


if __name__ == '__main__':
  app.run(main)
