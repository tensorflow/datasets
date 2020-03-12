# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""FileFolder datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import os

from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


SUPPORTED_IMAGE_FORMAT = (".jpg", ".jpeg", ".png")


class ImageLabelFolder(tfds.core.GeneratorBasedBuilder):
  """Generic image classification dataset created from manual directory.

  The data directory should have the following structure:

  ```
  path/to/manual_dir/<dataset_name>/
    split_name/  # Ex: 'train'
      label1/  # Ex: 'airplane' or '0015'
        xxx.png
        xxy.png
        xxz.png
      label2/
        xxx.png
        xxy.png
        xxz.png
    split_name/  # Ex: 'test'
      ...
  ```

  To use it:

  ```
  builder = tfds.image.ImageLabelFolder('<dataset_name>')
  dl_config = tfds.download.DownloadConfig(manual_dir='path/to/manual_dir/')
  builder.download_and_prepare(download_config=dl_config)
  print(builder.info)  # Splits, num examples,... automatically extracted
  ds = builder.as_dataset(split='split_name', shuffle_files=True)
  ```

  Or with load:

  ```
  dl_config = tfds.download.DownloadConfig(manual_dir='path/to/manual_dir/')
  tfds.load(
      'image_label_folder',
      split='split_name'
      builder_kwargs=dict(dataset_name='<dataset_name>'),
      download_and_prepare_kwargs=dict(download_config=dl_config),
  )
  ```

  """

  MANUAL_DOWNLOAD_INSTRUCTIONS = "This is a 'template' dataset."

  VERSION = tfds.core.Version(
      "2.0.0", "New split API (https://tensorflow.org/datasets/splits)")

  # TODO(epot): Image shape should be automatically deduced

  def __init__(self, dataset_name="image_label_folder", **kwargs):
    self.name = dataset_name
    super(ImageLabelFolder, self).__init__(**kwargs)

  def _info(self):
    if not self._data_dir:
      logging.warning(
          "ImageLabelFolder.info is only complete once the data has been "
          "generated. Please call .download_and_prepare() before calling "
          ".info. The .info.features won't be computed.")

    return tfds.core.DatasetInfo(
        builder=self,
        description="Generic image classification dataset.",
        # Generic features before the data is generated
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(num_classes=None),
        }),
        supervised_keys=("image", "label"),
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators from the folder names."""
    # At data creation time, parse the folder to deduce number of splits,
    # labels, image size,

    # The splits correspond to the high level folders
    split_names = list_folders(dl_manager.manual_dir)

    # Extract all label names and associated images
    split_label_images = {}  # dict[split_name][label_name] = list(img_paths)
    for split_name in split_names:
      split_dir = os.path.join(dl_manager.manual_dir, split_name)
      split_label_images[split_name] = {
          label_name: list_imgs(os.path.join(split_dir, label_name))
          for label_name in list_folders(split_dir)
      }

    # Merge all label names from all splits to get the final list of labels
    # Sorted list for determinism
    labels = [split.keys() for split in split_label_images.values()]
    labels = list(sorted(set(itertools.chain(*labels))))

    # Could improve the automated encoding format detection
    # Extract the list of all image paths
    image_paths = [
        image_paths
        for label_images in split_label_images.values()
        for image_paths in label_images.values()
    ]
    if any(f.lower().endswith(".png") for f in itertools.chain(*image_paths)):
      encoding_format = "png"
    else:
      encoding_format = "jpeg"

    # Update the info.features. Those info will be automatically resored when
    # the dataset is re-created
    self.info.features["image"].set_encoding_format(encoding_format)
    self.info.features["label"].names = labels

    # Define the splits
    return [
        tfds.core.SplitGenerator(
            name=split_name,
            gen_kwargs=dict(label_images=label_images,),
        ) for split_name, label_images in split_label_images.items()
    ]

  def _generate_examples(self, label_images):
    """Generate example for each image in the dict."""

    for label, image_paths in label_images.items():
      for image_path in image_paths:
        key = "%s/%s" % (label, os.path.basename(image_path))
        yield key, {
            "image": image_path,
            "label": label,
        }


def list_folders(root_dir):
  return [
      f for f in tf.io.gfile.listdir(root_dir)
      if tf.io.gfile.isdir(os.path.join(root_dir, f))
  ]


def list_imgs(root_dir):
  return [
      os.path.join(root_dir, f)
      for f in tf.io.gfile.listdir(root_dir)
      if any(f.lower().endswith(ext) for ext in SUPPORTED_IMAGE_FORMAT)
  ]
