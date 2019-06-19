# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""QuickDraw dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_QUICKDRAW_IMAGE_SIZE = 28
_QUICKDRAW_IMAGE_SHAPE = (_QUICKDRAW_IMAGE_SIZE, _QUICKDRAW_IMAGE_SIZE, 1)
_QUICKDRAW_BASE_URL = "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap"  # pylint: disable=line-too-long
_QUICKDRAW_LABELS_FNAME = "image/quickdraw_labels.txt"

_CITATION = """\
@article{DBLP:journals/corr/HaE17,
  author    = {David Ha and
               Douglas Eck},
  title     = {A Neural Representation of Sketch Drawings},
  journal   = {CoRR},
  volume    = {abs/1704.03477},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.03477},
  archivePrefix = {arXiv},
  eprint    = {1704.03477},
  timestamp = {Mon, 13 Aug 2018 16:48:30 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/HaE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_URL = "https://github.com/googlecreativelab/quickdraw-dataset"


class QuickdrawBitmap(tfds.core.GeneratorBasedBuilder):
  """Quickdraw bitmap dataset.

  This is the version of the QuickDraw data in which 28x28 grayscale images
  are generated from the raw vector information (i.e. the 'bitmap' dataset, not
  the 'raw' or 'simplified drawings' datasets).
  """
  VERSION = tfds.core.Version("1.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.0.0", experiments={tfds.core.Experiment.S3: True}),
      tfds.core.Version("1.0.0"),
  ]
  # Version history:
  # 2.0.0: S3 (new shuffling, sharding and slicing mechanism).

  def _info(self):
    labels_path = tfds.core.get_tfds_path(_QUICKDRAW_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=("The Quick Draw Dataset is a collection of 50 million "
                     "drawings across 345 categories, contributed by players "
                     "of the game Quick, Draw!. The bitmap dataset contains "
                     "these drawings converted from vector format into 28x28 "
                     "grayscale images"),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_QUICKDRAW_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names_file=labels_path),
        }),
        supervised_keys=("image", "label"),
        urls=[_URL],
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    # The QuickDraw bitmap repository is structured as one .npy file per label.
    labels = self.info.features["label"].names
    urls = {label: "{}/{}.npy".format(_QUICKDRAW_BASE_URL, label)
            for label in labels}

    file_paths = dl_manager.download(urls)

    # There is no predefined train/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=25,
            gen_kwargs={
                "file_paths": file_paths,
            })
    ]

  def _generate_examples(self, file_paths):
    """Generate QuickDraw bitmap examples.

    Given a list of file paths with data for each class label, generate examples
    in a random order.

    Args:
      file_paths: (dict of {str: str}) the paths to files containing the data,
                  indexed by label.

    Yields:
      The QuickDraw examples, as defined in the dataset info features.
    """
    for label, path in sorted(file_paths.items(), key=lambda x: x[0]):
      with tf.io.gfile.GFile(path, "rb") as f:
        class_images = np.load(f)
        for i, np_image in enumerate(class_images):
          record = {
              "image": np_image.reshape(_QUICKDRAW_IMAGE_SHAPE),
              "label": label,
          }
          if self.version.implements(tfds.core.Experiment.S3):
            yield "%s_%i" % (label, i), record
          else:
            yield record
