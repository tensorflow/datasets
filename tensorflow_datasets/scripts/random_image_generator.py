
""" Generate random images that compress better.
    By replacing the larger images with more compressable equivalents. """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import sys
import tempfile
import tarfile
import zipfile
import PIL.Image
import numpy as np
import absl.app
import absl.flags


FLAGS = absl.flags.FLAGS

absl.flags.DEFINE_string("dir_path",
                         "datasets\tensorflow_datasets\
                         testing\test_data\fake_examples",
                         "path to the directory which contains files")

def image_process(filepath):
  """ Generate random images and remove noise of the
  images to compress better.
  Args:
    filepath: path of the images to get processed
  """
  original_image_size = sys.getsizeof(filepath)
  image = np.array(PIL.Image.open(filepath))
  if image.dtype != np.bool:
    grey = int(hash(filepath) % 255)
    image = np.ones_like(image)*grey
    image = PIL.Image.fromarray(image)
    if image.mode == 'RGBA':
      image = image.convert('RGB')
    image.save(filepath)
    compressed_image_size = sys.getsizeof(filepath)
    if compressed_image_size > original_image_size:
      image.save(filepath, 'png')



def rewrite_zip(root_dir, zip_filepath):
  """ Rewrite the older .zip files into new better compressed one

  Args:
    root_dir: directory path which contain zip compressed file
    zip_filepath: path from directory to file

  """
    # creating a temporary file to store images
  with tempfile.TemporaryDirectory(dir=root_dir) as temp_dir:
    # Extraction of compressed .zip file
    with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
      zip_file.extractall(path=temp_dir)

    process_dir(temp_dir)  # Image Processing

        # Compressed the .zip file again
    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
      for file_dir, _, files in os.walk(temp_dir):
        for file in files:
          file_path = os.path.join(file_dir, file)
          zip_file.write(file_path)


def rewrite_tar(root_dir, tar_filepath):
  """ Rewrite the older .tar file into new better compressed one.
  Compression formats supports by this method (.tar.gz, .tgz, .tar.bz2)

  Args:
    root_dir: directory path which contain tar compressed file
    tar_filepath: path from directory to file

  """
  # Create a tempfile to store the images contain noise
  with tempfile.TemporaryDirectory(dir=root_dir) as temp_dir:
    #Checking the extension of file to be extract
    extension = tar_filepath.split('.')[-1]
    # Extraction of .tar file
    with tarfile.open(tar_filepath, 'r:'+extension) as tar:
      tar.extractall(path=temp_dir)
    # Image Process to decrease the size
    process_dir(temp_dir)

    # Converting into tarfile again to decrease the space taken by the file-
    with tarfile.open(tar_filepath, 'w:'+extension) as tar:
      tar.add(temp_dir, recursive=True)

def process_dir(dir_path):
  """ This method process the whole directory which contains the
  compressed files.

  Args:
    dir_path: path of the directory which contains all compression files
  """
  img_ext_list = ["jpg", "jpeg", "png"]
  for root_dir, _, files in os.walk(dir_path):
    for file in files:
      path = os.path.join(root_dir, file)
      img_ext = os.path.basename(file).split('.')[-1].lower()
      if img_ext in img_ext_list:
        image_process(path)
      elif path.endswith('.npz'):
        continue
      elif zipfile.is_zipfile(path):
        rewrite_zip(root_dir, path)

      elif tarfile.is_tarfile(path):
        rewrite_tar(root_dir, path)

def main(unused_argv):
  """ This method calls the process_dir method to start
  the process """
  del unused_argv
  process_dir(FLAGS.dir_path)


if __name__ == "__main__":
  absl.app.run(main)
