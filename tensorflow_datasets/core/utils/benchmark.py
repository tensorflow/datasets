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

"""Benchmark utils."""
from __future__ import annotations

import dataclasses
import statistics
import textwrap
import time
from typing import Any, Dict, Iterable, List, Optional, Union

from absl import logging
from tensorflow_datasets.core.utils import tqdm_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import pandas as pd

# pylint: disable=logging-format-interpolation

StatDict = Dict[str, Union[int, float]]


def _ns_to_s(time_in_ns: int) -> float:
  return time_in_ns / 1e9


@dataclasses.dataclass(frozen=True)
class RawBenchmarkResult:
  """Raw results of running the benchmark.

  Attributes:
    num_iter: the number of iterations over examples that were done.
    num_examples: the number of examples that were processed in these
      iterations. Note that when examples are batched, then one iteration
      processes multiple examples.
    start_time: the time (in ns) at which when the benchmark started.
    first_batch_time: the time (in ns) at which the first iteration was
      processed.
    end_time: the time (in ns) at which the benchmark ended.
    batch_size: the number of examples in each iteration.
    durations_ns: the duration in ns of each iteration that was processed.
  """

  num_iter: int
  num_examples: int
  start_time: int
  first_batch_time: int
  end_time: int
  batch_size: int
  durations_ns: Optional[List[int]] = None

  def examples(self, include_first: bool = True) -> int:
    if include_first:
      return self.num_examples
    return self.num_examples - 1

  def total_time_s(self, include_first: bool = True) -> float:
    if include_first:
      return _ns_to_s(self.end_time - self.start_time)
    return _ns_to_s(self.end_time - self.first_batch_time)

  def examples_per_second(self, include_first: bool = True) -> float:
    return self.examples(include_first) / self.total_time_s(include_first)

  def time_until_first(self, include_first: bool = True) -> Optional[float]:
    """Time in seconds that it took to load the first example."""
    if include_first:
      return _ns_to_s(self.first_batch_time - self.start_time)
    if self.durations_ns is not None and len(self.durations_ns) > 1:
      return _ns_to_s(self.durations_ns[1])
    return None

  def durations_s(self, include_first: bool = True) -> List[float]:
    if not include_first:
      return [_ns_to_s(d) for d in self.durations_ns[1:]]
    return [_ns_to_s(d) for d in self.durations_ns]

  def summary_statistics(
      self, include_first: bool
  ) -> Dict[str, Union[float, List[float]]]:
    if self.durations_ns is None:
      return {}
    durations = self.durations_s(include_first)
    return {
        'mean': statistics.mean(durations),
        'variance': statistics.pvariance(durations),
        'stdev': statistics.stdev(durations),
        'quantiles': statistics.quantiles(durations),
    }

  def raw_stats_pd(self) -> pd.DataFrame:  # pytype: disable=invalid-annotation  # typed-pandas
    raw_stats = {
        'start_time': _ns_to_s(self.start_time),
        'first_batch_time': _ns_to_s(self.first_batch_time),
        'end_time': _ns_to_s(self.end_time),
        'num_iter': self.num_iter,
    }
    return pd.DataFrame.from_dict(
        raw_stats, orient='index', columns=['duration']
    )

  def stats(self) -> Dict[str, StatDict]:
    return {
        'first+lasts': _log_stats(
            'First included',
            self.start_time,
            self.end_time,
            self.num_examples + self.batch_size,
        ),
        'first': _log_stats(
            'First only',
            self.start_time,
            self.first_batch_time,
            self.batch_size,
        ),
        'lasts': _log_stats(
            'First excluded',
            self.first_batch_time,
            self.end_time,
            self.num_examples,
        ),
    }

  def stats_pd(self) -> pd.DataFrame:  # pytype: disable=invalid-annotation  # typed-pandas
    return pd.DataFrame.from_dict(self.stats(), orient='index')

  def __repr__(self) -> str:
    return textwrap.dedent(
        f"""
      BenchmarkResult(
        num_iter = {self.num_iter}
        num_examples = {self.num_examples}
        batch_size = {self.batch_size}
        examples / sec = {self.examples_per_second()}
        duration: {self.summary_statistics(include_first=True)}
        duration without first: {self.summary_statistics(include_first=False)}
      )"""
    )


@dataclasses.dataclass(frozen=True)
class BenchmarkResult:
  stats: pd.DataFrame  # pytype: disable=invalid-annotation  # typed-pandas
  raw_stats: pd.DataFrame  # pytype: disable=invalid-annotation  # typed-pandas

  def _repr_html_(self) -> str:
    """Colab/notebook representation."""
    return '<strong>BenchmarkResult:</strong><br/>' + self.stats._repr_html_()  # pylint: disable=protected-access


def raw_benchmark(
    ds: Iterable[Any],
    *,
    num_iter: Optional[int] = None,
    batch_size: int = 1,
    detailed_stats: bool = False,
) -> RawBenchmarkResult:
  """Benchmarks any iterable (e.g `tf.data.Dataset`).

  Usage:

  ```py
  ds = tfds.load('mnist', split='train')
  ds = ds.batch(32).prefetch(buffer_size=tf.data.AUTOTUNE)
  tfds.benchmark(ds, batch_size=32)
  ```

  Args:
    ds: Dataset to benchmark. Can be any iterable. Note: The iterable will be
      fully consumed.
    num_iter: Number of iteration to perform (iteration might be batched)
    batch_size: Batch size of the dataset, used to normalize iterations
    detailed_stats: Whether to collect detailed statistics such as the time that
      each iteration took.

  Returns:
    raw results.
  """
  try:
    total = len(ds)  # pytype: disable=wrong-arg-types
  except TypeError:
    total = num_iter

  if num_iter is not None:
    total = min(total, num_iter)

  results = []
  actual_num_iter = 0
  first_batch_time = None
  start_time = time.perf_counter_ns()
  end_time = start_time
  for _ in tqdm_utils.tqdm(iter(ds), total=total):
    actual_num_iter += 1
    end_time = time.perf_counter_ns()
    if first_batch_time is None:
      first_batch_time = end_time
    if detailed_stats:
      results.append(end_time)
    if num_iter and actual_num_iter >= num_iter:
      break
  if not actual_num_iter:
    raise ValueError('Cannot benchmark dataset with 0 elements.')

  if num_iter and actual_num_iter < num_iter:
    logging.warning(
        'Number of iterations is shorter than expected ({} vs {})'.format(
            actual_num_iter, num_iter
        )
    )

  durations_ns = []
  for i in range(len(results)):
    if i == 0:
      durations_ns.append(results[i] - start_time)
    else:
      durations_ns.append(results[i] - results[i - 1])

  return RawBenchmarkResult(
      num_iter=actual_num_iter,
      num_examples=actual_num_iter * batch_size,
      start_time=start_time,
      first_batch_time=first_batch_time,
      end_time=end_time,
      batch_size=batch_size,
      durations_ns=durations_ns,
  )


def benchmark(
    ds: Iterable[Any],
    *,
    num_iter: Optional[int] = None,
    batch_size: int = 1,
) -> BenchmarkResult:
  """Benchmarks any iterable (e.g `tf.data.Dataset`).

  Usage:

  ```py
  ds = tfds.load('mnist', split='train')
  ds = ds.batch(32).prefetch(buffer_size=tf.data.AUTOTUNE)
  tfds.benchmark(ds, batch_size=32)
  ```

  Reports:

  - Total execution time
  - Setup time (first warmup batch)
  - Number of examples/sec

  Args:
    ds: Dataset to benchmark. Can be any iterable. Note: The iterable will be
      fully consumed.
    num_iter: Number of iteration to perform (iteration might be batched)
    batch_size: Batch size of the dataset, used to normalize iterations

  Returns:
    statistics: The recorded statistics, for eventual post-processing
  """
  print('\n************ Summary ************\n')
  raw_results = raw_benchmark(ds=ds, num_iter=num_iter, batch_size=batch_size)
  return BenchmarkResult(
      stats=raw_results.stats_pd(),
      raw_stats=raw_results.raw_stats_pd(),
  )


def _log_stats(msg: str, start: int, end: int, num_examples: int) -> StatDict:
  """Log and returns stats."""
  if not num_examples:
    stats = {
        'duration': 0.0,
        'num_examples': 0,
        'avg': 0.0,
    }
  else:
    # Make sure the total time is not 0.
    total_time_ns = (end - start) or 1
    total_time_s = _ns_to_s(total_time_ns)
    stats = {
        'duration': total_time_s,
        'num_examples': num_examples,
        'avg': num_examples / total_time_s,
    }
  print(
      'Examples/sec ({}) {avg:.2f} ex/sec (total: {num_examples} ex, '
      '{duration:.2f} sec)'.format(msg, **stats)
  )
  return stats
