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

"""INaturalist2018 dataset."""

import json
import os
import urllib

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
There are a total of 8,142 species in the dataset, with 437,513 training images,
and 24,426 validation images. Each image has one ground truth label.
"""
_CITATION = r"""\
@misc{inaturalist18,
    Howpublished = {~\url{https://github.com/visipedia/inat_comp/tree/master/2018}},
    Title = {{iNaturalist} 2018 competition dataset.},
    Year = {2018},
    key = {{iNaturalist} 2018 competition dataset},
    }
"""
_URL = "https://ml-inat-competition-datasets.s3.amazonaws.com/2018/"


class INaturalist2018(tfds.core.GeneratorBasedBuilder):
  """Dataset from the INaturalist Competition 2018."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self):
    """Define the dataset info."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(
                names_file=tfds.core.tfds_path(
                    os.path.join(
                        "image_classification",
                        "i_naturalist2018",
                        "inaturalist2018_labels.txt",
                    )
                )
            ),
            "supercategory": tfds.features.ClassLabel(
                names_file=tfds.core.tfds_path(
                    os.path.join(
                        "image_classification",
                        "i_naturalist2018",
                        "inaturalist2018_supercategories.txt",
                    )
                )
            ),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/visipedia/inat_comp/tree/master/2018",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    output_files = dl_manager.download_and_extract({
        "trainval_images": tfds.download.Resource(
            url=urllib.parse.urljoin(_URL, "train_val2018.tar.gz"),
            extract_method=tfds.download.ExtractMethod.NO_EXTRACT,
        ),
        "train_annos": urllib.parse.urljoin(_URL, "train2018.json.tar.gz"),
        "val_annos": urllib.parse.urljoin(_URL, "val2018.json.tar.gz"),
        "test_images": tfds.download.Resource(
            url=urllib.parse.urljoin(_URL, "test2018.tar.gz"),
            extract_method=tfds.download.ExtractMethod.NO_EXTRACT,
        ),
        "categories": urllib.parse.urljoin(_URL, "categories.json.tar.gz"),
    })
    return {
        "train": self._generate_examples(
            images_archive=dl_manager.iter_archive(
                output_files["trainval_images"]
            ),
            annon_file=os.path.join(
                output_files["train_annos"], "train2018.json"
            ),
            category_file=os.path.join(
                output_files["categories"], "categories.json"
            ),
        ),
        "validation": self._generate_examples(
            images_archive=dl_manager.iter_archive(
                output_files["trainval_images"]
            ),
            annon_file=os.path.join(output_files["val_annos"], "val2018.json"),
            category_file=os.path.join(
                output_files["categories"], "categories.json"
            ),
        ),
        "test": self._generate_examples(
            images_archive=dl_manager.iter_archive(output_files["test_images"]),
            annon_file=None,
            category_file=None,
        ),
    }

  def _generate_examples(self, images_archive, annon_file, category_file):
    """Generate examples."""
    if annon_file is not None:
      # Training and validation images.
      with tf.io.gfile.GFile(annon_file, "r") as f:
        data = json.load(f)
      with tf.io.gfile.GFile(category_file, "r") as f:
        categories = json.load(f)

        # First read the annotations file, used to filter the contents of the
      # tar.gz file when yielding examples.
      key2data = {}
      for image, annotation in zip(data["images"], data["annotations"]):
        category_id = annotation["category_id"]
        category = categories[category_id]["name"]
        supercategory = data["categories"][category_id]["supercategory"]
        key = os.path.basename(image["file_name"]).split(".")[0]
        key2data[key] = {
            "id": key,
            "label": category,
            "supercategory": supercategory,
        }
      # Read tar.gz file containing train & validation images and yield relevant
      # examples.
      for fpath, fobj in images_archive:
        key = os.path.basename(fpath).split(".")[0]
        if key in key2data:
          data = key2data[key].copy()
          data["image"] = fobj
          yield key, data
    else:
      # Read tar.gz file containing all test images and yield all examples.
      for fpath, fobj in images_archive:
        key = os.path.basename(fpath).split(".")[0]
        # Note: test labels are not annotated, so just return -1 as labels.
        yield key, {
            "id": key,
            "image": fobj,
            "label": -1,
            "supercategory": -1,
        }
