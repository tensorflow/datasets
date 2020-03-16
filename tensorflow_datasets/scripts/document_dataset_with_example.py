"""
Script used to generate documentation .md files with example figures

This script uses scripts/generate_visualization.py to generate
an example figure of a dataset, using show_examples() it gets a figure
that is temporary stores in examples/ and later used when generating
the documentation with document_single_builder(builder)

Typical usage example:

  ds_name = 'beans'
  generate_docs_with_visualization(ds_name)

"""

import os
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts import document_datasets

def generate_docs_with_visualization(ds_name):
  """
  Generates example figures of a dataset
  """
  # DatasetBuilder
  builder = tfds.builder(ds_name)

  # Download the dataset
  builder.download_and_prepare()

  # Construct a tf.data.Dataset
  #ds = builder.as_dataset(split='train')

  dst_dir = tfds.core.get_tfds_path('examples/')

  with open(os.path.join(dst_dir, f'{ds_name}.md'), "w") as f:
    doc_builder = document_datasets.document_single_builder(builder)
    f.write(doc_builder)

