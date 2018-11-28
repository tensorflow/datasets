# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""FileFolder datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import json
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


METADATA_FILENAME = "image_folder_metadata.json"
SUPPORTED_IMAGE_FORMAT = (".jpg", ".jpeg", ".png")


class ImageLabelFolder(tfds.core.GeneratorBasedDatasetBuilder):
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
  builder.download_and_prepare(manual_dir='path/to/manual_dir/')
  print(ds_builder.info)  # Splits, num samples,... automatically extracted
  ds = builder.as_dataset(split='split_name')
  ```

  Or with load:

  ```
  tfds.load(
      'image_label_folder',
      split='split_name'
      builder_kwargs=dict(name='<dataset_name>'),
      download_and_prepare_kwargs=dict(manual_dir='path/to/manual_dir/'),
  )
  ```

  """

  # TODO(epot): Image shape should be automatically deduced

  def __init__(self, name, **kwargs):
    self.name = name
    super(ImageLabelFolder, self).__init__(**kwargs)

    if self._data_dir:  # Data is restored
      self._load_info_features()

  def _load_info_features(self):
    """Load shape, labels,... from the recorded metadata."""
    metadata_filename = os.path.join(self._data_dir, METADATA_FILENAME)
    with tf.gfile.Open(metadata_filename) as f:
      info_data = json.load(f)
    self.info.features = tfds.features.FeaturesDict({
        "image": tfds.features.Image(
            encoding_format=info_data["encoding_format"],
        ),
        "label": tfds.features.ClassLabel(names=info_data["labels"]),
    })

  def _info(self):
    if not self._data_dir:
      tf.logging.warning(
          "ImageLabelFolder.info is only complete once the data has been "
          "generated. Please call .download_and_prepare() before calling "
          ".info. The .info.features won't be computed.")

    return tfds.core.DatasetInfo(
        name=self.name,
        description="Generic image classification dataset.",
        # Placeholder generic features before the data is generated
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(num_classes=1),
        }),
        supervised_keys=("image", "label"),
    )

  def _split_generators(self, dl_manager):

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

    # Save the automatically computed metadata on disk (every time the dataset
    # is restored, metadata will be restored as well)
    metadata_filename = os.path.join(self._data_dir, METADATA_FILENAME)
    with tf.gfile.Open(metadata_filename, "w") as f:
      json.dump({
          "labels": labels,
          "encoding_format": encoding_format,
      }, f)

    # Update the info.features from the metadata file
    self._load_info_features()

    def num_samples(label_images):
      return sum(len(imgs) for imgs in label_images.values())

    # Define the splits
    return [
        tfds.core.SplitGenerator(
            name=split_name,
            # The number of shards is a dynamic function of the total
            # number of images (between 0-10)
            num_shards=min(10, max(num_samples(label_images) // 1000, 1)),
            gen_kwargs=dict(
                label_images=label_images,
            ),
        ) for split_name, label_images in split_label_images.items()
    ]

  def _generate_samples(self, label_images):
    """Generate sample for each image in the dict."""

    for label, image_paths in label_images.items():
      for image_path in image_paths:
        yield self.info.features.encode_sample({
            "image": image_path,
            "label": label,
        })


def list_folders(root_dir):
  return [
      f for f in tf.gfile.ListDirectory(root_dir)
      if tf.gfile.IsDirectory(os.path.join(root_dir, f))
  ]


def list_imgs(root_dir):
  return [
      os.path.join(root_dir, f) for f in tf.gfile.ListDirectory(root_dir)
      if any(f.lower().endswith(ext) for ext in SUPPORTED_IMAGE_FORMAT)
  ]
