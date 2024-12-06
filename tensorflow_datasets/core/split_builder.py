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

"""Dataset generator code."""

from collections.abc import Iterable, Iterator, Sequence
import contextlib
import dataclasses
import functools
import itertools
import json
import sys
from typing import Any, Callable, Optional, Union

from absl import logging
from etils import epath
from etils import epy
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import psutil

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from tensorflow_datasets.core import example_serializer
  from tensorflow_datasets.core import features as features_lib
  from tensorflow_datasets.core import file_adapters
  from tensorflow_datasets.core import naming
  from tensorflow_datasets.core import splits as splits_lib
  from tensorflow_datasets.core import utils
  from tensorflow_datasets.core import writer as writer_lib
  from tensorflow_datasets.core.utils import shard_utils

  # pylint: enable=g-import-not-at-top


# Example key used for shuffling
Key = str | int
# The nested example dict passed to `features.encode_example`
Example = dict[str, Any]
KeyExample = tuple[Key, Example]

# Possible values returned by `GeneratorBasedBuilder._split_generators`
SplitGenerator = Union[
    Iterable[KeyExample],
    # Ideally we should add input/output type annotations
    # `beam.PTransform[[], KeyExample]`, similar to `Callable[[], KeyExample]`
    'beam.PTransform',
    'beam.PCollection[KeyExample]',
]
ExampleGeneratorFn = Callable[[], Iterator[KeyExample]]


@utils.docs.deprecated
@dataclasses.dataclass
class SplitGeneratorLegacy:
  """Defines the split information for the generator.

  DEPRECATED: `_split_generators` should return `dict<split_name, generators>`
  instead. See the
  [documentation](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/GeneratorBasedBuilder).

  Attributes:
    name: `str`, name of the Split for which the generator will create the
      examples.
    gen_kwargs: `dict`, kwargs to forward to the _generate_examples() method of
      the builder.
  """

  name: str
  gen_kwargs: dict[str, Any] | None = dataclasses.field(default_factory=dict)


class _SplitInfoFuture:
  """Future containing the `tfds.core.SplitInfo` result."""

  def __init__(self, callback: Callable[[], splits_lib.SplitInfo]):
    self._callback = callback

  def result(self) -> splits_lib.SplitInfo:
    return self._callback()


@dataclasses.dataclass
class PipelineProxy:
  """Proxy which allows access to beam.Pipeline result after completion.

  This is yielded by the maybe_beam_pipeline() context and can only be used if
  beam is used to generate the dataset.
  """

  _beam_pipeline: Optional['beam.Pipeline']

  @property
  def result(self):
    return self._beam_pipeline.result if self._beam_pipeline else None


class SplitBuilder:
  """Util class to build splits.

  Usage is as follow:

  ```py
  split_builder = SplitBuilder(...)

  with split_builder.maybe_beam_pipeline():
    split_info_future = split_builder.submit_split_generation(...)

  split_info = split_info_future.result()
  ```

  * submit_split_generation:
    * For generator based split: Generate the split
    * For Apache Beam based split: Create the `beam.PCollection` and returns
      a future.
  * `split_info_future.result()`: Called after all `beam.PCollection`s have
    finished. Finalize the `split_info` by collecting all pipeline results.

  `submit_split_generation` / `.result` should be called once per
  split.
  """

  def __init__(
      self,
      *,
      split_dict: splits_lib.SplitDict,  # Used for precomputed nb of examples
      features: features_lib.FeatureConnector,
      dataset_size: utils.Size,
      beam_options: Optional['beam.options.pipeline_options.PipelineOptions'],
      beam_runner: Optional['beam.runners.PipelineRunner'],
      max_examples_per_split: int | None,
      example_writer: writer_lib.ExampleWriter,
      shard_config: shard_utils.ShardConfig | None = None,
      ignore_duplicates: bool = False,
  ):
    self._split_dict = split_dict
    self._features = features
    self._dataset_size = dataset_size
    self._max_examples_per_split = max_examples_per_split

    self._in_contextmanager: bool = False
    self._beam_options = beam_options
    self._beam_runner = beam_runner
    self._beam_pipeline: Optional['beam.Pipeline'] = None
    self._shard_config = shard_config
    self._ignore_duplicates = ignore_duplicates
    self._example_writer = example_writer

  def submit_shard_based_generation(
      self,
      split_name: str,
      filename_template: naming.ShardedFileTemplate,
      example_gen_per_shard: Sequence[ExampleGeneratorFn],
  ) -> _SplitInfoFuture:
    """Creates the shards for the split with the given example generators.

    If a Beam runner was added when initializing the `SplitBuilder`, then
    the `example_gen_per_shard` will be run in parallel using Beam. Otherwise,
    they will be run sequentially in the current process.

    Args:
      split_name: Name of the split to generate
      filename_template: Template to format the filename for a shard.
      example_gen_per_shard: List of example generators, one per shard. Must be
        in the same order as the shards.

    Returns:
      a future with the split info.
    """
    num_shards = len(example_gen_per_shard)
    filename_template = filename_template.replace(split=split_name)
    serialized_info = self._features.get_serialized_info()
    serializer = example_serializer.ExampleSerializer(serialized_info)

    shard_writer = writer_lib.ShardWriter(
        serializer=serializer,
        example_writer=self._example_writer,
    )

    shard_paths = []
    shard_lengths = []
    if self._beam_runner is None:
      for shard_index, example_gen in enumerate(example_gen_per_shard):
        shard_path = filename_template.sharded_filepath(
            shard_index=shard_index, num_shards=num_shards
        )
        shard_paths.append(shard_path)
        num_examples = shard_writer.write(
            path=shard_path, examples=example_gen()
        )
        shard_lengths.append(num_examples)
    else:
      # To store the shard information temporarily, we use the same path as the
      # data shard paths, minus the shard suffix (e.g., 00000-of-00042), with
      # the suffix `.shard_infos.json`.
      shard_infos_path = epath.Path(
          f'{filename_template.filepath_prefix()}.shard_infos.json'
      )
      with self.maybe_beam_pipeline():
        shard_infos = []
        for shard_index, example_gen in enumerate(example_gen_per_shard):
          shard_path = filename_template.sharded_filepath(
              shard_index=shard_index, num_shards=num_shards
          )
          shard_paths.append(shard_path)
          shard_info = shard_writer.write_with_beam(
              path=shard_path,
              example_gen=example_gen,
              shard_index=shard_index,
              pipeline=self.beam_pipeline,
          )
          shard_infos.append(shard_info)

        def write_shard_infos(
            shard_infos: list[tuple[int, int]], path: epath.Path
        ) -> None:
          shard_infos_dict = {index: length for index, length in shard_infos}
          path.write_text(json.dumps(shard_infos_dict))

        _ = (
            shard_infos
            | f'FlattenShardInfos_{split_name}' >> beam.Flatten()
            | f'CombineShardInfos_{split_name}'
            >> beam.CombineGlobally(beam.combiners.ToListCombineFn())
            | f'WriteShardInfos_{split_name}'
            >> beam.Map(write_shard_infos, path=shard_infos_path)
        )

      shard_infos_dict = json.loads(shard_infos_path.read_text())
      shard_lengths = [
          num_examples for _, num_examples in sorted(shard_infos_dict.items())
      ]

    total_size = sum([shard_path.stat().length for shard_path in shard_paths])

    split_info = splits_lib.SplitInfo(
        name=split_name,
        shard_lengths=shard_lengths,
        num_bytes=total_size,
        filename_template=filename_template,
    )
    return _SplitInfoFuture(lambda: split_info)

  @contextlib.contextmanager
  def maybe_beam_pipeline(self) -> Iterator[PipelineProxy]:
    """Context manager wrapping the beam pipeline.

    If Apache Beam is used, then the pipeline created withing the contextmanager
    will be launched when exiting the context manager:

    ```py
    with split_builder.maybe_beam_pipeline():
      pcollection = (
          split_builder.beam_pipeline
          | beam.Create()
          | beam.Map()
      )
    ```

    Is equivalent to:

    ```py
    with beam.Pipeline() as beam_pipeline:
      pcollection = (
          beam_pipeline
          | beam.Create()
          | beam.Map()
      )
    ```

    If `split_builder.beam_pipeline` is never called, then `beam.Pipeline` is
    never created and this function is a no-op.

    Yields:
      PipelineProxy containing a reference to the beam pipeline, allowing access
        to the pipeline result for (e.g) logging metrics to file.
    """
    self._in_contextmanager = True
    try:
      # Entering the contextmanager is a no-op. Only if Apache Beam is used
      # is the `beam.Pipeline` contextmanager activated.
      # Construct pipeline proxy with a placeholder beam pipeline.
      pipeline_proxy = PipelineProxy(_beam_pipeline=None)
      yield pipeline_proxy
    except Exception:  # pylint: disable=broad-except
      # Close and forward the exception
      if not self._beam_pipeline or not self._beam_pipeline.__exit__(
          *sys.exc_info()
      ):
        raise  # Forward the exception
    else:
      # If the Beam pipeline was used, then exit it.
      if self._beam_pipeline is not None:
        self._beam_pipeline.__exit__(None, None, None)
        # Fill in the beam pipeline in the proxy.
        pipeline_proxy._beam_pipeline = self._beam_pipeline  # pylint:disable=protected-access
    self._in_contextmanager = False

  @functools.cached_property
  def beam_pipeline(self) -> 'beam.Pipeline':
    """Instanciates and returns Apache Beam pipeline.

    Calling this function starts the Apache Beam mode.

    Returns:
      pipeline: The beam pipeline
    """
    if not self._in_contextmanager:
      raise AssertionError(
          'beam_pipeline has to be created from within `SplitBuilder` '
          'contextmanager.'
      )

    # On Colab, stderr isn't displayed by default, so using `print`.
    print_fn = print if utils.is_notebook() else logging.warning
    if not self._beam_runner and not self._beam_options:
      msg = utils.dedent("""
          **************************** WARNING *********************************
          Warning: The dataset you're trying to generate is using Apache Beam,
          yet no `beam_runner` nor `beam_options` was explicitly provided.

          Some Beam datasets take weeks to generate, so are usually not suited
          for single machine generation. Please have a look at the instructions
          to setup distributed generation:

          https://www.tensorflow.org/datasets/beam_datasets#generating_a_beam_dataset
          **********************************************************************
          """)
      print_fn(msg)

      total_memory = psutil.virtual_memory().total
      if self._dataset_size >= total_memory:
        value = input(
            (
                f'The dataset is {self._dataset_size} in size, but your machine'
                f' has only {utils.Size(total_memory)} of memory. Continue?'
                '[Y/n] > '
            ),
        )
        if value.lower() in ('n', 'no'):
          sys.exit(1)

    beam_options = (
        self._beam_options or beam.options.pipeline_options.PipelineOptions()
    )
    # Beam type checking assumes transforms multiple outputs are of same type,
    # which is not our case. Plus it doesn't handle correctly all types, so we
    # are better without it.
    beam_options.view_as(
        beam.options.pipeline_options.TypeOptions
    ).pipeline_type_check = False
    # Create the global pipeline object common for all splits
    pipeline = beam.Pipeline(runner=self._beam_runner, options=beam_options)
    self._beam_pipeline = pipeline.__enter__()
    return self._beam_pipeline

  def normalize_legacy_split_generators(
      self,
      split_generators: dict[str, SplitGenerator] | list[SplitGeneratorLegacy],
      generator_fn: Callable[..., Any],
      is_beam: bool,
  ) -> dict[str, SplitGenerator]:
    """Normalize legacy split API into new dict[split_name, generator].

    This function convert the legacy `list[tfds.core.SplitGenerator]` into
    the new `{'split_name': generator}` structure.

    Could be removed if all datasets were updated.

    Args:
      split_generators: Either legacy or new split_generators
      generator_fn: The `GeneratorBasedBuilder._generate_examples` function.
      is_beam: `True` if using legacy `tfds.core.BeamBasedBuilder`

    Returns:
      split_generators: New split generator structure.
    """
    if isinstance(split_generators, dict):  # New structure
      return split_generators
    if isinstance(split_generators, list):  # Legacy structure
      if is_beam:  # Legacy `tfds.core.BeamBasedBuilder`
        generator_fn = beam.ptransform_fn(generator_fn)
        return {
            s.name: generator_fn(**s.gen_kwargs)  # Create the `beam.PTransform`
            for s in split_generators
        }
      else:
        return {
            split_generator.name: generator_fn(**split_generator.gen_kwargs)
            for split_generator in split_generators
        }
    else:
      raise TypeError(
          f'Invalid `_split_generators` returned value: {split_generators}'
      )

  def submit_split_generation(
      self,
      split_name: str,
      generator: SplitGenerator,
      filename_template: naming.ShardedFileTemplate,
      disable_shuffling: bool,
      nondeterministic_order: bool,
  ) -> _SplitInfoFuture:
    """Start the split generation.

    Args:
      split_name: Name of the split to generate.
      generator: Generator, beam.PTransform,... yielding the examples.
      filename_template: Template to format the filename for a shard.
      disable_shuffling: Specifies whether to shuffle the examples.
      nondeterministic_order: If True, it will not assure deterministic ordering
        when writing' examples to disk. This might result in quicker dataset
        preparation

    Returns:
      split_info_future: Future containing the `split_info`, once generation
        is complete. The `tfds.core.SplitInfo` can be accessed through
        `split_info_future.result()`
    """
    build_kwargs = dict(
        split_name=split_name,
        generator=generator,
        filename_template=filename_template,
        disable_shuffling=disable_shuffling,
    )
    # Depending on the type of generator, we use the corresponding
    # `_build_from_xyz` method.
    if isinstance(generator, Iterable):
      if nondeterministic_order:
        logging.warning(
            '`nondeterministic_order` is set to True for a dataset that does'
            ' not use beam. Setting `disable_shuffling` to True.'
        )
        build_kwargs['disable_shuffling'] = True
      return self._build_from_generator(**build_kwargs)
    else:  # Otherwise, beam required
      unknown_generator_type = TypeError(
          f'Invalid split generator value for split `{split_name}`. '
          'Expected generator or apache_beam object. Got: '
          f'{type(generator)}'
      )
      build_kwargs['nondeterministic_order'] = nondeterministic_order
      if isinstance(generator, beam.PTransform):
        # Generate the beam.PCollection
        pcollection = self.beam_pipeline | split_name >> generator
        build_kwargs['generator'] = pcollection
        return self._build_from_pcollection(**build_kwargs)
      elif isinstance(generator, beam.PCollection):
        return self._build_from_pcollection(**build_kwargs)
      else:
        raise unknown_generator_type

  def _build_from_generator(
      self,
      split_name: str,
      generator: Iterable[KeyExample],
      filename_template: naming.ShardedFileTemplate,
      disable_shuffling: bool,
  ) -> _SplitInfoFuture:
    """Split generator for example generators.

    Args:
      split_name: str,
      generator: Iterable[KeyExample],
      filename_template: Template to format the filename for a shard.
      disable_shuffling: Specifies whether to shuffle the examples,

    Returns:
      future: The future containing the `tfds.core.SplitInfo`.
    """
    if self._max_examples_per_split is not None:
      logging.warning(
          'Splits capped at %s examples max.', self._max_examples_per_split
      )
      generator = itertools.islice(generator, self._max_examples_per_split)
      total_num_examples = self._max_examples_per_split
    else:
      # If dataset info has been pre-downloaded from the internet,
      # we can use the pre-computed number of example for the progression bar.
      split_info = self._split_dict.get(split_name)
      if split_info and split_info.num_examples:
        total_num_examples = split_info.num_examples
      else:
        total_num_examples = None

    serialized_info = self._features.get_serialized_info()
    writer = writer_lib.Writer(
        serializer=example_serializer.ExampleSerializer(serialized_info),
        filename_template=filename_template,
        hash_salt=split_name,
        disable_shuffling=disable_shuffling,
        shard_config=self._shard_config,
        example_writer=self._example_writer,
        ignore_duplicates=self._ignore_duplicates,
    )
    for i, (key, example) in enumerate(
        utils.tqdm(
            generator,
            desc=f'Generating {split_name} examples...',
            unit=' examples',
            total=total_num_examples,
            leave=False,
            mininterval=1.0,
        )
    ):
      try:
        example = self._features.encode_example(example)
      except Exception as e:  # pylint: disable=broad-except
        utils.reraise(e, prefix=f'Failed to encode example:\n{example}\n')
      if disable_shuffling and not isinstance(key, int):
        # If `disable_shuffling` is set to True, the key must be an integer.
        key = i
      writer.write(key, example)
    try:
      shard_lengths, total_size = writer.finalize()
    except Exception as e:  # pylint: disable=broad-except
      utils.reraise(
          e, prefix=f'Failed to finalize writing of split "{split_name}": '
      )

    split_info = splits_lib.SplitInfo(
        name=split_name,
        shard_lengths=shard_lengths,
        num_bytes=total_size,
        filename_template=filename_template,
    )
    return _SplitInfoFuture(lambda: split_info)

  def _build_from_pcollection(
      self,
      split_name: str,
      generator: 'beam.PCollection[KeyExample]',
      filename_template: naming.ShardedFileTemplate,
      disable_shuffling: bool,
      nondeterministic_order: bool,
  ) -> _SplitInfoFuture:
    """Split generator for `beam.PCollection`."""
    # TODO(tfds): Should try to add support to `max_examples_per_split`
    serializer = example_serializer.ExampleSerializer(
        self._features.get_serialized_info()
    )
    if nondeterministic_order:
      logging.info(
          '`nondeterministic_order` is set to True, using NoShuffleBeamWriter'
      )
      num_shards = self._shard_config.num_shards if self._shard_config else None
      beam_writer = writer_lib.NoShuffleBeamWriter(
          serializer=serializer,
          file_format=file_adapters.FileFormat.from_value(
              filename_template.filetype_suffix
          ),
          filename_template=filename_template,
          num_shards=num_shards,
      )
    else:
      logging.info('Deterministic ordering is enabled, using BeamWriter')
      beam_writer = writer_lib.BeamWriter(
          serializer=serializer,
          filename_template=filename_template,
          hash_salt=split_name,
          disable_shuffling=disable_shuffling,
          shard_config=self._shard_config,
          example_writer=self._example_writer,
          ignore_duplicates=self._ignore_duplicates,
      )

    def _encode_example(key_ex, encode_fn=self._features.encode_example):
      # We do not access self._features in this function to avoid pickling the
      # entire class.
      return key_ex[0], encode_fn(key_ex[1])

    # Note: We need to wrap the pipeline in a PTransform to avoid
    # errors due to duplicated ``>> beam_labels`
    @beam.ptransform_fn
    def _encode_pcollection(pipeline):
      """PTransformation which build a single split."""
      pcoll_examples = pipeline | 'Encode' >> beam.Map(_encode_example)
      return beam_writer.write_from_pcollection(pcoll_examples)

    # Add the PCollection to the pipeline
    _ = generator | f'{split_name}_write' >> _encode_pcollection()  # pylint: disable=no-value-for-parameter

    def _resolve_future():
      if self._in_contextmanager:
        raise AssertionError(
            '`future.result()` should be called after the '
            '`maybe_beam_pipeline` contextmanager.'
        )
      logging.info('Retrieving split info for %s...', split_name)
      shard_lengths, total_size = beam_writer.finalize()
      return splits_lib.SplitInfo(
          name=split_name,
          shard_lengths=shard_lengths,
          num_bytes=total_size,
          filename_template=filename_template,
      )

    return _SplitInfoFuture(_resolve_future)
