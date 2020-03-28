# Lint as: python3
"""Script to Cleanup Metadata directory.

To test:
Goto tensorflow_datasets/scripts and run python metadata_cleanup.py

```
cd tensorflow_datasets/scripts
python metadata_cleanup.py
```
It delete all metadata directory versions 
which are not present in registered versions of 
datasets. Also it further check in last if there
is any empty folder remaining after remove all useless
versions from meatdata directory
"""

from absl import app
import os
import re
import shutil
import tensorflow as tf
from tensorflow_datasets.core import registered


__metadata_path = os.path.join(os.pardir, "testing/metadata")

def _extract_metadata_versions(metadata_dir):
    '''
       Get all metadata direcotry versions paths,
       It only extract the paths like 'dataset_name/version'
       or 'dataset_name/config/versions' in metadata dir
    '''
    _meta_paths = set()
    for root, dirs, files in os.walk(metadata_dir):
        for fileName in files:
            _meta_paths.add(os.path.join(root[len(metadata_dir)+1:]))
    _meta_paths.remove('')
    return _meta_paths

def _delete_metadata_dirs(metadata_dir):
    '''Remove metadata directories not present in registered versions '''
    _registered_path = set(i for i in registered.iter_dataset_full_names())
    _meta_paths= _extract_metadata_versions(metadata_dir)
    for extra_full_name in sorted(_meta_paths-_registered_path):
        tf.io.gfile.rmtree(os.path.join(metadata_dir, extra_full_name))


def _remove_empty_folders(path, removeRoot=True):
    '''
       This function checks & remove recursively,
       if there is any directory which completely
       empty after delete all useless metadata versions.
    '''
    if not os.path.isdir(path):
        return
    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                _remove_empty_folders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        os.rmdir(path)

def main(_):
    # delete metadata versions not present in register version.
    _delete_metadata_dirs(__metadata_path) 
    # delete directories which is completely empty after process.
    _remove_empty_folders(__metadata_path)


if __name__ == "__main__":
  app.run(main)
  
