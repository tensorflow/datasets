
""" Generate random images that compress better.
    By replacing the larger images with more compressable equivalents. """

import os
import tempfile
import zipfile
import tarfile
from PIL import Image
import numpy as np
from absl import app
from absl import flags


FLAGS = flags.FLAGS

flags.DEFINE_string("dir_path",
                    "testing/test_data/fake_examples",
                    "path to the directory which contains files")

def image_process(filepath):
    """ Generate random images and remove noise of the
        images to compress better.

          Args:
           filepath: path of the images to get processed

    """
    image = np.array(Image.open(filepath))
    grey = int(hash(filepath) % 255)
    image = np.ones_like(image)*grey
    image = Image.fromarray(image)
    image = image.convert('RGB')
    image.save(filepath)



def rewrite_zip(_dir, path):
    """ Rewrite the older .zip files into new better compressed one

            Args:
                _dir: directory path which contain zip compressed file
                path: path from directory to file

    """
    # creating a temporary file to store images
    with tempfile.TemporaryDirectory(dir=_dir) as temp:

        # Extraction of compressed .zip file
        with zipfile.ZipFile(path, 'r') as _zp:
            _zp.extractall(path=temp)

        process_dir(temp)  # Image Processing

        # Compressed the .zip file again
        with zipfile.ZipFile(path, 'w') as _zp:
            for _file_dir, _, files in os.walk(temp):
                for _file in files:
                    file_path = os.path.join(_file_dir, _file)
                    _zp.write(file_path)


def rewrite_tar(_dir, path):
    """ Rewrite the older .tar file into new better compressed one.
        Compression formats supports by this method (.tar.gz, .tgz, .tar.bz2)

            Args:
              _dir: directory path which contain tar compressed file
              path: path from directory to file

    """
    # Create a tempfile to store the images contain noise
    with tempfile.TemporaryDirectory(dir=_dir) as temp:

        #Checking the extension of file to be extract
        ext_list = ["gz", "tgz", "bz2"]
        read_ext = path.split('.')[-1]
        write_ext = path.split('.')[-1]
        if read_ext in ext_list:
            read_ext = "r:" + read_ext
            write_ext = "w:" + write_ext
        else:
            read_ext = "r"
            write_ext = "w"

        # Extraction of .tar file
        with tarfile.open(path, read_ext) as tar:
            tar.extractall(path=temp)
        # Image Process to decrease the size
        process_dir(temp)

        # Converting into tarfile again to decrease the space taken by the file-

        with tarfile.open(path, write_ext) as tar:
            for _file_dir, _, files in os.walk(temp):
                for _file in files:
                    file_path = os.path.join(_file_dir, _file)
                    tar.add(file_path, recursive=False)



def process_dir(dir_path):
    """ This method process the whole directory which contains the
         compressed files.

          Args:
            path: path of the directory which contains all compression files

    """
    img_ext_list = ["jpg", "jpeg", "png"]
    for _dir, _, _files in os.walk(dir_path):
        for file in _files:
            path = os.path.join(_dir, file)
            _name = os.path.basename(file).split('.')[-1]
            _name = _name.lower()
            if _name in img_ext_list:
                image_process(path)

            elif zipfile.is_zipfile(path):
                rewrite_zip(_dir, path)

            elif tarfile.is_tarfile(path):
                rewrite_tar(_dir, path)

def main(unused_argv):
    """ This method calls the process_dir method to start
    the process """
    process_dir(FLAGS.dir_path)


if __name__ == "__main__":
    app.run(main)
