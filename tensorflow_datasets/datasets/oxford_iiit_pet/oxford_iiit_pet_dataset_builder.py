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

"""Oxford-IIIT pet dataset."""

import os
import xml.etree.ElementTree

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "https://thor.robots.ox.ac.uk/~vgg/data/pets"

_LABEL_CLASSES = [
    "Abyssinian",
    "american_bulldog",
    "american_pit_bull_terrier",
    "basset_hound",
    "beagle",
    "Bengal",
    "Birman",
    "Bombay",
    "boxer",
    "British_Shorthair",
    "chihuahua",
    "Egyptian_Mau",
    "english_cocker_spaniel",
    "english_setter",
    "german_shorthaired",
    "great_pyrenees",
    "havanese",
    "japanese_chin",
    "keeshond",
    "leonberger",
    "Maine_Coon",
    "miniature_pinscher",
    "newfoundland",
    "Persian",
    "pomeranian",
    "pug",
    "Ragdoll",
    "Russian_Blue",
    "saint_bernard",
    "samoyed",
    "scottish_terrier",
    "shiba_inu",
    "Siamese",
    "Sphynx",
    "staffordshire_bull_terrier",
    "wheaten_terrier",
    "yorkshire_terrier",
]
_SPECIES_CLASSES = ["Cat", "Dog"]

# List of samples with corrupt image files
_SKIP_SAMPLES = [
    "beagle_116",
    "chihuahua_121",
    "Abyssinian_5",
    "Abyssinian_34",
    "Egyptian_Mau_14",
    "Egyptian_Mau_139",
    "Egyptian_Mau_145",
    "Egyptian_Mau_156",
    "Egyptian_Mau_167",
    "Egyptian_Mau_177",
    "Egyptian_Mau_186",
    "Egyptian_Mau_191"
]

def _get_head_bbox(annon_filepath):
  """Read head bbox from annotation XML file."""
  with tf.io.gfile.GFile(annon_filepath, "r") as f:
    root = xml.etree.ElementTree.parse(f).getroot()

    # Disable pytype to avoid attribute-error due to find returning
    # Optional[Element]
    # pytype: disable=attribute-error
    size = root.find("size")
    width = float(size.find("width").text)
    height = float(size.find("height").text)

    obj = root.find("object")
    bndbox = obj.find("bndbox")
    xmax = float(bndbox.find("xmax").text)
    xmin = float(bndbox.find("xmin").text)
    ymax = float(bndbox.find("ymax").text)
    ymin = float(bndbox.find("ymin").text)
    return tfds.features.BBox(
              ymin / height, xmin / width, ymax / height, xmax / width
        )


class Builder(tfds.core.GeneratorBasedBuilder):
  """Oxford-IIIT pet dataset."""

  VERSION = tfds.core.Version("3.2.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=_LABEL_CLASSES),
            "species": tfds.features.ClassLabel(names=_SPECIES_CLASSES),
            "file_name": tfds.features.Text(),
            "segmentation_mask": tfds.features.Image(
                shape=(None, None, 1), use_colormap=True
            ),
            "head": tfds.features.BBoxFeature()
        }),
        supervised_keys=("image", "label"),
        homepage="http://www.robots.ox.ac.uk/~vgg/data/pets/",
    )

  def _split_generators(self, dl_manager):
    """Returns splits."""
    # Download images and annotations that come in separate archives.
    # Note, that the extension of archives is .tar.gz even though the actual
    # archives format is uncompressed tar.
    dl_paths = dl_manager.download_and_extract({
        "images": _BASE_URL + "/images.tar.gz",
        "annotations": _BASE_URL + "/annotations.tar.gz",
    })

    images_path_dir = os.path.join(dl_paths["images"], "images")
    annotations_path_dir = os.path.join(dl_paths["annotations"], "annotations")

    # Setup train and test splits
    train_split = tfds.core.SplitGenerator(
        name="train",
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(
                annotations_path_dir, "trainval.txt"
            ),
        },
    )
    test_split = tfds.core.SplitGenerator(
        name="test",
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(annotations_path_dir, "test.txt"),
        },
    )

    return [train_split, test_split]

  def _generate_examples(
      self, images_dir_path, annotations_dir_path, images_list_file
  ):
    with tf.io.gfile.GFile(images_list_file, "r") as images_list:
      for line in images_list:
        image_name, label, species, _ = line.strip().split(" ")

        # skip corrupt samples
        if image_name in _SKIP_SAMPLES:
          continue

        trimaps_dir_path = os.path.join(annotations_dir_path, "trimaps")
        xmls_dir_path = os.path.join(annotations_dir_path, "xmls")

        trimap_name = image_name + ".png"
        xml_name = image_name + ".xml"
        image_name += ".jpg"
        label = int(label) - 1
        species = int(species) - 1

        try:
            head_bbox = _get_head_bbox(os.path.join(xmls_dir_path, xml_name))
        except tf.errors.NotFoundError:
            # test samples do not have an annotation file
            head_bbox = tfds.features.BBox(0., 0., 0., 0.)

        record = {
            "image": os.path.join(images_dir_path, image_name),
            "label": int(label),
            "species": species,
            "file_name": image_name,
            "segmentation_mask": os.path.join(trimaps_dir_path, trimap_name),
            "head": head_bbox
        }
        yield image_name, record
