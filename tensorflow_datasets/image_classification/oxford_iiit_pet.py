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

"""Oxford-IIIT pet dataset."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The Oxford-IIIT pet dataset is a 37 category pet image dataset with roughly 200
images for each class. The images have large variations in scale, pose and
lighting. All images have an associated ground truth annotation of breed.
"""

_CITATION = """\
@InProceedings{parkhi12a,
  author       = "Parkhi, O. M. and Vedaldi, A. and Zisserman, A. and Jawahar, C.~V.",
  title        = "Cats and Dogs",
  booktitle    = "IEEE Conference on Computer Vision and Pattern Recognition",
  year         = "2012",
}
"""

_BASE_URL = "http://www.robots.ox.ac.uk/~vgg/data/pets/data"

_LABEL_CLASSES = [
    "Abyssinian", "american_bulldog", "american_pit_bull_terrier",
    "basset_hound", "beagle", "Bengal", "Birman", "Bombay", "boxer",
    "British_Shorthair", "chihuahua", "Egyptian_Mau", "english_cocker_spaniel",
    "english_setter", "german_shorthaired", "great_pyrenees", "havanese",
    "japanese_chin", "keeshond", "leonberger", "Maine_Coon",
    "miniature_pinscher", "newfoundland", "Persian", "pomeranian", "pug",
    "Ragdoll", "Russian_Blue", "saint_bernard", "samoyed", "scottish_terrier",
    "shiba_inu", "Siamese", "Sphynx", "staffordshire_bull_terrier",
    "wheaten_terrier", "yorkshire_terrier"
]
_SPECIES_CLASSES = ["Cat", "Dog"]


class OxfordIIITPet(tfds.core.GeneratorBasedBuilder):
  """Oxford-IIIT pet dataset."""

  VERSION = tfds.core.Version("3.2.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(),
            "label":
                tfds.features.ClassLabel(names=_LABEL_CLASSES),
            "species":
                tfds.features.ClassLabel(names=_SPECIES_CLASSES),
            "file_name":
                tfds.features.Text(),
            "segmentation_mask":
                tfds.features.Image(shape=(None, None, 1), use_colormap=True)
        }),
        supervised_keys=("image", "label"),
        homepage="http://www.robots.ox.ac.uk/~vgg/data/pets/",
        citation=_CITATION,
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
            "images_dir_path":
                images_path_dir,
            "annotations_dir_path":
                annotations_path_dir,
            "images_list_file":
                os.path.join(annotations_path_dir, "trainval.txt"),
        },
    )
    test_split = tfds.core.SplitGenerator(
        name="test",
        gen_kwargs={
            "images_dir_path": images_path_dir,
            "annotations_dir_path": annotations_path_dir,
            "images_list_file": os.path.join(annotations_path_dir, "test.txt")
        },
    )

    return [train_split, test_split]

  def _generate_examples(self, images_dir_path, annotations_dir_path,
                         images_list_file):
    with tf.io.gfile.GFile(images_list_file, "r") as images_list:
      for line in images_list:
        image_name, label, species, _ = line.strip().split(" ")

        trimaps_dir_path = os.path.join(annotations_dir_path, "trimaps")

        trimap_name = image_name + ".png"
        image_name += ".jpg"
        label = int(label) - 1
        species = int(species) - 1

        record = {
            "image": os.path.join(images_dir_path, image_name),
            "label": int(label),
            "species": species,
            "file_name": image_name,
            "segmentation_mask": os.path.join(trimaps_dir_path, trimap_name)
        }
        yield image_name, record
