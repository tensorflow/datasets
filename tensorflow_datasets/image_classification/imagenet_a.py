# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""The ImageNet-A image classification dataset."""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = r"""
@article{hendrycks2019nae,
  title={Natural Adversarial Examples},
  author={Dan Hendrycks and Kevin Zhao and Steven Basart and Jacob Steinhardt and Dawn Song},
  journal={arXiv preprint arXiv:1907.07174},
  year={2019}
}
"""

_DESCRIPTION = """
ImageNet-A is a set of images labelled with ImageNet labels that were obtained
by collecting new data and keeping only those images that ResNet-50 models fail
to correctly classify. For more details please refer to the paper.

The label space is the same as that of ImageNet2012. Each example is
represented as a dictionary with the following keys:

* 'image': The image, a (H, W, 3)-tensor.
* 'label': An integer in the range [0, 1000).
* 'file_name': A unique sting identifying the example within the dataset.

"""

_IMAGENET_LABELS_FILENAME = r'image_classification/imagenet2012_labels.txt'
_IMAGENET_A_URL = r'https://people.eecs.berkeley.edu/~hendrycks/imagenet-a.tar'


class ImagenetA(tfds.core.GeneratorBasedBuilder):
  """Natural adversarial examples with ImageNet labels."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    names_file = tfds.core.tfds_path(_IMAGENET_LABELS_FILENAME)
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),
        }),
        # Used if as_supervised=True in # builder.as_dataset.
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/hendrycks/natural-adv-examples',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns a SplitGenerator for the test set."""
    imagenet_a_root = os.path.join(
        dl_manager.download_and_extract(_IMAGENET_A_URL), 'imagenet-a')
    return [
        tfds.core.SplitGenerator(
            # The dataset provides only a test split.
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'imagenet_a_root': imagenet_a_root},
        ),
    ]

  def _generate_examples(self, imagenet_a_root):
    """Yields the examples."""
    # The directory structure is `imagenet-a/imagenet_synset_id/filename.jpg`.
    for class_synset in tf.io.gfile.listdir(imagenet_a_root):
      class_dir = os.path.join(imagenet_a_root, class_synset)
      if not tf.io.gfile.isdir(class_dir):
        continue
      for image_filename in tf.io.gfile.listdir(class_dir):
        image_path = os.path.join(class_dir, image_filename)
        features = {
            'image': image_path,
            'label': class_synset,
            'file_name': image_filename,
        }
        yield image_filename, features

