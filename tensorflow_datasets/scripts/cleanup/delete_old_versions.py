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

r"""Script to detect all the versions of the various datasets
    and delete the old/non-existing ones

User is first given previews of all the versions of the datasets
    with the latest ones in bold

Instructions:

python -m tensorflow_datasets.scripts.delete_old_versions
    --data_dir=/path/to/data_dir/ --skip_confirmation=False

"""

import os
from absl import flags
from absl import app
from termcolor import colored

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import constants

FLAGS = flags.FLAGS
flags.DEFINE_string("data_dir",
  constants.DATA_DIR,
  "Path to the data directory")
flags.DEFINE_boolean("skip_confirmation",
  False,
  "Whether to skip user confirmation or not")

def get_datasets(data_dir, current_full_names):
  """
  Returns a tuple of installed datasets and rogue datasets

  Arguments:
      data_dir : The path to the data directory
      current_full_names : Names of the latest datasets supported in TFDS

  Returns:
      dirs_to_keep, dirs_to_del : \
                        Tuple of datasets to keep and delete respectively
  """
  #Making the paths in windows supported format
  current_full_names = [os.path.normpath(name) for name in current_full_names]
  all_datasets = {
    name.split(os.path.sep)[0]
    for name in current_full_names
    }

  installed_datasets = []
  exclude = {"downloads", "download", "manual", "extracted"}

  #Get all the non-existing datasets
  rogue_datasets = []
  for dataset in tf.io.gfile.listdir(data_dir):
    if dataset not in all_datasets:
      rogue_datasets.append(dataset)

  #Removing other folders
  for dataset in exclude:
    if dataset in rogue_datasets:
      rogue_datasets.remove(dataset)

  #Finding all installed datasets
  for root,dirs,_ in tf.io.gfile.walk(data_dir, topdown=True):
    #Excluding the downloads directory and the rogue datasets
    dirs[:] = [dataset for dataset in dirs if dataset not in exclude]
    dirs[:] = [dataset for dataset in dirs if dataset not in rogue_datasets]
    if dirs==[]:
      installed_datasets.append(
        os.path.normpath(os.path.relpath(root, data_dir)))

  #Determining which datasets to keep and delete
  dirs_to_keep = []
  dirs_to_delete = []
  for dataset in installed_datasets:
    if dataset not in current_full_names:
      dirs_to_delete.append(dataset)
    else:
      dirs_to_keep.append(dataset)

  dirs_to_delete = dirs_to_delete + rogue_datasets
  return dirs_to_keep, dirs_to_delete

def delete_old_versions(data_dir, skip_confirmation=False):
  """
  Detects and deletes the old/non-existing versions of the datasets
  """
  #Get the datasets to keep and to delete
  dirs_to_keep, dirs_to_delete = get_datasets(
    data_dir,
    current_full_names=tfds.core.load.list_full_names(
      current_version_only=True
      )
    )
  all_dirs = [
    colored(d, attrs=["bold"]) if d in dirs_to_keep else d
    for d in sorted(dirs_to_keep + dirs_to_delete)]

  #User preview
  print(f"The script will delete the following modifications to `{data_dir}`:")
  print("Path indicated in bold will be kept, the other will be deleted.\n")
  print("\n".join(all_dirs))

  if skip_confirmation:
    choice = ""
  else:
    choice = str(input("\nDo you want to continue (Y/n): "))
  #Deleting the datasets on user's choice
  if choice in ("Y", "y" , ""):
    for dataset in dirs_to_delete:
      path = os.path.join(data_dir, dataset)
      tf.io.gfile.rmtree(path)
    print("All old/non-existing dataset version and",
      "configs successfully deleted")

def main(_):
  delete_old_versions(FLAGS.data_dir, FLAGS.skip_confirmation)

if __name__ == "__main__":
  app.run(main)
