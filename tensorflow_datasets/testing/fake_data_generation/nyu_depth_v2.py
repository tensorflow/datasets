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

"""Generation script."""

import os

import h5py
import numpy as np

ref = h5py.File(
    os.path.expanduser(
        "~/tensorflow_datasets/downloads/extracted/TAR_GZ.datasets.lids.mit.edu_fastdept_nyudepthBjtXYu6zBBYUv0ByLqXPgFy4ygUuVvPRxjz9Ip5_97M.tar.gz/nyudepthv2/val/official/00001.h5"
    ),
    "r",
)

rgb = ref["rgb"][:]
depth = ref["depth"][:]
rgb_fake = np.ones(rgb.shape, dtype=np.uint8)  # np.zeros for val
depth_fake = np.ones(depth.shape).astype(depth.dtype)  # np.zeros for val

# 00001 and 00002 for train; 00001 for val
with h5py.File("00001.h5", "w") as f:
  f.create_dataset("rgb", data=rgb_fake, compression="gzip")
  f.create_dataset("depth", data=depth_fake, compression="gzip")
