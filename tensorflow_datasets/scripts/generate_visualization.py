"""
Script for generating dataset example figures

Uses show_examples() to generate example figures of a dataset
and stores it temporary in examples/

Typical usage example:

  ds_name = 'beans'
  generate_visualization(ds_name)

"""

import os
import tensorflow_datasets as tfds
from PIL import Image
from absl import app
import matplotlib.pyplot

FIG_DIR = ('../docs/catalog/images/examples/')

def generate_visualization(ds_name):
  """
  Method used to generate examples figures of a dataset
  """

  try:
    ds, ds_info = tfds.load(name=ds_name, split='train', with_info=True)
    path_dir = tfds.core.get_tfds_path(FIG_DIR)
    print(path_dir)
    fig = tfds.show_examples(ds_info, ds, plot_scale=2)
    suffix = '.png'
    fpath = os.path.join(path_dir, ds_name + suffix)
    fig.savefig(fname=fpath)

    # Optimizing figures
    optimize_image(ds_name)
    os.remove(fpath)

  except RuntimeError:
    print('The selected dataset is not supported')

def optimize_image(ds_name):
  """
  Optimizing image size by removing transparency
  """

  images_folder_path = tfds.core.get_tfds_path(FIG_DIR)
  image_file_name = ds_name + '.png'

  image_path = os.path.join(images_folder_path, image_file_name)
  print(image_path)
  image = Image.open(image_path)
  non_transparent_image = image.convert('RGB')

  optimized_image_file_name = ds_name + '.jpg'
  optimized_image_file_path = os.path.join(images_folder_path, optimized_image_file_name)
  non_transparent_image.save(optimized_image_file_path)

def main(_):
  generate_visualization('beans')

if __name__ == "__main__":
  app.run(main)

