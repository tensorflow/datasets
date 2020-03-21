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
from builtins import open as bltn_open

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

    os.chdir(root_dir) # Change directory to a legitimate file address, this is done so that directory not found error is not encountered because of rewrite_tar()
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
  with tempfile.TemporaryDirectory(dir=root_dir, suffix='fake') as temp_dir:
    # Checking the extension of file to be extract
    tar_filepath_lowercase = tar_filepath.lower()
    if tar_filepath_lowercase.endswith('gz'):
      extension = ':gz'
    elif tar_filepath_lowercase.endswith('bz2'):
      extension = ':bz2'
    elif tar_filepath_lowercase.endswith('xz'):
      extension = ':xz'
    else:
      extension = ''

    # Extraction of .tar file
    with tarfile.open(tar_filepath, 'r' + extension) as tar:
      tar.extractall(path=temp_dir)

    rewrite_dir(temp_dir)  # Recursivelly compress the archive content

    os.chdir(temp_dir) # Change to temporary directory so that temp directory name does not affect original filenames
    with tarfile.open(tar_filepath, 'w' + extension) as tar:
      tar_add(tar, '.', recursive=True) # Call custom recursive tar add operation


def tar_add(tar_file, name, arcname=None, recursive=True):
  """Perform addition of files to tarfile.
  This method replicates tarfile.add() and solves the issue of
  unnecessary filepaths like ., ./ and ./folder/.. being added to tarinfo.

  Args:
    tarfile: pass open tarfile object to which files need to be added
    name: Add the file `name' to the archive.
    `name' may be any type of file (directory, fifo, symbolic link, etc.)
    arcname: If given, `arcname' specifies an
    alternative name for the file in the archive.
    recursive: Option to specify if directories
    need to be added recursively.
    Directories are added recursively by default.
  """
  if arcname is None:
    arcname = name
  tarinfo = tar_file.gettarinfo(name, arcname)
  if tarinfo.isreg():
    with bltn_open(name, "rb") as f:
      # Filewise addition into tarball
      tar_file.addfile(tarinfo, f)
  elif tarinfo.isdir():
    if tarinfo.isfile(): # Only files should be added to tarinfo and not directories
      tar_file.addfile(tarinfo)
    if recursive:
      for f in sorted(os.listdir(name)):
        if name == os.curdir: # Remove redundant current directory address ',' from name
          name = ''
        arcname = name # Since arcname=None always, any changes to any changes to name should affect arcname
        tar_add(tar_file, os.path.join(name, f), os.path.join(arcname, f),
                recursive) # Recursive call to add all existing files to tarball


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
