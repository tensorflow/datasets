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
r"""Replace all images in the fake directory by more compressed version.

This allow to reduce size of the images in the `fake_data/` directory.

Instructions:

python replace_fake_images.py \
  --fake_dir=/path/to/tensorflow_datasets/testing/test_data/fake_examples


"""

import hashlib
import os
import tarfile
import tempfile
import zipfile
import shutil

import absl.app
import absl.flags
import numpy as np
import PIL.Image

FLAGS = absl.flags.FLAGS

absl.flags.DEFINE_string(
    'fake_dir', None, 'path to the directory which contains files')


def rewrite_image(filepath):
  """Replace the image by an new one with smaller size (uniform color).

  Args:
    filepath: path of the images to get processed
  """
  image_content = PIL.Image.open(filepath)
  image = np.array(image_content)
  # Filter unsuported images
  if image_content.mode == 'RGBA' or image.dtype == np.bool:
    return

  # The color is a deterministic function of the relative filepath.
  assert filepath.startswith(FLAGS.fake_dir)
  relative_filepath = filepath[len(FLAGS.fake_dir):]
  color = int(hashlib.md5(relative_filepath.encode('utf-8')).hexdigest(), 16)
  color %= 255

  image = np.ones_like(image) * color
  image = PIL.Image.fromarray(image)
  image.save(filepath, optimize=True)


def rewrite_zip(root_dir, zip_filepath):
  """Rewrite the given .zip file into a new one containing compressed images.

  Args:
    root_dir: directory path which contain zip compressed file
    zip_filepath: path from directory to file
  """
  # Creating a temporary file to store images
  with tempfile.TemporaryDirectory(dir=root_dir) as temp_dir:
    # Extraction of compressed .zip file
    with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
      zip_file.extractall(path=temp_dir)

    rewrite_dir(temp_dir)  # Recursivelly compress the archive content
    if zip_filepath.lower().endswith('zip'):
      shutil.make_archive(zip_filepath[:-len('.zip')], 'zip', temp_dir) #Copies the directory structure of the extracted file ans stores it back as zip

def rewrite_tar(root_dir, tar_filepath):
  """Rewrite the older .tar file into new better compressed one.

  Compression formats supports by this method (.tar.gz, .tgz, .tar.bz2)

  Args:
    root_dir: directory path which contain tar compressed file
    tar_filepath: path from directory to file

  """
  # Create a tempfile to store the images contain noise
  with tempfile.TemporaryDirectory(dir=root_dir) as temp_dir:
    # Checking the extension of file to be extract
    tar_filepath_lowercase = tar_filepath.lower()
    if tar_filepath_lowercase.endswith('gz'):
      extension = ':gz'
      shutil_extension = 'gztar'
      if tar_filepath_lowercase.endswith('tgz'):
        extension_removal_index = len('.tgz') # Obtain file name from filepath. Hardcoded indices are used as filenames may contain periods
      else:
        extension_removal_index = len('.tar.gz')
    elif tar_filepath_lowercase.endswith('bz2'):
      extension = ':bz2'
      shutil_extension = 'bztar'
      extension_removal_index = len('.tar.bz2')
    elif tar_filepath_lowercase.endswith('xz'):
      extension = ':xz'
      shutil_extension = 'xztar'
      extension_removal_index = len('.tar.xz')
    else:
      extension = ''
      shutil_extension = 'tar'
      extension_removal_index = -tar_filepath.find('.tar')

    # Extraction of .tar file
    with tarfile.open(tar_filepath, 'r' + extension) as tar:
      tar.extractall(path=temp_dir)

    rewrite_dir(temp_dir)  # Recursivelly compress the archive content
    shutil.make_archive(tar_filepath[:-extension_removal_index], shutil_extension, temp_dir) # Copies the directory structure of the extracted tar file and stores it back in the desired format


def rewrite_dir(fake_dir):
  """Process the whole directory which contains the compressed files.

  Args:
    fake_dir: path of the directory which contains all compression files
  """
  img_ext_list = ['jpg', 'jpeg', 'png']

  for root_dir, _, files in os.walk(fake_dir):
    for file in files:
      path = os.path.join(root_dir, file)
      img_ext = os.path.basename(file).split('.')[-1].lower()
      if img_ext in img_ext_list:
        rewrite_image(path)
      elif path.endswith('.npz'):  # Filter `.npz` files
        continue
      elif zipfile.is_zipfile(path):
        rewrite_zip(root_dir, path)
      elif tarfile.is_tarfile(path):
        rewrite_tar(root_dir, path)


def main(_):
  """Main script."""
  if FLAGS.fake_dir is None:
    raise ValueError('You should specify the path of the `fake_dir`')
  rewrite_dir(FLAGS.fake_dir)


if __name__ == '__main__':
  absl.app.run(main)
