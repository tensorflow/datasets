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
import matplotlib.pyplot

FIG_DIR = ('examples/')

def generate_visualization(ds_name):
  """
  Method used to generate examples figures of a dataset
  """

  try:
    ds, ds_info = tfds.load(name=ds_name, split='train', with_info=True)
    path_dir = tfds.core.get_tfds_path(FIG_DIR)
    print(path_dir)
    fig = tfds.show_examples(ds_info, ds, plot_scale=2)
    fname = path_dir + ds_name + '.png'
    fig.savefig(fname=fname)

    # Optimizing figures
    optimize_image(ds_name)
    os.remove(fname)

  except RuntimeError:
    print('The selected dataset is not supported')

def optimize_image(ds_name):
  """
  Optimizing image size by removing transparency
  """

  figure_path = tfds.core.get_tfds_path(FIG_DIR)
  file_path = figure_path+ ds_name +".png"
  print(file_path)
  image = Image.open(file_path)
  non_transparent_image = image.convert('RGB')
  non_transparent_image.save(figure_path+'beans.jpg')
