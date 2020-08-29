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

r"""Script to detect all the versions of the various datasets and delete the old/non-existing ones

User is first given previews of all the versions of the datasets with the latest ones in bold

Instructions:

python -m tensorflow_datasets.scripts.delete_old_versions \
  --data_dir=/path/to/data_dir/

"""

import os
from absl import flags
from absl import app

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

from tensorflow_datasets.core import constants
from tensorflow_datasets.core.load import list_full_names

FLAGS = flags.FLAGS
flags.DEFINE_string("data_dir",constants.DATA_DIR,"Path to the data directory")

def get_redundant_datasets(data_dir):
  installed_datasets = []
  all_datasets = tfds.list_builders()
  exclude = {"downloads","download","manual","extracted"}

  #Get all the non-existing datasets
  rogue_datasets = [dataset for dataset in tf.io.gfile.listdir(data_dir) if dataset not in all_datasets]
  rogue_datasets.remove("downloads")

  #Finding all installed datasets
  for root,dirs,files in os.walk(data_dir, topdown=True):
    #Excluding the downloads directory and the rogue datasets
    dirs[:] = [d for d in dirs if d not in exclude]
    dirs[:] = [d for d in dirs if d not in rogue_datasets]
    if dirs==[]:
      installed_datasets.append(root.split("tensorflow_datasets\\")[-1].replace("\\","/"))
  return installed_datasets, rogue_datasets

def main(_):
  #Get the latest dataset versions and configs alog with the locally installed datasets
  latest_datasets = list_full_names(current_version_only=True)
  installed_datasets, rogue_datasets = get_redundant_datasets(FLAGS.data_dir)
  old_datasets = []

  #Identify the old dataset version/configs
  for dataset in installed_datasets:
    if dataset not in latest_datasets:
      old_datasets.append(dataset)

  #User preview
  print("The script will delete the following modifications to `{}`:\nPath indicated in bold will be kept, the other will be deleted.\n".format(FLAGS.data_dir))
  for index,dataset in enumerate(installed_datasets):
    if dataset in old_datasets:
      print("{}\n".format(dataset))
    else:
      print(f"\033[1m{dataset}\033[0m")

  #Previewing the rogue datasets to user
  print("\nThe script will also delete the following non-existing datasets: \n")
  for dataset in rogue_datasets:
    print("{}".format(dataset))
  choice = str(input("\nDo you want to continue (Y/n): "))

  #Deleting the datasets on user's choice
  if choice=='Y' or choice=='y' or choice=="":
    for dataset in old_datasets:
      path = os.path.join(FLAGS.data_dir,dataset)
      tf.io.gfile.rmtree(path)
    print("All old/non-existing dataset version and configs successfully deleted")
    for dataset in rogue_datasets:
      path = os.path.join(FLAGS.data_dir,dataset)
      tf.io.gfile.rmtree(path)
    print("All non-existant datasets removed")

if __name__ == "__main__":
  app.run(main)
