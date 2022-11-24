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

"""penguins dataset."""

from __future__ import annotations

import csv
import dataclasses
import textwrap
import typing
from typing import Any, Mapping, Optional, Union

import tensorflow_datasets.core.utils as type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_PENGUINS_PATH = ('https://storage.googleapis.com/download.tensorflow.org/'
                  'data/palmer_penguins/')
_DESCRIPTION = """\
Measurements for three penguin species observed in the Palmer Archipelago, Antarctica.

These data were collected from 2007 - 2009 by Dr. Kristen Gorman with the [Palmer
Station Long Term Ecological Research Program](https://pal.lternet.edu/), part
of the [US Long Term Ecological Research Network](https://lternet.edu/). The
data were originally imported from the [Environmental Data
Initiative](https://environmentaldatainitiative.org/) (EDI) Data Portal, and are
available for use by CC0 license ("No Rights Reserved") in accordance with the
Palmer Station Data Policy. This copy was imported from [Allison Horst's GitHub
repository](https://allisonhorst.github.io/palmerpenguins/articles/intro.html).
"""

_CITATION = """\
@Manual{,
  title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},
  author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},
  year = {2020},
  note = {R package version 0.1.0},
  doi = {10.5281/zenodo.3960218},
  url = {https://allisonhorst.github.io/palmerpenguins/},
}
"""

if typing.TYPE_CHECKING:
  FeatureType = Union[type_utils.TfdsDType, tfds.core.features.FeatureConnector]
else:
  FeatureType = Any


@dataclasses.dataclass
class PenguinConfig(tfds.core.BuilderConfig):
  """Palmer Penguins dataset builder config."""
  # Basename of the file hosting the data.
  file_name: str = ''
  # FeatureDict fields.
  features: Mapping[str, FeatureType] = dataclasses.field(default_factory=dict)
  # Which of the features to use as the label. Packs other features into a
  # single feature for use with `supervised_keys`.
  label: Optional[str] = None
  # What to do with OOV data; field_name -> value.
  cleanup: Optional[Mapping[str, Any]] = None


class Penguins(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for penguins dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      # pytype: disable=wrong-keyword-args
      PenguinConfig(
          name='processed',
          file_name='penguins_processed.csv',
          features={
              'species': tfds.features.ClassLabel(num_classes=3),
              'culmen_length_mm': tf.float32,
              'culmen_depth_mm': tf.float32,
              'flipper_length_mm': tf.float32,
              'body_mass_g': tf.float32,
          },
          description=textwrap.dedent("""\
            `penguins/processed` is a drop-in replacement for the `iris`
            dataset. It contains 4 normalised numerical features presented as a
            single tensor, no missing values and the class label (species) is
            presented as an integer (n = 334).
          """),
          label='species'),
      PenguinConfig(
          name='simple',
          file_name='penguins_size.csv',
          description=textwrap.dedent("""\
            `penguins/simple` has been processed from the raw dataset, with
            simplified class labels derived from text fields, missing values
            marked as NaN/NA and retains only 7 significant features (n = 344).
          """),
          features={
              'species':
                  tfds.features.ClassLabel(
                      names=['Adelie', 'Chinstrap', 'Gentoo']),
              'island':
                  tfds.features.ClassLabel(
                      names=['Biscoe', 'Dream', 'Torgersen']),
              'culmen_length_mm':
                  tf.float32,
              'culmen_depth_mm':
                  tf.float32,
              'flipper_length_mm':
                  tf.float32,
              'body_mass_g':
                  tf.float32,
              'sex':
                  tfds.features.ClassLabel(names=['FEMALE', 'MALE', 'NA']),
          },
          label='species',
          cleanup={
              'culmen_length_mm': 'NaN',
              'culmen_depth_mm': 'NaN',
              'flipper_length_mm': 'NaN',
              'body_mass_g': 'NaN',
              'sex': 'NA',
          }),
      PenguinConfig(
          name='raw',
          file_name='penguins_lter.csv',
          description=textwrap.dedent("""\
            `penguins/raw` is the original, unprocessed copy from @allisonhorst,
            containing all 17 features, presented either as numeric types or as
            raw text (n = 344).
          """),
          features={
              'studyName': tfds.features.Text(),
              'Sample Number': tf.int32,
              'Species': tfds.features.Text(),
              'Region': tfds.features.Text(),
              'Island': tfds.features.Text(),
              'Stage': tfds.features.Text(),
              'Individual ID': tfds.features.Text(),
              'Clutch Completion': tfds.features.Text(),
              'Date Egg': tfds.features.Text(),
              'Culmen Length (mm)': tf.float32,
              'Culmen Depth (mm)': tf.float32,
              'Flipper Length (mm)': tf.float32,
              'Body Mass (g)': tf.float32,
              'Sex': tfds.features.Text(),
              'Delta 15 N (o/oo)': tf.float32,
              'Delta 13 C (o/oo)': tf.float32,
              'Comments': tfds.features.Text(),
          },
          label='Species',
          cleanup={
              'Culmen Length (mm)': 'NaN',
              'Culmen Depth (mm)': 'NaN',
              'Flipper Length (mm)': 'NaN',
              'Body Mass (g)': 'NaN',
              'Delta 15 N (o/oo)': 'NaN',
              'Delta 13 C (o/oo)': 'NaN',
          }),
      # pytype: enable=wrong-keyword-args
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    supervised_keys = None
    features = self.builder_config.features
    supervised_features = features.copy()
    label_name = self.builder_config.label

    if self.builder_config.name == 'processed':
      label_feature = supervised_features.pop(label_name, None)
      supervised_keys = ('features', label_name)
      features = {
          label_name:
              label_feature,
          'features':
              tfds.features.Tensor(
                  shape=(len(supervised_features),),
                  dtype=next(iter(supervised_features.values())))
      }
    elif self.builder_config.name == 'simple':
      supervised_feature_names = {
          key: key for key in supervised_features.keys()
      }
      supervised_keys = (supervised_feature_names, label_name)

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=supervised_keys,
        homepage='https://allisonhorst.github.io/palmerpenguins/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download(_PENGUINS_PATH + self.builder_config.file_name)
    return {'train': self._generate_examples(path)}

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:  # pytype: disable=attribute-error  # gen-stub-imports
      for i, row in enumerate(csv.DictReader(f)):
        row = {f: self._clean_up(f, v) for f, v in row.items()}

        # Pack features if requested.
        if self.builder_config.name == 'processed':
          label_name = self.builder_config.label
          label = row.pop(label_name, None)
          row = list(row.values())
          yield i, {'features': row, label_name: label}
        else:
          yield i, row

  def _clean_up(self, field, value):
    """Applies field-level pre-processing, if needed."""
    if not self.builder_config.cleanup:
      return value
    if field not in self.builder_config.cleanup:
      return value

    feature_type = self.builder_config.features[field]
    if feature_type == tf.float32:
      # Field is a float. If it won't parse, clean it up.
      try:
        return float(value)
      except ValueError:
        return self.builder_config.cleanup[field]
    elif isinstance(feature_type, tfds.features.ClassLabel):
      # Field is a class. If it's OOV, clean it up.
      if value not in feature_type.names:
        return self.builder_config.cleanup[field]

    return value
