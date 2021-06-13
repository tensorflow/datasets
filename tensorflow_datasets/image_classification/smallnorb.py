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

"""Smallnorb dataset."""

import numpy as np
from six import moves
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = r"""\
@article{LeCun2004LearningMF,
  title={Learning methods for generic object recognition with invariance to pose and lighting},
  author={Yann LeCun and Fu Jie Huang and L{\'e}on Bottou},
  journal={Proceedings of the 2004 IEEE Computer Society Conference on Computer Vision and Pattern Recognition},
  year={2004},
  volume={2},
  pages={II-104 Vol.2}
}
"""

_TRAINING_URL_TEMPLATE = (
    "https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/"
    "smallnorb-5x46789x9x18x6x2x96x96-training-{type}.mat.gz")
_TESTING_URL_TEMPLATE = (
    "https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/"
    "smallnorb-5x01235x9x18x6x2x96x96-testing-{type}.mat.gz")

_DESCRIPTION = r"""\
This database is intended for experiments in 3D object recognition from shape. It contains images of 50 toys belonging to 5 generic categories: four-legged animals, human figures, airplanes, trucks, and cars. The objects were imaged by two cameras under 6 lighting conditions, 9 elevations (30 to 70 degrees every 5 degrees), and 18 azimuths (0 to 340 every 20 degrees).

The training set is composed of 5 instances of each category (instances 4, 6, 7, 8 and 9), and the test set of the remaining 5 instances (instances 0, 1, 2, 3, and 5).
"""


class Smallnorb(tfds.core.GeneratorBasedBuilder):
  """Smallnorb data set."""

  VERSION = tfds.core.Version("2.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.1.0"),
  ]
  RELEASE_NOTES = {
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    features_dict = {
        "image":
            tfds.features.Image(shape=(96, 96, 1)),
        "image2":
            tfds.features.Image(shape=(96, 96, 1)),
        "label_category":
            tfds.features.ClassLabel(names=[
                "four-legged animals",
                "human figures",
                "airplanes",
                "trucks",
                "cars",
            ]),
        "instance":
            tfds.features.ClassLabel(num_classes=10),
        "label_elevation":
            tfds.features.ClassLabel(num_classes=9),
        "label_azimuth":
            tfds.features.ClassLabel(num_classes=18),
        "label_lighting":
            tfds.features.ClassLabel(num_classes=6),
    }
    if self.version > "2.0.0":
      features_dict["id"] = tfds.features.Text()
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        homepage="https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/",
        citation=_CITATION,
        supervised_keys=("image", "label_category"),
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    filenames = {
        "training_dat": _TRAINING_URL_TEMPLATE.format(type="dat"),
        "training_cat": _TRAINING_URL_TEMPLATE.format(type="cat"),
        "training_info": _TRAINING_URL_TEMPLATE.format(type="info"),
        "testing_dat": _TESTING_URL_TEMPLATE.format(type="dat"),
        "testing_cat": _TESTING_URL_TEMPLATE.format(type="cat"),
        "testing_info": _TESTING_URL_TEMPLATE.format(type="info"),
    }

    files = dl_manager.download_and_extract(filenames)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                split_prefix="train_",
                dat_path=files["training_dat"],
                cat_path=files["training_cat"],
                info_path=files["training_info"])),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                split_prefix="test_",
                dat_path=files["testing_dat"],
                cat_path=files["testing_cat"],
                info_path=files["testing_info"])),
    ]

  def _generate_examples(self, split_prefix, dat_path, cat_path, info_path):
    """Generate examples for the Smallnorb dataset.

    Args:
      split_prefix: Prefix that identifies the split.
      dat_path: Path to dat file of the chunk.
      cat_path: Path to cat file of the chunk.
      info_path: Path to info file of the chunk.

    Yields:
      Dictionaries with images and the different labels.
    """
    dat_arr, cat_arr, info_arr = _load_chunk(dat_path, cat_path, info_path)

    for i, (image, category,
            info_vec) in enumerate(moves.zip(dat_arr, cat_arr, info_arr)):
      record = {
          "image": image[0],
          "image2": image[1],
          "label_category": category,
          "instance": info_vec[0],
          "label_elevation": info_vec[1],
          "label_azimuth": info_vec[2],
          "label_lighting": info_vec[3],
      }
      if self.version > "2.0.0":
        record["id"] = "{}{:05d}".format(split_prefix, i)
      yield i, record


def _load_chunk(dat_path, cat_path, info_path):
  """Loads a data chunk as specified by the paths.

  Args:
    dat_path: Path to dat file of the chunk.
    cat_path: Path to cat file of the chunk.
    info_path: Path to info file of the chunk.

  Returns:
    Tuple with the dat, cat, info_arrays.
  """
  dat_array = read_binary_matrix(dat_path)
  # Even if the image is gray scale, we need to add an extra channel dimension
  # to be compatible with tfds.features.Image.
  dat_array = np.expand_dims(dat_array, -1)

  cat_array = read_binary_matrix(cat_path)

  info_array = read_binary_matrix(info_path)
  info_array = np.copy(info_array)  # Make read-only buffer array writable.
  # Azimuth values are 0, 2, 4, .., 34. We divide by 2 to get proper labels.
  info_array[:, 2] = info_array[:, 2] / 2

  return dat_array, cat_array, info_array


def read_binary_matrix(filename):
  """Reads and returns binary formatted matrix stored in filename.

  The file format is described on the data set page:
  https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/

  Args:
    filename: String with path to the file.

  Returns:
    Numpy array contained in the file.
  """
  with tf.io.gfile.GFile(filename, "rb") as f:
    s = f.read()

    # Data is stored in little-endian byte order.
    int32_dtype = np.dtype("int32").newbyteorder("<")

    # The first 4 bytes contain a magic code that specifies the data type.
    magic = int(np.frombuffer(s, dtype=int32_dtype, count=1))
    if magic == 507333717:
      data_dtype = np.dtype("uint8")  # uint8 does not have a byte order.
    elif magic == 507333716:
      data_dtype = np.dtype("int32").newbyteorder("<")
    else:
      raise ValueError("Invalid magic value for data type!")

    # The second 4 bytes contain an int32 with the number of dimensions of the
    # stored array.
    ndim = int(np.frombuffer(s, dtype=int32_dtype, count=1, offset=4))

    # The next ndim x 4 bytes contain the shape of the array in int32.
    dims = np.frombuffer(s, dtype=int32_dtype, count=ndim, offset=8)

    # If the array has less than three dimensions, three int32 are still used to
    # save the shape info (remaining int32 are simply set to 1). The shape info
    # hence uses max(3, ndim) bytes.
    bytes_used_for_shape_info = max(3, ndim) * 4

    # The remaining bytes are the array.
    data = np.frombuffer(
        s, dtype=data_dtype, offset=8 + bytes_used_for_shape_info)
  return data.reshape(tuple(dims))
