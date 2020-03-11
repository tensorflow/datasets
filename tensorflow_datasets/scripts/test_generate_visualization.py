import os
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts import generate_visualization
from tensorflow_datasets.scripts import document_datasets
from tensorflow_datasets.scripts import document_dataset_with_example

DATASET_TO_TESTS = ['beans']  # Datasets you want to test the script on.

def main():
    for ds_name in DATASET_TO_TESTS:
        # load dataset
        tfds.load(ds_name)

        # Generate figure for the dataset
        generate_visualization.generate_visualization(ds_name)

        # Generate documentation which example
        document_dataset_with_example.generate_docs_with_visualization(ds_name)

main()