"""
Script for generating dataset example figures

Uses show_examples() to generate example figures of a dataset
and stores it temporary in examples/

Typical usage example:

  ds_name = 'beans'
  generate_visualization(ds_name)

"""

import tensorflow_datasets as tfds
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
    fig.savefig(path_dir + ds_name + '.png')
    print('Saved '+ ds_name + '.png' + 'to' + path_dir)
  except RuntimeError:
    print('The selected dataset is not supported')

