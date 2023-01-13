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

"""Templates to generate dataset builders.

Depending on the given format, it will generate code to add format-specific
dataset builders to tfds.
"""
import textwrap

from tensorflow_datasets.scripts.cli import cli_utils

# Names of dataset builders.
STANDARD = 'standard'
CONLL = 'conll'
CONLLU = 'conllu'


def create_builder_template(info: cli_utils.DatasetInfo):
  """Calls the required (possibly format-specific) dataset builder template.

  Args:
    info: `cli_utils.DatasetInfo` object containing all information about the
      dataset necessary to generate a template for the new dataset.

  Returns:
    A string containing the builder-specific template for the new dataset, to be
    filled by the user.
  """
  if info.data_format == STANDARD:
    return _standard_template(info)
  elif info.data_format == CONLL:
    return _conll_template(info)
  elif info.data_format == CONLLU:
    return _conllu_template(info)
  else:
    raise ValueError(
        f"Required format {info.data_format} isn't associated with "
        'a format-specific builder in TFDS.'
    )


def _standard_template(info: cli_utils.DatasetInfo) -> str:
  """Returns a template for a `tfds.core.GeneratorBasedBuilder`."""
  content = textwrap.dedent(
      f'''\
      """{info.name} dataset."""

      import {info.tfds_api} as tfds


      class Builder(tfds.core.GeneratorBasedBuilder):
        """DatasetBuilder for {info.name} dataset."""

        VERSION = tfds.core.Version('1.0.0')
        RELEASE_NOTES = {{
            '1.0.0': 'Initial release.',
        }}

        def _info(self) -> tfds.core.DatasetInfo:
          """Returns the dataset metadata."""
          # {info.todo}: Specifies the tfds.core.DatasetInfo object
          return self.dataset_info_from_configs(
              features=tfds.features.FeaturesDict({{
                  # These are the features of your dataset like images, labels ...
                  'image': tfds.features.Image(shape=(None, None, 3)),
                  'label': tfds.features.ClassLabel(names=['no', 'yes']),
              }}),
              # If there's a common (input, target) tuple from the
              # features, specify them here. They'll be used if
              # `as_supervised=True` in `builder.as_dataset`.
              supervised_keys=('image', 'label'),  # Set to `None` to disable
              homepage='https://dataset-homepage/',
          )

        def _split_generators(self, dl_manager: tfds.download.DownloadManager):
          """Returns SplitGenerators."""
          # {info.todo}: Downloads the data and defines the splits
          path = dl_manager.download_and_extract('https://todo-data-url')

          # {info.todo}: Returns the Dict[split names, Iterator[Key, Example]]
          return {{
              'train': self._generate_examples(path / 'train_imgs'),
          }}

        def _generate_examples(self, path):
          """Yields examples."""
          # {info.todo}: Yields (key, example) tuples from the dataset
          for f in path.glob('*.jpeg'):
            yield 'key', {{
                'image': f,
                'label': 'yes',
            }}
      '''
  )
  return content


def _conll_template(info: cli_utils.DatasetInfo) -> str:
  """A template for ConllDatasetBuilder."""

  content = textwrap.dedent(
      f'''\
      """{info.name} dataset."""

      from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder_utils as conll_lib
      import {info.tfds_api} as tfds


      class {info.cls_name}(tfds.dataset_builders.ConllDatasetBuilder):
        """DatasetBuilder for {info.name} dataset."""

        VERSION = tfds.core.Version('1.0.0')
        RELEASE_NOTES = {{
            '1.0.0': 'Initial release.',
        }}
        # {info.todo}: Add details about the dataset's features.
        # conll_lib contains a set of ready-to-use features.
        BUILDER_CONFIGS = [conll_lib.CONLL_2003_CONFIG]

        def _info(self) -> tfds.core.DatasetInfo:
          """Returns the dataset metadata."""
          # {info.todo}: Specifies the dataset infos.
          return self.create_dataset_info(
            homepage="",
          )

        def _split_generators(self, dl_manager: tfds.download.DownloadManager):
          """Returns SplitGenerators."""
          # {info.todo}: Downloads the data and defines the splits
          path = dl_manager.download_and_extract('https://todo-data-url')

          return {{
            'train': self._generate_examples(path / 'train.txt',)
          }}

        # {info.todo}: If you need a customized _generate_examples function,
        # comment out the following.
        # def _generate_examples(
        #     self,
        #     path: Union[epath.PathLike, List[epath.PathLike]],
        #   ):
        #   """Yields (key, example) examples."""
        #   pass
      '''
  )
  return content


def _conllu_template(info: cli_utils.DatasetInfo) -> str:
  """A template for ConllUDatasetBuilder."""

  content = textwrap.dedent(
      f'''\
      """{info.name} dataset."""

      from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib
      import {info.tfds_api} as tfds


      class {info.cls_name}(tfds.dataset_builders.ConllUDatasetBuilder):
        """DatasetBuilder for {info.name} dataset."""

        VERSION = tfds.core.Version('1.0.0')
        RELEASE_NOTES = {{
            '1.0.0': 'Initial release.',
        }}
        # {info.todo}: Add details about the dataset's config to use to
        # BUILDER_CONFIGS. conllu_lib contains a set of ready-to-use features.
        BUILDER_CONFIGS = [
            conllu_lib.get_universal_morphology_config(
                language='',
                features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES,
                name='')
        ]

        def _info(self) -> tfds.core.DatasetInfo:
          """Returns the dataset metadata."""
          # {info.todo}: Specifies the dataset infos.
          return self.create_dataset_info(
              homepage='',
          )

        def _split_generators(self, dl_manager: tfds.download.DownloadManager):
          """Returns SplitGenerators."""
          # {info.todo}: Downloads the data and defines the splits
          path = dl_manager.download_and_extract('https://todo-data-url')

          # {info.todo}: Specify the process_example_fn to be used in the
          # `_generate_examples` method to process examples.
          # The default `process_example_fn` processes a conllu-annotated
          # example using the features specified in BUILDER_CONFIGS.
          # `conllu_dataset_builder` already provides a number of ready-to-use
          # process functions.
          return {{
              'train':
                  self._generate_examples(
                      filepaths=path / 'train.txt',
                      # Remove if you want to use the default `process_example_fn`.
                      # process_example_fn=
                  )
          }}

        # {info.todo}: If you need a customized _generate_examples function,
        # comment out the following, otherwise remove it.
        # def _generate_examples(
        #     self,
        #     path: Union[epath.PathLike, List[epath.PathLike]],
        #   ):
        #   """Yields (key, example) examples."""
        #   pass
      '''
  )
  return content
