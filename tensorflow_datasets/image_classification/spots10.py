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

"""spots10"""

import os

import numpy as np
from six.moves import urllib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# spots10 constants
_spots10_URL = "https://github.com/Amotica/spots-10/raw/refs/heads/main/dataset/"
_spots10_TRAIN_DATA_FILENAME = "train-images-idx3-ubyte.gz"
_spots10_TRAIN_LABELS_FILENAME = "train-labels-idx1-ubyte.gz"
_spots10_TEST_DATA_FILENAME = "test-images-idx3-ubyte.gz"
_spots10_TEST_LABELS_FILENAME = "test-labels-idx1-ubyte.gz"
_spots10_IMAGE_SIZE = 32
spots10_IMAGE_SHAPE = (_spots10_IMAGE_SIZE, _spots10_IMAGE_SIZE, 1)
spots10_NUM_CLASSES = 10
_TRAIN_EXAMPLES = 40000
_TEST_EXAMPLES = 10000

_spots10_CITATION = """\
@article{atanbori2024spots,
  title={spots-10: Animal Pattern Benchmark Dataset for Machine Learning Algorithms},
  author={Atanbori, John},
  journal={arXiv preprint arXiv:2410.21044},
  year={2024}
}
"""

class spots10(tfds.core.GeneratorBasedBuilder):
  """spots10."""

  URL = _spots10_URL

  VERSION = tfds.core.Version("1.0.0")

  NAME = "spots10"

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="spots10 dataset consisting of grayscale images featuring patterns from various animal species.",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=spots10_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=spots10_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/Amotica/spots-10",
        citation=_spots10_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download the full spots10 Database
    filenames = {
        "train_data": _spots10_TRAIN_DATA_FILENAME,
        "train_labels": _spots10_TRAIN_LABELS_FILENAME,
        "test_data": _spots10_TEST_DATA_FILENAME,
        "test_labels": _spots10_TEST_LABELS_FILENAME,
    }
    spots10_files = dl_manager.download_and_extract(
        {k: urllib.parse.urljoin(self.URL, v) for k, v in filenames.items()}
    )

    # spots10 provides TRAIN and TEST splits, not a VALIDATION split, so we only
    # write the TRAIN and TEST splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                num_examples=_TRAIN_EXAMPLES,
                data_path=spots10_files["train_data"],
                label_path=spots10_files["train_labels"],
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                num_examples=_TEST_EXAMPLES,
                data_path=spots10_files["test_data"],
                label_path=spots10_files["test_labels"],
            ),
        ),
    ]

  def _generate_examples(self, num_examples, data_path, label_path):
    """Generate spots10 examples as dicts.

    Args:
      num_examples (int): The number of example.
      data_path (str): Path to the data files
      label_path (str): Path to the labels

    Yields:
      Generator yielding the next examples
    """
    images = _extract_spots10_images(data_path, num_examples)
    labels = _extract_spots10_labels(label_path, num_examples)
    data = list(zip(images, labels))

    # Using index as key since data is always loaded in same order.
    for index, (image, label) in enumerate(data):
      record = {"image": image, "label": label}
      yield index, record


def _extract_spots10_images(image_filepath, num_images):
  with tf.io.gfile.GFile(image_filepath, "rb") as f:
    f.read(16)  # header
    buf = f.read(_spots10_IMAGE_SIZE * _spots10_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf,
        dtype=np.uint8,
    ).reshape(num_images, _spots10_IMAGE_SIZE, _spots10_IMAGE_SIZE, 1)
    return data


def _extract_spots10_labels(labels_filepath, num_labels):
  with tf.io.gfile.GFile(labels_filepath, "rb") as f:
    f.read(8)  # header
    buf = f.read(num_labels)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels

'''
def main():
    print("Loading spots10 dataset...")

    # Load the spots10 dataset
    (train_data, test_data), dataset_info = tfds.load(
        'spots10',
        split=['train', 'test'],
        with_info=True,
        as_supervised=True
    )

    print("Dataset loaded successfully!")
    print(f"Number of training examples: {len(list(train_data))}")
    print(f"Number of test examples: {len(list(test_data))}")

    # Display dataset information
    print("Dataset Info:")
    print(dataset_info)

    # Example of displaying a few images
    import matplotlib.pyplot as plt

    def show_images(dataset, title, num_images=5):
        plt.figure(figsize=(10, 5))
        for i, (image, label) in enumerate(dataset.take(num_images)):
            plt.subplot(1, num_images, i + 1)
            plt.imshow(image.numpy().squeeze(), cmap='gray')
            plt.title(f"Label: {label.numpy()}")
            plt.axis('off')
        plt.suptitle(title)
        plt.show()

    show_images(train_data, "Training Data Samples")
    show_images(test_data, "Test Data Samples")


if __name__ == "__main__":
    main()
'''