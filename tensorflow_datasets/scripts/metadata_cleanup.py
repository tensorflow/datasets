# Lint as: python3
"""Removes all dataset versions from metadata directory which are not 
   present in registered versions of TFDS.

To test:
Goto tensorflow_datasets/scripts

Args : dry_run : If given, it traverse and finds all
                 versions which are to be removed without
                 actually removing them.
                 
             r : If given it removes all unmatched dataset versions 
                 from metadata directory.
```
cd tensorflow_datasets/scripts

For check not delete : python metadata_cleanup.py --dry_run
For delete not check : python metadata_cleaup.py --r
For both delete & check : python metadata_cleanup.py --dry_run --r
```
"""
from absl import flags
from absl import app
import os
import tensorflow as tf
from tensorflow_datasets.core import registered


FLAGS = flags.FLAGS
flags.DEFINE_boolean('dry_run', False, "Shows all versions\
                      which are not registered")
flags.DEFINE_boolean('r', False, "Removes unmatched\
                      dataset versions from metadata")

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
    '''Remove metadata versions not present in registered versions '''
    _registered_path = set(i for i in registered.iter_dataset_full_names())
    _meta_paths= _extract_metadata_versions(metadata_dir)
    for extra_full_name in sorted(_meta_paths-_registered_path):
        if FLAGS.dry_run:
            print(extra_full_name)
        if FLAGS.r:
            tf.io.gfile.rmtree(os.path.join(metadata_dir, extra_full_name))
    # delete directories which is completely empty after process.
    _remove_empty_folders(__metadata_path)
            

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

def main(unused_argv):
    """This method calls the _delete_metadata_dirs &
        _remove_empty_folders method to start the process
    """
    del unused_argv
    if FLAGS.dry_run:
        print("\n These are the versions to be removed"
              " from metadata directory: \n")
    # delete metadata versions not present in register version.
    _delete_metadata_dirs(__metadata_path) 


if __name__ == "__main__":  
    app.run(main)
