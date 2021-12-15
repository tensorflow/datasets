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

"""Tree utils."""

import concurrent.futures
import functools
from typing import Callable, TypeVar

import tensorflow as tf
from tensorflow_datasets.core.utils import tqdm_utils as tqdm
from tensorflow_datasets.core.utils import type_utils

Tree = type_utils.Tree
_Tin = TypeVar('_Tin')
_Tout = TypeVar('_Tout')


def parallel_map(
    map_fn: Callable[..., _Tout],  # Callable[[_Tin0, _Tin1,...], Tout]
    *trees: Tree[_Tin],  # _Tin0, _Tin1,...
    max_workers: int = 32,
    report_progress: bool = False,
) -> Tree[_Tout]:  # pytype: disable=invalid-annotation
  """Same as `tf.nest.map_structure` but apply map_fn in parallel.

  Args:
    map_fn: Worker function
    *trees: Nested input to pass to the `map_fn`
    max_workers: Number of workers
    report_progress: If True, display a progression bar.

  Returns:
    The nested structure after `map_fn` has been applied.
  """
  with concurrent.futures.ThreadPoolExecutor(
      max_workers=max_workers,) as executor:
    launch_worker = functools.partial(executor.submit, map_fn)
    futures = tf.nest.map_structure(launch_worker, *trees)

    leaves = tf.nest.flatten(futures)

    itr = concurrent.futures.as_completed(leaves)
    if report_progress:
      itr = tqdm.tqdm(itr, total=len(leaves))

    for f in itr:  # Propagate exception to main thread.
      if f.exception():
        raise f.exception()

  return tf.nest.map_structure(lambda f: f.result(), futures)
