from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import PIL

from absl import app
from absl import flags

import tensorflow as tf
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(), "Path to tensorflow_datasets directory")

FLAGS = flags.FLAGS

NAME = "Img0001"
ANNOTATION = """
<annotation>
    <object>
		<name>RBC</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>78</xmin>
			<ymin>336</ymin>
			<xmax>184</xmax>
			<ymax>435</ymax>
		</bndbox>
	</object>
</annotation>
"""

def output_dir():
    return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "bccd")

def make_dir(path):
    dirpath = os.path.dirname(path)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def save_img(name):
    path = os.path.join(output_dir(), "JPEGImage", name + ".jpg")
    make_dir(path)
    image = fake_data_utils.get_random_picture(480, 640, 3)
    image = PIL.Image.fromarray(image)
    image.save(path)

def save_annotation(name):
    path = os.path.join(output_dir(), "Annotation", name + ".xml")
    make_dir(path)
    with open(path, "w") as f:
        f.write(ANNOTATION)

def save_train_txt(name):
    path = os.path.join(output_dir(), "ImageSets", "Main", "train.txt")
    make_dir(path)
    with open(path, "w") as f:
        f.write(name)

def main(argv):
    save_img(NAME)
    save_annotation(NAME)
    save_train_txt(NAME)

if __name__ == "__main__":
    app.run(main)
