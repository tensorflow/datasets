# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Generate fake data for SVHN.

"""

import numpy as np
import scipy.io

for split_name, num_examples in [
    ('train', 3),
    ('test', 2),
    ('extra', 1),
]:
  img_shape = (32, 32, 3, num_examples)
  scipy.io.savemat('{}_32x32.mat'.format(split_name), {
      'X': np.random.randint(255, size=img_shape, dtype=np.uint8),
      'y': np.random.randint(1, 10, size=(num_examples, 1)),
  })
