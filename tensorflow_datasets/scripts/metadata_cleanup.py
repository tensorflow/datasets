# Lint as: python3
"""Removes all dataset versions from metadata directory which are not
   present in registered versions of TFDS.

To test:
Goto tensorflow_datasets/scripts

Args:
    dry_run: If given, it traverse and finds all
         versions which are to be removed without
         actually removing them. If not given
         removes from metadata dir.
```
cd tensorflow_datasets/scripts

For check not Remove: python metadata_cleanup.py --dry_run
For Remove: python metadata_cleanup.py.
```
"""
import os
from absl import flags
from absl import app
import tensorflow as tf
from tensorflow_datasets.core import registered

FLAGS = flags.FLAGS
flags.DEFINE_boolean(
    'dry_run', False, "Shows all versions\
                      which are not registered")

metadata_path = os.path.join(os.pardir, "testing/metadata")


def _extract_metadata_versions(metadata_dir):
  """Get all metadata direcotry versions paths.
  
  It only extract the paths like 'dataset_name/version'
  or 'dataset_name/config/versions' in metadata dir.

  Args:
      metadata_dir: Path to metadat directory (testing/metadata).

  Returns:
      Set of correctly formated metadata paths.
  """
  meta_paths = set()
  for root, dirs, files in tf.io.gfile.walk(metadata_dir): # pylint: disable=unused-variable
    path_string = root[len(metadata_dir) + 1:]
    if registered.is_full_name(path_string[:]):
      meta_paths.add(path_string)
  return meta_paths


def _delete_metadata_dirs(metadata_dir):
  """Remove metadata versions not present in registered versions
     if --dry_run was not given else traverse and show dir to remove.

  Args:
      metadata_dir: Path to metadat directory (testing/metadata).
  """
  registered_path = set(registered.iter_dataset_full_names())
  meta_paths = _extract_metadata_versions(metadata_dir)
  for extra_full_name in sorted(meta_paths - registered_path):
    if FLAGS.dry_run:
      print(extra_full_name)
    else:
      tf.io.gfile.rmtree(os.path.join(metadata_dir, extra_full_name))


def main(unused_argv):
  """Main script."""
  del unused_argv
  if FLAGS.dry_run:
    print("\n These are the versions to be removed"
          " from metadata directory: \n")
  # Delete metadata versions not present in register version.
  _delete_metadata_dirs(metadata_path)


if __name__ == "__main__":
  app.run(main)
