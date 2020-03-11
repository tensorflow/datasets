import tensorflow_datasets as tfds
import os
import sys

# Returns metadata dir content
metadata_dir = os.walk(os.path.join(os.pardir,"testing/metadata"))
roots = [root for root,dir,file in metadata_dir]

# Import registered.py
reg_path = os.path.join(os.pardir, "core")
sys.path.insert(1, os.path.abspath(reg_path))
import registered

# Get list of all available versions of datasets
registered_versions = [i for i in registered.iter_dataset_full_names()]
print(registered_versions)
print(tfds.list_builders())
