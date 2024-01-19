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

"""diamonds dataset."""

from __future__ import annotations

import collections

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This classic dataset contains physical attributes and prices of 53940 diamonds.

Attributes:

  * price: Price in US dollars.
  * carat: Weight of the diamond.
  * cut: Cut quality (ordered worst to best).
  * color: Color of the diamond (ordered best to worst).
  * clarity: Clarity of the diamond (ordered worst to best).
  * x: Length in mm.
  * y: Width in mm.
  * z: Depth in mm.
  * depth: Total depth percentage: 100 * z / mean(x, y)
  * table: Width of the top of the diamond relative to the widest point.

"""

_CITATION = """
@Book{,
  author = {Hadley Wickham},
  title = {ggplot2: Elegant Graphics for Data Analysis},
  publisher = {Springer-Verlag New York},
  year = {2016},
  isbn = {978-3-319-24277-4},
  url = {https://ggplot2.tidyverse.org},
}
"""

_CUTS = ('Fair', 'Good', 'Very Good', 'Premium', 'Ideal')
_COLORS = ('D', 'E', 'F', 'G', 'H', 'I', 'J')
_CLARITY = ('I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF')


def _features():
  return collections.OrderedDict((
      ('carat', np.float32),
      ('cut', tfds.features.ClassLabel(names=_CUTS)),
      ('color', tfds.features.ClassLabel(names=_COLORS)),
      ('clarity', tfds.features.ClassLabel(names=_CLARITY)),
      ('x', np.float32),
      ('y', np.float32),
      ('z', np.float32),
      ('depth', np.float32),
      ('table', np.float32),
  ))


_URL = 'https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/diamonds.csv'


class Diamonds(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for diamonds dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'features': {k: v for k, v in _features().items()},
            'price': np.float32,
        }),
        supervised_keys=('features', 'price'),
        homepage='https://ggplot2.tidyverse.org/reference/diamonds.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    data = dl_manager.download({'data': _URL})
    # There is no predefined train/val/test split for this dataset.
    return {tfds.Split.TRAIN: self._generate_examples(file_path=data['data'])}

  def _generate_examples(self, file_path):
    """Yields examples."""
    pd = tfds.core.lazy_imports.pandas

    with epath.Path(file_path).open() as f:
      df = pd.read_csv(f)

    for row in df.itertuples():
      yield row.Index, {
          'features': {k: getattr(row, k) for k in _features().keys()},
          'price': row.price,
      }
