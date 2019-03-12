# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Visual Dialog Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{visdial,
  title={{V}isual {D}ialog},
  author={Abhishek Das and Satwik Kottur and Khushi Gupta and Avi Singh
    and Deshraj Yadav and Jos\'e M.F. Moura and Devi Parikh and Dhruv Batra},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2017}
}
"""

_Train_Dialogs = "https://dl.dropboxusercontent.com/s/ix8keeudqrd8hn8/visdial_1.0_train.zip"
_Validation_Dialogs = "https://dl.dropboxusercontent.com/s/ibs3a0zhw74zisc/visdial_1.0_val.zip"
_Validation_Images = "https://dl.dropboxusercontent.com/s/twmtutniktom7tu/VisualDialog_val2018.zip"
_Test_Dialogs = "https://dl.dropboxusercontent.com/s/o7mucbre2zm7i5n/visdial_1.0_test.zip"
_Test_Images = "https://dl.dropboxusercontent.com/s/mwlrg31hx0430mt/VisualDialog_test2018.zip"


