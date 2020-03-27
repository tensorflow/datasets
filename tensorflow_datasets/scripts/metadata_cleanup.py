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
"""

from absl import app
import os
import re
import shutil
import tensorflow as tf
from tensorflow_datasets.core import registered

metadata_path = os.path.join(os.pardir, "testing/metadata")

def _extract_full_names_from_dirs(metadata_dir):
    '''Get all metadata direcotry versions paths '''
    meta_paths = set()
    for root, dirs, files in os.walk(metadata_dir):
        for fileName in files:
            meta_paths.add(os.path.join( root[len(metadata_dir):]))
    meta_paths.remove('')
    return list(meta_paths)

def get_registered_version():
    ''' Get total registered paths'''
    registered_path = []
    for i in registered.iter_dataset_full_names():
        registered_path.append(os.path.join("\\",i))
    return registered_path


def delete_metadata_dirs(metadata_dir):
    '''Remove metadata directories not present in registered versions '''
    number_of_meta_removed = 0
    registered_paths = get_registered_version()
    meta_paths= _extract_full_names_from_dirs(metadata_dir)
    for i in range(0, len(meta_paths)):
        
        if meta_paths[i] not in registered_paths:
            number_of_meta_removed+=1
            tf.io.gfile.rmtree(os.path.join(metadata_dir, meta_paths[i][1:]))

    return number_of_meta_removed, len(registered_paths), len(meta_paths)


def removeEmptyFolders(path, removeRoot=True):
    '''This function checks & remove if there is any directory
       which completely empty after process of removing.
    '''
    if not os.path.isdir(path):
        return
    subpath_or_path_removed = 0
    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                subpath_or_path_removed+=1
                removeEmptyFolders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        print( "Removing empty folder:", path)
        os.rmdir(path)

def main(_):
    
    number_of_meta_removed, registered_paths, meta_paths = delete_metadata_dirs(metadata_path)
    subpath_or_path_removed = removeEmptyFolders(metadata_path)
    print("*"*80)
    print("Total number of registered versions : ", registered_paths)
    print("Total number of metadata versions : ", meta_paths)
    print("Total number of meta directories removed : ", number_of_meta_removed)
    print("*"*80)


if __name__ == "__main__":
  app.run(main)
