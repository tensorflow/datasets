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

"""Show example util.
"""

from typing import Any

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.visualization import image_visualizer
from tensorflow_metadata.proto.v0 import statistics_pb2


_ALL_VISUALIZERS = [
    image_visualizer.ImageGridVisualizer(),
]


def show_examples(
    ds: tf.data.Dataset,
    ds_info: dataset_info.DatasetInfo,
    **options_kwargs: Any
):
  """Visualize images (and labels) from an image classification dataset.

  This function is for interactive use (Colab, Jupyter). It displays and return
  a plot of (rows*columns) images from a tf.data.Dataset.

  Usage:
  ```python
  ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
  fig = tfds.show_examples(ds, ds_info)
  ```

  Args:
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until
      (rows * cols) are read or the dataset is consumed.
    ds_info: The dataset info object to which extract the label and features
      info. Available either through `tfds.load('mnist', with_info=True)` or
      `tfds.builder('mnist').info`
    **options_kwargs: Additional display options, specific to the dataset type
      to visualize. Are forwarded to `tfds.visualization.Visualizer.show`.
      See the `tfds.visualization` for a list of available visualizers.

  Returns:
    fig: The `matplotlib.Figure` object
  """
  if not isinstance(ds_info, dataset_info.DatasetInfo):  # Arguments inverted
    # `absl.logging` does not appear on Colab by default, so uses print instead.
    print('WARNING: For consistency with `tfds.load`, the `tfds.show_examples` '
          'signature has been modified from (info, ds) to (ds, info).\n'
          'The old signature is deprecated and will be removed. '
          'Please change your call to `tfds.show_examples(ds, info)`')
    ds, ds_info = ds_info, ds

  # Pack `as_supervised=True` datasets
  ds = dataset_info.pack_as_supervised_ds(ds, ds_info)

  for visualizer in _ALL_VISUALIZERS:
    if visualizer.match(ds_info):
      return visualizer.show(ds, ds_info, **options_kwargs)
    raise ValueError(
        'Visualisation not supported for dataset `{}`'.format(ds_info.name)
    )


def show_statistics(
    ds_info: dataset_info.DatasetInfo,
    split: splits.Split = splits.Split.TRAIN,
    disable_logging: bool = True,
) -> None:
  """Display the datasets statistics on a Colab/Jupyter notebook.

  `tfds.show_statistics` is a wrapper around
  [tensorflow_data_validation](https://www.tensorflow.org/tfx/data_validation/get_started)
  which calls `tfdv.visualize_statistics`. Statistics are displayed using
  [FACETS OVERVIEW](https://pair-code.github.io/facets/).

  Usage:

  ```
  builder = tfds.builder('mnist')
  tfds.show_statistics(builder.info)
  ```

  Or:

  ```
  ds, ds_info = tfds.load('mnist', with_info)
  tfds.show_statistics(ds_info)
  ```

  Note: In order to work, `tensorflow_data_validation` must be installed and
  the dataset info object must contain the statistics. For "official" datasets,
  only datasets which have been added/updated recently will contains statistics.
  For "custom" datasets, you need to generate the dataset with
  `tensorflow_data_validation` installed to have the statistics.

  Args:
    ds_info: The `tfds.core.DatasetInfo` object containing the statistics.
    split: Split for which generate the statistics.
    disable_logging: `bool`, if True, disable the tfdv logs which can be
      too verbose.

  Returns:
    `None`
  """
  tfdv = lazy_imports_lib.lazy_imports.tensorflow_data_validation

  if split not in ds_info.splits:
    raise ValueError(
        'Invalid requested split: \'{}\'. Only {} are availables.'.format(
            split, list(ds_info.splits)))

  # Creates the statistics.
  statistics = statistics_pb2.DatasetFeatureStatisticsList()
  statistics.datasets.add().CopyFrom(ds_info.splits[split].statistics)
  with utils.disable_logging() if disable_logging else utils.nullcontext():
    return tfdv.visualize_statistics(statistics)
