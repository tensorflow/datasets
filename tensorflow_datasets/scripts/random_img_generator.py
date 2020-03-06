import os
from zipfile import ZipFile
from PIL import Image
import numpy as np
import tarfile
import zipfile
import shutil
import gzip


# images_path variable to store the path of images for later compression
images_path = []


def image_process(root):
    """ Generate random images and remove noise of the
        images to compress better.

          Args:
           root: path of the images to get processed

    """
    images_path.append(root)
    image = np.array(Image.open(root))
    image = np.ones_like(image) * np.random.randint(np.amax(image))
    image = Image.fromarray(image)
    image = image.convert('RGB')
    image.save(root)


def rewrite_zip(filepath, filename):
    """ Rewrite the older .zip files into new better compressed one

            Args:
                filepath: path of the older zip file that need to be compressed
                filename: name of the older zip file that need to be compressed

    """
    # creating a temporary file to store images 
    temp = tempfile.TemporaryDirectory(dir=filepath)

    # Extraction of compressed .zip file
    with ZipFile(filepath+filename, 'r') as zip:
        zip.extractall(path=temp.name)
        print(temp.name)

        process_dir(temp.name+"/")  # Image Processing

    # Compressed the .zip file again
    with ZipFile(filepath+filename, 'w') as zip:
        for file in images_path:
            zip.write(file)


def rewrite_tar(filepath, filename):
    """ Rewrite the older .tar file into new better compressed one.
        Compression formats supports by this method (.tar.gz, .tgz, .tar.bz2)

            Args:
              filepath: path of the older .tar file that need to be compressed
              filename: name of the older .tar file that need to be compressed

    """
    # Create a tempfile to store the images with noise
    temp = tempfile.TemporaryDirectory(dir=filepath)

    # Extraction of .tar file
    with tarfile.open(filepath+filename, 'r') as tar:
        tar.extractall(path=temp.name)
        # Image Process to decrease the size
        process_dir(temp.name+"/")

    # Converting into tarfile again to decrease the space taken by the file-
    with tarfile.open(filepath+filename, 'w') as tar:
        for file in images_path:
            tar_handle.add(os.path.join(filepath, file))


def process_dir(path):
    """ This method process the whole directory which contains the
         compressed files.

          Args:
            path: path of the directory which contains all compression files

    """

    images_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            fileName = filepath.split('/')[-1]

            if filepath.endswith('.png') or filepath.endswith('.jpg')
            or filepath.endswith('.jpeg'):
                image_process(filepath)

            elif zipfile.is_zipfile(filepath):
                rewrite_zip(root, fileName)

            elif tarfile.is_tarfile(filepath):
                rewrite_tar(root, fileName)
