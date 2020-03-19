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
from absl import app
from tensorflow_datasets.scripts import document_datasets

FIG_DIR = ('../docs/catalog/')

def generate_docs_with_visualization(ds_name):
  """
  Prepare builder and generate example figures to /examples folder
  """
  builder = tfds.builder(ds_name)
  builder.download_and_prepare()
  dst_dir = tfds.core.get_tfds_path(FIG_DIR)

  with open(os.path.join(dst_dir, f'{ds_name}.md'), "w") as f:
    doc_builder = document_datasets.document_single_builder(builder)
    f.write(doc_builder)

def main(_):
  generate_docs_with_visualization('beans')

if __name__ == "__main__":
  app.run(main)
