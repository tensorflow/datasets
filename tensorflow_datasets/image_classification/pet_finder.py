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

"""PetFinder Dataset."""

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# petfinder: BibTeX citation
_CITATION = """
@ONLINE {kaggle-petfinder-adoption-prediction,
    author = "Kaggle and PetFinder.my",
    title  = "PetFinder.my Adoption Prediction",
    month  = "april",
    year   = "2019",
    url    = "https://www.kaggle.com/c/petfinder-adoption-prediction/data/"
}
"""

_URL = ("https://storage.googleapis.com/petfinder_dataset/")
_DATA_OPTIONS = [
    "test_metadata", "test_images", "test_sentiment", "train_metadata",
    "train_images", "train_sentiment"
]
_LABEL_OPTIONS = [
    "test", "train", "breed_labels", "state_labels", "color_labels"
]

_DL_URLS = {name: _URL + name + ".zip" for name in _DATA_OPTIONS}
_DL_URLS.update({label: _URL + label + ".csv" for label in _LABEL_OPTIONS})

_INT_FEATS = [
    "Type", "Age", "Breed1", "Breed2", "Gender", "Color1", "Color2", "Color3",
    "MaturitySize", "FurLength", "Vaccinated", "Dewormed", "Sterilized",
    "Health", "Quantity", "Fee", "State", "VideoAmt"
]
_FLOAT_FEATS = ["PhotoAmt"]
_OBJ_FEATS = ["name", "Type", "PetID", "RescurID"]
_DESCRIPTION = ((
    "A large set of images of cats and dogs."
    "Together with the metadata information of sentiment information."))


class PetFinder(tfds.core.GeneratorBasedBuilder):
  """Pet Finder."""
  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="Dataset with images from 5 classes (see config name for "
        "information on the specific class)",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),
            "PetID": tfds.features.Text(),
            "attributes": {name: tf.int64 for name in _INT_FEATS},
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        supervised_keys=("attributes", "label"),
        homepage="https://www.kaggle.com/c/petfinder-adoption-prediction/data",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # petfinder: Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    # dl_paths = dl_manager.download_kaggle_data(url)
    dl_paths = dl_manager.download_and_extract(_DL_URLS)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "csv_name": "train.csv",
                "csv_paths": dl_paths["train"],
                "img_paths": dl_paths["train_images"],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "csv_name": "test.csv",
                "csv_paths": dl_paths["test"],
                "img_paths": dl_paths["test_images"],
            },
        ),
    ]

  def _generate_examples(self, csv_name, csv_paths, img_paths):
    """Yields examples.

    Args:
      csv_name: file name for the csv file used in the split
      csv_paths: Path to csv files containing the label and attributes
        information.
      img_paths: Path to images.
    """
    pd = tfds.core.lazy_imports.pandas

    if not tf.io.gfile.exists(csv_paths):
      raise AssertionError("{} not exist".format(csv_name))
    with tf.io.gfile.GFile(csv_paths) as csv_file:
      dataframe = pd.read_csv(csv_file)
    # add a dummy label for test set
    if csv_name == "test.csv":
      dataframe["AdoptionSpeed"] = -1

    images = tf.io.gfile.listdir(img_paths)
    for image in images:
      pet_id = image.split("-")[0]
      image_path = os.path.join(img_paths, image)
      attr_dict = dataframe.loc[dataframe["PetID"] == pet_id]
      record = {
          "image": image_path,
          "image/filename": image,
          "PetID": pet_id,
          "attributes": attr_dict[_INT_FEATS].to_dict("records")[0],
          "label": attr_dict["AdoptionSpeed"].values[0]
      }
      yield image, record
