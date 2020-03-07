""" tiny-imagenet dataset """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

import os

# TODO(tiny_imagenet_dataset): BibTeX citation
_CITATION = """@article{tiny-imagenet,
author = {Li,Fei-Fei}, {Karpathy,Andrej} and {Johnson,Justin}"}
"""

# TODO(tiny_imagenet_dataset):
_DESCRIPTION = """Tiny ImageNet Challenge is a similar challenge as ImageNet with a smaller dataset but
less image classes. It contains 200 image classes, a training
dataset of 100, 000 images, a validation dataset of 10, 000
images, and a test dataset of 10, 000 images. All images are
of size 64×64.
"""

_URL = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
_EXTRACTED_FOLDER_NAME = "tiny-imagenet-200"

SUPPORTED_IMAGE_FORMAT = (".jpg", ".jpeg", ".png")

def _list_folders(root_dir):
    return [
        f for f in tf.io.gfile.listdir(root_dir)
        if tf.io.gfile.isdir(os.path.join(root_dir, f))
    ]


def _list_imgs(root_dir):
    return [
        os.path.join(root_dir, f)
        for f in tf.io.gfile.listdir(root_dir)
        if any(f.lower().endswith(ext) for ext in SUPPORTED_IMAGE_FORMAT)
    ]


class TinyImagenetDataset(tfds.core.GeneratorBasedBuilder):
  """ tiny-imagenet dataset """

  # TODO(tiny_imagenet_dataset): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(tiny_imagenet_dataset): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(64, 64, 3), encoding_format="jpeg"),
            "id": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=200),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        homepage='https://tiny-imagenet.herokuapp.com/',
        citation=_CITATION,
    )
  
  def _process_train_ds(self, ds_folder, identities):
        path_to_ds = os.path.join(ds_folder, 'train')
        names = _list_folders(path_to_ds)

        label_images = {}
        for n in names:
            images_dir = os.path.join(path_to_ds, n, 'images')
            total_images = _list_imgs(images_dir)
            label_images[n] = {
                'images': total_images,
                'id': identities.index(n)
            }

        return label_images

  def _process_val_ds(self, ds_folder, identities):
        path_to_ds = os.path.join(ds_folder, 'val')

        # read the val_annotations.txt file
        with tf.io.gfile.GFile(os.path.join(path_to_ds, 'val_annotations.txt')) as f:
            data_raw = f.read()

        lines = data_raw.split("\n")

        label_images = {}
        for line in lines:
            if line == '':
                continue
            row_values = line.strip().split()
            label_name = row_values[1]
            if not label_name in label_images.keys():
                label_images[label_name] = {
                    'images': [],
                    'id': identities.index(label_name)
                }

            label_images[label_name]['images'].append(
                os.path.join(path_to_ds, 'images', row_values[0]))

        return label_images

  def _split_generators(self, dl_manager):
        extracted_path = dl_manager.download_and_extract(_URL)

        ds_folder = os.path.join(extracted_path, _EXTRACTED_FOLDER_NAME)

        with tf.io.gfile.GFile(os.path.join(ds_folder, 'wnids.txt')) as f:
            data_raw = f.read()

        lines = data_raw.split("\n")

        train_label_images = self._process_train_ds(ds_folder, lines)
        validation_label_images = self._process_val_ds(ds_folder, lines)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs=dict(label_images=train_label_images,)),

            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=1,
                gen_kwargs=dict(label_images=validation_label_images,)),
        ]

  def _generate_examples(self, label_images):
      for label, image_info in label_images.items():
          for image_path in image_info['images']:
              key = "%s/%s" % (label, os.path.basename(image_path))
              yield key, {
                  "image": image_path,
                  "id": label,
                  "label": image_info['id'],
              }

