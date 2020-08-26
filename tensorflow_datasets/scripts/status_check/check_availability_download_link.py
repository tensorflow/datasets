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

r"""Check availability of download links.

"""

import os

from absl import app
from absl import flags
import numpy as np
import pandas as pd
import requests
import tensorflow.compat.v2 as tf
from tensorflow_datasets.core.utils import py_utils

# In TF 2.0, eager execution is enabled by default
tf.compat.v1.disable_eager_execution()

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

status_code_list = []
url_list = []
df_result = pd.DataFrame()


def data_dir():
  return os.path.join(FLAGS.tfds_dir, "scripts", "status_check", "data")


def get_url_file_path():
  return os.path.join(FLAGS.tfds_dir, "url_checksums")


def get_status_code_file_path():
  return os.path.join(data_dir(), "status_code.csv")


def main(_):
  print("In main")
  for root, _, file_name in tf.io.gfile.walk(get_url_file_path()):
    for fname in file_name:
      full_path = os.path.join(root, fname)
      print(full_path)
      with tf.io.gfile.GFile(full_path) as f:
        df = pd.read_csv(f, delimiter=" ")
        url = df.columns.values[0]
        url_list.append(url)
        try:
          response = requests.get(url, timeout=100)
          status = response.status_code
          status_code_list.append(status)
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):
          status_code_list.append("Exception")
        print(status)

  df_result["urls"] = np.array(url_list)
  df_result["status"] = np.array(status_code_list)
  df_result.to_csv(get_status_code_file_path(), index_label="Index")


if __name__ == "__main__":
  app.run(main)
