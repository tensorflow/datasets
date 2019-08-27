"""Tiny Imagenet: Smaller version of ImageNet"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import csv
import tensorflow as tf
import tensorflow_datasets as tfds

_CITATION = """\
@ONLINE {tiny_imagenet,
    title = "Tiny ImageNet Visual Recognition Challenge",
    url   = "https://tiny-imagenet.herokuapp.com"
}
"""

_DESCRIPTION = """\
Tiny Imagenet is a smaller version of ImageNet dataset.
Tiny Imagenet has 200 classes.
Each class has 500 training images, 50 validation images, and 50 test images.
Test split images don't have labels and return -1 as labels."""

_URL = "https://tiny-imagenet.herokuapp.com"


class TinyImagenet(tfds.core.GeneratorBasedBuilder):
  """Smaller version of ImageNet"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    """Returns Dataset Info"""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            # TODO(tiny_imagenet): Provide bbox from dataset
            # "bbox": tfds.features.BBoxFeature(),
            "label": tfds.features.ClassLabel(num_classes=200)
        }),
        supervised_keys=("image", "label"),
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Downloads data and returns SplitGenerators"""
    download_dir = dl_manager.download_and_extract(
        "http://cs231n.stanford.edu/tiny-imagenet-200.zip")
    download_dir = os.path.join(download_dir, "tiny-imagenet-200")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "download_dir": download_dir,
                "split": tfds.Split.TRAIN
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "download_dir": download_dir,
                "split": tfds.Split.VALIDATION
            }
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "download_dir": download_dir,
                "split": tfds.Split.TEST
            }
        )
    ]

  def _generate_examples(self, download_dir, split):
    """Yields examples."""
    with tf.io.gfile.GFile(os.path.join(download_dir, "wnids.txt")) as classes_f:
      classes = classes_f.read().split()
    assert len(classes) == 200, "Labels length should be exactly 200"

    if split == tfds.Split.TRAIN:
      images = tf.io.gfile.glob(os.path.join(
          download_dir, "train/*/images/*.JPEG"))
      for image in images:
        image_id = os.path.basename(image)[:-5]
        label = classes.index(image_id.split("_")[0])
        yield image_id, {"image": image, "label": label}
    elif split == tfds.Split.VALIDATION:
      with tf.io.gfile.GFile(os.path.join(download_dir, "val/val_annotations.txt")) as csvfile:
        rows = csv.reader(csvfile, delimiter="\t")
        for image, label, *_ in rows:
          image_id = image.split(".")[0]
          image = os.path.join(download_dir, "val/images", image)
          label = classes.index(label)
          yield image_id, {"image": image, "label": label}
    elif split == tfds.Split.TEST:
      for f in tf.io.gfile.glob(os.path.join(download_dir, "test", "*.JPEG")):
        image_id = os.path.basename(f)[:-5]
        yield image_id, {"image": f, "label": -1}
    else:
      raise NotImplementedError(
          "Invalid split: {}".format(str(split)))
