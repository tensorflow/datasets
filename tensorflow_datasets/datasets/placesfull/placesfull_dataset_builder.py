# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Dataset class for Placesfull (256x256) dataset."""
import csv
import os
import urllib

from etils import epath
import tensorflow_datasets.public_api as tfds

_BASE_URL = "http://data.csail.mit.edu/places/places365/"
_TRAIN_URL = "Images256.tar"
_FILE_ANNOTATION_URL = "filelist_placesfull.tar"

_IMAGE_SHAPE = (256, 256, 3)

_LABELS_FNAME = "datasets/placesfull/categories.txt"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Placesfull Images dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names_file=names_file),
            "filename": tfds.features.Text(),
        }),
        supervised_keys=("image", "label", "filename"),
        homepage="http://places2.csail.mit.edu/",
    )

  def _split_generators(self, dl_manager):
    output_archives = dl_manager.download(
        {
            "train": urllib.parse.urljoin(_BASE_URL, _TRAIN_URL),
        }
    )
    annotation_path = dl_manager.download_and_extract(
        urllib.parse.urljoin(_BASE_URL, _FILE_ANNOTATION_URL)
    )

    return {
        "train": self._generate_examples(
            archive=dl_manager.iter_archive(output_archives["train"]),
            path_prefix="Images256",
            split_name="train",
            annotation_path=os.path.join(
                annotation_path, "filelist_placesfull/imagelist_placesfull.txt"
            ),
        )
    }

  def _generate_examples(
      self, archive, path_prefix, split_name, annotation_path
  ):
    with epath.Path(annotation_path).open() as f:
      if split_name == "test":
        # Test split doesn't have labels assigned.
        file_to_class = {x[0]: -1 for x in csv.reader(f, delimiter=" ")}
      else:
        file_to_class = {x[0]: int(x[1]) for x in csv.reader(f, delimiter=" ")}

    for fname, fobj in archive:
      fname = fname.replace("\\", "/")  # For Windows compatibility.
      assert fname.startswith(path_prefix)
      # The filenames in annotations for train start with "/" while the names
      # for test and validation do not have a leading "/", so we chop
      # differently.
      chop = len(path_prefix) if split_name == "train" else len(path_prefix) + 1
      key = fname[chop:]

      class_id = file_to_class[key]
      yield fname, {"image": fobj, "label": class_id, "filename": fname}
