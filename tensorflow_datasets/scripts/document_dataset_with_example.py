import os

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts import generate_visualization
from tensorflow_datasets.scripts import document_datasets

def generate_docs_with_visualization(ds_name):
    # DatasetBuilder
    builder = tfds.builder(ds_name)

    # Download the dataset
    builder.download_and_prepare()

    # Construct a tf.data.Dataset
    ds = builder.as_dataset(split='train')

    dst_dir = tfds.core.get_tfds_path('examples/')

    with open(os.path.join(dst_dir, f'{ds_name}.md'), "w") as f:

        doc_builder = document_datasets.document_single_builder(builder)
        f.write(doc_builder)

