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

"""SUN (Scene UNderstanding) datasets."""

import io
import os

from absl import logging
import numpy as np
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_SUN397_URL = "https://vision.princeton.edu/projects/2010/SUN/"

# These images are badly encoded and cannot be decoded correctly (TF), or the
# decoding is not deterministic (PIL).
_SUN397_IGNORE_IMAGES = [
    "SUN397/c/church/outdoor/sun_bhenjvsvrtumjuri.jpg",
    "SUN397/t/track/outdoor/sun_aophkoiosslinihb.jpg",
]

_SUN397_BUILDER_CONFIG_DESCRIPTION_PATTERN = (
    "Train and test splits from the official partition number %d. "
    "Images are resized to have at most %s pixels, and compressed with 72 JPEG "
    "quality."
)


def _decode_image(fobj, session, filename):
  """Reads and decodes an image from a file object as a Numpy array.

  The SUN dataset contains images in several formats (despite the fact that
  all of them have .jpg extension). Some of them are:
    - BMP (RGB)
    - PNG (grayscale, RGBA, RGB interlaced)
    - JPEG (RGB)
    - GIF (1-frame RGB)
  Since TFDS assumes that all images have the same number of channels, we
  convert all of them to RGB.

  Args:
    fobj: File object to read from.
    session: TF session used to decode the images.
    filename: Filename of the original image in the archive.

  Returns:
    Numpy array with shape (height, width, channels).
  """

  buf = fobj.read()
  image = tfds.core.lazy_imports.cv2.imdecode(
      np.frombuffer(buf, dtype=np.uint8), flags=3
  )  # Note: Converts to RGB.
  if image is None:
    logging.warning(
        "Image %s could not be decoded by OpenCV, falling back to TF", filename
    )
    try:
      image = tf.image.decode_image(buf, channels=3)
      image = session.run(image)
    except tf.errors.InvalidArgumentError as e:
      raise ValueError(
          f"{e}. Image {filename} could not be decoded by Tensorflow."
      ) from e

  # The GIF images contain a single frame.
  if len(image.shape) == 4:  # rank=4 -> rank=3
    image = image.reshape(image.shape[1:])

  return image


def _encode_jpeg(image, quality=None):
  cv2 = tfds.core.lazy_imports.cv2
  extra_args = [[int(cv2.IMWRITE_JPEG_QUALITY), quality]] if quality else []
  _, buff = cv2.imencode(".jpg", image, *extra_args)
  return io.BytesIO(buff.tobytes())


def _process_image_file(
    fobj, session, filename, quality=None, target_pixels=None
):
  """Process image files from the dataset."""
  # We need to read the image files and convert them to JPEG, since some files
  # actually contain GIF, PNG or BMP data (despite having a .jpg extension) and
  # some encoding options that will make TF crash in general.
  image = _decode_image(fobj, session, filename=filename)
  # Get image height and width.
  height, width, _ = image.shape
  actual_pixels = height * width
  if target_pixels and actual_pixels > target_pixels:
    factor = np.sqrt(target_pixels / actual_pixels)
    image = tfds.core.lazy_imports.cv2.resize(
        image, dsize=None, fx=factor, fy=factor
    )
  return _encode_jpeg(image, quality=quality)


class Sun397Config(tfds.core.BuilderConfig):
  """BuilderConfig for Sun 397 dataset."""

  def __init__(
      self, target_pixels=None, partition=None, quality=None, **kwargs
  ):
    self._target_pixels = target_pixels
    self._partition = partition
    self._quality = quality
    super(Sun397Config, self).__init__(**kwargs)

  @property
  def target_pixels(self):
    return self._target_pixels

  @property
  def partition(self):
    return self._partition

  @property
  def quality(self):
    return self._quality


def _generate_builder_configs():
  """Return the BuilderConfig objects for the SUN397 dataset."""
  version = tfds.core.Version("4.0.0")
  builder_configs = [
      # Images randomly split into train/valid/test splits (70%/10%/20%), and
      # images resized to have at most 120,000 pixels.
      Sun397Config(
          name="tfds",
          version=version,
          target_pixels=120000,
          description=(
              "TFDS partition with random train/validation/test splits with "
              "70%/10%/20% of the images, respectively. Images are resized to "
              "have at most 120,000 pixels, and are compressed with 72 JPEG "
              "quality."
          ),
      ),
  ]
  # Configs for each of the standard partitions of the dataset.
  for partition in range(1, 10 + 1):
    description = _SUN397_BUILDER_CONFIG_DESCRIPTION_PATTERN % (
        partition,
        "120,000",
    )
    builder_configs.append(
        Sun397Config(
            name="standard-part%d-120k" % partition,
            partition=partition,
            target_pixels=120000,
            version=version,
            description=description,
        )
    )
  return builder_configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """Sun397 Scene Recognition Benchmark."""

  BUILDER_CONFIGS = _generate_builder_configs()

  def __init__(self, tfds_split_files=None, **kwargs):
    super(Builder, self).__init__(**kwargs)
    # Note: Only used for tests, since the data is fake.
    if not tfds_split_files:
      tfds_split_files = {
          "tr": "sun397_tfds_tr.txt",
          "te": "sun397_tfds_te.txt",
          "va": "sun397_tfds_va.txt",
      }
      for split, filename in tfds_split_files.items():
        tfds_split_files[split] = tfds.core.tfds_path(
            os.path.join("image_classification", filename)
        )
    self._tfds_split_files = tfds_split_files

  def _info(self):
    names_file = tfds.core.tfds_path(
        os.path.join("image_classification", "sun397_labels.txt")
    )
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "file_name": tfds.features.Text(),
            "image": tfds.features.Image(shape=(None, None, 3)),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        homepage=_SUN397_URL,
    )

  def _split_generators(self, dl_manager):
    paths = dl_manager.download_and_extract({
        "images": tfds.download.Resource(
            url=_SUN397_URL + "SUN397.tar.gz",
            extract_method=tfds.download.ExtractMethod.NO_EXTRACT,
        ),
        "partitions": _SUN397_URL + "download/Partitions.zip",
    })
    if not isinstance(paths, dict):
      # While testing download_and_extract() returns the dir containing the
      # test files.
      paths = {
          "images": os.path.join(paths, "SUN397.tar.gz"),
          "partitions": os.path.join(paths, "Partitions"),
      }
    images = tfds.download.Resource(
        path=paths["images"],
        extract_method=tfds.download.ExtractMethod.TAR_GZ_STREAM,
    )
    if self.builder_config.name == "tfds":
      subset_images = self._get_tfds_subsets_images()
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs=dict(
                  archive=dl_manager.iter_archive(images),
                  subset_images=subset_images["tr"],
              ),
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs=dict(
                  archive=dl_manager.iter_archive(images),
                  subset_images=subset_images["te"],
              ),
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs=dict(
                  archive=dl_manager.iter_archive(images),
                  subset_images=subset_images["va"],
              ),
          ),
      ]
    else:
      subset_images = self._get_partition_subsets_images(paths["partitions"])
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs=dict(
                  archive=dl_manager.iter_archive(images),
                  subset_images=subset_images["tr"],
              ),
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs=dict(
                  archive=dl_manager.iter_archive(images),
                  subset_images=subset_images["te"],
              ),
          ),
      ]

  def _generate_examples(self, archive, subset_images):
    prefix_len = len("SUN397")
    with tf.Graph().as_default():
      with utils.nogpu_session() as sess:
        for filepath, fobj in archive:
          if filepath in _SUN397_IGNORE_IMAGES:
            continue
          # Note: all files in the tar.gz are in SUN397/...
          filename = filepath[prefix_len:].replace("\\", "/")  # For windows
          if filename in subset_images:
            # Example:
            # From filename: /c/car_interior/backseat/sun_aenygxwhhmjtisnf.jpg
            # To class: /c/car_interior/backseat
            label = "/".join(filename.split("/")[:-1])
            image = _process_image_file(
                fobj,
                sess,
                filename,
                quality=self.builder_config.quality,
                target_pixels=self.builder_config.target_pixels,
            )
            record = {
                "file_name": filename,
                "image": image,
                "label": label,
            }
            yield filename, record

  def _get_tfds_subsets_images(self):
    splits_sets = {}
    for split, filepath in self._tfds_split_files.items():
      splits_sets[split] = self._load_image_set_from_file(filepath)
    return splits_sets

  def _get_partition_subsets_images(self, partitions_dir):
    # Get the ID of all images in the dataset.
    all_images = set()
    for split_images in self._get_tfds_subsets_images().values():
      all_images.update(split_images)
    # Load the images in the training/test split of this partition.
    filenames = {
        "tr": "Training_%02d.txt" % self.builder_config.partition,
        "te": "Testing_%02d.txt" % self.builder_config.partition,
    }
    splits_sets = {}
    for split, filename in filenames.items():
      filepath = os.path.join(partitions_dir, filename)
      splits_sets[split] = self._load_image_set_from_file(filepath)
    # Put the remaining images in the dataset into the "validation" split.
    splits_sets["va"] = all_images - (splits_sets["tr"] | splits_sets["te"])
    return splits_sets

  def _load_image_set_from_file(self, filepath):
    with tf.io.gfile.GFile(os.fspath(filepath), mode="r") as f:
      return set([line.strip() for line in f])
