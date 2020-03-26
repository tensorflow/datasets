# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Lint as: python3

"""Script to Cleanup Metadata directory.

To test:
Goto tensorflow_datasets/scripts and run using python metadata_cleanup.py

```
cd tensorflow_datasets/scripts
python metadata_cleanup.py
```
It returns :

Total number of registered datasets
Total number of subdirectories in metadata direcotry
Total number of meta directories removed 
Total number of empty metadata directory after removing
"""
from absl import app
import os
import re
import shutil
from tensorflow_datasets.core import registered

metadata_path = os.path.join(os.pardir, "testing/metadata")

def get_registered_versions():
    ''' Return list of all registered versions of datasets'''
    registered_versions = sorted([i for i in registered.iter_dataset_full_names()])
    return registered_versions


def get_meta_dir_paths():
    ''' Return list of all paths in metadata directory''' 

    meta_dirs = []
    meta_files = []

    for root, dirs, files in os.walk(metadata_path):
        meta_dirs.append(root)
        meta_files.append(dirs)

    metadata_names = meta_files.pop(0)

    return meta_dirs, metadata_names

def get_meta_dir_subpaths():
    '''Retruns list of all subpaths in metadata directory

       Get only meta paths which have some version string in its path string.
       Ex : meta_dirs have paths like -> ['..\\testing/metadata\\abstract_reasoning']
       ['..\\testing/metadata\\abstract_reasoning\\attr.rel.pairs\\0.0.2']
       so get path only have versions like 0.0.2.
    '''
    subpaths = []

    meta_dirs, metadata_names = get_meta_dir_paths() # get all meta paths and names

    for meta_dir in meta_dirs:
        match = re.search(r'\d\.\d\.\d', meta_dir) # Match paths

        try:
            meta_dir == match.group() # add subpaths only if meta_dir matches
            subpaths.append(os.path.relpath(meta_dir, '..\\testing/metadata'))
        except:
            continue # continue in some cases which not have version string in last 

    return subpaths


def remove_meta_paths():
    ''' Remove all metadata directories not includes in registered version list.'''

    subpaths = get_meta_dir_subpaths()
    registered_versions = get_registered_versions()

    number_of_meta_removed = 0

    for i in range(0,len(subpaths)):
        if subpaths[i] not in registered_versions:
            number_of_meta_removed+=1

            # Remove directories from metadata which not in registered version list
            shutil.rmtree(os.path.join(metadata_path,subpaths[i]),ignore_errors =True)

            empty_folder_paths = os.path.join(metadata_path,subpaths[i][:-6])

            # Check if subpath directories are empty after above delete
            if len(os.listdir(empty_folder_paths)) == 0:
                shutil.rmtree(empty_folder_paths, ignore_errors =True) # Remove empty subpath directories

    return len(registered_versions), len(subpaths), number_of_meta_removed


def delete_empty_directory():
    ''' Removes all metadata directories which are completely empty after above process'''

    empty_meta_folders = 0
    meta_dirs, metadata_names = get_meta_dir_paths()

    for i in range(0, len(metadata_names)):

        try:
            empty_folder_paths = os.path.join(metadata_path,metadata_names[i])

            if len(os.listdir(empty_folder_paths)) == 0: # Check is empty..
                empty_meta_folders+=1
                shutil.rmtree(empty_folder_paths, ignore_errors =True) 
        except:
            continue

    return empty_meta_folders

def main(_):
    
    registered_versions, subpaths, number_of_meta_removed = remove_meta_paths()
    empty_meta_folders = delete_empty_directory()
    print("*"*80)
    print("Total number of registered datasets : ", registered_versions)
    print("Total number of subdirectories in metadata direcotry : ", subpaths)
    print("Total number of meta directories removed : ", number_of_meta_removed)
    print("Total number of directories in metadata, empty after process : ", empty_meta_folders) 
    print("*"*80)


if __name__ == "__main__":
  app.run(main)
