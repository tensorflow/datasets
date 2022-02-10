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

r"""Historical wind field dataset for the Balloon Learning Environment."""

import concurrent.futures
import dataclasses
import itertools
from typing import Optional

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@software{ble2021,
author = {Greaves, Joshua and Candido, Salvatore and Dumoulin, Vincent and Goroshin, Ross and Ponda, Sameera S. and Bellemare, Marc G. and Castro, Pablo Samuel},
month = {12},
title = {{Balloon Learning Environment}},
url = {https://github.com/google/balloon-learning-environment},
version = {1.0.0},
year = {2021}
}

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,
Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,
Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,
Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,
Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,
Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,
Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF
atmospheric reanalyses of the global climate. Copernicus Climate Change Service
(C3S) Data Store (CDS). (Accessed on 01-04-2021)
"""

_DESCRIPTION = """

Historical wind field dataset for the Balloon Learning Environment.

4D wind fields, where the dimensions are latitude, longitude, altitude, and
time. Each entry contains two float values (_u_ and _v_) which indicate the wind
direction and magnitude at the specified location, altitude, and time.

Acknowledgements:

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Muñoz‐Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A.,
Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G.,
Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M.,
Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,
Healy, S., Hogan, R.J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P.,
Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F.,
Villaume, S., Thépaut, J-N. (2017): Complete ERA5: Fifth generation of ECMWF
atmospheric reanalyses of the global climate. Copernicus Climate Change Service
(C3S) Data Store (CDS). (Accessed on 01-04-2021)

"""


@dataclasses.dataclass
class BLEWindFieldConfig(tfds.core.BuilderConfig):
  num_fields: Optional[int] = None


class BLEWindField(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for the ble_wind_field dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      BLEWindFieldConfig(
          name='full',
          description='The entire historical wind field dataset.',
          num_fields=None),
      BLEWindFieldConfig(
          name='small',
          description='Small sample of 256 fields from the dataset.',
          num_fields=256),
  ]
  GCS_URL = tfds.core.as_path('gs://ble-public/downloads')
  GCS_FILENAME = 'historical_wind_fields.zarr'

  def _info(self) -> tfds.core.DatasetInfo:
    """Dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'field': tfds.features.Tensor(
                shape=(21, 21, 10, 9, 2),
                dtype=tf.float32,
                encoding=tfds.features.Encoding.ZLIB),
        }),
        supervised_keys=None,
        homepage='https://github.com/google/balloon-learning-environment',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    return {'train': self._generate_examples()}

  def _generate_examples(self):
    zarr = tfds.core.lazy_imports.zarr
    gcsfs_store = tfds.core.lazy_imports.gcsfs_store
    zarr_array = zarr.open_array(
        store=gcsfs_store(f'{self.GCS_URL}/{self.GCS_FILENAME}'),
        mode='r',
        synchronizer=zarr.ThreadSynchronizer())

    # During normal execution we don't expect `self.builder_config.num_fields`
    # to have a value larger than `zarr_array.shape[0]`, but for unit tests the
    # Zarr file used has a very small number of fields, so we take the minimum
    # to avoid trying to load more examples than available.
    num_fields = min(self.builder_config.num_fields or zarr_array.shape[0],
                     zarr_array.shape[0])

    # Zarr arrays are stored as compressed chunks on disk, and by default
    # read/write operations require to load and decompress entire chunks, even
    # if a single element in the chunk is accessed. The most efficient way of
    # iterating over elements is to load entire chunks and iterate over the
    # chunks' elements. The data can be chunked across all axes, but for
    # simplicity we assume that it's only chunked across the batch axis (which
    # is how the historical wind field array is organized).
    chunk_length = zarr_array.chunks[0]
    num_full_chunks = num_fields // chunk_length
    remainder = num_fields % chunk_length

    slices = (slice(i * chunk_length, (i + 1) * chunk_length)
              for i in range(num_full_chunks))
    if remainder:
      start = num_full_chunks * chunk_length
      slices = itertools.chain(slices, (slice(start, start + remainder),))

    keys = itertools.count()
    # We pipeline loading the data and writing it to tfrecords files using a
    # thread that loads chunks asynchronously.
    with concurrent.futures.ThreadPoolExecutor() as executor:
      load_fn = lambda next_slice: zarr_array[next_slice]
      # Keep at most 10 submitted loading tasks to reduce resource consumption.
      futures = {executor.submit(load_fn, next_slice)
                 for next_slice in itertools.islice(slices, 10)}
      while futures:
        done, futures = concurrent.futures.wait(
            futures, return_when=concurrent.futures.FIRST_COMPLETED)
        # Top up the submitted loading tasks.
        for next_slice in itertools.islice(slices, len(done)):
          futures.add(executor.submit(load_fn, next_slice))

        # Yield the loaded slices.
        for future in done:
          for field in future.result():
            yield next(keys), {'field': field}
