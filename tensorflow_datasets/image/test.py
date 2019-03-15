import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import numpy as np
import scipy.io
import os
import re


download_dir1 = "/home/iswariya/Desktop/working"
dl = tfds.download.DownloadManager(download_dir=download_dir1)

_IMAGES_URL = "http://www.vision.caltech.edu/visipedia-data/CUB-200/images.tgz"
path = dl.download(_IMAGES_URL)

print("DONNEEEEEEEEEEEEEEEEEEEEEEEE")
dl.iter_archive(path)

for fname, fobj in dl.iter_archive(path):
    print(fname)
